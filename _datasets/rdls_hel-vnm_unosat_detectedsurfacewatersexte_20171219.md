---
attributions:
- entity:
    affiliation: null
    email: null
    name: Radarsat-2 SAR imagery
    url: https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-in-ho-chi-minh-city-area-vietnam-2749
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-in-ho-chi-minh-city-area-vietnam-2749
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-in-ho-chi-minh-city-area-vietnam-2749
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-in-ho-chi-minh-city-area-vietnam-2749
dataset_id: rdls_hel-vnm_unosat_detectedsurfacewatersexte_20171219
description: 'This map illustrates the satellite-detected surface waters extent in
  Ho Chi Minh City area and surroundings, as observed from the Radarsat-2 SAR image
  acquired on 18 December 2017. In the analysed area (~3000 km2) about 5,400 ha of
  lands, mainly agricultural and paddy fields are likely flooded. In addition, using
  WorldPop data, we can estimate that ~220,000 people are living within flooded areas.
  It is likely that flood waters have been systematically underestimated along highly
  vegetated areas along main river banks and within built-up urban areas because of
  the special characteristics of the satellite data used. This is a preliminary analysis
  and has not yet been validated in the field. Please send ground feedback to UNITAR
  - UNOSAT.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-in-ho-chi-minh-city-area-vietnam-2749]'
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
    description: Agricultural and paddy fields in the study area affected by surface
      water
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
    description: Population living within satellite-detected flooded areas
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
  description: UNOSAT analysts processed Radarsat-2 SAR imagery from 18 December 2017
    to detect surface water extent in Ho Chi Minh City area through manual image interpretation
    and change detection. Flooded area polygons (~5,400 ha) were delineated and intersected
    with WorldPop gridded population data to estimate affected population (~220,000
    people), producing post-event flood impact assessment data.
  sources:
  - id: source_1
    license: null
    name: Radarsat-2 SAR imagery
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
- href: https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-in-ho-chi-minh-city-area-vietnam-2749
  rel: source
loss:
  losses:
  - asset_category: agriculture
    asset_dimension: product
    description: Direct agricultural land inundation from fluvial flooding detected
      via satellite imagery
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
          quantity_kind: area
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population affected by flood waters in Ho Chi Minh City area
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: flood
    id: loss_2
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
  description: Satellite Detected Surface Waters Extent in Ho Chi Minh City Area,
    Vietnam (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/VN/FL20171211VNM/FL20171211VNM_gdb.zip
  format: Geodatabase
  id: resource_830c9853
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20171211VNM_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite Detected Surface Waters Extent in Ho Chi Minh City Area,
    Vietnam (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/VN/FL20171211VNM/FL20171211VNM_shp.zip
  format: null
  id: resource_7ad5af15
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20171211VNM_shp.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-vnm_unosat_detectedsurfacewatersexte_20171219
spatial:
  bbox: null
  centroid: null
  countries:
  - VNM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-12-19'
temporal_resolution: null
title: Satellite Detected Surface Waters Extent in Ho Chi Minh City Area, Vietnam
version: null
vulnerability: null
---
