---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-idp-shelter-changes-in-hargeisa-somalia-between-20-august-2012-and-december-17-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-idp-shelter-changes-in-hargeisa-somalia-between-20-august-2012-and-december-17-2014
dataset_id: rdls_el-som_unosat_geodataidpshelterchangesh_20141217
description: 'This map illustrates areas of IDP settlement changes within the area
  of Hargeisa, Somalia, occurring between 20 August 2012 and 02 November 2014, as
  seen by the Pleiades and GeoEye-1 satellites. UNOSAT analysis revealed one new IDP
  settlement and one expanded IDP settlement by 02 November 2014. However, 4 other
  settlement areas contracted and 2 settlement areas did not change. As of 02 November
  2014, the IDP settlements occupy a total area of 71.06 ha, which represents an increase
  of 3.96 ha since 20 August 2012. A total of 7,108 IDP structures were detected as
  of 02 November 2014.This is a preliminary analysis and has not yet been validated
  in the field. Please send ground feedback to UNITAR / UNOSAT.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/geodata-of-idp-shelter-changes-in-hargeisa-somalia-between-20-august-2012-and-december-17-2014]'
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
      by construction type and temporal change status
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
  description: UNOSAT analysts compared Pleiades and GeoEye-1 satellite imagery from
    20 August 2012 and 02 November 2014 to detect IDP shelter structures and quantify
    settlement changes (new, expanded, contracted, unchanged) in Hargeisa. Shelter
    locations and attributes were digitized and validated to produce a geodatabase
    of 7,108 structures occupying 71.06 ha as of November 2014.
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
- href: https://data.humdata.org/dataset/geodata-of-idp-shelter-changes-in-hargeisa-somalia-between-20-august-2012-and-december-17-2014
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: IDP shelter settlement changes and displacement patterns in response
      to complex emergency
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
  description: Geodata of IDP Shelter changes in Hargeisa, Somalia between 20 August
    2012 and 02 November 2014 (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SO/CE20130710SOM/CE20130710SOM_shp.zip
  format: null
  id: resource_04bce2ed
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
  description: Geodata of IDP Shelter changes in Hargeisa, Somalia between 20 August
    2012 and 02 November 2014 (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SO/CE20130710SOM/CE20130710SOM.gdb.zip
  format: null
  id: resource_caacfc37
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
slug: rdls_el-som_unosat_geodataidpshelterchangesh_20141217
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
  start: '2014-12-17'
temporal_resolution: null
title: Geodata of IDP Shelter changes in Hargeisa, Somalia between 20 August 2012
  and 02 November 2014
version: null
vulnerability: null
---
