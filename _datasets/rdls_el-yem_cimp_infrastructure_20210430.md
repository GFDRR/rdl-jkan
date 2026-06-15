---
attributions:
- entity:
    affiliation: null
    email: null
    name: Civilian Impact Monitoring Project (CIMP)
    url: https://data.humdata.org/dataset/yemen-impact-on-civilian-infrastructure
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Civilian Impact Monitoring Project (inactive)
  url: https://data.humdata.org/dataset/yemen-impact-on-civilian-infrastructure
creator:
  affiliation: null
  email: null
  name: Civilian Impact Monitoring Project (inactive)
  url: https://data.humdata.org/dataset/yemen-impact-on-civilian-infrastructure
dataset_id: rdls_el-yem_cimp_infrastructure_20210430
description: 'The Civilian Impact Monitoring Project (CIMP) is a monitoring mechanism
  for real-time collection, analysis and dissemination of open source data on the
  civilian impact from armed violence in Yemen, with the purpose of informing and
  complementing protection programming. CIMP is a service under the United Nations
  Protection Cluster for Yemen and, since going live on 01 August 2018, has reported
  in real-time on the impact of incidents of armed violence on civilians at the national
  level, divided into 5 hubs: Al-Hudaydah, Sa''ada, Sana''a, Aden and Ibb. The dataset
  shows the number of incidents to have impacted upon civilian houses, farms, vehicles,
  businesses and markets and the number of incidents to have impacted upon civilian
  infrastructure sites since December 2017.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/yemen-impact-on-civilian-infrastructure]'
details: null
exposure:
- asset_type:
    description: Civilian infrastructure facilities and structures exposed to armed
      violence
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: CIMP collects open source data on armed violence incidents affecting
    civilians in Yemen through real-time monitoring across 5 regional hubs (Al-Hudaydah,
    Sa'ada, Sana'a, Aden, Ibb). Incident data are analyzed to quantify direct damage
    to civilian infrastructure and structures, with results disseminated to inform
    UN Protection Cluster programming.
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
- href: https://data.humdata.org/dataset/yemen-impact-on-civilian-infrastructure
  rel: source
loss:
  losses:
  - asset_category: infrastructure
    asset_dimension: structure
    description: Direct damage to civilian infrastructure from armed violence incidents
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
        metric: loss
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
  description: Number of incidents to have impacted upon civilian houses, farms, vehicles,
    businesses and markets since December 2017
  download_url: https://docs.google.com/spreadsheets/d/e/2PACX-1vTAsAy_THJFIDLIxrPWxpQ9saFxegIV_HXTTS20e3nfSxT22zBo-HY_8w4LjijXQxT_DcEGfPoUFvnB/pub?gid=246191683&single=true&output=csv
  format: null
  id: resource_e21a03c5
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Yemen_CIMP - Civilian Structure
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Number of incidents to have impacted upon civilian infrastructure sites
    since December 2017.
  download_url: https://docs.google.com/spreadsheets/d/e/2PACX-1vTAsAy_THJFIDLIxrPWxpQ9saFxegIV_HXTTS20e3nfSxT22zBo-HY_8w4LjijXQxT_DcEGfPoUFvnB/pub?gid=91397303&single=true&output=csv
  format: null
  id: resource_d0479d98
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Yemen_CIMP - Civilian Infrastructure damaged
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-yem_cimp_infrastructure_20210430
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
  end: null
  start: '2021-04-30'
temporal_resolution: null
title: Yemen Impact on Civilian Infrastructure.
version: null
vulnerability: null
---
