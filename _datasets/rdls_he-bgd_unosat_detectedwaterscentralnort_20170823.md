---
attributions:
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/satellite-detected-waters-in-central-northern-bangladesh
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Sentinel-1 SAR
    url: https://data.humdata.org/dataset/satellite-detected-waters-in-central-northern-bangladesh
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-waters-in-central-northern-bangladesh
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-waters-in-central-northern-bangladesh
dataset_id: rdls_he-bgd_unosat_detectedwaterscentralnort_20170823
description: 'This map illustrates satellite-detected surface water extent in the
  central and northern parts of Bangladesh using a Sentinel-1 satellite image acquired
  on the 22 August 2017. The total analysed area is about 4,284,431 ha. In this analysed
  area; 1,099,369 ha (39%) of lands are likely affected. These lands are mainly cropland
  irrigated and rainfed areas and estimated to 1,039,350 ha. The population exposure
  analysis using WorldPop data shows that ~10,000,000 people are potentially affected
  by floods in the analysed zone: ~5,400,000 are located in Dhaka Division and ~2,750,000
  in Rajshahi Division. Please note that for visualization purposes the analyzed area
  is wider than the extent of this map.This is a preliminary analysis and has not
  yet been validated in the field. Please send ground feedback to UNITAR-UNOSAT..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-waters-in-central-northern-bangladesh]'
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
    description: Irrigated and rainfed cropland areas affected by detected surface
      water, estimated at 1,039,350 ha
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
- asset_type:
    description: Population potentially exposed to flood-affected areas, approximately
      10,000,000 people across Dhaka and Rajshahi divisions
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_2
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
  description: Sentinel-1 SAR satellite imagery acquired on 22 August 2017 was analyzed
    by UNOSAT to detect surface water extent through comparison with reference imagery.
    Detected water polygons were intersected with agricultural land use data to quantify
    cropland exposure (1,039,350 ha) and with WorldPop gridded population data to
    estimate population exposure (~10,000,000 people) across the study area in central
    and northern Bangladesh.
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
    name: Sentinel-1 SAR
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/satellite-detected-waters-in-central-northern-bangladesh
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
  description: Satellite Detected Waters in Central & Northern Bangladesh (Zipped
    geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/BD/FL20170815BGD/FL20170815BGD_gdb.zip
  format: Geodatabase
  id: resource_ba6115f9
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20170815BGD_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite Detected Waters in Central & Northern Bangladesh (Zipped
    shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/BD/FL20170815BGD/FL20170815BGD_shp.zip
  format: null
  id: resource_0e17646c
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20170815BGD_shp.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-bgd_unosat_detectedwaterscentralnort_20170823
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
  start: '2017-08-23'
temporal_resolution: null
title: Satellite Detected Waters in Central & Northern Bangladesh
version: null
vulnerability: null
---
