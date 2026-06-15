---
attributions:
- entity:
    affiliation: null
    email: null
    name: "Instituto Nacional de Gest\xE3o e Redu\xE7\xE3o do Risco de Desastres (INGD)"
    url: https://data.humdata.org/dataset/impact-of-cyclones
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Mozambique
  url: https://data.humdata.org/dataset/impact-of-cyclones
creator:
  affiliation: null
  email: null
  name: OCHA Mozambique
  url: https://data.humdata.org/dataset/impact-of-cyclones
dataset_id: rdls_lss-moz_ochamoz_impactcyclones_2016
description: 'Impact of cyclones (people affected and injured by cyclones) in Mozambique
  from 2017 to 2025.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/impact-of-cyclones]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/publicdomain/zero/1.0/
lineage:
  description: Post-event impact data compiled by INGD from sample surveys documenting
    cyclone-affected and injured populations across Mozambique from 2017 to 2025,
    aggregated into national impact statistics.
  sources:
  - id: source_1
    license: null
    name: "Instituto Nacional de Gest\xE3o e Redu\xE7\xE3o do Risco de Desastres (INGD)"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/impact-of-cyclones
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by cyclones in Mozambique
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
    description: Population injured by cyclones in Mozambique
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
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Sample Survey
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: People affected by Cyclone Chido, Dikeledi and June from Dec 2024 -
    March 2025 disaggregated by sex and age group
  download_url: https://data.humdata.org/dataset/67d69410-1f2f-43eb-a522-1fe9633828ea/resource/683eba39-62b1-4d47-bf68-d027e1b3ade9/download/moz_2025-cyclones-people-affected-april-2025.xlsx
  format: null
  id: resource_683eba39
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MOZ_2025 Cyclones-People Affected
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Number of people affected and impacts by cyclones by admin 2 in Mozambique
    from 2017 to 2024.
  download_url: https://data.humdata.org/dataset/67d69410-1f2f-43eb-a522-1fe9633828ea/resource/b487b498-c23f-4fdc-b92a-83c0fd2da73b/download/cyclone_historical-data-2017-2024.xlsx
  format: null
  id: resource_b487b498
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Cyclone_Historical data 2017-2024.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-moz_ochamoz_impactcyclones_2016
spatial:
  bbox: null
  centroid: null
  countries:
  - MOZ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-03-31'
  start: '2016-10-01'
temporal_resolution: null
title: 'Mozambique: Impact of Cyclones'
version: null
vulnerability: null
---
