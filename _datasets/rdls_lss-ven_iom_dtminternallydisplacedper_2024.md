---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
      (DTM)
    url: https://data.humdata.org/dataset/venezuela-iom-dtm-idps
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/venezuela-iom-dtm-idps
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/venezuela-iom-dtm-idps
dataset_id: rdls_lss-ven_iom_dtminternallydisplacedper_2024
description: 'This dataset provide an overview of humanitarian needs in Venezuela
  at Municipal level. The data was collected via interviews with key informants in
  the community.. [Source: This metadata record was automatically extracted from the
  Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/venezuela-iom-dtm-idps]'
details: 'Sampling scheme: Indicative and by quotas, sampling by municipality to key
  informants. Sample size: 4,365 key informants. Please note that this data is for
  determining characteristics and does not represent the totality of IDPs in Venezuela.'
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: IOM DTM conducted sample surveys via key informant interviews across
    Venezuelan municipalities to document internally displaced persons and associated
    humanitarian needs. Data aggregated at municipal level to provide overview of
    displacement impacts and vulnerability.
  sources:
  - id: source_1
    license: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
      (DTM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/venezuela-iom-dtm-idps
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons from unspecified hazards in Venezuela
      at municipal level
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
purpose: Sample Survey
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Venezuela - IOM DTM Internally Displaced Persons (Round 2)
  download_url: https://data.humdata.org/dataset/72fe0ae6-78e6-41cd-82b8-25d1ae201c33/resource/056a5e59-4786-456e-9a02-7a26a7d0f7ec/download/oim_dtm_venezuela_ronda-ii_2024-vf08072024_cleaned.xlsx
  format: null
  id: resource_056a5e59
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: OIM_DTM_VENEZUELA_RONDA II_2024 VF08072024
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ven_iom_dtminternallydisplacedper_2024
spatial:
  bbox: null
  centroid: null
  countries:
  - VEN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-07-05'
  start: '2024-05-10'
temporal_resolution: null
title: Venezuela - IOM DTM Internally Displaced Persons
version: null
vulnerability: null
---
