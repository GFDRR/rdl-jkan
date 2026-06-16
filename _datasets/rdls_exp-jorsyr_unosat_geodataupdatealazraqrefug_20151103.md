---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-al-azraq-refugee-camp-az-zarqa-governorate-jordan-november-03-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-al-azraq-refugee-camp-az-zarqa-governorate-jordan-november-03-2015
dataset_id: rdls_exp-jorsyr_unosat_geodataupdatealazraqrefug_20151103
description: 'This map illustrates the refugee settlement in Al Azraq, Jordan as seen
  by the Pleiades satellite on 5 October 2015. Analysis by UNITAR-UNOSAT of the satellite
  image indicates a total of 14,227 structures are visible. This total includes 2,690
  infrastructure and support buildings as well as 10,071 transitional shelters. Preparations
  are continuing so as to accommodate additional incoming refugees. The previous analysis
  done by UNOSAT using an image from 11 November 2014 detected a total of 12,761 infrastructure,
  support buildings and transitional shelters. This is an increase of approximately
  0.5%. Water and sanitation services are also under development in multiple camp
  zones suitable for supporting thousands of proximate shelters. This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to UNITAR - UNOSAT.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-al-azraq-refugee-camp-az-zarqa-governorate-jordan-november-03-2015]'
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
    description: Transitional shelters and infrastructure buildings in Al Azraq refugee
      camp identified from satellite imagery
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
    description: Refugee population residing in Al Azraq camp
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
  description: UNOSAT analysts interpreted Pleiades satellite imagery from 5 October
    2015 of Al Azraq refugee camp, manually identifying and counting 14,227 structures
    (10,071 transitional shelters and 2,690 infrastructure/support buildings) through
    comparative analysis with previous imagery from November 2014. Results were delivered
    as vector geodata (shapefile and geodatabase formats) representing the spatial
    distribution and classification of refugee settlement structures.
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
- href: https://data.humdata.org/dataset/geodata-of-al-azraq-refugee-camp-az-zarqa-governorate-jordan-november-03-2015
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
  description: 'Geodata of Update: Al Azraq Refugee Camp, Az Zarqa Governorate, Jordan
    (Shapefile)'
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SY/CE20130604SYR/Azraq_20151103_shp.zip
  format: null
  id: resource_80be883f
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Azraq_20151103_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Geodata of Update: Al Azraq Refugee Camp, Az Zarqa Governorate, Jordan
    (Shapefile)'
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SY/CE20130604SYR/Azraq_20151103.gdb.zip
  format: null
  id: resource_6eb67c76
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Azraq_20151103.gdb.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-jorsyr_unosat_geodataupdatealazraqrefug_20151103
spatial:
  bbox: null
  centroid: null
  countries:
  - SYR
  - JOR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-11-03'
temporal_resolution: null
title: 'Geodata of Update: Al Azraq Refugee Camp, Az Zarqa Governorate, Jordan'
version: null
vulnerability: null
---
