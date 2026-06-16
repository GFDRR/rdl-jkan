---
attributions:
- entity:
    affiliation: null
    email: null
    name: Humanitarian partners
    url: https://data.humdata.org/dataset/somalia-drought-related-key-figures
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Regional Office for Southern and Eastern Africa (ROSEA)
  url: https://data.humdata.org/dataset/somalia-drought-related-key-figures
creator:
  affiliation: null
  email: null
  name: OCHA Regional Office for Southern and Eastern Africa (ROSEA)
  url: https://data.humdata.org/dataset/somalia-drought-related-key-figures
dataset_id: rdls_lss-som_ocharosea_droughtrelatedkeyfigures_20230731
description: 'Drought Related Key Figures for Somalia. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/somalia-drought-related-key-figures]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Drought-related key figures aggregated from humanitarian partners operating
    in Somalia, compiled by OCHA ROSEA to track drought impacts including affected
    populations, internally displaced persons, people in need, and malnutrition prevalence
    for the drought response and famine prevention plan.
  sources:
  - id: source_1
    license: null
    name: Humanitarian partners
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/somalia-drought-related-key-figures
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Affected population from drought in Somalia
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
    description: Internally displaced persons from drought in Somalia
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
  - asset_category: population
    asset_dimension: population
    description: People in need due to drought in Somalia
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
  url: https://reliefweb.int/report/somalia/somalia-drought-response-and-famine-prevention-plan-may-december-2022-june-2022
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia Drought Related - Key Figures (CSV)
  download_url: https://docs.google.com/spreadsheets/d/e/2PACX-1vRppQx8JTKkKRCKmzfnCMmTFEcvCpkbP9PdHs1sQTUyacmbsx8tlAXpgBLFce-lcehukreGGuXjA_4S/pub?gid=0&single=true&output=csv
  format: null
  id: resource_0b8dd14b
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: somalia-drought-key-figures
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-som_ocharosea_droughtrelatedkeyfigures_20230731
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
  start: '2023-07-31'
temporal_resolution: null
title: Somalia Drought Related - Key Figures
version: null
vulnerability: null
---
