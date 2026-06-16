---
attributions:
- entity:
    affiliation: null
    email: null
    name: USGS Earthquakes and Shakemaps
    url: https://data.humdata.org/dataset/earthquakes
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: USGS PAGER (Prompt Assessment of Global Earthquakes for Response)
    url: https://data.humdata.org/dataset/earthquakes
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Esri
  url: https://data.humdata.org/dataset/earthquakes
creator:
  affiliation: null
  email: null
  name: Esri
  url: https://data.humdata.org/dataset/earthquakes
dataset_id: rdls_hzd-esri_recentearthquakes_20200409
description: 'This map displays continuously updated data from the USGS Earthquakes
  and Shakemaps. This map is provided by the Esri Disaster Response Program.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/earthquakes]'
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
      intensity_measure: PGA:g
      process: ground_motion
      trigger: null
      type: earthquake
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC0-1.0
lineage:
  description: Earthquake locations and magnitudes are continuously collected by the
    USGS seismic monitoring network. Ground motion shakemaps are generated using the
    PAGER program methodology, which models seismic wave propagation and converts
    instrumental data into intensity measures for rapid hazard assessment and emergency
    response.
  sources:
  - id: source_1
    license: null
    name: USGS Earthquakes and Shakemaps
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: USGS PAGER (Prompt Assessment of Global Earthquakes for Response)
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/earthquakes
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
- access_url: https://disasterresponse.maps.arcgis.com/apps/webappviewer/index.html?id=e588a7f3ba0d41388b5052b6444457a8
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This web applications displays continuously updated data from the USGS
    Earthquakes and Shakemaps. This map is provided by the Esri Disaster Response
    Program.
  download_url: null
  format: null
  id: resource_d15bd1fa
  media_type: text/html
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Earthquake App
- access_url: https://services9.arcgis.com/RHVPKKiFTONKtxq3/arcgis/rest/services/USGS_Seismic_Data_v1/FeatureServer
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This service presents recent earthquake information from the USGS Prompt
    Assessment of Global Earthquakes for Response (PAGER) program.
  download_url: null
  format: null
  id: resource_538415b5
  media_type: text/html
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Earthquake Data
- access_url: https://www.arcgis.com/home/item.html?id=9e2f2b544c954fda9cd13b7f3e6eebce
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This service presents recent earthquake information from the USGS Prompt
    Assessment of Global Earthquakes for Response (PAGER) program.
  download_url: null
  format: null
  id: resource_0f32d1a4
  media_type: text/html
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Living Atlas Earthquakes Service
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-esri_recentearthquakes_20200409
spatial:
  bbox: null
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2020-04-09'
temporal_resolution: null
title: Recent Earthquakes
version: null
vulnerability: null
---
