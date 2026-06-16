---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-idp-settlements-and-shelters-in-kismayo-lower-juba-somalia-april-30-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-idp-settlements-and-shelters-in-kismayo-lower-juba-somalia-april-30-2014
dataset_id: rdls_exp-som_unosat_geodataidpsettlementsshel_20140430
description: 'This map illustrates probable IDP shelter in Kismayo, Somalia as seen
  in satellite imagery collected by the WorldView-1 satellite on 5 March 2014. In
  this area UNOSAT located 1,969 shelters in 57 apparent IDP settlements. However,
  poor image quality, density of shelters, and varied construction material introduces
  significant uncertainty into this analysis. The IDP settlement areas were also compared
  to an image from 11 August 2013 collected by the Pleaides satellite to give indications
  on whether settlements were new, had closed, or were increasing or decreasing in
  size. This is a preliminary analysis and has not yet been validated in the field.
  Please send ground feedback to UNITAR / UNOSAT.. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/geodata-of-idp-settlements-and-shelters-in-kismayo-lower-juba-somalia-april-30-2014]'
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
    description: IDP shelter structures identified in satellite imagery, classified
      by settlement and construction characteristics
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
    description: Internally displaced population residing in identified IDP settlements
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
  description: UNOSAT analysts compared multi-temporal satellite imagery (WorldView-1
    and Pleaides) to identify 1,969 shelters across 57 IDP settlements in Kismayo.
    Settlement areas were delineated and temporal changes assessed to determine settlement
    status (new, closed, expanding, contracting). Shelter counts and settlement polygons
    were extracted and validated against field observations where available.
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
- href: https://data.humdata.org/dataset/geodata-of-idp-settlements-and-shelters-in-kismayo-lower-juba-somalia-april-30-2014
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
  description: Geodata of IDP Settlements and Shelters in Kismayo, Lower Juba, Somalia
    (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SO/CE20130710SOM/Kismayo_shp.zip
  format: null
  id: resource_ae602e3b
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Kismayo_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of IDP Settlements and Shelters in Kismayo, Lower Juba, Somalia
    (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SO/CE20130710SOM/CE20130710SOM_Kismayo.gdb.zip
  format: null
  id: resource_b665a45e
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20130710SOM_Kismayo.gdb.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-som_unosat_geodataidpsettlementsshel_20140430
spatial:
  bbox: null
  centroid: null
  countries:
  - SOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2014-04-30'
temporal_resolution: null
title: Geodata of IDP Settlements and Shelters in Kismayo, Lower Juba, Somalia
version: null
vulnerability: null
---
