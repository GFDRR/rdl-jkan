---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-extent-in-el-geneina-deparment-west-darfur-state-sudan-as-of-25-september-2024
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-el-geneina-deparment-west-darfur-state-sudan-as-of-25-september-2024
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-el-geneina-deparment-west-darfur-state-sudan-as-of-25-september-2024
dataset_id: rdls_hzd-sdn_unosat_detectedwaterextentelgene_20240927
description: "UNOSAT code: FL20240924SDN This map illustrates satellite-detected water\
  \ extent in El Geneina Department, West Darfur State, Sudan as observed from a Pl\xE9\
  iades image acquired on 25 September 2024 at 11:46 local time. Within the cloud\
  \ free analysed area of about 20,000ha, a total of about 8050ha of lands appear\
  \ to be affected with flood waters. This is a preliminary analysis and has not yet\
  \ been validated in the field. Please send ground feedback to the United Nations\
  \ Satellite Centre (UNOSAT).. [Source: This metadata record was automatically extracted\
  \ from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-in-el-geneina-deparment-west-darfur-state-sudan-as-of-25-september-2024]"
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
  description: "UNOSAT analysts processed a Pl\xE9iades satellite image acquired on\
    \ 25 September 2024 over El Geneina Department, comparing cloud-free areas (20,000\
    \ ha) to detect water extent changes and delineate flood-affected zones. The resulting\
    \ water extent polygons with area measurements represent observed hazard extent\
    \ from a single post-event satellite acquisition."
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
- href: https://data.humdata.org/dataset/water-extent-in-el-geneina-deparment-west-darfur-state-sudan-as-of-25-september-2024
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
  description: Satellite detected water extent in El Geneina Deparment, West Darfur
    State, Sudan as of 25 September 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3982/FL20240924SDN_gdb.zip
  format: Geodatabase
  id: resource_bfe8897d
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240924SDN_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent in El Geneina Deparment, West Darfur
    State, Sudan as of 25 September 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3982/FL20240924SDN_SHP.zip
  format: null
  id: resource_29dceb26
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240924SDN_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-sdn_unosat_detectedwaterextentelgene_20240927
spatial:
  bbox: null
  centroid: null
  countries:
  - SDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-09-27'
temporal_resolution: null
title: Satellite detected water extent in El Geneina Deparment, West Darfur State,
  Sudan as of 25 September 2024
version: null
vulnerability: null
---
