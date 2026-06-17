---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/zambia-flood-fl-20230216-zmb-01
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/zambia-flood-fl-20230216-zmb-01
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/zambia-flood-fl-20230216-zmb-01
dataset_id: rdls_hel-zmb_wfpadam_flood36954210sqmfeb2023_20230216
description: 'ADAM ID: FL-20230216-ZMB-01 Flood covering 3695421.0 sq m on Feb 16
  2023 in Zambia. It impacted 452821 people.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/zambia-flood-fl-20230216-zmb-01]'
details: null
exposure:
- asset_type:
    description: Total population in flood-affected administrative areas
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
- asset_type:
    description: Cropland area within the flood extent
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_2
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
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
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: WFP ADAM system collected and analyzed geospatial data following the
    February 16, 2023 flood event in Zambia, delineating flood extent polygons and
    intersecting them with population and cropland datasets to quantify direct impacts.
    The resulting multi-format dataset (GeoJSON, GeoTIFF, GeoPackage) provides observed
    flood boundaries and impact metrics at district administrative levels.
  sources:
  - id: source_1
    license: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/zambia-flood-fl-20230216-zmb-01
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Direct population affected by February 2023 flood event in Zambia
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
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
  - asset_category: agriculture
    asset_dimension: product
    description: Direct cropland loss from flood inundation
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: flood
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
          unit: null
        metric: loss
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
  description: 'Zambia: Flood - 3695421.0 sq m - Feb 2023 (GeoJSON File)'
  download_url: https://data.humdata.org/dataset/3a5132e5-2be5-4e37-857c-8537ce1121e1/resource/7d35dda4-275f-4c3d-85d2-898e617e6190/download/fl-20230216-zmb-01.geojson
  format: null
  id: resource_7d35dda4
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20230216-ZMB-01.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Zambia: Flood - 3695421.0 sq m - Feb 2023 (GeoTIFF File)'
  download_url: https://data.humdata.org/dataset/3a5132e5-2be5-4e37-857c-8537ce1121e1/resource/bfdd9967-f006-4f00-a0b7-1fa0df3eeaa6/download/fl-20230216-zmb-01.tiff
  format: null
  id: resource_bfdd9967
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20230216-ZMB-01.tiff
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Zambia: Flood - 3695421.0 sq m - Feb 2023 (Geopackage File)'
  download_url: https://data.humdata.org/dataset/3a5132e5-2be5-4e37-857c-8537ce1121e1/resource/89bb8d1b-ef69-4688-832c-c979b5955e8e/download/fl-20230216-zmb-01.gpkg
  format: null
  id: resource_89bb8d1b
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20230216-ZMB-01.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Zambia: Flood - 3695421.0 sq m - Feb 2023 (Metadata File)'
  download_url: https://data.humdata.org/dataset/3a5132e5-2be5-4e37-857c-8537ce1121e1/resource/bfc2bae9-e85e-4a8c-80a5-30c6fda654f6/download/metadata.txt
  format: null
  id: resource_bfc2bae9
  media_type: text/plain
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: metadata.txt
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-zmb_wfpadam_flood36954210sqmfeb2023_20230216
spatial:
  bbox: null
  centroid: null
  countries:
  - ZMB
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-02-16'
temporal_resolution: null
title: 'Zambia: Flood - 3695421.0 sq m - Feb 2023'
version: null
vulnerability: null
---
