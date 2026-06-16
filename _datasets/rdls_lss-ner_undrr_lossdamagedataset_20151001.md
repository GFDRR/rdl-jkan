---
attributions:
- entity:
    affiliation: null
    email: null
    name: "Syst\xE8me d'Alerte Pr\xE9coce et de Gestion des Catastrophes (SAP)"
    url: https://data.humdata.org/dataset/disaster-loss-and-damage-dataset-for-niger
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: https://data.humdata.org/dataset/disaster-loss-and-damage-dataset-for-niger
creator:
  affiliation: null
  email: null
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: https://data.humdata.org/dataset/disaster-loss-and-damage-dataset-for-niger
dataset_id: rdls_lss-ner_undrr_lossdamagedataset_20151001
description: 'Disaster loss and damage dataset for Niger. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/disaster-loss-and-damage-dataset-for-niger]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: "Post-event disaster loss and damage data collected through the Syst\xE8\
    me d'Alerte Pr\xE9coce et de Gestion des Catastrophes (SAP) using direct observational\
    \ and anecdotal methods. Data compiled into spatial (shapefile) and tabular (spreadsheet)\
    \ formats documenting economic and structural impacts from disaster events in\
    \ Niger."
  sources:
  - id: source_1
    license: null
    name: "Syst\xE8me d'Alerte Pr\xE9coce et de Gestion des Catastrophes (SAP)"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/disaster-loss-and-damage-dataset-for-niger
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from flooding events in Niger
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
    description: Economic losses from flood disasters in Niger
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
  description: Disaster loss and damage dataset for Niger (Disaster data for Niger)
  download_url: https://data.humdata.org/dataset/60bb0852-2e19-4150-a142-34f7fc1e2fc0/resource/326e9447-51ce-4041-8f1a-dddadaa04275/download/niger.zip
  format: null
  id: resource_326e9447
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Niger.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Disaster loss and damage dataset for Niger (Disaster tabular data for
    Niger)
  download_url: https://data.humdata.org/dataset/60bb0852-2e19-4150-a142-34f7fc1e2fc0/resource/0f7c539d-baa5-403e-b049-01547f8bbd40/download/di_report-niger.xls
  format: null
  id: resource_0f7c539d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DI_Report-Niger.xls
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Disaster loss and damage dataset for Niger (Data dictionary with variable
    definitions)
  download_url: https://data.humdata.org/dataset/60bb0852-2e19-4150-a142-34f7fc1e2fc0/resource/8448d35f-74fc-45f5-aae1-7ec3c6bf1c94/download/datadictionary.docx
  format: DOCX
  id: resource_8448d35f
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
slug: rdls_lss-ner_undrr_lossdamagedataset_20151001
spatial:
  bbox: null
  centroid: null
  countries:
  - NER
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-10-01'
temporal_resolution: null
title: Disaster loss and damage dataset for Niger
version: null
vulnerability: null
---
