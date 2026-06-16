---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNDRR DesInventar
    url: https://data.humdata.org/dataset/state-of-palestine-disaster-inventory
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX
  url: https://data.humdata.org/dataset/state-of-palestine-disaster-inventory
creator:
  affiliation: null
  email: null
  name: UNDRR
  url: https://data.humdata.org/dataset/state-of-palestine-disaster-inventory
dataset_id: rdls_lss-pse_hdx_statedisasterinventory_1980
description: 'https://www.desinventar.net/DesInventar/profiletab.jsp?countrycode=pse.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/state-of-palestine-disaster-inventory]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: The State of Palestine Disaster Inventory is compiled from DesInventar,
    a UNDRR-maintained database that systematically records historical disaster events
    and their impacts. Data is collected from multiple sources including government
    reports, media, and humanitarian assessments, then standardized and georeferenced.
    The inventory captures multi-hazard events with associated damage and loss metrics
    organized by geographic distribution, hazard type, and temporal occurrence.
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
- href: https://data.humdata.org/dataset/state-of-palestine-disaster-inventory
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Building damage from flood events in Palestine disaster inventory
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
    description: Population affected by flood events in Palestine disaster inventory
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
    description: Building damage from strong wind events in Palestine disaster inventory
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
    description: Population affected by strong wind events in Palestine disaster inventory
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
  description: State of Palestine - Disaster Inventory (Excel)
  download_url: https://data.humdata.org/dataset/ecedc13f-cc10-41d3-82f9-a7881efaf970/resource/2baae404-fd46-4c74-9d92-0fa8231d0cb7/download/di_stat1132_geodist.xls
  format: null
  id: resource_2baae404
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DI_Stat1132_GeoDist.xls
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: State of Palestine - Disaster Inventory (Excel)
  download_url: https://data.humdata.org/dataset/ecedc13f-cc10-41d3-82f9-a7881efaf970/resource/e787fa30-2f49-4c57-893f-f2e9911b02df/download/di_stat1132_hazard.xls
  format: null
  id: resource_e787fa30
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DI_Stat1132_Hazard.xls
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: State of Palestine - Disaster Inventory (Excel)
  download_url: https://data.humdata.org/dataset/ecedc13f-cc10-41d3-82f9-a7881efaf970/resource/573ea9af-6fba-432e-8ae1-e8d7dfe94a54/download/di_stat1132_temporal.xls
  format: null
  id: resource_573ea9af
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DI_Stat1132_Temporal.xls
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-pse_hdx_statedisasterinventory_1980
spatial:
  bbox: null
  centroid: null
  countries:
  - PSE
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2013-12-31'
  start: '1980-01-01'
temporal_resolution: null
title: State of Palestine - Disaster Inventory
version: null
vulnerability: null
---
