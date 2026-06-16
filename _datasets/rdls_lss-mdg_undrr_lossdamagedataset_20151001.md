---
attributions:
- entity:
    affiliation: null
    email: null
    name: "Cellule de Pr\xE9vention et Gestion des Urgences - CPGU"
    url: https://data.humdata.org/dataset/disaster-loss-and-damage-dataset-for-madagascar
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: https://data.humdata.org/dataset/disaster-loss-and-damage-dataset-for-madagascar
creator:
  affiliation: null
  email: null
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: https://data.humdata.org/dataset/disaster-loss-and-damage-dataset-for-madagascar
dataset_id: rdls_lss-mdg_undrr_lossdamagedataset_20151001
description: 'Disaster loss and damage dataset for Madagascar. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/disaster-loss-and-damage-dataset-for-madagascar]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Post-event disaster loss and damage data collected directly by Madagascar's
    national disaster management authority (CPGU) through observational and anecdotal
    methods. Data compiled into a national loss database with geographic and economic
    impact metrics, structured as shapefile and tabular formats with accompanying
    data dictionary.
  sources:
  - id: source_1
    license: null
    name: "Cellule de Pr\xE9vention et Gestion des Urgences - CPGU"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/disaster-loss-and-damage-dataset-for-madagascar
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from flooding events in Madagascar
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
    description: Economic losses from flood disasters in Madagascar
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
  description: Disaster loss and damage dataset for Madagascar (Disaster data for
    Madagascar)
  download_url: https://data.humdata.org/dataset/7e62f19b-805c-44cb-8030-bd14275bd7b2/resource/0250ddbb-b0ad-4fad-a716-e7f26fbd0164/download/madagascar.zip
  format: null
  id: resource_0250ddbb
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Madagascar.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Disaster loss and damage dataset for Madagascar (Disaster tabular data
    for Madagascar)
  download_url: https://data.humdata.org/dataset/7e62f19b-805c-44cb-8030-bd14275bd7b2/resource/11f149bb-31df-42e4-b47d-0b18216e9f2d/download/di_report-madagascar.xls
  format: null
  id: resource_11f149bb
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DI_Report-Madagascar.xls
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Disaster loss and damage dataset for Madagascar (Data dictionary with
    variable definitions)
  download_url: https://data.humdata.org/dataset/7e62f19b-805c-44cb-8030-bd14275bd7b2/resource/b536a0a7-c362-48cb-97d0-f4a57c56352d/download/datadictionary.docx
  format: DOCX
  id: resource_b536a0a7
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
slug: rdls_lss-mdg_undrr_lossdamagedataset_20151001
spatial:
  bbox: null
  centroid: null
  countries:
  - MDG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-10-01'
temporal_resolution: null
title: Disaster loss and damage dataset for Madagascar
version: null
vulnerability: null
---
