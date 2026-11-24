"""schema.org and DCAT descriptions of the catalogue's datasets.

Both are built from the frontmatter made by mappers.make_dataset_frontmatter:

- make_schema_org: JSON-LD embedded in each dataset page, which is what Google
  Dataset Search indexes.
- make_dcat_catalog: the whole catalogue as one DCAT JSON-LD document, for
  harvesting by other data catalogues.
"""

from urllib.parse import quote

import config

SITE_URL = config.site_url
CATALOG_ID = f"{SITE_URL}/"
PUBLISHER = {"name": "GFDRR", "url": "https://www.gfdrr.org/"}

# Google ignores descriptions longer than 5000 characters.
SCHEMA_ORG_DESCRIPTION_MAX = 5000
# Keeps the page (and database) small for datasets with hundreds of files. The
# DCAT document lists them all.
SCHEMA_ORG_MAX_DISTRIBUTIONS = 20

DCAT_CONTEXT = {
    "dcat": "http://www.w3.org/ns/dcat#",
    "dct": "http://purl.org/dc/terms/",
    "foaf": "http://xmlns.com/foaf/0.1/",
    "geosparql": "http://www.opengis.net/ont/geosparql#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "vcard": "http://www.w3.org/2006/vcard/ns#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
}


def _compact(value):
    """Drop the keys that have no value."""
    return {k: v for k, v in value.items() if v not in (None, "", [], {})}


def dataset_url(slug):
    return f"{SITE_URL}/datasets/{slug}/"


def clean_url(value):
    """An absolute http(s) URL without characters illegal in an IRI, or None."""
    if not isinstance(value, str):
        return None
    value = value.strip()
    if value.lower().startswith("www."):
        value = f"https://{value}"
    if not value.lower().startswith(("http://", "https://")):
        return None
    return quote(value, safe=":/?#[]@!$&'()*+,;=%~")


def _humanize(value):
    return str(value).replace("_", " ")


def _unique(values):
    return list(dict.fromkeys(v for v in values if v))


def _keywords(fm):
    hazard = fm.get("hazard") or {}
    return _unique(
        [
            *map(_humanize, fm.get("risk_data_type") or []),
            *(_humanize(t) for t in hazard.get("type") or [] if t),
            *(
                _humanize(e["category"])
                for e in fm.get("exposure") or []
                if e and e.get("category")
            ),
            *(c["title"] for c in _countries(fm)),
        ]
    )


def _countries(fm):
    return [c for c in (fm.get("spatial") or {}).get("countries") or [] if c]


def _bbox(fm):
    """(min_lon, min_lat, max_lon, max_lat), or None."""
    # The mapper keeps only bboxes in degrees.
    bbox = (fm.get("spatial") or {}).get("bbox")
    return tuple(bbox) if bbox else None


def _links(fm, rel):
    return _unique(
        clean_url(link.get("href"))
        for link in fm.get("links") or []
        if link.get("rel") == rel
    )


def _temporal_coverage(temporal):
    """ISO 8601 interval, with ".." for an open end."""
    if not temporal:
        return None
    start, end = temporal.get("start"), temporal.get("end")
    if not start and not end:
        return str(temporal["central_year"]) if temporal.get("central_year") else None
    if start == end:
        return str(start)
    return f"{start or '..'}/{end or '..'}"


# schema.org


def _schema_org_entity(entity):
    if not entity or not entity.get("name"):
        return None
    return _compact(
        {
            "@type": "Organization",
            "name": entity["name"],
            "url": clean_url(entity.get("url")),
        }
    )


def _schema_org_spatial(fm):
    places = [{"@type": "Place", "name": c["title"]} for c in _countries(fm)]
    bbox = _bbox(fm)
    if bbox:
        min_lon, min_lat, max_lon, max_lat = bbox
        places.append(
            {
                "@type": "Place",
                "geo": {
                    "@type": "GeoShape",
                    # schema.org boxes are "south west north east"
                    "box": f"{min_lat} {min_lon} {max_lat} {max_lon}",
                },
            }
        )
    return places


def _schema_org_distribution(resource):
    content_url = clean_url(resource.get("download_url"))
    access_url = clean_url(resource.get("access_url"))
    if not content_url and not access_url:
        return None
    return _compact(
        {
            "@type": "DataDownload",
            "name": resource.get("title"),
            "encodingFormat": resource.get("media_type")
            or resource.get("format_label"),
            "contentUrl": content_url or access_url,
        }
    )


def _citation(related_resource):
    doi = related_resource.get("doi")
    if doi:
        return clean_url(doi) or f"https://doi.org/{doi}"
    return clean_url(related_resource.get("url")) or related_resource.get("name")


