---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-idp-settlement-in-boga-province-orientale-democratic-republic-of-c-june-03-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-idp-settlement-in-boga-province-orientale-democratic-republic-of-c-june-03-2014
dataset_id: rdls_el-cod_unosat_geodataidpsettlementbogap_20140603
description: 'This map illustrates structural changes within the town of Boga in Province
  Orientale, DRC occurring between 19 April 2011 and 04 February 2014 as seen in satellite
  imagery collected by the WoldView-1 and WorldView-2 satellites respectively. During
  this period there was multiple new structures appeared in the area analyzed including
  tent shelters as well are more permanent housing. These increases in structures
  are most likely due to influxes of large numbers of IDPs from surrounding areas
  gathering in Boga. This is a preliminary analysis and has not yet been validated
  in the field. Please send ground feedback to UNITAR / UNOSAT.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/geodata-of-idp-settlement-in-boga-province-orientale-democratic-republic-of-c-june-03-2014]'
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
    description: Internally displaced persons population in Boga settlement
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
  description: UNOSAT analysts compared multi-temporal satellite imagery (WorldView-1
    and WorldView-2) of Boga town between April 2011 and February 2014 to detect new
    structures (tent shelters and permanent housing) as proxy indicators of IDP influx
    from surrounding conflict-affected areas. Structural changes were mapped and attributed
    with settlement characteristics including camp status, shelter type, and trend
    information.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/geodata-of-idp-settlement-in-boga-province-orientale-democratic-republic-of-c-june-03-2014
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Shelter structures occupied by IDPs displaced from conflict in surrounding
      areas
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons from complex emergency/conflict gathering
      in Boga settlement
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
    id: loss_2
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
  description: Geodata of IDP Settlement in Boga, Province Orientale, Democratic Republic
    of Congo (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/CD/CE20131107COD/CE20131107COD_shp.zip
  format: null
  id: resource_eb8e1833
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
  description: Geodata of IDP Settlement in Boga, Province Orientale, Democratic Republic
    of Congo (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/CD/CE20131107COD/CE20131107COD.gdb.zip
  format: null
  id: resource_43f8abf0
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
slug: rdls_el-cod_unosat_geodataidpsettlementbogap_20140603
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
title: Geodata of IDP Settlement in Boga, Province Orientale, Democratic Republic
  of Congo
version: null
vulnerability: null
---
