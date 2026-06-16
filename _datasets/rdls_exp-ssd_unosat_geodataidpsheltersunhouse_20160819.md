---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-idp-shelters-in-un-house-compound-juba-central-equatoria-south-sud-august-19-2016
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-idp-shelters-in-un-house-compound-juba-central-equatoria-south-sud-august-19-2016
dataset_id: rdls_exp-ssd_unosat_geodataidpsheltersunhouse_20160819
description: 'This map illustrates satellite-detected areas of IDP shelters in the
  UN House compound in Juba, Central Equatoria, South Sudan. UNITAR-UNOSAT analysis
  of WorldView-3 satellite imagery acquired 18 August 2016 revealed a total of 8,706
  shelters as well as 345 infrastructure and support buildings within the compound.
  This represents an increase of approximately 2.7 percent in shelters and an increase
  of roughly 50 percent in infrastructure and support buildings since the previous
  UNITAR-UNOSAT analysis of 27 June 2016 satellite imagery. New structures and containers
  were detected within PoC2 on 27 June 2016, as seen in inset 2. This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to UNITAR - UNOSAT.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-idp-shelters-in-un-house-compound-juba-central-equatoria-south-sud-august-19-2016]'
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
    description: IDP shelter structures and infrastructure buildings detected via
      satellite imagery in UN House compound
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
    description: Internally displaced persons population residing in shelters within
      the compound
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
  description: UNOSAT analysts interpreted WorldView-3 satellite imagery acquired
    on 18 August 2016 and 5 September 2016 over the UN House compound in Juba, comparing
    multi-temporal images to detect shelter structures and infrastructure buildings
    through visual analysis and change detection. The resulting geodata provides spatial
    inventory of IDP shelters and support facilities as exposure assets.
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
- href: https://data.humdata.org/dataset/geodata-of-idp-shelters-in-un-house-compound-juba-central-equatoria-south-sud-august-19-2016
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
  description: Geodata of IDP Shelters in UN House Compound, Juba, Central Equatoria,
    South Sudan (Shapefile)
  download_url: https://cern.ch/unosat-maps/SS/CE20131218SSD/CE20131218SSD_Juba_20160818_shp.zip
  format: null
  id: resource_57b06e53
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20131218SSD_Juba_20160818_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of IDP Shelters in UN House Compound, Juba, Central Equatoria,
    South Sudan (Shapefile)
  download_url: https://cern.ch/unosat-maps/SS/CE20131218SSD/CE20131218SSD_Juba_20160818.gdb.zip
  format: null
  id: resource_c944edae
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20131218SSD_Juba_20160818.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of IDP Shelters in UN House Compound, Juba, Central Equatoria,
    South Sudan (Shapefile)
  download_url: https://cern.ch/unosat-maps/SS/CE20131218SSD/CE20131218SSD_Juba_20160905_shp.zip
  format: null
  id: resource_4226b4c7
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20131218SSD_Juba_20160905_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of IDP Shelters in UN House Compound, Juba, Central Equatoria,
    South Sudan (Shapefile)
  download_url: https://cern.ch/unosat-maps/SS/CE20131218SSD/CE20131218SSD_Juba_20160905.gdb.zip
  format: null
  id: resource_bad12054
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20131218SSD_Juba_20160905.gdb.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-ssd_unosat_geodataidpsheltersunhouse_20160819
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
  start: '2016-08-19'
temporal_resolution: null
title: Geodata of IDP Shelters in UN House Compound, Juba, Central Equatoria, South
  Sudan
version: null
vulnerability: null
---
