---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-idp-camp-in-unmiss-malakal-base-malakal-south-sudan-october-22-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-idp-camp-in-unmiss-malakal-base-malakal-south-sudan-october-22-2015
dataset_id: rdls_exp-ssd_unosat_geodataidpcampunmissmalak_20151022
description: 'This map illustrates satellite-detected areas of IDPs in the UNMISS
  Malakal base as seen by the WorldView-2 satellite on 26 September 2015. Imagery
  acquired on this date shows that the IDP camp extent has increased compared with
  the previous UNOSAT analysis. Imagery also shows that shelters installed outside
  the UNMISS base are still increasing. Note that IDP occupied areas include improvised
  shelters and, in some cases, administrative support and other structures which gives
  a total number of 536 Camp infrastructure buildings and 7,791 Shelter structures.
  As can be seen from the imagery, PoC 1, 2, 3 and 4 are the initial or old Protection
  of Civilians (PoC) zones, Sector 1 and 2 are the new PoC extensions while Sector
  3 is a contingency area mainly for administrative structures and Sector 4 is void
  of any infrastructure at the moment. This is a preliminary analysis and has not
  yet been validated in the field. Please send ground feedback to UNITAR / UNOSAT..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-idp-camp-in-unmiss-malakal-base-malakal-south-sudan-october-22-2015]'
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
    description: Camp infrastructure buildings and shelter structures in UNMISS Malakal
      Base IDP camp detected via satellite imagery
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
    description: Internally displaced persons occupying the Malakal IDP camp
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
  description: UNOSAT analysts reviewed and compared satellite imagery from WorldView-2
    to detect and delineate IDP camp areas and structures in the UNMISS Malakal Base.
    Multi-temporal imagery comparison identified changes in camp extent and shelter
    distribution, resulting in spatial vector data of 536 camp infrastructure buildings
    and 7,791 shelter structures.
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
- href: https://data.humdata.org/dataset/geodata-of-idp-camp-in-unmiss-malakal-base-malakal-south-sudan-october-22-2015
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
  description: Geodata of IDP Camp in UNMISS Malakal Base, Malakal, South Sudan (Shapefile)
  download_url: https://cern.ch/unosat-maps/SS/CE20131218SSD/CE20131218SSD_shp.zip
  format: null
  id: resource_ac65c506
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
  description: Geodata of IDP Camp in UNMISS Malakal Base, Malakal, South Sudan (Shapefile)
  download_url: https://cern.ch/unosat-maps/SS/CE20131218SSD/CE20131218SSD.gdb.zip
  format: null
  id: resource_bcb06384
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
slug: rdls_exp-ssd_unosat_geodataidpcampunmissmalak_20151022
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
  start: '2015-10-22'
temporal_resolution: null
title: Geodata of IDP Camp in UNMISS Malakal Base, Malakal, South Sudan
version: null
vulnerability: null
---
