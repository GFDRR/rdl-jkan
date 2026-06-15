---
attributions:
- entity:
    affiliation: null
    email: null
    name: AIDR (Artificial Intelligence for Disaster Response)
    url: https://data.humdata.org/dataset/typhoon-mangkhut-2018-twitter-data
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Twitter
    url: https://data.humdata.org/dataset/typhoon-mangkhut-2018-twitter-data
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Qatar Computing Research Institute
  url: https://data.humdata.org/dataset/typhoon-mangkhut-2018-twitter-data
creator:
  affiliation: null
  email: null
  name: Qatar Computing Research Institute
  url: https://data.humdata.org/dataset/typhoon-mangkhut-2018-twitter-data
dataset_id: rdls_lss-phl_qcri_typhoonmangkhut2018twitte_201809
description: 'This is a Twitter dataset collected during the typhoon Mangkhut 2018
  in the Philippines. The data was collected, processed, and analyzed by the AIDR
  (http://aidr.qcri.org) platform using state of the art machine learning techniques.
  The data includes the reports of number of injured and dead people, infrastructure
  damage reports, missing or found people, urgent needs and donation offers for each
  hour. Due to Twitter TOS, we do not share full tweets content on HDX. Please contact
  us via HDX or on aidr.qcri@gmail.com to get tweet ids of the dataset along with
  a tool which can be used to rehydrate tweets from tweet ids.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/typhoon-mangkhut-2018-twitter-data]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Twitter data was collected during Typhoon Mangkhut 2018 in the Philippines
    and processed through the AIDR platform using deep learning techniques to automatically
    extract and classify disaster impact reports including injured/dead persons, infrastructure
    damage, missing/found people, urgent needs, and donation offers aggregated by
    hourly intervals.
  sources:
  - id: source_1
    license: null
    name: AIDR (Artificial Intelligence for Disaster Response)
    risk_data_type:
    - loss
    type: model
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Twitter
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/typhoon-mangkhut-2018-twitter-data
  rel: source
loss:
  losses:
  - asset_category: infrastructure
    asset_dimension: structure
    description: Infrastructure damage reports from Typhoon Mangkhut extracted from
      social media
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_1
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
  - asset_category: population
    asset_dimension: population
    description: Injured persons reported during Typhoon Mangkhut from social media
      analysis
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
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
    description: Fatalities reported during Typhoon Mangkhut from social media analysis
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_3
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
  url: http://aidr.qcri.org
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Typhoon Mangkhut, known in the Philippines as Typhoon Ompong, was an
    extremely powerful tropical cyclone that brought widespread damages to Guam, the
    Philippines and South China in mid September in 2018. This dataset was collected
    from Twitter during the typhoon Mangkhut. The dataset was processed and analyzed
    using the AIDR (http://aidr.qcri.org) platform.
  download_url: https://data.humdata.org/dataset/6504f826-7974-42ce-817a-49d87ea0a930/resource/0a9ae82c-5cfc-4dce-b5ae-fb878a69d46a/download/typhoon_mangkhut_2018_twitter_aidr_data_analysis.xlsx
  format: null
  id: resource_0a9ae82c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Typhoon_Mangkhut_2018_Twitter_AIDR_Data_Analysis.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-phl_qcri_typhoonmangkhut2018twitte_201809
spatial:
  bbox: null
  centroid: null
  countries:
  - PHL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2018-09-26'
  start: '2018-09-16'
temporal_resolution: null
title: Philippines - Typhoon Mangkhut 2018 Twitter Data
version: null
vulnerability: null
---
