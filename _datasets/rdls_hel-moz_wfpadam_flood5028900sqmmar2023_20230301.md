---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/mozambique-flood-fl-20230301-moz-00
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/mozambique-flood-fl-20230301-moz-00
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/mozambique-flood-fl-20230301-moz-00
dataset_id: rdls_hel-moz_wfpadam_flood5028900sqmmar2023_20230301
description: 'ADAM ID: FL-20230301-MOZ-00 Flood covering 502890.0 sq m on Mar 01 2023
  in Mozambique. It impacted 401099 people.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/mozambique-flood-fl-20230301-moz-00]'
details: null
exposure:
- asset_type:
    description: Total population in the affected region
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
    description: Cropland area in the affected region
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
  description: WFP ADAM system collected and analysed geospatial data and socio-economic
    information following the March 2023 flood event in Mozambique. Flood extent was
    mapped and overlaid with population and cropland datasets to quantify directly
    affected populations and flooded agricultural areas. The resulting multi-layer
    geodataset integrates observed hazard extent with exposure and impact metrics
    for emergency response.
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
- href: https://data.humdata.org/dataset/mozambique-flood-fl-20230301-moz-00
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Direct population affected by the March 2023 flood event in Mozambique
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
    description: Direct cropland area impacted by flooding
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
  description: 'Mozambique: Flood - 502890.0 sq m - Mar 2023 (GeoJSON File)'
  download_url: https://data.humdata.org/dataset/da0bf933-67e8-4df6-864f-f3855d683f1d/resource/18ae23b3-9e84-461e-b2ab-5fa8cb076bc0/download/fl-20230301-moz-00.geojson
  format: null
  id: resource_18ae23b3
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20230301-MOZ-00.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mozambique: Flood - 502890.0 sq m - Mar 2023 (GeoTIFF File)'
  download_url: https://data.humdata.org/dataset/da0bf933-67e8-4df6-864f-f3855d683f1d/resource/a0548753-1c7c-443f-a1be-77d92f4bbae1/download/fl-20230301-moz-00.tiff
  format: null
  id: resource_a0548753
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20230301-MOZ-00.tiff
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mozambique: Flood - 502890.0 sq m - Mar 2023 (Geopackage File)'
  download_url: https://data.humdata.org/dataset/da0bf933-67e8-4df6-864f-f3855d683f1d/resource/37444472-5c14-4c44-a707-1594b5a43400/download/fl-20230301-moz-00.gpkg
  format: null
  id: resource_37444472
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20230301-MOZ-00.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mozambique: Flood - 502890.0 sq m - Mar 2023 (Metadata File)'
  download_url: https://data.humdata.org/dataset/da0bf933-67e8-4df6-864f-f3855d683f1d/resource/0e593fcd-9618-4101-944a-8e387e790ca4/download/metadata.txt
  format: null
  id: resource_0e593fcd
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
slug: rdls_hel-moz_wfpadam_flood5028900sqmmar2023_20230301
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
  start: '2023-03-01'
temporal_resolution: null
title: 'Mozambique: Flood - 502890.0 sq m - Mar 2023'
version: null
vulnerability: null
---
