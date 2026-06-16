---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-idp-shelters-in-un-house-compound-juba-central-equatoria-south-sud-october-14-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-idp-shelters-in-un-house-compound-juba-central-equatoria-south-sud-october-14-2015
dataset_id: rdls_exp-ssd_unosat_geodataidpsheltersunhouse_20151014
description: 'This map illustrates satellite-detected areas of IDP shelters in the
  UN House compound in Juba, Central Equatoria, South Sudan, as seen by WorldView-3
  satellite on 25 September 2015. Satellite imagery analysis indicates that the Protection
  of Civilians (PoCs) areas occupy 89 hectares, and as of 25 September 2015 they contained
  a total of 8,214 shelters and 239 infrastructure and support buildings. Also, as
  seen in inset 2 and 3 of PoC 2 from 22 August 2015 and 25 September 2015 all shelters
  have been removed and relocated as part of reorganization efforts in the area. This
  is a preliminary analysis and has not yet been validated in the field. Please send
  ground feedback to UNITAR - UNOSAT.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-idp-shelters-in-un-house-compound-juba-central-equatoria-south-sud-october-14-2015]'
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
      compound PoC areas
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
    description: Support and infrastructure buildings within IDP shelter compound
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
- asset_type:
    description: Internally displaced persons population residing in satellite-detected
      shelters
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_3
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: UNOSAT analysts reviewed WorldView-3 satellite imagery from 25 September
    2015 and compared it with earlier imagery (22 August 2015) to detect shelter structures
    and infrastructure within the UN House compound PoC areas in Juba. Shelter and
    building counts were derived through manual feature extraction and spatial analysis
    of satellite-detected structures, producing a geodatabase of shelter locations
    and associated metadata for displacement monitoring.
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
- href: https://data.humdata.org/dataset/geodata-of-idp-shelters-in-un-house-compound-juba-central-equatoria-south-sud-october-14-2015
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
  description: Geodata of IDP Shelters in UN House Compound, Juba, Central Equatoria,
    South Sudan (Shapefile)
  download_url: https://cern.ch/unosat-maps/SS/CE20131218SSD/CE20131218SSD_shp.zip
  format: null
  id: resource_4dc2af69
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
  description: Geodata of IDP Shelters in UN House Compound, Juba, Central Equatoria,
    South Sudan (Shapefile)
  download_url: https://cern.ch/unosat-maps/SS/CE20131218SSD/CE20131218SSD.gdb.zip
  format: null
  id: resource_b58259f4
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
slug: rdls_exp-ssd_unosat_geodataidpsheltersunhouse_20151014
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
  start: '2015-10-14'
temporal_resolution: null
title: Geodata of IDP Shelters in UN House Compound, Juba, Central Equatoria, South
  Sudan
version: null
vulnerability: null
---