def make_schema_org(fm):
    description = fm["description"]
    if len(description) > SCHEMA_ORG_DESCRIPTION_MAX:
        description = description[: SCHEMA_ORG_DESCRIPTION_MAX - 1].rstrip() + "…"
    url = dataset_url(fm["slug"])
    distributions = [
        d for d in map(_schema_org_distribution, fm.get("resources") or []) if d
    ]
    return _compact(
        {
            "@context": "https://schema.org/",
            "@type": "Dataset",
            "@id": url,
            "name": fm["title"],
            "description": description,
            "url": url,
            "identifier": [fm["dataset_id"], *_links(fm, "cite-as")],
            "sameAs": _links(fm, "source"),
            "version": fm.get("version"),
            "license": clean_url((fm.get("license") or {}).get("url")),
            "creator": _schema_org_entity(fm.get("creator")),
            "publisher": _schema_org_entity(fm.get("publisher")),
            "keywords": _keywords(fm),
            "spatialCoverage": _schema_org_spatial(fm),
            "temporalCoverage": _temporal_coverage(fm.get("temporal")),
            "citation": _unique(map(_citation, fm.get("referenced_by") or [])),
            "includedInDataCatalog": {
                "@type": "DataCatalog",
                "name": config.site_title,
                "url": CATALOG_ID,
            },
            "distribution": distributions[:SCHEMA_ORG_MAX_DISTRIBUTIONS],
        }
    )


# DCAT


def _ref(url):
    url = clean_url(url)
    return {"@id": url} if url else None


def _dcat_agent(entity):
    if not entity or not entity.get("name"):
        return None
    return _compact(
        {
            "@type": "foaf:Agent",
            "foaf:name": entity["name"],
            "foaf:homepage": _ref(entity.get("url")),
        }
    )


def _dcat_contact_point(entity):
    if not entity or not entity.get("name"):
        return None
    email = (entity.get("email") or "").strip()
    return _compact(
        {
            "@type": "vcard:Kind",
            "vcard:fn": entity["name"],
            "vcard:hasEmail": {"@id": f"mailto:{email}"} if email else None,
            "vcard:hasURL": _ref(entity.get("url")),
        }
    )


def _dcat_date(value):
    """Typed literal for a year, year-month or full date."""
    text = str(value)
    datatype = {4: "xsd:gYear", 7: "xsd:gYearMonth", 10: "xsd:date"}.get(len(text))
    return {"@value": text, "@type": datatype} if datatype else text


def _dcat_temporal(temporal):
    if not temporal:
        return None
    period = _compact(
        {
            "dcat:startDate": temporal.get("start") and _dcat_date(temporal["start"]),
            "dcat:endDate": temporal.get("end") and _dcat_date(temporal["end"]),
        }
    )
    return {"@type": "dct:PeriodOfTime", **period} if period else None


def _dcat_spatial(fm):
    places = [
        {"@type": "dct:Location", "rdfs:label": c["title"]} for c in _countries(fm)
    ]
    bbox = _bbox(fm)
    if bbox:
        min_lon, min_lat, max_lon, max_lat = bbox
        ring = [
            (min_lon, min_lat),
            (max_lon, min_lat),
            (max_lon, max_lat),
            (min_lon, max_lat),
            (min_lon, min_lat),
        ]
        wkt = "POLYGON((" + ", ".join(f"{x} {y}" for x, y in ring) + "))"
        places.append(
            {
                "@type": "dct:Location",
                "dcat:bbox": {"@value": wkt, "@type": "geosparql:wktLiteral"},
            }
        )
    return places


def _dcat_distribution(resource):
    access_url = _ref(resource.get("access_url")) or _ref(resource.get("download_url"))
    if not access_url:
        return None
    return _compact(
        {
            "@type": "dcat:Distribution",
            "dct:title": resource.get("title"),
            "dct:format": resource.get("format_label"),
            "dcat:mediaType": resource.get("media_type"),
            "dcat:accessURL": access_url,
            "dcat:downloadURL": _ref(resource.get("download_url")),
        }
    )


def make_dcat_dataset(fm):
    url = dataset_url(fm["slug"])
    license = fm.get("license") or {}
    return _compact(
        {
            "@id": url,
            "@type": "dcat:Dataset",
            "dct:identifier": fm["dataset_id"],
            "dct:title": fm["title"],
            "dct:description": fm["description"],
            "dcat:landingPage": {"@id": url},
            "dcat:version": fm.get("version"),
            "dct:license": _ref(license.get("url")) or license.get("title"),
            "dct:creator": _dcat_agent(fm.get("creator")),
            "dct:publisher": _dcat_agent(fm.get("publisher")),
            "dcat:contactPoint": _dcat_contact_point(fm.get("contact_point")),
            "dcat:keyword": _keywords(fm),
            "dct:spatial": _dcat_spatial(fm),
            "dct:temporal": _dcat_temporal(fm.get("temporal")),
            "dct:source": [{"@id": u} for u in _links(fm, "source")],
            "dct:conformsTo": [{"@id": u} for u in _links(fm, "describedby")],
            "dcat:distribution": [
                d for d in map(_dcat_distribution, fm.get("resources") or []) if d
            ],
        }
    )


def make_dcat_catalog(frontmatters):
    return {
        "@context": DCAT_CONTEXT,
        "@id": CATALOG_ID,
        "@type": "dcat:Catalog",
        "dct:title": config.site_title,
        "dct:description": config.site_description,
        "foaf:homepage": {"@id": CATALOG_ID},
        "dct:publisher": _dcat_agent(PUBLISHER),
        "dcat:dataset": [make_dcat_dataset(fm) for fm in frontmatters],
    }
