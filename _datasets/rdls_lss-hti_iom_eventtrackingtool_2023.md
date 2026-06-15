---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/haiti-event-tracking-tool
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/haiti-event-tracking-tool
dataset_id: rdls_lss-hti_iom_eventtrackingtool_2023
description: 'Emergency Tracking Tool (ETT) is implemented in Haiti to collect information
  on large and sudden population movements as well as security and climatic emergencies
  in order to inform and advocate for rapid assistance to affected populations. Information
  is collected through phone interviews with key informants and direct observation..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/haiti-event-tracking-tool]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: The Emergency Tracking Tool collects post-event impact data on population
    movements and casualties from climatic and security emergencies in Haiti through
    phone interviews with key informants and direct field observation, following IOM's
    Displacement Tracking Matrix (DTM) standard methodology to quantify displacement
    and mobility impacts.
  sources:
  - id: source_1
    license: null
    name: International Organization for Migration (IOM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/haiti-event-tracking-tool
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population displacement from climatic emergencies including storms
      and flooding
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
        metric: displaced
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population displacement from climatic emergencies including flooding
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
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
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://displacement.iom.int/sites/default/files/public/Methodological%20Framework%20used%20in%20DTM%20Operations%20for%20Quantifying%20Displacement%20and%20Mobility.pdf
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Emergency Tracking Tool (ETT) is implemented in Haiti to collect information
    on large and sudden population movements as well as security and climatic emergencies
    in order to inform and advocate for rapid assistance to affected populations.
    Information is collected through phone interviews with key informants and direct
    observation. This dataset contains ETT data collected since January 2023 when
    the DTM Haiti begun implementing this activity, up to December 2024.
  download_url: https://data.humdata.org/dataset/0fa0d970-3be3-4722-b6e4-9146a5df3795/resource/63501b55-8300-41b8-a3f7-46c6d0bf042c/download/ett-dataset-as-of-december-2024_public-version-1_0.xlsx
  format: null
  id: resource_63501b55
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Haiti - Event Tracking Tool - 2023/2024
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-hti_iom_eventtrackingtool_2023
spatial:
  bbox: null
  centroid: null
  countries:
  - HTI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-12-31'
  start: '2023-01-01'
temporal_resolution: null
title: Haiti - Event Tracking Tool
version: null
vulnerability: null
---
