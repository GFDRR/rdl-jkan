---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/zambia-flood-fl-20230130-zmb-00
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/zambia-flood-fl-20230130-zmb-00
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/zambia-flood-fl-20230130-zmb-00
dataset_id: rdls_hel-zmb_wfpadam_flood30149120sqmjan2023_20230130
description: 'ADAM ID: FL-20230130-ZMB-00 Flood covering 3014912.0 sq m on Jan 30
  2023 in Zambia. It impacted 386584 people.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/zambia-flood-fl-20230130-zmb-00]'
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
  description: WFP ADAM system processed satellite imagery and administrative boundary
    data to delineate the observed flood extent on 30 January 2023, intersected with
    gridded population and cropland datasets to quantify directly affected populations
    and agricultural losses, generating geospatial alert and response dashboards.
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
- href: https://data.humdata.org/dataset/zambia-flood-fl-20230130-zmb-00
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Direct population affected by flood inundation
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
  description: 'Zambia: Flood - 3014912.0 sq m - Jan 2023 (GeoJSON File)'
  download_url: https://data.humdata.org/dataset/23f9ff78-b546-43e5-a191-a9dcd3186b3e/resource/a5bf20ab-91e1-4f42-9f6e-6042be5ba3c5/download/fl-20230130-zmb-00.geojson
  format: null
  id: resource_a5bf20ab
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20230130-ZMB-00.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Zambia: Flood - 3014912.0 sq m - Jan 2023 (GeoTIFF File)'
  download_url: https://data.humdata.org/dataset/23f9ff78-b546-43e5-a191-a9dcd3186b3e/resource/3fa065f5-0271-4656-99a7-6ceddab506c2/download/fl-20230130-zmb-00.tiff
  format: null
  id: resource_3fa065f5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20230130-ZMB-00.tiff
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Zambia: Flood - 3014912.0 sq m - Jan 2023 (Geopackage File)'
  download_url: https://data.humdata.org/dataset/23f9ff78-b546-43e5-a191-a9dcd3186b3e/resource/f9e08591-234a-4818-9d9f-0ee240c4721c/download/fl-20230130-zmb-00.gpkg
  format: null
  id: resource_f9e08591
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20230130-ZMB-00.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Zambia: Flood - 3014912.0 sq m - Jan 2023 (Metadata File)'
  download_url: https://data.humdata.org/dataset/23f9ff78-b546-43e5-a191-a9dcd3186b3e/resource/c335ef20-388d-48b7-ad61-f3c5e4d9697c/download/metadata.txt
  format: null
  id: resource_c335ef20
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
slug: rdls_hel-zmb_wfpadam_flood30149120sqmjan2023_20230130
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
  start: '2023-01-30'
temporal_resolution: null
title: 'Zambia: Flood - 3014912.0 sq m - Jan 2023'
version: null
vulnerability: null
---
