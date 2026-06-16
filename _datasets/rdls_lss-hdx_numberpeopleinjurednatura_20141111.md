---
attributions:
- entity:
    affiliation: null
    email: null
    name: Centre for Research on the Epidemiology of Disasters (CRED) - EM-DAT
    url: https://data.humdata.org/dataset/number-of-people-injured-in-natural-disasters
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX
  url: https://data.humdata.org/dataset/number-of-people-injured-in-natural-disasters
creator:
  affiliation: null
  email: null
  name: Centre for Research on the Epidemiology of Disasters
  url: https://data.humdata.org/dataset/number-of-people-injured-in-natural-disasters
dataset_id: rdls_lss-hdx_numberpeopleinjurednatura_20141111
description: 'Number of people injured in natural disasters. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/number-of-people-injured-in-natural-disasters]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Injury counts from natural disaster events were extracted from the
    EM-DAT database maintained by the Centre for Research on the Epidemiology of Disasters
    (CRED). EM-DAT compiles disaster impact data from multiple sources including UN
    agencies, governments, and NGOs. The dataset aggregates injured person counts
    across natural disaster events, likely organized by country and/or year.
  sources:
  - id: source_1
    license: null
    name: Centre for Research on the Epidemiology of Disasters (CRED) - EM-DAT
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/number-of-people-injured-in-natural-disasters
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Number of people injured by natural disasters (multiple hazard types)
      compiled from EM-DAT historical event records
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
        metric: ppl_injured
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
  description: Number of people injured in natural disasters (Excel)
  download_url: https://data.humdata.org/dataset/0255cf49-2c13-430d-b738-aebdc9733bdd/resource/db014a67-98d4-4826-a9a2-7fc11ad269c5/download/injured-natural-disasters.xlsx
  format: null
  id: resource_db014a67
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: injured-natural-disasters.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Number of people injured in natural disasters (CSV)
  download_url: https://data.humdata.org/dataset/0255cf49-2c13-430d-b738-aebdc9733bdd/resource/b0633fdd-85c8-41c9-8b84-02b0dd896777/download/injured-natural-disasters.csv
  format: null
  id: resource_b0633fdd
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: injured-natural-disasters.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-hdx_numberpeopleinjurednatura_20141111
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
title: Number of people injured in natural disasters
version: null
vulnerability: null
---
