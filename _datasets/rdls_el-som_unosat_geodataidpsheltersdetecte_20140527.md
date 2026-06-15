---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-idp-shelters-detected-north-of-galkayo-somalia-may-27-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-idp-shelters-detected-north-of-galkayo-somalia-may-27-2014
dataset_id: rdls_el-som_unosat_geodataidpsheltersdetecte_20140527
description: 'This map illustrates satellite-detected shelters for displaced persons
  north of Galkayo in Somalia. Using a WorldView-2 image collected on 20 April 2014,
  UNOSAT located and marked a total of 2,816 new structures (1,879 metal shelters
  structures, 906 improvised shelters (buuls) and 31 administrative structures) in
  four camp areas. In addition of the previous analysis, a total of 5,068 IDP structures
  has been located in and around the town of Galkayo. This is a preliminary analysis
  & has not yet been validated in the field. Please send ground feedback to UNITAR
  / UNOSAT.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-idp-shelters-detected-north-of-galkayo-somalia-may-27-2014]'
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
    description: IDP shelter structures detected via satellite imagery, classified
      by shelter type (metal shelters, improvised buuls, administrative structures)
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: UNOSAT analysts reviewed WorldView-2 satellite imagery from 20 April
    2014 and compared it with previous imagery to identify and map newly constructed
    IDP shelter structures in four camp areas north of Galkayo. Shelters were classified
    by type (metal structures, improvised buuls, administrative buildings) and georeferenced
    as point or polygon features. The dataset represents a preliminary satellite-based
    assessment of displaced population shelter infrastructure.
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
- href: https://data.humdata.org/dataset/geodata-of-idp-shelters-detected-north-of-galkayo-somalia-may-27-2014
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Internally displaced persons shelters detected in IDP camps north
      of Galkayo, Somalia
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
  description: Geodata of IDP Shelters Detected, North of Galkayo, Somalia (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SO/CE20130710SOM/CE20130710SOM_Galkayo_shp.zip
  format: null
  id: resource_f0ee91c1
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20130710SOM_Galkayo_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of IDP Shelters Detected, North of Galkayo, Somalia (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SO/CE20130710SOM/CE20130710SOM_Galkayo_gdb.zip
  format: null
  id: resource_65a53abd
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20130710SOM_Galkayo_gdb.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-som_unosat_geodataidpsheltersdetecte_20140527
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
  start: '2014-05-27'
temporal_resolution: null
title: Geodata of IDP Shelters Detected, North of Galkayo, Somalia
version: null
vulnerability: null
---
