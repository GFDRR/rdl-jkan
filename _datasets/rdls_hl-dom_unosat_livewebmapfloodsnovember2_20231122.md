---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/unosat-live-webmap-floods-in-dominican-republic-november-2023
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-live-webmap-floods-in-dominican-republic-november-2023
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-live-webmap-floods-in-dominican-republic-november-2023
dataset_id: rdls_hl-dom_unosat_livewebmapfloodsnovember2_20231122
description: 'UNOSAT code: FL20231120DOM, GDACS ID: 1102342 This application provides
  geospatial information about the ongoing floods in Dominican Republic Important
  note: The boundaries and names shown and the designations used on this map do not
  imply official endorsement or acceptance by the United Nations. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/unosat-live-webmap-floods-in-dominican-republic-november-2023]'
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts reviewed and compared satellite imagery from the November
    2023 flooding event to identify notable changes and map flood extent. The resulting
    geodatabase and shapefile contain observed flood polygons with metadata including
    sensor date, sensor ID, and affected area measurements in square meters and hectares.
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
- href: https://data.humdata.org/dataset/unosat-live-webmap-floods-in-dominican-republic-november-2023
  rel: source
loss:
  losses:
  - asset_category: natural_environment
    asset_dimension: product
    description: Observed flood extent and affected area from satellite imagery during
      November 2023 flooding event
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
  description: UNOSAT Live webmap- Floods in Dominican Republic, November 2023 (Zipped
    geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3749/FL20231120DOM_gdb.zip
  format: Geodatabase
  id: resource_9279d2fe
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20231120DOM_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: UNOSAT Live webmap- Floods in Dominican Republic, November 2023 (Zipped
    shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3749/FL20231120DOM_SHP.zip
  format: null
  id: resource_b7c51718
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20231120DOM_SHP.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-dom_unosat_livewebmapfloodsnovember2_20231122
spatial:
  bbox: null
  centroid: null
  countries:
  - DOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-11-22'
temporal_resolution: null
title: UNOSAT Live webmap- Floods in Dominican Republic, November 2023
version: null
vulnerability: null
---
