---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-sido-refugee-camp-moyen-chari-region-republic-of-chad-june-03-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-sido-refugee-camp-moyen-chari-region-republic-of-chad-june-03-2014
dataset_id: rdls_exp-tcd_unosat_geodatasidorefugeecampmoy_20140603
description: 'This map illustrates satellite-detected areas of a refugee settlement
  in Sido village, southern Chad as seen by the WorldView-1 satellite on 29 January
  2014. Fleeing outbreaks of violence in the Central African Republic, refugees have
  established a settlement in a portion of Sido village. Note that the camp occupied
  areas include 543 improvised shelters and 200 tent shelters approximately. This
  is a preliminary analysis and has not yet been validated in the field. Please send
  ground feedback to UNITAR / UNOSAT.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-sido-refugee-camp-moyen-chari-region-republic-of-chad-june-03-2014]'
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
    description: Refugee camp shelters including improvised shelters and tent structures
      mapped from satellite imagery
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
    description: Refugee population residing in Sido camp settlement
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
  description: UNOSAT analysts reviewed WorldView-1 satellite imagery from 29 January
    2014 and identified refugee settlement areas in Sido village through manual image
    interpretation and change detection analysis. Shelter structures (543 improvised
    shelters and 200 tent shelters) were mapped as vector geometries with attributes
    including site identification, sensor metadata, confidence levels, and camp status.
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
- href: https://data.humdata.org/dataset/geodata-of-sido-refugee-camp-moyen-chari-region-republic-of-chad-june-03-2014
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
  description: Geodata of Sido Refugee Camp, Moyen - Chari Region, Republic of Chad
    (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/CF/CE20131212CAF/CE20131212CAF_shp.zip
  format: null
  id: resource_9765717c
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20131212CAF_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Sido Refugee Camp, Moyen - Chari Region, Republic of Chad
    (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/CF/CE20131212CAF/CE20131212CAF.gdb.zip
  format: null
  id: resource_090f2a9a
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20131212CAF.gdb.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-tcd_unosat_geodatasidorefugeecampmoy_20140603
spatial:
  bbox: null
  centroid: null
  countries:
  - TCD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2014-06-03'
temporal_resolution: null
title: Geodata of Sido Refugee Camp, Moyen - Chari Region, Republic of Chad
version: null
vulnerability: null
---
