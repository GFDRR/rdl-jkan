import config

def make_exposure(exposure):
    """Convert RDL exposure metadata into JKAN frontmatter"""
    if exposure is None:
        return None

    props_to_summarize = {
        "dimension": [],  # found on metric
        "quantity_kind": [],  # found on metric
    }

    if "metrics" in exposure:
        for metric in exposure["metrics"]:
            if metric["dimension"]:
                props_to_summarize["dimension"].append(metric["dimension"])
            if metric["quantity_kind"]:
                props_to_summarize["quantity_kind"].append(metric["quantity_kind"])

    return {
        # required; throw if missing
        "category": exposure["category"],
        # optional
        "taxonomy": exposure.get("taxonomy"),
        "dimension": ", ".join(sorted(set(props_to_summarize["dimension"]))),
        "quantity_kind": ", ".join(sorted(set(props_to_summarize["quantity_kind"]))),
    }


def make_hazard_v02(hazard):
    """Convert RDL hazard metadata into JKAN frontmatter"""
    if hazard is None:
        return None

    props_to_summarize = {
        "calculation_method": [],  # found on event, event_set
        "disaster_identifiers": [],  # found on event
        "hazard_analysis_type": [],  # found on event_set as analysis_type
        "hazard_type": hazard.get("type", []),  # found on hazard, event.hazard as type
        "intensity": hazard.get(
            "intensity_measure", []
        ),  # found on hazard, event.hazard as intensity_measure
        "occurrence_range": [],  # found on event_set
        "processes": hazard.get("processes", []),  # found on hazard, event.hazard
    }

    for event_set in hazard["event_sets"]:
        if "calculation_method" in event_set:
            props_to_summarize["calculation_method"].append(
                event_set["calculation_method"]
            )
        if "analysis_type" in event_set:
            props_to_summarize["hazard_analysis_type"].append(
                event_set["analysis_type"]
            )
        if "occurrence_range" in event_set:
            props_to_summarize["occurrence_range"].append(event_set["occurrence_range"])

        if "events" in event_set:
            for event in event_set["events"]:
                if "calculation_method" in event:
                    props_to_summarize["calculation_method"].append(
                        event["calculation_method"]
                    )
                if "disaster_identifiers" in event:
                    for di in event["disaster_identifiers"]:
                        props_to_summarize["disaster_identifiers"].append(
                            f"{di.get('id')}; {di.get('scheme')}"
                        )
                if "hazard" in event and "type" in event["hazard"]:
                    props_to_summarize["hazard_type"].append(event["hazard"]["type"])
                if "hazard" in event and "intensity_measure" in event["hazard"]:
                    props_to_summarize["intensity"].append(
                        event["hazard"]["intensity_measure"]
                    )
                if "hazard" in event and "processes" in event["hazard"]:
                    props_to_summarize["processes"].extend(event["hazard"]["processes"])
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


# v0.2 specific mappers
def make_resource_v02(resource):
    """Convert RDL v0.2 resource metadata into JKAN frontmatter"""
    return {
        # required; throw if missing
        "description": resource["description"],
        "format": resource["format"],
        "id": resource["id"],
        "title": resource["title"],
        # optional
        "coordinate_system": resource.get("coordinate_system"),
        "download_url": resource.get("download_url", resource.get("access_url")),
        "spatial_resolution": resource.get("spatial_resolution"),
    }

