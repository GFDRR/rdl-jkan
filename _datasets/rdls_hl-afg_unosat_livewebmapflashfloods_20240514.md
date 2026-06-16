---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/unosat-live-web-map-flash-floods-in-afghanistan
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-live-web-map-flash-floods-in-afghanistan
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-live-web-map-flash-floods-in-afghanistan
dataset_id: rdls_hl-afg_unosat_livewebmapflashfloods_20240514
description: 'UNOSAT code: FL20240512AFG, GDACS ID: 1102616 This application provides
  geospatial information on the ongoing floods in Afghanistan. Important note: The
  boundaries and names shown, and the designations used on this map do not imply official
  endorsement or acceptance by the United Nations. The United Nations Satellite Centre.
  UNOSAT is not responsible for the misuse or misrepresentation of the map.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/unosat-live-web-map-flash-floods-in-afghanistan]'
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
  description: UNOSAT analysts reviewed and compared multi-temporal satellite imagery
    to detect notable changes in water extent and classify flooded areas during the
    May 2024 flash flood event in Afghanistan. Satellite-derived water bodies and
    inundated zones were delineated with confidence levels and field validation flags,
    producing vector geometries with area measurements in hectares and square meters.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/unosat-live-web-map-flash-floods-in-afghanistan
  rel: source
loss:
  losses:
  - asset_category: natural_environment
    asset_dimension: product
    description: Spatial extent of water bodies and flooded areas from satellite-detected
      changes
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
  description: UNOSAT Live Web map - Flash floods in Afghanistan (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3841/FL20240512AFG_gdb.zip
  format: Geodatabase
  id: resource_56ff12b9
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240512AFG_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: UNOSAT Live Web map - Flash floods in Afghanistan (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3841/FL20240512AFG_SHP.zip
  format: null
  id: resource_073b02ca
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240512AFG_SHP.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-afg_unosat_livewebmapflashfloods_20240514
spatial:
  bbox: null
  centroid: null
  countries:
  - AFG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-05-14'
temporal_resolution: null
title: UNOSAT Live Web map - Flash floods in Afghanistan
version: null
vulnerability: null
---
