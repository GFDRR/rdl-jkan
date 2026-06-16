---
attributions:
- entity:
    affiliation: null
    email: null
    name: Food Security Information Network (FSIN)
    url: https://data.humdata.org/dataset/igad-regional-focus-of-the-2024-global-report-on-food-crises
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Intergovernmental Authority on Development (IGAD)
    url: https://data.humdata.org/dataset/igad-regional-focus-of-the-2024-global-report-on-food-crises
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Food Security Information Network
  url: https://data.humdata.org/dataset/igad-regional-focus-of-the-2024-global-report-on-food-crises
creator:
  affiliation: null
  email: null
  name: Food Security Information Network
  url: https://data.humdata.org/dataset/igad-regional-focus-of-the-2024-global-report-on-food-crises
dataset_id: rdls_lss-fsin_igadregionalfocus2024glob_2016
description: 'The IGAD Regional Focus of the 2024 Global Report on Food Crises is
  the result of a collaboration between the Food Security Information Network (FSIN)
  and the Intergovernmental Authority on Development (IGAD), a regional economic community
  that forms one of the building blocks of the African Union. It provides a comprehensive
  assessment of acute food insecurity and malnutrition in the eight IGAD countries
  as well as trends over time, key drivers and populations of highest concern based
  on a rigorous methodology. It also presents available data and information on forcibly
  displaced populations and includes a spotlight on the conflict in Sudan and a focus
  on pastoralism, deep-diving into important issues for the region.. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/igad-regional-focus-of-the-2024-global-report-on-food-crises]'
details: https://www.fsinplatform.org/igad-regional-focus-GRFC2024
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: The dataset aggregates acute food insecurity and malnutrition data
    from eight IGAD countries using the standardized Integrated Food Security Phase
    Classification (IPC) methodology. Population figures are classified into IPC phases
    (1-5) based on rigorous analysis of food security indicators, with primary drivers
    and trends documented. The regional focus integrates data from multiple national
    sources coordinated through FSIN and IGAD to provide comprehensive assessment
    of food crisis impacts.
  sources:
  - id: source_1
    license: null
    name: Food Security Information Network (FSIN)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Intergovernmental Authority on Development (IGAD)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/igad-regional-focus-of-the-2024-global-report-on-food-crises
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population in acute food insecurity phases (3-5) due to drought and
      food crises
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
purpose: Registry
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: IGAD Regional Focus of the 2024 Global Report on Food Crises (Data
    from the IGAD Regional Focus of the 2024 Global Report on Food Crises.)
  download_url: https://data.humdata.org/dataset/c24dc6db-1155-49da-bfbd-228f2f6c2d8d/resource/a58a4fc6-ce62-4a7d-9df8-fce458dc1fc7/download/igad-data.xlsx
  format: null
  id: resource_a58a4fc6
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: IGAD regional report data.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-fsin_igadregionalfocus2024glob_2016
spatial:
  bbox: null
  centroid: null
  countries:
  - DJI
  - ERI
  - ETH
  - KEN
  - SOM
  - SSD
  - UGA
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-12-31'
  start: '2016-01-01'
temporal_resolution: null
title: IGAD Regional Focus of the 2024 Global Report on Food Crises
version: null
vulnerability: null
---
