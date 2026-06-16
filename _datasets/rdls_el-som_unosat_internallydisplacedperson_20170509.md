---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/internally-displaced-persons-shelters-in-baidoa-town
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/internally-displaced-persons-shelters-in-baidoa-town
dataset_id: rdls_el-som_unosat_internallydisplacedperson_20170509
description: 'This map illustrates satellite-detected areas of displaced person settlements
  in Baidoa town, the southwestern capital of Bay region in Somalia. Using a Worlview-2
  satellite image collected on 21 April 2017, UNOSAT analyzed the town of Baidoa and
  its outskirts areas and identified 272 locations where displaced person shelters
  are visible. A total of approximately 33,467 shelter structures are estimated to
  be within the ~149 hectares of settlement area. This represent an increase of 143%
  in shelter structures compared with the last UNOSAT analysis performed using imagery
  collected on 22 January 2017, where a total of 13,766 shelters, inside 144 locations,
  within 96 hectares of settlement area were detected. Note that also 1,288 additional
  shelters were detected in the previous analysis but were not detected in the current
  one as they are obscured by clouds in the image from 21 April 2017. This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to UNITAR-UNOSAT.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/internally-displaced-persons-shelters-in-baidoa-town]'
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
    description: Shelter structures in displaced person settlements identified through
      satellite imagery analysis
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts processed Worldview-2 satellite imagery from 21 April
    2017 and compared it with imagery from 22 January 2017 to identify shelter structures
    in IDP settlements. Shelter locations were manually delineated and counted, with
    approximately 33,467 structures mapped across ~149 hectares in Baidoa town, representing
    a 143% increase from the previous survey period.
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
- href: https://data.humdata.org/dataset/internally-displaced-persons-shelters-in-baidoa-town
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons sheltering in Baidoa town due to complex
      emergency
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
  description: Somalia - Internally Displaced Persons Shelters in Baidoa Town (Zipped
    geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SO/CE20130710SOM/UNOSAT_Baidoa_21APRIL2017.gdb.zip
  format: Geodatabase
  id: resource_9cba12d7
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_Baidoa_21APRIL2017.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia - Internally Displaced Persons Shelters in Baidoa Town (Zipped
    shapefile.)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SO/CE20130710SOM/UNOSAT_Baidoa_21APRIL2017_shp.zip
  format: null
  id: resource_638fcc94
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_Baidoa_21APRIL2017_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia - Internally Displaced Persons Shelters in Baidoa Town (Zipped
    geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SO/CE20130710SOM/UNOSAT_REACH_Baidoa_22JAN2017.gdb.zip
  format: Geodatabase
  id: resource_e220eb1f
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_REACH_Baidoa_22JAN2017.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia - Internally Displaced Persons Shelters in Baidoa Town (Zipped
    shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SO/CE20130710SOM/UNOSAT_REACH_Baidoa_22JAN2017_shp.zip
  format: null
  id: resource_95cf1f0c
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_REACH_Baidoa_22JAN2017_shp.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-som_unosat_internallydisplacedperson_20170509
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
  start: '2017-05-09'
temporal_resolution: null
title: Somalia - Internally Displaced Persons Shelters in Baidoa Town
version: null
vulnerability: null
---
