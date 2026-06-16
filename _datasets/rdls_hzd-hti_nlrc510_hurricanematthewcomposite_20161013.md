---
attributions:
- entity:
    affiliation: null
    email: null
    name: Accumulated GPM IMERG data for Haiti Hurricane Matthew October 3-6th 2016
    url: https://data.humdata.org/dataset/haiti-hurricane-matthew-composite-index-hurricane-impact-wind-rain
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Hurricane Matthew Gust Footprint - Tropical Storm Risk, University College
      London
    url: https://data.humdata.org/dataset/haiti-hurricane-matthew-composite-index-hurricane-impact-wind-rain
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Netherlands Red Cross - 510
  url: https://data.humdata.org/dataset/haiti-hurricane-matthew-composite-index-hurricane-impact-wind-rain
creator:
  affiliation: null
  email: null
  name: Netherlands Red Cross - 510
  url: https://data.humdata.org/dataset/haiti-hurricane-matthew-composite-index-hurricane-impact-wind-rain
dataset_id: rdls_hzd-hti_nlrc510_hurricanematthewcomposite_20161013
description: 'Includes the windspeed per adm3-area, and a combined 1-10 score for
  windspeed and accumulated rainfall. Datasets used: https://data.humdata.org/dataset/accumulated-gpm-imerg-data-for-haiti-hurricane-matthew-october-3-6th-2016
  https://data.humdata.org/dataset/hurricane-matthew-gust-footprint-tropical-storm-risk-university-college-london.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/haiti-hurricane-matthew-composite-index-hurricane-impact-wind-rain]'
details: '- converted windspeed vector input layer to raster in QGIS - used ''Zonal
  statistics'' in QGIS to compute average windspeed per adm3-area - computed 1-10
  scores for both rain and windspeed by transforming the min-max range linearly to
  a 1-10 range (simply computed manually in Attribute Table) and averaged them (with
  equal weights) to a composite score.'
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
license: CC-BY-4.0
lineage:
  description: Wind speed and accumulated rainfall data from two independent sources
    (TSR gust footprint model and GPM IMERG satellite observations) were integrated
    and aggregated to administrative level 3 boundaries. A composite 1-10 impact index
    was calculated combining normalized windspeed and rainfall metrics to characterize
    Hurricane Matthew's hazard intensity across Haiti.
  sources:
  - id: source_1
    license: null
    name: Accumulated GPM IMERG data for Haiti Hurricane Matthew October 3-6th 2016
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: Hurricane Matthew Gust Footprint - Tropical Storm Risk, University College
      London
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/haiti-hurricane-matthew-composite-index-hurricane-impact-wind-rain
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
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Haiti - Hurricane Matthew - composite index hurricane impact (wind,
    rain) (Shapefile)
  download_url: https://data.humdata.org/dataset/37455eee-27bc-4aef-b766-eae0583187b3/resource/44cbb8a5-4dee-4c67-b972-945453e329e8/download/rain_wind_matthew_adm3.zip
  format: null
  id: resource_44cbb8a5
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rain_wind_matthew_adm3.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Haiti - Hurricane Matthew - composite index hurricane impact (wind,
    rain) (PCODED, HXL)
  download_url: https://data.humdata.org/dataset/37455eee-27bc-4aef-b766-eae0583187b3/resource/69c81dab-f62b-4dfa-b0ca-22f6f833dd93/download/rainfall_windspeed_output.xlsx
  format: null
  id: resource_69c81dab
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rain_wind_matthew_adm3.xlsx
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-hti_nlrc510_hurricanematthewcomposite_20161013
spatial:
  bbox: null
  centroid: null
  countries:
  - HTI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-10-13'
temporal_resolution: null
title: Haiti - Hurricane Matthew - composite index hurricane impact (wind, rain)
version: null
vulnerability: null
---
