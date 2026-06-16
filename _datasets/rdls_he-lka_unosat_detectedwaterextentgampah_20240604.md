---
attributions:
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/water-extent-in-gampaha-colombo-and-kalutara-districts-western-province-as-of-04-june-2024
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Sentinel-1
    url: https://data.humdata.org/dataset/water-extent-in-gampaha-colombo-and-kalutara-districts-western-province-as-of-04-june-2024
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-gampaha-colombo-and-kalutara-districts-western-province-as-of-04-june-2024
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-gampaha-colombo-and-kalutara-districts-western-province-as-of-04-june-2024
dataset_id: rdls_he-lka_unosat_detectedwaterextentgampah_20240604
description: "UNOSAT code: FL20240603LKA, GDACS ID: 1102660 This map illustrates satellite-detected\
  \ water extent in Gampaha, Colombo and Kalutara Districts, Western Province, Sri\
  \ Lanka as observed from a Sentinel-1 image acquired on 04 June 2024 at 00:25 UTC.\
  \ Within the analysed areas of about 8,000 km\xB2, a total of about 124 km\xB2 of\
  \ lands appear to be affected with flood waters. Based on WorldPop population data\
  \ and the flood extent about 100,000 people are potentially exposed. This is a preliminary\
  \ analysis and has not yet been validated in the field. Please send ground feedback\
  \ to the United Nations Satellite Centre (UNOSAT). Important note: Flood analysis\
  \ from radar images may underestimate the presence of standing waters in built-up\
  \ areas and densely vegetated areas due to backscattering properties of the radar\
  \ signal.. [Source: This metadata record was automatically extracted from the Humanitarian\
  \ Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-in-gampaha-colombo-and-kalutara-districts-western-province-as-of-04-june-2024]"
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
    description: Potentially exposed population derived from WorldPop data intersected
      with satellite-detected flood extent, approximately 100,000 people
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
      process: pluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: "Satellite-detected water extent was derived from Sentinel-1 SAR imagery\
    \ acquired on 04 June 2024 through manual analyst interpretation and comparison\
    \ of satellite images to identify notable changes. The flood extent polygon (124\
    \ km\xB2) was then intersected with WorldPop gridded population data to estimate\
    \ approximately 100,000 potentially exposed people in the three districts of Western\
    \ Province, Sri Lanka."
  sources:
  - id: source_1
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: Sentinel-1
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/water-extent-in-gampaha-colombo-and-kalutara-districts-western-province-as-of-04-june-2024
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
  description: Sri Lanka - Satellite detected water extent in Gampaha, Colombo and
    Kalutara Districts, Western Province as of 04 June 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3868/FL20240603LKA_gdb.zip
  format: Geodatabase
  id: resource_4cbe355b
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
  description: Sri Lanka - Satellite detected water extent in Gampaha, Colombo and
    Kalutara Districts, Western Province as of 04 June 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3868/FL20240603LKA_SHP.zip
  format: null
  id: resource_b9b45a82
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240603LKA_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Sri Lanka - Satellite detected water extent in Gampaha, Colombo and
    Kalutara Districts, Western Province as of 04 June 2024 (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3868/UNOSAT_Population_Exposure_FL20240603LKA_WestSriLanka_06June2024.xlsx
  format: null
  id: resource_796c01dc
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_Population_Exposure_FL20240603LKA_WestSriLanka_06June2024.xlsx
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-lka_unosat_detectedwaterextentgampah_20240604
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
  start: '2024-06-04'
temporal_resolution: null
title: Sri Lanka - Satellite detected water extent in Gampaha, Colombo and Kalutara
  Districts, Western Province as of 04 June 2024
version: null
vulnerability: null
---
