---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNEP/UNISDR GAR 2013
    url: https://data.humdata.org/dataset/ica-sudan-2018-flood-risk-2013
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Sudan
  url: https://data.humdata.org/dataset/ica-sudan-2018-flood-risk-2013
creator:
  affiliation: null
  email: null
  name: OCHA Sudan
  url: https://data.humdata.org/dataset/ica-sudan-2018-flood-risk-2013
dataset_id: rdls_he-sdn_ochasdn_ica2018floodrisk2013_20181122
description: 'This layer contains information about the flood risk - by second-level
  administrative area - estimated during the Integrated Context Analysis (ICA) run
  in Sudan in 2018. Data sources: UNEP/UNISDR, GAR 2013. The main indicators used
  for the analysis were the percentage of district surface at flood risk and the maximum
  expected frequency of flood events with a 100-year return period.. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/ica-sudan-2018-flood-risk-2013]'
details: null
exposure:
- asset_type:
    description: Population distribution across districts with percentage of surface
      area at flood risk
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: inferred
    event_count: 1
    events:
    - calculation_method: inferred
      description: Probabilistic flood hazard assessment by administrative district
        with maximum expected frequency at 100-year return period
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_flood
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_100yr
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.01
          probability: null
          return_period: 100
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-4.0
lineage:
  description: The Integrated Context Analysis (ICA) Sudan 2018 integrated flood risk
    data from UNEP/UNISDR GAR 2013 to estimate probabilistic flood hazard at the second-level
    administrative district scale. Key indicators include the percentage of district
    surface area at flood risk and maximum expected frequency of flood events at the
    100-year return period, aggregated by administrative boundaries.
  sources:
  - id: source_1
    license: null
    name: UNEP/UNISDR GAR 2013
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/ica-sudan-2018-flood-risk-2013
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Sample Survey
referenced_by: []
resources:
- access_url: https://geonode.wfp.org/geoserver/wfs?format_options=charset%3AUTF-8&typename=geonode%3Asdn_ica_floodrisk_geonode_20180201&outputFormat=SHAPE-ZIP&version=1.0.0&service=WFS&request=GetFeature
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: 'This layer contains information about the flood risk - by second-level
    administrative area - estimated during the Integrated Context Analysis (ICA) run
    in Sudan in 2018. Data sources: UNEP/UNISDR, GAR 2013. The main indicators used
    for the analysis were the percentage of district surface at flood risk and the
    maximum expected frequency of flood events with a 100-year return period.'
  download_url: null
  format: null
  id: resource_b3a9fddc
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Sudan, 2018 - Flood Risk, 2013
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-sdn_ochasdn_ica2018floodrisk2013_20181122
spatial:
  bbox: null
  centroid: null
  countries:
  - SDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-11-22'
temporal_resolution: null
title: ICA Sudan, 2018 - Flood Risk, 2013
version: null
vulnerability: null
---
