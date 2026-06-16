---
attributions:
- entity:
    affiliation: null
    email: null
    name: IPC (Integrated Food Security Phase Classification)
    url: https://data.humdata.org/dataset/northeast-and-northwest-nigeria-acute-malnutrition
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX
  url: https://data.humdata.org/dataset/northeast-and-northwest-nigeria-acute-malnutrition
creator:
  affiliation: null
  email: null
  name: IPC and Partners
  url: https://data.humdata.org/dataset/northeast-and-northwest-nigeria-acute-malnutrition
dataset_id: rdls_lss-nga_hdx_northeastnorthwestacutema_2023
description: 'The high-risk contributing factors to acute malnutrition in northeast
  and northwest Nigeria include very poor food consumption (quantity and quality)
  and poor health seeking behaviors. Additionally, poor health services, feeding practices,
  food insecurity and access to water, sanitation, and hygiene (WASH) services and
  facilities play a significant role. In the second projection period of January to
  April 2024, the situation is projected to worsen slightly in the northeast region.
  Conversely, a slight improvement is expected in the northwest region.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/northeast-and-northwest-nigeria-acute-malnutrition]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Acute malnutrition case estimates were extracted from the IPC Acute
    Malnutrition report for Nigeria covering January-April 2024. Data aggregates malnutrition
    classifications (Severe Acute Malnutrition, Global Acute Malnutrition, Moderate
    Acute Malnutrition) by region (northeast and northwest) and vulnerable population
    groups (children under 5, pregnant and lactating women), reflecting indirect impacts
    of food insecurity and poor health/WASH conditions.
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
- href: https://data.humdata.org/dataset/northeast-and-northwest-nigeria-acute-malnutrition
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Acute malnutrition cases in children under 5 and pregnant/lactating
      women resulting from food insecurity and poor WASH access linked to drought
      conditions
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
        type: indirect
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
  url: https://www.ipcinfo.org/fileadmin/user_upload/ipcinfo/docs/IPC_Nigeria_Acute_Malnutrition_May2023_Apr2024_Report.pdf
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Northeast and Northwest Nigeria : Acute Malnutrition (Nigeria Acute
    Malnutrition SAM GAM and MAM April 2024.xlsx)'
  download_url: https://data.humdata.org/dataset/81b9ae00-ddcc-4bf4-bc3b-d639024b7cf5/resource/39d89cf3-48a0-4984-95b8-19df68910518/download/nigeria-acute-malnutrition-sam-gam-and-mam-april-2024.xlsx
  format: null
  id: resource_39d89cf3
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Nigeria Acute Malnutrition SAM GAM and MAM April 2024.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-nga_hdx_northeastnorthwestacutema_2023
spatial:
  bbox: null
  centroid: null
  countries:
  - NGA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-04-30'
  start: '2023-05-01'
temporal_resolution: null
title: 'Northeast and Northwest Nigeria : Acute Malnutrition'
version: null
vulnerability: null
---
