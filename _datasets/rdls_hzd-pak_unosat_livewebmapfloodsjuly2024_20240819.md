---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/unosat-live-webmap-floods-in-pakistan-july-2024
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-live-webmap-floods-in-pakistan-july-2024
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-live-webmap-floods-in-pakistan-july-2024
dataset_id: rdls_hzd-pak_unosat_livewebmapfloodsjuly2024_20240819
description: 'UNOSAT code: FL20240804PAK This application provides cumulative satellite-detected
  water using VIIRS in Pakistan from July 2024 based on NOAA-20 [VIIRS] data.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/unosat-live-webmap-floods-in-pakistan-july-2024]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure: []
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
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts processed NOAA-20 VIIRS satellite imagery from July
    2024, comparing multiple temporal images to detect notable changes in water extent.
    Satellite-detected water polygons were classified by confidence level and validated
    against field observations, then compiled into geodatabase and shapefile formats
    with metadata on sensor, date, and validation status.
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
- href: https://data.humdata.org/dataset/unosat-live-webmap-floods-in-pakistan-july-2024
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
  description: UNOSAT Live webmap, Floods in Pakistan, July 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3917/FL20240804PAK_gdb.zip
  format: Geodatabase
  id: resource_de84fa78
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240804PAK_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: UNOSAT Live webmap, Floods in Pakistan, July 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3917/FL20240804PAK_SHP.zip
  format: null
  id: resource_5df4d731
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240804PAK_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-pak_unosat_livewebmapfloodsjuly2024_20240819
spatial:
  bbox: null
  centroid: null
  countries:
  - PAK
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-08-19'
temporal_resolution: null
title: UNOSAT Live webmap, Floods in Pakistan, July 2024
version: null
vulnerability: null
---
