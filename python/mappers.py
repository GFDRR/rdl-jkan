"""
Differences between RDLS and output frontmatter:
    - catalog added; derived from links and resources
"""

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
        "links": dataset["links"],
        "publisher": make_entity(dataset["publisher"]),
        "resources": [make_resource(resource) for resource in dataset["resources"]],
        "risk_data_type": dataset["risk_data_type"],
        "schema": make_schema(dataset["links"]),
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
        "hazard": make_hazard_top_level(dataset.get("hazard")),
        "lineage": make_lineage(dataset["lineage"]) if "lineage" in dataset else None,
        "loss": [make_loss(l) for l in dataset.get("loss", {}).get("losses",[])],
        "project": make_project(dataset["project"]) if "project" in dataset else None,
        "purpose": dataset.get("purpose"),
        "referenced_by": [
            make_related_resource(related_resource)
            for related_resource in dataset.get("referenced_by", [])
        ],
        "spatial_resolution": dataset.get("spatial_resolution"),
        "temporal": (
            make_temporal(dataset["temporal"]) if "temporal" in dataset else None
        ),
        "temporal_resolution": dataset.get("temporal_resolution"),
        "version": dataset.get("version"),
        "vulnerability": make_vulnerability(dataset.get("vulnerability")),
    }


def make_affiliation(affiliation):
    if affiliation is None:
        return None
    return {
        # required; throw if missing
        "name": affiliation["name"],
        # optional
        "url": affiliation.get("url"),
    }


