---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/unosat-live-web-map-floods-in-d-r-of-the-congo
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-live-web-map-floods-in-d-r-of-the-congo
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-live-web-map-floods-in-d-r-of-the-congo
dataset_id: rdls_hl-cod_unosat_livewebmapfloodsdr_20250411
description: 'UNOSAT code: FL20250408COD This application provides flood impact assessment
  in Kinshasa, Democratic Republic of the Congo The boundaries and names shown, and
  the designations used on this map do not imply official endorsement or acceptance
  by the United Nations. The designations employed and the presentation of material
  on this map do not imply the expression of any opinion whatsoever on the part of
  the Secretariat of the United Nations concerning the legal status of any country,
  territory, city or area or of its authorities, or concerning the delimitation of
  its frontiers or boundaries.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/unosat-live-web-map-floods-in-d-r-of-the-congo]'
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
  description: "UNOSAT analysts reviewed and compared satellite imagery to identify\
    \ flood-affected areas in Kinshasa. The resulting flood extent polygons with area\
    \ measurements (m\xC2\xB2 and hectares) represent direct observation of inundated\
    \ zones from remote sensing data, classified as post-event impact assessment."
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
- href: https://data.humdata.org/dataset/unosat-live-web-map-floods-in-d-r-of-the-congo
  rel: source
loss:
  losses:
  - asset_category: natural_environment
    asset_dimension: product
    description: Flood-affected area extent in Kinshasa mapped from satellite imagery
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
  description: UNOSAT Live web map - Floods in D.R. of the Congo (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4099/FL20250408COD_gdb.zip
  format: Geodatabase
  id: resource_99220bf2
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20250408COD_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: UNOSAT Live web map - Floods in D.R. of the Congo (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4099/FL20250408COD_SHP.zip
  format: null
  id: resource_7394a0d6
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20250408COD_SHP.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-cod_unosat_livewebmapfloodsdr_20250411
spatial:
  bbox: null
  centroid: null
  countries:
  - COD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-04-11'
temporal_resolution: null
title: UNOSAT Live web map - Floods in D.R. of the Congo
version: null
vulnerability: null
---
