---
attributions:
- entity:
    affiliation: null
    email: null
    name: Humanitarian Partners
    url: https://data.humdata.org/dataset/2021-hazards-planning-numbers
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Sudan
  url: https://data.humdata.org/dataset/2021-hazards-planning-numbers
creator:
  affiliation: null
  email: null
  name: OCHA Sudan
  url: https://data.humdata.org/dataset/2021-hazards-planning-numbers
dataset_id: rdls_el-sdn_ochasdn_peopleriskshazards_2021
description: 'This dataset is made for planning purposes. It contains the number of
  people potentially at risk of hazards (floods, disease outbreaks and conflict) in
  Sudan.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/2021-hazards-planning-numbers]'
details: null
exposure:
- asset_type:
    description: Population potentially at risk of multiple hazards for humanitarian
      planning purposes
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Planning figures compiled from multiple humanitarian partner sources
    estimating populations potentially at risk of floods, disease outbreaks, and conflict
    in Sudan for 2021-2022 planning cycles.
  sources:
  - id: source_1
    license: null
    name: Humanitarian Partners
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/2021-hazards-planning-numbers
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: People at risk of flooding for planning purposes
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
        metric: exposure
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: People at risk of disease outbreaks for planning purposes
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_pest_infestation
      intensity_measure: Pest:count/area
      process: null
      trigger: null
      type: pest_infestation
    id: loss_2
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
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Sudan - People at risks of hazards (Excel)
  download_url: https://data.humdata.org/dataset/e3412945-5c50-4ad5-b0fd-b2420e2aa37b/resource/9ef63381-65e4-4109-ac3f-10fc15964c6d/download/2022-hazards-planning-figures.xlsx
  format: null
  id: resource_9ef63381
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2022-Hazards-planning-figures.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This dataset is made for planning purposes. It contains the 2021 number
    of people potentially at risk of hazards (floods, disease outbreaks and conflict)
    in Sudan.
  download_url: https://data.humdata.org/dataset/e3412945-5c50-4ad5-b0fd-b2420e2aa37b/resource/afd530a0-95b7-4b5f-a39a-7a9d4caddf74/download/2021-hazards-planning-figures.xlsx
  format: null
  id: resource_afd530a0
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2021 Hazards planning figures.xlsx
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-sdn_ochasdn_peopleriskshazards_2021
spatial:
  bbox: null
  centroid: null
  countries:
  - SDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2022-12-31'
  start: '2021-01-01'
temporal_resolution: null
title: Sudan - People at risks of hazards
version: null
vulnerability: null
---