def make_vulnerability_v02(vulnerability):
    """Convert RDL vulnerability metadata into JKAN frontmatter"""
    if vulnerability is None:
        return None

    impact = vulnerability.get("impact")

    # TODO: will there ever actually be more than one function type present on a vulnerability?
    approach = []
    relationship = []
    function_type = []
    functions = vulnerability.get("functions")
    if "vulnerability" in functions:
        if "approach" in functions["vulnerability"]:
            approach.append(functions["vulnerability"]["approach"])
        if "relationship" in functions["vulnerability"]:
            relationship.append(functions["vulnerability"]["relationship"])
        function_type.append("vulnerability")
    if "fragility" in functions:
        if "approach" in functions["fragility"]:
            approach.append(functions["fragility"].get("approach"))
        if "relationship" in functions["fragility"]:
            relationship.append(functions["fragility"].get("relationship"))
        function_type.append("fragility")
    if "damage_to_loss" in functions:
        if "approach" in functions["damage_to_loss"]:
            approach.append(functions["damage_to_loss"].get("approach"))
        if "relationship" in functions["damage_to_loss"]:
            relationship.append(functions["damage_to_loss"].get("relationship"))
        function_type.append("damage_to_loss")
    if "engineering_demand" in functions:
        if "approach" in functions["engineering_demand"]:
            approach.append(functions["engineering_demand"].get("approach"))
        if "relationship" in functions["engineering_demand"]:
            relationship.append(functions["engineering_demand"].get("relationship"))
        function_type.append("engineering_demand")

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
        "base_data_type": impact.get("base_data_type"),
        "category": vulnerability.get("category"),
        "dimension": ", ".join(sorted(set(props_to_summarize["dimension"]))),
        "function_type": ", ".join(sorted(set(function_type))),
        "hazard_primary": vulnerability.get("hazard_primary"),
        "intensity": vulnerability.get("intensity"),
        "metric": impact.get("metric"),
        "relationship": ", ".join(sorted(set(relationship))),
        "scale": vulnerability.get("spatial").get("scale"),
        "type": impact.get("type"),
        "unit": ", ".join(sorted(set(props_to_summarize["unit"]))),
        "impact_unit": impact.get("unit"),
        # optional
        "hazard_analysis_type": vulnerability.get("hazard_analysis_type"),
        "hazard_process_primary": vulnerability.get("hazard_process_primary"),
        "hazard_process_secondary": vulnerability.get("hazard_process_secondary"),
        "hazard_secondary": vulnerability.get("hazard_secondary"),
        "taxonomy": vulnerability.get("taxonomy"),
    }

def make_dataset_frontmatter_v02(dataset):
    """Formats RDL v0.2 metadata into JKAN frontmatter for a dataset"""

    payload = {
        "schema": "rdl-02",
        # try first; required by write_yaml
        "title": dataset["title"],
        # required; throw if missing
        "catalog": make_catalog(dataset),
        "contact_point": dataset["contact_point"],
        "creator": dataset["creator"],
        "dataset_id": dataset["id"],
        "slug": dataset["id"],
        "license": dataset["license"],
        "publisher": dataset["publisher"],
        "resources": [make_resource_v02(resource) for resource in dataset["resources"]],
        "risk_data_type": dataset["risk_data_type"],
        "spatial": dataset["spatial"],
        # optional
        "description": dataset.get("description"),
        "details": dataset.get("details"),
        "project": dataset.get("project"),
        "purpose": dataset.get("purpose"),
        "version": dataset.get("version"),
        # must include one of
        "exposure": make_exposure(dataset.get("exposure")),
        "hazard": make_hazard_v02(dataset.get("hazard")),
        "loss": make_loss(dataset.get("loss")),
        "vulnerability": make_vulnerability_v02(dataset.get("vulnerability")),
    }

    if payload["spatial"].get("scale") == "global":
        if (
            "countries" in payload["spatial"]
            and type(payload["spatial"]["countries"]) == list
        ):
            payload["spatial"]["countries"].append("GLO")
        else:
            payload["spatial"]["countries"] = ["GLO"]
    return payload


# v0.3 specific mappers
def make_attribution(attribution_or_attributions, role=None):
    if role is not None:
        attributions = attribution_or_attributions
        attribution = next((a for a in attributions if a["role"] == role), None)
        if attribution is None:
            return None
    else:
        attribution = attribution_or_attributions

    entity = attribution["entity"]
    payload = {
        "email": entity.get("email"),
        "id": attribution["id"],
        "name": entity["name"],
        "url": entity.get("url"),
    }

    if role is None:
        # add role to attribution if it's not named on the RDL schema
        # e.g. contact_point, creator, publisher
        payload["role"] = attribution["role"]

    return payload


def make_catalog(dataset):
    link_hrefs = [link.get("href") for link in dataset.get("links", [])]     
    access_urls = [resource.get("access_url") for resource in dataset.get("resources", [])]

    for url in link_hrefs + access_urls:
        for prefix, label in config.dataset_catalogs.items():
            if url is not None and prefix in url:
                return label
    return None

