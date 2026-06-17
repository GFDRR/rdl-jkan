---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-2 satellite imagery
    url: https://data.humdata.org/dataset/satellite-detected-water-extent-in-al-hodeidah-governorate-yemen-as-of-07-august-2024
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop population data
    url: https://data.humdata.org/dataset/satellite-detected-water-extent-in-al-hodeidah-governorate-yemen-as-of-07-august-2024
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-in-al-hodeidah-governorate-yemen-as-of-07-august-2024
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-in-al-hodeidah-governorate-yemen-as-of-07-august-2024
dataset_id: rdls_he-yem_unosat_detectedwaterextentalhode_20240812
description: "UNOSAT code: FL20240812YEM This map illustrates satellite-detected water\
  \ extent in Al Hodeidah Governorate, Yemen as observed from a Sentinel-2 satellite\
  \ image acquired on 07 August 2024 at 10:59 local time . Within the cloud free analysed\
  \ areas of about 20,000 km\xB2, a total of about 450 km\xB2 of lands appear to be\
  \ affected with flood waters. Based on Worldpop population data and the flood extent,\
  \ approximately 170,000 people are potentially exposed or living close to flooded\
  \ areas. This is a preliminary analysis and has not yet been validated in the field.\
  \ Please send ground feedback to the United Nations Satellite Centre (UNOSAT)..\
  \ [Source: This metadata record was automatically extracted from the Humanitarian\
  \ Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extent-in-al-hodeidah-governorate-yemen-as-of-07-august-2024]"
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
    description: Population potentially exposed or living close to flooded areas,
      estimated at approximately 170,000 people based on WorldPop data
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
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: "UNOSAT analysts reviewed Sentinel-2 satellite imagery acquired on\
    \ 07 August 2024 and performed visual change detection analysis to delineate flood\
    \ water extent across cloud-free areas of approximately 20,000 km\xB2 in Al Hodeidah\
    \ Governorate. The detected inundation extent (450 km\xB2) was then intersected\
    \ with WorldPop gridded population data to estimate population exposure. This\
    \ is a preliminary post-event assessment not yet validated in the field."
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
- href: https://data.humdata.org/dataset/satellite-detected-water-extent-in-al-hodeidah-governorate-yemen-as-of-07-august-2024
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
  description: Satellite detected water extent in Al Hodeidah Governorate, Yemen as
    of 07 August 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3908/FL20240812YEM_gdb.zip
  format: Geodatabase
  id: resource_9d88af12
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240812YEM_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent in Al Hodeidah Governorate, Yemen as
    of 07 August 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3908/FL20240812YEM_SHP.zip
  format: null
  id: resource_48a49801
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240812YEM_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent in Al Hodeidah Governorate, Yemen as
    of 07 August 2024 (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3908/UNOSAT_Population_Exposure_FL20240812YEM_AlHodeidahGovernorate_07Aug2024.xlsx
  format: null
  id: resource_c6cfbb8e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_Population_Exposure_FL20240812YEM_AlHodeidahGovernorate_07Aug2024.xlsx
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-yem_unosat_detectedwaterextentalhode_20240812
spatial:
  bbox: null
  centroid: null
  countries:
  - YEM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-08-12'
temporal_resolution: null
title: Satellite detected water extent in Al Hodeidah Governorate, Yemen as of 07
  August 2024
version: null
vulnerability: null
---
