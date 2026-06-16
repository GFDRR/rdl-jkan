---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Afghanistan
  url: https://data.humdata.org/dataset/afghanistan-conflict-induced-displacements-in-2018
creator:
  affiliation: null
  email: null
  name: OCHA Afghanistan
  url: https://data.humdata.org/dataset/afghanistan-conflict-induced-displacements-in-2018
dataset_id: rdls_lss-afg_ochaafg_conflictinduceddisplaceme_2018
description: 'Newly displaced population due to conflict between 01 January 2018 and
  31 December 2018, compiled by OCHA sub offices based on inter-agency assessment
  results. This data is a snapshot as of 28 January 2019 and the numbers are expected
  to change as new assessment figures become available.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/afghanistan-conflict-induced-displacements-in-2018]'
details: The dataset is a snapshot as of 28 January 2019. Assessments are ongoing
  in the field and these numbers are subject to change as new information becomes
  available.
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Displacement data compiled by OCHA Afghanistan sub-offices from inter-agency
    assessment results conducted throughout 2018, aggregated at the national level
    to produce a snapshot of conflict-induced internal displacement as of January
    2019.
  sources:
  - id: source_1
    license: null
    name: OCHA Afghanistan
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/afghanistan-conflict-induced-displacements-in-2018
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced population due to conflict-induced violence
      in 2018
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
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
  description: Afghanistan - Conflict Induced Displacements in 2018 (Excel)
  download_url: https://data.humdata.org/dataset/8a6ea378-1813-4c3c-9d4c-b9d1adcefa8d/resource/0cfe97fb-7288-47cd-aa08-94450a437176/download/afghanistan_conflict_displacements_2018.xlsx
  format: null
  id: resource_0cfe97fb
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Afghanistan_Conflict_Displacements_2018.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Afghanistan - Conflict Induced Displacements in 2018 (CSV)
  download_url: https://data.humdata.org/dataset/8a6ea378-1813-4c3c-9d4c-b9d1adcefa8d/resource/16e559ae-57d2-4c37-b16f-a09fce110761/download/afghanistan_conflict_displacements_2018.csv
  format: null
  id: resource_16e559ae
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Afghanistan_Conflict_Displacements_2018.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-afg_ochaafg_conflictinduceddisplaceme_2018
spatial:
  bbox: null
  centroid: null
  countries:
  - AFG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2018-12-31'
  start: '2018-01-01'
temporal_resolution: null
title: Afghanistan - Conflict Induced Displacements in 2018
version: null
vulnerability: null
---
