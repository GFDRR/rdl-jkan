---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Sudan
  url: https://data.humdata.org/dataset/2021_hno-baseline_data
creator:
  affiliation: null
  email: null
  name: OCHA Sudan
  url: https://data.humdata.org/dataset/2021_hno-baseline_data
dataset_id: rdls_el-sdn_ochasdn_2021hnobaselinedata_2021
description: 'Dataset contains Sudan baseline data -population,IDPs,Refugees,GAM,IPC-
  and the overall number of people in need(PIN ) and by sector down to admin 2 level..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/2021_hno-baseline_data]'
details: null
exposure:
- asset_type:
    description: Total population including IDPs, refugees, and returnees at admin
      2 level
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Baseline data compiled from sample surveys across Sudan at admin 2
    level, integrating population counts, displacement figures (IDPs and refugees),
    food security classifications (IPC), and nutritional status (GAM) to establish
    humanitarian needs assessment baseline for 2021.
  sources:
  - id: source_1
    license: null
    name: OCHA Sudan
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/2021_hno-baseline_data
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Food insecurity classification (IPC) and Global Acute Malnutrition
      (GAM) prevalence among affected population
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
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons (IDPs) and refugees as displacement
      outcomes
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Sample Survey
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Dataset contains Sudan baseline data -population,IDPs,Refugees,GAM,IPC-
    and the overall number of people in need(PIN ) and by sector down to admin 2 level.
  download_url: https://data.humdata.org/dataset/92134b91-578b-4f0e-90ef-9d63170e9ead/resource/57501c43-83a4-4e7c-b69f-b034f65b9cd2/download/sudan_hno-2021_baseline-data.xlsx
  format: null
  id: resource_57501c43
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SUDAN_HNO 2021_Baseline Data.xlsx
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-sdn_ochasdn_2021hnobaselinedata_2021
spatial:
  bbox: null
  centroid: null
  countries:
  - SDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2021-12-31'
  start: '2021-01-01'
temporal_resolution: null
title: 'Sudan: 2021 HNO Baseline Data'
version: null
vulnerability: null
---
