---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-idp-camp-expansion-in-unmiss-base-juba-airport-south-sudan-january-31-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-idp-camp-expansion-in-unmiss-base-juba-airport-south-sudan-january-31-2014
dataset_id: rdls_el-ssd_unosat_geodataupdateidpcampexpan_20140131
description: 'This map illustrates the camp for internally displaced persons (IDPs)
  in the UNMISS base at Juba airport as seen by the WorldView-1, Pleiades and WorldView-2
  satellites on 30 January, 19 January, 7 January 2014 and 28 December 2013. As of
  28 December 2013 a significant portion of the airport was used by IDP?s shelters,
  occupying approximately 7 ha. Imagery acquired on 30 January 2014 shows that the
  total area of IDP?s occupies about 9 ha, compared to the 7.9 ha detected on 7 January
  2014. Note that IDP occupied areas include improvised shelters and, in some cases,
  administrative support and other structures. Analysis indicates the extent of the
  IDP camp on 30 January is largely unchanged from the previous analysis done using
  an image from 19 January 2014. This is a preliminary analysis and has not yet been
  validated in the field. Please send ground feedback to UNITAR / UNOSAT.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-idp-camp-expansion-in-unmiss-base-juba-airport-south-sudan-january-31-2014]'
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
    description: Internally displaced persons sheltering in UNMISS base camp at Juba
      Airport
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
hazard: null
license: CC-BY-4.0
lineage:
  description: UNOSAT analysts reviewed and compared multi-temporal satellite imagery
    (December 2013 to January 2014) of the UNMISS base at Juba Airport to detect and
    map IDP shelter locations and quantify camp area expansion from 7 ha to 9 ha.
    Spatial vector data (shapefiles and geodatabase) were produced from manual image
    interpretation and change detection analysis.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/geodata-of-idp-camp-expansion-in-unmiss-base-juba-airport-south-sudan-january-31-2014
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Displaced population from complex emergency/conflict requiring shelter
      in IDP camp
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
  description: 'Geodata of Update: IDP Camp Expansion in UNMISS Base, Juba Airport,
    South Sudan (Shapefile)'
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SS/CE20131218SSD/CE20131218SSD_shp.zip
  format: null
  id: resource_a0ab8d34
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
  description: 'Geodata of Update: IDP Camp Expansion in UNMISS Base, Juba Airport,
    South Sudan (Shapefile)'
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SS/CE20131218SSD/CE20131218SSD.gdb.zip
  format: null
  id: resource_5353a2c1
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
slug: rdls_el-ssd_unosat_geodataupdateidpcampexpan_20140131
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
  start: '2014-01-31'
temporal_resolution: null
title: 'Geodata of Update: IDP Camp Expansion in UNMISS Base, Juba Airport, South
  Sudan'
version: null
vulnerability: null
---
