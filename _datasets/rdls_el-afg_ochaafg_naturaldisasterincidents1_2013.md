---
attributions:
- entity:
    affiliation: null
    email: null
    name: OCHA Field Offices
    url: https://data.humdata.org/dataset/natural-disaster-incidents-from-1-january-to-31-december-2013
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: IOM Afghanistan Humanitarian Assistance Database (HADB)
    url: https://data.humdata.org/dataset/natural-disaster-incidents-from-1-january-to-31-december-2013
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Afghanistan
  url: https://data.humdata.org/dataset/natural-disaster-incidents-from-1-january-to-31-december-2013
creator:
  affiliation: null
  email: null
  name: OCHA Afghanistan
  url: https://data.humdata.org/dataset/natural-disaster-incidents-from-1-january-to-31-december-2013
dataset_id: rdls_el-afg_ochaafg_naturaldisasterincidents1_2013
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
  dataset: https://data.humdata.org/dataset/natural-disaster-incidents-from-1-january-to-31-december-2013]'
details: These figures may fluctuate since the number of affected Afghans, people
  killed and injured, and houses damaged or destroyed are based on a combination of
  verified and non-verified reports received. Hence, these figures may change as updates
  are received.
exposure:
- asset_type:
    description: Afghan population affected by natural disaster incidents in 2013
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
  description: Natural disaster incident data was collected from OCHA field offices
    and the IOM Afghanistan Humanitarian Assistance Database (HADB) throughout 2013.
    HADB served as the primary reference source, supplemented by OCHA field office
    reports for incidents lacking HADB documentation. Data combines verified joint
    assessments with non-verified local reports to create a comprehensive record of
    disaster events affecting Afghan populations.
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
- href: https://data.humdata.org/dataset/natural-disaster-incidents-from-1-january-to-31-december-2013
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by flood incidents in Afghanistan during 2013
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
    description: Population affected by landslide and mudflow incidents in Afghanistan
      during 2013
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
    description: Population affected by extreme wind events in Afghanistan during
      2013
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
    description: Population affected by extreme winter conditions in Afghanistan during
      2013
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
  download_url: https://data.humdata.org/dataset/49d674f6-5c1f-4c07-a0c5-2aea3dc300f3/resource/3bb7611c-d793-44cc-a367-b3204b2ce8aa/download/afg-naturaldisasters2013-ocha-iom-a3-201403mar29.xlsx
  format: null
  id: resource_3bb7611c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Afghanistan Natural Disaster Incidents from 1 January to 31 December 2013
- access_url: http://bit.ly/V7Aie9
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Afghanistan - Natural disaster incidents from 1 January to 31 December
    2013 (Summary of 2013 flood incidents by district)
  download_url: null
  format: null
  id: resource_e246c934
  media_type: text/html
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Summary of Flood Incidents in 2013 (Map)
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-afg_ochaafg_naturaldisasterincidents1_2013
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
  end: '2013-12-31'
  start: '2013-01-01'
temporal_resolution: null
title: Afghanistan - Natural disaster incidents from 1 January to 31 December 2013
version: null
vulnerability: null
---
