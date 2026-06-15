---
attributions:
- entity:
    affiliation: null
    email: null
    name: INFORM Initiative
    url: https://data.humdata.org/dataset/the-inform-honduras-model
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Inter-Agency Standing Committee (IASC)
    url: https://data.humdata.org/dataset/the-inform-honduras-model
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: European Commission
    url: https://data.humdata.org/dataset/the-inform-honduras-model
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: INFORM
  url: https://data.humdata.org/dataset/the-inform-honduras-model
creator:
  affiliation: null
  email: null
  name: INFORM
  url: https://data.humdata.org/dataset/the-inform-honduras-model
dataset_id: rdls_ev-hnd_inform_model
description: 'The INFOM Honduras tool has been implemented and will be updated by
  the Permanent Contingency Commission (COPECO). COPECO and other government institutions
  will jointly implement the INFORM initiative in the context of the National Risk
  Management System (SINAGER). The national Humanitarian Network, Civil Society Organizations,
  Academic institutions, and the Association of Municipalities of Honduras (AMHON)
  will also collaborate with the initiative.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/the-inform-honduras-model]'
details: null
exposure:
- asset_type:
    description: Population exposed to multiple natural hazards (earthquakes, floods,
      cyclones, landslides, drought, wildfires, pests) at municipal level
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
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: The INFORM Honduras model integrates multi-hazard exposure data (earthquakes,
    floods, cyclones, landslides, drought, wildfires, pests), socioeconomic vulnerability
    indicators (poverty, inequality, development), and coping capacity metrics (governance,
    infrastructure, health) at municipal level. The composite risk index is calculated
    following INFORM methodology published in scientific literature, combining these
    three dimensions to produce an overall humanitarian risk score for Honduras.
  sources:
  - id: source_1
    license: null
    name: INFORM Initiative
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: Inter-Agency Standing Committee (IASC)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_3
    license: null
    name: European Commission
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/the-inform-honduras-model
  rel: source
loss:
  losses: []
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
- author_names: null
  date_published: null
  doi: null
  id: reference_2
  name: Methodology documentation
  url: https://bit.ly/2OedEgO
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'INFORM Honduras is a municipal risk index that identifies risks, threats,
    vulnerabilities and response capacities in the 298 municipalities of Honduras.
    The municipal risk index simplifies information about crisis risk and is comprised
    of 35 indicators representing the three dimensions of risk: hazard and exposure,
    vulnerability, and lack of coping capacity.'
  download_url: https://data.humdata.org/dataset/64ad5a07-33b0-48d8-a38b-cd948152723d/resource/f926a1a4-6fdf-41bc-9452-3f7a8f911d3b/download/inform_honduras_25_oct_2021.xlsx
  format: null
  id: resource_f926a1a4
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: INFORM_Honduras_25_OCT_2021.xlsx
risk_data_type:
- exposure
- vulnerability
schema: rdls-10
slug: rdls_ev-hnd_inform_model
spatial:
  bbox: null
  centroid: null
  countries:
  - HND
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: INFORM Honduras model
version: null
vulnerability: null
---
