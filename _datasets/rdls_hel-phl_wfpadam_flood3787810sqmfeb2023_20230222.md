---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/philippines-flood-fl-20230222-phl-00
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/philippines-flood-fl-20230222-phl-00
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/philippines-flood-fl-20230222-phl-00
dataset_id: rdls_hel-phl_wfpadam_flood3787810sqmfeb2023_20230222
description: 'ADAM ID: FL-20230222-PHL-00 Flood covering 378781.0 sq m on Feb 22 2023
  in Philippines. It impacted 2261305 people.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/philippines-flood-fl-20230222-phl-00]'
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
    description: Cropland area within flood-affected zones
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
license: CC-BY-SA-4.0
lineage:
  description: WFP ADAM system collected and analyzed geospatial data following the
    February 22, 2023 flood event in Philippines, mapping flood extent (378,781 sq
    m) and overlaying with population and cropland datasets to quantify direct impacts.
    Data aggregated by administrative boundaries (region, district) to produce impact
    dashboards and response assessments.
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
- href: https://data.humdata.org/dataset/philippines-flood-fl-20230222-phl-00
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Direct population affected by February 2023 flood event
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
    description: Direct cropland area impacted by flood inundation
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
  description: 'Philippines: Flood - 378781.0 sq m - Feb 2023 (GeoJSON File)'
  download_url: https://data.humdata.org/dataset/9c73549c-af70-4382-a75a-6faa03bc3cdf/resource/9f176088-123a-45a7-a4ed-38f1ae033082/download/fl-20230222-phl-00.geojson
  format: null
  id: resource_9f176088
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20230222-PHL-00.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Philippines: Flood - 378781.0 sq m - Feb 2023 (GeoTIFF File)'
  download_url: https://data.humdata.org/dataset/9c73549c-af70-4382-a75a-6faa03bc3cdf/resource/c9ac7963-e915-4cf0-a590-302e4a1f491a/download/fl-20230222-phl-00.tiff
  format: null
  id: resource_c9ac7963
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20230222-PHL-00.tiff
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Philippines: Flood - 378781.0 sq m - Feb 2023 (Geopackage File)'
  download_url: https://data.humdata.org/dataset/9c73549c-af70-4382-a75a-6faa03bc3cdf/resource/5f37f275-2aad-4e0b-aab6-880dfe530b50/download/fl-20230222-phl-00.gpkg
  format: null
  id: resource_5f37f275
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20230222-PHL-00.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Philippines: Flood - 378781.0 sq m - Feb 2023 (Metadata File)'
  download_url: https://data.humdata.org/dataset/9c73549c-af70-4382-a75a-6faa03bc3cdf/resource/6c73e244-1488-4ef7-9a7e-cf3c5a4b096f/download/metadata.txt
  format: null
  id: resource_6c73e244
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
slug: rdls_hel-phl_wfpadam_flood3787810sqmfeb2023_20230222
spatial:
  bbox: null
  centroid: null
  countries:
  - PHL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-02-22'
temporal_resolution: null
title: 'Philippines: Flood - 378781.0 sq m - Feb 2023'
version: null
vulnerability: null
---
