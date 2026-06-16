---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-extents-between-29-december-2023-and-2-january-2024-over-republic-of-congo
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/water-extents-between-29-december-2023-and-2-january-2024-over-republic-of-congo
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-between-29-december-2023-and-2-january-2024-over-republic-of-congo
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-between-29-december-2023-and-2-january-2024-over-republic-of-congo
dataset_id: rdls_he-cog_unosat_detectedwaterextentsbetwe_20240108
description: 'UNOSAT code: FL20240102COG This map illustrates cumulative satellite-detected
  minimum floodwater using VIIRS in Republic of Congo between 29 December 2023 and
  2 January 2024. Within the cloud free analysed area of about 330,000 km2, a total
  of about 1,000 km2 of lands appear to be affected with flood waters. Based on Worldpop
  population data and the minimum flood water coverage, ~114,000 people are potentially
  exposed or living close to flooded areas. This is a preliminary analysis and has
  not yet been validated in the field. Please provide ground feedback to the United
  Nations Satellite Centre (UNOSAT). Important note: Minimum floodwater extent indicates
  the portion of the pixel (375m) covered by 80 to 100% of flood water.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/water-extents-between-29-december-2023-and-2-january-2024-over-republic-of-congo]'
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
    description: Population potentially exposed or living close to satellite-detected
      flooded areas based on WorldPop data
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
  event_sets_by_hazard_type:
    flood:
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
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts compared VIIRS satellite imagery acquired between 29
    December 2023 and 2 January 2024 to detect cumulative floodwater extent through
    visual interpretation of notable changes. Detected water areas (~1,000 km2) were
    intersected with WorldPop population data to estimate ~114,000 people potentially
    exposed to flooded areas. This is preliminary post-event observed hazard data
    not yet validated in the field.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
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
- href: https://data.humdata.org/dataset/water-extents-between-29-december-2023-and-2-january-2024-over-republic-of-congo
  rel: source
loss:
  losses: []
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
  description: Satellite detected water extents between 29 December 2023 and 2 January
    2024 over Republic of Congo (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3783/FL20240102COG_gdb.zip
  format: Geodatabase
  id: resource_6b52cf61
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240102COG_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents between 29 December 2023 and 2 January
    2024 over Republic of Congo (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3783/FL20240102COG_SHP.zip
  format: null
  id: resource_63a9ee8f
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240102COG_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents between 29 December 2023 and 2 January
    2024 over Republic of Congo (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3783/UNOSAT_Population_Exposure_FL20230102COG_29Dec2023_02Jan2024_Congo%20(1).xlsx
  format: null
  id: resource_d8fe0dd8
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_Population_Exposure_FL20230102COG_29Dec2023_02Jan2024_Congo (1).xlsx
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-cog_unosat_detectedwaterextentsbetwe_20240108
spatial:
  bbox: null
  centroid: null
  countries:
  - COG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-01-08'
temporal_resolution: null
title: Satellite detected water extents between 29 December 2023 and 2 January 2024
  over Republic of Congo
version: null
vulnerability: null
---
