---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP ADAM
    url: https://data.humdata.org/dataset/india-cyclone-1000975
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/india-cyclone-1000975
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/india-cyclone-1000975
dataset_id: rdls_he-indpak_wfpadam_cyclonetropicalstormjun20_202306
description: 'ADAM ID: 1000975_37 Cyclone (tropical storm) during the period Jun 06
  2023-Jun 15 2023 in India, Pakistan. It impacted 0 people.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/india-cyclone-1000975]'
details: null
exposure:
- asset_type:
    description: Population exposed to tropical cyclone wind hazard
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard:
  event_sets_by_hazard_type:
    strong_wind:
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
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: WFP ADAM collected and mapped geospatial data on the June 2023 tropical
    cyclone event in India and Pakistan, including storm track geometry, wind speed
    measurements, and population exposure. The shapefile contains event-specific attributes
    including cyclone classification, wind speed, and alert levels derived from operational
    emergency response monitoring.
  sources:
  - id: source_1
    license: null
    name: WFP ADAM
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/india-cyclone-1000975
  rel: source
loss:
  losses: []
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
  description: 'India: Cyclone - Tropical storm - Jun 2023 (Shape File)'
  download_url: https://data.humdata.org/dataset/3af285ed-2a0b-4e93-9fcc-3560b4191e2f/resource/4c3f6942-e4cd-4445-8309-1e327ad41d90/download/1000975-39-adam-ts-1000975-39-shp.zip
  format: null
  id: resource_4c3f6942
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 1000975-39-adam-ts-1000975-39-shp.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-indpak_wfpadam_cyclonetropicalstormjun20_202306
spatial:
  bbox: null
  centroid: null
  countries:
  - IND
  - PAK
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-06-15'
  start: '2023-06-06'
temporal_resolution: null
title: 'India: Cyclone - Tropical storm - Jun 2023'
version: null
vulnerability: null
---
