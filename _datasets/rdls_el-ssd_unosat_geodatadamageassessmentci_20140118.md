---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-in-the-city-of-bentiu-unity-state-south-sudan-january-18-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-in-the-city-of-bentiu-unity-state-south-sudan-january-18-2014
dataset_id: rdls_el-ssd_unosat_geodatadamageassessmentci_20140118
description: 'This map illustrates satellite-detected areas of damage in the town
  of Bentiu, South Sudan, resulting from ongoing violence in the area. Using an image
  collected 18 January 2014 by the WorldView-1 satellite, UNOSAT identified almost
  1,200 destroyed structures in and around the town. Destruction is largely concentrated
  along the northern edge of the town along the Bahr al-Gazal river bank and primarily
  affects homes and related structures as well as some commercial buildings. Using
  pre-conflict building data UNOSAT estimates that about 8% of the structures in Bentiu
  are destroyed. This is a preliminary analysis and is based on an enhanced rapid
  analysis methodology. It has not yet been validated in the field. Please send ground
  feedback to UNITAR / UNOSAT.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-damage-assessment-in-the-city-of-bentiu-unity-state-south-sudan-january-18-2014]'
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
    description: Building stock in Bentiu town classified by damage status from satellite
      imagery
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
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: UNOSAT analysts compared pre-conflict and post-conflict satellite imagery
    (WorldView-1, January 2014) to identify structural damage in Bentiu. Building
    footprints were manually delineated and classified as destroyed or intact, with
    confidence levels assigned. Approximately 1,200 destroyed structures were identified
    and georeferenced as polygon features, representing ~8% of the total building
    stock based on pre-conflict baseline data.
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
- href: https://data.humdata.org/dataset/geodata-of-damage-assessment-in-the-city-of-bentiu-unity-state-south-sudan-january-18-2014
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from conflict-related destruction
      in Bentiu
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
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
  description: Geodata of Damage Assessment in the City of Bentiu, Unity State, South
    Sudan (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SS/CE20131218SSD/CE20131218SSD_shp.zip
  format: null
  id: resource_04aa5eaf
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20131218SSD_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Damage Assessment in the City of Bentiu, Unity State, South
    Sudan (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SS/CE20131218SSD/CE20131218SSD.gdb.zip
  format: null
  id: resource_fe0e800c
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20131218SSD.gdb.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-ssd_unosat_geodatadamageassessmentci_20140118
spatial:
  bbox: null
  centroid: null
  countries:
  - SSD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2014-01-18'
temporal_resolution: null
title: Geodata of Damage Assessment in the City of Bentiu, Unity State, South Sudan
version: null
vulnerability: null
---
