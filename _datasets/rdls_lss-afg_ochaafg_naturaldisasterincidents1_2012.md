---
attributions:
- entity:
    affiliation: null
    email: null
    name: OCHA Field Offices
    url: https://data.humdata.org/dataset/natural-disaster-incidents-from-1-january-to-31-december-2012
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: HADB (Humanitarian Affairs Database)
    url: https://data.humdata.org/dataset/natural-disaster-incidents-from-1-january-to-31-december-2012
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: ANDMA and Red Crescent
    url: https://data.humdata.org/dataset/natural-disaster-incidents-from-1-january-to-31-december-2012
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Afghanistan
  url: https://data.humdata.org/dataset/natural-disaster-incidents-from-1-january-to-31-december-2012
creator:
  affiliation: null
  email: null
  name: OCHA Afghanistan
  url: https://data.humdata.org/dataset/natural-disaster-incidents-from-1-january-to-31-december-2012
dataset_id: rdls_lss-afg_ochaafg_naturaldisasterincidents1_2012
description: '1) Natural disaster events include avalanches, extreme winter conditions,
  flooding, heavy rainfall, landslides & mudflows, and extreme weather (sandstorms,
  hail, wind, etc) as recorded by OCHA field offices. 2) A natural disaster incident
  is defined as an event that has affected (i.e. impacted) Afghans, who may or may
  not require humanitarian assistance. 3) HADB information is used as a main reference
  and supplemented by OCHA Field Office reports for those incidents where information
  is not available from the HADB. OCHA information includes assessment figures from
  OCHA, ANDMA, Red Crescent Societies, national NGOs, international NGOs, and ERM..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/natural-disaster-incidents-from-1-january-to-31-december-2012]'
details: These figures may fluctuate since the number of affected Afghans, people
  killed and injured, and houses damaged or destroyed are based on a combination of
  verified and non-verified reports received. Hence, these figures may change as updates
  are received.
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Post-event disaster incident records compiled from OCHA field offices
    and the Humanitarian Affairs Database (HADB) for Afghanistan during 2012. Data
    combines verified joint assessments with non-verified local reports from OCHA,
    ANDMA, and Red Crescent organizations. Incidents are classified by hazard type
    (avalanche, extreme winter, flood, heavy rainfall, landslide, extreme weather)
    and include affected population counts and fatality figures.
  sources:
  - id: source_1
    license: null
    name: OCHA Field Offices
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: HADB (Humanitarian Affairs Database)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: ANDMA and Red Crescent
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/natural-disaster-incidents-from-1-january-to-31-december-2012
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by flood incidents in Afghanistan during 2012
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
    description: Fatalities from flood incidents in Afghanistan during 2012
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
        metric: death
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population affected by landslide and mudflow incidents in Afghanistan
      during 2012
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
  - asset_category: population
    asset_dimension: population
    description: Fatalities from landslide and mudflow incidents in Afghanistan during
      2012
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
        metric: death
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population affected by extreme wind and sandstorm incidents in Afghanistan
      during 2012
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
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
    description: Population affected by extreme winter condition incidents in Afghanistan
      during 2012
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_extreme_temperature
      intensity_measure: AirTemp:C
      process: null
      trigger: null
      type: extreme_temperature
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
  description: Natural disaster events include avalanches, extreme winter conditions,
    flooding, heavy rainfall, landslides & mudflows, and extreme weather (sandstorms,
    hail, wind, etc) as recorded by OCHA field offices.
  download_url: https://data.humdata.org/dataset/0b9f8bb0-a78e-4b49-b127-39c0f71a45d1/resource/0ee1f39a-6bd7-419a-a98f-2346b6766b8a/download/afg-naturaldisasters2012-ocha-iom-201406may01.xlsx
  format: null
  id: resource_0ee1f39a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Afghanistan Natural Disaster Incidents from 1 January to 31 December 2012
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-afg_ochaafg_naturaldisasterincidents1_2012
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
  end: '2012-12-31'
  start: '2012-01-01'
temporal_resolution: null
title: Afghanistan - Natural disaster incidents from 1 January to 31 December 2012
version: null
vulnerability: null
---
