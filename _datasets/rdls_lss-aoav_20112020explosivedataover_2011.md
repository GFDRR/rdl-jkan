---
attributions:
- entity:
    affiliation: null
    email: null
    name: Action on Armed Violence (AOAV)
    url: https://data.humdata.org/dataset/aoav-2011-2017-explosive-violence-data-overview
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Action on Armed Violence
  url: https://data.humdata.org/dataset/aoav-2011-2017-explosive-violence-data-overview
creator:
  affiliation: null
  email: null
  name: Action on Armed Violence
  url: https://data.humdata.org/dataset/aoav-2011-2017-explosive-violence-data-overview
dataset_id: rdls_lss-aoav_20112020explosivedataover_2011
description: 'Action on Armed Violence (AOAV) monitors casualties from the use of
  explosive weapons worldwide based on English-language news media. This data provides
  an overview of the impact in the last decade.. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/aoav-2011-2017-explosive-violence-data-overview]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: AOAV systematically monitors English-language news media to identify
    and record incidents involving explosive weapons globally. Casualty data (deaths,
    injuries, affected persons) are extracted and compiled into an annual overview
    dataset covering 2011-2020, providing post-event impact records of explosive violence
    incidents.
  sources:
  - id: source_1
    license: null
    name: Action on Armed Violence (AOAV)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/aoav-2011-2017-explosive-violence-data-overview
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Casualty figures from explosive violence incidents monitored globally
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
    description: Injury counts from explosive violence incidents monitored globally
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
    description: Total affected population from explosive violence incidents monitored
      globally
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
  url: https://aoav.org.uk/explosiveviolence/methodology/
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: AOAV 2011-2020 Explosive violence data overview (Key Explosive Violence
    Dataset 2011-2020.xlsx)
  download_url: https://data.humdata.org/dataset/ffe30bca-75b4-4fdf-8b5a-23ede457be41/resource/44d1b07a-f097-4533-8672-4365a0ac9eb0/download/key-2011-2020-data.xlsx
  format: null
  id: resource_44d1b07a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Key Explosive Violence Dataset 2011-2020.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-aoav_20112020explosivedataover_2011
spatial:
  bbox: null
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-12-31'
  start: '2011-01-01'
temporal_resolution: null
title: AOAV 2011-2020 Explosive violence data overview
version: null
vulnerability: null
---
