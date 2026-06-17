---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/zambia-flood-fl-20230210-zmb-00
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/zambia-flood-fl-20230210-zmb-00
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/zambia-flood-fl-20230210-zmb-00
dataset_id: rdls_hel-zmb_wfpadam_flood30569210sqmfeb2023_20230210
description: 'ADAM ID: FL-20230210-ZMB-00 Flood covering 3056921.0 sq m on Feb 10
  2023 in Zambia. It impacted 409508 people.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/zambia-flood-fl-20230210-zmb-00]'
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
    description: Cropland area exposed to flooding
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
    February 10, 2023 flood event in Zambia. Flood extent was mapped and overlaid
    with population and cropland datasets to quantify directly affected populations
    and flooded agricultural areas. The resulting geodataset integrates observed hazard
    extent with exposure and impact metrics for operational response.
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
- href: https://data.humdata.org/dataset/zambia-flood-fl-20230210-zmb-00
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Directly affected population from February 2023 flood event
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
    description: Flooded cropland area from February 2023 flood event
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
  description: 'Zambia: Flood - 3056921.0 sq m - Feb 2023 (GeoJSON File)'
  download_url: https://data.humdata.org/dataset/b02c9456-e116-446e-96de-45c8e85fc41a/resource/03b5ef43-66d7-40fa-a74d-3129d57d235b/download/fl-20230210-zmb-00.geojson
  format: null
  id: resource_03b5ef43
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20230210-ZMB-00.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Zambia: Flood - 3056921.0 sq m - Feb 2023 (GeoTIFF File)'
  download_url: https://data.humdata.org/dataset/b02c9456-e116-446e-96de-45c8e85fc41a/resource/4e7bd3de-e51c-46b8-8510-9cc32f069317/download/fl-20230210-zmb-00.tiff
  format: null
  id: resource_4e7bd3de
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20230210-ZMB-00.tiff
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Zambia: Flood - 3056921.0 sq m - Feb 2023 (Geopackage File)'
  download_url: https://data.humdata.org/dataset/b02c9456-e116-446e-96de-45c8e85fc41a/resource/1a0f7cb5-e645-492a-a4b0-8273fbd56bbb/download/fl-20230210-zmb-00.gpkg
  format: null
  id: resource_1a0f7cb5
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20230210-ZMB-00.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Zambia: Flood - 3056921.0 sq m - Feb 2023 (Metadata File)'
  download_url: https://data.humdata.org/dataset/b02c9456-e116-446e-96de-45c8e85fc41a/resource/c29dee5b-d0a9-4799-9018-a5fd91684c93/download/metadata.txt
  format: null
  id: resource_c29dee5b
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
slug: rdls_hel-zmb_wfpadam_flood30569210sqmfeb2023_20230210
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
  start: '2023-02-10'
temporal_resolution: null
title: 'Zambia: Flood - 3056921.0 sq m - Feb 2023'
version: null
vulnerability: null
---
