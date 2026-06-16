---
attributions:
- entity:
    affiliation: null
    email: null
    name: Direction de la Protection Civile - DPC
    url: https://data.humdata.org/dataset/disaster-loss-and-damage-dataset-for-senegal
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: https://data.humdata.org/dataset/disaster-loss-and-damage-dataset-for-senegal
creator:
  affiliation: null
  email: null
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: https://data.humdata.org/dataset/disaster-loss-and-damage-dataset-for-senegal
dataset_id: rdls_lss-sen_undrr_lossdamagedataset_20151001
description: 'Disaster loss and damage dataset for Senegal. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/disaster-loss-and-damage-dataset-for-senegal]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Post-event disaster loss and damage data collected by Senegal's Direction
    de la Protection Civile through direct observation and anecdotal reporting, compiled
    and standardized by UNDRR into a national loss dataset with geographic and economic
    impact metrics.
  sources:
  - id: source_1
    license: null
    name: "Direction de la Protection Civile \xE2\u20AC\u201C DPC"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/disaster-loss-and-damage-dataset-for-senegal
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from flooding events in Senegal
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
    description: Direct economic losses from flooding events in Senegal
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
  description: Disaster loss and damage dataset for Senegal (Disaster data for Senegal)
  download_url: https://data.humdata.org/dataset/34f077f2-7270-45db-8f95-da5e4bfd5c9a/resource/33a8ca9d-9c6a-429b-9e13-daf4588e4689/download/senegal.zip
  format: null
  id: resource_33a8ca9d
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Senegal.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Disaster loss and damage dataset for Senegal (Disaster tabular data
    for Senegal)
  download_url: https://data.humdata.org/dataset/34f077f2-7270-45db-8f95-da5e4bfd5c9a/resource/7afd0d14-1561-4bd8-9d62-729fc2e6f6bf/download/di_report-senegal.xls
  format: null
  id: resource_7afd0d14
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DI_Report-Senegal.xls
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Disaster loss and damage dataset for Senegal (Data dictionary with
    variable definitions)
  download_url: https://data.humdata.org/dataset/34f077f2-7270-45db-8f95-da5e4bfd5c9a/resource/d0424625-1d7c-4423-b266-6c345eb6c067/download/datadictionary.docx
  format: DOCX
  id: resource_d0424625
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
slug: rdls_lss-sen_undrr_lossdamagedataset_20151001
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
  start: '2015-10-01'
temporal_resolution: null
title: Disaster loss and damage dataset for Senegal
version: null
vulnerability: null
---
