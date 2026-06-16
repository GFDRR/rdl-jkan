---
attributions:
- entity:
    affiliation: null
    email: null
    name: Global Disaster Alert and Coordination System (GDACS)
    url: https://data.humdata.org/dataset/gdacs-rss-information
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Global Disaster Alert and Coordination System
  url: https://data.humdata.org/dataset/gdacs-rss-information
creator:
  affiliation: null
  email: null
  name: Global Disaster Alert and Coordination System
  url: https://data.humdata.org/dataset/gdacs-rss-information
dataset_id: rdls_hzd-bolcod_global_disaster_gdacsrssinformation_2022
description: 'GDACS alerts are issued for earthquakes and possible subsequent tsunamis,
  tropical cyclones, floods and volcanoes. Earthquake, tsunami and tropical cyclones
  calculations and assessments are done automatically, without human intervention.
  Floods and volcanic eruptions are currently manually introduced. Research and development
  is continuous to improve the global monitoring.. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/gdacs-rss-information]'
details: While we try everything to ensure accuracy, this information is purely indicative
  and should not be used for any decision making without alternate sources of information.
  The JRC is not responsible for any damage or loss resulting from use of the information
  presented on this website.
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
      id: hzd_earthquake
      intensity_measure: PGA:g
      process: ground_motion
      trigger: null
      type: earthquake
    id: es_earthquake
    occurrence_range: null
    seasonality: null
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hzd_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: es_flood
    occurrence_range: null
    seasonality: null
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hzd_wind
      intensity_measure: ws:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: es_wind
    occurrence_range: null
    seasonality: null
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hzd_volcanic
      intensity_measure: T:cm
      process: ashfall
      trigger: null
      type: volcanic
    id: es_volcanic
    occurrence_range: null
    seasonality: null
license: CC-BY-4.0
lineage:
  description: GDACS integrates multiple hazard detection systems (automatic for seismic
    and cyclone events, manual for floods and volcanoes) to generate real-time alert
    information. The RSS feed aggregates severity assessments and event metadata across
    multiple hazard types for global disaster monitoring and coordination.
  sources:
  - id: source_1
    license: null
    name: Global Disaster Alert and Coordination System (GDACS)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/gdacs-rss-information
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://gdacs.org/Knowledge/overview.aspx
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: GDACS RSS Information (CSV)
  download_url: https://data.humdata.org/dataset/a87f96f8-16e6-4d51-872c-cfa54a8251ec/resource/4ef001d1-7888-4f5d-98ce-0ca8006787f7/download/gdacs_rss_information.csv
  format: null
  id: resource_4ef001d1
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gdacs_rss_information.csv
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-bolcod_global_disaster_gdacsrssinformation_2022
spatial:
  bbox: null
  centroid: null
  countries:
  - BOL
  - COD
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-02-03'
  start: '2022-09-21'
temporal_resolution: null
title: GDACS RSS Information
version: null
vulnerability: null
---
