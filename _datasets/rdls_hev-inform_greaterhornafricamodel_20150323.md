---
attributions:
- entity:
    affiliation: null
    email: null
    name: Inter-Agency Standing Committee (IASC)
    url: https://data.humdata.org/dataset/inform-greater-horn-of-africa-model
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: European Commission
    url: https://data.humdata.org/dataset/inform-greater-horn-of-africa-model
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Intergovernmental Authority on Development (IGAD)
    url: https://data.humdata.org/dataset/inform-greater-horn-of-africa-model
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: INFORM
  url: https://data.humdata.org/dataset/inform-greater-horn-of-africa-model
creator:
  affiliation: null
  email: null
  name: INFORM
  url: https://data.humdata.org/dataset/inform-greater-horn-of-africa-model
dataset_id: rdls_hev-inform_greaterhornafricamodel_20150323
description: 'The INFORM Greater Horn of Africa model is part of an initiative of
  Intergovernmental Authority on Development (IGAD) and OCHA to improve IGAD''s ability
  to analyse, visualise and disseminate information to support the prevention, preparedness
  and response to humanitarian crises in the region. The model will be updated regularly
  to support regional coordination and prioritise humanitarian, development, risk
  management and resilience investments.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/inform-greater-horn-of-africa-model]'
details: null
exposure:
- asset_type:
    description: Population exposure indicators as part of the INFORM Hazards & Exposure
      dimension
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
      quantity_kind: index
      unit: null
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: inferred
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: The INFORM model integrates multiple data sources across three risk
    dimensions (Hazards & Exposure, Vulnerability, Lack of Coping Capacity) using
    a composite index methodology. Indicators are normalized and aggregated to produce
    sub-national risk scores for humanitarian crisis prevention and preparedness planning
    in the IGAD region.
  sources:
  - id: source_1
    license: null
    name: Inter-Agency Standing Committee (IASC)
    risk_data_type:
    - vulnerability
    type: dataset
    url: null
    used_in: vulnerability
  - id: source_2
    license: null
    name: European Commission
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
  - id: source_3
    license: null
    name: Intergovernmental Authority on Development (IGAD)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/inform-greater-horn-of-africa-model
  rel: source
loss: null
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
  url: https://bit.ly/2MB0ZIj
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: INFORM Greater Horn of Africa Model (INFORM_GHoA vs 20 March 2015 .xlsx)
  download_url: https://data.humdata.org/dataset/b77e83a3-a6a0-4176-aaa5-e40062e8dc57/resource/0e19d685-526b-4787-9830-f7c1b7805cee/download/inform_ghoa-vs-20-march-2015-.xlsx
  format: null
  id: resource_0e19d685
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: INFORM_GHoA vs 20 March 2015 .xlsx
risk_data_type:
- hazard
- exposure
- vulnerability
schema: rdls-10
slug: rdls_hev-inform_greaterhornafricamodel_20150323
spatial:
  bbox: null
  centroid: null
  countries:
  - DJI
  - ERI
  - ETH
  - KEN
  - SOM
  - SSD
  - SDN
  - UGA
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-03-23'
temporal_resolution: null
title: INFORM Greater Horn of Africa Model
version: null
vulnerability: null
---
