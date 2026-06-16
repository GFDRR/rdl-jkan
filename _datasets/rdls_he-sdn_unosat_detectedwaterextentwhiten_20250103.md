---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-2 satellite imagery
    url: https://data.humdata.org/dataset/satellite-detected-water-extent-in-white-nile-state-sudan-as-of-1-january-2025
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop population data
    url: https://data.humdata.org/dataset/satellite-detected-water-extent-in-white-nile-state-sudan-as-of-1-january-2025
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-in-white-nile-state-sudan-as-of-1-january-2025
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-in-white-nile-state-sudan-as-of-1-january-2025
dataset_id: rdls_he-sdn_unosat_detectedwaterextentwhiten_20250103
description: "UNOSAT code: FL20241224SDN This map illustrates the satellite-detected\
  \ water extent in White Nile State, Sudan, as observed from a Sentinel-2 satellite\
  \ image acquired on 1 January 2025 at 10:13 local time (08:13 UTC). Within the analyzed\
  \ area of approximately 24,000 km\xB2, about 145 km\xB2 of land appears to be affected\
  \ by floodwaters. Floodwater extent seems to have increased by about 5 km\xB2 compared\
  \ to 27 December 2024. Based on WorldPop population data and the flood extent, approximately\
  \ 63,000 people are potentially exposed or living close to the flooded areas. This\
  \ is a preliminary analysis and has not yet been validated in the field. Please\
  \ send ground feedback to the United Nations Satellite Centre (UNOSAT).. [Source:\
  \ This metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extent-in-white-nile-state-sudan-as-of-1-january-2025]"
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
    description: Population potentially exposed or living close to flooded areas based
      on WorldPop data
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
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "UNOSAT analysts reviewed Sentinel-2 satellite imagery acquired on\
    \ 1 January 2025 and compared it with imagery from 27 December 2024 to detect\
    \ changes in water extent. Water bodies were delineated and classified by confidence\
    \ level. Detected flood extent (145 km\xB2) was overlaid with WorldPop population\
    \ data to estimate approximately 63,000 people potentially exposed to floodwaters\
    \ in White Nile State."
  sources:
  - id: source_1
    license: null
    name: Sentinel-2 satellite imagery
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: WorldPop population data
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/satellite-detected-water-extent-in-white-nile-state-sudan-as-of-1-january-2025
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
  description: Satellite detected water extent in White Nile State, Sudan as of 1
    January 2025 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4065/FL20241224SDN_gdb.zip
  format: Geodatabase
  id: resource_4f7a9af3
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20241224SDN_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent in White Nile State, Sudan as of 1
    January 2025 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4065/FL20241224SDN_SHP.zip
  format: null
  id: resource_a0c325ed
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20241224SDN_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent in White Nile State, Sudan as of 1
    January 2025 (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/4065/UNOSAT_Population_Exposure_FL20241224SDN_1Jan2024_Sudan.xlsx
  format: null
  id: resource_86257d2c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_Population_Exposure_FL20241224SDN_1Jan2024_Sudan.xlsx
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-sdn_unosat_detectedwaterextentwhiten_20250103
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
  start: '2025-01-03'
temporal_resolution: null
title: Satellite detected water extent in White Nile State, Sudan as of 1 January
  2025
version: null
vulnerability: null
---
