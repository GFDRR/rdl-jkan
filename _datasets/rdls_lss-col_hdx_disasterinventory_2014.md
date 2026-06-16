---
attributions:
- entity:
    affiliation: null
    email: null
    name: DesInventar
    url: https://data.humdata.org/dataset/colombia-disaster-inventory
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX
  url: https://data.humdata.org/dataset/colombia-disaster-inventory
creator:
  affiliation: null
  email: null
  name: UNDRR
  url: https://data.humdata.org/dataset/colombia-disaster-inventory
dataset_id: rdls_lss-col_hdx_disasterinventory_2014
description: 'https://www.desinventar.net/DesInventar/profiletab.jsp?countrycode=col.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/colombia-disaster-inventory]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: The Colombia Disaster Inventory aggregates post-event impact data from
    DesInventar, a UNDRR-maintained system that systematically collects and standardizes
    disaster damage assessments across multiple hazard types. Data includes recorded
    casualties, displaced persons, damaged buildings, and economic losses from historical
    disaster events, organized temporally and by hazard type.
  sources:
  - id: source_1
    license: null
    name: DesInventar
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/colombia-disaster-inventory
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from flood events
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
    description: Direct building damage from strong wind events
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
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from earthquake events
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
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from landslide events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
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
  description: Colombia - Disaster Inventory (Excel)
  download_url: https://data.humdata.org/dataset/702f3a52-ad26-4c78-bd5e-4c5956bab6ed/resource/3915e394-8ab9-42e1-93c9-a7975333c778/download/di_stat1017_hxl.xlsx
  format: null
  id: resource_3915e394
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DI_Stat1017_HXL.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Colombia - Disaster Inventory (Excel)
  download_url: https://data.humdata.org/dataset/702f3a52-ad26-4c78-bd5e-4c5956bab6ed/resource/c95ee245-dad8-415c-87ef-ec18d951409b/download/di_stat1019_temporal.xlsx
  format: null
  id: resource_c95ee245
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DI_Stat1019_Temporal.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Colombia - Disaster Inventory (Excel)
  download_url: https://data.humdata.org/dataset/702f3a52-ad26-4c78-bd5e-4c5956bab6ed/resource/cae12b9b-56fc-4554-b5bf-f628de93f2a6/download/di_stat1020_hazard.xlsx
  format: null
  id: resource_cae12b9b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DI_Stat1020_Hazard.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-col_hdx_disasterinventory_2014
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
  end: '2018-12-31'
  start: '2014-01-01'
temporal_resolution: null
title: Colombia - Disaster Inventory
version: null
vulnerability: null
---
