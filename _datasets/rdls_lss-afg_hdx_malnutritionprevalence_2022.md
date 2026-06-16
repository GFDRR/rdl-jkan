---
attributions:
- entity:
    affiliation: null
    email: null
    name: IPC and Partners
    url: https://data.humdata.org/dataset/afg-malnutrition-prevalence
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX
  url: https://data.humdata.org/dataset/afg-malnutrition-prevalence
creator:
  affiliation: null
  email: null
  name: IPC and Partners
  url: https://data.humdata.org/dataset/afg-malnutrition-prevalence
dataset_id: rdls_lss-afg_hdx_malnutritionprevalence_2022
description: 'The major drivers of acute malnutrition in Afghanistan include inadequate
  quantity and poor quality of children diets, high prevalence of diseases (diarrhea,
  malaria, acute respiratory infection and measles outbreaks) and inadequate access
  to safe drinking water, sanitation and low hygiene practices. Additionally, reduced
  access to health and nutrition services, suboptimal breastfeeding practices, and
  high levels of food insecurity exacerbate acute malnutrition. Other risk factors
  like widespread shocks, including drought, flooding and population displacement
  continue to negatively impact the nutrition situation.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/afg-malnutrition-prevalence]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Acute malnutrition case estimates were calculated by multiplying the
    number of children under 5 and pregnant/breastfeeding women by prevalence rates
    (SAM, MAM, GAM) and applying incident correction factors, following national practices.
    Data aggregates provincial-level malnutrition assessments from IPC and partners
    across multiple time periods (2022-2026), capturing indirect impacts of drought,
    flooding, and food insecurity on vulnerable populations.
  sources:
  - id: source_1
    license: null
    name: IPC and Partners
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/afg-malnutrition-prevalence
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Acute malnutrition cases in children and pregnant/breastfeeding women,
      driven by drought-induced food insecurity and disease
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
        type: indirect
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Acute malnutrition cases in children and pregnant/breastfeeding women,
      driven by flood-induced food insecurity and displacement
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: indirect
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
  description: 'Afghanistan - Malnutrition Prevalence (IPC AMN: Projection period
    of January - December 2026.)'
  download_url: https://data.humdata.org/dataset/9fbf1b7f-9217-4ec1-84d0-f88339fcba54/resource/b8d5ef8f-1c97-41d5-9f32-21a4cf8c78f8/download/afghanistan_malnutrition_data_jan-dec2026.xlsx
  format: null
  id: resource_b8d5ef8f
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: afghanistan_malnutrition_data_jan-dec2026.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'IPC AMN: current analysis period of June - October 2024 and projection
    period of November 2024 - May 2025.'
  download_url: https://data.humdata.org/dataset/9fbf1b7f-9217-4ec1-84d0-f88339fcba54/resource/3defd36d-10e5-4c84-a279-872a35df1166/download/afghanistan_malnutrition_data_jun2024-may2025.xlsx
  format: null
  id: resource_3defd36d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: afghanistan_malnutrition_data_jun2024-may2025
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'IPC AMN: current analysis period of Sep-Oct 2022 and projection period
    of November 2022 - April 2023.'
  download_url: https://data.humdata.org/dataset/9fbf1b7f-9217-4ec1-84d0-f88339fcba54/resource/c1e5582f-6f77-4c4b-a31e-be22c500e0b8/download/afghanistan_malnutrition_data_sep2022-apr2023-2.xlsx
  format: null
  id: resource_c1e5582f
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: afghanistan_malnutrition_data_sep2022-apr2023
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-afg_hdx_malnutritionprevalence_2022
spatial:
  bbox: null
  centroid: null
  countries:
  - AFG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-12-31'
  start: '2022-09-01'
temporal_resolution: null
title: Afghanistan - Malnutrition Prevalence
version: null
vulnerability: null
---
