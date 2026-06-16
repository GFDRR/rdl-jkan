---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-idp-camp-in-melut-upper-nile-state-south-sudan-december-23-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-idp-camp-in-melut-upper-nile-state-south-sudan-december-23-2014
dataset_id: rdls_exp-ssd_unosat_geodataidpcampmelutuppern_20141223
description: 'This map illustrates IDP settlements in Melut, Upper Nile State, South
  Sudan. Using high-resolution imagery optical satellite imagery collected by the
  WorldView-3 satellite on 2 December 2014, UNOSAT located 3,587 IDP structures (3,005
  shelters and 582 Tukuls). The 6 distinct IDP settlements identified by UNOSAT occupy
  a total area of 86.09 ha. Of these, a total of 214 IDP structures are found within
  the Melut UNMISS Base, covering a total area of 1.84 ha. This is a preliminary analysis
  and has not yet been validated in the field. Please send ground feedback to UNITAR
  / UNOSAT.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-idp-camp-in-melut-upper-nile-state-south-sudan-december-23-2014]'
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
    description: IDP shelter structures identified from satellite imagery, including
      3,005 shelters and 582 Tukuls across 6 settlements
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
    description: Internally displaced population residing in identified IDP camp structures
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
  description: UNOSAT analysts interpreted high-resolution optical satellite imagery
    (WorldView-3, 2 December 2014) to manually identify and delineate IDP shelter
    structures and settlement boundaries in Melut, Upper Nile State. Structures were
    classified by type (shelters vs. Tukuls) and aggregated into 6 distinct settlements
    with calculated areas. This represents a spatial inventory of displaced population
    assets derived from remote sensing observation.
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
- href: https://data.humdata.org/dataset/geodata-of-idp-camp-in-melut-upper-nile-state-south-sudan-december-23-2014
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
  description: Geodata of IDP Camp in Melut, Upper Nile State, South Sudan (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SS/CE20131218SSD/CE20131218SSD_Melut_shp.zip
  format: null
  id: resource_6d21ee52
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20131218SSD_Melut_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of IDP Camp in Melut, Upper Nile State, South Sudan (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SS/CE20131218SSD/CE20131218SSD_Melut.gdb.zip
  format: null
  id: resource_71467f24
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20131218SSD_Melut.gdb.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-ssd_unosat_geodataidpcampmelutuppern_20141223
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
  start: '2014-12-23'
temporal_resolution: null
title: Geodata of IDP Camp in Melut, Upper Nile State, South Sudan
version: null
vulnerability: null
---
