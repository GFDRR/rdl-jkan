---
attributions:
- entity:
    affiliation: null
    email: null
    name: NOAA20-VIIRS
    url: https://data.humdata.org/dataset/population-potentially-exposed-to-floods-between-12-21-july-2020-in-bangladesh
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/population-potentially-exposed-to-floods-between-12-21-july-2020-in-bangladesh
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/population-potentially-exposed-to-floods-between-12-21-july-2020-in-bangladesh
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/population-potentially-exposed-to-floods-between-12-21-july-2020-in-bangladesh
dataset_id: rdls_he-bgd_unosat_populationpotentiallyexpo_20200724
description: 'UNOSAT code: FL20200713BGD This map illustrates potentially exposed
  population to floods (cumulative) aggregated by district using NOAA20-VIIRS in Bangladesh
  between the 12th and the 21st of July 2020 and Worldpop spatial demographic data.
  About 34 million people were exposed or living close to flooded areas. The most
  exposed districts mainly located in Sylhet, Mymensingh and Rajshahi divisions..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/population-potentially-exposed-to-floods-between-12-21-july-2020-in-bangladesh]'
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
    description: Population potentially exposed to floods aggregated by district using
      WorldPop spatial demographic data
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
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts compared multi-temporal NOAA20-VIIRS satellite imagery
    from July 12-21, 2020 to detect flood extent changes during the monsoon event.
    Observed flood areas were intersected with WorldPop gridded population data and
    aggregated by administrative district to quantify population exposure to flooded
    areas.
  sources:
  - id: source_1
    license: null
    name: NOAA20-VIIRS
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
- href: https://data.humdata.org/dataset/population-potentially-exposed-to-floods-between-12-21-july-2020-in-bangladesh
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
  description: Population potentially exposed to floods between 12&21 July 2020 in
    Bangladesh (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/BD/FL20200713BGD/FL20200713BGD_gdb.zip
  format: Geodatabase
  id: resource_5c37dd01
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20200713BGD_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Population potentially exposed to floods between 12&21 July 2020 in
    Bangladesh (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/BD/FL20200713BGD/FL20200713BGD_SHP.zip
  format: null
  id: resource_03bb9ae2
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20200713BGD_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-bgd_unosat_populationpotentiallyexpo_20200724
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
  start: '2020-07-24'
temporal_resolution: null
title: Population potentially exposed to floods between 12&21 July 2020 in Bangladesh
version: null
vulnerability: null
---
