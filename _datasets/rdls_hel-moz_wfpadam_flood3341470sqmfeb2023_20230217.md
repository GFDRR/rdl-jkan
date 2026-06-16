---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/mozambique-flood-fl-20230217-moz-00
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/mozambique-flood-fl-20230217-moz-00
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/mozambique-flood-fl-20230217-moz-00
dataset_id: rdls_hel-moz_wfpadam_flood3341470sqmfeb2023_20230217
description: 'ADAM ID: FL-20230217-MOZ-00 Flood covering 334147.0 sq m on Feb 17 2023
  in Mozambique. It impacted 204989 people.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/mozambique-flood-fl-20230217-moz-00]'
details: null
exposure:
- asset_type:
    description: Cropland area affected by flooding
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_1
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
- asset_type:
    description: Population directly affected by the flood event
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_2
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
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: WFP ADAM system collected and analyzed geospatial data and socio-economic
    information following the February 17, 2023 flood event in Mozambique. Flood extent
    was mapped and overlaid with population and cropland datasets to quantify directly
    affected populations and flooded agricultural areas. The resulting dataset aggregates
    observed hazard extent with exposure and impact metrics.
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
- href: https://data.humdata.org/dataset/mozambique-flood-fl-20230217-moz-00
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Direct population impact from February 2023 flood event in Mozambique
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
    description: Direct cropland area loss from flooding
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
  description: 'Mozambique: Flood - 334147.0 sq m - Feb 2023 (GeoJSON File)'
  download_url: https://data.humdata.org/dataset/fbea8d02-40ce-45e6-96fd-2af5b78127e5/resource/b0ea3878-e5e7-45ea-9e1c-52c84a7cd91e/download/fl-20230217-moz-00.geojson
  format: null
  id: resource_b0ea3878
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20230217-MOZ-00.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mozambique: Flood - 334147.0 sq m - Feb 2023 (GeoTIFF File)'
  download_url: https://data.humdata.org/dataset/fbea8d02-40ce-45e6-96fd-2af5b78127e5/resource/b03244c1-8e1a-47cf-8f7f-6fd527c39669/download/fl-20230217-moz-00.tiff
  format: null
  id: resource_b03244c1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20230217-MOZ-00.tiff
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mozambique: Flood - 334147.0 sq m - Feb 2023 (Geopackage File)'
  download_url: https://data.humdata.org/dataset/fbea8d02-40ce-45e6-96fd-2af5b78127e5/resource/945af654-410a-4585-a35d-57603bcd0fa7/download/fl-20230217-moz-00.gpkg
  format: null
  id: resource_945af654
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20230217-MOZ-00.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mozambique: Flood - 334147.0 sq m - Feb 2023 (Metadata File)'
  download_url: https://data.humdata.org/dataset/fbea8d02-40ce-45e6-96fd-2af5b78127e5/resource/3d00b119-1d3a-4f37-98ea-bbed1c50dd70/download/metadata.txt
  format: null
  id: resource_3d00b119
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
slug: rdls_hel-moz_wfpadam_flood3341470sqmfeb2023_20230217
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
  start: '2023-02-17'
temporal_resolution: null
title: 'Mozambique: Flood - 334147.0 sq m - Feb 2023'
version: null
vulnerability: null
---
