---
attributions:
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-13-17-november-2020-in-honduras
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: NOAA20-VIIRS
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-13-17-november-2020-in-honduras
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-13-17-november-2020-in-honduras
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-13-17-november-2020-in-honduras
dataset_id: rdls_he-hnd_unosat_detectedwaterextentsbetwe_20201118
description: 'UNOSAT code: TC20201116HND This map illustrates satellite-detected surface
  waters (cumulative) aggregated using NOAA20-VIIRS in Honduras between 13 and 17
  November 2020. Based on Worldpop spatial demographic data, about 140,000 people
  are exposed or living close to flooded areas. The potentially exposed population
  is mainly located in the department of Cortes with ~80,000 people, Choluteca with
  ~23,000 people, and Valle with ~14,000 people. This is a preliminary analysis and
  has not yet been validated in the field. Please send ground feedback to UNITAR-UNOSAT.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extents-between-13-17-november-2020-in-honduras]'
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
    description: Population exposed or living close to satellite-detected flooded
      areas, aggregated by department
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
      process: pluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts processed NOAA20-VIIRS satellite imagery from 13-17
    November 2020 to detect cumulative surface water extents in Honduras. Detected
    water polygons were overlaid with WorldPop spatial demographic data to estimate
    potentially exposed population by administrative department. This is a preliminary
    post-event assessment based on satellite observation without field validation.
  sources:
  - id: source_1
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: NOAA20-VIIRS
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/satellite-detected-water-extents-between-13-17-november-2020-in-honduras
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
  description: Satellite detected water extents between 13 & 17 November 2020 in Honduras
    (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/HN/TC20201116HND/TC20201116HND_gdb.zip
  format: Geodatabase
  id: resource_66f6867a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20201116HND_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents between 13 & 17 November 2020 in Honduras
    (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/HN/TC20201116HND/TC20201116HND_SHP.zip
  format: null
  id: resource_f53ab353
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20201116HND_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-hnd_unosat_detectedwaterextentsbetwe_20201118
spatial:
  bbox: null
  centroid: null
  countries:
  - HND
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2020-11-18'
temporal_resolution: null
title: Satellite detected water extents between 13 & 17 November 2020 in Honduras
version: null
vulnerability: null
---
