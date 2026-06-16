---
attributions:
- entity:
    affiliation: null
    email: null
    name: Humanitarian partners
    url: https://data.humdata.org/dataset/south-sudan-flood-data
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA South Sudan
  url: https://data.humdata.org/dataset/south-sudan-flood-data
creator:
  affiliation: null
  email: null
  name: OCHA South Sudan
  url: https://data.humdata.org/dataset/south-sudan-flood-data
dataset_id: rdls_lss-ssd_ochassd_flooddata_2021
description: 'Reported number of flood-affected people by county and state in South
  Sudan.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/south-sudan-flood-data]'
details: The numbers reflect people who have been assessed and verified as affected
  to date, and might not be a reflection of all those affected. The figures reflect
  the number of people 'affected' but not displaced, who will be a subset of those
  affected. There was no significant flooding reported 2023. In 2024, the rainy season
  has not resulted in flooding yet
exposure: []
hazard: null
license: https://creativecommons.org/publicdomain/zero/1.0/
lineage:
  description: Post-event flood impact data compiled from direct observational reports
    and anecdotal information provided by humanitarian partners operating in South
    Sudan, aggregated by administrative divisions (counties and states) to produce
    time-series records of affected and displaced populations from 2012-2024.
  sources:
  - id: source_1
    license: null
    name: Humanitarian partners
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/south-sudan-flood-data
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Reported number of people affected by floods across South Sudan counties
      and states
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
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Reported number of people displaced by floods across South Sudan
      counties and states
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
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Summary of South Sudan flood-affected people by county and state as
    of 11th November 2025.
  download_url: https://data.humdata.org/dataset/70cefa0a-e4bd-481e-b773-20c2a462ea2e/resource/eb064156-f948-4520-8e2c-3b271badbd5c/download/ss_people_affected_and_displaced_by_floods_20251130.xlsx
  format: null
  id: resource_eb064156
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SS_People_Affected_and_Displaced_by_Floods_20251130.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Initial reports from field locations in South Sudan of flood-affected
    people by county and state as of 5th December 2024.
  download_url: https://data.humdata.org/dataset/70cefa0a-e4bd-481e-b773-20c2a462ea2e/resource/eed79fad-e7d2-4890-881d-de8e0ec88a41/download/ssd_flood_response_20122024.xlsx
  format: null
  id: resource_eed79fad
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SSD_Flood_Response_20122024.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Initial reports from field locations in South Sudan of flood-affected
    people by county and state as of end of November 2024
  download_url: https://data.humdata.org/dataset/70cefa0a-e4bd-481e-b773-20c2a462ea2e/resource/918b0b51-30d3-4d46-b0c5-1688bdf27b8e/download/ssd_flood_response_301122.xlsx
  format: null
  id: resource_918b0b51
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SSD_floods_301122.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Initial reports from field locations in South Sudan of flood-affected
    people by county and state as of 21 October 2022.
  download_url: https://data.humdata.org/dataset/70cefa0a-e4bd-481e-b773-20c2a462ea2e/resource/bfa47921-2a7b-43e4-b08d-fb4dfec8326e/download/ssd_flood_response_211022.xlsx
  format: null
  id: resource_bfa47921
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SSD_floods_211022.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Initial reports from field locations in South Sudan of flood-affected
    people by county and state as of 13 December 2021.
  download_url: https://data.humdata.org/dataset/70cefa0a-e4bd-481e-b773-20c2a462ea2e/resource/1f91a97c-5c60-4375-8e5d-8967f764cbac/download/ss_floodsaffected_people_20211213.xlsx
  format: null
  id: resource_1f91a97c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SSD_floods_131221.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ssd_ochassd_flooddata_2021
spatial:
  bbox: null
  centroid: null
  countries:
  - SSD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-11-30'
  start: '2021-04-01'
temporal_resolution: null
title: 'South Sudan: Flood Data'
version: null
vulnerability: null
---
