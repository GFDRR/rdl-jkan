---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNISYS
    url: https://data.humdata.org/dataset/asia-pacific-storm-tracks-1956-to-2018
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: NOAA
    url: https://data.humdata.org/dataset/asia-pacific-storm-tracks-1956-to-2018
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Regional Office for Asia and the Pacific (ROAP)
  url: https://data.humdata.org/dataset/asia-pacific-storm-tracks-1956-to-2018
creator:
  affiliation: null
  email: null
  name: OCHA Regional Office for Asia and the Pacific (ROAP)
  url: https://data.humdata.org/dataset/asia-pacific-storm-tracks-1956-to-2018
dataset_id: rdls_hzd-ocharoap_stormtracks19562018_20181231
description: 'This shape file consists of consolidated history of tropical storm paths
  over the past 50 years in the West Pacific, South Pacific, South Indian and North
  Indian basin. Attributes provides details such as storm Name, Date, Time, wind speed
  and GPS points for each advisory point. Wind speeds are in knots for more details
  on speeds conversion and storm categories please visit the original source of data:
  UNISYS (http://weather.unisys.com/hurricane/index.php), NOAA (http://rammb.cira.colostate.edu/products/tc_realtime/index.asp).
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/asia-pacific-storm-tracks-1956-to-2018]'
details: Updated as of 31 December 2018.
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
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC0-1.0
lineage:
  description: Historical tropical cyclone tracks were consolidated from UNISYS and
    NOAA sources covering 1956-2018 across West Pacific, South Pacific, South Indian,
    and North Indian basins. Each track point includes observed wind speed (in knots),
    pressure, date, time, and geographic coordinates. Data is provided as a shapefile
    with advisory-level spatial resolution.
  sources:
  - id: source_1
    license: null
    name: UNISYS
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
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
- href: https://data.humdata.org/dataset/asia-pacific-storm-tracks-1956-to-2018
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Registry
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This shape file consists of consolidated history of tropical storm
    paths over the past 50 years in the West Pacific, South Pacific, South Indian
    and North Indian basin. Attributes provides details such as storm Name, Date,
    Time, wind speed and GPS points for each advisory point. Wind speeds are in knots
    for more details on speeds conversion and storm categories please visit the original
    source of data: UNISYS, NOAA (http://rammb.cira.colostate.edu/products/tc_realtime/index.asp)'
  download_url: https://data.humdata.org/dataset/b1068a22-ec52-459d-9541-0fb63906bb39/resource/85fe1efc-e737-4b9a-ae87-b0365a1cced3/download/unisys_tracks_1956_2018dec31.zip
  format: null
  id: resource_85fe1efc
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNISYS_tracks_1956_2018Dec31.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-ocharoap_stormtracks19562018_20181231
spatial:
  bbox: null
  centroid: null
  countries:
  - KOR
  - VNM
  - AUS
  - FJI
  - IDN
  - IND
  - JPN
  - KHM
  - LAO
  - LKA
  - MMR
  - MYS
  - PHL
  - SGP
  - THA
  - TLS
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-12-31'
temporal_resolution: null
title: 'Asia Pacific: Storm tracks 1956 to 2018'
version: null
vulnerability: null
---
