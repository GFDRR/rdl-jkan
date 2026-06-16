---
attributions:
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/ethiopia-flooding-somali-region
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Sentinel-1
    url: https://data.humdata.org/dataset/ethiopia-flooding-somali-region
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/ethiopia-flooding-somali-region
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/ethiopia-flooding-somali-region
dataset_id: rdls_he-eth_unosat_floodingsomaliregion_20180501
description: 'UNOSAT produced satellite-detected flood water extent in Somali Region,
  Ethiopia. The analysis was conducted by analysing a Sentinel-1 image acquired on
  the 1 May 2018. As observed from the satellite radar image, a total of 9,200 ha
  of land were inundated in the area of interest. By using WorldPop data, we estimate
  that at least 12,000 people are potentially affected or living close to the flooded
  area. This corresponds to about 7% of the population living in the area of interest.
  It is likely that flood waters have been systematically underestimated along highly
  vegetated areas along main river banks and within built-up urban areas because of
  the special characteristics of the satellite data used. This is a preliminary analysis
  and has not yet been validated in the field. Please send ground feedback to UNITAR
  UNOSAT. Satellite Data: Sentinel-1. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/ethiopia-flooding-somali-region]'
details: 'From UNOSAT documentation: ''It is likely that flood waters have been systematically
  underestimated along highly vegetated areas along main river banks and within built-up
  urban areas because of the special characteristics of the satellite data used. '''
exposure:
- asset_type:
    description: Population living in or near flooded areas, estimated at 12,000 people
      (7% of area population) using WorldPop data
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
hazard:
  event_sets_by_hazard_type:
    flood:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: AA:km2
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: UNOSAT analyzed a Sentinel-1 SAR image acquired on 1 May 2018 to detect
    and delineate flood water extent in Somali Region, Ethiopia. The observed inundated
    area (9,200 ha) was intersected with WorldPop gridded population data to estimate
    affected population. Flood waters were systematically underestimated in highly
    vegetated areas along main rivers due to radar signal penetration limitations.
  sources:
  - id: source_1
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: Sentinel-1
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/ethiopia-flooding-somali-region
  rel: source
loss:
  losses: []
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
  description: Analysis of the 2018 05 01 flooding - Shabelle & Afder Zones, Somali
    region, Ethiopia
  download_url: https://data.humdata.org/dataset/74f5d67a-75e6-4d00-bb1e-8342a166aa3b/resource/3ba00d3b-2930-4394-8901-4e4fd70519b5/download/fl20180501som_ethiopia_imi.xlsx
  format: null
  id: resource_3ba00d3b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20180501SOM_Ethiopia_Imi.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite-detected flood water 2018 05 01 flooding - Shabelle & Afder
    Zones, Somali region, Ethiopia
  download_url: https://data.humdata.org/dataset/74f5d67a-75e6-4d00-bb1e-8342a166aa3b/resource/d5ee1331-ea91-4d24-8fbe-cf9be1cab31a/download/st20180501_somali_flood_water.zip
  format: null
  id: resource_d5ee1331
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ST20180501_Somali_Flood_Water.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-eth_unosat_floodingsomaliregion_20180501
spatial:
  bbox: null
  centroid: null
  countries:
  - ETH
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-05-01'
temporal_resolution: null
title: Ethiopia flooding Somali region
version: null
vulnerability: null
---
