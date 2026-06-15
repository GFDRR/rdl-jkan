---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/kenya-flood-fl-20231121-ken-03
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/kenya-flood-fl-20231121-ken-03
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/kenya-flood-fl-20231121-ken-03
dataset_id: rdls_hel-ken_wfpadam_flood5437930sqmnov2023_20231121
description: 'ADAM ID: FL-20231121-KEN-03 Flood covering 543793.0 sq m on Nov 21 2023
  in Kenya. It impacted 242812 people.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/kenya-flood-fl-20231121-ken-03]'
details: null
exposure:
- asset_type:
    description: Total population in the affected flood area
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
  event_sets_by_hazard_type:
    flood:
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
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: WFP ADAM collected and mapped geospatial flood extent data and socio-economic
    information following the November 2023 flood event in Kenya. Flood boundaries
    were delineated from satellite or field observations, overlaid with population
    and cropland datasets to quantify direct impacts on people and agricultural assets.
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
- href: https://data.humdata.org/dataset/kenya-flood-fl-20231121-ken-03
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Direct population affected by the November 2023 flood event in Kenya
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
  description: 'Kenya: Flood - 543793.0 sq m - Nov 2023 (GeoJSON File)'
  download_url: https://data.humdata.org/dataset/f1b3e7d8-6fb9-4f43-846e-ff04e814aeab/resource/5d14fa34-666a-4e2e-b5b4-20c1a315fe8e/download/fl-20231121-ken-03.geojson
  format: null
  id: resource_5d14fa34
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20231121-KEN-03.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kenya: Flood - 543793.0 sq m - Nov 2023 (GeoTIFF File)'
  download_url: https://data.humdata.org/dataset/f1b3e7d8-6fb9-4f43-846e-ff04e814aeab/resource/533e3889-3b71-4132-927b-97cfd64db3ae/download/fl-20231121-ken-03.tiff
  format: null
  id: resource_533e3889
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20231121-KEN-03.tiff
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kenya: Flood - 543793.0 sq m - Nov 2023 (Geopackage File)'
  download_url: https://data.humdata.org/dataset/f1b3e7d8-6fb9-4f43-846e-ff04e814aeab/resource/92b4f835-3497-47c7-bb9a-ae92385ac89a/download/fl-20231121-ken-03.gpkg
  format: null
  id: resource_92b4f835
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20231121-KEN-03.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kenya: Flood - 543793.0 sq m - Nov 2023 (Metadata File)'
  download_url: https://data.humdata.org/dataset/f1b3e7d8-6fb9-4f43-846e-ff04e814aeab/resource/5b30ce47-2e28-45a8-90ec-56524f0d6ffd/download/metadata.txt
  format: null
  id: resource_5b30ce47
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
slug: rdls_hel-ken_wfpadam_flood5437930sqmnov2023_20231121
spatial:
  bbox: null
  centroid: null
  countries:
  - KEN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-11-21'
temporal_resolution: null
title: 'Kenya: Flood - 543793.0 sq m - Nov 2023'
version: null
vulnerability: null
---
