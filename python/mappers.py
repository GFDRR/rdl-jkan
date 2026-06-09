'''
Differences between RDLS and output frontmatter:
    - links are replaced by catalog, derived from links and resources 
'''
import config


def make_dataset_frontmatter(dataset):
    """Formats RDL v1.0 metadata into JKAN frontmatter for a dataset"""

    return {
        "schema": "rdls-1.0",
        # try first; required by write_yaml
        "title": dataset["title"],
        # required; throw if missing
        "contact_point": make_entity(dataset["contact_point"]),
        "creator": make_entity(dataset["creator"]),
        "dataset_id": dataset["id"],
        "description": dataset["description"],
        "license": dataset["license"],
        "publisher": make_entity(dataset["publisher"]),
        "resources": [make_resource(resource) for resource in dataset["resources"]],
        "risk_data_type": dataset["risk_data_type"],
        "slug": dataset["id"],
        "spatial": make_spatial(dataset["spatial"]),
        # optional
        "attributions": [
            make_attribution(attribution)
            for attribution in dataset.get("attributions", [])
        ],
        "catalog": make_catalog(dataset),
        "details": dataset.get("details"),
        "exposure": [
            make_exposure(exposure) for exposure in dataset.get("exposure", [])
        ],
        "hazard": make_hazard(dataset.get("hazard")),
        "lineage": make_lineage(dataset["lineage"]) if "lineage" in dataset else None,
        "loss": make_loss(dataset.get("loss")),
        "project": make_project(dataset["project"]) if "project" in dataset else None,
        "purpose": dataset.get("purpose"),
        "referenced_by": [
            make_related_resource(related_resource)
            for related_resource in dataset.get("referenced_by", [])
        ],
        "spatial_resolution": dataset.get("spatial_resolution"),
        "temporal": make_temporal(dataset["temporal"]) if "temporal" in dataset else None,
        "temporal_resolution": dataset.get("temporal_resolution"),
        "version": dataset.get("version"),
        "vulnerability": make_vulnerability(dataset.get("vulnerability")),
    }


def make_affiliation(affiliation):
    return {
        # required; throw if missing
        "name": affiliation["name"],
        # optional
        "url": affiliation.get("url"),
    }



def make_attribution(attribution):
    return {
        # required; throw if missing
        "id": attribution["id"],
        "entity": make_entity(attribution["entity"]),
        "role": attribution["role"],
    }


def make_catalog(dataset):
    link_hrefs = [link.get("href") for link in dataset.get("links", [])]
    access_urls = [
        resource.get("access_url") for resource in dataset.get("resources", [])
    ]

    for url in link_hrefs + access_urls:
        for prefix, label in config.dataset_catalogs.items():
            if url is not None and prefix in url:
                return label
    return None

def make_climate(climate):
    return {
        # optional
        "model": climate.get("model"),
        "scenario": climate.get("scenario"),
        "percentile": climate.get("percentile"),
    }

def make_entity(attribution):
    return {
        # required; throw if missing
        "name": attribution["name"],
        # optional
        "email": attribution.get("email"),
        "url": attribution.get("url"),
        "affiliation": make_affiliation(attribution["affiliation"]) if "affiliation" in attribution else None,
    }


def make_exposure(exposure_array):
    """Convert RDL exposure metadata into JKAN frontmatter"""
    if exposure_array is None:
        return None

    props_to_summarize = {
        "category": [],  # found on exposure
        "taxonomy": [],  # found on exposure
        "dimension": [],  # found on metric
        "quantity_kind": [],  # found on metric
    }
    for exposure in exposure_array:
        # required; throw if missing
        props_to_summarize["category"].append(exposure["category"])
        if "taxonomy" in exposure:
            props_to_summarize["taxonomy"].append(exposure["taxonomy"])
        if "metrics" in exposure:
            for metric in exposure["metrics"]:
                if metric["dimension"]:
                    props_to_summarize["dimension"].append(metric["dimension"])
                if metric["quantity_kind"]:
                    props_to_summarize["quantity_kind"].append(metric["quantity_kind"])

    return {
        # required; throw if missing
        "category": ", ".join(sorted(set(props_to_summarize["category"]))),
        # optional
        "taxonomy": (
            ", ".join(sorted(set(props_to_summarize["taxonomy"])))
            if len(props_to_summarize["taxonomy"]) > 0
            else None
        ),
        "dimension": (
            ", ".join(sorted(set(props_to_summarize["dimension"])))
            if len(props_to_summarize["dimension"]) > 0
            else None
        ),
        "quantity_kind": (
            ", ".join(sorted(set(props_to_summarize["quantity_kind"])))
            if len(props_to_summarize["quantity_kind"]) > 0
            else None
        ),
    }
