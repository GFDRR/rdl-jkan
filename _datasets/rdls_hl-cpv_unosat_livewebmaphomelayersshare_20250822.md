---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/unosat-live-web-map-home-layers-share-un-asign-flash-flood-in-cabo-verde
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-live-web-map-home-layers-share-un-asign-flash-flood-in-cabo-verde
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-live-web-map-home-layers-share-un-asign-flash-flood-in-cabo-verde
dataset_id: rdls_hl-cpv_unosat_livewebmaphomelayersshare_20250822
description: 'UNOSAT code: FL20250812CPV This application provides flood impact assessments
  in Cabo Verde, Islands of Sao Vicente and Santo Antao Important note: The boundaries
  and names shown, and the designations used on this map do not imply official endorsement
  or acceptance by the United Nations. The designations employed and the presentation
  of material on this map do not imply the expression of any opinion whatsoever on
  the part of the Secretariat of the United Nations concerning the legal status of
  any country, territory, city or area or of its authorities, or concerning the delimitation
  of its frontiers or boundaries.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/unosat-live-web-map-home-layers-share-un-asign-flash-flood-in-cabo-verde]'
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
        process: pluvial_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts reviewed and compared satellite imagery from the flash
    flood event in Cabo Verde (August 12, 2025) to identify notable changes and map
    flood-affected areas. Geodatabase and shapefile outputs contain validated impact
    polygons with confidence levels, sensor metadata, and area measurements derived
    from multi-temporal satellite image analysis.
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
- href: https://data.humdata.org/dataset/unosat-live-web-map-home-layers-share-un-asign-flash-flood-in-cabo-verde
  rel: source
loss:
  losses:
  - asset_category: natural_environment
    asset_dimension: product
    description: Direct flood impact areas mapped from satellite imagery in Sao Vicente
      and Santo Antao islands
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
  description: UNOSAT Live web map - Home Layers Share UN-ASIGN Flash flood in Cabo
    Verde (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4176/FL20250812CPV_GDB.zip
  format: Geodatabase
  id: resource_5a4acc9a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20250812CPV_GDB.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: UNOSAT Live web map - Home Layers Share UN-ASIGN Flash flood in Cabo
    Verde (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4176/FL20250812CPV_SHP.zip
  format: null
  id: resource_26e270ca
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20250812CPV_SHP.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-cpv_unosat_livewebmaphomelayersshare_20250822
spatial:
  bbox: null
  centroid: null
  countries:
  - CPV
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-08-22'
temporal_resolution: null
title: UNOSAT Live web map - Home Layers Share UN-ASIGN Flash flood in Cabo Verde
version: null
vulnerability: null
---
