---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNHCR
    url: https://data.humdata.org/dataset/unhcr-bgd-msna-2019-june-v2-1
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: IOM Needs and Population Monitoring
    url: https://data.humdata.org/dataset/unhcr-bgd-msna-2019-june-v2-1
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: ACAPS
    url: https://data.humdata.org/dataset/unhcr-bgd-msna-2019-june-v2-1
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WFP VAM
    url: https://data.humdata.org/dataset/unhcr-bgd-msna-2019-june-v2-1
  id: attribution_4
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: REACH
    url: https://data.humdata.org/dataset/unhcr-bgd-msna-2019-june-v2-1
  id: attribution_5
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: UNHCR - The UN Refugee Agency
  url: https://data.humdata.org/dataset/unhcr-bgd-msna-2019-june-v2-1
creator:
  affiliation: null
  email: null
  name: UNHCR - The UN Refugee Agency
  url: https://data.humdata.org/dataset/unhcr-bgd-msna-2019-june-v2-1
dataset_id: rdls_el-bgd_unhcr_multisectorneedsassessmen_201906
description: 'In successive waves over four decades, Rohingya refugees have been fleeing
  to Bangladesh from Rakhine State, Myanmar, where they have suffered systematic ongoing
  persecution. Since August 2017, an estimated 745,000 Rohingya refugees have arrived
  in Cox''s Bazar, Bangladesh, increasing the total number of Rohingya refugees to
  more than 900,000. Most of the newly-arrived refugees have settled in hilly, formerly-forested
  areas that are vulnerable to landslides and flash-flooding in monsoon season and
  rely heavily on humanitarian assistance to cover their basic needs. As the crisis
  moves beyond the initial emergency phase, comprehensive information on the needs
  and vulnerabilities of affected populations is needed in order to inform the design
  and implementation of effective inter-sectoral programming. To this aim, a Joint
  Multi-Sector Needs Assessment (J-MSNA) was conducted across Rohingya refugee populations
  to support humanitarian planning and enhance operational and strategic decision-making.
  The J-MSNA was conducted in support of the mid-term review of the 2019 Joint Response
  Plan (JRP), with the specific objective of enabling the tracking of JRP 2019 indicators
  for monitoring and review purposes. A total of 876 households were surveyed across
  33 refugee sites. This J-MSNA was funded by UNHCR and coordinated through the MSNA
  Technical Working Group of the Information Management and Assessment Working Group
  (IMAWG), led by the Inter-Sector Coordination Group (ISCG) and comprised of: UNHCR,
  IOM Needs and Population Monitoring (NPM), ACAPS, WFP VAM, Translators without Borders,
  and REACH.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/unhcr-bgd-msna-2019-june-v2-1]'
details: The data must be requested via the resource download link
exposure:
- asset_type:
    description: Rohingya refugee population in Cox's Bazar camps surveyed for needs
      assessment
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
hazard: null
license: CC-BY-4.0
lineage:
  description: Household survey data collected from 876 households across 33 refugee
    sites in Cox's Bazar using simple random sampling of shelter footprints. Multi-sector
    needs assessment integrated data from UNHCR, IOM, ACAPS, WFP, and REACH to evaluate
    humanitarian needs across food security, health, shelter, and livelihoods in flood
    and landslide-vulnerable refugee settlements.
  sources:
  - id: source_1
    license: null
    name: UNHCR
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: IOM Needs and Population Monitoring
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: ACAPS
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_4
    license: null
    name: WFP VAM
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_5
    license: null
    name: REACH
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/unhcr-bgd-msna-2019-june-v2-1
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population needs and vulnerability assessment in flood-prone refugee
      settlements
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
    description: Population needs and vulnerability assessment in landslide-prone
      refugee settlements
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
- access_url: https://microdata.unhcr.org/index.php/auth/login/?destination=catalog/208/get-microdata
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Clicking 'Download' leads outside HDX where you can request access
    to the data in csv, xlsx & dta formats
  download_url: null
  format: null
  id: resource_78d2c92b
  media_type: text/html
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Bangladesh - Multi Sector Needs Assessment: Cox''s Bazar, Rohingya Refugee
    Response - June 2019'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bangladesh - Multi Sector Needs Assessment: Cox''s Bazar, Rohingya
    Refugee Response - June 2019 (Contains information about the dataset''s metadata
    and data)'
  download_url: https://microdata.unhcr.org/index.php/catalog/208/pdf-documentation
  format: null
  id: resource_07f7c826
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Codebook
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-bgd_unhcr_multisectorneedsassessmen_201906
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
  end: '2019-06-24'
  start: '2019-06-09'
temporal_resolution: null
title: 'Bangladesh - Multi Sector Needs Assessment: Cox''s Bazar, Rohingya Refugee
  Response - June 2019'
version: null
vulnerability: null
---
