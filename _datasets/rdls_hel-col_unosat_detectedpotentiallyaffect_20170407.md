---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-potentially-affected-zones-by-the-mudflow-in-mocoa-colombia
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-potentially-affected-zones-by-the-mudflow-in-mocoa-colombia
dataset_id: rdls_hel-col_unosat_detectedpotentiallyaffect_20170407
description: 'This map illustrates satellite-detected water bodies and inundated areas
  in Mocoa city, Putumayo department in Colombia as seen on Resourcesat-2 satellite
  imagery collected 04 April 2017. Heavy rainfall in the area caused flooding, landslides
  and mudflow that affected the city. UNOSAT extracted a water index from the satellite
  image to determine areas of standing water as well as soils with varying levels
  of water content (i.e. mud). Within the city of Mocoa and the current map extent,
  about 18 km of roads are potentially affected. About 2900 buildings are within areas
  which experienced floods and mudflow. It is likely that flood waters and inundation
  have been systematically underestimated along highly vegetated areas and within
  built-up urban areas because of the special characteristics of the satellite data
  used. This analysis has not yet been validated in the field. Please send ground
  feedback to UNITAR /UNOSAT.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-potentially-affected-zones-by-the-mudflow-in-mocoa-colombia]'
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
    description: Building stock within flood and mudflow-affected zones in Mocoa city
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Road network potentially affected by flooding and mudflow
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
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: LSI:-
      process: landslide_mudflow
      trigger: null
      type: landslide
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts processed Resourcesat-2 satellite imagery from 4 April
    2017 to extract a water index identifying standing water and mud-saturated soils
    in Mocoa following heavy rainfall-triggered flooding and mudflow. Satellite-detected
    inundated zones were mapped as polygons with area calculations and overlaid with
    building footprints and road networks to quantify exposure and direct impacts.
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
- href: https://data.humdata.org/dataset/satellite-detected-potentially-affected-zones-by-the-mudflow-in-mocoa-colombia
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Buildings within satellite-detected mudflow and inundated areas
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_1
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
  - asset_category: infrastructure
    asset_dimension: structure
    description: Road infrastructure affected by mudflow and flooding
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
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
  description: Colombia - Satellite detected potentially affected zones by the mudflow
    in Mocoa. (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/CO/LS20170403COL/LS20170403COL.gdb.zip
  format: Geodatabase
  id: resource_138d2460
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: LS20170403COL.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Colombia - Satellite detected potentially affected zones by the mudflow
    in Mocoa. (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/CO/LS20170403COL/LS20170403COL_SHP.zip
  format: null
  id: resource_931361be
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: LS20170403COL_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-col_unosat_detectedpotentiallyaffect_20170407
spatial:
  bbox: null
  centroid: null
  countries:
  - COL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-04-07'
temporal_resolution: null
title: Colombia - Satellite detected potentially affected zones by the mudflow in
  Mocoa.
version: null
vulnerability: null
---
