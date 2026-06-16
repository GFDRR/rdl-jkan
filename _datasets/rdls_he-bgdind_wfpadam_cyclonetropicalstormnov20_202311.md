---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/bangladesh-cyclone-1001034
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/bangladesh-cyclone-1001034
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/bangladesh-cyclone-1001034
dataset_id: rdls_he-bgdind_wfpadam_cyclonetropicalstormnov20_202311
description: 'ADAM ID: 1001034_4 Cyclone (tropical storm) during the period Nov 16
  2023-Nov 17 2023 in India, Bangladesh. It impacted 0 people.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/bangladesh-cyclone-1001034]'
details: null
exposure:
- asset_type:
    description: Population exposed to tropical cyclone wind speeds at 60 km/h threshold
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: ADAM collected observed tropical cyclone track and wind speed data
    during the November 16-17, 2023 event. Geospatial wind speed fields were mapped
    to administrative boundaries and intersected with gridded population data to estimate
    population exposure at the 60 km/h wind speed threshold across Bangladesh and
    India.
  sources:
  - id: source_1
    license: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/bangladesh-cyclone-1001034
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
  description: 'Bangladesh: Cyclone - Tropical storm - Nov 2023 (Shape File)'
  download_url: https://data.humdata.org/dataset/2fdd2689-b4d2-42d1-97b8-5e8b55fda4ef/resource/c201662e-54b5-4cdd-848e-4cb8a9ce8156/download/1001034-4-adam-ts-1001034-4-shp.zip
  format: null
  id: resource_c201662e
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 1001034-4-adam-ts-1001034-4-shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bangladesh: Cyclone - Tropical storm - Nov 2023 (Population Estimation)'
  download_url: https://data.humdata.org/dataset/2fdd2689-b4d2-42d1-97b8-5e8b55fda4ef/resource/7d8c5ad2-769b-451b-8792-e3ff36fd9fe9/download/1001034-4-adam-ts-1001034-4-pop-estimation.csv
  format: null
  id: resource_7d8c5ad2
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 1001034-4-adam-ts-1001034-4-pop-estimation.csv
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-bgdind_wfpadam_cyclonetropicalstormnov20_202311
spatial:
  bbox: null
  centroid: null
  countries:
  - BGD
  - IND
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-11-17'
  start: '2023-11-16'
temporal_resolution: null
title: 'Bangladesh: Cyclone - Tropical storm - Nov 2023'
version: null
vulnerability: null
---
