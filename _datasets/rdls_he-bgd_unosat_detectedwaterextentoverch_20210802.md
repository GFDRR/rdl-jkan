---
attributions:
- entity:
    affiliation: null
    email: null
    name: Worldpop
    url: https://data.humdata.org/dataset/satellite-detected-water-extent-over-chittagong-division-bangladesh-as-of-30-july-2021
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Sentinel-1 SAR imagery
    url: https://data.humdata.org/dataset/satellite-detected-water-extent-over-chittagong-division-bangladesh-as-of-30-july-2021
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-over-chittagong-division-bangladesh-as-of-30-july-2021
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-over-chittagong-division-bangladesh-as-of-30-july-2021
dataset_id: rdls_he-bgd_unosat_detectedwaterextentoverch_20210802
description: 'UNOSAT code: FL20210729BGD This map illustrates satellite-detected surface
  waters in Chittagong division, Bangladesh as observed from a Sentinel-1 image acquired
  on 30 July 2021 at 05:33 local time Within the analyzed area of about 18,700 km2
  and, about 852 km2 of lands appear to be flooded. The water extent appears to have
  decreased of about 18km2 since 27 July 2021. Based on Worldpop population data and
  the detected surface waters in the analyzed area, the potentially exposed population
  is mainly located in the district of Cox''s Bazar with ~425,000 people, Chittagong
  with ~392,300 people. This is a preliminary analysis and has not yet been validated
  in the field. Please send ground feedback to United Nations Satellite Centre (UNOSAT).
  Important note: Flood analysis from radar images may underestimate the presence
  of standing waters in built-up areas and densely vegetated areas due to backscattering
  properties of the radar signal.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extent-over-chittagong-division-bangladesh-as-of-30-july-2021]'
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
    description: Potentially exposed population in flood-affected areas, primarily
      in Cox's Bazar (~425,000 people) and Chittagong districts
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
  description: Sentinel-1 SAR imagery acquired 30 July 2021 was analyzed by UNOSAT
    through visual interpretation and multi-temporal comparison with 27 July 2021
    imagery to detect surface water extent. Detected flood polygons (852 km2) were
    intersected with Worldpop gridded population data to estimate potentially exposed
    population in Chittagong division.
  sources:
  - id: source_1
    license: null
    name: Worldpop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: Sentinel-1 SAR imagery
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/satellite-detected-water-extent-over-chittagong-division-bangladesh-as-of-30-july-2021
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
    as of 30 July 2021. (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/BD/FL20210729BGD/FL20210729BGD_gdb.zip
  format: Geodatabase
  id: resource_43de9c1e
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
    as of 30 July 2021. (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/BD/FL20210729BGD/FL20210729BGD_SHP.zip
  format: null
  id: resource_a4e753f6
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
slug: rdls_he-bgd_unosat_detectedwaterextentoverch_20210802
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
  start: '2021-08-02'
temporal_resolution: null
title: Satellite detected water extent over Chittagong division, Bangladesh as of
  30 July 2021.
version: null
vulnerability: null
---
