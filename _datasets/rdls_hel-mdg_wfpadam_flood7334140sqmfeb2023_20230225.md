---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/madagascar-flood-fl-20230225-mdg-00
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/madagascar-flood-fl-20230225-mdg-00
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/madagascar-flood-fl-20230225-mdg-00
dataset_id: rdls_hel-mdg_wfpadam_flood7334140sqmfeb2023_20230225
description: 'ADAM ID: FL-20230225-MDG-00 Flood covering 733414.0 sq m on Feb 25 2023
  in Madagascar. It impacted 1214587 people.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/madagascar-flood-fl-20230225-mdg-00]'
details: null
exposure:
- asset_type:
    description: Cropland area exposed to flooding, including total croplands and
      flooded croplands
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
    description: Total population and directly affected population in flooded areas
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
  description: WFP ADAM collected and analyzed geospatial flood extent data and socio-economic
    impact information following the February 25, 2023 flood event in Madagascar.
    The dataset integrates observed flood boundaries with exposure data (population
    and cropland) to produce direct impact assessments including affected population
    counts and flooded agricultural area.
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
- href: https://data.humdata.org/dataset/madagascar-flood-fl-20230225-mdg-00
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Direct population impact from February 2023 flood event in Madagascar
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
    description: Direct agricultural loss from flooded cropland area
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
  description: 'Madagascar: Flood - 733414.0 sq m - Feb 2023 (GeoJSON File)'
  download_url: https://data.humdata.org/dataset/c7fc2916-1f61-4695-ba3b-2fedca613138/resource/80b31246-b1d6-43c6-b4db-04a0e374c699/download/fl-20230225-mdg-00.geojson
  format: null
  id: resource_80b31246
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20230225-MDG-00.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Madagascar: Flood - 733414.0 sq m - Feb 2023 (GeoTIFF File)'
  download_url: https://data.humdata.org/dataset/c7fc2916-1f61-4695-ba3b-2fedca613138/resource/b83875e4-ede0-49e4-a98f-fd10a2759157/download/fl-20230225-mdg-00.tiff
  format: null
  id: resource_b83875e4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20230225-MDG-00.tiff
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Madagascar: Flood - 733414.0 sq m - Feb 2023 (Geopackage File)'
  download_url: https://data.humdata.org/dataset/c7fc2916-1f61-4695-ba3b-2fedca613138/resource/cacc0995-8082-48f7-991e-d674fe234a9e/download/fl-20230225-mdg-00.gpkg
  format: null
  id: resource_cacc0995
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20230225-MDG-00.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Madagascar: Flood - 733414.0 sq m - Feb 2023 (Metadata File)'
  download_url: https://data.humdata.org/dataset/c7fc2916-1f61-4695-ba3b-2fedca613138/resource/9401e9e3-182a-4ded-994c-9be1690d9e16/download/metadata.txt
  format: null
  id: resource_9401e9e3
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
slug: rdls_hel-mdg_wfpadam_flood7334140sqmfeb2023_20230225
spatial:
  bbox: null
  centroid: null
  countries:
  - MDG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-02-25'
temporal_resolution: null
title: 'Madagascar: Flood - 733414.0 sq m - Feb 2023'
version: null
vulnerability: null
---
