---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-landslide-in-ab-barek-badakshan-province-afghanistan-may-08-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-landslide-in-ab-barek-badakshan-province-afghanistan-may-08-2014
dataset_id: rdls_hel-afg_unosat_geodataupdatelandslideabb_20140508
description: 'This map illustrates satellite-detected areas of landslide damage in
  the village of Ab Barek, Badakshan, Afghanistan. Following heavy rains in the region,
  a landslide partially buried Ab Barek on 2 May 2014. Using a satellite image acquired
  5 May 2014 by the WorldView-2 satellite, UNOSAT delineated the landslide area. In
  addition, areas of IDPs, relief operations, and water pooling due to the landslide
  are indicated as of 5 May. The 5 May 2014 image was compared to an image from 7
  June 2013 in an attempt to determine how many structures were buried, and a total
  of 87 such structures were located. However, between 7 June 2013 and the occurrence
  of the landslide Ab Barek had changed and grown considerably, and thus its possible
  additional buried structures exist which are not identified in this analysis. This
  is a preliminary analysis and has not yet been validated in the field. Please send
  ground feedback to UNITAR / UNOSAT.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-landslide-in-ab-barek-badakshan-province-afghanistan-may-08-2014]'
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
    description: Building structures in Ab Barek village identified and mapped via
      satellite imagery
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
    description: Internally displaced persons (IDPs) identified in affected areas
      as of 5 May 2014
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
    landslide:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: LSI:-
        process: landslide_general
        trigger: null
        type: landslide
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: UNOSAT analysts performed multi-temporal satellite image analysis comparing
    WorldView-2 imagery from 5 May 2014 (post-event) with baseline imagery from 7
    June 2013 to detect and delineate the landslide area triggered by heavy rainfall
    on 2 May 2014. Change detection methods were applied to identify buried structures
    (87 counted) and map concurrent impacts including IDP locations and water pooling.
    Vector geometries were produced in shapefile and geodatabase formats.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/geodata-of-landslide-in-ab-barek-badakshan-province-afghanistan-may-08-2014
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from landslide burial; 87 structures identified
      as buried by satellite analysis
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
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons resulting from landslide event in Ab
      Barek
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
        metric: displaced
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
  description: 'Geodata of Update: Landslide in Ab Barek, Badakshan Province, Afghanistan
    (Shapefile)'
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/AF/FL20140430AFG/FL20140430AFG_shp.zip
  format: null
  id: resource_1a6add88
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20140430AFG_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Geodata of Update: Landslide in Ab Barek, Badakshan Province, Afghanistan
    (Shapefile)'
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/AF/FL20140430AFG/FL20140430AFG.gdb.zip
  format: null
  id: resource_943b9100
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20140430AFG.gdb.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-afg_unosat_geodataupdatelandslideabb_20140508
spatial:
  bbox: null
  centroid: null
  countries:
  - AFG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2014-05-08'
temporal_resolution: null
title: 'Geodata of Update: Landslide in Ab Barek, Badakshan Province, Afghanistan'
version: null
vulnerability: null
---
