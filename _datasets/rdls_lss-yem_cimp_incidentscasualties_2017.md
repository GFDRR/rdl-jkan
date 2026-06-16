---
attributions:
- entity:
    affiliation: null
    email: null
    name: Civilian Impact Monitoring Project (CIMP)
    url: https://data.humdata.org/dataset/yemen-civilian-impact-incidents-and-civilian-casualties
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Civilian Impact Monitoring Project (inactive)
  url: https://data.humdata.org/dataset/yemen-civilian-impact-incidents-and-civilian-casualties
creator:
  affiliation: null
  email: null
  name: Civilian Impact Monitoring Project (inactive)
  url: https://data.humdata.org/dataset/yemen-civilian-impact-incidents-and-civilian-casualties
dataset_id: rdls_lss-yem_cimp_incidentscasualties_2017
description: 'The Civilian Impact Monitoring Project (CIMP) is a monitoring mechanism
  for real-time collection, analysis and dissemination of open source data on the
  civilian impact from armed violence in Yemen, with the purpose of informing and
  complementing protection programming. CIMP is a service under the United Nations
  Protection Cluster for Yemen and, since going live on 01 August 2018, has reported
  in real-time on the impact of incidents of armed violence on civilians at the national
  level, divided into 5 hubs: Al-Hudaydah, Sa''ada, Sana''a, Aden and Ibb. The dataset
  contains the total number of incidents of armed violence reported to have impacted
  upon civilians each month since December 2017, and the total number of civilian
  casualties reported each month and per hub.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/yemen-civilian-impact-incidents-and-civilian-casualties]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: CIMP collects open source data on armed violence incidents affecting
    civilians in Yemen through real-time monitoring across 5 regional hubs (Al-Hudaydah,
    Sa'ada, Sana'a, Aden, Ibb). Data is analyzed and disseminated to inform protection
    programming, with records aggregated into incident counts and casualty figures
    at the national level.
  sources:
  - id: source_1
    license: null
    name: Civilian Impact Monitoring Project (CIMP)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/yemen-civilian-impact-incidents-and-civilian-casualties
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Civilian deaths from armed violence incidents
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: casualty_count
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Civilian injuries from armed violence incidents
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: ppl_injured
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Civilian incidents from armed violence
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
    id: loss_3
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
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://civilianimpactmonitoring.org/methodology
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Yemen Civilian Impact Incidents and Civilian Casualties (Number of
    casualties per month)
  download_url: https://docs.google.com/spreadsheets/d/e/2PACX-1vTAsAy_THJFIDLIxrPWxpQ9saFxegIV_HXTTS20e3nfSxT22zBo-HY_8w4LjijXQxT_DcEGfPoUFvnB/pub?gid=360019480&single=true&output=csv
  format: null
  id: resource_ad496fd4
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Yemen_CIMP - Number of casualities
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Yemen Civilian Impact Incidents and Civilian Casualties (Number of
    incidents per hub and per month)
  download_url: https://docs.google.com/spreadsheets/d/e/2PACX-1vTAsAy_THJFIDLIxrPWxpQ9saFxegIV_HXTTS20e3nfSxT22zBo-HY_8w4LjijXQxT_DcEGfPoUFvnB/pub?gid=0&single=true&output=csv
  format: null
  id: resource_0d60b429
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Yemen_CIMP - Number of incidents
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-yem_cimp_incidentscasualties_2017
spatial:
  bbox: null
  centroid: null
  countries:
  - YEM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2021-04-01'
  start: '2017-12-01'
temporal_resolution: null
title: Yemen Civilian Impact Incidents and Civilian Casualties
version: null
vulnerability: null
---
