---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Mobile Accord, Inc. (GeoPoll)
  url: https://data.humdata.org/dataset/mozambique-cyclone-idai-data
creator:
  affiliation: null
  email: null
  name: Mobile Accord, Inc. (GeoPoll)
  url: https://data.humdata.org/dataset/mozambique-cyclone-idai-data
dataset_id: rdls_lss-moz_geopoll_cycloneidaidata_20190321
description: 'This dataset includes 700 completed interviews from Mozambique following
  Cyclone Idai, including respondents from Sofala province and Beira. All respondents
  were affected by the cyclone, and data includes information on home and community
  damages, food security, and access to resources including clean water and electricity.
  Data was collected via remote SMS survey March 21st, 2019 - March 22nd 2019 and
  is not nationally or regionally representative but is intended to show a snapshot
  of the cyclone''s impact on the ground. Statistical disclosure control methods have
  been applied to the data in order to protect individual respondents information..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/mozambique-cyclone-idai-data]'
details: This data was collected via remote SMS survey following Cyclone Idai and
  is not intended to be fully representative of the situation or population, but provides
  a snapshot view based on those who were able to be reached via SMS.
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Post-event impact data collected via remote SMS survey from 700 affected
    respondents in Mozambique within 2 days of Cyclone Idai landfall. Survey captured
    self-reported damages to homes and communities, food security status, and access
    disruptions to water and electricity. Statistical disclosure control methods were
    applied to anonymize individual responses for this snapshot assessment of cyclone
    impacts.
  sources:
  - id: source_1
    license: null
    name: Mobile Accord, Inc. (GeoPoll)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/mozambique-cyclone-idai-data
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct home and community damage from Cyclone Idai
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: Loss of access to clean water and electricity infrastructure
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_2
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
  - asset_category: economic_indicator
    asset_dimension: index
    description: Food security impacts and resource access disruption
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_3
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
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
purpose: Sample Survey
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This dataset includes 700 completed interviews from Mozambique following
    Cyclone Idai, including respondents from Sofala province and Beira. Data was collected
    via SMS and is not regionally or nationally representative. Non-perturbative statistical
    disclosure control methods have been applied to the data in order to protect individual
    respondents information. Hence, the detail in the data has been reduced without
    distorting the structure.
  download_url: https://data.humdata.org/dataset/44e9264a-5efb-4c96-873a-2735a65c0363/resource/8ab6219b-52c5-4c22-966a-b376d808598f/download/anonymized_geopoll_mozambique_cyclone_data_round1_final_dataset.xlsx
  format: null
  id: resource_8ab6219b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: anonymized_geopoll_mozambique_cyclone_data_round1_final_dataset.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-moz_geopoll_cycloneidaidata_20190321
spatial:
  bbox: null
  centroid: null
  countries:
  - MOZ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2019-03-21'
temporal_resolution: null
title: Mozambique Cyclone Idai Data
version: null
vulnerability: null
---