def make_asset_type(asset_type):
    if asset_type is None:
        return None
    return {
        # required; throw if missing
        "id": asset_type["id"],
        # optional
        "scheme": asset_type.get("scheme"),
        "title": asset_type.get("title"),
        "description": asset_type.get("description"),
        "uri": asset_type.get("uri"),
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


def make_classification(classification):
    if classification is None:
        return None
    return {
        # required; throw if missing
        "id": classification["id"],
        # optional
        "description": classification.get("description"),
        "scheme": classification.get("scheme"),
        "title": classification.get("title"),
        "uri": classification.get("uri"),
    }


def make_climate(climate):
    return {
        # optional
        "model": climate.get("model"),
        "scenario": climate.get("scenario"),
        "percentile": climate.get("percentile"),
    }


def make_disaster_identifier(disaster_identifier):
    return {
        # required; throw if missing
        "id": disaster_identifier["id"],
        # optional
        "description": disaster_identifier.get("description"),
        "scheme": disaster_identifier.get("scheme"),
        "title": disaster_identifier.get("title"),
        "uri": disaster_identifier.get("uri"),
    }


def make_entity(attribution):
    return {
        # required; throw if missing
        "name": attribution["name"],
        # optional
        "email": attribution.get("email"),
        "url": attribution.get("url"),
        "affiliation": make_affiliation(attribution.get("affiliation")),
    }


def make_event(event):
    return {
        # required; throw if missing
        "id": event["id"],
        "calculation_method": event["calculation_method"],
        "hazard": make_hazard(event["hazard"]),
        "occurrence": make_occurrence(event["occurrence"]),
        # optional
        "disaster_identifiers": [
            make_disaster_identifier(di) for di in event.get("disaster_identifiers", [])
        ],
        "description": event.get("description"),
    }


def make_event_set(event_set):
    return {
        # required; throw if missing
        "id": event_set["id"],
        "hazards": [make_hazard(hazard) for hazard in event_set["hazards"]],
        "analysis_type": event_set["analysis_type"],
        # optional
        "frequency_distribution": event_set.get("frequency_distribution"),
        "seasonality": event_set.get("seasonality"),
        "calculation_method": event_set.get("calculation_method"),
        "event_count": event_set.get("event_count"),
        "occurrence_range": event_set.get("occurrence_range"),
        "events": [make_event(event) for event in event_set.get("events", [])],
    }


def make_exposure(exposure):
    """Convert RDL exposure metadata into JKAN frontmatter"""
    if exposure is None:
        return None

    return {
        # required; throw if missing
        "id": exposure["id"],
        "category": exposure["category"],
        "metrics": [make_metric(metric) for metric in exposure.get("metrics", [])],
        # optional
        "asset_type": make_asset_type(exposure.get("asset_type")),
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


def make_hazard_top_level(hazard):
    """Convert RDL hazard metadata into JKAN frontmatter"""
    if hazard is None:
        return None

    return {
        "event_sets": [make_event_set(event_set) for event_set in hazard["event_sets"]],
    }


def make_hazard(hazard):
    return {
        # required; throw if missing
        "id": hazard["id"],
        "type": hazard["type"],
        "process": hazard["process"],
        "intensity_measure": hazard["intensity_measure"],
        # optional
        "classification": make_classification(hazard.get("classification")),
        "trigger": make_trigger(hazard["trigger"]) if "trigger" in hazard else None,
    }


def make_impact(impact):
    if impact is None:
        return None
    return {
        # optional
        "measurement": make_measurement(impact.get("measurement")),
        "metric": impact.get("metric"),
        "modelling": impact.get("modelling"),
        "type": impact.get("type"),
    }


def make_impact_and_losses(impact_and_losses):
    return {
        # required; throw if missing
        "loss_type": impact_and_losses["loss_type"],
        "loss_approach": impact_and_losses["loss_approach"],
        "loss_frequency_type": impact_and_losses["loss_frequency_type"],
        # optional
        "impact": make_impact(impact_and_losses.get("impact")),
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
    return {
        # requred; throw if missing
        "id": loss["id"],
        "asset_category": loss["asset_category"],
        "asset_dimension": loss["asset_dimension"],
        "hazard": make_hazard(loss["hazard"]),
        "impact_and_losses": make_impact_and_losses(loss["impact_and_losses"]),
        # optional
        "description": loss.get("description"),
        "disaster_identifiers": [
            make_disaster_identifier(di) for di in loss.get("disaster_identifiers", [])
        ],
    }


def make_measurement(measurement):
    return {
        # optional
        "quantity_kind": measurement.get("quantity_kind"),
        "unit": measurement.get("unit"),
    }


def make_metric(metric):
    return {
        # required; throw if missing
        "id": metric["id"],
        "dimension": metric["dimension"],
        "measurement": make_measurement(metric["measurement"]),
    }


def make_occurrence(occurrence):
    return {
        # required; throw if missing
        # optional
        "deterministic": make_occurrence_deterministic(occurrence.get("deterministic")),
        "empirical": make_occurrence_empirical(occurrence.get("empirical")),
        "probabilistic": make_occurrence_probabilistic(occurrence.get("probabilistic")),
    }


def make_occurrence_deterministic(deterministic):
    if deterministic is None:
        return None
    return {
        # optional
        "index_criteria": deterministic.get("index_criteria"),
        "thresholds": deterministic.get("thresholds"),
        "description": deterministic.get("description"),
    }


def make_occurrence_empirical(empirical):
    if empirical is None:
        return None
    return {
        # optional
        "temporal": (
            make_temporal(empirical["temporal"]) if "temporal" in empirical else None
        ),
        "return_period": empirical.get("return_period"),
    }


def make_occurrence_probabilistic(probabilistic):
    if probabilistic is None:
        return None
    return {
        # optional
        "return_period": probabilistic.get("return_period"),
        "event_rate": probabilistic.get("event_rate"),
        "probability": make_occurrence_probablilistic_probability(
            probabilistic.get("probability")
        ),
    }


def make_occurrence_probablilistic_probability(probability):
    if probability is None:
        return None
    return {
        # required; throw if missing
        "span": probability["span"],
        # optional
        "value": probability.get("value"),
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
        "temporal": (
            make_temporal(resource["temporal"]) if "temporal" in resource else None
        ),
        "temporal_resolution": resource.get("temporal_resolution"),
        "baseline_period": (
            make_temporal(resource["baseline_period"])
            if "baseline_period" in resource
            else None
        ),
        "climate": make_climate(resource["climate"]) if "climate" in resource else None,
    }


def make_schema(links):
    for link in links:
        if link.get("rel") == "describedby":
            return link.get("href")
    return None


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
        if "countries" in spatial and type(spatial["countries"]) == list:
            spatial["countries"].append("GLO")
        else:
            spatial["countries"] = ["GLO"]
    return {
        "bbox": spatial.get("bbox"),
        "centroid": spatial.get("centroid"),
        "countries": spatial.get("countries"),
        "gazetteer_entries": [
            make_gazetteer_entry(g) for g in spatial.get("gazetteer_entries", [])
        ],
        "scale": spatial.get("scale"),
    }


def make_temporal(temporal):
    return {
        "start": temporal.get("start"),
        "end": temporal.get("end"),
        "duration": temporal.get("duration"),
        "central_year": temporal.get("central_year"),
    }


def make_trigger(trigger):
    return {
        # required; throw if missing
        "type": trigger["type"],
        # optional
        "process": trigger.get("process"),
    }


def make_vulnerability(vulnerability):
    """Convert RDL vulnerability metadata into JKAN frontmatter"""
    if vulnerability is None or vulnerability.get("functions") is None:
        return None
    return {
        # optional
        "functions": {
            "damage_to_loss": [
                make_vulnerability_function_damage_to_loss(vf)
                for vf in vulnerability["functions"].get("damage_to_loss", [])
            ],
            "engineering_demand": [
                make_vulnerability_function_engineering_demand(vf)
                for vf in vulnerability["functions"].get("engineering_demand", [])
            ],
            "fragility": [
                make_vulnerability_function_fragility(vf)
                for vf in vulnerability["functions"].get("fragility", [])
            ],
            "socio_economic": [
                make_vulnerability_function_socio_economic(vf)
                for vf in vulnerability["functions"].get("socio_economic", [])
            ],
            "vulnerability": [
                make_vulnerability_function_vulnerability(vf)
                for vf in vulnerability["functions"].get("vulnerability", [])
            ],
        }
    }


def make_vulnerability_function_vulnerability(vf):
    return {
        # required; throw if missing
        "id": vf["id"],
        "approach": vf["approach"],
        "relationship": vf["relationship"],
        # optional
        "analysis_details": vf.get("analysis_details"),
        "category": vf.get("category"),
        "hazard_analysis_type": vf.get("hazard_analysis_type"),
        "hazard_primary": (
            make_hazard(vf["hazard_primary"]) if "hazard_primary" in vf else None
        ),
        "hazard_secondary": (
            make_hazard(vf["hazard_secondary"]) if "hazard_secondary" in vf else None
        ),
        "impact": make_impact(vf.get("impact")),
        "taxonomy": vf.get("taxonomy"),
    }


def make_vulnerability_function_fragility(vf):
    return {
        # required; throw if missing
        "id": vf["id"],
        "approach": vf["approach"],
        "relationship": vf["relationship"],
        # optional
        "analysis_details": vf.get("analysis_details"),
        "category": vf.get("category"),
        "hazard_analysis_type": vf.get("hazard_analysis_type"),
        "hazard_primary": (
            make_hazard(vf["hazard_primary"]) if "hazard_primary" in vf else None
        ),
        "hazard_secondary": (
            make_hazard(vf["hazard_secondary"]) if "hazard_secondary" in vf else None
        ),
        "impact": make_impact(vf.get("impact")),
        "damage_scale_name": vf.get("damage_scale_name"),
        "damage_states_names": vf.get("damage_states_names"),
        "taxonomy": vf.get("taxonomy"),
    }


def make_vulnerability_function_damage_to_loss(vf):
    return {
        # required; throw if missing
        "id": vf["id"],
        "approach": vf["approach"],
        "relationship": vf["relationship"],
        # optional
        "analysis_details": vf.get("analysis_details"),
        "category": vf.get("category"),
        "hazard_analysis_type": vf.get("hazard_analysis_type"),
        "hazard_primary": (
            make_hazard(vf["hazard_primary"]) if "hazard_primary" in vf else None
        ),
        "hazard_secondary": (
            make_hazard(vf["hazard_secondary"]) if "hazard_secondary" in vf else None
        ),
        "impact": make_impact(vf.get("impact")),
        "loss_scale_name": vf.get("loss_scale_name"),
        "loss_states_names": vf.get("loss_states_names"),
        "taxonomy": vf.get("taxonomy"),
    }


def make_vulnerability_function_engineering_demand(vf):
    return {
        # required; throw if missing
        "id": vf["id"],
        "approach": vf["approach"],
        "relationship": vf["relationship"],
        # optional
        "analysis_details": vf.get("analysis_details"),
        "category": vf.get("category"),
        "hazard_analysis_type": vf.get("hazard_analysis_type"),
        "hazard_primary": (
            make_hazard(vf["hazard_primary"]) if "hazard_primary" in vf else None
        ),
        "hazard_secondary": (
            make_hazard(vf["hazard_secondary"]) if "hazard_secondary" in vf else None
        ),
        "impact": make_impact(vf.get("impact")),
        "demand_scale_name": vf.get("demand_scale_name"),
        "demand_states_names": vf.get("demand_states_names"),
        "taxonomy": vf.get("taxonomy"),
        "parameter": vf.get("parameter"),
    }


def make_vulnerability_function_socio_economic(vf):
    return {
        # required; throw if missing
        "id": vf["id"],
        "indicator_name": vf["indicator_name"],
        "indicator_code": vf["indicator_code"],
        "description": vf["description"],
        "reference_year": vf["reference_year"],
        # optional
        "scheme": vf.get("scheme"),
        "threshold": vf.get("threshold"),
        "uri": vf.get("uri"),
        "analysis_details": vf.get("analysis_details"),
    }
