---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNHCR
    url: https://data.humdata.org/dataset/unhcr-bgd-msna-2018-v2-1
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: UNHCR - The UN Refugee Agency
  url: https://data.humdata.org/dataset/unhcr-bgd-msna-2018-v2-1
creator:
  affiliation: null
  email: null
  name: UNHCR - The UN Refugee Agency
  url: https://data.humdata.org/dataset/unhcr-bgd-msna-2018-v2-1
dataset_id: rdls_lss-bgd_unhcr_multisectorneedsassessmen_201807
description: 'An estimated 723,000 Rohingya refugees have fled violence in Myanmar''s
  Rakhine state since August 25, 2017. Most of the newly-arrived refugees rely on
  humanitarian assistance, having left with few possessions and exhausted their financial
  resources during the journey. The monsoon season began in May and continues into
  September, threatening the vast majority of refugees living in makeshift shelters
  and settlements highly vulnerable to floods and landsides. To understand the priority
  needs of the refugees, a Multi-Sector Needs Assessment (MSNA), comissioned by UNHCR
  and with technical support from REACH, was conducted at the household level in 31
  refugee sites (3,171 households were surveyed). Translators Without Borders supported
  in questionnaire translation and enumerator training. This survey identified a number
  of areas where the basic needs of Rohingya refugees are being met. At the same time,
  this assessment has identified continuing service gaps in the Rohingya response.
  For example, the majority of households do not believe there is enough light at
  night to safely access latrines, and WASH facilities are generally perceived as
  dangerous areas for girls under age 18. In terms of access to protection services,
  only a small number of households report members making use of children and women
  friendly spaces. Despite widespread distribution coverage of key non-food items
  such as kitchen sets, demand for these items remains high, and refugees are spending
  the greatest portion of their limited financial resources on basic items including
  food, clothing and fuel. Findings suggest that there are uncertainties around actions
  to prepare for cyclones. The mahjis remain almost the sole focal point for communication
  and complaints with refugees, reflecting their continued prominent position within
  refugee communities. Finally, the median household debt is twice the median household
  income for the 30 days prior to data collection, with only two-fifths of households
  reporting any source of income at all.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/unhcr-bgd-msna-2018-v2-1]'
details: The data must be requested via the resource download link
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Household survey conducted by UNHCR across 31 of 34 refugee sites in
    Cox's Bazar during July 2018, capturing multi-sector needs (education, food security,
    health, shelter, facilities-infrastructure) of approximately 723,000 Rohingya
    refugees vulnerable to monsoon-driven floods and landslides. Data aggregated at
    household and individual levels to assess humanitarian impact and priority needs.
  sources:
  - id: source_1
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
- href: https://data.humdata.org/dataset/unhcr-bgd-msna-2018-v2-1
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Multi-sector needs assessment of Rohingya refugee population affected
      by monsoon flooding and landslide hazards
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
    description: Multi-sector needs assessment of Rohingya refugee population affected
      by landslide hazards during monsoon season
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
- access_url: https://microdata.unhcr.org/index.php/auth/login/?destination=catalog/136/get-microdata
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Clicking 'Download' leads outside HDX where you can request access
    to the data in csv, xlsx & dta formats
  download_url: null
  format: null
  id: resource_91aa3dc2
  media_type: text/html
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Bangladesh - Multi Sector Needs Assessment: Cox''s Bazar, Rohingya Refugee
    Response - July 2018'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bangladesh - Multi Sector Needs Assessment: Cox''s Bazar, Rohingya
    Refugee Response - July 2018 (Contains information about the dataset''s metadata
    and data)'
  download_url: https://microdata.unhcr.org/index.php/catalog/136/pdf-documentation
  format: null
  id: resource_b20e6dcc
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
slug: rdls_lss-bgd_unhcr_multisectorneedsassessmen_201807
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
  end: '2018-07-31'
  start: '2018-07-02'
temporal_resolution: null
title: 'Bangladesh - Multi Sector Needs Assessment: Cox''s Bazar, Rohingya Refugee
  Response - July 2018'
version: null
vulnerability: null
---
