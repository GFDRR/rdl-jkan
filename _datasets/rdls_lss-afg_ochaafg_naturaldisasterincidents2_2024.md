---
attributions:
- entity:
    affiliation: null
    email: null
    name: OCHA
    url: https://data.humdata.org/dataset/afghanistan-natural-disaster-incidents-in-2024
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: ANDMA
    url: https://data.humdata.org/dataset/afghanistan-natural-disaster-incidents-in-2024
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: IOM
    url: https://data.humdata.org/dataset/afghanistan-natural-disaster-incidents-in-2024
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Red Crescent Societies
    url: https://data.humdata.org/dataset/afghanistan-natural-disaster-incidents-in-2024
  id: attribution_4
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: ERM
    url: https://data.humdata.org/dataset/afghanistan-natural-disaster-incidents-in-2024
  id: attribution_5
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Afghanistan
  url: https://data.humdata.org/dataset/afghanistan-natural-disaster-incidents-in-2024
creator:
  affiliation: null
  email: null
  name: OCHA Afghanistan
  url: https://data.humdata.org/dataset/afghanistan-natural-disaster-incidents-in-2024
dataset_id: rdls_lss-afg_ochaafg_naturaldisasterincidents2_2024
description: '1) Natural disaster events include avalanches, earthquakes, flooding,
  heavy rainfall & snowfall, and landslides & mudflows as recorded by OCHA field offices
  based on assessments in the field. 2) A natural disaster incident is defined as
  an event that has affected (i.e. impacted) people, who may or may not require humanitarian
  assistance. 3) The information includes assessment figures from OCHA, ANDMA, IOM,
  Red Crescent Societies, national NGOs, international NGOs, and ERM. 4) The number
  of affected people and houses damaged or destroyed are based on the reports received.
  These figures may change as updates are received.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/afghanistan-natural-disaster-incidents-in-2024]'
details: These figures may fluctuate since the number of affected population, people
  killed and injured, and houses damaged or destroyed are based on a combination of
  verified reports and information not verified by inter-agency assessments. Hence,
  these figures may change as updates are received.
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Post-event natural disaster incident data compiled from direct field
    assessments conducted by OCHA, ANDMA, IOM, Red Crescent Societies, national and
    international NGOs, and ERM across Afghanistan during 2024. Incident records include
    event type, date, location (region, province, district), and impact metrics (casualties,
    injuries, affected families/individuals, damaged/destroyed houses) aggregated
    from multiple humanitarian partner reports.
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
    name: ERM
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/afghanistan-natural-disaster-incidents-in-2024
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from flooding events
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
    description: Population affected by flooding
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
    description: Direct building damage from landslides and mudflows
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
    description: Population affected by landslides and mudflows
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
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from earthquakes
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
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population affected by earthquakes
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
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from heavy rainfall and snowfall
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
    id: loss_7
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
    description: Population affected by heavy rainfall and snowfall
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
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
  description: Afghanistan - Natural Disaster Incidents in 2024 (Excel)
  download_url: https://data.humdata.org/dataset/3b4368e1-a9b9-4add-8701-6b167f6a30bd/resource/86d3d1d1-f551-4d9b-80c7-b927ffe7ff38/download/afghanistan-natural-disaster-incidents-from-january-to-december-2024.xlsx
  format: null
  id: resource_86d3d1d1
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
  description: Afghanistan - Natural Disaster Incidents in 2024 (CSV)
  download_url: https://data.humdata.org/dataset/3b4368e1-a9b9-4add-8701-6b167f6a30bd/resource/5c665a73-76ef-4de9-ba1f-aeff0f677c8d/download/afghanistan-natural-disaster-incidents-from-january-to-december-2024.csv
  format: null
  id: resource_5c665a73
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: afghanistan-natural-disaster-incidents-from-january-to-december-2024.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-afg_ochaafg_naturaldisasterincidents2_2024
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
  end: '2024-12-09'
  start: '2024-01-01'
temporal_resolution: null
title: Afghanistan - Natural Disaster Incidents in 2024
version: null
vulnerability: null
---
