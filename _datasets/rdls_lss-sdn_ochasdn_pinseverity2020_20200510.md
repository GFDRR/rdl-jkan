---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Sudan
  url: https://data.humdata.org/dataset/sudan-pin-and-severity-2020
creator:
  affiliation: null
  email: null
  name: OCHA Sudan
  url: https://data.humdata.org/dataset/sudan-pin-and-severity-2020
dataset_id: rdls_lss-sdn_ochasdn_pinseverity2020_20200510
description: 'This data set contains people in need figures for Sudan by locality
  (Admin level 2) and sector. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/sudan-pin-and-severity-2020]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: People in need figures were compiled from direct observational data
    and anecdotal reports collected through the 2020 Humanitarian Profile and Cluster
    assessment process by OCHA Sudan. Data were aggregated by sector and administrative
    locality (Admin level 2) to produce PIN estimates and severity classifications
    for humanitarian response planning.
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
- href: https://data.humdata.org/dataset/sudan-pin-and-severity-2020
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: People in need figures by sector and locality in Sudan, aggregated
      from humanitarian assessments
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
        metric: exposure
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
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This data set contains people in need figures for Sudan by locality
    (Admin level 2) and sector
  download_url: https://data.humdata.org/dataset/9d18c2ed-83b5-4bff-a70e-224afd41eef2/resource/dd079132-bc41-4ac2-b4e7-92894277d7de/download/hpc-2020-sector-pins-targets-final.xlsx
  format: null
  id: resource_dd079132
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: HPC 2020 sector PINs Targets final.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sudan: PIN and Severity 2020 (The data set contains prioritized targeted
    localities)'
  download_url: https://data.humdata.org/dataset/9d18c2ed-83b5-4bff-a70e-224afd41eef2/resource/9d0ccddf-d983-4e86-b08e-4377a794d9f8/download/hpc-2020_prioritized-targeted-localities.xlsx
  format: null
  id: resource_9d0ccddf
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: HPC 2020_Prioritized Targeted localities.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-sdn_ochasdn_pinseverity2020_20200510
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
  end: null
  start: '2020-05-10'
temporal_resolution: null
title: 'Sudan: PIN and Severity 2020'
version: null
vulnerability: null
---
