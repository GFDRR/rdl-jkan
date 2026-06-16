---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-1 SAR imagery
    url: https://data.humdata.org/dataset/water-extent-over-the-boga-yangon-regions-and-mon-state-surrounding-the-gulf-of-martaban-m
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/water-extent-over-the-boga-yangon-regions-and-mon-state-surrounding-the-gulf-of-martaban-m
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-over-the-boga-yangon-regions-and-mon-state-surrounding-the-gulf-of-martaban-m
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-over-the-boga-yangon-regions-and-mon-state-surrounding-the-gulf-of-martaban-m
dataset_id: rdls_he-mmr_unosat_detectedwaterextentoverbo_20210904
description: 'UNOSAT code: FL20210831MMR This map illustrates satellite-detected surface
  waters over the Boga, Yangon regions and Mon state, surrounding the Gulf of Martaban,
  Myanmar as observed from a Sentinel-1 image acquired on 1 September 2021 at 05:55
  local time. Within the analyzed area of about 10,000 km2 , 240 km2 of lands appear
  to be flooded. The water extent appears to have decreased of about 470 km2 since
  25 August 2021. Based on Worldpop population data and the detected surface waters
  in the analyzed area, the potentially exposed population is mainly located in the
  township of Thanatpin with ~ 7,300 people. Thaton with ~ 7,000 people. and Paung
  with ~ 5,700 people. This is a preliminary analysis and has not yet been validated
  in the field. Please send ground feedback to United Nations Satellite Centre (UNOSAT).
  Important note: Flood analysis from radar images may underestimate the presence
  of standing waters in built-up areas and densely vegetated areas due to backscattering
  properties of the radar signal.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-over-the-boga-yangon-regions-and-mon-state-surrounding-the-gulf-of-martaban-m]'
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
    description: Potentially exposed population in flooded areas derived from WorldPop
      population data
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
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "Sentinel-1 SAR imagery from 1 September 2021 was analyzed by UNOSAT\
    \ analysts through visual interpretation and multi-temporal change detection (comparing\
    \ to 25 August 2021 image) to delineate surface water extent. Detected water polygons\
    \ were intersected with WorldPop population grids to estimate potentially exposed\
    \ population in the 10,000 km\xC2\xB2 study area covering Boga, Yangon regions\
    \ and Mon state."
  sources:
  - id: source_1
    license: null
    name: Sentinel-1 SAR imagery
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/water-extent-over-the-boga-yangon-regions-and-mon-state-surrounding-the-gulf-of-martaban-m
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
  description: Satellite detected water extent over the Boga, Yangon regions and Mon
    state, surrounding the Gulf of Martaban, Myanmar (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/MM/FL20210831MMR/FL20210831MMR_gdb.zip
  format: Geodatabase
  id: resource_8dfee504
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20210831MMR_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent over the Boga, Yangon regions and Mon
    state, surrounding the Gulf of Martaban, Myanmar (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/MM/FL20210831MMR/FL20210831MMR_shp.zip
  format: null
  id: resource_69f82efa
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20210831MMR_shp.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-mmr_unosat_detectedwaterextentoverbo_20210904
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
  start: '2021-09-04'
temporal_resolution: null
title: Satellite detected water extent over the Boga, Yangon regions and Mon state,
  surrounding the Gulf of Martaban, Myanmar
version: null
vulnerability: null
---
