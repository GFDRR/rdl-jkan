---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/structures-at-the-yusuf-batil-settlement-in-south-sudan-2751
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/structures-at-the-yusuf-batil-settlement-in-south-sudan-2751
dataset_id: rdls_exp-ssd_unosat_structuresyusufbatilsettl_20180103
description: 'This map illustrates satellite-detected structures in the area of the
  Yusuf Batil settlement in South Sudan. Using a satellite image collected by the
  Pleiades satellite on 31 October 2017, UNOSAT located 15,970 structures. Of these,
  209 were administrative structures, 5,012 were improvised shelters, 70 were semi-permanent
  structures, and 10,679 were tent shelters. This settlement is located the northern
  part of the country, in Eastern Nile State, about 40km from the border with Sudan.
  The population in November 2017 was about 43,000. This is a preliminary analysis
  and has not yet been validated in the field. Please send ground feedback to UNITAR
  - UNOSAT.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/structures-at-the-yusuf-batil-settlement-in-south-sudan-2751]'
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
    description: 'Satellite-detected structures in Yusuf Batil settlement classified
      by type: administrative buildings, improvised shelters, semi-permanent structures,
      and tent shelters'
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
    description: Resident population of Yusuf Batil settlement estimated at approximately
      43,000 in November 2017
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts manually reviewed Pleiades satellite imagery from 31
    October 2017 of the Yusuf Batil IDP settlement in South Sudan and identified 15,970
    structures through visual interpretation, classifying them by shelter type (tents,
    improvised shelters, semi-permanent, administrative). The resulting spatial inventory
    provides a snapshot of settlement infrastructure and population distribution at
    a specific point in time.
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
- href: https://data.humdata.org/dataset/structures-at-the-yusuf-batil-settlement-in-south-sudan-2751
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
  description: Structures at the Yusuf Batil settlement in South Sudan. (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SS/CE20131218SSD/CE20131218SSD_UNOSAT_REACH_2017.gdb.zip
  format: Geodatabase
  id: resource_c5237571
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20131218SSD_UNOSAT_REACH_2017.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Structures at the Yusuf Batil settlement in South Sudan. (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SS/CE20131218SSD/CE20131218SSD_UNOSAT_REACH_2017_shp.zip
  format: null
  id: resource_ef181312
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20131218SSD_UNOSAT_REACH_2017_shp.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-ssd_unosat_structuresyusufbatilsettl_20180103
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
  start: '2018-01-03'
temporal_resolution: null
title: Structures at the Yusuf Batil settlement in South Sudan.
version: null
vulnerability: null
---
