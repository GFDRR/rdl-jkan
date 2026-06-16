---
attributions:
- entity:
    affiliation: null
    email: null
    name: IPC (Integrated Food Security Phase Classification)
    url: https://data.humdata.org/dataset/mozambique-acute-malnutrition
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX
  url: https://data.humdata.org/dataset/mozambique-acute-malnutrition
creator:
  affiliation: null
  email: null
  name: IPC and Partners
  url: https://data.humdata.org/dataset/mozambique-acute-malnutrition
dataset_id: rdls_lss-moz_hdx_acutemalnutrition_2024
description: 'This dataset gives estimates of the population of children and pregnant
  and lactating women affected by acute malnutrition. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/mozambique-acute-malnutrition]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Population estimates of acute malnutrition were extracted from the
    IPC Mozambique Acute Food Insecurity and Acute Malnutrition report (April 2024-March
    2025). The IPC methodology integrates data from multiple partners to classify
    food insecurity phases and estimate affected populations, with acute malnutrition
    identified as a direct consequence of food insecurity and drought conditions.
  sources:
  - id: source_1
    license: null
    name: IPC (Integrated Food Security Phase Classification)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/mozambique-acute-malnutrition
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population of children and pregnant/lactating women affected by acute
      malnutrition due to food insecurity
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_1
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
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://www.ipcinfo.org/fileadmin/user_upload/ipcinfo/docs/1_IPC_Mozambique_Acute_Food_Insecurity_Acute_Malnutrition_April2024_Mar2025_Report_Portuguese.pdf
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: estimates of the population of children and pregnant and lactating
    women affected by acute malnutrition (April - September 2024)
  download_url: https://data.humdata.org/dataset/3af7aa97-3195-4fc1-9dd7-afd6ce020aca/resource/8f73aea3-c08a-44dd-9a2f-2bbbf32949f3/download/mozambique-acute-malnutrition.xlsx
  format: null
  id: resource_8f73aea3
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Mozambique Acute Malnutrition.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-moz_hdx_acutemalnutrition_2024
spatial:
  bbox: null
  centroid: null
  countries:
  - MOZ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-09-30'
  start: '2024-04-01'
temporal_resolution: null
title: 'Mozambique : Acute Malnutrition'
version: null
vulnerability: null
---
