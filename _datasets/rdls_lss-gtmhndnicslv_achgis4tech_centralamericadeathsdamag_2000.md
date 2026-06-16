---
attributions:
- entity:
    affiliation: null
    email: null
    name: EM-DAT
    url: https://data.humdata.org/dataset/central-america-deaths-and-damages-in-usd-caused-by-disasters
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: "Acci\xF3n contra el hambre - GIS4tech"
  url: https://data.humdata.org/dataset/central-america-deaths-and-damages-in-usd-caused-by-disasters
creator:
  affiliation: null
  email: null
  name: "Acci\xF3n contra el hambre - GIS4tech"
  url: https://data.humdata.org/dataset/central-america-deaths-and-damages-in-usd-caused-by-disasters
dataset_id: rdls_lss-gtmhndnicslv_achgis4tech_centralamericadeathsdamag_2000
description: 'The dataset presents the number of affected people and the number of
  fatalities caused by natural disasters in El Salvador, Guatemala, Honduras, and
  Nicaragua, showing the variation over the years, differentiated by disaster type.
  The data have been assessed based on information obtained from EM-DAT. For more
  information contact GIS4Tech: info@gis4tech.com. You can also visit the PREDISAN
  platform https://predisan.gis4tech.com/ca4 for detailed, accurate information..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/central-america-deaths-and-damages-in-usd-caused-by-disasters]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Post-event impact data were extracted from the EM-DAT database, standardized,
    and compiled into tabular format covering deaths and affected populations by disaster
    type and year for El Salvador, Guatemala, Honduras, and Nicaragua.
  sources:
  - id: source_1
    license: null
    name: EM-DAT
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/central-america-deaths-and-damages-in-usd-caused-by-disasters
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Fatalities caused by flood disasters
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
        metric: death
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: People affected by flood disasters
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
  - asset_category: population
    asset_dimension: population
    description: Fatalities caused by earthquake disasters
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
        metric: death
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: People affected by earthquake disasters
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_4
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
    description: Fatalities caused by strong wind disasters
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_5
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: death
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: People affected by strong wind disasters
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_6
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
  description: Central America - Deaths and Damages in USD Caused by Disasters (Deaths
    and damages in USD caused by disasters by ACH-GIS4Tech.csv)
  download_url: https://data.humdata.org/dataset/e8c12839-2e06-4958-9d93-700b09d3355d/resource/0b5b6c7f-3aeb-46bb-8677-2d28e65299e7/download/deaths_damages_caused_by_disasters.csv
  format: null
  id: resource_0b5b6c7f
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: deaths_damages_caused_by_disasters.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-gtmhndnicslv_achgis4tech_centralamericadeathsdamag_2000
spatial:
  bbox: null
  centroid: null
  countries:
  - SLV
  - GTM
  - HND
  - NIC
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-07-01'
  start: '2000-01-01'
temporal_resolution: null
title: Central America - Deaths and Damages in USD Caused by Disasters
version: null
vulnerability: null
---
