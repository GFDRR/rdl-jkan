---
attributions:
- entity:
    affiliation: null
    email: null
    name: CSA
    url: https://data.humdata.org/dataset/2014-2015-food-security-ipc-analysis
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WFP
    url: https://data.humdata.org/dataset/2014-2015-food-security-ipc-analysis
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: FAO
    url: https://data.humdata.org/dataset/2014-2015-food-security-ipc-analysis
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Food Security Cluster
    url: https://data.humdata.org/dataset/2014-2015-food-security-ipc-analysis
  id: attribution_4
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Mali
  url: https://data.humdata.org/dataset/2014-2015-food-security-ipc-analysis
creator:
  affiliation: null
  email: null
  name: OCHA Mali
  url: https://data.humdata.org/dataset/2014-2015-food-security-ipc-analysis
dataset_id: rdls_lss-mli_ochamli_20142015foodsecurityipcan_2005
description: 'The data represents the IPC (Integrated Food Security Phase Classification)
  analysis as of March 2015 for Mali and its related projection for June - August
  2015.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/2014-2015-food-security-ipc-analysis]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: IPC analysis conducted through sample survey methodology by the Food
    Security Cluster, integrating data from CSA, WFP, and FAO to classify food insecurity
    phases and project food security conditions for Mali from March 2015 baseline
    through June-August 2015 projection period.
  sources:
  - id: source_1
    license: null
    name: CSA
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: WFP
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: FAO
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_4
    license: null
    name: Food Security Cluster
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/2014-2015-food-security-ipc-analysis
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Food insecurity classification and affected population from drought-driven
      food security crisis
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
  description: 'Mali: 2014/2015 Food Security IPC analysis (2015 Food Security IPC
    analysis- MALI_ VF.xlsx)'
  download_url: https://data.humdata.org/dataset/0aa6e8ee-5961-4e08-a6fc-1a5436daf257/resource/78ff5664-ee87-41ae-9f27-e24a7998697b/download/20142015-food-security-ipc-analysis-mali-vf.xlsx
  format: null
  id: resource_78ff5664
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2015 Food Security IPC analysis- MALI_ VF.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-mli_ochamli_20142015foodsecurityipcan_2005
spatial:
  bbox: null
  centroid: null
  countries:
  - MLI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2015-08-31'
  start: '2005-03-01'
temporal_resolution: null
title: 'Mali: 2014/2015 Food Security IPC analysis'
version: null
vulnerability: null
---
