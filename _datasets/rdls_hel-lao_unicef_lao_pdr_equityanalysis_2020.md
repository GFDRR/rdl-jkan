---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNICEF Division of Data, Analysis, Planning and Monitoring (DAPM)
    url: https://data.humdata.org/dataset/unicef-lao-pdr-equity-analysis-base-layer
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: UNICEF Lao PDR
  url: https://data.humdata.org/dataset/unicef-lao-pdr-equity-analysis-base-layer
creator:
  affiliation: null
  email: null
  name: UNICEF Lao PDR
  url: https://data.humdata.org/dataset/unicef-lao-pdr-equity-analysis-base-layer
dataset_id: rdls_hel-lao_unicef_lao_pdr_equityanalysis_2020
description: 'UNICEF Lao PDR Equity Analysis (Base Layer) is a child rights-focused
  statistical tool developed by UNICEF''s Division of Data, Analysis, Planning and
  Monitoring (DAPM). Launched in 2025, it aims to identify and assess disparities
  affecting children by analyzing both deprivation and hazard dimensions using selected
  national and global datasets, with data collected from 2011 to 2024. 1) Deprivation
  Analysis examines critical areas impacting children''s well-being, including: Health,
  Nutrition, Education, Protection, Water, Sanitation and Hygiene (WASH), and Social
  Policy. 2) Hazard Analysis evaluates the prevalence and impact of climatic hazards
  such as floods, droughts, landslides, storms, heat wave, and air pollution. By highlighting
  inequities across population group and sub-national levels, Equity Analysis provides
  critical insights that support not only program planning, monitoring, and effectiveness
  for child-focused initiatives, but also inform decision-making for a wide range
  of stakeholders.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/unicef-lao-pdr-equity-analysis-base-layer]'
details: 'Limitations and Special Considerations in Equity Analysis: 1) Limited data
  availability: The analysis relies on secondary data, which may not be available
  for all indicators, regions, or population groups. 2) Lack of disaggregated data:
  Many datasets lack disaggregation by key equity dimensions such as age, sex, disability,
  ethnicity, or socioeconomic status, limiting deeper equity insights. 3) Outdated
  or infrequent data: Some sources are not regularly updated, which may affect the
  accuracy of current deprivation estimates. 4) Data consistency and comparability:
  Differences in indicator definitions, data collection methods, and reference years
  across sources may limit comparability. 5) Use of population projections: In the
  absence of up-to-date census data, population projections are used to estimate intensity
  (number affected), which introduces assumptions and potential uncertainty in the
  results. 6) Use of proxy indicators: When direct data is not available, proxy indicators
  are applied, which may not fully capture the intended deprivation. 7) Simplification
  through index scoring: The deprivation index (0 = least deprived, 10 = most deprived)
  is a simplified composite score used for prioritization, which may not capture the
  full complexity of each issue or context.'
exposure:
- asset_type:
    description: Child population disaggregated by age groups, gender, and ethnicity
      at provincial and district levels
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
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: inferred
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Secondary data from national and global datasets (2011-2024) were collected
    and synthesized to compute deprivation indices across health, nutrition, education,
    WASH, protection, and social policy domains, combined with hazard exposure metrics
    to generate composite equity indices at admin1 and admin2 levels.
  sources:
  - id: source_1
    license: null
    name: UNICEF Division of Data, Analysis, Planning and Monitoring (DAPM)
    risk_data_type:
    - loss
    type: model
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/unicef-lao-pdr-equity-analysis-base-layer
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Child deprivation indicators across health, nutrition, education,
      WASH, and protection domains
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
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Child deprivation indicators linked to drought hazard exposure
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
  description: Lao PDR - Equity Analysis (Equity Analysis_Base Layer.xlsx)
  download_url: https://data.humdata.org/dataset/c20e57ca-dae8-4c65-896b-bd4ba25ca0a6/resource/28df5ba6-40a6-4df0-886d-ee4c0817ba6b/download/equity-analysis_base-layer.xlsx
  format: null
  id: resource_28df5ba6
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Equity Analysis_Base Layer.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Lao PDR - Equity Analysis (Equity Analysis_Hazard Layer.xlsx)
  download_url: https://data.humdata.org/dataset/c20e57ca-dae8-4c65-896b-bd4ba25ca0a6/resource/d39b5a7e-8754-438e-825e-78b66ef46fa4/download/equity-analysis_hazard-layer.xlsx
  format: null
  id: resource_d39b5a7e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Equity Analysis_Hazard Layer.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Lao PDR - Equity Analysis (Equity Analysis_Deprivation Layer.xlsx)
  download_url: https://data.humdata.org/dataset/c20e57ca-dae8-4c65-896b-bd4ba25ca0a6/resource/a1c600e7-49ca-4097-8a79-fd03e69c1a0f/download/equity-analysis_deprivation-layer.xlsx
  format: null
  id: resource_a1c600e7
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Equity Analysis_Deprivation Layer.xlsx
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-lao_unicef_lao_pdr_equityanalysis_2020
spatial:
  bbox: null
  centroid: null
  countries:
  - LAO
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-04-01'
  start: '2020-01-01'
temporal_resolution: null
title: Lao PDR - Equity Analysis
version: null
vulnerability: null
---
