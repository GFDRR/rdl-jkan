---
attributions:
- entity:
    affiliation: null
    email: null
    name: United Nations for Development Programme (UNDP)
    url: https://data.humdata.org/dataset/mauritania-damage-assessments
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA West and Central Africa (ROWCA)
  url: https://data.humdata.org/dataset/mauritania-damage-assessments
creator:
  affiliation: null
  email: null
  name: OCHA West and Central Africa (ROWCA)
  url: https://data.humdata.org/dataset/mauritania-damage-assessments
dataset_id: rdls_lss-mrt_ocharowca_floodsdamageassessments_20120711
description: 'Floods damages assessment in Mauritania This table displays floods impacts
  in Mauritania in 2010.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/mauritania-damage-assessments]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Post-event damage assessment data collected by UNDP through sample
    survey methodology in Mauritania following the 2010 floods. The dataset documents
    direct impacts on buildings and population from the flood event, compiled into
    a structured tracking tool for damage monitoring and humanitarian response planning.
  sources:
  - id: source_1
    license: null
    name: United Nations for Development Programme (UNDP)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/mauritania-damage-assessments
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from flooding in Mauritania
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
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
  - asset_category: population
    asset_dimension: population
    description: Population affected by flooding in Mauritania
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_2
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
purpose: Sample Survey
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'The dataset represents a tool for flood impacts monitoring. Source:
    UNDP'
  download_url: https://data.humdata.org/dataset/cce71e24-303c-4183-b399-1e9ff95631d6/resource/02e092de-3e74-4484-856b-50a9370c4507/download/outil_de_suivi_degats_inondations_15.08.2010.xls
  format: null
  id: resource_02e092de
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: outil_de_suivi_degats_inondations_15.08.2010.xls
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-mrt_ocharowca_floodsdamageassessments_20120711
spatial:
  bbox: null
  centroid: null
  countries:
  - MRT
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2012-07-11'
temporal_resolution: null
title: Mauritania - Floods Damage Assessments
version: null
vulnerability: null
---
