---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Colombia
  url: https://data.humdata.org/dataset/people-in-need
creator:
  affiliation: null
  email: null
  name: OCHA Colombia
  url: https://data.humdata.org/dataset/people-in-need
dataset_id: rdls_lss-col_ochacol_peopleneed_20141031
description: 'The population in need for 2015 is an estimated humanitarian caseload,
  including people affected by the armed conflict and people affected by natural disasters.
  It is calculated based on trends from the last two and a half years (2012-2014)..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/people-in-need]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Population in need estimates were derived from trend analysis of conflict
    and disaster-affected populations recorded between 2012 and 2014, with 2015 projections
    calculated using historical averages and trend extrapolation. The dataset aggregates
    humanitarian caseload data from multiple sources into departmental-level estimates
    of total people in need.
  sources:
  - id: source_1
    license: null
    name: OCHA Colombia
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/people-in-need
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by armed conflict and natural disasters in 2015
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
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
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Colombia - People in need (People in need.csv)
  download_url: https://data.humdata.org/dataset/82226a46-4592-45ab-841c-89630b465f51/resource/f1553385-c3a3-4474-bcb4-63cf6a7e4a8f/download/people-in-need.csv
  format: null
  id: resource_f1553385
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: People in need.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Colombia - People in need (People in need.xlsx)
  download_url: https://data.humdata.org/dataset/82226a46-4592-45ab-841c-89630b465f51/resource/2acbeced-752a-4fbb-b348-886c53024e40/download/people-in-need.xlsx
  format: null
  id: resource_2acbeced
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: People in need.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Colombia - People in need (People in need 2016.csv)
  download_url: https://data.humdata.org/dataset/82226a46-4592-45ab-841c-89630b465f51/resource/6bdebde4-ec75-4845-b91d-f29ae984ea4c/download/151106people_in_need_mpal.csv
  format: null
  id: resource_6bdebde4
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: People in need 2016.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Colombia - People in need (People in need 2016 - Departamental.csv)
  download_url: https://data.humdata.org/dataset/82226a46-4592-45ab-841c-89630b465f51/resource/a4886611-c34d-4e12-8e91-de74da77c12d/download/151106people_in_need_dpto.csv
  format: null
  id: resource_a4886611
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: People in need 2016 - Departamental.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-col_ochacol_peopleneed_20141031
spatial:
  bbox: null
  centroid: null
  countries:
  - COL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2014-10-31'
temporal_resolution: null
title: Colombia - People in need
version: null
vulnerability: null
---
