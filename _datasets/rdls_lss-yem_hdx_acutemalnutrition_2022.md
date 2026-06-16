---
attributions:
- entity:
    affiliation: null
    email: null
    name: IPC (Integrated Food Security Phase Classification)
    url: https://data.humdata.org/dataset/yemen-acute-malnutrition
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX
  url: https://data.humdata.org/dataset/yemen-acute-malnutrition
creator:
  affiliation: null
  email: null
  name: IPC
  url: https://data.humdata.org/dataset/yemen-acute-malnutrition
dataset_id: rdls_lss-yem_hdx_acutemalnutrition_2022
description: 'This dataset shows the IPC AMN analysis. The IPC Acute Malnutrition
  (IPC AMN) classification was introduced in Yemen in 2020. However, due to limited
  data availability, the initial analysis relied on Mid-Upper Arm Circumference (MUAC)
  screening data and historical information. Overall, the trend shows a deterioration
  in the nutrition situation in the GoY areas, reflecting the worsening economy, rising
  food prices, long-term effects of conflict, chronic displacement, and limited access
  to basic services and infrastructure. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/yemen-acute-malnutrition]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: IPC AMN classification data extracted from the November 2023 to October
    2024 Yemen analysis report. The dataset aggregates MUAC screening data and historical
    information across governorates and districts to classify acute malnutrition cases
    by severity (SAM, MAM, GAM) in children under 5 and pregnant/breastfeeding women,
    reflecting nutrition impacts from conflict, economic deterioration, and limited
    service access.
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
- href: https://data.humdata.org/dataset/yemen-acute-malnutrition
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Acute malnutrition cases in children under 5 and pregnant/breastfeeding
      women classified by IPC AMN severity levels (SAM, MAM, GAM)
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
  url: https://www.ipcinfo.org/fileadmin/user_upload/ipcinfo/docs/IPC_Yemen_Acute_Food_Malnutrition_Nov2023_Oct2024_Report.pdf
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Total number of children and women affected by acute malnutrition and
    in need of treatment (Malnutrition burden) Nov2023_Oct2024. . Notably, the most
    recent IPC analysis recorded IPC AMN Phase 5 in three districts-two in Southern
    Hodeidah and one in Taiz Lowland-during the current period from November 2023
    to June 2024. Additionally, the district count in IPC AMN Phase 5 increased to
    four, with another district from Taiz Lowland added during the projection period
  download_url: https://data.humdata.org/dataset/a9c198fb-28d7-41ac-8855-c09bef9f2659/resource/0564914a-8295-438d-9cba-a596c1ca3ac4/download/ipc_yemen_acute_food_malnutrition_nov2023_oct2024.xlsx
  format: null
  id: resource_0564914a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: IPC_Yemen_Acute_Food_Malnutrition
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Total number of children and women affected by acute malnutrition and
    in need of treatment (Malnutrition burden) Oct 2022 - May 2023
  download_url: https://data.humdata.org/dataset/a9c198fb-28d7-41ac-8855-c09bef9f2659/resource/9233a57e-94d2-4b6e-ad0b-5ea36c5e06f4/download/current-acute-malnutrition-situation-oct-2022-may-2023.xlsx
  format: null
  id: resource_9233a57e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Current Acute Malnutrition Situation.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-yem_hdx_acutemalnutrition_2022
spatial:
  bbox: null
  centroid: null
  countries:
  - YEM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-10-31'
  start: '2022-10-01'
temporal_resolution: null
title: 'Yemen: Acute Malnutrition'
version: null
vulnerability: null
---
