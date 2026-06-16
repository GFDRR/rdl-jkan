---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-1 satellite imagery
    url: https://data.humdata.org/dataset/satellite-detected-water-extent-in-cox-s-bazar-district-chittagong-division-bangladesh
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/satellite-detected-water-extent-in-cox-s-bazar-district-chittagong-division-bangladesh
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-in-cox-s-bazar-district-chittagong-division-bangladesh
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-in-cox-s-bazar-district-chittagong-division-bangladesh
dataset_id: rdls_hel-bgd_unosat_detectedwaterextentcoxsba_20170531
description: 'This map illustrates satellite-detected surface water extent in the
  District of Cox''s Bazar, Chittagong Division, located in the southeastern part
  of Bangladesh after the tropical cyclone Mora-17 using a Sentinel-1 satellite image
  acquired on the 30 May 2017. A total of 23,058 ha surface waters were observed.
  In many zones, the affected lands are mainly agricultural. The analysis of this
  image reveals also that about 234 km of roads mainly tertiary roads seem to be potentially
  affected. The population exposure analysis using WorldPop data shows that ~267,000
  people are potentially affected by floods within map extent. This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to UNITAR - UNOSAT.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extent-in-cox-s-bazar-district-chittagong-division-bangladesh]'
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
    description: Agricultural lands affected by surface water inundation in Cox's
      Bazar District
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
    description: Road network (tertiary roads) potentially affected by surface water
      extent
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
- asset_type:
    description: Population potentially exposed to surface water extent based on WorldPop
      data
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_3
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
      process: coastal_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: Sentinel-1 SAR satellite imagery from 30 May 2017 was analyzed by UNOSAT
    to detect surface water extent changes in Cox's Bazar District following tropical
    cyclone Mora-17 through multi-temporal image comparison. Detected water areas
    (23,058 ha) were intersected with road networks and WorldPop population grids
    to quantify exposure of agricultural lands, infrastructure, and population to
    the inundation event.
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
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/satellite-detected-water-extent-in-cox-s-bazar-district-chittagong-division-bangladesh
  rel: source
loss:
  losses:
  - asset_category: agriculture
    asset_dimension: product
    description: Direct agricultural land inundation from tropical cyclone Mora-17
      coastal flooding
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
      process: coastal_flood
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: Direct road infrastructure disruption from tropical cyclone Mora-17
      coastal flooding
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
      process: coastal_flood
      trigger: null
      type: flood
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population affected by tropical cyclone Mora-17 coastal flooding
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
      process: coastal_flood
      trigger: null
      type: flood
    id: loss_3
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
  description: Bangladesh - Satellite Detected Water Extent in Cox's Bazar District,
    Chittagong Division (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/BD/TC20170529BGD/TC20170529BGD_gdb.zip
  format: Geodatabase
  id: resource_e3a569bc
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
  description: Bangladesh - Satellite Detected Water Extent in Cox's Bazar District,
    Chittagong Division (Zipped shapefile.)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/BD/TC20170529BGD/TC20170529BGD_SHP.zip
  format: null
  id: resource_00974165
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
- loss
schema: rdls-10
slug: rdls_hel-bgd_unosat_detectedwaterextentcoxsba_20170531
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
  start: '2017-05-31'
temporal_resolution: null
title: Bangladesh - Satellite Detected Water Extent in Cox's Bazar District, Chittagong
  Division
version: null
vulnerability: null
---
