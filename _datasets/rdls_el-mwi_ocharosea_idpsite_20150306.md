---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM)
    url: https://data.humdata.org/dataset/malawi-affected-persons-locations-0-0
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Regional Office for Southern and Eastern Africa (ROSEA)
  url: https://data.humdata.org/dataset/malawi-affected-persons-locations-0-0
creator:
  affiliation: null
  email: null
  name: OCHA Regional Office for Southern and Eastern Africa (ROSEA)
  url: https://data.humdata.org/dataset/malawi-affected-persons-locations-0-0
dataset_id: rdls_el-mwi_ocharosea_idpsite_20150306
description: 'Obtained from IOM. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/malawi-affected-persons-locations-0-0]'
details: '**Languages:** EN'
exposure:
- asset_type:
    description: Internally displaced persons enumerated at IDP sites in Malawi
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: CC-BY-4.0
lineage:
  description: IOM conducted a Displacement Tracking Matrix (DTM) survey in March
    2015 to enumerate internally displaced persons residing at IDP sites across Malawi,
    capturing population displacement as a direct loss impact from prior hazard events.
  sources:
  - id: source_1
    license: null
    name: International Organization for Migration (IOM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/malawi-affected-persons-locations-0-0
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced population from flood-related displacement
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
        metric: displaced
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
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Malawi - IDP Site (Excel)
  download_url: https://data.humdata.org/dataset/39b969c0-8e17-45c8-8d2b-6cc6e73a36fb/resource/12fe6473-65c2-4214-9e95-92022444eff1/download/02_dtm_iom_master_dataset_malawi_idp_site_round1_march_6_2015.xlsx
  format: null
  id: resource_12fe6473
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 02_DTM_IOM_Master_Dataset_Malawi_IDP_Site_Round1_March_6_2015.xlsx
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-mwi_ocharosea_idpsite_20150306
spatial:
  bbox: null
  centroid: null
  countries:
  - MWI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-03-06'
temporal_resolution: null
title: Malawi - IDP Site
version: null
vulnerability: null
---