def make_gazetteer_entry(gazetteer_entry):
    return {
        # required; throw if missing
        "id": gazetteer_entry["id"],
        # optional
        "scheme": gazetteer_entry.get("scheme"),
        "description": gazetteer_entry.get("description"),
        "uri": gazetteer_entry.get("uri"),
    }

def make_hazard(hazard):
    """Convert RDL hazard metadata into JKAN frontmatter"""
    if hazard is None:
        return None

    props_to_summarize = {
        "calculation_method": [],  # found on event, event_set
        "disaster_identifiers": [],  # found on event
        "hazard_analysis_type": [],  # found on event_set as analysis_type
        "hazard_type": [],  # found on event_set as type
        "intensity": [],  # found on hazard, event.hazard as intensity_measure
        "occurrence_range": [],  # found on event_set
        "processes": [],  # found on event_set, event_set.hazard
        "seasonality": [],  # found on event_set
    }

    for event_set in hazard["event_sets"]:
        for es_hazard in event_set.get("hazards", []):
            if "type" in es_hazard:
                props_to_summarize["hazard_type"].append(es_hazard["type"])
            if "hazard_process" in es_hazard:
                props_to_summarize["processes"].append(es_hazard["hazard_process"])
            if "intensity_measure" in es_hazard:
                props_to_summarize["intensity"].append(es_hazard["intensity_measure"])

        if "analysis_type" in event_set:
            props_to_summarize["hazard_analysis_type"].append(
                event_set["analysis_type"]
            )
        if "calculation_method" in event_set:
            props_to_summarize["calculation_method"].append(
                event_set["calculation_method"]
            )
        if "intensity_measure" in event_set:
            props_to_summarize["intensity"].append(event_set["intensity_measure"])
        if "occurrence_range" in event_set:
            props_to_summarize["occurrence_range"].append(event_set["occurrence_range"])
        if "hazard_process" in event_set:
            props_to_summarize["processes"].append(event_set["hazard_process"])
        if "seasonality" in event_set:
            props_to_summarize["seasonality"].append(event_set["seasonality"])
        if "type" in event_set:
            props_to_summarize["hazard_type"].append(event_set["type"])

        if "events" in event_set:
            for event in event_set["events"]:
                if "disaster_identifiers" in event:
                    for di in event["disaster_identifiers"]:
                        props_to_summarize["disaster_identifiers"].append(
                            f"{di.get('id')}; {di.get('scheme')}"
                        )

    return {
        "calculation_method": ", ".join(
            sorted(set(props_to_summarize["calculation_method"]))
        ),
        "disaster_identifiers": ", ".join(
            sorted(set(props_to_summarize["disaster_identifiers"]))
        ),
        "hazard_analysis_type": ", ".join(
            sorted(set(props_to_summarize["hazard_analysis_type"]))
        ),
        "hazard_type": ", ".join(sorted(set(props_to_summarize["hazard_type"]))),
        "intensity": ", ".join(sorted(set(props_to_summarize["intensity"]))),
        "occurrence_range": ", ".join(
            sorted(set(props_to_summarize["occurrence_range"]))
        ),
        "processes": ", ".join(sorted(set(props_to_summarize["processes"]))),
        "seasonality": ", ".join(sorted(set(props_to_summarize["seasonality"]))),
    }


def make_lineage(lineage):
    return {
        # optional
        "description": lineage.get("description"),
        "sources": [make_source(source) for source in lineage.get("sources", [])],
    }


