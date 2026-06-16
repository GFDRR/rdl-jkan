---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Haiti
  url: https://data.humdata.org/dataset/ocha-haiti-topline-figures
creator:
  affiliation: null
  email: null
  name: OCHA Haiti
  url: https://data.humdata.org/dataset/ocha-haiti-topline-figures
dataset_id: rdls_lss-hti_ochahti_toplinefigures_20161019
description: 'Topline figures dataset for OCHA Haiti organisation page. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/ocha-haiti-topline-figures]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Topline figures aggregated from multiple sources documenting cyclone
    and hurricane impacts on Haiti, compiled by OCHA Haiti for situational awareness
    and humanitarian response coordination.
  sources:
  - id: source_1
    license: null
    name: Multiple Sources
    risk_data_type:
    - loss
    type: null
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/ocha-haiti-topline-figures
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by cyclones and hurricanes in Haiti
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
        metric: exposure
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
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
  description: OCHA Haiti Topline Figures (CSV)
  download_url: https://docs.google.com/spreadsheets/d/1K0qwvwJsluYGWOJ66203RqSSctXEgAdAliVOWdcXVXE/pub?gid=0&single=true&output=csv
  format: null
  id: resource_d2530424
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: topline_figures.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-hti_ochahti_toplinefigures_20161019
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
  start: '2016-10-19'
temporal_resolution: null
title: OCHA Haiti Topline Figures
version: null
vulnerability: null
---
