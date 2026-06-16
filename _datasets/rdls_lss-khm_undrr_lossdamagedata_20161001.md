---
attributions:
- entity:
    affiliation: null
    email: null
    name: La Red
    url: https://data.humdata.org/dataset/disaster-loss-and-damage-data-for-cambodia
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: OSSO
    url: https://data.humdata.org/dataset/disaster-loss-and-damage-data-for-cambodia
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: DNPAD
    url: https://data.humdata.org/dataset/disaster-loss-and-damage-data-for-cambodia
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: PREDECAN
    url: https://data.humdata.org/dataset/disaster-loss-and-damage-data-for-cambodia
  id: attribution_4
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: https://data.humdata.org/dataset/disaster-loss-and-damage-data-for-cambodia
creator:
  affiliation: null
  email: null
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: https://data.humdata.org/dataset/disaster-loss-and-damage-data-for-cambodia
dataset_id: rdls_lss-khm_undrr_lossdamagedata_20161001
description: 'Disaster loss and damage data for Cambodia at several levels of disaggregation.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/disaster-loss-and-damage-data-for-cambodia]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Disaster loss and damage data compiled from direct observational records
    and anecdotal reports collected by La Red, OSSO, DNPAD, and PREDECAN. Data aggregated
    at multiple administrative levels across Cambodia with spatial representation
    in shapefile format and tabular impact metrics in spreadsheet format.
  sources:
  - id: source_1
    license: null
    name: La Red
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: OSSO
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: DNPAD
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_4
    license: null
    name: PREDECAN
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/disaster-loss-and-damage-data-for-cambodia
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from flooding events in Cambodia
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
    description: Direct economic losses from flooding events in Cambodia
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
  description: Disaster loss and damage data for Cambodia (Disaster data for Cambodia)
  download_url: https://data.humdata.org/dataset/0fccd714-7418-4ce5-9632-bbe125681738/resource/bbb63796-5079-45af-b461-6f8b085b91a9/download/camdodia.zip
  format: null
  id: resource_bbb63796
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Camdodia.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Disaster loss and damage data for Cambodia (Disaster Tabular data for
    Cambodia)
  download_url: https://data.humdata.org/dataset/0fccd714-7418-4ce5-9632-bbe125681738/resource/484f981d-278f-4bf0-8581-1fc38d70232a/download/di_report-cambodia.xls
  format: null
  id: resource_484f981d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DI_Report-Cambodia.xls
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Disaster loss and damage data for Cambodia (Data dictionary with variable
    definitions)
  download_url: https://data.humdata.org/dataset/0fccd714-7418-4ce5-9632-bbe125681738/resource/acb47d23-aa60-4b35-8e56-e4a45c7236cb/download/datadictionary.docx
  format: DOCX
  id: resource_acb47d23
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
slug: rdls_lss-khm_undrr_lossdamagedata_20161001
spatial:
  bbox: null
  centroid: null
  countries:
  - KHM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-10-01'
temporal_resolution: null
title: Disaster loss and damage data for Cambodia
version: null
vulnerability: null
---