def make_extra_attributions(attributions):
    main_attributions = ["contact_point", "creator", "publisher"]
    return [
        make_attribution(a) for a in attributions if a["role"] not in main_attributions
    ]


def make_hazard_v03(hazard):
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


def make_metric(metric):
    return {
        # required; throw if missing
        "id": metric["id"],
        "dimension": metric["dimension"],
        "quantity_kind": metric["quantity_kind"],
    }


def make_period(period):
    if period is None:
        return None
    return {
        "start": period.get("start"),
        "end": period.get("end"),
        "duration": period.get("duration"),
        "temporal_resolution": period.get("temporal_resolution"),
    }

def make_exposure_v03(exposure_array):
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
        "taxonomy": ", ".join(sorted(set(props_to_summarize["taxonomy"]))) if len(props_to_summarize["taxonomy"]) > 0 else None,
        "dimension": ", ".join(sorted(set(props_to_summarize["dimension"])))  if len(props_to_summarize["dimension"]) > 0 else None,
        "quantity_kind": ", ".join(sorted(set(props_to_summarize["quantity_kind"])))  if len(props_to_summarize["quantity_kind"]) > 0 else None,
    }


def make_resource_v03(resource):
    """Convert RDL v0.3 resource metadata into JKAN frontmatter"""
    return {
        # required; throw if missing
        "description": resource["description"],
        "format": resource["data_format"],
        "id": resource["id"],
        "title": resource["title"],
        # optional
        "coordinate_system": resource.get("coordinate_system"),
        "download_url": resource.get("download_url", resource.get("access_url")),
        "spatial_resolution": resource.get("spatial_resolution"),
        "media_type": resource.get("media_type"),
        "temporal": make_period(resource.get("temporal")),
    }

def make_vulnerability_v03(vulnerability):
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
    functions = vulnerability.get("functions", {}).get("vulnerability", []) + vulnerability.get("functions", {}).get("fragility", []) + vulnerability.get("functions", {}).get("damage_to_loss", [])+ vulnerability.get("functions", {}).get("engineering_demand", [])
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
        "category":  ", ".join(sorted(set(category))),
        "dimension": ", ".join(sorted(set(props_to_summarize["dimension"]))),
        "function_type": ", ".join(sorted(set(function_type))),
        "hazard_primary":  ", ".join(sorted(set(hazard_primary))),
        "intensity":  ", ".join(sorted(set(intensity))),
        "metric":  ", ".join(sorted(set(metric))),
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


def make_dataset_frontmatter_v03(dataset):
    """Formats RDL v0.3 metadata into JKAN frontmatter for a dataset"""

    payload = {
        "schema": "rdl-03",
        # try first; required by write_yaml
        "title": dataset["title"],
        # required; throw if missing
        "dataset_id": dataset["id"],
        "slug": dataset["id"],
        "license": dataset["license"],
        "resources": [make_resource_v03(resource) for resource in dataset["resources"]],
        "risk_data_type": dataset["risk_data_type"],
        "spatial": dataset["spatial"],
        "catalog": make_catalog(dataset),
        # must include one of the following three properties
        "contact_point": make_attribution(dataset["attributions"], "contact_point"),
        "creator": make_attribution(dataset["attributions"], "creator"),
        "publisher": make_attribution(dataset["attributions"], "publisher"),
        # optional
        "description": dataset.get("description"),
        "details": dataset.get("details"),
        "extra_attributions": make_extra_attributions(dataset["attributions"]),
        "project": dataset.get("project"),
        "purpose": dataset.get("purpose"),
        "version": dataset.get("version"),
        "exposure": make_exposure_v03(dataset.get("exposure")),
        "hazard": make_hazard_v03(dataset.get("hazard")),
        "loss": make_loss(dataset.get("loss")),
        "vulnerability": make_vulnerability_v03(dataset.get("vulnerability")),
    }

    if payload["spatial"].get("scale") == "global":
        if (
            "countries" in payload["spatial"]
            and type(payload["spatial"]["countries"]) == list
        ):
            payload["spatial"]["countries"].append("GLO")
        else:
            payload["spatial"]["countries"] = ["GLO"]
    return payload
