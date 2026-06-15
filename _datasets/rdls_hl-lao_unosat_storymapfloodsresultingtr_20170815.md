---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/story-map-floods-in-laos-resulting-from-tropical-cyclone-sonca-17
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/story-map-floods-in-laos-resulting-from-tropical-cyclone-sonca-17
dataset_id: rdls_hl-lao_unosat_storymapfloodsresultingtr_20170815
description: 'This UNOSAT LIVE map integrates geo-spatial data in support of response
  efforts following Tropical Cyclone SONCA-17, after it made landfall in Laos on 26
  July 2017. More specifically, it was created with the aim of supporting a food security
  field assessment carried out by World Food Programme on the ground. Up-to-date,
  comprehensive satellite image derived flood analyses are displayed, together with
  photos automatically uploaded from the UN-ASIGN smartphone app. Additional supporting
  GIS data are also included on the map.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/story-map-floods-in-laos-resulting-from-tropical-cyclone-sonca-17]'
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
  description: UNOSAT analysts compared multi-temporal satellite imagery to identify
    flood extent changes resulting from Tropical Cyclone Sonca-17 landfall in Laos
    on 26 July 2017. Flood polygons with area measurements were digitized and compiled
    into geodatabase and shapefile formats to support WFP food security field assessments.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/story-map-floods-in-laos-resulting-from-tropical-cyclone-sonca-17
  rel: source
loss:
  losses:
  - asset_category: natural_environment
    asset_dimension: product
    description: Post-event flood extent and inundated area derived from satellite
      imagery following Tropical Cyclone Sonca-17
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
  description: 'Story Map: Floods in Laos resulting from Tropical Cyclone Sonca 17
    (Zipped geodatabase)'
  download_url: https://cern.ch/unosat-maps/LA/TC20170731LAO/TC20170731LAO.gdb.zip
  format: Geodatabase
  id: resource_0519ce5c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20170731LAO.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Story Map: Floods in Laos resulting from Tropical Cyclone Sonca 17
    (Zipped shapefile)'
  download_url: https://cern.ch/unosat-maps/LA/TC20170731LAO/TC20170731LAO_shp.zip
  format: null
  id: resource_66a51604
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20170731LAO_shp.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-lao_unosat_storymapfloodsresultingtr_20170815
spatial:
  bbox: null
  centroid: null
  countries:
  - LAO
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-08-15'
temporal_resolution: null
title: 'Story Map: Floods in Laos resulting from Tropical Cyclone Sonca 17'
version: null
vulnerability: null
---
