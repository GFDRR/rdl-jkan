---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-idp-shelter-changes-in-baidoa-somalia-between-21-august-2013-and-0-march-18-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-idp-shelter-changes-in-baidoa-somalia-between-21-august-2013-and-0-march-18-2014
dataset_id: rdls_el-som_unosat_geodataidpshelterchangesb_20140318
description: 'This map illustrates area of IDP shelter changes within the area of
  Baidoa, Somalia occurring between 21 August 2013 and 8 February 2014 as seen in
  satellite imagery collected by the Pleiades satellite. There were significant increases
  in the IDP areas during this time due to the 20 IDP sites that appeared and the
  14 IDP sites that were expanded during the analysis period. The 78 IDP areas occupy
  an area of approximately 38.76 ha, which represent an increase of 0.48 ha since
  the previous analysis. This is a preliminary analysis and has not yet been validated
  in the field. Please send ground feedback to UNITAR / UNOSAT.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/geodata-of-idp-shelter-changes-in-baidoa-somalia-between-21-august-2013-and-0-march-18-2014]'
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
    description: Internally displaced persons (IDPs) sheltering in camps across Baidoa
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
  description: UNOSAT analysts compared Pleiades satellite imagery from 21 August
    2013 and 08 February 2014 to detect changes in IDP shelter locations and areal
    extent in Baidoa. Shelter polygons were digitized and classified by site status
    (new, expanded, closed) and structural characteristics (shelter type, roofing
    material). The resulting geodataset documents 78 IDP sites occupying 38.76 hectares
    with a net increase of 0.48 hectares over the analysis period.
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
- href: https://data.humdata.org/dataset/geodata-of-idp-shelter-changes-in-baidoa-somalia-between-21-august-2013-and-0-march-18-2014
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: IDP population displacement and shelter expansion due to drought-driven
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
  description: Geodata of IDP Shelter Changes in Baidoa, Somalia, Between 21 August
    2013 and 08 February 2014 (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SO/CE20130710SOM/CE20130710SOM_shp.zip
  format: null
  id: resource_df7ce479
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
  description: Geodata of IDP Shelter Changes in Baidoa, Somalia, Between 21 August
    2013 and 08 February 2014 (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SO/CE20130710SOM/CE20130710SOM.gdb.zip
  format: null
  id: resource_20237944
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
slug: rdls_el-som_unosat_geodataidpshelterchangesb_20140318
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
title: Geodata of IDP Shelter Changes in Baidoa, Somalia, Between 21 August 2013 and
  08 February 2014
version: null
vulnerability: null
---
