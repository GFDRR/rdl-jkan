---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/waters-extent-in-el-salam-el-jabalain-districts-white-nile-state-sudan-as-of-11-september-
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/waters-extent-in-el-salam-el-jabalain-districts-white-nile-state-sudan-as-of-11-september-
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/waters-extent-in-el-salam-el-jabalain-districts-white-nile-state-sudan-as-of-11-september-
dataset_id: rdls_hl-sdn_unosat_detectedwatersextentelsal_20220914
description: "UNOSAT code FL20220816SDN This map illustrates satellite-detected surface\
  \ waters in El Salan & El Jabalain districts, White Nile State as observed from\
  \ a RCM-3 image acquired on 11 September 2022. Within the analyzed area of about\
  \ 200 km\xB2, about 17 km\xB2 of lands appear to be flooded. Water extent appears\
  \ to have decreased of about 13 km\xB2 since the 04 September 2022. Flood waters\
  \ are observed in the vicinity of Alagaya refugee camp as of 11 September 2022.\
  \ Kilo Arba refugee camp appears to be affected by floods as of 11 September 2022.\
  \ This is a preliminary analysis and has not yet been validated in the field. Please\
  \ send ground feedback to United Nations Satellite Centre (UNOSAT).. [Source: This\
  \ metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/waters-extent-in-el-salam-el-jabalain-districts-white-nile-state-sudan-as-of-11-september-]"
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "UNOSAT analysts processed RCM-3 satellite imagery acquired on 11 September\
    \ 2022, comparing it with imagery from 04 September 2022 to detect changes in\
    \ surface water extent. Water bodies were delineated and quantified within a 200\
    \ km\xB2 study area covering El Salam and El Jabalain districts, White Nile State,\
    \ Sudan, producing vector geometries of flooded areas with area measurements."
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
- href: https://data.humdata.org/dataset/waters-extent-in-el-salam-el-jabalain-districts-white-nile-state-sudan-as-of-11-september-
  rel: source
loss:
  losses:
  - asset_category: natural_environment
    asset_dimension: product
    description: "Direct flood extent impact on land surface, with approximately 17\
      \ km\xB2 of flooded area detected"
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
          quantity_kind: area
          unit: null
        metric: loss
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
  description: Satellite detected waters extent in El Salam & El Jabalain districts,
    White Nile State, Sudan as of 11 September 2022 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3353/FL20220816SDN_gdb.zip
  format: Geodatabase
  id: resource_a2c9ca24
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20220816SDN_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected waters extent in El Salam & El Jabalain districts,
    White Nile State, Sudan as of 11 September 2022 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3353/FL20220816SDN_SHP.zip
  format: null
  id: resource_76e58d40
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20220816SDN_SHP.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-sdn_unosat_detectedwatersextentelsal_20220914
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
  start: '2022-09-14'
temporal_resolution: null
title: Satellite detected waters extent in El Salam & El Jabalain districts, White
  Nile State, Sudan as of 11 September 2022
version: null
vulnerability: null
---
