---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-idps-in-unmiss-base-bor-jonglei-state-south-sudan-october-30-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-idps-in-unmiss-base-bor-jonglei-state-south-sudan-october-30-2015
dataset_id: rdls_exp-ssd_unosat_geodataidpsunmissbaseborj_20151030
description: 'This map illustrates satellite-detected areas of IDPs in Bor UNMISS
  Base and Protection of Civilian (PoC) areas, in Jonglei state, as seen by the WorldView-3
  satellite on 8 October 2015. The IDP structures were moved from the old PoC area
  in the northeast of the base to the new PoC area found in the south, and currently
  all the IDP shelters are now entirely in the southern extension of the UNMISS base.
  There are currently 1,077 structures in the IDP settlement with 101 consisting of
  infrastructure buildings and 976 of shelter structures. A large part of the camp
  still remains unoccupied and this can be seen as the Contingency area. This is a
  preliminary analysis and has not yet been validated in the field. Please send ground
  feedback to UNITAR -UNOSAT. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-idps-in-unmiss-base-bor-jonglei-state-south-sudan-october-30-2015]'
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
    description: IDP shelter structures and infrastructure buildings in UNMISS Base
      PoC area, satellite-detected
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
    description: Internally displaced persons population residing in the UNMISS Base
      PoC settlement
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
  description: UNOSAT analysts interpreted WorldView-3 satellite imagery acquired
    on 8 October 2015 to identify and delineate IDP shelter structures and infrastructure
    buildings within the Bor UNMISS Base Protection of Civilian area in Jonglei State.
    Structures were manually digitized and classified into shelter (976 units) and
    infrastructure (101 units) categories, with confidence levels and validation flags
    recorded for each feature.
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
- href: https://data.humdata.org/dataset/geodata-of-idps-in-unmiss-base-bor-jonglei-state-south-sudan-october-30-2015
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
  description: Geodata of IDPs in UNMISS Base, Bor, Jonglei State, South Sudan (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SS/CE20131218SSD/CE20131218SSD_shp.zip
  format: null
  id: resource_ef227bc1
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
  description: Geodata of IDPs in UNMISS Base, Bor, Jonglei State, South Sudan (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SS/CE20131218SSD/CE20131218SSD.gdb.zip
  format: null
  id: resource_ec6fb5f2
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20131218SSD.gdb.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-ssd_unosat_geodataidpsunmissbaseborj_20151030
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
  start: '2015-10-30'
temporal_resolution: null
title: Geodata of IDPs in UNMISS Base, Bor, Jonglei State, South Sudan
version: null
vulnerability: null
---
