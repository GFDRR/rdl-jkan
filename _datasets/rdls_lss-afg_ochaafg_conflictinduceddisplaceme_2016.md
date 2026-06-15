---
attributions:
- entity:
    affiliation: null
    email: null
    name: Inter-Agency Assessments
    url: https://data.humdata.org/dataset/afg-conflict-idps
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Afghanistan
  url: https://data.humdata.org/dataset/afg-conflict-idps
creator:
  affiliation: null
  email: null
  name: OCHA Afghanistan
  url: https://data.humdata.org/dataset/afg-conflict-idps
dataset_id: rdls_lss-afg_ochaafg_conflictinduceddisplaceme_2016
description: 'Newly displaced population due to conflict between 01 Jan 2016 and 31
  Dec 2016, compiled by OCHA sub offices based on inter-agency assessment results.
  This data is a snapshot as of 04 June 2017 and the numbers are expected to change
  as new assessment figures become available.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/afg-conflict-idps]'
details: That dataset is a snapshot as of 04 June 2017. Assessments are ongoing in
  the field and these numbers are subject to change as new information becomes available.
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Newly displaced population counts were compiled by OCHA sub-offices
    based on inter-agency assessment results conducted between 01 January and 31 December
    2016. Data represents a snapshot as of 04 June 2017 and was aggregated at the
    national level using census methodology.
  sources:
  - id: source_1
    license: null
    name: OCHA Afghanistan
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Inter-Agency Assessments
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/afg-conflict-idps
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population displacement due to conflict-induced violence in 2016
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
  description: Afghanistan - Conflict Induced Displacements in 2016 (Excel)
  download_url: https://data.humdata.org/dataset/ace9787d-1a4e-4ea5-a6c0-512c6e23a14e/resource/8df22107-ffd4-4c06-a701-16ff5d1bd2b4/download/afghanistan_conflict_displacements_2016.xlsx
  format: null
  id: resource_8df22107
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Afghanistan_Conflict_Displacements_2016.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Afghanistan - Conflict Induced Displacements in 2016 (CSV)
  download_url: https://data.humdata.org/dataset/ace9787d-1a4e-4ea5-a6c0-512c6e23a14e/resource/41edd142-121e-4d15-adb7-9d050206b99c/download/afghanistan_conflict_displacements_2017.csv
  format: null
  id: resource_41edd142
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Afghanistan_Conflict_Displacements_2017.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-afg_ochaafg_conflictinduceddisplaceme_2016
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
  end: '2016-12-30'
  start: '2016-01-01'
temporal_resolution: null
title: Afghanistan - Conflict Induced Displacements in 2016
version: null
vulnerability: null
---
