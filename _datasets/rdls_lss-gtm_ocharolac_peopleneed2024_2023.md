---
attributions:
- entity:
    affiliation: null
    email: null
    name: JIAF 2.0
    url: https://data.humdata.org/dataset/guatemala-people-in-need-2024
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: HNO 2023 Guatemala
    url: https://data.humdata.org/dataset/guatemala-people-in-need-2024
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Latin America and the Caribbean (ROLAC)
  url: https://data.humdata.org/dataset/guatemala-people-in-need-2024
creator:
  affiliation: null
  email: null
  name: OCHA Latin America and the Caribbean (ROLAC)
  url: https://data.humdata.org/dataset/guatemala-people-in-need-2024
dataset_id: rdls_lss-gtm_ocharolac_peopleneed2024_2023
description: 'The dataset contains information on the number of people in need in
  Guatemala in 2024 at the admin 2 level.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/guatemala-people-in-need-2024]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: People in need figures were derived from multiple sources integrated
    through the JIAF 2.0 methodology as documented in the 2023 HNO. The dataset aggregates
    humanitarian needs assessments at admin 2 level for Guatemala in 2024, combining
    multi-hazard and multi-sectoral impact data.
  sources:
  - id: source_1
    license: null
    name: JIAF 2.0
    risk_data_type:
    - loss
    type: model
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: HNO 2023 Guatemala
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/guatemala-people-in-need-2024
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: People in need in Guatemala derived from multi-hazard humanitarian
      needs assessment
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
  url: https://reliefweb.int/attachments/b31b5b19-fcad-4fe9-acad-4620ed02e91c/HNO%20GT%202023%20eng.pdf
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
    Guatemala in 2024 at the admin 2 level.
  download_url: https://data.humdata.org/dataset/70741d48-f37e-4bd4-9f2d-331b033a0a49/resource/e8c9046f-b4bf-47e8-b64e-4c271204f866/download/guatemala-pin-hno-2024-v2-.csv
  format: null
  id: resource_e8c9046f
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guatemala-pin-hno-2024 v2-.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-gtm_ocharolac_peopleneed2024_2023
spatial:
  bbox: null
  centroid: null
  countries:
  - GTM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-12-31'
  start: '2023-01-01'
temporal_resolution: null
title: Guatemala - People in Need 2024
version: null
vulnerability: null
---
