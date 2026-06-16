---
attributions:
- entity:
    affiliation: null
    email: null
    name: NOAA
    url: https://data.humdata.org/dataset/current-weather-and-wind-station-data
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Esri
  url: https://data.humdata.org/dataset/current-weather-and-wind-station-data
creator:
  affiliation: null
  email: null
  name: Esri
  url: https://data.humdata.org/dataset/current-weather-and-wind-station-data
dataset_id: rdls_hzd-usa_esri_currentweatherwindstation_20200506
description: 'Live feed sources on severe weather across the United States. The Current
  Weather and Wind Station Data layer is created from hourly METAR station data provided
  from NOAA and contains approximately 11 weather variables for each location.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/current-weather-and-wind-station-data]'
details: null
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
      intensity_measure: sws_10m:m/s
      process: extratropical_cyclone
      trigger: null
      type: strong_wind
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC0-1.0
lineage:
  description: Hourly METAR station data from NOAA are ingested and processed by Esri
    to create a live feed geoservice containing approximately 11 weather variables
    per station location, enabling real-time monitoring of severe weather and wind
    conditions across the United States.
  sources:
  - id: source_1
    license: null
    name: NOAA
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/current-weather-and-wind-station-data
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: https://www.arcgis.com/home/item.html?id=cb1886ff0a9d4156ba4d2fadd7e8a139
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The Current Weather and Wind Station Data layer is created from hourly
    METAR station data provided from NOAA and contains approximately 11 weather variables
    for each location.
  download_url: null
  format: null
  id: resource_f469b50f
  media_type: text/html
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Current Weather and Wind Station Data
- access_url: https://www.arcgis.com/home/item.html?id=250d053c7b2049548d4435ccbe8d658d
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Description Map containing live feed sources for severe weather across
    the United States.
  download_url: null
  format: null
  id: resource_b954d34a
  media_type: text/html
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Severe Weather App
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-usa_esri_currentweatherwindstation_20200506
spatial:
  bbox: null
  centroid: null
  countries:
  - USA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2020-05-06'
temporal_resolution: null
title: United States - Current Weather and Wind Station data
version: null
vulnerability: null
---
