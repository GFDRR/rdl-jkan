---
attributions:
- entity:
    affiliation: null
    email: null
    name: DTM (Displacement Tracking Matrix)
    url: https://data.humdata.org/dataset/somalia-harmonised-idp-figures
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: CCCM (Camp Coordination and Camp Management)
    url: https://data.humdata.org/dataset/somalia-harmonised-idp-figures
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Somalia
  url: https://data.humdata.org/dataset/somalia-harmonised-idp-figures
creator:
  affiliation: null
  email: null
  name: OCHA Somalia
  url: https://data.humdata.org/dataset/somalia-harmonised-idp-figures
dataset_id: rdls_lss-som_ochasom_harmonisedidpfigures_2025
description: 'Harmonised IDP data from DTM and CCCM covering all regions.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/somalia-harmonised-idp-figures]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Harmonised IDP figures compiled from DTM and CCCM data sources covering
    all regions of Somalia. Data collected through direct observational methods and
    anecdotal reports from humanitarian partners, consolidated into a unified spatial
    dataset of internally displaced persons.
  sources:
  - id: source_1
    license: null
    name: DTM (Displacement Tracking Matrix)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: CCCM (Camp Coordination and Camp Management)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/somalia-harmonised-idp-figures
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons from flood and other hazards in Somalia
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
        metric: displaced
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
  description: 'Somalia: Harmonised IDP figures (IDP consolidated file spatial results
    Sep2025 share.xlsx)'
  download_url: https://data.humdata.org/dataset/f0771914-3a30-4c79-8525-7d351fee3751/resource/445ce158-42fb-4221-9998-d04be2ee6b37/download/idp-consolidated-file-spatial-results-sep2025-share.xlsx
  format: null
  id: resource_445ce158
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: IDP consolidated file spatial results Sep2025 share.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-som_ochasom_harmonisedidpfigures_2025
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
  end: '2025-09-30'
  start: '2025-01-01'
temporal_resolution: null
title: 'Somalia: Harmonised IDP figures'
version: null
vulnerability: null
---
