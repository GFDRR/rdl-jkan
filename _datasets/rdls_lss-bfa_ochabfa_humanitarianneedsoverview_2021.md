---
attributions:
- entity:
    affiliation: null
    email: null
    name: Humanitarian Partners
    url: https://data.humdata.org/dataset/burkina-humanitarian-needs-overview-2021
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Burkina Faso
  url: https://data.humdata.org/dataset/burkina-humanitarian-needs-overview-2021
creator:
  affiliation: null
  email: null
  name: OCHA Burkina Faso
  url: https://data.humdata.org/dataset/burkina-humanitarian-needs-overview-2021
dataset_id: rdls_lss-bfa_ochabfa_humanitarianneedsoverview_2021
description: 'This data is a snapshot of the humanitarian situation in Burkina Faso..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/burkina-humanitarian-needs-overview-2021]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: This Humanitarian Needs Overview aggregates impact data from multiple
    humanitarian partners operating in Burkina Faso to provide a snapshot of affected
    populations, internally displaced persons, and humanitarian needs. The dataset
    synthesizes field assessments and administrative records to quantify disaster-related
    population impacts at the national level.
  sources:
  - id: source_1
    license: null
    name: Humanitarian Partners
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/burkina-humanitarian-needs-overview-2021
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by flooding in Burkina Faso
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
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons from flood-related displacement
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
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
  url: https://bit.ly/2S2rUAx
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Burkina Faso : Humanitarian Needs Overview (Burkina Faso Humanitarian
    Needs Overview 2021)'
  download_url: https://data.humdata.org/dataset/bad884cd-48ef-407a-acc4-208675e091d2/resource/b0db3d0b-1c6c-41ec-a4c6-bbc0bc22f27c/download/bfa_hno_2021.xlsx
  format: null
  id: resource_b0db3d0b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bfa_hno_2021.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-bfa_ochabfa_humanitarianneedsoverview_2021
spatial:
  bbox: null
  centroid: null
  countries:
  - BFA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2021-12-31'
  start: '2021-01-01'
temporal_resolution: null
title: 'Burkina Faso : Humanitarian Needs Overview'
version: null
vulnerability: null
---
