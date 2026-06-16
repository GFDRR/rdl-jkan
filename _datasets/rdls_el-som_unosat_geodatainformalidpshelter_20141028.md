---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-informal-idp-shelters-in-border-town-of-doolow-somalia-october-28-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-informal-idp-shelters-in-border-town-of-doolow-somalia-october-28-2014
dataset_id: rdls_el-som_unosat_geodatainformalidpshelter_20141028
description: 'This map illustrates IDP shelter changes near Doolow, Somalia as visible
  in satellite imagery acquired 15 September 2014. As of 15 September 2014, within
  Qansalay IDP settlement south west of Doolow, 904 shelters and 11 administrative
  buildings were detected and within Kabasa IDP settlement east of the city, 1,457
  shelters and 20 administrative buildings were located and marked. Settlement conditions
  have changed greatly since previous analysis. As 3 March 2013, 99% of the shelters
  were improvised structures (buuls). As 15 September 2014, overall the number of
  detected shelters decreased but more importantly converted from improvised shelters
  into temporary housing or semi-permanent structures. This is a preliminary analysis
  and has not yet been validated in the field. Please send ground feedback to UNITAR
  / UNOSAT.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-informal-idp-shelters-in-border-town-of-doolow-somalia-october-28-2014]'
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
    description: Informal IDP shelter structures (buuls and administrative buildings)
      detected via satellite imagery
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
  description: UNOSAT analysts reviewed and compared satellite imagery acquired on
    15 September 2014 against baseline imagery from 3 March 2013 to detect changes
    in IDP settlement extent and shelter inventory. Shelter locations and administrative
    buildings were manually delineated and attributed with structural type, roof material,
    and settlement status to document displacement-driven shelter proliferation in
    Doolow border town.
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
- href: https://data.humdata.org/dataset/geodata-of-informal-idp-shelters-in-border-town-of-doolow-somalia-october-28-2014
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: IDP shelter inventory changes in response to drought-driven displacement
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
        metric: exposure
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
  description: Geodata of Informal IDP shelters in border town of Doolow, Somalia
    (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SO/CE20130710SOM/CE20130710SOM_shp.zip
  format: null
  id: resource_48759243
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20130710SOM_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Informal IDP shelters in border town of Doolow, Somalia
    (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SO/CE20130710SOM/CE20130710SOM.gdb.zip
  format: null
  id: resource_7280b102
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20130710SOM.gdb.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-som_unosat_geodatainformalidpshelter_20141028
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
  start: '2014-10-28'
temporal_resolution: null
title: Geodata of Informal IDP shelters in border town of Doolow, Somalia
version: null
vulnerability: null
---
