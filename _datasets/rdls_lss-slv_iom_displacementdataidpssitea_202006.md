---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/el-salvador-displacement-data-idps-site-assessment-iom-dtm
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/el-salvador-displacement-data-idps-site-assessment-iom-dtm
dataset_id: rdls_lss-slv_iom_displacementdataidpssitea_202006
description: 'The dataset contains number of displaced persons by gender and age dis-aggregated.
  Dataset contains data on Covid-19, WASH, Shelter and other needs.. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/el-salvador-displacement-data-idps-site-assessment-iom-dtm]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: IOM DTM conducted site assessments at IDP settlements in El Salvador
    across two rounds, collecting displacement counts disaggregated by gender and
    age, along with associated humanitarian needs data (WASH, shelter, COVID-19 status).
    The dataset represents post-displacement impact records from IDP populations without
    explicit hazard triggering information.
  sources:
  - id: source_1
    license: null
    name: International Organization for Migration (IOM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/el-salvador-displacement-data-idps-site-assessment-iom-dtm
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons by gender and age from unspecified hazard
      triggers
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
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
  description: El Salvador Displacement Data - [IDPs] - Site Assessment [IOM DTM]
    (DTM El Salvador Site Assessment Round 2)
  download_url: https://data.humdata.org/dataset/c0a14c66-a782-45bd-8a7e-1a464167e9ea/resource/13243fb8-1679-496c-aa59-0edaf25dafe5/download/dtm-el-salvador-site-assessment-round-2.xlsx
  format: null
  id: resource_13243fb8
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM El Salvador Site Assessment Round 2
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: El Salvador Displacement Data - [IDPs] - Site Assessment [IOM DTM]
    (DTM El Salvador Site Assessment Round 1)
  download_url: https://data.humdata.org/dataset/c0a14c66-a782-45bd-8a7e-1a464167e9ea/resource/9915b5f5-a716-4701-b13c-72b4cdc2fef9/download/dtm-el-salvador-site-assessment-round-1.xlsx
  format: null
  id: resource_9915b5f5
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM El Salvador Site Assessment Round 1
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-slv_iom_displacementdataidpssitea_202006
spatial:
  bbox: null
  centroid: null
  countries:
  - SLV
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-06-20'
  start: '2020-06-17'
temporal_resolution: null
title: El Salvador Displacement Data - [IDPs] - Site Assessment [IOM DTM]
version: null
vulnerability: null
---
