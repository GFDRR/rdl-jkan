---
attributions:
- entity:
    affiliation: null
    email: null
    name: VIIRS satellite imagery
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-01-and-05-february-2025-over-south-sudan
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop population data
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-01-and-05-february-2025-over-south-sudan
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-01-and-05-february-2025-over-south-sudan
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-01-and-05-february-2025-over-south-sudan
dataset_id: rdls_hel-ssd_unosat_detectedwaterextentsbetwe_20250206
description: "UNOSAT code: FL20250110SSD This map illustrates cumulative satellite-detected\
  \ water using VIIRS in South Sudan between 01 to 05 February 2025 compared with\
  \ the period from 18 to 22 January 2025 . Within the cloud free analysed areas of\
  \ about 630,000 km\xB2, a total of about 38,000 km\xB2 of lands appear to be affected\
  \ with flood waters. Water extent appears to have decreased of about 4,000 km\xB2\
  \ since the period between 18 to 22 January 2025 within the cloud free analysed\
  \ areas. Based on Worldpop population data and the maximal flood water extent ~605,000\
  \ people are potentially exposed or living close to flooded areas. This is a preliminary\
  \ analysis and has not yet been validated in the field. Please send ground feedback\
  \ to the United Nations Satellite Centre (UNOSAT).. [Source: This metadata record\
  \ was automatically extracted from the Humanitarian Data Exchange (HDX); Original\
  \ dataset: https://data.humdata.org/dataset/satellite-detected-water-extents-between-01-and-05-february-2025-over-south-sudan]"
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "UNOSAT analysts processed VIIRS satellite imagery from 01-05 February\
    \ 2025 and compared it with baseline imagery from 18-22 January 2025 to detect\
    \ cumulative water extents across South Sudan. The resulting water extent polygons\
    \ (38,000 km\xB2 affected area within 630,000 km\xB2 cloud-free analysis area)\
    \ were intersected with WorldPop population data to estimate approximately 605,000\
    \ potentially exposed people. Change analysis showed a 4,000 km\xB2 decrease in\
    \ water extent compared to the baseline period."
  sources:
  - id: source_1
    license: null
    name: VIIRS satellite imagery
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
- href: https://data.humdata.org/dataset/satellite-detected-water-extents-between-01-and-05-february-2025-over-south-sudan
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by satellite-detected flood water extent in South
      Sudan
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
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
  description: Satellite detected water extents between 01 and 05 February 2025 over
    South Sudan (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4074/FL20220424SSD_gdb.zip
  format: Geodatabase
  id: resource_225f8b3b
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
  description: Satellite detected water extents between 01 and 05 February 2025 over
    South Sudan (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4074/FL20220424SSD_SHP.zip
  format: null
  id: resource_fc4ad4c7
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
  description: Satellite detected water extents between 01 and 05 February 2025 over
    South Sudan (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/4074/UNOSAT_Population_Exposure_FL20250110SSD_01Feb_05Feb2025_SouthSudan_Week34.xlsx
  format: null
  id: resource_b3251cde
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_Population_Exposure_FL20250110SSD_01Feb_05Feb2025_SouthSudan_Week34.xlsx
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-ssd_unosat_detectedwaterextentsbetwe_20250206
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
  start: '2025-02-06'
temporal_resolution: null
title: Satellite detected water extents between 01 and 05 February 2025 over South
  Sudan
version: null
vulnerability: null
---
