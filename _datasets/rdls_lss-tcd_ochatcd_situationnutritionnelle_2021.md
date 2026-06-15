---
attributions:
- entity:
    affiliation: null
    email: null
    name: Global Nutrition Cluster
    url: https://data.humdata.org/dataset/chad-nutrition-smart-survey
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: IPC (Integrated Food Security Phase Classification)
    url: https://data.humdata.org/dataset/chad-nutrition-smart-survey
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Chad
  url: https://data.humdata.org/dataset/chad-nutrition-smart-survey
creator:
  affiliation: null
  email: null
  name: OCHA Chad
  url: https://data.humdata.org/dataset/chad-nutrition-smart-survey
dataset_id: rdls_lss-tcd_ochatcd_situationnutritionnelle_2021
description: 'This data is about Global Acute Malnutrition (GAM), Moderate Acute Malnutrition
  (MAM), and Severe Acute Malnutrition (SAM) at administrative division 2 level in
  Chad.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/chad-nutrition-smart-survey]'
details: See more details on the Standardized Monitoring and Assessment of Relief
  and Transitions (SMART) methodology [here](https://smartmethodology.org/survey-planning-tools/smart-methodology/smart-methodology-manual/)
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Nutritional status data collected through sample surveys (SMART methodology)
    by the Global Nutrition Cluster across administrative divisions in Chad. Multiple
    survey rounds (2021, 2022, and Oct2023-Sept2024) were compiled and integrated
    with IPC acute malnutrition classifications to assess population-level food insecurity
    and malnutrition impacts.
  sources:
  - id: source_1
    license: null
    name: Global Nutrition Cluster
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: IPC (Integrated Food Security Phase Classification)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/chad-nutrition-smart-survey
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Global Acute Malnutrition (GAM) prevalence in population affected
      by food insecurity and nutritional crisis
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
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Moderate Acute Malnutrition (MAM) cases in vulnerable populations
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
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Severe Acute Malnutrition (SAM) cases in vulnerable populations
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
purpose: Sample Survey
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Tchad: Situation Nutritionnelle (Nutritional Situation of 15 Provinces,
    27 Departments, and N''Djamena 2023-2024)'
  download_url: https://data.humdata.org/dataset/c9def68c-60c8-4d78-91a7-bf0697dab9b2/resource/c38a08ba-0000-48ec-9beb-b6e0955e05bd/download/ipc_chad_acute_malnutrition_oct2023_sept2024_report_french.xlsx
  format: null
  id: resource_c38a08ba
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: IPC_Chad_Acute_Malnutrition_Oct2023_Sept2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Tchad: Situation Nutritionnelle (Smart Survey 2022)'
  download_url: https://data.humdata.org/dataset/c9def68c-60c8-4d78-91a7-bf0697dab9b2/resource/5c07f462-1d3d-4f46-8141-1326481717ff/download/tcd_nutrition_smart_2022.xlsx
  format: null
  id: resource_5c07f462
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TCD_Nutrition_Smart_2022
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Tchad: Situation Nutritionnelle (Smart Survey 2021)'
  download_url: https://data.humdata.org/dataset/c9def68c-60c8-4d78-91a7-bf0697dab9b2/resource/175fe47a-ab68-495d-8ac0-defce8e4924d/download/tcd_data_smart2021.xlsx
  format: null
  id: resource_175fe47a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TCD_DATA_SMART2021
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-tcd_ochatcd_situationnutritionnelle_2021
spatial:
  bbox: null
  centroid: null
  countries:
  - TCD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-09-30'
  start: '2021-04-30'
temporal_resolution: null
title: 'Tchad: Situation Nutritionnelle'
version: null
vulnerability: null
---
