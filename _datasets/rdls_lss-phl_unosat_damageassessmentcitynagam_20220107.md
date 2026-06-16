---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-city-of-naga-municipality-cebu-province-region-vii-philippines-as-of-
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-city-of-naga-municipality-cebu-province-region-vii-philippines-as-of-
dataset_id: rdls_lss-phl_unosat_damageassessmentcitynagam_20220107
description: 'UNOSAT code: TC20211216PHL This map illustrates potentially damaged
  structures and buildings in City of Naga & Minglanilla municipalities, Cebu province,
  Region VII (Central Visayas), Philippines as observed from a Pleiades image acquired
  on 21 December 2021. Within the analyzed area, UNOSAT identified 876 damaged structures
  and 1,361 potentially damaged structures. This is a preliminary analysis and has
  not yet been validated in the field. Please send ground feedback to UNITAR-UNOSAT..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-in-city-of-naga-municipality-cebu-province-region-vii-philippines-as-of-]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure: []
hazard: null
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts reviewed Pleiades satellite imagery acquired on 21
    December 2021 following Typhoon Odette and performed change detection analysis
    to identify structural damage in City of Naga and Minglanilla municipalities.
    The analysis identified 876 confirmed damaged structures and 1,361 potentially
    damaged structures through visual interpretation of satellite imagery, producing
    vector geodatabase and shapefile outputs with damage classification and building
    footprint geometry.
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
- href: https://data.humdata.org/dataset/damage-assessment-in-city-of-naga-municipality-cebu-province-region-vii-philippines-as-of-
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from tropical cyclone (Typhoon Odette) assessed
      via satellite imagery
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
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
  description: Damage assessment in City of Naga Municipality, Cebu Province, Region
    VII, Philippines as of 21 December 2021 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/PH/TC20211216PHL/TC20211216PHL_gdb.zip
  format: Geodatabase
  id: resource_37b96be9
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20211216PHL_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Damage assessment in City of Naga Municipality, Cebu Province, Region
    VII, Philippines as of 21 December 2021 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/PH/TC20211216PHL/TC20211216PHL_SHP.zip
  format: null
  id: resource_4da3c7d4
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20211216PHL_SHP.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-phl_unosat_damageassessmentcitynagam_20220107
spatial:
  bbox: null
  centroid: null
  countries:
  - PHL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-01-07'
temporal_resolution: null
title: Damage assessment in City of Naga Municipality, Cebu Province, Region VII,
  Philippines as of 21 December 2021
version: null
vulnerability: null
---
