---
attributions:
- entity:
    affiliation: null
    email: null
    name: National Disaster Operation Centre
    url: https://data.humdata.org/dataset/disaster-loss-and-damage-dataset-for-kenya
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: https://data.humdata.org/dataset/disaster-loss-and-damage-dataset-for-kenya
creator:
  affiliation: null
  email: null
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: https://data.humdata.org/dataset/disaster-loss-and-damage-dataset-for-kenya
dataset_id: rdls_lss-ken_undrr_lossdamagedataset_20151001
description: 'Disaster loss and damage dataset for Kenya. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/disaster-loss-and-damage-dataset-for-kenya]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Post-event disaster loss and damage data collected through direct observation
    and anecdotal reports by the National Disaster Operation Centre, compiled into
    a national geodataset with damage assessments and economic impact quantification
    for Kenya.
  sources:
  - id: source_1
    license: null
    name: National Disaster Operation Centre
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/disaster-loss-and-damage-dataset-for-kenya
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from flooding events in Kenya
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
    description: Direct economic losses from flooding events in Kenya
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
  description: Disaster loss and damage dataset for Kenya (Disaster data for Kenya)
  download_url: https://data.humdata.org/dataset/7debae59-b034-4e9a-9fb1-4f270e57435d/resource/4d984de9-cd1b-483c-a887-860c9cb7a7c8/download/kenya.zip
  format: null
  id: resource_4d984de9
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Kenya.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Disaster loss and damage dataset for Kenya (Disaster tabular data for
    Kenya)
  download_url: https://data.humdata.org/dataset/7debae59-b034-4e9a-9fb1-4f270e57435d/resource/e518eeff-0d26-4f7b-9ab8-47fdcd5865b8/download/di_report-kenya.xls
  format: null
  id: resource_e518eeff
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DI_Report-Kenya.xls
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Disaster loss and damage dataset for Kenya (Data dictionary with variable
    definitions)
  download_url: https://data.humdata.org/dataset/7debae59-b034-4e9a-9fb1-4f270e57435d/resource/4d1359dc-7782-4e1a-a40b-29c021529c39/download/datadictionary.docx
  format: DOCX
  id: resource_4d1359dc
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
slug: rdls_lss-ken_undrr_lossdamagedataset_20151001
spatial:
  bbox: null
  centroid: null
  countries:
  - KEN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-10-01'
temporal_resolution: null
title: Disaster loss and damage dataset for Kenya
version: null
vulnerability: null
---
