---
attributions:
- entity:
    affiliation: null
    email: null
    name: Centre for Research on the Epidemiology of Disasters (CRED)
    url: https://data.humdata.org/dataset/total-number-of-people-affected-by-natural-disasters
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX
  url: https://data.humdata.org/dataset/total-number-of-people-affected-by-natural-disasters
creator:
  affiliation: null
  email: null
  name: Centre for Research on the Epidemiology of Disasters
  url: https://data.humdata.org/dataset/total-number-of-people-affected-by-natural-disasters
dataset_id: rdls_lss-hdx_totalnumberpeopleaffected_20141111
description: 'Number of people affected by natural disasters disaggregated by country
  and year. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/total-number-of-people-affected-by-natural-disasters]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Data compiled from the EM-DAT (Emergency Events Database) maintained
    by CRED, aggregating reported disaster impact records from multiple sources. The
    dataset presents total affected population counts disaggregated by country and
    year across multiple natural hazard types, representing post-event impact assessments.
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
- href: https://data.humdata.org/dataset/total-number-of-people-affected-by-natural-disasters
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Total number of people affected by flood events
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
  - asset_category: population
    asset_dimension: population
    description: Total number of people affected by earthquake events
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
        metric: exposure
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Total number of people affected by strong wind events
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
        metric: exposure
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Total number of people affected by drought events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_4
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
  - asset_category: population
    asset_dimension: population
    description: Total number of people affected by landslide events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_5
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
  - asset_category: population
    asset_dimension: population
    description: Total number of people affected by wildfire events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: null
      trigger: null
      type: wildfire
    id: loss_6
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
  description: Total number of people affected by natural disasters (Excel)
  download_url: https://data.humdata.org/dataset/97e007af-4733-4b60-a472-a733f10dedd5/resource/fc53c2b6-8143-45b1-a796-55644f8d9d55/download/total-affected-natural-disasters.xlsx
  format: null
  id: resource_fc53c2b6
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: total-affected-natural-disasters.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Total number of people affected by natural disasters (CSV)
  download_url: https://data.humdata.org/dataset/97e007af-4733-4b60-a472-a733f10dedd5/resource/cb274aca-d979-4fac-a2b5-a0de5910c6e2/download/total-affected-natural-disasters.csv
  format: null
  id: resource_cb274aca
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: total-affected-natural-disasters.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-hdx_totalnumberpeopleaffected_20141111
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
title: Total number of people affected by natural disasters
version: null
vulnerability: null
---
