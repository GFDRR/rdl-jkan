---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Somalia
  url: https://data.humdata.org/dataset/somalia-flood-may-2018
creator:
  affiliation: null
  email: null
  name: OCHA Somalia
  url: https://data.humdata.org/dataset/somalia-flood-may-2018
dataset_id: rdls_lss-som_ochasom_floodmay2018_20180514
description: 'Number of people affected in a district level.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/somalia-flood-may-2018]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: District-level census data aggregating the number of people affected
    by the May 2018 flood event in Somalia, compiled by OCHA Somalia from post-event
    impact assessments.
  sources:
  - id: source_1
    license: null
    name: OCHA Somalia
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/somalia-flood-may-2018
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Total population affected by flooding at district level
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
purpose: Census
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia flood - May 2018 (Number of people affected in a district level.)
  download_url: https://docs.google.com/spreadsheets/d/e/2PACX-1vTwCdz-isFqHIqIZjGN1Rm_JdOjXhZIINhQ_jorshyTg2J2_-AKr1WIbfu6TiXo1rFR337qP_MWhmBS/pub?gid=0&single=true&output=csv
  format: null
  id: resource_25b04cb5
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia flood - people affected per district
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-som_ochasom_floodmay2018_20180514
spatial:
  bbox: null
  centroid: null
  countries:
  - SOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-05-14'
temporal_resolution: null
title: Somalia flood - May 2018
version: null
vulnerability: null
---
