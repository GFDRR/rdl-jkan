---
attributions:
- entity:
    affiliation: null
    email: null
    name: OCHA
    url: https://data.humdata.org/dataset/afghanistan-natural-disaster-incidents-in-2023
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: ANDMA
    url: https://data.humdata.org/dataset/afghanistan-natural-disaster-incidents-in-2023
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: IOM
    url: https://data.humdata.org/dataset/afghanistan-natural-disaster-incidents-in-2023
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Red Crescent Societies
    url: https://data.humdata.org/dataset/afghanistan-natural-disaster-incidents-in-2023
  id: attribution_4
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: National and international NGOs
    url: https://data.humdata.org/dataset/afghanistan-natural-disaster-incidents-in-2023
  id: attribution_5
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: ERM
    url: https://data.humdata.org/dataset/afghanistan-natural-disaster-incidents-in-2023
  id: attribution_6
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Afghanistan
  url: https://data.humdata.org/dataset/afghanistan-natural-disaster-incidents-in-2023
creator:
  affiliation: null
  email: null
  name: OCHA Afghanistan
  url: https://data.humdata.org/dataset/afghanistan-natural-disaster-incidents-in-2023
dataset_id: rdls_lss-afg_ochaafg_naturaldisasterincidents2_2023
description: '1) Natural disaster events include avalanches, earthquakes, flooding,
  heavy rainfall & snowfall, and landslides & mudflows as recorded by OCHA field offices
  based on assessments in the field. 2) A natural disaster incident is defined as
  an event that has affected (i.e. impacted) people, who may or may not require humanitarian
  assistance. 3) The information includes assessment figures from OCHA, ANDMA, IOM,
  Red Crescent Societies, national NGOs, international NGOs, and ERM. 4) The number
  of affected people and houses damaged or destroyed are based on the reports received.
  These figures may change as updates are received.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/afghanistan-natural-disaster-incidents-in-2023]'
details: These figures may fluctuate since the number of affected population, people
  killed and injured, and houses damaged or destroyed are based on a combination of
  verified reports and information not verified by inter-agency assessments. Hence,
  these figures may change as updates are received.
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Post-event natural disaster incident data compiled from direct field
    assessments conducted by OCHA field offices in Afghanistan, supplemented by reports
    from humanitarian partners (ANDMA, IOM, Red Crescent Societies, national and international
    NGOs, and ERM) during January-November 2023. Incident records include event type,
    date, location, and impact metrics (persons killed/injured, families and individuals
    affected, houses damaged/destroyed) based on field observations and partner reports.
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
- href: https://data.humdata.org/dataset/afghanistan-natural-disaster-incidents-in-2023
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Individuals affected by flooding incidents
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
    description: Houses damaged or destroyed by flooding
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
    description: Individuals affected by landslides and mudflows
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
    description: Houses damaged or destroyed by landslides and mudflows
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
    description: Individuals affected by earthquakes
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
    description: Houses damaged or destroyed by earthquakes
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
    description: Individuals affected by heavy snowfall and avalanches
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
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
    description: Houses damaged or destroyed by heavy snowfall and avalanches
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
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
  description: Natural disaster events include avalanches, earthquakes, flooding,
    heavy rainfall & snowfall, and landslides & mudflows as recorded by OCHA field
    offices based on assessments in the field.
  download_url: https://data.humdata.org/dataset/4a56ede0-5e94-4b24-b1fe-0c2110ead68d/resource/dd12a3c8-b9e7-4b80-9835-f982dd0a4f76/download/afghanistan-natural-disaster-incidents-from-january-to-november-2023.xlsx
  format: null
  id: resource_dd12a3c8
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
  description: Natural disaster events include avalanches, earthquakes, flooding,
    heavy rainfall & snowfall, and landslides & mudflows as recorded by OCHA field
    offices based on assessments in the field.
  download_url: https://data.humdata.org/dataset/4a56ede0-5e94-4b24-b1fe-0c2110ead68d/resource/b5c4b612-d84f-4204-974e-0dfb56f7cc56/download/afghanistan-natural-disaster-incidents-from-january-to-november-2023.csv
  format: null
  id: resource_b5c4b612
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
slug: rdls_lss-afg_ochaafg_naturaldisasterincidents2_2023
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
  end: '2023-11-22'
  start: '2023-01-01'
temporal_resolution: null
title: Afghanistan - Natural Disaster Incidents in 2023
version: null
vulnerability: null
---
