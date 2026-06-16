---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-1 SAR imagery
    url: https://data.humdata.org/dataset/satellite-detected-water-extent-in-north-western-province-sri-lanka-as-of-04-june-2024
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/satellite-detected-water-extent-in-north-western-province-sri-lanka-as-of-04-june-2024
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-in-north-western-province-sri-lanka-as-of-04-june-2024
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-in-north-western-province-sri-lanka-as-of-04-june-2024
dataset_id: rdls_he-lka_unosat_detectedwaterextentnorthw_20240606
description: "UNOSAT code: FL20240603LKA, GDACS ID: 1102660 This map illustrates satellite-detected\
  \ water extent in the North Western Province, Sri Lanka, as observed from a Sentinel-1\
  \ image acquired on June 4, 2024, at 00:25 UTC. Within the analyzed area of about\
  \ 4,000 km\xB2, a total of about 46 km\xB2 of land appears to be affected by floodwaters.\
  \ The water extent appears to have receded by about 34 km\xB2 since May 23, 2024.\
  \ Based on WorldPop population data and the flood extent, approximately 16,000 people\
  \ are potentially exposed. This is a preliminary analysis and has not yet been validated\
  \ in the field. Please send ground feedback to the United Nations Satellite Centre\
  \ (UNOSAT). Important note: Flood analysis from radar images may underestimate the\
  \ presence of standing waters in built-up areas and densely vegetated areas due\
  \ to backscattering properties of the radar signal.. [Source: This metadata record\
  \ was automatically extracted from the Humanitarian Data Exchange (HDX); Original\
  \ dataset: https://data.humdata.org/dataset/satellite-detected-water-extent-in-north-western-province-sri-lanka-as-of-04-june-2024]"
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
    description: Population potentially exposed to flood extent based on WorldPop
      data overlay
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
  description: "Sentinel-1 SAR imagery acquired on June 4, 2024 was analyzed by UNOSAT\
    \ analysts through visual interpretation and change detection comparison with\
    \ historical imagery from May 23, 2024 to delineate water extent polygons. The\
    \ resulting flood extent (46 km\xB2) was overlaid with WorldPop population data\
    \ to estimate approximately 16,000 people potentially exposed to floodwaters in\
    \ the North Western Province study area."
  sources:
  - id: source_1
    license: null
    name: Sentinel-1 SAR imagery
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/satellite-detected-water-extent-in-north-western-province-sri-lanka-as-of-04-june-2024
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
  description: Satellite detected water extent in North Western Province, Sri Lanka
    as of 04 June 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3873/FL20240603LKA_gdb.zip
  format: Geodatabase
  id: resource_638122b5
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240603LKA_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent in North Western Province, Sri Lanka
    as of 04 June 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3873/FL20240603LKA_SHP.zip
  format: null
  id: resource_4157733a
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240603LKA_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-lka_unosat_detectedwaterextentnorthw_20240606
spatial:
  bbox: null
  centroid: null
  countries:
  - LKA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-06-06'
temporal_resolution: null
title: Satellite detected water extent in North Western Province, Sri Lanka as of
  04 June 2024
version: null
vulnerability: null
---
