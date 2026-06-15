---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-1 satellite imagery
    url: https://data.humdata.org/dataset/water-extent-over-nawalparasi-west-rupandehi-and-kapilbastu-districts-nepal-as-of-7-july-2
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop population data
    url: https://data.humdata.org/dataset/water-extent-over-nawalparasi-west-rupandehi-and-kapilbastu-districts-nepal-as-of-7-july-2
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-over-nawalparasi-west-rupandehi-and-kapilbastu-districts-nepal-as-of-7-july-2
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-over-nawalparasi-west-rupandehi-and-kapilbastu-districts-nepal-as-of-7-july-2
dataset_id: rdls_he-npl_unosat_detectedwaterextentoverna_20210708
description: 'UNOSAT code: FL20210630NPL This map illustrates satellite-detected surface
  waters in Nawalparasi West, Rupandehi and Kapilbastu districts, Lumbini province,
  Nepal as observed from a Sentinel-1 image acquired on 7 July 2021 at 06:12 local
  time and using an automated analysis with Machine learning method. Within the analyzed
  area of about 1,500 km2 and, about 67km2 of lands appear to be flooded. The water
  extent appears to have decreased of about 110 km2 since 2 July 2021 and moved toward
  India. Based on Worldpop population data and the detected surface waters in the
  analyzed area, the potentially exposed population is mainly located in the district
  of Rupandehi with ~59,000 people and Nawalparasi West with ~5,200 people. This is
  a preliminary analysis and has not yet been validated in the field. Please send
  ground feedback to United Nations Satellite Centre (UNOSAT). Important note: Flood
  analysis from radar images may underestimate the presence of standing waters in
  built-up areas and densely vegetated areas due to backscattering properties of the
  radar signal.. [Source: This metadata record was automatically extracted from the
  Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-over-nawalparasi-west-rupandehi-and-kapilbastu-districts-nepal-as-of-7-july-2]'
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
    description: Population exposed to detected flood waters based on WorldPop population
      data
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
  description: "Sentinel-1 SAR imagery from 7 July 2021 was processed using automated\
    \ machine learning methods to detect surface water extent across 1,500 km\xB2\
    \ in three districts of Lumbini province. Detected water polygons (67 km\xB2 total)\
    \ were compared to a prior acquisition from 2 July 2021 to assess flood extent\
    \ changes. Population exposure was estimated by intersecting detected water extent\
    \ with WorldPop gridded population data."
  sources:
  - id: source_1
    license: null
    name: Sentinel-1 satellite imagery
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
- href: https://data.humdata.org/dataset/water-extent-over-nawalparasi-west-rupandehi-and-kapilbastu-districts-nepal-as-of-7-july-2
  rel: source
loss:
  losses: []
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
  description: Satellite detected water extent over Nawalparasi West, Rupandehi and
    Kapilbastu districts, Nepal as of 7 July 2021 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/NP/FL20210630NPL/FL20210630NPL_gdb.zip
  format: Geodatabase
  id: resource_a5b16caa
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20210630NPL_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent over Nawalparasi West, Rupandehi and
    Kapilbastu districts, Nepal as of 7 July 2021 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/NP/FL20210630NPL/FL20210630NPL_SHP.zip
  format: null
  id: resource_b40bc670
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20210630NPL_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-npl_unosat_detectedwaterextentoverna_20210708
spatial:
  bbox: null
  centroid: null
  countries:
  - NPL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2021-07-08'
temporal_resolution: null
title: Satellite detected water extent over Nawalparasi West, Rupandehi and Kapilbastu
  districts, Nepal as of 7 July 2021
version: null
vulnerability: null
---
