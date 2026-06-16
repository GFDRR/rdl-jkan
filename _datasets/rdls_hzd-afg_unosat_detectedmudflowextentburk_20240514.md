---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/mudflow-extent-in-burka-district-baghlan-province-afghanistan-as-of-14-may-2024
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/mudflow-extent-in-burka-district-baghlan-province-afghanistan-as-of-14-may-2024
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/mudflow-extent-in-burka-district-baghlan-province-afghanistan-as-of-14-may-2024
dataset_id: rdls_hzd-afg_unosat_detectedmudflowextentburk_20240514
description: "UNOSAT code: FL20240512AFG, GDACS ID: 1102616 This map illustrates satellite-detected\
  \ mudflow extent in Burka District, Baghlan Province, Afghanistan as observed from\
  \ a Pl\xE9iades image acquired on 14 May 2024 at 10:48 local time. Within the analysed\
  \ area of about 130 km\xB2, a total of about 18 km\xB2 of lands appear to be affected\
  \ by mudflow. This is a preliminary analysis and has not yet been validated in the\
  \ field. Please send ground feedback to the United Nations Satellite Centre (UNOSAT)..\
  \ [Source: This metadata record was automatically extracted from the Humanitarian\
  \ Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/mudflow-extent-in-burka-district-baghlan-province-afghanistan-as-of-14-may-2024]"
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
      intensity_measure: AA:km2
      process: landslide_mudflow
      trigger: null
      type: landslide
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: "UNOSAT analysts processed Pl\xE9iades satellite imagery acquired on\
    \ 14 May 2024 over Burka District, comparing pre- and post-event images to identify\
    \ and delineate mudflow-affected areas. The analysis identified approximately\
    \ 18 km\xB2 of mudflow extent within a 130 km\xB2 study area. Results were provided\
    \ as vector geodatabase and shapefile formats with confidence and validation metadata\
    \ fields."
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
- href: https://data.humdata.org/dataset/mudflow-extent-in-burka-district-baghlan-province-afghanistan-as-of-14-may-2024
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
  description: Satellite detected mudflow extent in Burka District, Baghlan Province,
    Afghanistan as of 14 May 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3842/FL20240512AFG_gdb.zip
  format: Geodatabase
  id: resource_0c38ed97
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240512AFG_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected mudflow extent in Burka District, Baghlan Province,
    Afghanistan as of 14 May 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3842/FL20240512AFG_SHP.zip
  format: null
  id: resource_5edd0935
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240512AFG_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-afg_unosat_detectedmudflowextentburk_20240514
spatial:
  bbox: null
  centroid: null
  countries:
  - AFG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-05-14'
temporal_resolution: null
title: Satellite detected mudflow extent in Burka District, Baghlan Province, Afghanistan
  as of 14 May 2024
version: null
vulnerability: null
---
