---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/united-republic-of-tanzania-flood-fl-20231117-tza-00
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/united-republic-of-tanzania-flood-fl-20231117-tza-00
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/united-republic-of-tanzania-flood-fl-20231117-tza-00
dataset_id: rdls_hel-tza_wfpadam_unitedrepublicflood238073_20231117
description: 'ADAM ID: FL-20231117-TZA-00 Flood covering 238073.0 sq m on Nov 17 2023
  in Tanzania, United Republic of. It impacted 201641 people.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/united-republic-of-tanzania-flood-fl-20231117-tza-00]'
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
license: CC-BY-SA-4.0
lineage:
  description: WFP ADAM collected and mapped observed flood extent and socio-economic
    impact data following the 17 November 2023 flood event in Tanzania. Geospatial
    flood boundaries were delineated and overlaid with population and cropland datasets
    to quantify directly affected populations and agricultural losses. The resulting
    multi-format dataset (GeoJSON, GeoTIFF, GeoPackage) provides post-event impact
    assessment for humanitarian response.
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
- href: https://data.humdata.org/dataset/united-republic-of-tanzania-flood-fl-20231117-tza-00
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Direct population affected by the November 2023 flood event in Tanzania
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
  description: 'United Republic of Tanzania: Flood - 238073.0 sq m - Nov 2023 (GeoJSON
    File)'
  download_url: https://data.humdata.org/dataset/50d2467d-2b1c-418a-8a28-bb9fa1a910f1/resource/9ce11df7-1523-4dde-b1ed-8a58fb8f0eae/download/fl-20231117-tza-00.geojson
  format: null
  id: resource_9ce11df7
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20231117-TZA-00.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Republic of Tanzania: Flood - 238073.0 sq m - Nov 2023 (GeoTIFF
    File)'
  download_url: https://data.humdata.org/dataset/50d2467d-2b1c-418a-8a28-bb9fa1a910f1/resource/e58abe11-65d8-4975-909f-e118533fbd44/download/fl-20231117-tza-00.tiff
  format: null
  id: resource_e58abe11
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20231117-TZA-00.tiff
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Republic of Tanzania: Flood - 238073.0 sq m - Nov 2023 (Geopackage
    File)'
  download_url: https://data.humdata.org/dataset/50d2467d-2b1c-418a-8a28-bb9fa1a910f1/resource/ffc55a7b-6f0d-44e7-8d2f-5a1111447d0a/download/fl-20231117-tza-00.gpkg
  format: null
  id: resource_ffc55a7b
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20231117-TZA-00.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Republic of Tanzania: Flood - 238073.0 sq m - Nov 2023 (Metadata
    File)'
  download_url: https://data.humdata.org/dataset/50d2467d-2b1c-418a-8a28-bb9fa1a910f1/resource/618b3e48-9c1c-4678-8844-57d6032bd038/download/metadata.txt
  format: null
  id: resource_618b3e48
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
slug: rdls_hel-tza_wfpadam_unitedrepublicflood238073_20231117
spatial:
  bbox: null
  centroid: null
  countries:
  - TZA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-11-17'
temporal_resolution: null
title: 'United Republic of Tanzania: Flood - 238073.0 sq m - Nov 2023'
version: null
vulnerability: null
---
