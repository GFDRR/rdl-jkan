---
attributions:
- entity:
    affiliation: null
    email: null
    name: Government of Ukraine
    url: https://data.humdata.org/dataset/ukraine-idps
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: OCHA and Humanitarian Partners
    url: https://data.humdata.org/dataset/ukraine-idps
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Ukraine
  url: https://data.humdata.org/dataset/ukraine-idps
creator:
  affiliation: null
  email: null
  name: OCHA Ukraine
  url: https://data.humdata.org/dataset/ukraine-idps
dataset_id: rdls_lss-ukr_ochaukr_internallydisplacedperson_20210215
description: 'These figures were endorsed as the baseline figure of IDPs residing
  in government-controlled areas (GCAs) in 2020 by OCHA and other humanitarian partners
  in the Humanitarian Needs Overview for Ukraine for 2021.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/ukraine-idps]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: IDP displacement figures were compiled from Government of Ukraine registration
    records (1.5 million baseline) and endorsed by OCHA and humanitarian partners
    as the official baseline for IDPs in government-controlled areas in 2020, incorporated
    into the 2021 Humanitarian Needs Overview.
  sources:
  - id: source_1
    license: null
    name: Government of Ukraine
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: OCHA and Humanitarian Partners
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/ukraine-idps
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons from conflict in Ukraine residing in
      government-controlled areas
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
        metric: displaced
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
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Ukraine: Internally Displaced Persons (UA-IDPs (2021 HNO).xlsx)'
  download_url: https://data.humdata.org/dataset/4304319f-db3b-485f-9ec9-c3bf288d95cc/resource/b5bda083-b26c-49a6-9aa4-f476f19f17d0/download/2021-06-29-idps.xlsx
  format: null
  id: resource_b5bda083
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UA-IDPs (2021 HNO).xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ukr_ochaukr_internallydisplacedperson_20210215
spatial:
  bbox: null
  centroid: null
  countries:
  - UKR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2021-02-15'
temporal_resolution: null
title: 'Ukraine: Internally Displaced Persons'
version: null
vulnerability: null
---
