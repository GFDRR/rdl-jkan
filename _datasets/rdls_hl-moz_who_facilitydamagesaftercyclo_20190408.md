---
attributions:
- entity:
    affiliation: null
    email: null
    name: Health Cluster Mozambique
    url: https://data.humdata.org/dataset/mozambique-health-facility-damages-after-cyclone-idai
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: MapAction
    url: https://data.humdata.org/dataset/mozambique-health-facility-damages-after-cyclone-idai
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: World Health Organization
  url: https://data.humdata.org/dataset/mozambique-health-facility-damages-after-cyclone-idai
creator:
  affiliation: null
  email: null
  name: World Health Organization
  url: https://data.humdata.org/dataset/mozambique-health-facility-damages-after-cyclone-idai
dataset_id: rdls_hl-moz_who_facilitydamagesaftercyclo_20190408
description: 'This dataset contains the shapefile of health facility damages due to
  Tropical Cyclone Idai as at 8 April 2019. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/mozambique-health-facility-damages-after-cyclone-idai]'
details: null
exposure: []
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-4.0
lineage:
  description: Health facility locations and damage status were collected through
    direct observational assessment and anecdotal reports by WHO and Health Cluster
    partners following Tropical Cyclone Idai in March 2019. Facility coordinates were
    georeferenced using OpenStreetMap and national administrative data (INE), and
    damage information was compiled into shapefiles documenting facility operational
    status as of 8 April 2019.
  sources:
  - id: source_1
    license: null
    name: World Health Organization
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Health Cluster Mozambique
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: MapAction
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/mozambique-health-facility-damages-after-cyclone-idai
  rel: source
loss:
  losses:
  - asset_category: infrastructure
    asset_dimension: structure
    description: Direct damage to health facility infrastructure from Tropical Cyclone
      Idai
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
        metric: loss
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
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
  description: 'Mozambique: Health Facility Damages After Cyclone Idai (Shapefile)'
  download_url: https://data.humdata.org/dataset/429d8571-0c3e-4697-8040-2bebf8d24e40/resource/d26e6d57-ea1d-4dce-a886-d49f99b68fe1/download/215_heal.zip
  format: null
  id: resource_d26e6d57
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 215_heal.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mozambique: Health Facility Damages After Cyclone Idai (Additional
    assessed health facilities not in included in the 215_heal.zip data.)'
  download_url: https://data.humdata.org/dataset/429d8571-0c3e-4697-8040-2bebf8d24e40/resource/232724ee-407d-4fbc-a4e6-849ce8bed58b/download/moz_missinghealthfacilities_2019mar.kmz
  format: null
  id: resource_232724ee
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MOZ_MissingHealthFacilities_2019Mar.kmz
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-moz_who_facilitydamagesaftercyclo_20190408
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
  end: null
  start: '2019-04-08'
temporal_resolution: null
title: 'Mozambique: Health Facility Damages After Cyclone Idai'
version: null
vulnerability: null
---
