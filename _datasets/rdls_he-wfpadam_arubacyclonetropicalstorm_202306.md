---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP ADAM
    url: https://data.humdata.org/dataset/aruba-cyclone-1000977
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/aruba-cyclone-1000977
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/aruba-cyclone-1000977
dataset_id: rdls_he-wfpadam_arubacyclonetropicalstorm_202306
description: 'ADAM ID: 1000977_4 Cyclone (tropical storm) during the period Jun 19
  2023-Jun 24 2023 in Colombia, Venezuela, Aruba, Netherlands Antilles, Grenada, Saint
  Vincent and the Grenadines, Martinique, Saint Lucia, Barbados. It impacted 0 people..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/aruba-cyclone-1000977]'
details: null
exposure:
- asset_type:
    description: Population exposed to tropical cyclone winds in affected countries
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
license: CC-BY-SA-4.0
lineage:
  description: WFP ADAM collected and mapped tropical cyclone track data and wind
    speed measurements from the June 2023 tropical storm event affecting the Caribbean
    region. The shapefile contains observed storm track geometry with associated wind
    speed and alert level attributes derived from meteorological monitoring.
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
- href: https://data.humdata.org/dataset/aruba-cyclone-1000977
  rel: source
loss: null
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
  description: 'Aruba: Cyclone - Tropical storm - Jun 2023 (Shape File)'
  download_url: https://data.humdata.org/dataset/b4dfe0f5-65a8-4e05-ba66-9b2d306f2277/resource/549ef1b2-dde7-4443-9a88-53b5c66cb2d4/download/1000977-22-adam-ts-1000977-22-shp.zip
  format: null
  id: resource_549ef1b2
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 1000977-22-adam-ts-1000977-22-shp.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-wfpadam_arubacyclonetropicalstorm_202306
spatial:
  bbox: null
  centroid: null
  countries:
  - ABW
  - COL
  - VEN
  - GRD
  - VCT
  - MTQ
  - LCA
  - BRB
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-06-24'
  start: '2023-06-19'
temporal_resolution: null
title: 'Aruba: Cyclone - Tropical storm - Jun 2023'
version: null
vulnerability: null
---
