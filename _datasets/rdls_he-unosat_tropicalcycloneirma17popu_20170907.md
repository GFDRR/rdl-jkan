---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/population-exposure-estimates-based-on-tropical-cyclone-irma-s-path
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/population-exposure-estimates-based-on-tropical-cyclone-irma-s-path
dataset_id: rdls_he-unosat_tropicalcycloneirma17popu_20170907
description: 'Population exposure estimates based on tropical cyclone IRMA-17 path
  observed and predicted at 7 September 2017.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/population-exposure-estimates-based-on-tropical-cyclone-irma-s-path]'
details: This is a preliminary analysis and has not yet been validated in the field.
exposure:
- asset_type:
    description: Population exposed to tropical cyclone IRMA-17 path by administrative
      boundary
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
  description: UNOSAT derived the observed and predicted track of tropical cyclone
    IRMA-17 from satellite data as of 7 September 2017. Population exposure was estimated
    by intersecting the cyclone track corridor with gridded or administrative-level
    population data to quantify the number of people in the path of the storm.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/population-exposure-estimates-based-on-tropical-cyclone-irma-s-path
  rel: source
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Sample Survey
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Population exposure estimates based on tropical cyclone IRMA-17 path
    observed and predicted at 7 September 2017. The tropical cyclone path and wind
    speed zones were derived from Joint Research Centre data (Warning 33 issued the
    07 th September 2017 at 09:00 UTC). This is a preliminary analysis and has not
    yet been validated in the field.
  download_url: https://data.humdata.org/dataset/f5a928ff-c23b-4c44-9a48-94d7197b48ba/resource/4dd75d03-5928-4061-91d0-d6481178d5c5/download/admin_pop.zip
  format: null
  id: resource_4dd75d03
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Admin_Pop.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-unosat_tropicalcycloneirma17popu_20170907
spatial:
  bbox: null
  centroid: null
  countries:
  - BES
  - USA
  - ATG
  - BRB
  - DMA
  - DOM
  - GRD
  - HTI
  - JAM
  - KNA
  - LCA
  - VCT
  - VGB
  - VIR
  - PRI
  - TCA
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-09-07'
temporal_resolution: null
title: 'Tropical Cyclone IRMA-17 : Population Exposure estimates'
version: null
vulnerability: null
---
