---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP ADAM
    url: https://data.humdata.org/dataset/bangladesh-cyclone-1000976
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/bangladesh-cyclone-1000976
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/bangladesh-cyclone-1000976
dataset_id: rdls_he-bgdindmmr_wfpadam_cyclonetropicalstormjun20_202306
description: 'ADAM ID: 1000976_2 Cyclone (tropical storm) during the period Jun 09
  2023-Jun 10 2023 in Bangladesh, Myanmar, India. It impacted 0 people.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/bangladesh-cyclone-1000976]'
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
  type: strong_wind
license: CC-BY-SA-4.0
lineage:
  description: WFP ADAM collected and mapped observed tropical cyclone track and wind
    speed data from the June 2023 event affecting Bangladesh, Myanmar, and India.
    The shapefile contains event episode information, cyclone classification, wind
    speed measurements, and population exposure data aggregated from operational emergency
    response monitoring.
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
- href: https://data.humdata.org/dataset/bangladesh-cyclone-1000976
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
  description: 'Bangladesh: Cyclone - Tropical storm - Jun 2023 (Shape File)'
  download_url: https://data.humdata.org/dataset/8dda3ee9-10a9-46e9-8379-94d747b36ef6/resource/b2b5cf58-e6d2-4976-9e9e-c2574b11ad28/download/1000976-4-adam-ts-1000976-4-shp.zip
  format: null
  id: resource_b2b5cf58
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 1000976-4-adam-ts-1000976-4-shp.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-bgdindmmr_wfpadam_cyclonetropicalstormjun20_202306
spatial:
  bbox: null
  centroid: null
  countries:
  - BGD
  - MMR
  - IND
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-06-10'
  start: '2023-06-09'
temporal_resolution: null
title: 'Bangladesh: Cyclone - Tropical storm - Jun 2023'
version: null
vulnerability: null
---
