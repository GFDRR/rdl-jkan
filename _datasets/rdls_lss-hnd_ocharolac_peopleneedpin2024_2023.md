---
attributions:
- entity:
    affiliation: null
    email: null
    name: JIAF 2.0 Methodology
    url: https://data.humdata.org/dataset/honduras-people-in-need-2024
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Honduras Humanitarian Needs and Response Plan (HNRP) 2024
    url: https://data.humdata.org/dataset/honduras-people-in-need-2024
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Latin America and the Caribbean (ROLAC)
  url: https://data.humdata.org/dataset/honduras-people-in-need-2024
creator:
  affiliation: null
  email: null
  name: OCHA Latin America and the Caribbean (ROLAC)
  url: https://data.humdata.org/dataset/honduras-people-in-need-2024
dataset_id: rdls_lss-hnd_ocharolac_peopleneedpin2024_2023
description: 'The dataset contains information on the number of people in need in
  Honduras in 2024 at the admin 2 level.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/honduras-people-in-need-2024]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: People in need figures were derived from multiple humanitarian assessment
    sources using the JIAF 2.0 methodology framework. Data was aggregated at the admin
    2 level with severity classifications to produce the Honduras Humanitarian Needs
    and Response Plan 2024, representing total affected populations across multiple
    hazard and vulnerability contexts.
  sources:
  - id: source_1
    license: null
    name: JIAF 2.0 Methodology
    risk_data_type:
    - loss
    type: model
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Honduras Humanitarian Needs and Response Plan (HNRP) 2024
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/honduras-people-in-need-2024
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: People in need across Honduras derived from multi-hazard humanitarian
      needs assessment
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
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
  url: https://reliefweb.int/report/honduras/honduras-necesidades-humanitarias-y-plan-de-respuesta-2024-enero-2024
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
    Honduras in 2024 at the admin 2 level.
  download_url: https://data.humdata.org/dataset/f3010e23-761e-4d55-80c1-527e6e245bd9/resource/163a7d81-b337-4d3a-8b9e-4b1653dbfd06/download/honduras-pin-hno-2024.xlsx
  format: null
  id: resource_163a7d81
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: honduras-pin-hno-2024.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-hnd_ocharolac_peopleneedpin2024_2023
spatial:
  bbox: null
  centroid: null
  countries:
  - HND
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-12-31'
  start: '2023-01-01'
temporal_resolution: null
title: Honduras People in Need PIN 2024
version: null
vulnerability: null
---
