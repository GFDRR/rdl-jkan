---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-in-maheshkhali-chakaria-and-cox-s-bazar-sadar-upazilas
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-in-maheshkhali-chakaria-and-cox-s-bazar-sadar-upazilas
dataset_id: rdls_he-bgd_unosat_detectedwaterextentmahesh_20170602
description: 'This map illustrates satellite-detected surface water extent around
  Maheshkhali, Chakaria and Cox''S Bazar Sadar Upazilas in the District of Cox''s
  Bazar, Chittagong Division in the south eastern part of Bangladesh as detected by
  a TerraSAR-X image acquired on the 1st June 2017. A total of ~20,000 ha of lands
  seem to be affected with flood waters. Some of the affected lands are mainly agricultural
  fields. The analysis of this satellite image reveals also that about 100 km of roads
  with mainly tertiary roads seem to be also potentially affected. We can also estimate,
  within this map extent and using the WorldPop data, about 265,000 people living
  in flood affected zones. This is a preliminary analysis and has not yet been validated
  in the field. Please send ground feedback to UNITAR - UNOSAT.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/satellite-detected-water-extent-in-maheshkhali-chakaria-and-cox-s-bazar-sadar-upazilas]'
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
    description: Agricultural fields affected by flood waters in the study area
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
    description: Road network (approximately 100 km of tertiary roads) potentially
      affected by flood waters
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: length
      unit: null
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
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts interpreted TerraSAR-X satellite imagery acquired on
    1 June 2017 to detect and delineate surface water extent in three upazilas of
    Cox's Bazar District, Bangladesh. The analysis involved visual comparison of satellite
    images to identify notable changes and map flooded areas, resulting in vector
    geodatabase and shapefile outputs with area measurements in hectares and affected
    infrastructure lengths.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/satellite-detected-water-extent-in-maheshkhali-chakaria-and-cox-s-bazar-sadar-upazilas
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
  description: Bangladesh - Satellite Detected Water Extent in Maheshkhali, Chakaria
    and Cox'S Bazar Sadar Upazilas (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/BD/TC20170529BGD/TC20170529BGD_gdb.zip
  format: Geodatabase
  id: resource_c70f02ed
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20170529BGD_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bangladesh - Satellite Detected Water Extent in Maheshkhali, Chakaria
    and Cox'S Bazar Sadar Upazilas (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/BD/TC20170529BGD/TC20170529BGD_SHP.zip
  format: null
  id: resource_e97172d3
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20170529BGD_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-bgd_unosat_detectedwaterextentmahesh_20170602
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
  start: '2017-06-02'
temporal_resolution: null
title: Bangladesh - Satellite Detected Water Extent in Maheshkhali, Chakaria and Cox'S
  Bazar Sadar Upazilas
version: null
vulnerability: null
---
