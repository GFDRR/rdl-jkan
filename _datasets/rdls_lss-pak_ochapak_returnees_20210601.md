---
attributions:
- entity:
    affiliation: null
    email: null
    name: CEW PDMA Khyber Pakhtoonkhwa
    url: https://data.humdata.org/dataset/pakistan-returnees
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Pakistan
  url: https://data.humdata.org/dataset/pakistan-returnees
creator:
  affiliation: null
  email: null
  name: OCHA Pakistan
  url: https://data.humdata.org/dataset/pakistan-returnees
dataset_id: rdls_lss-pak_ochapak_returnees_20210601
description: 'Pakistan district wise Returnees with PCodes. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/pakistan-returnees]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: District-level returnee counts were compiled from CEW PDMA Khyber Pakhtunkhwa
    registry data, aggregated by administrative district with PCodes for spatial reference.
    This dataset documents post-displacement population movements and recovery patterns
    following flood events.
  sources:
  - id: source_1
    license: null
    name: CEW PDMA Khyber Pakhtoonkhwa
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/pakistan-returnees
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population returnees (displaced persons returning) by district following
      flood displacement
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
purpose: Registry
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pakistan Returnees by district with PCodes
  download_url: https://data.humdata.org/dataset/d6e54f33-f42f-4e1e-bfaf-fd652384ad40/resource/e8636257-9619-4798-9314-bff0eba3bf6f/download/pakistan-total-returnees.xlsx
  format: null
  id: resource_e8636257
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Pakistan Returnees by District
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-pak_ochapak_returnees_20210601
spatial:
  bbox: null
  centroid: null
  countries:
  - PAK
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2021-06-01'
temporal_resolution: null
title: Pakistan Returnees
version: null
vulnerability: null
---
