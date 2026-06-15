---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Sudan
  url: https://data.humdata.org/dataset/sudan-flood-affected-people-from-2013-to-2021
creator:
  affiliation: null
  email: null
  name: OCHA Sudan
  url: https://data.humdata.org/dataset/sudan-flood-affected-people-from-2013-to-2021
dataset_id: rdls_lss-sdn_ochasdn_floodaffectedpeople201320_2020
description: 'Flood affected people in Sudan by state for the last few years.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/sudan-flood-affected-people-from-2013-to-2021]'
details: null
exposure: []
hazard: null
license: https://opendatacommons.org/licenses/odbl/1-0/
lineage:
  description: Flood-affected population data compiled from administrative records
    and humanitarian assessments by OCHA Sudan covering the period 2013-2021, aggregated
    by state to document direct impacts from flood events.
  sources:
  - id: source_1
    license: null
    name: OCHA Sudan
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/sudan-flood-affected-people-from-2013-to-2021
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Direct affected population from flooding events in Sudan by state
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
purpose: Registry
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Sudan Flood Affected people from 2013 to 2021 (Excel)
  download_url: https://data.humdata.org/dataset/8c932626-54ba-4f0e-a016-6dcea1da1d9f/resource/2ede2be1-e598-4ebc-9d4a-1909f685ad51/download/floods-affected-people_sudan_2013-to-2021.xlsx
  format: null
  id: resource_2ede2be1
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: floods-affected-people_sudan_2013-to-2021.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-sdn_ochasdn_floodaffectedpeople201320_2020
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
  end: '2021-10-11'
  start: '2020-10-11'
temporal_resolution: null
title: Sudan Flood Affected people from 2013 to 2021
version: null
vulnerability: null
---
