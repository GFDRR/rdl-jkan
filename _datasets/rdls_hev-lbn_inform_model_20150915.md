---
attributions:
- entity:
    affiliation: null
    email: null
    name: Inter-Agency Standing Committee (IASC)
    url: https://data.humdata.org/dataset/inform-lebanon-model
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: European Commission
    url: https://data.humdata.org/dataset/inform-lebanon-model
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: INFORM
  url: https://data.humdata.org/dataset/inform-lebanon-model
creator:
  affiliation: null
  email: null
  name: INFORM
  url: https://data.humdata.org/dataset/inform-lebanon-model
dataset_id: rdls_hev-lbn_inform_model_20150915
description: 'INFORM Lebanon was developed by the Lebanon Joint Analysis Unit, which
  supports the Resident/Humanitarian Coordinator and is a collaboration of humanitarian,
  development and governmental partners that supports cross sectoral planning at the
  national level. INFORM Lebanon is being embedded in regional processes and coordination
  mechanisms to help all partners quantify and prioritise humanitarian and disaster
  risks in Lebanon in the context of the regional Syrian Crisis Response.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/inform-lebanon-model]'
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
      quantity_kind: count
      unit: count
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
      intensity_measure: PGA:g
      process: ground_motion
      trigger: null
      type: earthquake
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: The INFORM Lebanon model integrates multiple indicator datasets across
    three risk dimensions (Hazards & Exposure, Vulnerability, Lack of Coping Capacity)
    at cadastral level, following the INFORM global methodology adapted for subnational
    analysis in the context of the Syrian Crisis Response.
  sources:
  - id: source_1
    license: null
    name: Inter-Agency Standing Committee (IASC)
    risk_data_type:
    - vulnerability
    type: model
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
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/inform-lebanon-model
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
  description: INFORM Lebanon Model (INFORM_LEBANON 2015_CADASTRAL_v034.xlsx)
  download_url: https://data.humdata.org/dataset/e40e7133-42a8-441f-9f9e-97853f6a82a7/resource/b5fff2a5-e021-4495-84b9-d4617b121dfb/download/inform_lebanon-2015_cadastral_v034.xlsx
  format: null
  id: resource_b5fff2a5
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: INFORM_LEBANON 2015_CADASTRAL_v034.xlsx
risk_data_type:
- hazard
- exposure
- vulnerability
schema: rdls-10
slug: rdls_hev-lbn_inform_model_20150915
spatial:
  bbox: null
  centroid: null
  countries:
  - LBN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-09-15'
temporal_resolution: null
title: INFORM Lebanon Model
version: null
vulnerability: null
---
