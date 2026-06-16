---
attributions:
- entity:
    affiliation: null
    email: null
    name: OCHA Field Offices
    url: https://data.humdata.org/dataset/natural-disaster-incidents-from-1-january-to-31-december-2014
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: IOM Afghanistan Humanitarian Assistance Database (HADB)
    url: https://data.humdata.org/dataset/natural-disaster-incidents-from-1-january-to-31-december-2014
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Afghanistan
  url: https://data.humdata.org/dataset/natural-disaster-incidents-from-1-january-to-31-december-2014
creator:
  affiliation: null
  email: null
  name: OCHA Afghanistan
  url: https://data.humdata.org/dataset/natural-disaster-incidents-from-1-january-to-31-december-2014
dataset_id: rdls_lss-afg_ochaafg_naturaldisasterincidents1_2014
description: '1) Natural disaster events include avalanches, extreme winter conditions,
  flooding, heavy rainfall, landslides & mudflows, and extreme weather (sandstorms,
  hail, wind, etc) as recorded by OCHA field offices and IOM Afghanistan Humanitarian
  Assistance Database (HADB). 2) A natural disaster incident is defined as an event
  that has affected (i.e. impacted) Afghans, who may or may not require humanitarian
  assistance. 3) HADB information is used as a main reference and supplemented by
  OCHA Field Office reports for those incidents where information is not available
  from the HADB. OCHA information includes assessment figures from OCHA, ANDMA, Red
  Crescent Societies, national NGOs, international NGOs, and ERM.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/natural-disaster-incidents-from-1-january-to-31-december-2014]'
details: These figures may fluctuate since the number of affected Afghans, people
  killed and injured, and houses damaged or destroyed are based on a combination of
  verified and non-verified reports received. Hence, these figures may change as updates
  are received.
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Post-event natural disaster incident data compiled from IOM Afghanistan's
    Humanitarian Assistance Database (primary source) and supplemented by OCHA field
    office reports for incidents lacking HADB coverage. Data combines verified joint
    assessments with non-verified local reports of avalanches, extreme weather, flooding,
    landslides, and mudflows affecting Afghan populations during 2014.
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
    name: IOM Afghanistan Humanitarian Assistance Database (HADB)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/natural-disaster-incidents-from-1-january-to-31-december-2014
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by flooding incidents
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
    description: Population affected by landslides and mudflows
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
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
  - asset_category: population
    asset_dimension: population
    description: Population affected by extreme weather including sandstorms, hail,
      and wind
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
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
    description: Population affected by extreme winter conditions
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_extreme_temperature
      intensity_measure: AirTemp:C
      process: null
      trigger: null
      type: extreme_temperature
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
    hail, wind, etc) as recorded by OCHA field offices and IOM Afghanistan Humanitarian
    Assistance Database (HADB).
  download_url: https://data.humdata.org/dataset/85001b26-5007-49e1-bfae-0450a31b834d/resource/9bb58c34-33f2-4e39-a97c-a314b0432eac/download/afg-naturaldisasters2014-ocha-iom-20150111.xlsx
  format: null
  id: resource_9bb58c34
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Afghanistan Natural Disaster Incidents from 1 January to 31 December 2014
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-afg_ochaafg_naturaldisasterincidents1_2014
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
  end: '2014-12-31'
  start: '2014-01-01'
temporal_resolution: null
title: Afghanistan - Natural disaster incidents from 1 January to 31 December 2014
version: null
vulnerability: null
---
