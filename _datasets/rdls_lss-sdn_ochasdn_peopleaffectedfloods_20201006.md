---
attributions:
- entity:
    affiliation: null
    email: null
    name: Government of Sudan - HAC
    url: https://data.humdata.org/dataset/sudan-people-affected-by-floods-as-of-6-october-2020
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Sudan
  url: https://data.humdata.org/dataset/sudan-people-affected-by-floods-as-of-6-october-2020
creator:
  affiliation: null
  email: null
  name: OCHA Sudan
  url: https://data.humdata.org/dataset/sudan-people-affected-by-floods-as-of-6-october-2020
dataset_id: rdls_lss-sdn_ochasdn_peopleaffectedfloods_20201006
description: 'The data shows the number of people, Household, houses damaged and destroyed
  by floods and was shared by the government of Sudan (HAC). [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/sudan-people-affected-by-floods-as-of-6-october-2020]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Post-event impact data collected from the field by the Government of
    Sudan Humanitarian Aid Commission (HAC) documenting people affected, households
    impacted, and buildings damaged or destroyed by floods, aggregated by state and
    locality.
  sources:
  - id: source_1
    license: null
    name: Government of Sudan - HAC
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/sudan-people-affected-by-floods-as-of-6-october-2020
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from flooding in Sudan
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
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population affected by flooding in Sudan
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
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Sudan People Affected by Floods (SDN_HAC_Flood data by state and locality_07102020.xlsx)
  download_url: https://data.humdata.org/dataset/6fbfb14c-5a27-44ff-86c6-9d028756f262/resource/9bcb9d2d-3bb5-432f-8e81-27265bbe93cd/download/sdn_hac_flood-data-by-state-and-locality_07102020.xlsx
  format: null
  id: resource_9bcb9d2d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SDN_HAC_Flood data by state and locality_07102020.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-sdn_ochasdn_peopleaffectedfloods_20201006
spatial:
  bbox: null
  centroid: null
  countries:
  - SDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2020-10-06'
temporal_resolution: null
title: Sudan People Affected by Floods
version: null
vulnerability: null
---
