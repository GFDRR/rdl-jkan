---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNDRR DesInventar
    url: https://data.humdata.org/dataset/indonesia-disaster-inventory
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX
  url: https://data.humdata.org/dataset/indonesia-disaster-inventory
creator:
  affiliation: null
  email: null
  name: UNDRR
  url: https://data.humdata.org/dataset/indonesia-disaster-inventory
dataset_id: rdls_el-idn_hdx_disasterinventory_1815
description: 'https://www.desinventar.net/DesInventar/profiletab.jsp?countrycode=idn.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/indonesia-disaster-inventory]'
details: null
exposure:
- asset_type:
    description: Building stock affected by disaster events
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Population exposed to and affected by disaster events
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_2
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Infrastructure assets impacted by disasters
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_3
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: The Indonesia Disaster Inventory is compiled from DesInventar, UNDRR's
    standardized disaster impact database system. Post-event damage and loss data
    are collected from multiple sources and systematically recorded with geographic,
    temporal, and hazard-type classifications. The dataset aggregates observed impacts
    across multiple hazard types (flood, earthquake, landslide, strong wind, etc.)
    with spatial distribution and temporal trends.
  sources:
  - id: source_1
    license: null
    name: UNDRR DesInventar
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/indonesia-disaster-inventory
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Building damage from flood events
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
  - asset_category: population
    asset_dimension: population
    description: Population affected by flood events
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
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: Building damage from earthquake events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_3
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
  - asset_category: population
    asset_dimension: population
    description: Population affected by earthquake events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_4
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
  - asset_category: buildings
    asset_dimension: structure
    description: Building damage from strong wind events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_5
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
    description: Building damage from landslide events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_6
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
  url: https://www.desinventar.net/methodology.html
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Indonesia - Disaster Inventory (Excel)
  download_url: https://data.humdata.org/dataset/a63ce98d-7f6a-4249-9162-043be89090ce/resource/c2d8ad7a-6a5c-4a3e-be83-fb72fa9d0dda/download/di_stat1114_geodist_hxl.xls
  format: null
  id: resource_c2d8ad7a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DI_Stat1114_GeoDist_HXL.xls
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Indonesia - Disaster Inventory (Excel)
  download_url: https://data.humdata.org/dataset/a63ce98d-7f6a-4249-9162-043be89090ce/resource/0ea35cb3-9cbb-4fd8-a4b4-1debf18967fc/download/di_stat1114_hazard.xls
  format: null
  id: resource_0ea35cb3
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DI_Stat1114_Hazard.xls
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Indonesia - Disaster Inventory (Excel)
  download_url: https://data.humdata.org/dataset/a63ce98d-7f6a-4249-9162-043be89090ce/resource/30982afb-b8d1-4fd0-89e9-d79f0cadd0e1/download/di_stat1114_temporal.xls
  format: null
  id: resource_30982afb
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DI_Stat1114_Temporal.xls
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-idn_hdx_disasterinventory_1815
spatial:
  bbox: null
  centroid: null
  countries:
  - IDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2018-12-31'
  start: '1815-01-01'
temporal_resolution: null
title: Indonesia - Disaster Inventory
version: null
vulnerability: null
---
