---
attributions:
- entity:
    affiliation: null
    email: null
    name: Inter-Agency Standing Committee (IASC)
    url: https://data.humdata.org/dataset/inform-guatemala-model
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: European Commission
    url: https://data.humdata.org/dataset/inform-guatemala-model
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: National Coordination System for Disaster Risk Reduction (CONRED)
    url: https://data.humdata.org/dataset/inform-guatemala-model
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: INFORM
  url: https://data.humdata.org/dataset/inform-guatemala-model
creator:
  affiliation: null
  email: null
  name: INFORM
  url: https://data.humdata.org/dataset/inform-guatemala-model
dataset_id: rdls_ev-gtm_inform_model
description: 'INFORM Guatemala is a municipal risk index that identifies risks, threats,
  vulnerabilities and response capacities in the 340 municipalities of Guatemala.
  The municipal risk index simplifies information about crisis risk and is comprised
  of 29 indicators representing the three dimensions of risk: hazard and exposure,
  vulnerability, and lack of coping capacity. The results of the Guatemala INFORM
  index will be used by the National Coordination System for Disaster Risk Reduction
  (CONRED) for its analysis of risk of humanitarian crisis and disasters, municipal
  response capacities and potential humanitarian needs. Government institutions, civil
  society and international cooperation organizations can also use the results to
  focus the design and implementation of development programs and projects. The Guatemala
  INFORM initiative is supported by UNICEF, OCHA and WFP.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/inform-guatemala-model]'
details: null
exposure:
- asset_type:
    description: Total municipal population estimates
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
- asset_type:
    description: Forest cover and annual rate of change by municipality
    id: natural_environment
    scheme: null
    title: null
    uri: null
  category: natural_environment
  id: exposure_2
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
- asset_type:
    description: Road network density and electrification coverage at municipal level
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_3
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: length
      unit: null
- asset_type:
    description: Economic indicators including GDP per capita, poverty rates, and
      remittances as percentage of GDP
    id: economic_indicator
    scheme: null
    title: null
    uri: null
  category: economic_indicator
  id: exposure_4
  metrics:
  - dimension: index
    id: metric_1
    measurement:
      quantity_kind: index
      unit: null
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: The INFORM Guatemala model integrates 29 indicators from multiple national
    and international sources across three risk dimensions (hazard & exposure, vulnerability,
    coping capacity) normalized and aggregated to produce a composite municipal risk
    index. Data sources include observed disaster events 2008-2021, socioeconomic
    indicators from national census and development agencies, and institutional capacity
    assessments, all processed through the INFORM v3.2021 methodology to generate
    normalized sub-indices and an overall risk score for each of Guatemala's 340 municipalities.
  sources:
  - id: source_1
    license: null
    name: Inter-Agency Standing Committee (IASC)
    risk_data_type:
    - vulnerability
    type: model
    url: null
    used_in: vulnerability
  - id: source_2
    license: null
    name: European Commission
    risk_data_type:
    - vulnerability
    type: model
    url: null
    used_in: vulnerability
  - id: source_3
    license: null
    name: National Coordination System for Disaster Risk Reduction (CONRED)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/inform-guatemala-model
  rel: source
loss:
  losses: []
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
  url: https://bit.ly/2MB0ZIj
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'INFORM Guatemala is a municipal risk index that identifies risks,
    threats, vulnerabilities and response capacities in the 340 municipalities of
    Guatemala. The municipal risk index simplifies information about crisis risk and
    is comprised of 29 indicators representing the three dimensions of risk: hazard
    and exposure, vulnerability, and lack of coping capacity.'
  download_url: https://data.humdata.org/dataset/d9e378fd-164e-43c4-893d-148cb18f23f3/resource/fa5bbe16-8c43-40b5-973e-d91692f7c2e6/download/inform-v3.2021.xlsx
  format: null
  id: resource_fa5bbe16
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: INFORM v3.2021.xlsx
risk_data_type:
- exposure
- vulnerability
schema: rdls-10
slug: rdls_ev-gtm_inform_model
spatial:
  bbox: null
  centroid: null
  countries:
  - GTM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: INFORM Guatemala Model
version: null
vulnerability: null
---
