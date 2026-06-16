---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: iMMAP Inc.
  url: https://data.humdata.org/dataset/population-monitoring-initiative-november-2017-dataset
creator:
  affiliation: null
  email: null
  name: iMMAP Inc.
  url: https://data.humdata.org/dataset/population-monitoring-initiative-november-2017-dataset
dataset_id: rdls_lss-syr_immap_populationmonitoringiniti_201711
description: 'The November 2017 dataset of the iMMAP Population Monitoring Initiative
  for South Syria.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/population-monitoring-initiative-november-2017-dataset]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Census-based enumeration of internally displaced populations in South
    Syria conducted by iMMAP in November 2017, providing direct counts of displacement
    impacts from conflict.
  sources:
  - id: source_1
    license: null
    name: iMMAP Inc.
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/population-monitoring-initiative-november-2017-dataset
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons monitored through population census
      in South Syria
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
purpose: Census
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Syrian Arab Republic - Population Monitoring Initiative - November
    2017 (Excel)
  download_url: https://data.humdata.org/dataset/d920e1a6-c68e-4a9b-a855-07b2cdf1be2c/resource/e76d2db0-246d-4474-8909-dc9f4c2ed55b/download/pmi_ssyria_master_dataset_nov_2017_public_final.xlsx
  format: null
  id: resource_e76d2db0
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PMI_SSyria_Master_Dataset_Nov_2017_Public_Final.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-syr_immap_populationmonitoringiniti_201711
spatial:
  bbox: null
  centroid: null
  countries:
  - SYR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2017-11-19'
  start: '2017-11-15'
temporal_resolution: null
title: Syrian Arab Republic - Population Monitoring Initiative - November 2017
version: null
vulnerability: null
---
