---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/tropical-cyclone-lola-over-vanuatu-and-solomon-unosat-live-web-map
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/tropical-cyclone-lola-over-vanuatu-and-solomon-unosat-live-web-map
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/tropical-cyclone-lola-over-vanuatu-and-solomon-unosat-live-web-map
dataset_id: rdls_he-slbvut_unosat_tropicalcyclonelolaoverso_20231023
description: 'UNOSAT code TC20231023VUT, GDACS Id: 1001027 This application provides
  geospatial information about tropical cyclone infomation and number of potentially
  population affected by the tropical cyclone Lola over Vanuatu and Solomon. Important
  note: The boundaries and names shown and the designations used on this map do not
  imply official endorsement or acceptance by the United Nations. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/tropical-cyclone-lola-over-vanuatu-and-solomon-unosat-live-web-map]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure:
- asset_type:
    description: Population potentially affected by tropical cyclone Lola
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
      quantity_kind: count
      unit: count
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts reviewed satellite imagery to track tropical cyclone
    Lola and delineate its spatial extent, then conducted population exposure analysis
    to estimate the number of people potentially affected by the cyclone over Vanuatu
    and Solomon Islands.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/tropical-cyclone-lola-over-vanuatu-and-solomon-unosat-live-web-map
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Tropical Cyclone Lola over Vanuatu and Solomon- UNOSAT Live-Web Map
    (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3700/UNOSAT_PopulationExposureAnalysis_LOLA23_Vanuatu_SolomonIslands_24102023.xlsx
  format: null
  id: resource_a8b34d42
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_PopulationExposureAnalysis_LOLA23_Vanuatu_SolomonIslands_24102023.xlsx
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-slbvut_unosat_tropicalcyclonelolaoverso_20231023
spatial:
  bbox: null
  centroid: null
  countries:
  - VUT
  - SLB
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-10-23'
temporal_resolution: null
title: Tropical Cyclone Lola over Vanuatu and Solomon- UNOSAT Live-Web Map
version: null
vulnerability: null
---
