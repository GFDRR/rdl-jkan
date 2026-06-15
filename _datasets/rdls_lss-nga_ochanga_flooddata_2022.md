---
attributions:
- entity:
    affiliation: null
    email: null
    name: National Emergency Management Agency (NEMA)
    url: https://data.humdata.org/dataset/nigeria-nema-flood-affected-geographical-areasnorth-east-nigeria-flood-affected-geographical-areas
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: State Emergency Management Agency (SEMA)
    url: https://data.humdata.org/dataset/nigeria-nema-flood-affected-geographical-areasnorth-east-nigeria-flood-affected-geographical-areas
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Nigeria
  url: https://data.humdata.org/dataset/nigeria-nema-flood-affected-geographical-areasnorth-east-nigeria-flood-affected-geographical-areas
creator:
  affiliation: null
  email: null
  name: OCHA Nigeria
  url: https://data.humdata.org/dataset/nigeria-nema-flood-affected-geographical-areasnorth-east-nigeria-flood-affected-geographical-areas
dataset_id: rdls_lss-nga_ochanga_flooddata_2022
description: 'The dataset contains information on flood-affected people and locations
  in Nigeria.. [Source: This metadata record was automatically extracted from the
  Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/nigeria-nema-flood-affected-geographical-areasnorth-east-nigeria-flood-affected-geographical-areas]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Post-event flood impact data collected through direct observation and
    anecdotal reports by OCHA Nigeria, NEMA, and SEMA partners across multiple years
    (2022-2025). Data aggregated at state, LGA, ward, and facility levels with demographic
    disaggregation of affected and displaced populations, plus infrastructure damage
    assessments. Spatial boundaries provided as shapefiles for administrative units.
  sources:
  - id: source_1
    license: null
    name: OCHA Nigeria
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: National Emergency Management Agency (NEMA)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: State Emergency Management Agency (SEMA)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/nigeria-nema-flood-affected-geographical-areasnorth-east-nigeria-flood-affected-geographical-areas
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Direct flood-affected population by demographic groups (children,
      women, men, elderly, PWD)
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
    description: Population displaced by flooding by demographic groups
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
  - asset_category: population
    asset_dimension: population
    description: Injuries resulting from flood events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_3
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
  - asset_category: infrastructure
    asset_dimension: structure
    description: Damage to facilities and infrastructure from flooding
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_4
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
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nigeria: Flood data (Number of affected people from Sept ''24 to Sept
    ''25)'
  download_url: https://data.humdata.org/dataset/4cc05f0e-e794-4541-8e99-2073ace1f237/resource/a49a2ce7-f9a4-4cb2-b9be-d7ae5a68cd85/download/bay_data_2025.xlsx
  format: null
  id: resource_a49a2ce7
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BAY_Data_2025.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nigeria: Flood data (Number of affected people from June to September
    2024)'
  download_url: https://data.humdata.org/dataset/4cc05f0e-e794-4541-8e99-2073ace1f237/resource/dfba2c08-a472-40b4-adea-fe5acb5b2491/download/floods-bay_states.csv
  format: null
  id: resource_dfba2c08
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Floods BAY_States 2024.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nigeria: Flood data (Number of affected people from April to August
    2023)'
  download_url: https://data.humdata.org/dataset/4cc05f0e-e794-4541-8e99-2073ace1f237/resource/91346a26-1109-4f45-940e-1b43c38059bc/download/nigeria-floods-2023.xlsx
  format: null
  id: resource_91346a26
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nigeria-floods-2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nigeria: Flood data (The number of people affected by floods as of
    November 2022.)'
  download_url: https://data.humdata.org/dataset/4cc05f0e-e794-4541-8e99-2073ace1f237/resource/833fe41d-1b92-4ca8-bfa0-8b483ed81690/download/nema-flood-data-06102022.xlsx
  format: null
  id: resource_833fe41d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NEMA Flood Data 06102022.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nigeria: Flood data (People affected by floods BAY area)'
  download_url: https://data.humdata.org/dataset/4cc05f0e-e794-4541-8e99-2073ace1f237/resource/20faeb75-3e45-4bfe-adef-1c6685b709c3/download/2022-flood-affected-areas-2022-by-lgas-as-of-30th-october-2022-3.csv
  format: null
  id: resource_20faeb75
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2022-flood-affected-areas-2022-by-lgas-as-of-30th-october-2022 (3).csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nigeria: Flood data (Shapefile)'
  download_url: https://data.humdata.org/dataset/4cc05f0e-e794-4541-8e99-2073ace1f237/resource/822d5519-2324-41e3-9077-8136afc0d3cf/download/2022_flood-affected_areas_2022_by_ward_as_of_8th_august.zip
  format: null
  id: resource_822d5519
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2022_Flood-affected_Areas_2022_by_Ward_as_of_8th_August.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nigeria: Flood data (Shapefile)'
  download_url: https://data.humdata.org/dataset/4cc05f0e-e794-4541-8e99-2073ace1f237/resource/8361b0f1-5880-4791-a531-071f6066e3b2/download/2022_flood-affected_areas_2022_by_lga_as_of_8th_august.zip
  format: null
  id: resource_8361b0f1
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2022_Flood-affected_Areas_2022_by_LGA_as_of_8th_August.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nigeria: Flood data (2022 Flood-affected Areas 2022 by LGA as of 8
    August 2022.csv)'
  download_url: https://data.humdata.org/dataset/4cc05f0e-e794-4541-8e99-2073ace1f237/resource/919f0acf-5d4c-45c4-8145-3290a65df67f/download/bylga-as-of-8-august-2022.csv
  format: null
  id: resource_919f0acf
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2022 Flood-affected Areas 2022 by LGA as of 8 August 2022.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nigeria: Flood data (2022 Flood-affected Areas by Ward as of 8 August
    2022.csv)'
  download_url: https://data.humdata.org/dataset/4cc05f0e-e794-4541-8e99-2073ace1f237/resource/56c8089d-b7da-40df-8cb8-d1423b6609d2/download/byward-as-of-8-august-2022.csv
  format: null
  id: resource_56c8089d
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2022 Flood-affected Areas by Ward as of 8 August 2022.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-nga_ochanga_flooddata_2022
spatial:
  bbox: null
  centroid: null
  countries:
  - NGA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-09-24'
  start: '2022-01-01'
temporal_resolution: null
title: 'Nigeria: Flood data'
version: null
vulnerability: null
---
