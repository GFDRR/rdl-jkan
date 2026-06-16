---
attributions:
- entity:
    affiliation: null
    email: null
    name: World Bank
    url: https://data.humdata.org/dataset/senegal-damage-assessments
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA West and Central Africa (ROWCA)
  url: https://data.humdata.org/dataset/senegal-damage-assessments
creator:
  affiliation: null
  email: null
  name: OCHA West and Central Africa (ROWCA)
  url: https://data.humdata.org/dataset/senegal-damage-assessments
dataset_id: rdls_lss-sen_ocharowca_floodsdamagesassessment_20120809
description: 'Floods damages assessment in Senegal in 2009. The Excel file represents
  floods damages in Senegal in 2009.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/senegal-damage-assessments]'
details: '**Languages:** EN'
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Post-event damage assessment conducted by the World Bank documenting
    direct building damages from the 2009 flood event in Senegal. The dataset aggregates
    damage records at the national level to quantify the impact of the flooding event.
  sources:
  - id: source_1
    license: null
    name: World Bank
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/senegal-damage-assessments
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from flooding in Senegal during 2009 flood
      event
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
  description: Senegal - Floods damages assessment (Excel)
  download_url: https://data.humdata.org/dataset/cf790ed9-8275-4dde-9375-d7582af0e2c5/resource/9e4697a8-2830-439a-8361-e661e1e3fb1c/download/sen_floods_damages_2009_wb.xls
  format: null
  id: resource_9e4697a8
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sen_floods_damages_2009_wb.xls
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-sen_ocharowca_floodsdamagesassessment_20120809
spatial:
  bbox: null
  centroid: null
  countries:
  - SEN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2012-08-09'
temporal_resolution: null
title: Senegal - Floods damages assessment
version: null
vulnerability: null
---
