---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/unosat-cuba-popexposure-windspeed-matthew-20161006
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-cuba-popexposure-windspeed-matthew-20161006
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-cuba-popexposure-windspeed-matthew-20161006
dataset_id: rdls_he-cub_unosat_populationexposurewindspe_20161006
description: 'Population Exposure Wind Speed Zones, Cuba. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/unosat-cuba-popexposure-windspeed-matthew-20161006]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics and the limitations of the sources
  used to implement those results.
exposure:
- asset_type:
    description: Population exposed to different wind speed zones from Hurricane Matthew
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
    strong_wind:
    - analysis_type: deterministic
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
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: UNOSAT derived wind speed exposure zones from Hurricane Matthew satellite
    observations and classified them into three threshold categories (60, 90, 120
    km/h). Population counts from census data were spatially intersected with these
    wind speed zones at the administrative level to quantify population exposure by
    wind intensity.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/unosat-cuba-popexposure-windspeed-matthew-20161006
  rel: source
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Census
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Cuba - Population Exposure Wind Speed from Hurricane Matthew (UNOSAT,
    2016-10-06.) (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/HT/TC20161003HTI/UNOSAT_Cuba_PopExposure_WindSpeed_Matthew_20161006.zip
  format: null
  id: resource_8a870910
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_Cuba_PopExposure_WindSpeed_Matthew_20161006
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-cub_unosat_populationexposurewindspe_20161006
spatial:
  bbox: null
  centroid: null
  countries:
  - CUB
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-10-06'
temporal_resolution: null
title: Cuba - Population Exposure Wind Speed from Hurricane Matthew (UNOSAT, 2016-10-06.)
version: null
vulnerability: null
---