def make_loss(loss):
    """Convert RDL loss metadata into JKAN frontmatter"""
    if loss is None:
        return None

    props_to_summarize = {
        # required; throw if missing
        "dimension": [],
        "hazard_type": [],
        # optional
        "approach": [],
        "base_data_type": [],
        "category": [],
        "description": [],
        "exposure_id": [],
        "hazard_analysis_type": [],
        "hazard_id": [],
        "hazard_process": [],
        "impact_metric": [],
        "impact_type": [],
        "impact_unit": [],
        "type": [],
        "vulnerability_id": [],
    }

    for l in loss.get("losses", []):
        if "dimension" in l.get("cost", {}):
            props_to_summarize["dimension"].append(l["cost"]["dimension"])
        if "hazard_type" in l:
            props_to_summarize["hazard_type"].append(l["hazard_type"])
        if "approach" in l:
            props_to_summarize["approach"].append(l["approach"])
        if "base_data_type" in l.get("impact", {}):
            props_to_summarize["base_data_type"].append(l["impact"]["base_data_type"])
        if "category" in l:
            props_to_summarize["category"].append(l["category"])
        if "description" in l:
            props_to_summarize["description"].append(l["description"])
        if "exposure_id" in l:
            props_to_summarize["exposure_id"].append(l["exposure_id"])
        if "hazard_analysis_type" in l:
            props_to_summarize["hazard_analysis_type"].append(l["hazard_analysis_type"])
        if "hazard_id" in l:
            props_to_summarize["hazard_id"].append(l["hazard_id"])
        if "hazard_process" in l:
            props_to_summarize["hazard_process"].append(l["hazard_process"])
        if "metric" in l.get("impact", {}):
            props_to_summarize["impact_metric"].append(l["impact"]["metric"])
        if "type" in l.get("impact", {}):
            props_to_summarize["impact_type"].append(l["impact"]["type"])
        if "unit" in l.get("impact", {}):
            props_to_summarize["impact_unit"].append(l["impact"]["unit"])
        if "type" in l:
            props_to_summarize["type"].append(l["type"])
        if "vulnerability_id" in l:
            props_to_summarize["vulnerability_id"].append(l["vulnerability_id"])

    return {
        "dimension": ", ".join(sorted(set(props_to_summarize["dimension"]))),
        "hazard_type": ", ".join(sorted(set(props_to_summarize["hazard_type"]))),
        "approach": ", ".join(sorted(set(props_to_summarize["approach"]))),
        "base_data_type": ", ".join(sorted(set(props_to_summarize["base_data_type"]))),
        "category": ", ".join(sorted(set(props_to_summarize["category"]))),
        "description": ", ".join(sorted(set(props_to_summarize["description"]))),
        "exposure_id": ", ".join(sorted(set(props_to_summarize["exposure_id"]))),
        "hazard_analysis_type": ", ".join(
            sorted(set(props_to_summarize["hazard_analysis_type"]))
        ),
        "hazard_id": ", ".join(sorted(set(props_to_summarize["hazard_id"]))),
        "hazard_process": ", ".join(sorted(set(props_to_summarize["hazard_process"]))),
        "impact_metric": ", ".join(sorted(set(props_to_summarize["impact_metric"]))),
        "impact_type": ", ".join(sorted(set(props_to_summarize["impact_type"]))),
        "impact_unit": ", ".join(sorted(set(props_to_summarize["impact_unit"]))),
        "type": ", ".join(sorted(set(props_to_summarize["type"]))),
        "vulnerability_id": ", ".join(
            sorted(set(props_to_summarize["vulnerability_id"]))
        ),
    }


def make_metric(metric):
    return {
        # required; throw if missing
        "id": metric["id"],
        "dimension": metric["dimension"],
        "quantity_kind": metric["quantity_kind"],
    }



def make_project(project):
    return {
        "name": project["name"],
        "url": project.get("url"),
    }


def make_related_resource(related_resource):
    return {
        # required; throw if missing
        "id": related_resource["id"],
        # optional
        "author_names": related_resource.get("author_names"),
        "date_published": related_resource.get("date_published"),
        "doi": related_resource.get("doi"),
        "name": related_resource.get("name"),
        "url": related_resource.get("url"),
    }


def make_resource(resource):
    """Convert resource metadata into JKAN frontmatter"""
    return {
        # required; throw if missing
        "description": resource["description"],
        "id": resource["id"],
        "title": resource["title"],
        # optional
        "access_url": resource.get("access_url"),
        "download_url": resource.get("download_url"),
        "media_type": resource.get("media_type"),
        "format": resource.get("format"),
        "conforms_to": resource.get("conforms_to"),
        "spatial": make_spatial(resource["spatial"]) if "spatial" in resource else None,
        "spatial_aggregation": resource.get("spatial_aggregation"),
        "spatial_resolution": resource.get("spatial_resolution"),
        "coordinate_system": resource.get("coordinate_system"),
        "temporal": make_temporal(resource["temporal"]) if "temporal" in resource else None,
        "temporal_resolution": resource.get("temporal_resolution"),
        "baseline_period": make_temporal(resource["baseline_period"]) if "baseline_period" in resource else None,
        "climate": make_climate(resource["climate"]) if "climate" in resource else None,    
    }


