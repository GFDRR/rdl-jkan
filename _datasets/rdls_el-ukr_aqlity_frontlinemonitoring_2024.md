---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AQLITY
  url: https://data.humdata.org/dataset/ukraine
creator:
  affiliation: null
  email: null
  name: AQLITY
  url: https://data.humdata.org/dataset/ukraine
dataset_id: rdls_el-ukr_aqlity_frontlinemonitoring_2024
description: 'This dataset is part of AQLITY''s Security, Logistics, Access and Cash
  Feasibility (SLAC) Monitoring tool. It captures granular, settlement-level data
  collected through direct observation and key informant interviews across eastern
  Ukraine. The dataset includes information on population presence and vulnerability,
  access constraints, availability of basic services, market functionality, infrastructure
  damage, and cash feasibility. Each record reflects a specific assessment round in
  a given settlement and contributes to tracking humanitarian access and service availability
  in hard-to-reach and high-risk areas. The dataset is intended to provide operational
  data for humanitarian organisations and prompt further assessment and/or principled
  response.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/ukraine]'
details: SLAC data is collected through direct observation and key informant interviews
  by trained field teams using a harmonised tool. While it offers timely, settlement-level
  insights, it is not statistically representative and reflects conditions at the
  time of visit. Access challenges, limited civilian presence, or security risks may
  constrain data completeness. In some cases, data is based solely on observation
  or information from neighbouring areas. Findings are intended to support operational
  planning, access monitoring, and response feasibility rather than replace multisectoral
  needs assessments.
exposure:
- asset_type:
    description: Civilian population presence and demographic composition at settlement
      level
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
    description: Basic services infrastructure and facilities availability including
      health, water, and market functionality
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: CC-BY-4.0
lineage:
  description: Settlement-level data collected through direct observation and key
    informant interviews across eastern Ukraine, organized into demographic, security,
    access, services, infrastructure, and cash feasibility blocks. Multiple assessment
    rounds (August 2024 - February 2025) tracked changes in humanitarian conditions
    and infrastructure status in conflict-affected areas.
  sources:
  - id: source_1
    license: null
    name: AQLITY
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/ukraine
  rel: source
loss:
  losses:
  - asset_category: infrastructure
    asset_dimension: structure
    description: Infrastructure damage and service disruption from conflict-related
      security incidents
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
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
    description: Affected civilian population and vulnerability indicators from conflict
      exposure
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
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
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Ukraine - Frontline Monitoring (AQLITY_dataset 082024_022025.xlsx)
  download_url: https://data.humdata.org/dataset/0b24b3cf-6463-48c7-8201-7e6d87f629d6/resource/ed35c7f7-ec33-4ead-b3c1-e58632032262/download/aqlity_dataset-082024_022025.xlsx
  format: null
  id: resource_ed35c7f7
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: AQLITY_dataset 082024_022025.xlsx
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-ukr_aqlity_frontlinemonitoring_2024
spatial:
  bbox: null
  centroid: null
  countries:
  - UKR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-02-20'
  start: '2024-08-20'
temporal_resolution: null
title: Ukraine - Frontline Monitoring
version: null
vulnerability: null
---
