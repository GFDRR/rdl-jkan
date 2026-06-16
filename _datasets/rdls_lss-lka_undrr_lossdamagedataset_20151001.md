---
attributions:
- entity:
    affiliation: null
    email: null
    name: Disaster Management Centre (DMC) of the Ministry of Disaster Management
    url: https://data.humdata.org/dataset/disaster-loss-and-damage-dataset-for-sri-lanka
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: https://data.humdata.org/dataset/disaster-loss-and-damage-dataset-for-sri-lanka
creator:
  affiliation: null
  email: null
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: https://data.humdata.org/dataset/disaster-loss-and-damage-dataset-for-sri-lanka
dataset_id: rdls_lss-lka_undrr_lossdamagedataset_20151001
description: 'Disaster loss and damage dataset for Sri Lanka. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/disaster-loss-and-damage-dataset-for-sri-lanka]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Post-event disaster loss and damage data collected directly by the
    Disaster Management Centre of Sri Lanka's Ministry of Disaster Management through
    observational and anecdotal reporting mechanisms, compiled into a national geodatabase
    with economic and structural impact assessments.
  sources:
  - id: source_1
    license: null
    name: Disaster Management Centre (DMC) of the Ministry of Disaster Management
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/disaster-loss-and-damage-dataset-for-sri-lanka
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from flooding events in Sri Lanka
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
  - asset_category: economic_indicator
    asset_dimension: index
    description: Direct economic losses from flooding events in Sri Lanka
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
          quantity_kind: currency
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
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Disaster loss and damage dataset for Sri Lanka (Disaster data for Sri
    Lanka)
  download_url: https://data.humdata.org/dataset/08c9ca36-8b95-4361-abf1-ce21bfc49184/resource/49adba32-509f-49e7-b63e-928ef743c52e/download/srilanka.zip
  format: null
  id: resource_49adba32
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SriLanka.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Disaster loss and damage dataset for Sri Lanka (Disaster tabular data
    for Sri Lanka)
  download_url: https://data.humdata.org/dataset/08c9ca36-8b95-4361-abf1-ce21bfc49184/resource/4cb4bd14-e5ba-4443-af23-948bfb05f479/download/di_report-srilanka.xls
  format: null
  id: resource_4cb4bd14
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DI_report-SriLanka.xls
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Disaster loss and damage dataset for Sri Lanka (Data dictionary with
    variable definitions)
  download_url: https://data.humdata.org/dataset/08c9ca36-8b95-4361-abf1-ce21bfc49184/resource/12751158-ba60-4a70-be04-9a409351e27e/download/datadictionary.docx
  format: DOCX
  id: resource_12751158
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DataDictionary.docx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-lka_undrr_lossdamagedataset_20151001
spatial:
  bbox: null
  centroid: null
  countries:
  - LKA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-10-01'
temporal_resolution: null
title: Disaster loss and damage dataset for Sri Lanka
version: null
vulnerability: null
---
