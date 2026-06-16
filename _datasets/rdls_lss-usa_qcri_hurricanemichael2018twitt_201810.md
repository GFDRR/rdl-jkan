---
attributions:
- entity:
    affiliation: null
    email: null
    name: Twitter
    url: https://data.humdata.org/dataset/hurricane-michael-2018-twitter-data
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: AIDR (Artificial Intelligence for Disaster Response)
    url: https://data.humdata.org/dataset/hurricane-michael-2018-twitter-data
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Qatar Computing Research Institute
  url: https://data.humdata.org/dataset/hurricane-michael-2018-twitter-data
creator:
  affiliation: null
  email: null
  name: Qatar Computing Research Institute
  url: https://data.humdata.org/dataset/hurricane-michael-2018-twitter-data
dataset_id: rdls_lss-usa_qcri_hurricanemichael2018twitt_201810
description: 'About the dataset: Hurricane Michael was the third-most intense Atlantic
  hurricane to make landfall in the United States in terms of pressure. This dataset
  was collected from Twitter during Hurricane Michael. The dataset was processed and
  analyzed using the AIDR (http://aidr.qcri.org) platform. Dataset Description: This
  is a Twitter dataset collected during Hurricane Michael 2018. The data was collected,
  processed, and analyzed by the AIDR (http://aidr.qcri.org) platform using state-of-the-art
  machine learning techniques. The data includes the number of injured and dead people,
  infrastructure damage reports, missing or found people, urgent needs and donation
  offers for each hour. Due to Twitter TOS, we do not share full tweets content on
  HDX. Please contact us via HDX or on aidr.qcri@gmail.com to get tweet ids of the
  dataset along with a tool which can be used to rehydrate tweets from tweet ids..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/hurricane-michael-2018-twitter-data]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Twitter data was collected during Hurricane Michael 2018 and processed
    through the AIDR platform using deep learning algorithms to automatically extract
    and classify impact reports including casualties, injuries, infrastructure damage,
    and displacement from unstructured social media text and imagery.
  sources:
  - id: source_1
    license: null
    name: Twitter
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: AIDR (Artificial Intelligence for Disaster Response)
    risk_data_type:
    - loss
    type: model
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/hurricane-michael-2018-twitter-data
  rel: source
loss:
  losses:
  - asset_category: infrastructure
    asset_dimension: structure
    description: Infrastructure damage reports from Hurricane Michael extracted from
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
    description: Injured persons from Hurricane Michael reported via Twitter
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
    description: Fatalities from Hurricane Michael reported via Twitter
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
  - asset_category: population
    asset_dimension: population
    description: Displaced persons from Hurricane Michael extracted from social media
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_4
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
  url: http://aidr.qcri.org
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This is a Twitter dataset collected during Hurricane Michael 2018.
    The data was collected, processed, and analyzed by the AIDR (http://aidr.qcri.org)
    platform using state-of-the-art machine learning techniques. The data includes
    the number of injured and dead people, infrastructure damage reports, missing
    or found people, urgent needs and donation offers for each hour. Due to Twitter
    TOS, we do not share full tweets content on HDX. Please contact us via HDX or
    on aidr.qcri@gmail.com to get tweet ids of the dataset along with a tool which
    can be used to rehydrate tweets from tweet ids.
  download_url: https://data.humdata.org/dataset/bc7525cb-a7ac-482f-8961-c5234d8c3275/resource/cf031d00-b817-4f6f-ac58-6bf74a000cb6/download/hurricane_michael_twitter_data_analysis_summarytable.xlsx
  format: null
  id: resource_cf031d00
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Hurricane_Michael_Twitter_Data_Analysis_SummaryTable.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-usa_qcri_hurricanemichael2018twitt_201810
spatial:
  bbox: null
  centroid: null
  countries:
  - USA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2018-10-20'
  start: '2018-10-10'
temporal_resolution: null
title: United States - Hurricane Michael 2018 Twitter Data
version: null
vulnerability: null
---
