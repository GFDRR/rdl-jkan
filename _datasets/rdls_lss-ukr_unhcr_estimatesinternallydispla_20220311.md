---
attributions:
- entity:
    affiliation: null
    email: null
    name: Protection Cluster Ukraine
    url: https://data.humdata.org/dataset/ukraine-estimates-on-internally-displaced-people
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UNHCR
    url: https://data.humdata.org/dataset/ukraine-estimates-on-internally-displaced-people
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: UNHCR - The UN Refugee Agency
  url: https://data.humdata.org/dataset/ukraine-estimates-on-internally-displaced-people
creator:
  affiliation: null
  email: null
  name: UNHCR - The UN Refugee Agency
  url: https://data.humdata.org/dataset/ukraine-estimates-on-internally-displaced-people
dataset_id: rdls_lss-ukr_unhcr_estimatesinternallydispla_20220311
description: 'Estimates of the number of internally displaced persons (IDPs) in Ukraine.
  The estimates are based on data received from authorities, partners, and colleagues
  present in the field. It considers a clusterized approach (applying various estimation
  methodology based on geographic location and context), on top of the historical
  data from the past, and the refugee flows. For any queries, please contact: ukraineinfomanagement@unhcr.org
  or protectionclusterukraine@unhcr.org. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/ukraine-estimates-on-internally-displaced-people]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: IDP estimates were generated through a clusterized estimation approach
    applied by the Protection Cluster Ukraine, integrating field reports from authorities
    and humanitarian partners with historical displacement data and refugee flow information.
    The methodology varies by geographic location and operational context to account
    for data availability and security constraints across Ukraine.
  sources:
  - id: source_1
    license: null
    name: Protection Cluster Ukraine
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: UNHCR
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/ukraine-estimates-on-internally-displaced-people
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons from conflict-related violence in Ukraine
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
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://www.understandingwar.org/
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Ukraine - Estimates on Internally Displaced People (Excel)
  download_url: https://data.humdata.org/dataset/697c4fb9-1b76-4a66-808a-9a8fb5ffff1a/resource/013ffdf6-1b14-4a25-a194-4acf82251c75/download/idp_estimation_08_03_2022-unhcr-protection-cluster_.xlsx
  format: null
  id: resource_013ffdf6
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: idp_estimation_08_03_2022-unhcr-protection-cluster
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ukr_unhcr_estimatesinternallydispla_20220311
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
  end: null
  start: '2022-03-11'
temporal_resolution: null
title: Ukraine - Estimates on Internally Displaced People
version: null
vulnerability: null
---
