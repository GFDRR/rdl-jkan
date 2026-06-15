---
attributions:
- entity:
    affiliation: null
    email: null
    name: Uganda Red Cross Society
    url: https://data.humdata.org/dataset/uganda-districts-affected-by-floods-and-rising-water-levels
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Uganda Red Cross Society (inactive)
  url: https://data.humdata.org/dataset/uganda-districts-affected-by-floods-and-rising-water-levels
creator:
  affiliation: null
  email: null
  name: Uganda Red Cross Society (inactive)
  url: https://data.humdata.org/dataset/uganda-districts-affected-by-floods-and-rising-water-levels
dataset_id: rdls_el-uga_ugrc_districtsaffectedfloodsri_20200612
description: 'This data is about Uganda Districts affected by Floods and Rising Water
  Levels in Lakes as of Friday, 12th June 2020. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/uganda-districts-affected-by-floods-and-rising-water-levels]'
details: This data is generated from Uganda Red Cross Society disaster reporting.
  For any queries, please contact Joel Kitutu (jkitutu@redcrossug.org).
exposure:
- asset_type:
    description: District-level population data including male, female, and total
      population counts
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
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Uganda Red Cross Society field disaster reports were collected and
    processed using QGIS software to generate a spatial dataset identifying districts
    affected by floods and rising water levels. The dataset integrates administrative
    district boundaries with population statistics and flood impact observations from
    June 2020.
  sources:
  - id: source_1
    license: null
    name: Uganda Red Cross Society
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/uganda-districts-affected-by-floods-and-rising-water-levels
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Districts affected by floods and rising water levels as of June 12,
      2020
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
  description: Layer of Uganda Districts affected by Floods and Rising Water Levels
    in Lakes as of Friday, 12th June 2020
  download_url: https://data.humdata.org/dataset/6241b9fd-712c-4588-9e41-6ad113cc7c53/resource/ff4084ef-72b8-4cf0-a454-b445ddfe4a50/download/map-of-uganda-showing-districts-affected-by-floods-and-rising-water-levels-in-lakes-as-of-friday.kml
  format: null
  id: resource_ff4084ef
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Map of Uganda Showing Districts affected by Floods and Rising Water Levels
    in Lakes as of Friday 12th June 2020.kml
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-uga_ugrc_districtsaffectedfloodsri_20200612
spatial:
  bbox: null
  centroid: null
  countries:
  - UGA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2020-06-12'
temporal_resolution: null
title: Uganda Districts affected by Floods and Rising Water Levels
version: null
vulnerability: null
---
