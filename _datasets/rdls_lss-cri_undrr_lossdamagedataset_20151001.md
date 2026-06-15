---
attributions:
- entity:
    affiliation: null
    email: null
    name: La Red - FLACSO
    url: https://data.humdata.org/dataset/disaster-loss-and-damage-dataset-for-costa-rica
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: https://data.humdata.org/dataset/disaster-loss-and-damage-dataset-for-costa-rica
creator:
  affiliation: null
  email: null
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: https://data.humdata.org/dataset/disaster-loss-and-damage-dataset-for-costa-rica
dataset_id: rdls_lss-cri_undrr_lossdamagedataset_20151001
description: 'Disaster loss and damage data for Colombia at several levels of disaggregation.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/disaster-loss-and-damage-dataset-for-costa-rica]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: "Disaster loss and damage data compiled from direct observational records\
    \ and anecdotal reports by La Red\u2013FLACSO, disaggregated across multiple administrative\
    \ and sectoral levels in Costa Rica. The dataset captures post-event impacts including\
    \ building damage and economic losses from various hazard events, organized in\
    \ spatial (shapefile) and tabular (spreadsheet) formats with accompanying data\
    \ dictionary documentation."
  sources:
  - id: source_1
    license: null
    name: "La Red \u2013 FLACSO"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/disaster-loss-and-damage-dataset-for-costa-rica
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from flooding events
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
    description: Direct economic losses from flooding
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
  description: Disaster loss and damage dataset for Costa Rica (Disaster data for
    Costa Rica)
  download_url: https://data.humdata.org/dataset/84aa5ccd-46eb-4bde-b39a-f9cb1a159fc3/resource/293b09b9-84bb-44e2-a674-6a2d6d219100/download/costarica.zip
  format: null
  id: resource_293b09b9
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CostaRica.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Disaster loss and damage dataset for Costa Rica (Disaster tabular data
    for Costa Rica)
  download_url: https://data.humdata.org/dataset/84aa5ccd-46eb-4bde-b39a-f9cb1a159fc3/resource/d574ac1d-d41e-436a-b108-905d6de744e0/download/di_report-costarica.xls
  format: null
  id: resource_d574ac1d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DI_Report-CostaRica.xls
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Disaster loss and damage dataset for Costa Rica (ata dictionary with
    variable definitions)
  download_url: https://data.humdata.org/dataset/84aa5ccd-46eb-4bde-b39a-f9cb1a159fc3/resource/3c91f517-d739-4bf7-bf42-b90e1fa0ac03/download/datadictionary.docx
  format: DOCX
  id: resource_3c91f517
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
slug: rdls_lss-cri_undrr_lossdamagedataset_20151001
spatial:
  bbox: null
  centroid: null
  countries:
  - CRI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-10-01'
temporal_resolution: null
title: Disaster loss and damage dataset for Costa Rica
version: null
vulnerability: null
---
