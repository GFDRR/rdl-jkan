---
attributions:
- entity:
    affiliation: null
    email: null
    name: General Directorate of Civil Emergencies
    url: https://data.humdata.org/dataset/disaster-loss-and-damage-data-for-albania
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: https://data.humdata.org/dataset/disaster-loss-and-damage-data-for-albania
creator:
  affiliation: null
  email: null
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: https://data.humdata.org/dataset/disaster-loss-and-damage-data-for-albania
dataset_id: rdls_lss-alb_undrr_lossdamagedataset_20151001
description: 'Disaster loss and damage data for Albania at several levels of disaggregation.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/disaster-loss-and-damage-data-for-albania]'
details: 'More information can be found here: http://www.mbrojtjacivile.al/'
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Disaster loss and damage data collected through direct observational
    methods and anecdotal reporting by Albania's General Directorate of Civil Emergencies,
    compiled at multiple administrative levels for national disaster risk assessment.
  sources:
  - id: source_1
    license: null
    name: General Directorate of Civil Emergencies
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/disaster-loss-and-damage-data-for-albania
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Economic losses and damage from multiple disaster types in Albania
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
  - asset_category: buildings
    asset_dimension: structure
    description: Building damage records from seismic events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_2
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
  - asset_category: agriculture
    asset_dimension: product
    description: Agricultural losses from drought events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_3
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
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
  description: Disaster loss and damage dataset for Albania (Disaster data for Albania)
  download_url: https://data.humdata.org/dataset/01c902dd-fec3-499b-a6c0-d092c18bc73e/resource/6850c4bf-cceb-4975-8716-8a5108ad82c3/download/albania.zip
  format: null
  id: resource_6850c4bf
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Albania.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Disaster loss and damage dataset for Albania (Disaster Tabular data
    for Albania)
  download_url: https://data.humdata.org/dataset/01c902dd-fec3-499b-a6c0-d092c18bc73e/resource/0d9d729f-658c-4e7d-bbf7-f2558e8a9715/download/di_report-albania.xls
  format: null
  id: resource_0d9d729f
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DI_Report-Albania.xls
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Disaster loss and damage dataset for Albania (Data dictionary with
    variable definitions)
  download_url: https://data.humdata.org/dataset/01c902dd-fec3-499b-a6c0-d092c18bc73e/resource/36fd1618-d45a-488a-8b86-58c682314b04/download/datadictionary.docx
  format: DOCX
  id: resource_36fd1618
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
slug: rdls_lss-alb_undrr_lossdamagedataset_20151001
spatial:
  bbox: null
  centroid: null
  countries:
  - ALB
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-10-01'
temporal_resolution: null
title: Disaster loss and damage dataset for Albania
version: null
vulnerability: null
---
