---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Internal Displacement Monitoring Centre (IDMC)
  url: https://data.humdata.org/dataset/socio-economic-impacts-of-internal-displacement-in-sierra-leone
creator:
  affiliation: null
  email: null
  name: Internal Displacement Monitoring Centre (IDMC)
  url: https://data.humdata.org/dataset/socio-economic-impacts-of-internal-displacement-in-sierra-leone
dataset_id: rdls_hl-sle_idmc_socioeconomicimpacts_202406
description: 'This dataset contains both quantitative and qualitative data, as well
  as financial information, measuring the impacts of internal displacement in Plantain
  Island, Sierra Leone as a result of rising sea levels. It includes data on both
  economic and non-economic losses experienced by internally displaced people (IDPs)
  and host communities and covers various dimensions such as livelihoods, housing,
  health, security and education. Methodology: Developed in 2019, IDMC''s survey tool
  collects quantitative and qualitative data, as well as financial information, to
  measure the impacts of internal displacement. The survey captures both economic
  and non-economic losses experienced by internally displaced people (IDPs) and host
  communities and covers key dimensions including livelihoods, housing, health, security
  and education. It allows for data disaggregation by sex, age, disability status,
  income and education levels, area of origin, duration of displacement and ethnolinguistic
  identity, helping to identify overlapping vulnerabilities. Data compilation process:
  Data was collected using a combination of random walk and respondent-driven sampling
  techniques. On Plantain Island, enumerators employed a random walk approach to select
  participants, while in Tombo and Tissana, respondent-driven sampling was used to
  identify people displaced from the island. Primary sources: IDMC and the Sierra
  Leone National Disaster Management Agency (NDMA).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/socio-economic-impacts-of-internal-displacement-in-sierra-leone]'
details: 'The study includes interviews from 197 IDPs and 31 of their non-displaced
  counterparts across Plantain Island, Shenge, Tissana and Tombo. Given the small
  sample size of host community members, the analysis focused primarily on the IDPs.
  The findings are not nationally representative and should be interpreted as indicative
  of the situation of people displaced by disasters living in those specific locations.
  Report published: https://doi.org/10.55363/IDMC.UCXV2874'
exposure: []
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: slr:cm
      process: sea_level_rise
      trigger: null
      type: sea_level_rise
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-4.0
lineage:
  description: IDMC's standardized survey tool administered in 2019 collected quantitative,
    qualitative, and financial data from internally displaced persons and host communities
    in Plantain Island, Sierra Leone. Data covers multiple dimensions of displacement
    impact including livelihoods, housing, health, security, and education, with specific
    focus on sea level rise as the triggering hazard.
  sources:
  - id: source_1
    license: null
    name: Internal Displacement Monitoring Centre (IDMC)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/socio-economic-impacts-of-internal-displacement-in-sierra-leone
  rel: source
loss:
  losses:
  - asset_category: economic_indicator
    asset_dimension: index
    description: Internally displaced persons from sea level rise in Plantain Island
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_sea_level_rise
      intensity_measure: slr:cm
      process: null
      trigger: null
      type: sea_level_rise
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: null
        metric: displaced
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
      loss_type: ground_up
  - asset_category: economic_indicator
    asset_dimension: index
    description: Economic losses experienced by IDPs and host communities including
      housing and livelihood impacts
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_sea_level_rise
      intensity_measure: slr:cm
      process: null
      trigger: null
      type: sea_level_rise
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: null
        metric: loss
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
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
  description: Socio economic impacts of internal displacement in Sierra Leone (Excel)
  download_url: https://data.humdata.org/dataset/5e9d9557-2a0e-40eb-ab3f-90af68176830/resource/e5b5d002-43d5-477e-8f7f-fd81c7ece8ee/download/idmc_sierra_leone_socioeconomicimpact_idps_01062024_27062024.xlsx
  format: null
  id: resource_e5b5d002
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: idmc_sierra_leone_socioeconomicimpact_idps_01062024_27062024.xlsx
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-sle_idmc_socioeconomicimpacts_202406
spatial:
  bbox: null
  centroid: null
  countries:
  - SLE
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-06-27'
  start: '2024-06-01'
temporal_resolution: null
title: Socio economic impacts of internal displacement in Sierra Leone
version: null
vulnerability: null
---
