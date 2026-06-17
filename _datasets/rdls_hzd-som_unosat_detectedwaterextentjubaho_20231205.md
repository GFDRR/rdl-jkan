---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-extent-in-juba-hoose-and-juba-dhexe-region-somalia-3-december-2023
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-juba-hoose-and-juba-dhexe-region-somalia-3-december-2023
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-juba-hoose-and-juba-dhexe-region-somalia-3-december-2023
dataset_id: rdls_hzd-som_unosat_detectedwaterextentjubaho_20231205
description: 'UNOSAT code: FL20231105SOM This map illustrates satellite-detected surface
  waters in Juba Hoose and Juba Dhexe Region, Somalia as observed from a Sentinel-2
  image acquired on 3 December 2023 at 07:39 UTC. Within the analysed area of about
  20,000 km2 about 1,300 km2 of land appears to be flooded. This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to United Nations Satellite Centre (UNOSAT).. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/water-extent-in-juba-hoose-and-juba-dhexe-region-somalia-3-december-2023]'
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
  description: "Sentinel-2 satellite imagery acquired on 3 December 2023 was analyzed\
    \ by UNOSAT analysts through visual interpretation and comparison with reference\
    \ imagery to detect and delineate surface water extent. The resulting water polygon\
    \ dataset represents observed flood extent at a single point in time across approximately\
    \ 20,000 km\xC2\xB2 in southern Somalia."
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
- href: https://data.humdata.org/dataset/water-extent-in-juba-hoose-and-juba-dhexe-region-somalia-3-december-2023
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
  description: Satellite detected water extent in Juba Hoose and Juba Dhexe Region,
    Somalia, 3 December 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3765/FL20231105SOM.gdb.zip
  format: Geodatabase
  id: resource_3f9f3dfb
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20231105SOM.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent in Juba Hoose and Juba Dhexe Region,
    Somalia, 3 December 2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3765/FL20231105SOM_SHP.zip
  format: null
  id: resource_c01b3bbb
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
slug: rdls_hzd-som_unosat_detectedwaterextentjubaho_20231205
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
  start: '2023-12-05'
temporal_resolution: null
title: Satellite detected water extent in Juba Hoose and Juba Dhexe Region, Somalia,
  3 December 2023
version: null
vulnerability: null
---
