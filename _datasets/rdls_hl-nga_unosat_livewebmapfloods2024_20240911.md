---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/unosat-live-web-map-floods-in-nigeria-2024
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-live-web-map-floods-in-nigeria-2024
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-live-web-map-floods-in-nigeria-2024
dataset_id: rdls_hl-nga_unosat_livewebmapfloods2024_20240911
description: 'UNOSAT code: FL20240902NGA, GDACS ID: 1102720 This application provides
  flood impact assessments for Nigeria in September 2024.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/unosat-live-web-map-floods-in-nigeria-2024]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure: []
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
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts performed multi-temporal satellite imagery comparison
    to detect notable changes in inundation patterns during the September 2024 flood
    event in Nigeria. Flood extent polygons were delineated through visual interpretation
    and change detection analysis, with area measurements calculated in square meters
    and hectares. The resulting geodatabase and shapefile products represent observed
    flood impact footprints suitable for emergency response and damage assessment.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/unosat-live-web-map-floods-in-nigeria-2024
  rel: source
loss:
  losses:
  - asset_category: natural_environment
    asset_dimension: product
    description: Flood-inundated area extent derived from satellite imagery comparison
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
  description: UNOSAT Live Web map - Floods in Nigeria, 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3961/FL20240902NGA_gdb.zip
  format: Geodatabase
  id: resource_512dcce8
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240902NGA_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: UNOSAT Live Web map - Floods in Nigeria, 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3961/FL20240902NGA_SHP.zip
  format: null
  id: resource_98161fc5
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240902NGA_SHP.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-nga_unosat_livewebmapfloods2024_20240911
spatial:
  bbox: null
  centroid: null
  countries:
  - NGA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-09-11'
temporal_resolution: null
title: UNOSAT Live Web map - Floods in Nigeria, 2024
version: null
vulnerability: null
---
