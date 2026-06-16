---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/somalia-flood-fl-20231108-som-00
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/somalia-flood-fl-20231108-som-00
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/somalia-flood-fl-20231108-som-00
dataset_id: rdls_hel-som_wfpadam_flood3937490sqmnov2023_20231108
description: 'ADAM ID: FL-20231108-SOM-00 Flood covering 393749.0 sq m on Nov 08 2023
  in Somalia. It impacted 248941 people.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/somalia-flood-fl-20231108-som-00]'
details: null
exposure:
- asset_type:
    description: Total population in the flooded area
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: WFP ADAM collected and mapped geospatial flood extent data from the
    November 8, 2023 flood event in Somalia. Flood boundaries were delineated and
    overlaid with population and cropland datasets to quantify directly affected populations
    and agricultural losses. The resulting geodataset integrates hazard extent with
    exposure and impact metrics for operational response.
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
- href: https://data.humdata.org/dataset/somalia-flood-fl-20231108-som-00
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Direct population affected by the November 2023 flood event in Somalia
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
  description: 'Somalia: Flood - 393749.0 sq m - Nov 2023 (GeoJSON File)'
  download_url: https://data.humdata.org/dataset/21fbfc0d-fd14-4d36-bb8c-5e3b1a8f9747/resource/2abc8d74-bbfc-4d7e-97b6-4dec82002bd3/download/fl-20231108-som-00.geojson
  format: null
  id: resource_2abc8d74
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20231108-SOM-00.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Somalia: Flood - 393749.0 sq m - Nov 2023 (GeoTIFF File)'
  download_url: https://data.humdata.org/dataset/21fbfc0d-fd14-4d36-bb8c-5e3b1a8f9747/resource/35cedeb1-9882-4dbd-b32e-02eb7b1435d0/download/fl-20231108-som-00.tiff
  format: null
  id: resource_35cedeb1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20231108-SOM-00.tiff
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Somalia: Flood - 393749.0 sq m - Nov 2023 (Geopackage File)'
  download_url: https://data.humdata.org/dataset/21fbfc0d-fd14-4d36-bb8c-5e3b1a8f9747/resource/df11a7b6-28c7-4013-afd7-93c50832945c/download/fl-20231108-som-00.gpkg
  format: null
  id: resource_df11a7b6
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20231108-SOM-00.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Somalia: Flood - 393749.0 sq m - Nov 2023 (Metadata File)'
  download_url: https://data.humdata.org/dataset/21fbfc0d-fd14-4d36-bb8c-5e3b1a8f9747/resource/f0454007-45a8-4517-b420-a0dc607e6586/download/metadata.txt
  format: null
  id: resource_f0454007
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
slug: rdls_hel-som_wfpadam_flood3937490sqmnov2023_20231108
spatial:
  bbox: null
  centroid: null
  countries:
  - SOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-11-08'
temporal_resolution: null
title: 'Somalia: Flood - 393749.0 sq m - Nov 2023'
version: null
vulnerability: null
---
