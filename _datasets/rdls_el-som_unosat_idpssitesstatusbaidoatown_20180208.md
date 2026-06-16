---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/idps-sites-status-in-baidoa-town
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/idps-sites-status-in-baidoa-town
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/idps-sites-status-in-baidoa-town
dataset_id: rdls_el-som_unosat_idpssitesstatusbaidoatown_20180208
description: 'This map illustrates satellite-detected areas of displaced person settlements
  in Baidoa town, the southwestern capital of Bay Region in Somalia. Using a WorldView-2
  satellite image collected on 30 December 2017, UNOSAT analyzed a total of 286 distinct
  IDP shelter sites including 81 new sites, 62 expanded sites, 49 contracted site
  and 94 unchanged sites as well as 73 closed sites. Compared to the previous analysis
  on 21 April 2017, this represents an increase of 16 sites (5.9%). This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to UNITAR - UNOSAT.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/idps-sites-status-in-baidoa-town]'
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
    description: Internally displaced persons sheltered in identified IDP settlement
      sites
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: CC-BY-4.0
lineage:
  description: WorldView-2 satellite imagery from 30 December 2017 was analyzed by
    UNOSAT to detect and classify 286 distinct IDP shelter sites in Baidoa town through
    visual interpretation and comparison with prior imagery from 21 April 2017. Site
    status was categorized as new, expanded, contracted, unchanged, or closed, providing
    a spatial inventory of displaced population settlements and their temporal dynamics.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/idps-sites-status-in-baidoa-town
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Displaced population enumerated through satellite-detected IDP shelter
      sites
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
  description: Somalia - IDPs sites status in Baidoa Town (zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SO/CE20130710SOM/CE20130710SOM_Baidoa_20171230_shp.zip
  format: null
  id: resource_d6fc9fef
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20130710SOM_Baidoa_20171230_shp.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-som_unosat_idpssitesstatusbaidoatown_20180208
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
  start: '2018-02-08'
temporal_resolution: null
title: Somalia - IDPs sites status in Baidoa Town
version: null
vulnerability: null
---
