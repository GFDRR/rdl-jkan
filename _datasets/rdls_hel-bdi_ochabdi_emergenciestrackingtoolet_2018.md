---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration
    url: https://data.humdata.org/dataset/burundi-emergencies-tracking-tool-ett
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Burundi
  url: https://data.humdata.org/dataset/burundi-emergencies-tracking-tool-ett
creator:
  affiliation: null
  email: null
  name: OCHA Burundi
  url: https://data.humdata.org/dataset/burundi-emergencies-tracking-tool-ett
dataset_id: rdls_hel-bdi_ochabdi_emergenciestrackingtoolet_2018
description: 'The dataset contains information on natural disasters, such as floods
  and heavy rains, in Burundi.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/burundi-emergencies-tracking-tool-ett]'
details: null
exposure:
- asset_type:
    description: Residential housing stock affected by flooding, classified by damage
      state (destroyed, partially destroyed, flooded)
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
    description: Critical infrastructure assets including schools, health facilities,
      bridges, roads, water systems, religious buildings, markets, and administrative
      offices
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Agricultural land and crop fields destroyed by flooding events
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_3
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: The Emergencies Tracking Tool (ETT) aggregates direct observational
    data and anecdotal reports collected by IOM field teams across Burundi documenting
    flood and heavy rainfall events. Data collection spans January 2018 to May 2023
    with incident-level records including spatial location (admin divisions), event
    date, and detailed damage assessments across residential buildings, infrastructure,
    and agricultural assets. The dataset represents post-event impact documentation
    rather than hazard modeling.
  sources:
  - id: source_1
    license: null
    name: International Organization for Migration
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/burundi-emergencies-tracking-tool-ett
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct damage to residential housing from flooding, including total
      destruction, partial destruction, and inundation
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
  - asset_category: infrastructure
    asset_dimension: structure
    description: Direct damage to critical infrastructure including schools, health
      facilities, bridges, roads, water systems, and administrative buildings
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
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: agriculture
    asset_dimension: product
    description: Direct damage to agricultural fields and crops from flooding
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
          quantity_kind: area
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
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Data about natural disasters such as floods and heavy rains in Burundi
    from January 2018 to May 2023.
  download_url: https://data.humdata.org/dataset/4749e6e5-a7ec-4954-9df5-c4625ab1c34d/resource/25331ba5-b9f6-4b7c-a272-0745585627c2/download/eet-dataset_2018_to_20_mai-2023.xlsx
  format: null
  id: resource_25331ba5
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EET dataset_Jan_2018_to_May_2023
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-bdi_ochabdi_emergenciestrackingtoolet_2018
spatial:
  bbox: null
  centroid: null
  countries:
  - BDI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-05-19'
  start: '2018-01-01'
temporal_resolution: null
title: 'Burundi: Emergencies Tracking Tool - ETT'
version: null
vulnerability: null
---
