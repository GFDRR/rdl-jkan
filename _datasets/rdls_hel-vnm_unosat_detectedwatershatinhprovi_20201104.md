---
attributions:
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/satellite-detected-waters-in-ha-tinh-province-of-viet-nam-as-of-3-november-2020
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: SAOCOM-1A
    url: https://data.humdata.org/dataset/satellite-detected-waters-in-ha-tinh-province-of-viet-nam-as-of-3-november-2020
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-waters-in-ha-tinh-province-of-viet-nam-as-of-3-november-2020
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-waters-in-ha-tinh-province-of-viet-nam-as-of-3-november-2020
dataset_id: rdls_hel-vnm_unosat_detectedwatershatinhprovi_20201104
description: 'UNOSAT code: TC20201028VNM This map illustrates satellite-detected surface
  waters in Ha Tinh Province of Viet Nam as observed from a SAOCOM-1A image acquired
  on 3 November 2020 at about 16:52 local time. Within the analyzed area of about
  5,800 km2, a total of about 580 km2 of lands appear to be flooded. The water extent
  appears to have increased of about 80 km2 since 30 October 2020. Based on Worldpop
  population data and the detected surface waters, about 260,000 people are potentially
  exposed or living close to flooded areas. This is a preliminary analysis and has
  not yet been validated in the field. Please send ground feedback to UNITAR-UNOSAT.
  Important Note: Flood analysis from radar images may underestimate the presence
  of standing waters in built-up areas and densely vegetated areas due to backscattering
  properties of the radar signal.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-waters-in-ha-tinh-province-of-viet-nam-as-of-3-november-2020]'
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
    description: Population potentially exposed or living close to flooded areas derived
      from WorldPop data
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
license: CC-BY-SA-4.0
lineage:
  description: "UNOSAT analysts processed SAOCOM-1A SAR satellite imagery acquired\
    \ on 3 November 2020 to detect surface water extent through visual interpretation\
    \ and comparison with prior imagery from 30 October 2020. Detected flood area\
    \ (580 km\xC2\xB2) was intersected with WorldPop gridded population data to estimate\
    \ approximately 260,000 people potentially exposed to flooded areas in Ha Tinh\
    \ Province."
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
    name: SAOCOM-1A
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/satellite-detected-waters-in-ha-tinh-province-of-viet-nam-as-of-3-november-2020
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population exposed to detected flood waters in Ha Tinh Province
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
  description: Satellite detected waters in Ha Tinh Province of Viet Nam as of 3 November
    2020 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/VN/TC20201028VNM/TC20201028VNM_gdb.zip
  format: Geodatabase
  id: resource_ef7b54d4
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20201028VNM_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected waters in Ha Tinh Province of Viet Nam as of 3 November
    2020 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/VN/TC20201028VNM/TC20201028VNM_SHP.zip
  format: null
  id: resource_d3c4023a
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20201028VNM_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-vnm_unosat_detectedwatershatinhprovi_20201104
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
  start: '2020-11-04'
temporal_resolution: null
title: Satellite detected waters in Ha Tinh Province of Viet Nam as of 3 November
  2020
version: null
vulnerability: null
---
