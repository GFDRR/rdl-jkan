---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-1 SAR imagery
    url: https://data.humdata.org/dataset/waters-in-ilocos-central-luzon-and-national-capital-regions-of-philippines-as-of-17-novemb
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/waters-in-ilocos-central-luzon-and-national-capital-regions-of-philippines-as-of-17-novemb
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/waters-in-ilocos-central-luzon-and-national-capital-regions-of-philippines-as-of-17-novemb
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/waters-in-ilocos-central-luzon-and-national-capital-regions-of-philippines-as-of-17-novemb
dataset_id: rdls_he-phl_unosat_detectedwatersilocoscentr_20201118
description: 'UNOSAT code: TC20201111PHL This map illustrates satellite-detected surface
  waters in Ilocos, Central Luzon and National Capital regions of Philippines as observed
  from a Sentinel-1 image acquired on 17 November 2020 at 05:46 local time. Within
  the analyzed area of about 16,500 km2, a total of about 300 km2 of lands appear
  to be flooded. The water extent appears to have receded of about 900 km2 since 13
  November 2020. Based on Worldpop population data and the detected surface waters,
  about 200,000 people are potentially exposed or living close to flooded areas. This
  is a preliminary analysis and has not yet been validated in the field. Please send
  ground feedback to UNITAR-UNOSAT. Important Note: Flood analysis from radar images
  may underestimate the presence of standing waters in built-up areas and densely
  vegetated areas due to backscattering properties of the radar signal.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/waters-in-ilocos-central-luzon-and-national-capital-regions-of-philippines-as-of-17-novemb]'
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
    description: Population potentially exposed or living close to flooded areas based
      on WorldPop data
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
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts processed Sentinel-1 SAR imagery acquired on 17 November
    2020 to detect surface water extent through change detection analysis, comparing
    with imagery from 13 November 2020 to quantify water recession. Detected flood
    extent was overlaid with WorldPop population data to estimate exposed population
    in the three affected regions.
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
- href: https://data.humdata.org/dataset/waters-in-ilocos-central-luzon-and-national-capital-regions-of-philippines-as-of-17-novemb
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
  description: Satellite detected waters in Ilocos, Central Luzon and National Capital
    regions of Philippines as of 17 November 2020 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/PH/TC20201111PHL/TC20201111PHL_gdb.zip
  format: Geodatabase
  id: resource_2731ec81
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20201111PHL_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected waters in Ilocos, Central Luzon and National Capital
    regions of Philippines as of 17 November 2020 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/PH/TC20201111PHL/TC20201111PHL_SHP.zip
  format: null
  id: resource_20df4f39
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20201111PHL_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-phl_unosat_detectedwatersilocoscentr_20201118
spatial:
  bbox: null
  centroid: null
  countries:
  - PHL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2020-11-18'
temporal_resolution: null
title: Satellite detected waters in Ilocos, Central Luzon and National Capital regions
  of Philippines as of 17 November 2020
version: null
vulnerability: null
---
