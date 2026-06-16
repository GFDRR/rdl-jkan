---
attributions:
- entity:
    affiliation: null
    email: null
    name: Humanitarian partners
    url: https://data.humdata.org/dataset/desplazamientos-colombia
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Colombia
  url: https://data.humdata.org/dataset/desplazamientos-colombia
creator:
  affiliation: null
  email: null
  name: OCHA Colombia
  url: https://data.humdata.org/dataset/desplazamientos-colombia
dataset_id: rdls_lss-col_ochacol_desplazamientos_2008
description: 'Current and Historical Data of IDPs in Colombia. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/desplazamientos-colombia]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Registry-based compilation of internally displaced person (IDP) records
    from humanitarian partners in Colombia, covering both mass displacement events
    and individual displacement incidents from 2008-2025. Data includes demographic
    characteristics (age, gender, ethnicity), geographic origin and reception locations,
    event categorization, and temporal tracking of displacement flows.
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
- href: https://data.humdata.org/dataset/desplazamientos-colombia
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons from mass displacement events in Colombia
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
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
  - asset_category: population
    asset_dimension: population
    description: Individuals affected by displacement incidents in Colombia
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
    id: loss_2
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
purpose: Registry
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Colombia: Desplazamientos (Eventos de Desplazamiento Masivos 2025)'
  download_url: https://data.humdata.org/dataset/ccb9dfdf-b432-4d50-bd19-ac5616a0447b/resource/32ea5b37-59b2-4c83-ad21-37007ba6588e/download/desplazamientos-masivos-2025.xlsx
  format: null
  id: resource_32ea5b37
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Desplazamientos Masivos 2025.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Colombia: Desplazamientos (Hist\xF3rico de desplazamientos individuales\
    \ por lugar de ocurrencia y recepci\xF3n)"
  download_url: https://data.humdata.org/dataset/ccb9dfdf-b432-4d50-bd19-ac5616a0447b/resource/3b30a602-f361-491b-9ec2-e185a6ce88c1/download/desplazamientos-2023-2025.xlsx
  format: null
  id: resource_3b30a602
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: desplazamientos 2008-2025.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Colombia: Desplazamientos (Desplazamientos individuales por lugar
    de recepecion.xlsx)'
  download_url: https://data.humdata.org/dataset/ccb9dfdf-b432-4d50-bd19-ac5616a0447b/resource/e0683cf5-4292-4fb3-a8fa-23fc456ff0f2/download/grouped_data_recep.xlsx
  format: null
  id: resource_e0683cf5
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Desplazamientos individuales por lugar de recepecion.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Informaci\xF3n sobre desplazamientos en Colombia desde 2020 hasta\
    \ 26 de noviembre 2024"
  download_url: https://data.humdata.org/dataset/ccb9dfdf-b432-4d50-bd19-ac5616a0447b/resource/879ff3a5-cc16-4aa8-93fa-ebfe151c32b6/download/output_tables.xlsx
  format: null
  id: resource_879ff3a5
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Desplazamiento individual y masivo Colombia enero 2020 a 26 de noviembre
    2024.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-col_ochacol_desplazamientos_2008
spatial:
  bbox: null
  centroid: null
  countries:
  - COL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-12-02'
  start: '2008-01-01'
temporal_resolution: null
title: 'Colombia: Desplazamientos'
version: null
vulnerability: null
---
