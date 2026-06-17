---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/satellite-detected-water-extent-in-juba-hoose-region-somalia-as-of-07-november-2023
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-in-juba-hoose-region-somalia-as-of-07-november-2023
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-in-juba-hoose-region-somalia-as-of-07-november-2023
dataset_id: rdls_hzd-som_unosat_detectedwaterextentjubaho_20231108
description: "UNOSAT code FL20231105SOM This map illustrates satellite-detected surface\
  \ waters in Jilib District, Juba Dhexe & Afmadow Jamaame District, Juba Hoose Region,\
  \ Somalia as observed from a Sentinel-1 image acquired on 07 November 2023 at 02:54\
  \ UTC. Within the analysed area of about 7,300 km\xB2, about 60 km\xB2 of land appear\
  \ to be flooded. This is a preliminary analysis and has not yet been validated in\
  \ the field. Please send ground feedback to United Nations Satellite Centre (UNOSAT).\
  \ Important note: Flood analysis from radar images may underestimate the presence\
  \ of standing waters in built-up areas and densely vegetated areas due to backscattering\
  \ properties of the radar signal.. [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extent-in-juba-hoose-region-somalia-as-of-07-november-2023]"
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
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: "UNOSAT analysts processed Sentinel-1 SAR imagery acquired on 07 November\
    \ 2023 over Juba Hoose Region, Somalia, applying change detection and visual interpretation\
    \ methods to identify surface water extent. The analysis delineated approximately\
    \ 60 km\xB2 of flooded area within a 7,300 km\xB2 study area covering Jilib, Juba\
    \ Dhexe, Afmadow, and Jamaame districts. This is a preliminary post-event observation\
    \ not yet validated in the field."
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
- href: https://data.humdata.org/dataset/satellite-detected-water-extent-in-juba-hoose-region-somalia-as-of-07-november-2023
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
  description: Satellite detected water extent in Juba Hoose Region, Somalia as of
    07 November 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3729/FL20231105SOM_gdb.zip
  format: Geodatabase
  id: resource_04567cb0
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20231105SOM_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent in Juba Hoose Region, Somalia as of
    07 November 2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3729/FL20231105SOM_SHP.zip
  format: null
  id: resource_900fbec4
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20231105SOM_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-som_unosat_detectedwaterextentjubaho_20231108
spatial:
  bbox: null
  centroid: null
  countries:
  - SOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-11-08'
temporal_resolution: null
title: Satellite detected water extent in Juba Hoose Region, Somalia as of 07 November
  2023
version: null
vulnerability: null
---
