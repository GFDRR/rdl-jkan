---
attributions:
- entity:
    affiliation: null
    email: null
    name: VIIRS-NOAA satellite imagery
    url: https://data.humdata.org/dataset/water-extents-between-the-13th-and-the-17th-november-2020-in-el-salvador
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: HRSL population data
    url: https://data.humdata.org/dataset/water-extents-between-the-13th-and-the-17th-november-2020-in-el-salvador
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-between-the-13th-and-the-17th-november-2020-in-el-salvador
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-between-the-13th-and-the-17th-november-2020-in-el-salvador
dataset_id: rdls_hel-slv_unosat_detectedwaterextentsbetwe_20201118
description: 'UNOSAT code: TC20201118SLV This map illustrates satellite-detected surface
  waters (cumulative) in El Salvador as detected by VIIRS-NOAA satellite between 13th
  & 17th November 2020. Within the analyzed area of about 20,000 km2, a total of about
  440 km2 of lands appear to be flooded. Based on HRSL population data and the detected
  surface waters, about 44,000 people are potentially exposed or living close to flooded
  areas. The potentially exposed population is mainly located in the departments of
  Usulutan with ~9,000 people, La Union with ~8,500 people, and Santa Ana with ~7,500
  people. This is a preliminary analysis and has not yet been validated in the field.
  Please send ground feedback to UNITAR-UNOSAT.. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/water-extents-between-the-13th-and-the-17th-november-2020-in-el-salvador]'
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
    description: Population living close to or potentially exposed to detected flooded
      areas based on HRSL population data
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
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: "UNOSAT analysts processed VIIRS-NOAA satellite imagery acquired between\
    \ 13-17 November 2020, comparing multi-temporal images to detect surface water\
    \ changes and cumulative inundation extents across ~20,000 km\xB2 in El Salvador.\
    \ Detected water areas (~440 km\xB2) were intersected with HRSL population data\
    \ to estimate potentially exposed population by administrative department."
  sources:
  - id: source_1
    license: null
    name: VIIRS-NOAA satellite imagery
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: HRSL population data
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/water-extents-between-the-13th-and-the-17th-november-2020-in-el-salvador
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population potentially exposed to flooded areas detected by satellite
      imagery during November 2020 event
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
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
  description: Satellite detected water extents between the 13th and the 17th November
    2020 in El Salvador (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/SV/TC20201118SLV/TC20201118SLV_gdb.zip
  format: Geodatabase
  id: resource_d1e365e3
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20201118SLV_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents between the 13th and the 17th November
    2020 in El Salvador (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/SV/TC20201118SLV/TC20201118SLV_SHP.zip
  format: null
  id: resource_0307a0b4
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20201118SLV_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-slv_unosat_detectedwaterextentsbetwe_20201118
spatial:
  bbox: null
  centroid: null
  countries:
  - SLV
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2020-11-18'
temporal_resolution: null
title: Satellite detected water extents between the 13th and the 17th November 2020
  in El Salvador
version: null
vulnerability: null
---
