---
attributions:
- entity:
    affiliation: null
    email: null
    name: JIAF 2.0 Methodology
    url: https://data.humdata.org/dataset/el-salvador-people-in-need-pin-2024
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Latin America and the Caribbean (ROLAC)
  url: https://data.humdata.org/dataset/el-salvador-people-in-need-pin-2024
creator:
  affiliation: null
  email: null
  name: OCHA Latin America and the Caribbean (ROLAC)
  url: https://data.humdata.org/dataset/el-salvador-people-in-need-pin-2024
dataset_id: rdls_lss-slv_ocharolac_peopleneedpin2024_2023
description: 'The dataset contains information on the number of people in need in
  El Salvador in 2024 at the admin 1 level.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/el-salvador-people-in-need-pin-2024]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: People in need figures were derived from multiple sources using the
    JIAF 2.0 methodology as documented in the 2024 Humanitarian Needs Overview for
    El Salvador. The dataset aggregates humanitarian needs assessments at the admin
    1 level to produce a consolidated estimate of affected population requiring assistance.
  sources:
  - id: source_1
    license: null
    name: JIAF 2.0 Methodology
    risk_data_type:
    - loss
    type: model
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/el-salvador-people-in-need-pin-2024
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: People in need in El Salvador derived from multi-source humanitarian
      assessment
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
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
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://reliefweb.int/attachments/51220b12-022e-4d70-9720-cf5e2143f344/HNO_SV%202024_20240212.pdf?_gl=1*8u5sef*_ga*Mjg3NjM4MDcyLjE2OTM4NTE4ODk.*_ga_E60ZNX2F68*MTcxMjM0MTY1My4zOS4wLjE3MTIzNDE2NTMuNjAuMC4w
- author_names: null
  date_published: null
  doi: null
  id: reference_2
  name: Methodology documentation
  url: https://analysis.jiaf.info/
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The dataset contains information on the number of people in need in
    El Salvador in 2024 at the admin 1 level.
  download_url: https://data.humdata.org/dataset/653ed446-b89f-4bfe-bf47-573e9aee9148/resource/d79ca5c2-9f7e-46b0-b301-707f6eb159d3/download/el-salvador-pin-hno-2024-.csv
  format: null
  id: resource_d79ca5c2
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: el-salvador-pin-hno-2024-.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-slv_ocharolac_peopleneedpin2024_2023
spatial:
  bbox: null
  centroid: null
  countries:
  - SLV
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-12-31'
  start: '2023-01-01'
temporal_resolution: null
title: El Salvador People in Need PIN 2024
version: null
vulnerability: null
---
