---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNDRR DesInventar
    url: https://data.humdata.org/dataset/venezuela-disaster-inventory
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX
  url: https://data.humdata.org/dataset/venezuela-disaster-inventory
creator:
  affiliation: null
  email: null
  name: UNDRR
  url: https://data.humdata.org/dataset/venezuela-disaster-inventory
dataset_id: rdls_lss-ven_hdx_disasterinventory_20151231
description: 'https://www.desinventar.net/DesInventar/profiletab.jsp?countrycode=ven.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/venezuela-disaster-inventory]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: DesInventar is a disaster inventory system that compiles observed disaster
    event records from multiple sources including government agencies, media reports,
    and field assessments. The Venezuela dataset aggregates historical disaster events
    with associated hazard types, geographic distribution, temporal patterns, and
    impact metrics (damage, affected population, casualties). Data is organized by
    hazard type, geographic location, and temporal occurrence to support disaster
    risk assessment and historical analysis.
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
- href: https://data.humdata.org/dataset/venezuela-disaster-inventory
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
    description: Direct building damage from landslide events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
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
    description: Population affected by landslide events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
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
  description: Venezuela - Disaster Inventory (Excel)
  download_url: https://data.humdata.org/dataset/4b09fe42-d91b-4343-97da-5f17fc58b09e/resource/4b1a074a-02fb-45c1-9bc7-2af001420628/download/di_stat1127_geodist_hxl.xls
  format: null
  id: resource_4b1a074a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DI_Stat1127_GeoDist_HXL.xls
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Venezuela - Disaster Inventory (Excel)
  download_url: https://data.humdata.org/dataset/4b09fe42-d91b-4343-97da-5f17fc58b09e/resource/be9caf38-cacb-4585-85c8-cd7ca35aa1ad/download/di_stat1127_hazard.xls
  format: null
  id: resource_be9caf38
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DI_Stat1127_Hazard.xls
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Venezuela - Disaster Inventory (Excel)
  download_url: https://data.humdata.org/dataset/4b09fe42-d91b-4343-97da-5f17fc58b09e/resource/89ead809-4f79-402e-8ce6-5745d99679ad/download/di_stat1127_temporal.xls
  format: null
  id: resource_89ead809
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DI_Stat1127_Temporal.xls
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ven_hdx_disasterinventory_20151231
spatial:
  bbox: null
  centroid: null
  countries:
  - VEN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-12-31'
temporal_resolution: null
title: Venezuela - Disaster Inventory
version: null
vulnerability: null
---
