---
attributions:
- entity:
    affiliation: null
    email: null
    name: DSWD (Department of Social Welfare and Development)
    url: https://data.humdata.org/dataset/philippines-humanitarian-profile
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Philippines
  url: https://data.humdata.org/dataset/philippines-humanitarian-profile
creator:
  affiliation: null
  email: null
  name: OCHA Philippines
  url: https://data.humdata.org/dataset/philippines-humanitarian-profile
dataset_id: rdls_lss-phl_ochaphl_dromicdatamunicipalitiesw_20140126
description: 'DROMIC data by DSWD on municipalities within the 50km radius of the
  typhoon Haiyan/Yolanda track as of 27 January 2014. Historic COD used during response
  to Typhoon Haiyan, November 2013.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/philippines-humanitarian-profile]'
details: '**Languages:** EN'
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: DSWD compiled DROMIC impact data from municipalities within the 50km
    radius of Typhoon Haiyan/Yolanda track during the November 2013 response. The
    dataset consolidates displacement and affected population figures from administrative
    reports collected through the disaster response monitoring system.
  sources:
  - id: source_1
    license: null
    name: DSWD (Department of Social Welfare and Development)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/philippines-humanitarian-profile
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population displacement from Typhoon Haiyan impact in municipalities
      within 50km radius of track
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Affected population from Typhoon Haiyan in municipalities within
      50km radius of track
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
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
  description: Philippines - DROMIC data on municipalities within 50km radius of typhoon
    Haiyan (Typhoon Yolanda DSWD DROMIC Consolidated 27Jan2014.xlsx)
  download_url: https://data.humdata.org/dataset/280623c2-b56a-4946-8d11-d4d251fe7967/resource/84f2722c-a20d-48b0-8a44-f86e4547b370/download/typhoon-yolanda-dswd-dromic-consolidated-27jan2014.xlsx
  format: null
  id: resource_84f2722c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Typhoon Yolanda DSWD DROMIC Consolidated 27Jan2014.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-phl_ochaphl_dromicdatamunicipalitiesw_20140126
spatial:
  bbox: null
  centroid: null
  countries:
  - PHL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2014-01-26'
temporal_resolution: null
title: Philippines - DROMIC data on municipalities within 50km radius of typhoon Haiyan
version: null
vulnerability: null
---
