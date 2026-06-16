---
attributions:
- entity:
    affiliation: null
    email: null
    name: ANDMA (Afghanistan National Disaster Management Authority)
    url: https://data.humdata.org/dataset/afghanistan-natural-disaster-incidents-in-2018
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: IOM (International Organization for Migration)
    url: https://data.humdata.org/dataset/afghanistan-natural-disaster-incidents-in-2018
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Red Crescent Societies
    url: https://data.humdata.org/dataset/afghanistan-natural-disaster-incidents-in-2018
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: ERM (Emergency Response Mechanism)
    url: https://data.humdata.org/dataset/afghanistan-natural-disaster-incidents-in-2018
  id: attribution_4
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Afghanistan
  url: https://data.humdata.org/dataset/afghanistan-natural-disaster-incidents-in-2018
creator:
  affiliation: null
  email: null
  name: OCHA Afghanistan
  url: https://data.humdata.org/dataset/afghanistan-natural-disaster-incidents-in-2018
dataset_id: rdls_lss-afg_ochaafg_naturaldisasterincidents2_2018
description: '1) Natural disaster events include avalanches, drought, earthquakes,
  flooding, heavy rainfall & snowfall, and landslides & mudflows as recorded by OCHA
  field offices based on assessments in the field. 2) A natural disaster incident
  is defined as an event that has affected (i.e. impacted) people, who may or may
  not require humanitarian assistance. 3) The information includes assessment figures
  from OCHA, ANDMA, IOM, Red Crescent Societies, national NGOs, international NGOs,
  and ERM. 4) The number of affected people and houses damaged or destroyed are based
  on the reports received. These figures may change as updates are received.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/afghanistan-natural-disaster-incidents-in-2018]'
details: These figures may fluctuate since the number of affected population, people
  killed and injured, and houses damaged or destroyed are based on a combination of
  verified reports and information not verified by inter-agency assessments. Hence,
  these figures may change as updates are received.
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Incident-level impact data were compiled by OCHA Afghanistan from field
    assessments conducted by OCHA, ANDMA, IOM, Red Crescent Societies, national and
    international NGOs, and ERM following natural disaster events in 2018. Assessment
    methodology varied between household and rapid assessments depending on event
    type and access. The resulting dataset records affected population counts and
    housing damage figures per incident across multiple hazard types including avalanches,
    drought, earthquakes, flooding, heavy rainfall and snowfall, and landslides and
    mudflows.
  sources:
  - id: source_1
    license: null
    name: OCHA Afghanistan
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: ANDMA (Afghanistan National Disaster Management Authority)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: IOM (International Organization for Migration)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_4
    license: null
    name: Red Crescent Societies
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_5
    license: null
    name: ERM (Emergency Response Mechanism)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/afghanistan-natural-disaster-incidents-in-2018
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Number of people affected by flooding events recorded by OCHA field
      offices in Afghanistan in 2018
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
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: Number of houses damaged or destroyed by flooding events in Afghanistan
      in 2018
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
  - asset_category: population
    asset_dimension: population
    description: Number of people affected by earthquake events recorded by OCHA field
      offices in Afghanistan in 2018
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
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: Number of houses damaged or destroyed by earthquake events in Afghanistan
      in 2018
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
  - asset_category: population
    asset_dimension: population
    description: Number of people affected by landslide and mudflow events recorded
      by OCHA field offices in Afghanistan in 2018
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
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: Number of houses damaged or destroyed by landslide and mudflow events
      in Afghanistan in 2018
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
  - asset_category: population
    asset_dimension: population
    description: Number of people affected by drought events recorded by OCHA field
      offices in Afghanistan in 2018
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_7
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
  - asset_category: population
    asset_dimension: population
    description: Number of people affected by heavy snowfall events recorded by OCHA
      field offices in Afghanistan in 2018
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_extreme_temperature
      intensity_measure: AirTemp:C
      process: null
      trigger: null
      type: extreme_temperature
    id: loss_8
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
  - asset_category: population
    asset_dimension: population
    description: Number of people affected by avalanche events recorded by OCHA field
      offices in Afghanistan in 2018
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_9
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
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Natural disaster events include avalanches, earthquakes, flooding,
    heavy rainfall & snowfall, and landslides & mudflows as recorded by OCHA field
    offices based on assessments in the field.
  download_url: https://data.humdata.org/dataset/001d5cac-9f29-4ad0-af6b-9b359ac12bd9/resource/c1aa0994-3ef0-4d7b-9701-8ec0b50231a7/download/afghanistan-natural-disaster-incidents-from-january-to-december-2018.xlsx
  format: null
  id: resource_c1aa0994
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: afghanistan-natural-disaster-incidents-from-january-to-december-2018.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Natural disaster events include avalanches, earthquakes, flooding,
    heavy rainfall & snowfall, and landslides & mudflows as recorded by OCHA field
    offices based on assessments in the field.
  download_url: https://data.humdata.org/dataset/001d5cac-9f29-4ad0-af6b-9b359ac12bd9/resource/d8072936-ab2b-49df-9452-4f883e089244/download/afghanistan-natural-disaster-incidents-from-january-to-december-2018.csv
  format: null
  id: resource_d8072936
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: afghanistan-natural-disaster-incidents-from-january-to-december-2018.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-afg_ochaafg_naturaldisasterincidents2_2018
spatial:
  bbox: null
  centroid: null
  countries:
  - AFG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2018-12-31'
  start: '2018-01-01'
temporal_resolution: null
title: Afghanistan - Natural Disaster Incidents in 2018
version: null
vulnerability: null
---
