---
attributions:
- entity:
    affiliation: null
    email: null
    name: Centre for Research on the Epidemiology of Disasters (CRED)
    url: https://data.humdata.org/dataset/number-of-people-made-homeless-by-natural-disasters
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX
  url: https://data.humdata.org/dataset/number-of-people-made-homeless-by-natural-disasters
creator:
  affiliation: null
  email: null
  name: Centre for Research on the Epidemiology of Disasters
  url: https://data.humdata.org/dataset/number-of-people-made-homeless-by-natural-disasters
dataset_id: rdls_lss-hdx_numberpeoplemadehomelessn_20141111
description: 'Number of people made homeless by natural disasasters disaggregated
  by country and year. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/number-of-people-made-homeless-by-natural-disasters]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Post-event homelessness data compiled from the EM-DAT (Emergency Events
    Database) maintained by CRED, aggregating reported displacement figures from natural
    disasters by country and year. Data represents direct impacts of multiple hazard
    types on populations, with records sourced from official disaster reports and
    humanitarian assessments.
  sources:
  - id: source_1
    license: null
    name: Centre for Research on the Epidemiology of Disasters (CRED)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/number-of-people-made-homeless-by-natural-disasters
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: People made homeless by flood events
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
  - asset_category: population
    asset_dimension: population
    description: People made homeless by earthquake events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_2
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
  - asset_category: population
    asset_dimension: population
    description: People made homeless by strong wind events
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
          quantity_kind: count
          unit: null
        metric: displaced
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: People made homeless by landslide events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_4
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
  - asset_category: population
    asset_dimension: population
    description: People made homeless by volcanic events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_volcanic
      intensity_measure: h_vaf:mm
      process: null
      trigger: null
      type: volcanic
    id: loss_5
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
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: http://www.emdat.be/explanatory-notes
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Number of people made homeless by natural disasters (Excel)
  download_url: https://data.humdata.org/dataset/d2ec211d-faf6-4fb5-a46c-2094dc5830af/resource/b4ba3634-14d6-468d-81ef-18b096c1cf85/download/homeless-natural-disasters.xlsx
  format: null
  id: resource_b4ba3634
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: homeless-natural-disasters.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Number of people made homeless by natural disasters (CSV)
  download_url: https://data.humdata.org/dataset/d2ec211d-faf6-4fb5-a46c-2094dc5830af/resource/70f102af-6d2b-461b-9676-c597e7bf33d4/download/homeless-natural-disasters.csv
  format: null
  id: resource_70f102af
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: homeless-natural-disasters.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-hdx_numberpeoplemadehomelessn_20141111
spatial:
  bbox: null
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2014-11-11'
temporal_resolution: null
title: Number of people made homeless by natural disasters
version: null
vulnerability: null
---
