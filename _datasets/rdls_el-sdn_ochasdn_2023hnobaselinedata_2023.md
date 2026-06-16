---
attributions:
- entity:
    affiliation: null
    email: null
    name: Humanitarian partners
    url: https://data.humdata.org/dataset/sudan-2023-hno-baseline-data
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Sudan
  url: https://data.humdata.org/dataset/sudan-2023-hno-baseline-data
creator:
  affiliation: null
  email: null
  name: OCHA Sudan
  url: https://data.humdata.org/dataset/sudan-2023-hno-baseline-data
dataset_id: rdls_el-sdn_ochasdn_2023hnobaselinedata_2023
description: 'Dataset contains Sudan baseline data -population,IDPs,Refugees,GAM,IPC-
  and the overall number of people in need(PIN ) and by sector down to admin 2 level..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/sudan-2023-hno-baseline-data]'
details: null
exposure:
- asset_type:
    description: Baseline population including IDPs, refugees, and returnees at admin
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
license: CC-BY-4.0
lineage:
  description: Baseline data aggregated from humanitarian partners' field assessments
    and administrative records at admin 2 level, integrating population counts, IDP/refugee
    figures, Global Acute Malnutrition (GAM) prevalence, and Integrated Food Security
    Phase Classification (IPC) assessments to estimate sectoral people in need (PIN)
    for the 2023 Humanitarian Needs Overview.
  sources:
  - id: source_1
    license: null
    name: Humanitarian partners
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/sudan-2023-hno-baseline-data
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Food insecurity and malnutrition impacts measured via IPC classification
      and GAM prevalence
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
    description: Internally displaced persons and refugees as humanitarian consequences
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
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://reliefweb.int/report/sudan/sudan-humanitarian-needs-overview-2023-november-2022
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Dataset contains Sudan baseline data -population, IDPs, Refugees, GAM,
    IPC- and the overall number of people in need (PIN ) and PIN by sector. All data
    is disaggregated down to admin 2 level.
  download_url: https://data.humdata.org/dataset/74569091-7cce-4f18-8ae7-f187945fef24/resource/bc8b7b00-8a64-4b3d-97dc-8c0470f0cc03/download/sdn-2023-hno.xlsx
  format: null
  id: resource_bc8b7b00
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SDN 2023 HNO.xlsx
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-sdn_ochasdn_2023hnobaselinedata_2023
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
  end: '2023-12-31'
  start: '2023-01-01'
temporal_resolution: null
title: 'Sudan: 2023 HNO Baseline Data'
version: null
vulnerability: null
---
