---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-idp-shelter-changes-in-kismayo-somalia-between-11-august-2013-05-m-march-18-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-idp-shelter-changes-in-kismayo-somalia-between-11-august-2013-05-m-march-18-2014
dataset_id: rdls_el-som_unosat_geodataidpshelterchangesk_20140318
description: 'This map illustrates IDP shelter changes within the city of Kismayo,
  Somalia occurring between 11 August 2013 and 05 March 2014 as seen in satellite
  imagery collected by the Pleiades and WorldView-1 satellites. During this period
  there was little change seen in the vast majority of the IDP sites visible in the
  city. However, about 26 new camps opened in the area and are located primarily on
  the outskirts of Kismayo. Total IDP camp area is 31.38 ha as of 5 March 2014, versus
  29.02 ha as of 11 August 2013. This is a preliminary analysis and has not yet been
  validated in the field. Please send ground feedback to UNITAR / UNOSAT.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-idp-shelter-changes-in-kismayo-somalia-between-11-august-2013-05-m-march-18-2014]'
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
    description: Internally displaced persons (IDPs) sheltering in camps within Kismayo
      city
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: UNOSAT analysts compared satellite imagery from Pleiades and WorldView-1
    sensors acquired on 11 August 2013 and 5 March 2014 to identify and map IDP shelter
    locations and quantify changes in camp area and distribution within Kismayo. The
    analysis identified 26 new camps and measured total camp area expansion from 29.02
    ha to 31.38 ha, providing spatial exposure data for the displaced population during
    the complex emergency.
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
- href: https://data.humdata.org/dataset/geodata-of-idp-shelter-changes-in-kismayo-somalia-between-11-august-2013-05-m-march-18-2014
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: IDP population displacement and shelter changes in Kismayo during
      complex emergency
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
        type: total
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
  description: Geodata of IDP shelter Changes in Kismayo, Somalia, Between 11 August
    2013 - 05 March 2014 (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SO/CE20130710SOM/CE20130710SOM_shp.zip
  format: null
  id: resource_91adc49c
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
  description: Geodata of IDP shelter Changes in Kismayo, Somalia, Between 11 August
    2013 - 05 March 2014 (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SO/CE20130710SOM/CE20130710SOM.gdb.zip
  format: null
  id: resource_6505c9ff
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
slug: rdls_el-som_unosat_geodataidpshelterchangesk_20140318
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
  start: '2014-03-18'
temporal_resolution: null
title: Geodata of IDP shelter Changes in Kismayo, Somalia, Between 11 August 2013
  - 05 March 2014
version: null
vulnerability: null
---
