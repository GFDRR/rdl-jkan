---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-25-and-29-april-2025-over-south-sudan
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-25-and-29-april-2025-over-south-sudan
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-25-and-29-april-2025-over-south-sudan
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-25-and-29-april-2025-over-south-sudan
dataset_id: rdls_he-ssd_unosat_detectedwaterextentsbetwe_20250501
description: "UNOSAT code: FL20250110SSD This map illustrates cumulative satellite-detected\
  \ water using VIIRS in South Sudan between 25 to 29 April 2025 compared with the\
  \ period from 15 to 19 March 2025 . Within the cloud free analysed areas of about\
  \ 620,000 km\xB2, a total of about 11,000 km\xB2 of lands appear to be affected\
  \ with flood waters. Water extent appears to have decreased of about 10,600 km\xB2\
  \ since the period between 15 to 19 March 2025 within the cloud free analysed areas.\
  \ Based on Worldpop population data and the maximal flood water extent ~180,000\
  \ people are potentially exposed or living close to flooded areas. This is a preliminary\
  \ analysis and has not yet been validated in the field. Please send ground feedback\
  \ to the United Nations Satellite Centre (UNOSAT).. [Source: This metadata record\
  \ was automatically extracted from the Humanitarian Data Exchange (HDX); Original\
  \ dataset: https://data.humdata.org/dataset/satellite-detected-water-extents-between-25-and-29-april-2025-over-south-sudan]"
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
    description: Population potentially exposed to flood waters based on WorldPop
      data and maximal flood extent
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
  description: UNOSAT analysts compared VIIRS satellite imagery from 25-29 April 2025
    with baseline imagery from 15-19 March 2025 to detect cumulative water extents
    across cloud-free areas of South Sudan. Population exposure was estimated by intersecting
    the maximal flood water extent with WorldPop gridded population data to quantify
    potentially affected populations.
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
- href: https://data.humdata.org/dataset/satellite-detected-water-extents-between-25-and-29-april-2025-over-south-sudan
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
  description: Satellite detected water extents between 25 and 29 April 2025 over
    South Sudan (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4126/FL20220424SSD_gdb.zip
  format: Geodatabase
  id: resource_12c64616
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20220424SSD_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents between 25 and 29 April 2025 over
    South Sudan (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4126/FL20220424SSD_SHP.zip
  format: null
  id: resource_1c26e66e
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20220424SSD_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents between 25 and 29 April 2025 over
    South Sudan (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/4126/UNOSAT_Population_Exposure_FL20250110SSD_25Apr_29Apr2025_SouthSudan_Week37.xlsx
  format: null
  id: resource_c924456b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_Population_Exposure_FL20250110SSD_25Apr_29Apr2025_SouthSudan_Week37.xlsx
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-ssd_unosat_detectedwaterextentsbetwe_20250501
spatial:
  bbox: null
  centroid: null
  countries:
  - SSD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-05-01'
temporal_resolution: null
title: Satellite detected water extents between 25 and 29 April 2025 over South Sudan
version: null
vulnerability: null
---