def make_source(source):
    return {
        # required; throw if missing
        "id": source["id"],
        # optional
        "license": source.get("license"),
        "name": source.get("name"),
        "risk_data_type": source.get("risk_data_type"),
        "type": source.get("type"),
        "url": source.get("url"),
        "used_in": source.get("used_in"),
    }


def make_spatial(spatial):
    # TODO: spatial is required but has no required properties??
    # unless there must be one gazetteer entry?
    if spatial.get("scale") == "global":
        if (
            "countries" in spatial
            and type(spatial["countries"]) == list
        ):
            spatial["countries"].append("GLO")
        else:
            spatial["countries"] = ["GLO"]
    return {
        "bbox": spatial.get("bbox"),
        "centroid": spatial.get("centroid"),
        "countries": spatial.get("countries"),
        "gazetteer_entries": [make_gazetteer_entry(g) for g in spatial.get("gazetteer_entries", [])],
        "scale": spatial.get("scale"),
    }
    

def make_temporal(temporal):
    return {
        "start": temporal.get("start"),
        "end": temporal.get("end"),
        "duration": temporal.get("duration"),
        "central_year": temporal.get("central_year"),
    }


def make_vulnerability(vulnerability):
    """Convert RDL vulnerability metadata into JKAN frontmatter"""
    if vulnerability is None:
        return None

    approach = []
    relationship = []
    base_data_type = []
    function_type = []
    category = []
    hazard_primary = []
    intensity = []
    metric = []
    unit = []
    hazard_analysis_type = []
    hazard_process_primary = []
    hazard_process_secondary = []
    hazard_secondary = []
    taxonomy = []
    impact_type = []
    functions = (
        vulnerability.get("functions", {}).get("vulnerability", [])
        + vulnerability.get("functions", {}).get("fragility", [])
        + vulnerability.get("functions", {}).get("damage_to_loss", [])
        + vulnerability.get("functions", {}).get("engineering_demand", [])
    )
    for f in functions:
        if "approach" in f:
            approach.append(f["approach"])
        if "relationship" in f:
            relationship.append(f["relationship"])
        if "approach" in f:
            approach.append(f["approach"])
        if "impact_modelling" in f:
            base_data_type.append(f["impact_modelling"])
        if "category" in f:
            category.append(f["category"])
        if "hazard_primary" in f:
            hazard_primary.append(f["hazard_primary"])
        if "intensity" in f:
            intensity.append(f["intensity"])
        if "impact_metric" in f:
            metric.append(f["impact_metric"])
        if "impact_type" in f:
            impact_type.append(f["impact_type"])
        if "quantity_kind" in f:
            unit.append(f["quantity_kind"])
        if "hazard_analysis_type" in f:
            hazard_analysis_type.append(f["hazard_analysis_type"])
        if "hazard_process_primary" in f:
            hazard_process_primary.append(f["hazard_process_primary"])
        if "hazard_process_secondary" in f:
            hazard_process_secondary.append(f["hazard_process_secondary"])
        if "hazard_secondary" in f:
            hazard_secondary.append(f["hazard_secondary"])
        if "taxonomy" in f:
            taxonomy.append(f["taxonomy"])

    props_to_summarize = {"dimension": [], "unit": []}

    if "cost" in vulnerability:
        for cost in vulnerability["cost"]:
            if cost["dimension"]:
                props_to_summarize["dimension"].append(cost["dimension"])
            if cost["unit"]:
                props_to_summarize["unit"].append(cost["unit"])

    return {
        # required; throw if missing
        "approach": ", ".join(sorted(set(approach))),
        "base_data_type": ", ".join(sorted(set(base_data_type))),
        "category": ", ".join(sorted(set(category))),
        "dimension": ", ".join(sorted(set(props_to_summarize["dimension"]))),
        "function_type": ", ".join(sorted(set(function_type))),
        "hazard_primary": ", ".join(sorted(set(hazard_primary))),
        "intensity": ", ".join(sorted(set(intensity))),
        "metric": ", ".join(sorted(set(metric))),
        "relationship": ", ".join(sorted(set(relationship))),
        # "scale": vulnerability.get("spatial").get("scale"),
        "unit": ", ".join(sorted(set(props_to_summarize["unit"]))),
        # optional
        "hazard_analysis_type": ", ".join(sorted(set(hazard_analysis_type))),
        "hazard_process_primary": ", ".join(sorted(set(hazard_process_primary))),
        "hazard_process_secondary": ", ".join(sorted(set(hazard_process_secondary))),
        "hazard_secondary": ", ".join(sorted(set(hazard_secondary))),
        "taxonomy": ", ".join(sorted(set(taxonomy))),
    }
