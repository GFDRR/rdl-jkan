---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/unosat-live-web-map-cyclone-ditwah-and-floods-in-sri-lanka-november-2025
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-live-web-map-cyclone-ditwah-and-floods-in-sri-lanka-november-2025
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-live-web-map-cyclone-ditwah-and-floods-in-sri-lanka-november-2025
dataset_id: rdls_hel-lka_unosat_livewebmapcycloneditwahfl_20251203
description: 'UNOSAT code: FL20251128LKA, GDACS ID: 1001238 This application provides
  geospatial information from ongoing satellite-based assessments of the floods in
  Sri Lanka triggered by Cyclone DITWAH in November 2025. Important note: Flood analysis
  derived from radar imagery may underestimate the presence of standing water in built-up
  and densely vegetated areas due to the backscattering properties of the radar signal..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/unosat-live-web-map-cyclone-ditwah-and-floods-in-sri-lanka-november-2025]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure:
- asset_type:
    description: Population exposed to flood inundation derived from satellite assessment
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
      process: pluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts compared pre- and post-event satellite imagery (radar
    and optical) to delineate flood extent and water depth across Sri Lanka following
    Cyclone Ditwah in November 2025. Population exposure was calculated by intersecting
    flood extent polygons with gridded population data. Results are provided as geodatabase,
    shapefile, and tabular population exposure summaries.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/unosat-live-web-map-cyclone-ditwah-and-floods-in-sri-lanka-november-2025
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by flooding from Cyclone Ditwah
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
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
  description: UNOSAT Live Web map- Cyclone Ditwah and Floods in Sri Lanka (November
    2025) (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4223/FL20251128LKA_gdb.zip
  format: Geodatabase
  id: resource_0924de56
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20251128LKA_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: UNOSAT Live Web map- Cyclone Ditwah and Floods in Sri Lanka (November
    2025) (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4223/FL20251128LKA_SHP.zip
  format: null
  id: resource_752717c2
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20251128LKA_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: UNOSAT Live Web map- Cyclone Ditwah and Floods in Sri Lanka (November
    2025) (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/4223/UNOSAT_PopulationExposure_FL20251128LKA_SriLanka_26_To_30_Nov2025.xlsx
  format: null
  id: resource_968c608a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_PopulationExposure_FL20251128LKA_SriLanka_26_To_30_Nov2025.xlsx
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-lka_unosat_livewebmapcycloneditwahfl_20251203
spatial:
  bbox: null
  centroid: null
  countries:
  - LKA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-12-03'
temporal_resolution: null
title: UNOSAT Live Web map- Cyclone Ditwah and Floods in Sri Lanka (November 2025)
version: null
vulnerability: null
---
