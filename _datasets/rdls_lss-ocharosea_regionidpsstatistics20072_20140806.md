---
attributions:
- entity:
    affiliation: null
    email: null
    name: OCHA
    url: https://data.humdata.org/dataset/eastern-africa-region-idps-statistics-2007-2014
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: IOM
    url: https://data.humdata.org/dataset/eastern-africa-region-idps-statistics-2007-2014
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UNHCR
    url: https://data.humdata.org/dataset/eastern-africa-region-idps-statistics-2007-2014
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Regional Office for Southern and Eastern Africa (ROSEA)
  url: https://data.humdata.org/dataset/eastern-africa-region-idps-statistics-2007-2014
creator:
  affiliation: null
  email: null
  name: OCHA Regional Office for Southern and Eastern Africa (ROSEA)
  url: https://data.humdata.org/dataset/eastern-africa-region-idps-statistics-2007-2014
dataset_id: rdls_lss-ocharosea_regionidpsstatistics20072_20140806
description: 'IDP numbers in Burundi, Djibouti, DRC, Eritrea, Ethiopia, Kenya, Rwanda,
  S.Sudan, Somalia, Sudan, Tanzania and Uganda since December 2007.. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/eastern-africa-region-idps-statistics-2007-2014]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: IDP statistics were manually aggregated from OCHA, IOM, and UNHCR sources
    across 12 Eastern African countries from December 2007 to March 2015. The dataset
    compiles displacement counts resulting from multiple hazard and conflict-related
    triggers into a time series of internally displaced persons by country.
  sources:
  - id: source_1
    license: null
    name: OCHA
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: IOM
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: UNHCR
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/eastern-africa-region-idps-statistics-2007-2014
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons from various hazards including flood
      across Eastern Africa
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
    description: Internally displaced persons from various hazards including earthquake
      across Eastern Africa
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
    description: Internally displaced persons from various hazards including drought
      across Eastern Africa
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
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
    description: Internally displaced persons from conflict and other causes across
      Eastern Africa
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
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
  description: Eastern Africa Region IDPs Statistics 2007 - 2015 (Number of IDPs in
    the Horn of Africa (Eastern Africa region))
  download_url: https://data.humdata.org/dataset/35f44b0e-c97c-436d-9e9a-28028edd4215/resource/f375ce25-106f-48ba-acbb-d384959361b0/download/ea-idp-stats-jun-07-to-date-09mar2015.csv
  format: null
  id: resource_f375ce25
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EA_IDP Stats Jun 07 to date_09Mar2015.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ocharosea_regionidpsstatistics20072_20140806
spatial:
  bbox: null
  centroid: null
  countries:
  - COD
  - BDI
  - DJI
  - ERI
  - ETH
  - KEN
  - RWA
  - SSD
  - SOM
  - SDN
  - TZA
  - UGA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2014-08-06'
temporal_resolution: null
title: Eastern Africa Region IDPs Statistics 2007 - 2015
version: null
vulnerability: null
---
