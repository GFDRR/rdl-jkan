---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/internally-displaced-persons-shelters-in-maungdaw-township-of-rakhine-state-in-myanmar-2731
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/internally-displaced-persons-shelters-in-maungdaw-township-of-rakhine-state-in-myanmar-2731
dataset_id: rdls_el-mmr_unosat_internallydisplacedperson_20171118
description: 'This map illustrates satellite-detected internally displaced persons
  shelters in the village tract of Nyaung Pin Gyi, Maungdaw Township, Rakhine State.
  Using satellite imagery collected on 6 November 2017 UNOSAT identified a total of
  457 shelters in a beach area 7 km south of Maungdaw town, next to the mouth of the
  Naf River between Myanmar and Bangladesh. Several unidentified trucks are observed
  on the road located adjacent to the internally displaced persons settlement. As
  of 11 November 2017, 307 shelters were identified which represents a 33 percent
  decrease from 6 November. Additionally, several likely rafts are observed by the
  shoreline on 11 November 2017. Additional imagery analysis indicates this settlement
  began before 6 October and grew quickly, with shelters starting to decrease after
  11 November as noted. A smaller camp is located 7 km southeast in the village tract
  of Ka Nyin Tan Alel Than Kyaw Ka Nyin Tan with approximately 200 shelters as of
  11 November 2017. This is a preliminary analysis and has not yet been validated
  in the field. Please send ground feedback to UNITAR - UNOSAT.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/internally-displaced-persons-shelters-in-maungdaw-township-of-rakhine-state-in-myanmar-2731]'
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
    description: Satellite-detected shelter structures occupied by internally displaced
      persons
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
  description: UNOSAT analysts compared satellite imagery from 6 November 2017 and
    11 November 2017 over Nyaung Pin Gyi village tract to detect and map internally
    displaced persons shelter structures, recording confidence levels and temporal
    trends in shelter presence and status.
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
- href: https://data.humdata.org/dataset/internally-displaced-persons-shelters-in-maungdaw-township-of-rakhine-state-in-myanmar-2731
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Shelter structures affected by complex emergency displacement, with
      temporal change in shelter count
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
  description: Internally Displaced Persons Shelters in Maungdaw Township of Rakhine
    State in Myanmar (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps\MM\CE20130326MMR\CE20130326MMR_IDPs_20171111.gdb.zip
  format: Geodatabase
  id: resource_ec2352f3
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: unosat-maps\MM\CE20130326MMR\CE20130326MMR_IDPs_20171111.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Internally Displaced Persons Shelters in Maungdaw Township of Rakhine
    State in Myanmar (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps\MM\CE20130326MMR\IDP_Structures_11November2017.zip
  format: null
  id: resource_b8649e44
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: unosat-maps\MM\CE20130326MMR\IDP_Structures_11November2017.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-mmr_unosat_internallydisplacedperson_20171118
spatial:
  bbox: null
  centroid: null
  countries:
  - MMR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-11-18'
temporal_resolution: null
title: Internally Displaced Persons Shelters in Maungdaw Township of Rakhine State
  in Myanmar
version: null
vulnerability: null
---
