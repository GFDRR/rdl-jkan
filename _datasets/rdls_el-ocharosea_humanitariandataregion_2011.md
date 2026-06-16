---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNOCHA
    url: https://data.humdata.org/dataset/humanitarian-data-for-eastern-africa-region
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UNHCR
    url: https://data.humdata.org/dataset/humanitarian-data-for-eastern-africa-region
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: FEWSNET
    url: https://data.humdata.org/dataset/humanitarian-data-for-eastern-africa-region
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Regional Office for Southern and Eastern Africa (ROSEA)
  url: https://data.humdata.org/dataset/humanitarian-data-for-eastern-africa-region
creator:
  affiliation: null
  email: null
  name: OCHA Regional Office for Southern and Eastern Africa (ROSEA)
  url: https://data.humdata.org/dataset/humanitarian-data-for-eastern-africa-region
dataset_id: rdls_el-ocharosea_humanitariandataregion_2011
description: 'This dataset includes the Refugee, IDPs, People in need by Sector, Humanitarian
  Funding, inform indexes and humanitarian priorites data for countries in the wider
  horn of Africa Region from 2011 to date. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/humanitarian-data-for-eastern-africa-region]'
details: The dataset is not complete and may be out of date for some columns e.g funding,
  some of the details are subject for verification. A zero entry may mean that the
  particular information is unavailable and not actually zero.
exposure:
- asset_type:
    description: Refugee and internally displaced person populations in the Horn of
      Africa region
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: CC-BY-4.0
lineage:
  description: Regional humanitarian data aggregated from multiple UN and specialized
    agency sources (UNOCHA, UNHCR, FEWSNET) covering refugee populations, internally
    displaced persons, people in need by sector, and humanitarian funding requirements
    across the Horn of Africa from 2011 onwards. Data was compiled from the Financial
    Tracking Service and other authoritative humanitarian information systems to support
    regional humanitarian analysis and prioritization.
  sources:
  - id: source_1
    license: null
    name: UNOCHA
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: UNHCR
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_3
    license: null
    name: FEWSNET
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/humanitarian-data-for-eastern-africa-region
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: People in need by sector due to drought and food insecurity in the
      Horn of Africa
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
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
    description: Internally displaced persons and refugees from drought-affected areas
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_2
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
  description: Humanitarian Data for Eastern Africa Region (East Africa Humanitarian
    Data.csv)
  download_url: https://data.humdata.org/dataset/507f8e56-eb0b-4daa-bf0b-974d7777a4fb/resource/c4a88eb9-e445-4a48-8f4f-563189b5e137/download/fundingcleaned.csv
  format: null
  id: resource_c4a88eb9
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: East Africa Humanitarian Data.csv
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-ocharosea_humanitariandataregion_2011
spatial:
  bbox: null
  centroid: null
  countries:
  - DZA
  - BDI
  - DJI
  - ERI
  - ETH
  - KEN
  - SOM
  - SSD
  - UGA
  - TZA
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2015-06-09'
  start: '2011-06-09'
temporal_resolution: null
title: Humanitarian Data for Eastern Africa Region
version: null
vulnerability: null
---
