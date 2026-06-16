---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNDRR DesInventar
    url: https://data.humdata.org/dataset/yemen-disaster-inventory
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX
  url: https://data.humdata.org/dataset/yemen-disaster-inventory
creator:
  affiliation: null
  email: null
  name: UNDRR
  url: https://data.humdata.org/dataset/yemen-disaster-inventory
dataset_id: rdls_el-yem_hdx_disasterinventory_1979
description: 'https://www.desinventar.net/DesInventar/profiletab.jsp?countrycode=yem.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/yemen-disaster-inventory]'
details: null
exposure:
- asset_type:
    description: Building stock affected by disasters in Yemen
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
    description: Population exposed to and affected by disasters in Yemen
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
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: DesInventar is a standardized disaster inventory system that compiles
    post-event disaster records from multiple sources including government agencies,
    humanitarian organizations, and media reports. The Yemen inventory contains observed
    disaster events with spatial, temporal, and impact data organized by hazard type
    and geographic distribution, serving as an empirical loss database for disaster
    risk assessment.
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
- href: https://data.humdata.org/dataset/yemen-disaster-inventory
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from flood events recorded in disaster inventory
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
    description: Direct building damage from strong wind/cyclone events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
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
    description: Population affected by strong wind/cyclone events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
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
  description: Yemen - Disaster Inventory (Excel)
  download_url: https://data.humdata.org/dataset/ffc25c2f-b3a8-4c5f-85c9-4e47907692ac/resource/7032dafc-713d-4969-b2f7-44b561836346/download/di_stat1129_geodist_hxl.xls
  format: null
  id: resource_7032dafc
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DI_Stat1129_GeoDist_HXL.xls
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Yemen - Disaster Inventory (Excel)
  download_url: https://data.humdata.org/dataset/ffc25c2f-b3a8-4c5f-85c9-4e47907692ac/resource/fcf52b94-72c9-4098-8500-c705eb6dabea/download/di_stat1129_hazard.xls
  format: null
  id: resource_fcf52b94
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DI_Stat1129_Hazard.xls
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Yemen - Disaster Inventory (Excel)
  download_url: https://data.humdata.org/dataset/ffc25c2f-b3a8-4c5f-85c9-4e47907692ac/resource/8b701889-9c3f-42cc-8cb4-d943a3521dc0/download/di_stat1129_temporal.xls
  format: null
  id: resource_8b701889
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DI_Stat1129_Temporal.xls
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-yem_hdx_disasterinventory_1979
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
  end: '2010-12-31'
  start: '1979-01-01'
temporal_resolution: null
title: Yemen - Disaster Inventory
version: null
vulnerability: null
---
