---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-20-and-24-august-2024-over-chad
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-20-and-24-august-2024-over-chad
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-20-and-24-august-2024-over-chad
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-20-and-24-august-2024-over-chad
dataset_id: rdls_he-tcd_unosat_detectedwaterextentsbetwe_20240826
description: "UNOSAT code: FL20240820TCD This map illustrates cumulative satellite-detected\
  \ water using VIIRS in Chad between 20 to 24 August 2024. Within the cloud free\
  \ analysed areas of about 1,200,000 km\xB2, a total of about 18,900 km\xB2 of lands\
  \ appear to be affected with flood waters. Maximum flood water extent has remained\
  \ relatively stable, with a decrease of about 500 km\xB2 since the period between\
  \ 15 to 19 August 2024. Based on Worldpop population data and the maximum flood\
  \ water extent, ~170,000 people in Mayo-Kebbi Est Department, ~160,000 people in\
  \ Logone Oriental Department and ~120,000 people in Tandjil\xE9 This is a preliminary\
  \ analysis and has not yet been validated in the field. Please send ground feedback\
  \ to the United Nations Satellite Centre (UNOSAT).. [Source: This metadata record\
  \ was automatically extracted from the Humanitarian Data Exchange (HDX); Original\
  \ dataset: https://data.humdata.org/dataset/satellite-detected-water-extents-between-20-and-24-august-2024-over-chad]"
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
    description: Population exposed to flood waters in Mayo-Kebbi Est and Logone Oriental
      departments based on WorldPop data
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
license: CC-BY-SA-4.0
lineage:
  description: "UNOSAT analysts processed VIIRS satellite imagery from 20-24 August\
    \ 2024 to detect and delineate cumulative water extents across cloud-free areas\
    \ of Chad. Detected flood water polygons (18,900 km\xB2 total) were intersected\
    \ with WorldPop population grids to estimate affected populations by administrative\
    \ department, producing both spatial flood extent data and population exposure\
    \ metrics."
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
- href: https://data.humdata.org/dataset/satellite-detected-water-extents-between-20-and-24-august-2024-over-chad
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
  description: Satellite detected water extents between 20 and 24 August 2024 over
    Chad (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3928/FL20240820TCD_gdb.zip
  format: Geodatabase
  id: resource_fa86bc53
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240820TCD_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents between 20 and 24 August 2024 over
    Chad (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3928/FL20240820TCD_SHP.zip
  format: null
  id: resource_268d00da
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240820TCD_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents between 20 and 24 August 2024 over
    Chad (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3928/UNOSAT_Population_Exposure_FL20240820TCD_20Aug_24Aug2024_Chad.xlsx
  format: null
  id: resource_ae9e9959
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_Population_Exposure_FL20240820TCD_20Aug_24Aug2024_Chad.xlsx
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-tcd_unosat_detectedwaterextentsbetwe_20240826
spatial:
  bbox: null
  centroid: null
  countries:
  - TCD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-08-26'
temporal_resolution: null
title: Satellite detected water extents between 20 and 24 August 2024 over Chad
version: null
vulnerability: null
---
