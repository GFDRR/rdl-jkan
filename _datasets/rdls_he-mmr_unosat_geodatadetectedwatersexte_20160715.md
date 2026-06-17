---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-satellite-detected-waters-extent-over-northwestern-rakhine-state-m-july-15-2016
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-satellite-detected-waters-extent-over-northwestern-rakhine-state-m-july-15-2016
dataset_id: rdls_he-mmr_unosat_geodatadetectedwatersexte_20160715
description: 'This map illustrates satellite-detected flood waters in the northwestern
  part of Rakhine State in the townships of Kyauktaw, Mrauk-U and Ponnagyun, Myanmar
  as imaged by the SENTINEL-1 satellite on 14 July 2016. Heavy rains at the onset
  of the monsoon season have caused flooding. The most affected lands seem to be mainly
  agricultural and/or paddy fields, many of which are of course frequently inundated
  at other times as well. This is a preliminary analysis and has not yet been validated
  in the field. Please send ground feedback to UNITAR-UNOSAT.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/geodata-of-satellite-detected-waters-extent-over-northwestern-rakhine-state-m-july-15-2016]'
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
    description: Agricultural and paddy fields affected by satellite-detected flood
      waters
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_1
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
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
      process: pluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: flood
license: CC-BY-4.0
lineage:
  description: UNOSAT analysts processed SENTINEL-1 satellite imagery acquired on
    14 July 2016 by comparing pre- and post-monsoon onset images to detect notable
    changes in water extent. Flood water polygons were delineated through visual interpretation
    and digitized into vector shapefiles with area calculations in square meters and
    hectares. This preliminary analysis represents observed flood extent without field
    validation.
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
- href: https://data.humdata.org/dataset/geodata-of-satellite-detected-waters-extent-over-northwestern-rakhine-state-m-july-15-2016
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
  description: Geodata of Satellite Detected Waters Extent Over Northwestern Rakhine
    State, Myanmar (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MM/FL20160714MMR/FL20160714MMR_shp.zip
  format: null
  id: resource_bebc717e
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20160714MMR_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Satellite Detected Waters Extent Over Northwestern Rakhine
    State, Myanmar (Geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MM/FL20160714MMR/FL20160714MMR.gdb.zip
  format: Geodatabase
  id: resource_db58d1f2
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20160714MMR.gdb.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-mmr_unosat_geodatadetectedwatersexte_20160715
spatial:
  bbox: null
  centroid: null
  countries:
  - MMR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-07-15'
temporal_resolution: null
title: Geodata of Satellite Detected Waters Extent Over Northwestern Rakhine State,
  Myanmar
version: null
vulnerability: null
---
