---
attributions:
- entity:
    affiliation: null
    email: null
    name: Humanitarian Country Team Somalia
    url: https://data.humdata.org/dataset/somalia-drought-dashboard
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Somalia
  url: https://data.humdata.org/dataset/somalia-drought-dashboard
creator:
  affiliation: null
  email: null
  name: OCHA Somalia
  url: https://data.humdata.org/dataset/somalia-drought-dashboard
dataset_id: rdls_hl-som_ochasom_flooddroughtdashboard_20200630
description: 'This dataset contains the data used by the Humanitarian Country Team
  in Somalia to monitor the evolution of the drought and flood situation in Somalia.
  The data covers the following topics: Internal displacement by cause (drought related,
  conflict/insecurity, other cause) River levels in the Shabelle and Juba rivers Water
  prices by Region Cumulative annual rainfall Disease burden (acute watery diarrhea
  (AWD)/cholera, bloody diarrhea and measles) Monthly response monitoring by region
  for the following indicators: CCCM: Number of people benefiting from site improvement
  projects EDUCATION: Number of children with access to safe drinking water FOOD SECURITY:
  Number of people reached through activities geared towards improving access to food
  and safety nets HEALTH: Number of medical consultations NUTRITION: Number of acute
  malnutrition admissions PROTECTION: Number of girls and boys, women and men participating
  in community-based psycho-social activities SHELTER: Number of people in need of
  emergency assistance receiving appropriate NFIs through in-kind distribution, vouchers
  or cash WASH: Number of people reached with access to sustainable safe water services
  The sources for the data are as follows: IDP data (PRMN/UNHCR); Rainfall and Rivers
  (SWALIM); Diseases (Health Cluster/WHO); Monthly Response (Humanitarian Clusters),
  Water Prices (FAO). [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/somalia-drought-dashboard]'
details: null
exposure: []
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: es_flood_hzd
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: es_flood
    occurrence_range: null
    seasonality: null
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: es_drought_hzd
      intensity_measure: SPI:-
      process: meteorological_drought
      trigger: null
      type: drought
    id: es_drought
    occurrence_range: null
    seasonality: null
  type: flood, drought
license: CC-BY-4.0
lineage:
  description: The dataset aggregates observed hazard data (river levels, rainfall)
    and post-event impact records (displacement by cause, disease burden, water prices)
    collected by the Humanitarian Country Team in Somalia to monitor drought and flood
    evolution. Data is compiled from multiple sources through a registry methodology
    for humanitarian monitoring and response coordination.
  sources:
  - id: source_1
    license: null
    name: Humanitarian Country Team Somalia
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/somalia-drought-dashboard
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internal displacement caused by drought in Somalia
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
        metric: displaced
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Internal displacement caused by flooding in Somalia
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
        metric: displaced
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
  description: Somalia Flood and Drought Dashboard (People affected or displaced due
    to flood)
  download_url: https://data.humdata.org/dataset/b701b0bd-16b7-4d17-8723-77ac80abd4a4/resource/f11c52d0-901c-453f-8a4c-11f7071a33ee/download/20200503_people-affected-displaced-matrix.xlsx
  format: null
  id: resource_f11c52d0
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20200503_People affected-displaced matrix
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia Flood and Drought Dashboard (Hagaa Season Floods - April to
    June)
  download_url: https://data.humdata.org/dataset/b701b0bd-16b7-4d17-8723-77ac80abd4a4/resource/130faaf5-64f7-44d3-9f2a-ccb383068bed/download/people-affected-displaced-matrix-_hagaa.xlsx
  format: null
  id: resource_130faaf5
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: People affected-displaced matrix _Hagaa
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-som_ochasom_flooddroughtdashboard_20200630
spatial:
  bbox: null
  centroid: null
  countries:
  - SOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2020-06-30'
temporal_resolution: null
title: Somalia Flood and Drought Dashboard
version: null
vulnerability: null
---
