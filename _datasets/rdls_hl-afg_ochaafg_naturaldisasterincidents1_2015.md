---
attributions:
- entity:
    affiliation: null
    email: null
    name: IOM Afghanistan Humanitarian Assistance Database (HADB)
    url: https://data.humdata.org/dataset/natural-disaster-incidents-from-1-january-to-31-december-2015
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: OCHA Field Office reports
    url: https://data.humdata.org/dataset/natural-disaster-incidents-from-1-january-to-31-december-2015
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Afghanistan
  url: https://data.humdata.org/dataset/natural-disaster-incidents-from-1-january-to-31-december-2015
creator:
  affiliation: null
  email: null
  name: OCHA Afghanistan
  url: https://data.humdata.org/dataset/natural-disaster-incidents-from-1-january-to-31-december-2015
dataset_id: rdls_hl-afg_ochaafg_naturaldisasterincidents1_2015
description: '1) Natural disaster events include avalanches,earthquake, flooding,
  heavy rainfall & snowfall, and landslides & mudflows as recorded by OCHA field offices
  and IOM Afghanistan Humanitarian Assistance Database (HADB). 2) A natural disaster
  incident is defined as an event that has affected (i.e. impacted) people, who may
  or may not require humanitarian assistance. 3) HADB information is used as a main
  reference and supplemented by OCHA Field Office reports for those incidents where
  information is not available from the HADB. OCHA information includes assessment
  figures from OCHA, ANDMA, Red Crescent Societies, national NGOs, international NGOs,
  and ERM. 4) The number of affected people and houses damaged or destroyed are based
  on the reports received. These figures may change as updates are received.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/natural-disaster-incidents-from-1-january-to-31-december-2015]'
details: These figures may fluctuate since the number of affected people, people killed
  and injured, and houses damaged or destroyed are based on a combination of verified
  and non-verified reports received. Hence, these figures may change as updates are
  received.
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
  description: Post-event disaster incident records compiled from OCHA field offices
    and IOM Afghanistan HADB for calendar year 2015, documenting natural disaster
    events (avalanches, earthquakes, floods, heavy rainfall/snowfall, landslides,
    mudflows) that affected populations. HADB served as the primary reference source,
    supplemented by OCHA field assessments and ANDMA reports where HADB data were
    incomplete.
  sources:
  - id: source_1
    license: null
    name: IOM Afghanistan Humanitarian Assistance Database (HADB)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: OCHA Field Office reports
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/natural-disaster-incidents-from-1-january-to-31-december-2015
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by flooding incidents in Afghanistan during 2015
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
  - asset_category: population
    asset_dimension: population
    description: Fatalities from flooding incidents in Afghanistan during 2015
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
        metric: casualty_count
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population affected by earthquake incidents in Afghanistan during
      2015
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
  - asset_category: population
    asset_dimension: population
    description: Fatalities from earthquake incidents in Afghanistan during 2015
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
        metric: casualty_count
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population affected by landslide and mudflow incidents in Afghanistan
      during 2015
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
  - asset_category: population
    asset_dimension: population
    description: Fatalities from landslide and mudflow incidents in Afghanistan during
      2015
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
        metric: casualty_count
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
    offices and IOM Afghanistan Humanitarian Assistance Database (HADB).
  download_url: https://data.humdata.org/dataset/7aac14c2-012c-409a-a0b3-b6d74976b9a5/resource/3f660e0d-5667-4a5c-a5c8-bfb73bf9b8e9/download/afghanistan-natural-disaster-incidents-from-1-january-to-31-december-2015.xlsx
  format: null
  id: resource_3f660e0d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: afghanistan-natural-disaster-incidents-from-1-january-to-31-december-2015.xlsx
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-afg_ochaafg_naturaldisasterincidents1_2015
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
  end: '2015-12-31'
  start: '2015-01-01'
temporal_resolution: null
title: Afghanistan - Natural disaster incidents from 1 January to 31 December 2015
version: null
vulnerability: null
---
