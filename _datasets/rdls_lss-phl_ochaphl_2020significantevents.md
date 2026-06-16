---
attributions:
- entity:
    affiliation: null
    email: null
    name: Philippine government websites
    url: https://data.humdata.org/dataset/philippines-2020-significant-events
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Philippines
  url: https://data.humdata.org/dataset/philippines-2020-significant-events
creator:
  affiliation: null
  email: null
  name: OCHA Philippines
  url: https://data.humdata.org/dataset/philippines-2020-significant-events
dataset_id: rdls_lss-phl_ochaphl_2020significantevents
description: 'Consolidated information of different events happened in the Philippines
  in 2020 such, Taal volcano eruption, COVID-19, earthquakes, and typhoons.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/philippines-2020-significant-events]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Consolidated event data collected from multiple Philippine government
    websites documenting significant natural hazard events (volcanic, seismic, and
    meteorological) that occurred in 2020, cleaned and geocoded for spatial reference.
  sources:
  - id: source_1
    license: null
    name: Philippine government websites
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/philippines-2020-significant-events
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by Taal volcano eruption in 2020
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_volcanic
      intensity_measure: h_vaf:mm
      process: null
      trigger: null
      type: volcanic
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
    description: Population affected by earthquakes in 2020
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
    description: Population affected by typhoons in 2020
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
  description: 'PHILIPPINES: 2020 Significant events (Philippines_2020 Significant
    events.xlsx)'
  download_url: https://data.humdata.org/dataset/6a6dc47a-ee7d-4421-8f93-559f9b166fdc/resource/f423f5f9-c980-4a74-95d5-a1e4ac3820a2/download/philippines_2020-significant-events.xlsx
  format: null
  id: resource_f423f5f9
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Philippines_2020 Significant events.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-phl_ochaphl_2020significantevents
spatial:
  bbox: null
  centroid: null
  countries:
  - PHL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: 'PHILIPPINES: 2020 Significant events'
version: null
vulnerability: null
---
