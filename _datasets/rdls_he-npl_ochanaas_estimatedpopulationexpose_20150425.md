---
attributions:
- entity:
    affiliation: null
    email: null
    name: WorldPoP Project
    url: https://data.humdata.org/dataset/estimated-population-exposed-to-earthquake-shaking
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: USGS-Pager
    url: https://data.humdata.org/dataset/estimated-population-exposed-to-earthquake-shaking
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: OCHA
    url: https://data.humdata.org/dataset/estimated-population-exposed-to-earthquake-shaking
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Needs Assessment and Analysis Section (NAAS) (inactive)
  url: https://data.humdata.org/dataset/estimated-population-exposed-to-earthquake-shaking
creator:
  affiliation: null
  email: null
  name: OCHA Needs Assessment and Analysis Section (NAAS) (inactive)
  url: https://data.humdata.org/dataset/estimated-population-exposed-to-earthquake-shaking
dataset_id: rdls_he-npl_ochanaas_estimatedpopulationexpose_20150425
description: 'Population data by district and severity class. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/estimated-population-exposed-to-earthquake-shaking]'
details: null
exposure:
- asset_type:
    description: Population by district exposed to earthquake ground shaking at different
      severity levels
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
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: PGA:g
      process: ground_motion
      trigger: null
      type: earthquake
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-4.0
lineage:
  description: USGS-Pager earthquake ground motion data (PGA severity classes) was
    intersected with WorldPoP gridded population distribution to estimate population
    exposure by district and shaking intensity level. Census administrative boundaries
    were used to aggregate results at the district level for needs assessment purposes.
  sources:
  - id: source_1
    license: null
    name: WorldPoP Project
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: USGS-Pager
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
  - id: source_3
    license: null
    name: OCHA
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/estimated-population-exposed-to-earthquake-shaking
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Census
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Estimated Population Exposed to Nepal Earthquake shaking (Excel)
  download_url: https://data.humdata.org/dataset/4ae4f428-f959-4413-b752-5736f19ed70d/resource/730c55b0-f4a5-49b6-a750-a223e5262867/download/pga-affecteddistricts-pop.xlsx
  format: null
  id: resource_730c55b0
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PGA_AffectedDistricts_POP.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Estimated Population Exposed to Nepal Earthquake shaking (CSV)
  download_url: https://data.humdata.org/dataset/4ae4f428-f959-4413-b752-5736f19ed70d/resource/3165c3f0-eb74-4d7b-bb8e-a1ae9e9c6586/download/pga-affecteddistricts-pop.csv
  format: null
  id: resource_3165c3f0
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PGA_AffectedDistricts_POP.csv
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-npl_ochanaas_estimatedpopulationexpose_20150425
spatial:
  bbox: null
  centroid: null
  countries:
  - NPL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-04-25'
temporal_resolution: null
title: Estimated Population Exposed to Nepal Earthquake shaking
version: null
vulnerability: null
---
