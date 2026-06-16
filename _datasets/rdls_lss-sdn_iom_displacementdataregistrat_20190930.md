---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
      (DTM)
    url: https://data.humdata.org/dataset/sudan-registration-data-iom-dtm
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/sudan-registration-data-iom-dtm
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/sudan-registration-data-iom-dtm
dataset_id: rdls_lss-sdn_iom_displacementdataregistrat_20190930
description: 'This dataset reflects the aggregation of the registration exercises
  conducted in Sudan since 2010, contains IDPs, households and Returnees by age and
  sex. All DTM registration and assessment exercises were jointly conducted in collaboration
  with Humanitarian Aid Commission (HAC).. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/sudan-registration-data-iom-dtm]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: IOM DTM conducted registration and assessment exercises in Sudan since
    2010 in collaboration with HAC, aggregating data on internally displaced persons,
    households, and returnees. The dataset captures displacement populations disaggregated
    by age and sex, representing post-displacement impact records from multiple hazard
    events.
  sources:
  - id: source_1
    license: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
      (DTM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/sudan-registration-data-iom-dtm
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons and returnees registered through DTM
      exercises, disaggregated by age and sex
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
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
  description: Aggregation of the registration exercises conducted in Sudan since
    2010. The dataset has individuals and households by gender and age dis-aggregated
    and return locations.
  download_url: https://data.humdata.org/dataset/132c64c2-53e6-4e45-8364-35bf4e22987f/resource/90ee46eb-ab51-4095-8c32-b9f8361364b5/download/dtm-sudan-registration.xlsx
  format: null
  id: resource_90ee46eb
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Sudan Registration
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-sdn_iom_displacementdataregistrat_20190930
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
  start: '2019-09-30'
temporal_resolution: null
title: Sudan Displacement Data - Registration [IOM DTM]
version: null
vulnerability: null
---
