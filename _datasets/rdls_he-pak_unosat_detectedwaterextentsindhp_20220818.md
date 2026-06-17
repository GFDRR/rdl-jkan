---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-1 SAR imagery
    url: https://data.humdata.org/dataset/satellite-detected-water-extent-in-sindh-province-pakistan-as-of-15-august-2022
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/satellite-detected-water-extent-in-sindh-province-pakistan-as-of-15-august-2022
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-in-sindh-province-pakistan-as-of-15-august-2022
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-in-sindh-province-pakistan-as-of-15-august-2022
dataset_id: rdls_he-pak_unosat_detectedwaterextentsindhp_20220818
description: 'UNOSAT code: FL20220808PAK This map illustrates satellite-detected surface
  waters in Sindh province, Pakistan as observed from a Sentinel-1 image acquired
  on 15 August 2022 at 18:36 local time. Within the analyzed area of about 30,000
  km2, about 1,550 km2 of lands appear to be flooded. Water extent appears to have
  decreased of about 325 km2 since the 06 August 2022. within the analyzed area. Based
  on Worldpop population data and the detected surface waters in the analyzed area,
  about 410,000 are potentially exposed or living close to flooded areas. This is
  a preliminary analysis and has not yet been validated in the field. Please send
  ground feedback to United Nations Satellite Centre (UNOSAT). Important note: Flood
  analysis from radar images may underestimate the presence of standing waters in
  built-up areas and densely vegetated areas due to backscattering properties of the
  radar signal.. [Source: This metadata record was automatically extracted from the
  Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extent-in-sindh-province-pakistan-as-of-15-august-2022]'
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
    description: Population potentially exposed or living close to detected flooded
      areas, estimated at approximately 410,000 people based on WorldPop data
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
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: Sentinel-1 SAR satellite imagery from 15 August 2022 was analyzed by
    UNOSAT analysts through visual interpretation and comparison with prior imagery
    (6 August 2022) to detect surface water extent changes. Detected water polygons
    were intersected with WorldPop population data to estimate exposed population,
    producing a post-event flood extent map with exposure assessment for Sindh province.
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
- href: https://data.humdata.org/dataset/satellite-detected-water-extent-in-sindh-province-pakistan-as-of-15-august-2022
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
  description: Satellite detected water extent in Sindh province, Pakistan, as of
    15 August 2022 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/PK/FL20220808PAK/FL20220808PAK_gdb.zip
  format: Geodatabase
  id: resource_46d6fc15
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20220808PAK_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent in Sindh province, Pakistan, as of
    15 August 2022 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/PK/FL20220808PAK/FL20220808PAK_SHP.zip
  format: null
  id: resource_9e4a59d0
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20220808PAK_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-pak_unosat_detectedwaterextentsindhp_20220818
spatial:
  bbox: null
  centroid: null
  countries:
  - PAK
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-08-18'
temporal_resolution: null
title: Satellite detected water extent in Sindh province, Pakistan, as of 15 August
  2022
version: null
vulnerability: null
---
