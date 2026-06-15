---
attributions:
- entity:
    affiliation: null
    email: null
    name: CSA
    url: https://data.humdata.org/dataset/mali-2015-2016-food-security-ipc-analysis
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WFP
    url: https://data.humdata.org/dataset/mali-2015-2016-food-security-ipc-analysis
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: FAO
    url: https://data.humdata.org/dataset/mali-2015-2016-food-security-ipc-analysis
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Food Security Cluster
    url: https://data.humdata.org/dataset/mali-2015-2016-food-security-ipc-analysis
  id: attribution_4
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Mali
  url: https://data.humdata.org/dataset/mali-2015-2016-food-security-ipc-analysis
creator:
  affiliation: null
  email: null
  name: OCHA Mali
  url: https://data.humdata.org/dataset/mali-2015-2016-food-security-ipc-analysis
dataset_id: rdls_lss-mli_ochamli_20152016foodsecurityipcan_20160429
description: 'The data represents the IPC (Integrated Food Security Phase Classification)
  analysis as of November 2015 for Mali and its related projection for June - August
  2016.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/mali-2015-2016-food-security-ipc-analysis]'
details: 'For more information please contact : marysap2@yahoo.fr'
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: IPC analysis conducted through sample survey methodology by the Food
    Security Cluster, integrating data from CSA, WFP, and FAO to classify population
    food insecurity phases and estimate affected populations in Mali for November
    2015 and projected June-August 2016 periods.
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
- href: https://data.humdata.org/dataset/mali-2015-2016-food-security-ipc-analysis
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population food insecurity classification and affected counts from
      drought-driven food security crisis
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
  description: 'Mali: 2015/2016 Food Security IPC analysis (Estimation of people in
    food insecurity per region as of november 2015)'
  download_url: https://data.humdata.org/dataset/1b06fe14-7d76-4442-a731-c002b29cb64d/resource/6d123d42-09d6-48d4-a512-57117aec394c/download/etape-4-tableau-5-estimation-des-populations-mali_2015-2016_vf.xlsx
  format: null
  id: resource_6d123d42
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Tableau 5 - Estimation des populations - MALI_2015-2016_nov.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mali: 2015/2016 Food Security IPC analysis (Estimation of people in
    food insecurity per region as of mars 2016)'
  download_url: https://data.humdata.org/dataset/1b06fe14-7d76-4442-a731-c002b29cb64d/resource/b104a341-5356-415f-8f6e-464a55e069e1/download/etape-4-tableau-5-estimation-des-populations-mali_2015-2016_vf.xls
  format: null
  id: resource_b104a341
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Tableau 5 - Estimation des populations - MALI_2015-2016_mars.xls
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-mli_ochamli_20152016foodsecurityipcan_20160429
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
  end: null
  start: '2016-04-29'
temporal_resolution: null
title: 'Mali: 2015/2016 Food Security IPC analysis'
version: null
vulnerability: null
---
