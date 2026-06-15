---
attributions:
- entity:
    affiliation: null
    email: null
    name: REACH Initiative
    url: https://data.humdata.org/dataset/state-of-palestine-msna-findings
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA occupied Palestinian territory (oPt)
  url: https://data.humdata.org/dataset/state-of-palestine-msna-findings
creator:
  affiliation: null
  email: null
  name: OCHA occupied Palestinian territory (oPt)
  url: https://data.humdata.org/dataset/state-of-palestine-msna-findings
dataset_id: rdls_lss-pse_ochapse_statemsnafindings_20210718
description: 'The first Multi-Sector Needs Assesment (MSNA), conducted by REACH Initiative
  in close collaboration with OCHA, aims to understand the multi-sectoral and sector-specific
  needs, circumstances, and vulnerabilities of households across the entirety of the
  Occupied Palestinian Territory (oPt). The current assessment is designed to support
  humanitarian actors in their development of the 2022 Humanitarian Needs Overview
  (HNO) and Humanitarian Response Plan (HRP), in addition to supporting humanitarian,
  development, and peace actors in their development and implementation of a nexus
  approach for the oPt.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/state-of-palestine-msna-findings]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: REACH Initiative conducted a sample survey of households across the
    Occupied Palestinian Territory to assess multi-sectoral needs and vulnerabilities
    in food security, water/sanitation/hygiene, and education sectors. Survey findings
    were compiled and validated by OCHA to support the 2022 Humanitarian Needs Overview
    and Humanitarian Response Plan development.
  sources:
  - id: source_1
    license: null
    name: REACH Initiative
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: OCHA occupied Palestinian territory (oPt)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/state-of-palestine-msna-findings
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Food security needs and vulnerabilities affecting households in oPt
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
    description: Water, sanitation and hygiene needs affecting households in oPt
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
  - asset_category: population
    asset_dimension: population
    description: Education sector needs and vulnerabilities affecting households in
      oPt
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
purpose: Sample Survey
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: State of Palestine - MSNA findings (Excel)
  download_url: https://data.humdata.org/dataset/cfd6dbe2-dab8-40c9-9106-f66c82347adc/resource/704dfa8a-f0c1-405f-8516-3b14de3630bf/download/opt_msna.xlsx
  format: null
  id: resource_704dfa8a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: oPt_MSNA_findings
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-pse_ochapse_statemsnafindings_20210718
spatial:
  bbox: null
  centroid: null
  countries:
  - PSE
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2021-07-18'
temporal_resolution: null
title: State of Palestine - MSNA findings
version: null
vulnerability: null
---
