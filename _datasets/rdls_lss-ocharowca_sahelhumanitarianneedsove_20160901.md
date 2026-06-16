---
attributions:
- entity:
    affiliation: null
    email: null
    name: United Nations Office for the Coordination of Humanitarian Affairs (OCHA)
    url: https://data.humdata.org/dataset/sahel-humanitarian-needs-overview
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA West and Central Africa (ROWCA)
  url: https://data.humdata.org/dataset/sahel-humanitarian-needs-overview
creator:
  affiliation: null
  email: null
  name: OCHA West and Central Africa (ROWCA)
  url: https://data.humdata.org/dataset/sahel-humanitarian-needs-overview
dataset_id: rdls_lss-ocharowca_sahelhumanitarianneedsove_20160901
description: 'This dataset is produced by the United Nations for the Coordination
  of Humanitarian Affairs (OCHA) in collaboration with humanitarian partners. It covers
  the period from January to December 2017 and was issued on December 2016.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/sahel-humanitarian-needs-overview]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Multi-organizational humanitarian needs data aggregated by OCHA ROWCA
    from partner assessments across Sahel countries. Data covers people in need, food
    insecurity classifications, nutrition status, and displacement figures for the
    2017 humanitarian response planning cycle, compiled from country-level assessments.
  sources:
  - id: source_1
    license: null
    name: United Nations Office for the Coordination of Humanitarian Affairs (OCHA)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/sahel-humanitarian-needs-overview
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: People in need due to food insecurity and drought-related humanitarian
      crisis in the Sahel
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
    description: Population displacement across Sahel countries due to drought and
      food insecurity
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
    description: Nutrition-affected population in the Sahel and Lake Chad region
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
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sahel : Humanitarian Needs Overview (HNO 2017 Sahel - Nutrition)'
  download_url: https://data.humdata.org/dataset/47f6ef46-500f-421a-9fa2-fefd93facf95/resource/2527ac5b-66fe-46f0-8b9b-7086d2c4ddd3/download/hno-2017-sahel-nutrition.csv
  format: null
  id: resource_2527ac5b
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: HNO -2017 -Sahel-nutrition.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sahel : Humanitarian Needs Overview (HNO 2017 sahel - Lake Chad -
    Nutrition)'
  download_url: https://data.humdata.org/dataset/47f6ef46-500f-421a-9fa2-fefd93facf95/resource/487e329d-3959-49bf-8e12-2675be7008ae/download/hno-2017-sahel-lake-chad-nutrition-as-of-25_11_2016.csv
  format: null
  id: resource_487e329d
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: HNO 2017 Sahel-Lake Chad Nutrition as of 25_11_2016.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sahel : Humanitarian Needs Overview (HNO 2017 Sahel - Displacement
    per country)'
  download_url: https://data.humdata.org/dataset/47f6ef46-500f-421a-9fa2-fefd93facf95/resource/d648d73f-8e66-461f-864f-0d66b19bcfa2/download/hno-2017-sahel-displacement_per_country.xlsx
  format: null
  id: resource_d648d73f
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: HNO-2017-Sahel- Displacement_per_country.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sahel : Humanitarian Needs Overview (HNO 2017 Sahel - People in need)'
  download_url: https://data.humdata.org/dataset/47f6ef46-500f-421a-9fa2-fefd93facf95/resource/d9248be4-7bfb-4a81-a7aa-c035dcb737a2/download/hno-2017-sahel-people-in-need.xlsx
  format: null
  id: resource_d9248be4
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: HNO-2017-Sahel- People in need.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sahel : Humanitarian Needs Overview (HNO 2017 Sahel - Food Insecurity)'
  download_url: https://data.humdata.org/dataset/47f6ef46-500f-421a-9fa2-fefd93facf95/resource/798b6a50-75da-4c8c-8034-4a4439630a3a/download/hno-2017-sahel-food-insecurity.xlsx
  format: null
  id: resource_798b6a50
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: HNO-2017-Sahel-Food Insecurity.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ocharowca_sahelhumanitarianneedsove_20160901
spatial:
  bbox: null
  centroid: null
  countries:
  - BEN
  - BFA
  - CMR
  - TCD
  - CIV
  - GMB
  - GIN
  - GNB
  - MLI
  - MRT
  - NER
  - SEN
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-09-01'
temporal_resolution: null
title: 'Sahel : Humanitarian Needs Overview'
version: null
vulnerability: null
---
