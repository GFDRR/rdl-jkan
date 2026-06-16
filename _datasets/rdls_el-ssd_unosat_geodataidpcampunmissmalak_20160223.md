---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-idp-camp-in-unmiss-malakal-base-malakal-south-sudan-february-23-2016
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-idp-camp-in-unmiss-malakal-base-malakal-south-sudan-february-23-2016
dataset_id: rdls_el-ssd_unosat_geodataidpcampunmissmalak_20160223
description: 'This map illustrates satellite-detected areas of IDPs in the UNMISS
  Malakal base as seen by the WorldView-2 satellite. As of 20 February 2016, 6,438
  shelters as well as 228 infrastructure and support buildings were identified. Burned
  areas in sectors 1, 2 and 3 were also visible. A total of 2,839 structures were
  burned, including 96 camp infrastructure buildings and 2,743 shelters. As can be
  seen from the imagery, the number of structures in the initial Protection of Civilians
  (PoC) zones 1, 2, 3 and 4 has increased since the fire, and an additional area has
  been set up with shelters. Sectors 1 and 2 are newer PoC extensions with larger
  shelters, each holding up to 30 people. This is a preliminary analysis and has not
  yet been validated in the field. Please send ground feedback to UNITAR-UNOSAT..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-idp-camp-in-unmiss-malakal-base-malakal-south-sudan-february-23-2016]'
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
    description: Shelter structures and camp infrastructure buildings in UNMISS Malakal
      PoC zones identified via satellite imagery
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
    description: Internally displaced persons population residing in the Malakal IDP
      camp
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
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: UNOSAT analysts reviewed and compared multi-temporal WorldView-2 satellite
    imagery to identify shelter and infrastructure structures in the UNMISS Malakal
    PoC camp and detect burned areas resulting from a fire event. Structures were
    manually delineated and classified by type (shelter vs. infrastructure) and damage
    status, producing a geospatial inventory of camp assets and direct fire impacts.
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
- href: https://data.humdata.org/dataset/geodata-of-idp-camp-in-unmiss-malakal-base-malakal-south-sudan-february-23-2016
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from fire event affecting shelters and camp
      infrastructure in Malakal PoC zones
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
  description: Geodata of IDP Camp in UNMISS Malakal Base, Malakal, South Sudan (Shapefile)
  download_url: https://cern.ch/unosat-maps/SS/CE20131218SSD/CE20131218SSD_Malakal_20Feb2016.shp.zip
  format: null
  id: resource_2d07305d
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20131218SSD_Malakal_20Feb2016.shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of IDP Camp in UNMISS Malakal Base, Malakal, South Sudan (Shapefile)
  download_url: https://cern.ch/unosat-maps/SS/CE20131218SSD/CE20131218SSD_Malakal_20Feb2016.gdb.zip
  format: null
  id: resource_2413c2b7
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20131218SSD_Malakal_20Feb2016.gdb.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-ssd_unosat_geodataidpcampunmissmalak_20160223
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
  start: '2016-02-23'
temporal_resolution: null
title: Geodata of IDP Camp in UNMISS Malakal Base, Malakal, South Sudan
version: null
vulnerability: null
---
