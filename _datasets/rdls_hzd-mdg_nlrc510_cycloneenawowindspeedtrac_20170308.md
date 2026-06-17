---
attributions:
- entity:
    affiliation: null
    email: null
    name: University College London
    url: https://data.humdata.org/dataset/cyclone-enawo-madagascar-windspeed-track-and-rainfall
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: GPM (Global Precipitation Measurement)
    url: https://data.humdata.org/dataset/cyclone-enawo-madagascar-windspeed-track-and-rainfall
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Netherlands Red Cross - 510
  url: https://data.humdata.org/dataset/cyclone-enawo-madagascar-windspeed-track-and-rainfall
creator:
  affiliation: null
  email: null
  name: Netherlands Red Cross - 510
  url: https://data.humdata.org/dataset/cyclone-enawo-madagascar-windspeed-track-and-rainfall
dataset_id: rdls_hzd-mdg_nlrc510_cycloneenawowindspeedtrac_20170308
description: 'Please note that the windspeed and track dataset only covers the part
  where the this was still a tropical cyclone. For explanation see below caveats.
  Due to this we will not release a priority index, since windspeed data is missing
  for most of the country. Dataset of windspeed and track was kindly provided by University
  College London. The rainfall data is calculated based on GPM. It is the accumulated
  rainfall from March 6th midnight to March 10th 10:00am Madagascar time.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/cyclone-enawo-madagascar-windspeed-track-and-rainfall]'
details: Last update on tropical cyclone Enawo was at 18:00 UT 7th March 2017. The
  data is issued by the Joint Typhoon Warning Center (JTWC) in Hawaii. JTWC stops
  issuing data on landfalling tropical cyclones when they loose their tropical cyclone
  status (due to loss of storm structure and organisation). This happened at 18:00
  UT 7th March 2017 for Enawo. (Such loss of structure after landfall does not occur
  for tropical cyclones which strike the Philippines nor for any small island country
  worldwide).
exposure: []
hazard:
  event_sets:
  - analysis_type: probabilistic
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
  type: strong_wind
license: CC-BY-4.0
lineage:
  description: Windspeed and track data were directly observed/measured by University
    College London during Cyclone Enawo's passage. Rainfall accumulation was derived
    from GPM satellite precipitation measurements for the period March 6-10, 2017.
    The dataset captures the hazard footprint of a tropical cyclone event in Madagascar.
  sources:
  - id: source_1
    license: null
    name: University College London
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: GPM (Global Precipitation Measurement)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/cyclone-enawo-madagascar-windspeed-track-and-rainfall
  rel: source
loss: null
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
  description: Cyclone Enawo - Madagascar - windspeed, track and rainfall (Cyclone
    Enawo - track.zip)
  download_url: https://data.humdata.org/dataset/1ffa6ae8-438d-43c7-921b-40356647981f/resource/3ac3332b-8a31-4e5a-8cff-2d545ddb61be/download/cyclone-enawo-track.zip
  format: null
  id: resource_3ac3332b
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Cyclone Enawo - track.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Cyclone Enawo - Madagascar - windspeed, track and rainfall (Cyclone
    Enawo - windspeeds.zip)
  download_url: https://data.humdata.org/dataset/1ffa6ae8-438d-43c7-921b-40356647981f/resource/d16093a7-3f2d-48f3-b7b3-46d497b879c4/download/cyclone-enawo-windspeeds.zip
  format: null
  id: resource_d16093a7
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Cyclone Enawo - windspeeds.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Cyclone Enawo - Madagascar - windspeed, track and rainfall (CSV)
  download_url: https://data.humdata.org/dataset/1ffa6ae8-438d-43c7-921b-40356647981f/resource/e4b58dfd-0a05-4b62-90a8-0a75328a7150/download/enawo_rainfall.csv
  format: null
  id: resource_e4b58dfd
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Enawo_rainfall.csv
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-mdg_nlrc510_cycloneenawowindspeedtrac_20170308
spatial:
  bbox: null
  centroid: null
  countries:
  - MDG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-03-08'
temporal_resolution: null
title: Cyclone Enawo - Madagascar - windspeed, track and rainfall
version: null
vulnerability: null
---
