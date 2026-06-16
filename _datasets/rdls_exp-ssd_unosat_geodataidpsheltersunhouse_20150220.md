---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-idp-shelters-in-un-house-compound-juba-south-sudan-february-20-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-idp-shelters-in-un-house-compound-juba-south-sudan-february-20-2015
dataset_id: rdls_exp-ssd_unosat_geodataidpsheltersunhouse_20150220
description: 'This map illustrates IDP shelters in the UN House compound in Juba,
  South Sudan, as seen by the GeoEye-1 satellite on 15 February 2015. Imagery acquired
  on that date indicates that the four IDP Protection of Civilian areas (PoCs) occupy
  16 hectares. As of 15 February 2015 a total of 2,910 shelters were detected, as
  well as 85 infrastructure and support buildings, within the PoCs. This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to UNITAR / UNOSAT.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-idp-shelters-in-un-house-compound-juba-south-sudan-february-20-2015]'
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
    description: IDP shelter structures detected via satellite imagery in UN House
      compound PoCs
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
    description: Infrastructure and support buildings within IDP Protection of Civilian
      areas
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: UNOSAT analysts reviewed GeoEye-1 satellite imagery acquired on 15
    February 2015 of the UN House compound in Juba and manually detected shelter structures
    and infrastructure buildings within four IDP Protection of Civilian areas, producing
    a spatial inventory of 2,910 shelters and 85 support buildings across 16 hectares.
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
- href: https://data.humdata.org/dataset/geodata-of-idp-shelters-in-un-house-compound-juba-south-sudan-february-20-2015
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
  description: Geodata of IDP Shelters in UN House Compound, Juba, South Sudan (Shapefile)
  download_url: https://cern.ch/unosat-maps/SS/CE20131218SSD/CE20131218SSD_shp.zip
  format: null
  id: resource_a42733ac
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
  description: Geodata of IDP Shelters in UN House Compound, Juba, South Sudan (Shapefile)
  download_url: https://cern.ch/unosat-maps/SS/CE20131218SSD/CE20131218SSD.gdb.zip
  format: null
  id: resource_fea51a20
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
slug: rdls_exp-ssd_unosat_geodataidpsheltersunhouse_20150220
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
  start: '2015-02-20'
temporal_resolution: null
title: Geodata of IDP Shelters in UN House Compound, Juba, South Sudan
version: null
vulnerability: null
---
