---
attributions:
- entity:
    affiliation: null
    email: null
    name: Ethiopian Disaster Risk Management Commission (EDRMC)
    url: https://data.humdata.org/dataset/ethiopia-flood-response-monitoring
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Ethiopia
  url: https://data.humdata.org/dataset/ethiopia-flood-response-monitoring
creator:
  affiliation: null
  email: null
  name: OCHA Ethiopia
  url: https://data.humdata.org/dataset/ethiopia-flood-response-monitoring
dataset_id: rdls_lss-eth_ochaeth_floodresponsemonitoring_20220831
description: 'Flood events in 2022 and their impact on people.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/ethiopia-flood-response-monitoring]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Impact data on affected populations from 2022 flood events in Ethiopia
    were compiled by OCHA Ethiopia from regional reports submitted by the Ethiopian
    Disaster Risk Management Commission, aggregated at woreda (district) administrative
    level to create a flood response monitoring matrix.
  sources:
  - id: source_1
    license: null
    name: Ethiopian Disaster Risk Management Commission (EDRMC)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/ethiopia-flood-response-monitoring
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Affected population from flood events in 2022
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
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Ethiopia - Flood Response Monitoring (Excel)
  download_url: https://data.humdata.org/dataset/1d98ea41-12da-4894-957e-c173ae2d5cbb/resource/dedff8c3-065b-413d-9d01-2570e82d566b/download/flood-response-monitoring-matrix-august-2022-coded-woredas.xlsx
  format: null
  id: resource_dedff8c3
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: flood-response-monitoring-matrix-august-2022-coded-woredas.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-eth_ochaeth_floodresponsemonitoring_20220831
spatial:
  bbox: null
  centroid: null
  countries:
  - ETH
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-08-31'
temporal_resolution: null
title: Ethiopia - Flood Response Monitoring
version: null
vulnerability: null
---
