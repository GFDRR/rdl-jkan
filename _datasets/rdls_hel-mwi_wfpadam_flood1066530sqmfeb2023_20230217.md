---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/malawi-flood-fl-20230217-mwi-01
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/malawi-flood-fl-20230217-mwi-01
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/malawi-flood-fl-20230217-mwi-01
dataset_id: rdls_hel-mwi_wfpadam_flood1066530sqmfeb2023_20230217
description: 'ADAM ID: FL-20230217-MWI-01 Flood covering 106653.0 sq m on Feb 17 2023
  in Malawi. It impacted 182158 people.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/malawi-flood-fl-20230217-mwi-01]'
details: null
exposure:
- asset_type:
    description: Total population in the flood-affected area
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
    description: Cropland area affected by flooding
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
  description: Post-event flood extent was mapped and analyzed by WFP ADAM following
    the February 17, 2023 flood in Malawi. Flood boundaries were delineated from geospatial
    analysis, overlaid with population and cropland datasets to quantify direct impacts
    (182,158 people affected, flooded cropland area calculated). Data compiled into
    multi-format geospatial products (GeoJSON, GeoTIFF, GeoPackage) for operational
    response.
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
- href: https://data.humdata.org/dataset/malawi-flood-fl-20230217-mwi-01
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Direct population affected by the February 2023 flood event in Malawi
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
    description: Direct cropland loss from flooding
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
  description: 'Malawi: Flood - 106653.0 sq m - Feb 2023 (GeoJSON File)'
  download_url: https://data.humdata.org/dataset/7e1f8b34-3e68-49e9-b7b4-29690d509546/resource/d9e2f9a4-1297-4562-b28a-e5908a01c6d5/download/fl-20230217-mwi-01.geojson
  format: null
  id: resource_d9e2f9a4
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20230217-MWI-01.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Malawi: Flood - 106653.0 sq m - Feb 2023 (GeoTIFF File)'
  download_url: https://data.humdata.org/dataset/7e1f8b34-3e68-49e9-b7b4-29690d509546/resource/f1157981-4bc1-432c-b0f8-119d6d5e109f/download/fl-20230217-mwi-01.tiff
  format: null
  id: resource_f1157981
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20230217-MWI-01.tiff
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Malawi: Flood - 106653.0 sq m - Feb 2023 (Geopackage File)'
  download_url: https://data.humdata.org/dataset/7e1f8b34-3e68-49e9-b7b4-29690d509546/resource/2d9e8b50-37ed-4c34-95c9-05ee84725c59/download/fl-20230217-mwi-01.gpkg
  format: null
  id: resource_2d9e8b50
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20230217-MWI-01.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Malawi: Flood - 106653.0 sq m - Feb 2023 (Metadata File)'
  download_url: https://data.humdata.org/dataset/7e1f8b34-3e68-49e9-b7b4-29690d509546/resource/9ee56118-2b9a-48ad-b853-914bcebec590/download/metadata.txt
  format: null
  id: resource_9ee56118
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
slug: rdls_hel-mwi_wfpadam_flood1066530sqmfeb2023_20230217
spatial:
  bbox: null
  centroid: null
  countries:
  - MWI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-02-17'
temporal_resolution: null
title: 'Malawi: Flood - 106653.0 sq m - Feb 2023'
version: null
vulnerability: null
---
