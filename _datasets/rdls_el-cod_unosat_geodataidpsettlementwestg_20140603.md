---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-idp-settlement-in-west-geti-province-orientale-democratic-republic-june-03-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-idp-settlement-in-west-geti-province-orientale-democratic-republic-june-03-2014
dataset_id: rdls_el-cod_unosat_geodataidpsettlementwestg_20140603
description: 'This map illustrates structural changes within the West of the town
  of Geti in Province Orientale, DRC occurring between 3 January 2010 and 04 February
  2014 as seen in satellite imagery collected by the WoldView-1 and WorldView-2 satellites
  respectively. During this period there was multiple new structures appeared in the
  area analyzed including tent shelters as well are more permanent housing. These
  increases in structures are most likely due to influxes of large numbers of IDPs
  from surrounding areas gathering in Geti. This is a preliminary analysis and has
  not yet been validated in the field. Please send ground feedback to UNITAR / UNOSAT..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-idp-settlement-in-west-geti-province-orientale-democratic-republic-june-03-2014]'
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
    description: Shelter structures in IDP settlement including tent shelters and
      permanent housing
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
    description: Internally displaced persons population in West Geti settlement
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
  description: UNOSAT analysts compared satellite imagery from WorldView-1 (January
    2010) and WorldView-2 (February 2014) to detect structural changes in West Geti
    settlement. New shelter structures and permanent housing were identified through
    visual interpretation of satellite imagery, with results mapped as vector geometries
    with confidence and validation attributes.
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
- href: https://data.humdata.org/dataset/geodata-of-idp-settlement-in-west-geti-province-orientale-democratic-republic-june-03-2014
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons from conflict/complex emergency in surrounding
      areas
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
  description: Geodata of IDP Settlement in West Geti, Province Orientale, Democratic
    Republic of Congo (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/CD/CE20131107COD/CE20131107COD_shp.zip
  format: null
  id: resource_55eb764a
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20131107COD_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of IDP Settlement in West Geti, Province Orientale, Democratic
    Republic of Congo (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/CD/CE20131107COD/CE20131107COD.gdb.zip
  format: null
  id: resource_de7cfd8c
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20131107COD.gdb.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-cod_unosat_geodataidpsettlementwestg_20140603
spatial:
  bbox: null
  centroid: null
  countries:
  - COD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2014-06-03'
temporal_resolution: null
title: Geodata of IDP Settlement in West Geti, Province Orientale, Democratic Republic
  of Congo
version: null
vulnerability: null
---
