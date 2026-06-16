---
attributions:
- entity:
    affiliation: null
    email: null
    name: IOM
    url: https://data.humdata.org/dataset/sudan-2022-msna-houshold-survey-without-refugees
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Sudan
  url: https://data.humdata.org/dataset/sudan-2022-msna-houshold-survey-without-refugees
creator:
  affiliation: null
  email: null
  name: OCHA Sudan
  url: https://data.humdata.org/dataset/sudan-2022-msna-houshold-survey-without-refugees
dataset_id: rdls_lss-sdn_ochasdn_2022msnahousholdsurveywit_2022
description: 'The purpose of the 2022 Sudan Multi-Sector Needs Assessment (MSNA) is
  to provide household data on the priority humanitarian needs of populations in States
  around Sudan. The findings intend to provide timely updates on key sectoral needs
  to inform humanitarian response and strategic programming for non-displaced, and
  IDP households. The 2022 MSNA will inform the 2023 Humanitarian Needs Overview (HNO)
  and the 2023 Humanitarian Response Plan (HRP). Data was collected through structured
  household interviews using the KOBO data collection package. Findings are representative
  at the state level with a confidence interval of 98% and a 5% margin of error. The
  MSNA data is a relational dataset. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/sudan-2022-msna-houshold-survey-without-refugees]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Household-level survey data collected through structured KOBO interviews
    across Sudan states to assess multi-sector humanitarian needs (food security,
    health, WASH, nutrition, protection, NFI, education) among non-displaced and IDP
    populations. Data aggregated to state-level representative estimates to inform
    the 2023 Humanitarian Needs Overview and Response Plan.
  sources:
  - id: source_1
    license: null
    name: IOM
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/sudan-2022-msna-houshold-survey-without-refugees
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Humanitarian needs assessment capturing population affected by multiple
      hazards including flood impacts on food security, health, and WASH
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
    description: Humanitarian needs assessment capturing population affected by drought
      impacts on food security and livelihoods
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
purpose: Sample Survey
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This is the 2022 multisector needs analysis data (MSNA) - a comprehensive
    household-level analysis covering all states in Sudan.
  download_url: https://data.humdata.org/dataset/09d6d1f7-f5b7-4348-ba99-a69f2f9783f6/resource/54bd7544-d094-44b0-84d1-f63c70317619/download/sud_msna__2022_data-tables_without-refugees.xlsx
  format: null
  id: resource_54bd7544
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SUD_MSNA__2022_Data Tables_without Refugees.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-sdn_ochasdn_2022msnahousholdsurveywit_2022
spatial:
  bbox: null
  centroid: null
  countries:
  - SDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-09-30'
  start: '2022-09-01'
temporal_resolution: null
title: Sudan:2022 MSNA Houshold Survey without Refugees
version: null
vulnerability: null
---
