---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/unosat-live-web-map-lewotobi-volcanic-eruption-indonesia
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-live-web-map-lewotobi-volcanic-eruption-indonesia
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-live-web-map-lewotobi-volcanic-eruption-indonesia
dataset_id: rdls_he-idn_unosat_livewebmaplewotobivolcani_20241106
description: 'UNOSAT code: VO20241105IDN, GDACS ID: 1000099 This application provides
  analaysis related to the Lewotobi volcanic eruption in November 2024.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/unosat-live-web-map-lewotobi-volcanic-eruption-indonesia]'
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
    description: Spatial extent of volcanic eruption impact zones mapped from satellite
      imagery
    id: natural_environment
    scheme: null
    title: null
    uri: null
  category: natural_environment
  id: exposure_1
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: h_vaf:mm
      process: ashfall
      trigger: null
      type: volcanic
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: volcanic
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts reviewed and compared multi-temporal satellite imagery
    of the Lewotobi volcanic eruption in Indonesia (November 2024) to identify and
    map notable changes in affected areas. Spatial features were extracted and compiled
    into geodatabase and shapefile formats with site-level attributes including area
    measurements.
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
- href: https://data.humdata.org/dataset/unosat-live-web-map-lewotobi-volcanic-eruption-indonesia
  rel: source
loss: null
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
  description: UNOSAT Live Web map - Lewotobi volcanic eruption, Indonesia (Zipped
    geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4018/VO20241105IDN_gdb.zip
  format: Geodatabase
  id: resource_10dd8c81
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VO20241105IDN_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: UNOSAT Live Web map - Lewotobi volcanic eruption, Indonesia (Zipped
    shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4018/VO20241105IDN_SHP.zip
  format: null
  id: resource_dcd771d7
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VO20241105IDN_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-idn_unosat_livewebmaplewotobivolcani_20241106
spatial:
  bbox: null
  centroid: null
  countries:
  - IDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-11-06'
temporal_resolution: null
title: UNOSAT Live Web map - Lewotobi volcanic eruption, Indonesia
version: null
vulnerability: null
---
