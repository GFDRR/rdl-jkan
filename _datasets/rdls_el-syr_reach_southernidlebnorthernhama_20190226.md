---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: REACH Initiative
  url: https://data.humdata.org/dataset/reach_southern_idleb_northern_hama_rapid_needs_assessment
creator:
  affiliation: null
  email: null
  name: REACH Initiative
  url: https://data.humdata.org/dataset/reach_southern_idleb_northern_hama_rapid_needs_assessment
dataset_id: rdls_el-syr_reach_southernidlebnorthernhama_20190226
description: 'Since the end of January 2019, southern Idleb and northern Hama governorates
  have seen a significant escalation of conflict. Shelling and airstrikes intensified
  in the area, leading to a deterioration of the humanitarian situation. In response,
  REACH conducted a rapid needs assessment to provide actors with an update on the
  humanitarian situation. The latest conflict escalation affects an area that is home
  to an estimated 700,000 residents and internally displaced persons (IDPs), increasing
  vulnerability, and in some cases, leading to secondary and tertiary displacements.
  From late 2017, the region has witnessed a large-scale influx of IDPs, following
  escalations of conflict and displacements from formerly opposition-held areas in
  south-east Idleb, south-west Aleppo, Rural Damascus, Homs, Hama, Dar''a and Quneitra
  governorates. The increase in IDP population in Idleb governorate and surrounding
  areas has led to a growing strain on resources and an increase in inter-communal
  tensions in the region. Further complicating the situation, there has been increasing
  concern regarding a potential military offensive in the region since September 2018,
  with shelling and airstrikes occurring with increased frequency. While the mid-September
  2018 announcement of a demilitarised zone put a pause on concerns over an imminent
  military offensive in the region, clashes have continued unabated. Data for this
  assessment was collected from 25-26 February 2019 in 85 opposition-controlled communities
  in 12 sub-districts via community-level key informant (KI) interviews. KIs were
  asked to report on the previous week (18 to 25 February). This dataset provides
  the findings for indicators on demographics, shelter, food, livelihoods, electricity
  & NFIs, WASH, health, education, protection, reported priority needs, and reported
  movement intentions.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/reach_southern_idleb_northern_hama_rapid_needs_assessment]'
details: Sub-districts were selected focusing on areas affected by increased airstrikes
  and shelling in the week(s) prior to data collection. Data was collected at the
  community level, with enumerators interviewing between 2 and 5 key informants (KIs)
  per community and with KIs selected based on their knowledge of IDP and resident
  populations in the community and sector-specific expertise. Communities were assessed
  based on available data on total populations, focusing on those reported to have
  large IDP and resident populations at the time of data collection. The definition
  of IDPs used by enumerators for this assessment was 'Individuals or groups of people
  who have been forced to leave their homes or places of habitual residence, in particular
  as a result of or in order to avoid the effects of armed conflict, situations of
  generalised violence, violations of human rights, or natural or man-made disasters,
  and who have not crossed an international border'. The definition of resident (pre-conflict)
  population was 'Individuals or groups of people who currently reside in their communities
  of origin, or communities of permanent residence prior to the Syrian conflict. This
  includes populations that were never displaced as well as previously displaced populations
  that have returned to their communities of origin'. Information should be considered
  as reflective of the situation at the time of data collection, given the dynamic
  situation in the region. In addition, information should be considered as indicative,
  and not representative, of the situation in the wider Idleb governorate and surrounding
  areas region.
exposure:
- asset_type:
    description: Internally displaced persons and resident population in southern
      Idleb and northern Hama
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: REACH conducted direct observational rapid needs assessments in southern
    Idleb and northern Hama governorates during February 2019 following conflict escalation.
    Field teams collected anecdotal and observational data on humanitarian impacts,
    population displacement, and sectoral needs across multiple domains (food security,
    health, shelter, WASH, education, livelihoods, NFI). Data was compiled into structured
    datasets documenting affected and displaced populations and humanitarian needs.
  sources:
  - id: source_1
    license: null
    name: REACH Initiative
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/reach_southern_idleb_northern_hama_rapid_needs_assessment
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by conflict-related shelling and airstrikes in
      southern Idleb and northern Hama
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
        metric: exposure
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Secondary and tertiary displacement of population due to conflict
      escalation
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
  description: REACH Rapid Needs Assessment for Southern Idleb and Northern Hama for
    13-16 December 2018. This dataset covers 69 communities in 7 sub-districts (Heish,
    Khan Shaykun, Tamanaah, Sanjar, Ma'arrat An Nu'man, Suran, Kafr Zeita).
  download_url: https://data.humdata.org/dataset/f97891e9-609a-4307-b472-b88191463d91/resource/6f584aee-b24e-41a8-a834-3cd94e4632c9/download/reach-idleb-rna-13-16-december-2018_18122018_cleaned.xlsx
  format: null
  id: resource_6f584aee
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: REACH Idleb RNA 13-16 December 2018_18122018_cleaned.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: REACH Rapid Needs Assessment for Southern Idleb and Northern Hama for
    25-26 February 2019. This dataset covers 85 communities across 12 sub-districts.
  download_url: https://data.humdata.org/dataset/f97891e9-609a-4307-b472-b88191463d91/resource/2377fc47-5534-4547-bf2d-0f906ba3dc49/download/reach_syr_dataset_southern-idleb-and-northern-hama-rna_25_26_february-2019.xlsx
  format: null
  id: resource_2377fc47
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: REACH_SYR_Dataset_Southern Idleb and Northern Hama RNA_25_26_February 2019.xlsx
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-syr_reach_southernidlebnorthernhama_20190226
spatial:
  bbox: null
  centroid: null
  countries:
  - SYR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2019-02-26'
temporal_resolution: null
title: Syrian Arab Republic - REACH Southern Idleb Northern Hama Rapid Needs Assessment
  25-26 February 2019
version: null
vulnerability: null
---
