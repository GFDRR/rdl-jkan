---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-satellite-detected-waters-over-can-avid-in-dolores-area-eastern-sa-december-09-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-satellite-detected-waters-over-can-avid-in-dolores-area-eastern-sa-december-09-2014
dataset_id: rdls_hel-phl_unosat_geodatadetectedwatersover_20141209
description: 'This map illustrates satellite-detected areas with waters as detected
  bySentinel-1 imagery acquired the 08 December 2014 in Can-Avid municipality, west
  of Dolores city, Eastern Samar Province (Philippines). The heavy rains related to
  the typhoon Hagupit induced areas with standing waters that affected 460 ha of agriculural
  fields. This analysis has not yet been validated in the field. Please send ground
  feedback to UNITAR /UNOSAT.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-satellite-detected-waters-over-can-avid-in-dolores-area-eastern-sa-december-09-2014]'
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
    description: Agricultural fields affected by standing water in Can-Avid municipality
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
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: strong_wind
license: CC-BY-4.0
lineage:
  description: Sentinel-1 satellite imagery acquired on 8 December 2014 was analyzed
    by UNOSAT to detect standing water areas resulting from heavy rains associated
    with Typhoon Hagupit. Analysts compared satellite images to identify notable changes
    and delineate affected agricultural areas in Can-Avid municipality, Eastern Samar
    Province.
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
- href: https://data.humdata.org/dataset/geodata-of-satellite-detected-waters-over-can-avid-in-dolores-area-eastern-sa-december-09-2014
  rel: source
loss:
  losses:
  - asset_category: agriculture
    asset_dimension: product
    description: Direct impact on 460 hectares of agricultural fields from Typhoon
      Hagupit-induced standing waters
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
          unit: null
        metric: exposure
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
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
  description: Geodata of Satellite Detected Waters Over Can-Avid in Dolores Area,
    Eastern Samar, Eastern Visayas, Philippines (Shapefile)
  download_url: https://cern.ch/unosat-maps/PH/TC20141204PHL/TC20141204PHL_shp.zip
  format: null
  id: resource_ebefa8fa
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20141204PHL_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Satellite Detected Waters Over Can-Avid in Dolores Area,
    Eastern Samar, Eastern Visayas, Philippines (Shapefile)
  download_url: https://cern.ch/unosat-maps/PH/TC20141204PHL/TC20141204PHL.gdb.zip
  format: null
  id: resource_0b3ce29c
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20141204PHL.gdb.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-phl_unosat_geodatadetectedwatersover_20141209
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
  start: '2014-12-09'
temporal_resolution: null
title: Geodata of Satellite Detected Waters Over Can-Avid in Dolores Area, Eastern
  Samar, Eastern Visayas, Philippines
version: null
vulnerability: null
---
