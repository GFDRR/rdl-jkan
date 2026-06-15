---
attributions:
- entity:
    affiliation: null
    email: null
    name: NDRMC / DROMIC reports
    url: https://data.humdata.org/dataset/philippines-typhoon-impact-data-2014-2020
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Netherlands Red Cross - 510
  url: https://data.humdata.org/dataset/philippines-typhoon-impact-data-2014-2020
creator:
  affiliation: null
  email: null
  name: Netherlands Red Cross - 510
  url: https://data.humdata.org/dataset/philippines-typhoon-impact-data-2014-2020
dataset_id: rdls_lss-phl_nlrc510_typhoonimpactdata20142020_2014
description: 'This dataset has been consolidated from NDRMC / DROMIC reports from
  2014 - 2020 to summarize the number of people affected and houses damaged in the
  Philippines as a result of typhoons.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/philippines-typhoon-impact-data-2014-2020]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Post-event impact data were consolidated from NDRMC DROMIC PDF reports
    covering typhoon events in the Philippines from 2014-2020. The reports document
    direct impacts including affected population counts and damaged house counts aggregated
    at the national level for each typhoon event.
  sources:
  - id: source_1
    license: null
    name: NDRMC / DROMIC reports
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/philippines-typhoon-impact-data-2014-2020
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Direct population impact from typhoons
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
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from typhoons
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
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This dataset has been consolidated from NDRMC / DROMIC reports from
    2014 - 2020 to summarize the number of people affected and houses damaged in the
    Philippines as a result of typhoons.
  download_url: https://data.humdata.org/dataset/7579a8b1-0112-4447-8753-2dc64e246b12/resource/70fb3b7a-078c-40c7-b601-0b265a6c71df/download/typhonn-impacts.xlsx
  format: null
  id: resource_70fb3b7a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Philippines Typhoon Impact Data 2014-2020
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-phl_nlrc510_typhoonimpactdata20142020_2014
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
  end: '2022-12-01'
  start: '2014-01-01'
temporal_resolution: null
title: The Philippines - Typhoon Impact Data 2014 - 2020
version: null
vulnerability: null
---
