---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sudan Humanitarian Aid Commission, Flood Task Force
    url: https://data.humdata.org/dataset/sudan-flood-affected-people-from-2013-to-2020
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Sudan
  url: https://data.humdata.org/dataset/sudan-flood-affected-people-from-2013-to-2020
creator:
  affiliation: null
  email: null
  name: OCHA Sudan
  url: https://data.humdata.org/dataset/sudan-flood-affected-people-from-2013-to-2020
dataset_id: rdls_lss-sdn_ochasdn_floodaffectedpeople201320_20201110
description: 'This data is showing the number of affected people by floods per year
  from 2013 to 2020. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/sudan-flood-affected-people-from-2013-to-2020]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Annual flood impact data collected through direct observation and anecdotal
    reporting by the Sudan Humanitarian Aid Commission and Flood Task Force, aggregated
    by year from 2013 to 2020 to document the number of people affected by flood events
    across Sudan.
  sources:
  - id: source_1
    license: null
    name: Sudan Humanitarian Aid Commission, Flood Task Force
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/sudan-flood-affected-people-from-2013-to-2020
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Annual count of people affected by floods in Sudan from 2013 to 2020
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
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flood affected people from 2013 to 2020 across Sudan, with different
    states. Only 2014 is missing.
  download_url: https://data.humdata.org/dataset/d80d6da2-a634-4d2a-9dc8-6f73804dbf3e/resource/ab735cf3-4633-477c-a17a-b470e6c4bd8b/download/floods-affected-people_sudan_2013-to-2020.xlsx
  format: null
  id: resource_ab735cf3
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Floods-Affected-People_Sudan_2013-to-2020.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-sdn_ochasdn_floodaffectedpeople201320_20201110
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
  start: '2020-11-10'
temporal_resolution: null
title: Sudan - Flood Affected People from 2013 to 2020
version: null
vulnerability: null
---
