---
attributions:
- entity:
    affiliation: null
    email: null
    name: Digital Globe
    url: https://data.humdata.org/dataset/damage-assessment-in-san-andres-cholula-and-san-pedro-cholula-state-of-puebla-mexico-2717
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: IGG-UNAM
    url: https://data.humdata.org/dataset/damage-assessment-in-san-andres-cholula-and-san-pedro-cholula-state-of-puebla-mexico-2717
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-san-andres-cholula-and-san-pedro-cholula-state-of-puebla-mexico-2717
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-san-andres-cholula-and-san-pedro-cholula-state-of-puebla-mexico-2717
dataset_id: rdls_lss-mex_unosat_damageassessmentsanandres_20171106
description: "This map illustrates damaged structures detected with different media\
  \ support (newspapers, government reports, web news) and Digital Globe images captured\
  \ on September 20 (from the web site https://www.digitalglobe.com/opendata/mexico-city-earthquake/post-event)\
  \ in San Andr\xE9s Cholula and San Pedro Cholula located in Puebla State, Mexico.\
  \ The analyzed area is located at 60 km of the epicentral zone of the 19 September\
  \ 2017 M7.1 earthquake. IGG-UNAM identified 39 damaged structures. Please send ground\
  \ feedback to UNITAR-UNOSAT.. [Source: This metadata record was automatically extracted\
  \ from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-in-san-andres-cholula-and-san-pedro-cholula-state-of-puebla-mexico-2717]"
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: Post-event damage assessment conducted by UNOSAT analysts through multi-temporal
    satellite imagery comparison (pre- and post-earthquake) from Digital Globe, corroborated
    with media reports and government sources. IGG-UNAM provided ground validation
    identifying 39 damaged structures in the study municipalities located 60 km from
    the earthquake epicenter.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Digital Globe
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: IGG-UNAM
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/damage-assessment-in-san-andres-cholula-and-san-pedro-cholula-state-of-puebla-mexico-2717
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from the 19 September 2017 M7.1
      earthquake in Puebla State
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
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
  description: "Damage Assessment in San Andr\xE9s Cholula and San Pedro Cholula,\
    \ State of Puebla, Mexico (Zipped geodatabase)"
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MX/EQ20170919MEX/EQ20170919MEX_gdb.zip
  format: Geodatabase
  id: resource_c7d64372
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20170919MEX_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Damage Assessment in San Andr\xE9s Cholula and San Pedro Cholula,\
    \ State of Puebla, Mexico (Zipped shapefile)"
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MX/EQ20170919MEX/EQ20170919MEX_shp.zip
  format: null
  id: resource_4d2de7f0
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20170919MEX_shp.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-mex_unosat_damageassessmentsanandres_20171106
spatial:
  bbox: null
  centroid: null
  countries:
  - MEX
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-11-06'
temporal_resolution: null
title: "Damage Assessment in San Andr\xE9s Cholula and San Pedro Cholula, State of\
  \ Puebla, Mexico"
version: null
vulnerability: null
---
