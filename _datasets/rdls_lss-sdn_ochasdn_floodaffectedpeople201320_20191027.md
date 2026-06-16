---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Sudan
  url: https://data.humdata.org/dataset/sudan-flood-affected-people-from-2013-to-2019
creator:
  affiliation: null
  email: null
  name: OCHA Sudan
  url: https://data.humdata.org/dataset/sudan-flood-affected-people-from-2013-to-2019
dataset_id: rdls_lss-sdn_ochasdn_floodaffectedpeople201320_20191027
description: 'Flood affected people in Sudan by state for the last few years.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/sudan-flood-affected-people-from-2013-to-2019]'
details: null
exposure: []
hazard: null
license: ODbL-1.0/
lineage:
  description: Post-event flood impact data aggregated from multiple sources by OCHA
    Sudan, compiled into a state-level registry documenting affected population counts
    across Sudan from 2013 to 2019.
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
- href: https://data.humdata.org/dataset/sudan-flood-affected-people-from-2013-to-2019
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by flooding in Sudan by state from 2013 to 2019
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
purpose: Registry
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flood affected people from 2013 to 2019 across Sudan, with different
    states. Only 2014 is missing.
  download_url: https://data.humdata.org/dataset/74eafdd9-1be5-40bd-8ce0-1e103f0918d0/resource/1ef32c2a-0179-4528-b6a8-d06b51ef29dc/download/floods-affected-people_sudan_2013-to-2019.xlsx
  format: null
  id: resource_1ef32c2a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: floods-affected-people_Sudan_2013-to-2019.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-sdn_ochasdn_floodaffectedpeople201320_20191027
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
  start: '2019-10-27'
temporal_resolution: null
title: Sudan Flood Affected people from 2013 to 2019
version: null
vulnerability: null
---
