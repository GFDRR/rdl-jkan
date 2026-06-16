---
attributions:
- entity:
    affiliation: null
    email: null
    name: OCHA
    url: https://data.humdata.org/dataset/afghanistan-natural-disaster-incidents
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: ANDMA
    url: https://data.humdata.org/dataset/afghanistan-natural-disaster-incidents
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: IOM
    url: https://data.humdata.org/dataset/afghanistan-natural-disaster-incidents
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Red Crescent Societies
    url: https://data.humdata.org/dataset/afghanistan-natural-disaster-incidents
  id: attribution_4
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: National and international NGOs
    url: https://data.humdata.org/dataset/afghanistan-natural-disaster-incidents
  id: attribution_5
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: ERM
    url: https://data.humdata.org/dataset/afghanistan-natural-disaster-incidents
  id: attribution_6
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Afghanistan
  url: https://data.humdata.org/dataset/afghanistan-natural-disaster-incidents
creator:
  affiliation: null
  email: null
  name: OCHA Afghanistan
  url: https://data.humdata.org/dataset/afghanistan-natural-disaster-incidents
dataset_id: rdls_lss-afg_ochaafg_naturaldisasterincidents_2023
description: '1) Natural disaster events include avalanches, earthquakes, flooding,
  heavy rainfall & snowfall, and landslides & mudflows as recorded by OCHA field offices
  based on assessments in the field. 2) A natural disaster incident is defined as
  an event that has affected (i.e. impacted) people, who may or may not require humanitarian
  assistance. 3) The information includes assessment figures from OCHA, ANDMA, IOM,
  Red Crescent Societies, national NGOs, international NGOs, and ERM. 4) The number
  of affected people and houses damaged or destroyed are based on the reports received.
  These figures may change as updates are received.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/afghanistan-natural-disaster-incidents]'
details: These figures may fluctuate since the number of affected population, people
  killed and injured, and houses damaged or destroyed are based on a combination of
  verified reports and information not verified by inter-agency assessments. Hence,
  these figures may change as updates are received.
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Post-event natural disaster incident records compiled from direct field
    assessments by OCHA and humanitarian partners (ANDMA, IOM, Red Crescent, NGOs,
    ERM) across Afghanistan. Data includes counts of affected persons, injured, killed,
    and houses damaged/destroyed by incident type and administrative location, collected
    through anecdotal and observational methods from 2023-2025.
  sources:
  - id: source_1
    license: null
    name: OCHA
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: ANDMA
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: IOM
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
    name: National and international NGOs
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_6
    license: null
    name: ERM
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/afghanistan-natural-disaster-incidents
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Individuals affected by flood incidents
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
    description: Houses damaged or destroyed by flood incidents
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
    description: Individuals affected by landslide and mudflow incidents
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
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: Houses damaged or destroyed by landslide and mudflow incidents
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
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Individuals affected by earthquake incidents
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
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
    description: Houses damaged or destroyed by earthquake incidents
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
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
    description: Individuals affected by heavy rainfall and snowfall incidents
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_extreme_temperature
      intensity_measure: AirTemp:C
      process: null
      trigger: null
      type: extreme_temperature
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
  - asset_category: buildings
    asset_dimension: structure
    description: Houses damaged or destroyed by heavy rainfall and snowfall incidents
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
  description: Afghanistan - Natural Disaster Incidents (Excel)
  download_url: https://data.humdata.org/dataset/0eb7c089-7b18-442a-afeb-6380ffed95f6/resource/0eeacf3c-8a7e-4b71-ab1b-88b97ad63837/download/afghanistan-natural-disaster-incidents-from-january-to-december-2025.xlsx
  format: null
  id: resource_0eeacf3c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: afghanistan-natural-disaster-incidents-from-january-to-december-2025.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Afghanistan - Natural Disaster Incidents (CSV)
  download_url: https://data.humdata.org/dataset/0eb7c089-7b18-442a-afeb-6380ffed95f6/resource/083789cf-47a7-4b78-ac8f-d0f6833cc89b/download/afghanistan-natural-disaster-incidents-from-january-to-december-2025.csv
  format: null
  id: resource_083789cf
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: afghanistan-natural-disaster-incidents-from-january-to-december-2025.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Afghanistan - Natural Disaster Incidents (Excel)
  download_url: https://data.humdata.org/dataset/0eb7c089-7b18-442a-afeb-6380ffed95f6/resource/af8d63e2-8a60-4ad9-ad8c-ba4bcae908ba/download/afghanistan-natural-disaster-incidents-from-january-to-december-2024.xlsx
  format: null
  id: resource_af8d63e2
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: afghanistan-natural-disaster-incidents-from-january-to-december-2024.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Afghanistan - Natural Disaster Incidents (CSV)
  download_url: https://data.humdata.org/dataset/0eb7c089-7b18-442a-afeb-6380ffed95f6/resource/387b4ce9-8df1-443c-865f-9f1398485089/download/afghanistan-natural-disaster-incidents-from-january-to-december-2024.csv
  format: null
  id: resource_387b4ce9
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: afghanistan-natural-disaster-incidents-from-january-to-december-2024.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Afghanistan - Natural Disaster Incidents (Excel)
  download_url: https://data.humdata.org/dataset/0eb7c089-7b18-442a-afeb-6380ffed95f6/resource/a41a718c-79ee-40da-968d-fa06e2919f67/download/afghanistan-natural-disaster-incidents-from-january-to-november-2023.xlsx
  format: null
  id: resource_a41a718c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: afghanistan-natural-disaster-incidents-from-january-to-november-2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Afghanistan - Natural Disaster Incidents (CSV)
  download_url: https://data.humdata.org/dataset/0eb7c089-7b18-442a-afeb-6380ffed95f6/resource/3cd7b03d-6298-4796-a2a7-ab3aceff32d1/download/afghanistan-natural-disaster-incidents-from-january-to-november-2023.csv
  format: null
  id: resource_3cd7b03d
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: afghanistan-natural-disaster-incidents-from-january-to-november-2023.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-afg_ochaafg_naturaldisasterincidents_2023
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
  end: '2025-12-29'
  start: '2023-01-01'
temporal_resolution: null
title: Afghanistan - Natural Disaster Incidents
version: null
vulnerability: null
---
