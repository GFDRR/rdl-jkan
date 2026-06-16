---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-shagarab-1-refugee-camp-al-qadarif-province-sudan-july-21-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-shagarab-1-refugee-camp-al-qadarif-province-sudan-july-21-2014
dataset_id: rdls_exp-sdn_unosat_geodatashagarab1refugeeca_20140721
description: 'This map illustrates satellite-detected structures at the Shagarab 1
  refugee camp in al Qadarif Province, Sudan as seen on 09 December 2013 by the WorldView-2
  satellite. This camp lies about 70 km South-East of New Halfa and 105 km North-East
  of Al Qadarif city. UNOSAT analyzed a total of 6,242 structures in the 209 ha of
  the camp. This is a preliminary analysis and has not yet been validated in the field.
  Please send ground feedback to UNITAR / UNOSAT.. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/geodata-of-shagarab-1-refugee-camp-al-qadarif-province-sudan-july-21-2014]'
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
    description: Satellite-detected structures at Shagarab 1 refugee camp identified
      from WorldView-2 imagery
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
    description: Refugee population residing in structures at Shagarab 1 camp
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
  description: UNOSAT analysts manually reviewed WorldView-2 satellite imagery from
    December 2013 and identified 6,242 structures across 209 hectares of Shagarab
    1 refugee camp through visual interpretation and comparison of satellite images.
    The resulting geodatabase contains structure locations and counts as spatial features
    representing the built environment of the camp.
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
- href: https://data.humdata.org/dataset/geodata-of-shagarab-1-refugee-camp-al-qadarif-province-sudan-july-21-2014
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
  description: Geodata of Shagarab 1 Refugee Camp, Al Qadarif Province, Sudan (Geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SD/RC20140709SDN/RC20140709SDN.gdb.zip
  format: Geodatabase
  id: resource_745ee50a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: RC20140709SDN.gdb.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-sdn_unosat_geodatashagarab1refugeeca_20140721
spatial:
  bbox: null
  centroid: null
  countries:
  - SDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2014-07-21'
temporal_resolution: null
title: Geodata of Shagarab 1 Refugee Camp, Al Qadarif Province, Sudan
version: null
vulnerability: null
---
