---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-1 SAR imagery
    url: https://data.humdata.org/dataset/satellite-detected-water-extent-over-chittagong-division-bangladesh-as-of-8-august-2021
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop population data
    url: https://data.humdata.org/dataset/satellite-detected-water-extent-over-chittagong-division-bangladesh-as-of-8-august-2021
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-over-chittagong-division-bangladesh-as-of-8-august-2021
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-over-chittagong-division-bangladesh-as-of-8-august-2021
dataset_id: rdls_he-bgd_unosat_detectedwaterextentoverch_20210809
description: 'UNOSAT code: FL20210729BGD This map illustrates satellite-detected surface
  waters in Chittagong division, Bangladesh as observed from a Sentinel-1 image acquired
  on 8 August 2021 at 17:55 local time. Within the analyzed area of about 18,700 km2
  and, about 873 km2 of lands appear to be flooded. The water extent appears to have
  increased of about 21 km2 since 30 July 2021. Based on Worldpop population data
  and the detected surface waters in the analyzed area, the potentially exposed population
  is mainly located in the district of Cox''s Bazar with ~393,240 people, Chittagong
  with ~358,320 people. This is a preliminary analysis and has not yet been validated
  in the field. Please send ground feedback to United Nations Satellite Centre (UNOSAT).
  Important note: Flood analysis from radar images may underestimate the presence
  of standing waters in built-up areas and densely vegetated areas due to backscattering
  properties of the radar signal.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extent-over-chittagong-division-bangladesh-as-of-8-august-2021]'
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
    description: Potentially exposed population in Cox's Bazar and Chittagong districts
      based on WorldPop data overlaid with detected water extent
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
  description: Sentinel-1 SAR imagery from 8 August 2021 was analyzed by UNOSAT analysts
    through visual interpretation and multi-temporal comparison with 30 July 2021
    imagery to detect surface water extent changes. Detected water polygons (873 km2)
    were overlaid with WorldPop population data to estimate potentially exposed population
    in affected districts, producing a post-event flood extent map with exposure assessment.
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
    name: WorldPop population data
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/satellite-detected-water-extent-over-chittagong-division-bangladesh-as-of-8-august-2021
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
  description: Satellite detected water extent over Chittagong division, Bangladesh
    as of 8 August 2021 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/BD/FL20210729BGD/FL20210729BGD_gdb.zip
  format: Geodatabase
  id: resource_f215676c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20210729BGD_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent over Chittagong division, Bangladesh
    as of 8 August 2021 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/BD/FL20210729BGD/FL20210729BGD_SHP.zip
  format: null
  id: resource_2c5ba17a
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20210729BGD_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-bgd_unosat_detectedwaterextentoverch_20210809
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
  start: '2021-08-09'
temporal_resolution: null
title: Satellite detected water extent over Chittagong division, Bangladesh as of
  8 August 2021
version: null
vulnerability: null
---
