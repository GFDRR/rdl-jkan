---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/unosat-live-web-map
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-live-web-map
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-live-web-map
dataset_id: rdls_hl-pak_unosat_livewebmap_20250926
description: 'UNOSAT code: FL20250818PAK, GDACS ID: 1103435 This application provides
  flood impact assessments in Pakistan. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/unosat-live-web-map]'
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
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts performed multi-temporal satellite imagery comparison
    to detect notable changes in water extent and classify inundated areas. The resulting
    flood extent polygons were validated in the field and attributed with water classification,
    sensor information, confidence levels, and validation status to produce post-event
    flood impact assessments.
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
- href: https://data.humdata.org/dataset/unosat-live-web-map
  rel: source
loss:
  losses:
  - asset_category: natural_environment
    asset_dimension: product
    description: Flood-inundated water surface area and extent derived from satellite
      imagery comparison
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
          quantity_kind: area
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
  description: Pakistan - UNOSAT Live Web map (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4203/FL20250818PAK_gdb.zip
  format: Geodatabase
  id: resource_358b9d7d
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20250818PAK_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pakistan - UNOSAT Live Web map (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4203/FL20250818PAK_SHP.zip
  format: null
  id: resource_ff972b7d
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20250818PAK_SHP.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-pak_unosat_livewebmap_20250926
spatial:
  bbox: null
  centroid: null
  countries:
  - PAK
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-09-26'
temporal_resolution: null
title: Pakistan - UNOSAT Live Web map
version: null
vulnerability: null
---
