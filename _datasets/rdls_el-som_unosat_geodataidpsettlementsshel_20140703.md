---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-idp-settlements-and-shelters-in-kismayo-lower-juba-somalia-july-03-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-idp-settlements-and-shelters-in-kismayo-lower-juba-somalia-july-03-2014
dataset_id: rdls_el-som_unosat_geodataidpsettlementsshel_20140703
description: 'This map illustrates probable IDP shelters in Kismayo, Somalia as seen
  in satellite imagery collected by the WorldView-1 satellite on 3 May 2014. In this
  area UNOSAT located 2,952 shelters in 64 apparent IDP settlements. However, poor
  image quality, density of shelters, and varied construction material introduces
  significant uncertainty into this analysis. The IDP settlement areas were also compared
  to an image from 05 March 2014 collected by the WorldView-1 satellite to give indications
  on whether settlements were new, had closed, or were increasing or decreasing in
  size. This is a preliminary analysis and has not yet been validated in the field.
  Please send ground feedback to UNITAR / UNOSAT.. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/geodata-of-idp-settlements-and-shelters-in-kismayo-lower-juba-somalia-july-03-2014]'
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
      by settlement and construction material
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
hazard: null
license: CC-BY-4.0
lineage:
  description: UNOSAT analysts manually interpreted WorldView-1 satellite imagery
    from 3 May 2014 and compared it with imagery from 5 March 2014 to identify and
    map 2,952 IDP shelters across 64 settlements in Kismayo. Change detection analysis
    assessed settlement dynamics (new, closed, expanding, contracting). Shelter locations
    and settlement boundaries were digitized as vector geometries with attributes
    including shelter count, area, confidence levels, and validation status.
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
- href: https://data.humdata.org/dataset/geodata-of-idp-settlements-and-shelters-in-kismayo-lower-juba-somalia-july-03-2014
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced population in IDP settlements resulting from
      drought-driven complex emergency
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
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
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SO/CE20130710SOM/CE20130710SOM_GalkayoKismayoLuuq_shp.zip
  format: null
  id: resource_6339224c
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20130710SOM_GalkayoKismayoLuuq_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of IDP Settlements and Shelters in Kismayo, Lower Juba, Somalia
    (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SO/CE20130710SOM/CE20130710SOM_GalkayoKismayoLuuq_gdb.gdb.zip
  format: null
  id: resource_c6a2fc68
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20130710SOM_GalkayoKismayoLuuq_gdb.gdb.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-som_unosat_geodataidpsettlementsshel_20140703
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
  start: '2014-07-03'
temporal_resolution: null
title: Geodata of IDP Settlements and Shelters in Kismayo, Lower Juba, Somalia
version: null
vulnerability: null
---
