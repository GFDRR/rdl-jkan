---
attributions:
- entity:
    affiliation: null
    email: null
    name: ACAPS INFORM Severity Index
    url: https://data.humdata.org/dataset/hdx-signals
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: ACLED Conflict Data
    url: https://data.humdata.org/dataset/hdx-signals
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: IDMC Displacement Data
    url: https://data.humdata.org/dataset/hdx-signals
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: IPC Food Insecurity Classifications
    url: https://data.humdata.org/dataset/hdx-signals
  id: attribution_4
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: JRC Agricultural Hotspots
    url: https://data.humdata.org/dataset/hdx-signals
  id: attribution_5
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WFP Market Monitor
    url: https://data.humdata.org/dataset/hdx-signals
  id: attribution_6
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WHO Cholera Data
    url: https://data.humdata.org/dataset/hdx-signals
  id: attribution_7
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX
  url: https://data.humdata.org/dataset/hdx-signals
creator:
  affiliation: null
  email: null
  name: Multiple Partners
  url: https://data.humdata.org/dataset/hdx-signals
dataset_id: rdls_lss-hdx_signals_1998
description: 'HDX Signals monitors key datasets and generates automated emails when
  significant, negative changes are detected. Receive signals direct in your inbox
  by signing up on the home page . Explore historical signals and access all email
  content in the resources below.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/hdx-signals]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: HDX Signals is an automated monitoring system that ingests multiple
    humanitarian and disaster-related datasets (ACLED, IDMC, IPC, JRC, WFP, WHO, ACAPS
    INFORM) and applies statistical anomaly detection algorithms to identify significant
    negative changes in key indicators. The system generates alert signals when changes
    exceed defined thresholds, aggregating multi-source impact data at location and
    temporal scales to support early warning and situational awareness.
  sources:
  - id: source_1
    license: null
    name: ACAPS INFORM Severity Index
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: ACLED Conflict Data
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: IDMC Displacement Data
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_4
    license: null
    name: IPC Food Insecurity Classifications
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_5
    license: null
    name: JRC Agricultural Hotspots
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_6
    license: null
    name: WFP Market Monitor
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_7
    license: null
    name: WHO Cholera Data
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/hdx-signals
  rel: source
loss:
  losses:
  - asset_category: agriculture
    asset_dimension: product
    description: Agricultural hotspots and drought impacts detected through JRC agricultural
      monitoring
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
          quantity_kind: area
          unit: null
        metric: exposure
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: economic_indicator
    asset_dimension: index
    description: Food insecurity classifications from IPC assessments triggered by
      drought conditions
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
          quantity_kind: currency
          unit: null
        metric: exposure
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Displacement counts from conflict and disaster-related events tracked
      by IDMC
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_3
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
  - asset_category: economic_indicator
    asset_dimension: index
    description: Market price monitoring and food security impacts from WFP market
      monitor
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_4
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
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
purpose: Read details of the methodology [here]((see referenced_by)).
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://eur02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fgithub.com%2FOCHA-DAP%2Fhdx-signals&data=05%7C02%7Cisabelle.tot%40un.org%7Cef19ac36eb2446def80508dc7a4cb394%7C0f9e35db544f4f60bdcc5ea416e6dc70%7C0%7C0%7C638519717049790832%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C0%7C%7C%7C&sdata=aNvklZHs3U2rkoSmTPwq4eZk%2BSg%2Bj4%2FmWq25eXoytEA%3D&reserved=0
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Location-level metadata file with location name, regional classifications,
    and up-to-date coverage indicating whether it is included in each of the datasets
    monitored in HDX Signals.
  download_url: https://data.humdata.org/dataset/464950af-0d57-47ae-a1fa-b4413b0adaf7/resource/400acc9c-e58e-4461-b003-c0602a910c3f/download/hdx_signals_location_metadata.csv
  format: null
  id: resource_400acc9c
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hdx_signals_location_metadata.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: File of historical signals, containing all email content, from all
    text in the email, key figures, and hyperlinks to images, original sources, and
    individual emails.
  download_url: https://data.humdata.org/dataset/464950af-0d57-47ae-a1fa-b4413b0adaf7/resource/49056751-af41-430e-92e8-81c4b0e5b38f/download/hdx_signals.csv
  format: null
  id: resource_49056751
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hdx_signals.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: HDX Signals (Data dictionary explaining the columns in the historical
    signals alerts file.)
  download_url: https://data.humdata.org/dataset/464950af-0d57-47ae-a1fa-b4413b0adaf7/resource/fec6b8ba-1629-455b-b151-7436b83a84e8/download/hdx_signals_data_dictionary.csv
  format: null
  id: resource_fec6b8ba
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hdx_signals_data_dictionary.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-hdx_signals_1998
spatial:
  bbox: null
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-22'
  start: '1998-05-15'
temporal_resolution: null
title: HDX Signals
version: null
vulnerability: null
---
