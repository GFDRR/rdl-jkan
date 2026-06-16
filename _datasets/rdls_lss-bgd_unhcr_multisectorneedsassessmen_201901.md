---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: UNHCR - The UN Refugee Agency
  url: https://data.humdata.org/dataset/unhcr-bgd-msna-2019-v2-1
creator:
  affiliation: null
  email: null
  name: UNHCR - The UN Refugee Agency
  url: https://data.humdata.org/dataset/unhcr-bgd-msna-2019-v2-1
dataset_id: rdls_lss-bgd_unhcr_multisectorneedsassessmen_201901
description: 'An estimated 738,000 Rohingya refugees have fled violence in Myanmar''s
  Rakhine state since August 25, 2017. Most of the refugees rely on humanitarian assistance,
  having left with few possessions and exhausted their financial resources on the
  journey. The cyclone and monsoon seasons, stretching from May to October, further
  threatened the living conditions of the vast majority of refugees living who are
  in makeshift shelters and settlements highly vulnerable to floods and landsides.
  To understand the evolving priority needs of the refugees, and to understand change
  over time, this Multi-Sector Needs Assessment (MSNA), coordinated by the United
  Nations High Commissioner for Refugees (UNHCR) and with technical support from REACH,
  was conducted in 33 refugee sites using a household survey methodology (3,165 households
  were surveyed). It is a follow up assessment to MSNA I in July 2018. Results of
  this MSNA are generalizable to the camp level with 95% confidence level and 10%
  margin of error. Support for questionnaire translation and enumerator language training
  was provided by Translators Without Borders.. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/unhcr-bgd-msna-2019-v2-1]'
details: The data must be requested via the resource download link
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Household survey data collected by UNHCR across 33 refugee sites in
    Cox's Bazar using stratified sampling methodology (95% confidence, 5-10% margin
    of error at camp level). The dataset captures multi-sector needs and vulnerabilities
    of 738,000 Rohingya refugees, including exposure to cyclone, monsoon, flood, and
    landslide hazards during May-October seasons, providing post-displacement impact
    assessment for humanitarian response planning.
  sources:
  - id: source_1
    license: null
    name: UNHCR - The UN Refugee Agency
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/unhcr-bgd-msna-2019-v2-1
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Multi-sector needs assessment capturing flood vulnerability and impact
      on refugee population in Cox's Bazar
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
    description: Multi-sector needs assessment capturing landslide vulnerability and
      impact on refugee population in Cox's Bazar
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
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
purpose: null
referenced_by: []
resources:
- access_url: https://microdata.unhcr.org/index.php/auth/login/?destination=catalog/137/get-microdata
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Clicking 'Download' leads outside HDX where you can request access
    to the data in csv, xlsx & dta formats
  download_url: null
  format: null
  id: resource_97ee6a0c
  media_type: text/html
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Bangladesh - Multi Sector Needs Assessment: Cox''s Bazar, Rohingya Refugee
    Response - January 2019'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bangladesh - Multi Sector Needs Assessment: Cox''s Bazar, Rohingya
    Refugee Response - January 2019 (Contains information about the dataset''s metadata
    and data)'
  download_url: https://microdata.unhcr.org/index.php/catalog/137/pdf-documentation
  format: null
  id: resource_3eed08a6
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Codebook
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-bgd_unhcr_multisectorneedsassessmen_201901
spatial:
  bbox: null
  centroid: null
  countries:
  - BGD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2019-01-26'
  start: '2019-01-08'
temporal_resolution: null
title: 'Bangladesh - Multi Sector Needs Assessment: Cox''s Bazar, Rohingya Refugee
  Response - January 2019'
version: null
vulnerability: null
---
