---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-sido-refugee-camp-moyen-chari-region-republic-of-chad-june-19-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-sido-refugee-camp-moyen-chari-region-republic-of-chad-june-19-2014
dataset_id: rdls_exp-tcd_unosat_geodatasidorefugeecampmoy_20140619
description: 'This map illustrates satellite-detected areas of likely refugee populations
  in Sido village, Moyen - Chari Region, Republic of Chad, as seen by the WorldView-1
  and WorldView-2 satellites on 29 January 2014 and 13 June 2014. As of 29 January,
  fleeing outbreaks of violence in the Central African Republic, refugees had established
  a primary settlement area in the central portion of Sido village and along the primary
  road. As of that date, the camp included approximately 543 improvised shelters and
  200 tent shelters. As of 13 June 2014 approximately 2,731 tent shelters and new
  housing structures, 798 improvised shelters or small huts, and 1,255 tukuls or large
  huts were detected within and around Sido village. This is a preliminary analysis
  and has not yet been validated in the field. Please send ground feedback to UNITAR
  / UNOSAT.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-sido-refugee-camp-moyen-chari-region-republic-of-chad-june-19-2014]'
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
    description: Refugee shelter structures (improvised shelters and tent shelters)
      detected via satellite imagery in Sido refugee camp
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
    description: Refugee population residing in Sido camp, inferred from shelter counts
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
license: CC-BY-4.0
lineage:
  description: UNOSAT analysts reviewed and compared WorldView-1 and WorldView-2 satellite
    imagery from 29 January 2014 and 13 June 2014 to detect changes in refugee settlement
    patterns and shelter structures in Sido village. Satellite-detected shelter locations
    and camp boundaries were digitized and validated to create a spatial inventory
    of refugee camp infrastructure and population distribution.
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
- href: https://data.humdata.org/dataset/geodata-of-sido-refugee-camp-moyen-chari-region-republic-of-chad-june-19-2014
  rel: source
loss: null
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
  id: resource_6f8aa8f6
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
  id: resource_3657d0c0
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
slug: rdls_exp-tcd_unosat_geodatasidorefugeecampmoy_20140619
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
  start: '2014-06-19'
temporal_resolution: null
title: Geodata of Sido Refugee Camp, Moyen - Chari Region, Republic of Chad
version: null
vulnerability: null
---
