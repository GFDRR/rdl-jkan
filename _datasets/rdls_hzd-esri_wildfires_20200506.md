---
attributions:
- entity:
    affiliation: null
    email: null
    name: NASA LANCE VIIRS Thermal Hotspots and Fire Activity
    url: https://data.humdata.org/dataset/wildfires
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: NASA EOSDIS MODIS Global Fires
    url: https://data.humdata.org/dataset/wildfires
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Esri
  url: https://data.humdata.org/dataset/wildfires
creator:
  affiliation: null
  email: null
  name: Esri
  url: https://data.humdata.org/dataset/wildfires
dataset_id: rdls_hzd-esri_wildfires_20200506
description: 'This includes layers for detectable thermal activity from VIIRS satellites
  for the last 7 days and MODIS satellites for the last 48 hours. VIIRS Thermal Hotspots
  and Fire Activity is a product of NASA''s Land, Atmosphere Near real-time Capability
  for EOS (LANCE) Earth Observation Data, while MODIS Global Fires is a product of
  NASA''s Earth Observing System Data and Information System (EOSDIS), both a part
  of NASA''s Earth Science Data. EOSDIS integrates remote sensing and GIS technologies
  to deliver global MODIS hotspot/fire locations to natural resource managers and
  other stakeholders around the World. The application includes live feed sources
  for US wildfire reports (I-209), perimeters, MODIS hot spots, wildfire conditions
  / red flag warnings, wildfire potential and weather radar. Each of these layers
  provides insight into where a fire is located, its intensity and the surrounding
  areas susceptibility to wildfire.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/wildfires]'
details: null
exposure: []
hazard:
  event_sets_by_hazard_type:
    wildfire:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: FWI:-
        process: wildfire
        trigger: null
        type: wildfire
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/publicdomain/zero/1.0/
lineage:
  description: Thermal hotspot data are collected from VIIRS and MODIS satellite sensors
    and processed by NASA LANCE and EOSDIS systems to detect active fire thermal signatures.
    The data are delivered as near real-time geoservices and web applications for
    natural resource managers and stakeholders to monitor current wildfire activity
    globally.
  sources:
  - id: source_1
    license: null
    name: NASA LANCE VIIRS Thermal Hotspots and Fire Activity
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: NASA EOSDIS MODIS Global Fires
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/wildfires
  rel: source
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: https://www.arcgis.com/home/item.html?id=dece90af1a0242dcbf0ca36d30276aa3
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Thermal activity detected by the VIIRS sensors on the NOAA/NASA Suomi
    NPP and NOAA-20 satellites during the last 7 days.
  download_url: null
  format: null
  id: resource_7680c8c0
  media_type: text/html
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Satellite (VIIRS) Thermal Hotspots and Fire Activity
- access_url: https://www.arcgis.com/home/item.html?id=b8f4033069f141729ffb298b7418b653
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Thermal activity detected by the MODIS sensors on the NASA Aqua and
    Terra satellites during the last 48 hours.
  download_url: null
  format: null
  id: resource_11b51f0f
  media_type: text/html
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Satellite (MODIS) Thermal Hotspots and Fire Activity
- access_url: https://www.arcgis.com/home/item.html?id=2ff1677111ae4018ac705fcce7c3312f
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Map containing live feed sources for US wildfire reports (I-209), perimeters,
    MODIS hot spots, and wildfire potential.
  download_url: null
  format: null
  id: resource_e02424c0
  media_type: text/html
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: USA Wildfire Application
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-esri_wildfires_20200506
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
  start: '2020-05-06'
temporal_resolution: null
title: Wildfires
version: null
vulnerability: null
---
