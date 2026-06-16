---
attributions:
- entity:
    affiliation: null
    email: null
    name: Twitter API
    url: https://data.humdata.org/dataset/turkiye-earthquake-feb-2023
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: AIDR system
    url: https://data.humdata.org/dataset/turkiye-earthquake-feb-2023
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Qatar Computing Research Institute
  url: https://data.humdata.org/dataset/turkiye-earthquake-feb-2023
creator:
  affiliation: null
  email: null
  name: Qatar Computing Research Institute
  url: https://data.humdata.org/dataset/turkiye-earthquake-feb-2023
dataset_id: rdls_lss-syrtur_qcri_earthquaketwitterdata_202302
description: "This resource provides important information about individuals who were\
  \ reported missing or stranded, requests and offers of shelter, and general calls\
  \ for assistance, such as requests for food and donations, from Twitter data collected\
  \ during The 2023 T\xFCrkiye-Syria earthquake. Additionally, the resource provides\
  \ damage reports collected from Twitter in the form of images. The data provides\
  \ district-level aggregation of particular type of information, raw data points,\
  \ population, and a district-level impact score. The data was collected using the\
  \ AIDR system (http://aidr.qcri.org/) and processed/analyzed using machine learning\
  \ and rule-based techniques.. [Source: This metadata record was automatically extracted\
  \ from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/turkiye-earthquake-feb-2023]"
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: "Twitter data was collected during the 2023 T\xFCrkiye-Syria earthquake\
    \ using AIDR (Artificial Intelligence for Disaster Response) system with earthquake-related\
    \ keywords. Raw tweets were processed through machine learning models and rule-based\
    \ systems to classify and aggregate information into district-level impact categories\
    \ including missing persons, shelter requests, assistance needs, and damage reports\
    \ with associated impact scores."
  sources:
  - id: source_1
    license: null
    name: Twitter API
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: AIDR system
    risk_data_type:
    - loss
    type: model
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/turkiye-earthquake-feb-2023
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessed from Twitter-sourced damage images
      and reports
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
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
  - asset_category: population
    asset_dimension: population
    description: Missing and stranded individuals reported via Twitter during the
      earthquake
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_2
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
    description: Population requiring shelter assistance as reported via Twitter
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_3
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
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The file contains district-level aggregation of geo-mapped reports
    of general help requests collected from Twitter. Additionally, an impact score
    is computed that yields a measure of the impact of the earthquake on each district
    based on general help requests also taking into account the district population
    and raw tweets.
  download_url: https://data.humdata.org/dataset/a22adc4d-4ae3-4252-a9ba-5d7278f17282/resource/ae7a53d1-7e09-4eaa-9790-13ddcb140e62/download/help_requests_twitter.xlsx
  format: null
  id: resource_ae7a53d1
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: help_requests_twitter.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The file contains district-level aggregation of geo-mapped reports
    of shelter requests collected from Twitter. Additionally, an impact score is computed
    that yields a measure of the impact of the earthquake on each district based on
    shelter requests also taking into account the district population and raw tweets.
  download_url: https://data.humdata.org/dataset/a22adc4d-4ae3-4252-a9ba-5d7278f17282/resource/ed7a25db-e2fb-402a-a433-e3da0b62d3c4/download/shelter_requests_twitter.xlsx
  format: null
  id: resource_ed7a25db
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: shelter_requests_twitter.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The file contains district-level aggregation of geo-mapped reports
    of missing or stranded people collected from Twitter. Additionally, an impact
    score is computed that yields a measure of the impact of the earthquake on each
    district based on missing people reports also taking into account the district
    population and raw tweets.
  download_url: https://data.humdata.org/dataset/a22adc4d-4ae3-4252-a9ba-5d7278f17282/resource/1e6539f1-d7c0-40d2-bfe9-09f4dd0485c7/download/missing_people_reports_twitter.xlsx
  format: null
  id: resource_1e6539f1
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: missing_people_reports_twitter.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The file contains district-level aggregation of geo-mapped damage reports
    in the form of images shared on Twitter. Additionally, an impact score is computed
    that yields a measure of the impact of the earthquake on each district based on
    damage reports also taking into account the district population and raw tweets.
  download_url: https://data.humdata.org/dataset/a22adc4d-4ae3-4252-a9ba-5d7278f17282/resource/3f8c3277-cd31-4952-884f-c8ebe2188a00/download/damage_images_twitter.xlsx
  format: null
  id: resource_3f8c3277
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: damage_images_twitter.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-syrtur_qcri_earthquaketwitterdata_202302
spatial:
  bbox: null
  centroid: null
  countries:
  - TUR
  - SYR
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-02-28'
  start: '2023-02-06'
temporal_resolution: null
title: "T\xFCrkiye Earthquake (Twitter data)"
version: null
vulnerability: null
---
