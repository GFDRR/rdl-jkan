---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-satellite-detected-waters-evolution-in-central-bangladesh-prelimin-july-29-2016
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-satellite-detected-waters-evolution-in-central-bangladesh-prelimin-july-29-2016
dataset_id: rdls_hzd-bgd_unosat_geodatadetectedwatersevol_20160729
description: 'Preliminary Satellite Detected Waters Evolution in Central Bangladesh
  Report (28 July 2016). [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-satellite-detected-waters-evolution-in-central-bangladesh-prelimin-july-29-2016]'
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
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-4.0
lineage:
  description: UNOSAT analysts compared multi-temporal satellite imagery acquired
    on 25 July 2016 to detect changes in water extent and map flood inundation areas
    in Central Bangladesh. Water bodies were delineated through visual interpretation
    and automated change detection, with results delivered as vector polygons with
    area measurements in hectares and square meters.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/geodata-of-satellite-detected-waters-evolution-in-central-bangladesh-prelimin-july-29-2016
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
  description: Geodata of Satellite Detected Waters Evolution in Central Bangladesh
    - Preliminary Report (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/BD/FL20160725BGD/FL20160725BGD_shp.zip
  format: null
  id: resource_9d999ebf
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20160725BGD_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Satellite Detected Waters Evolution in Central Bangladesh
    - Preliminary Report (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/BD/FL20160725BGD/FL20160725BGD.gdb.zip
  format: null
  id: resource_3f23388e
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20160725BGD.gdb.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-bgd_unosat_geodatadetectedwatersevol_20160729
spatial:
  bbox: null
  centroid: null
  countries:
  - BGD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-07-29'
temporal_resolution: null
title: Geodata of Satellite Detected Waters Evolution in Central Bangladesh - Preliminary
  Report
version: null
vulnerability: null
---
