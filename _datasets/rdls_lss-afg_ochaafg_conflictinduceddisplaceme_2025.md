---
attributions:
- entity:
    affiliation: null
    email: null
    name: OCHA Afghanistan sub offices
    url: https://data.humdata.org/dataset/afghanistan-conflict-induced-displacements
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Humanitarian partners
    url: https://data.humdata.org/dataset/afghanistan-conflict-induced-displacements
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Afghanistan
  url: https://data.humdata.org/dataset/afghanistan-conflict-induced-displacements
creator:
  affiliation: null
  email: null
  name: OCHA Afghanistan
  url: https://data.humdata.org/dataset/afghanistan-conflict-induced-displacements
dataset_id: rdls_lss-afg_ochaafg_conflictinduceddisplaceme_2025
description: 'Newly displaced population due to conflict compiled by OCHA sub offices
  based on inter-agency assessment results. The numbers are expected to change as
  new assessment figures become available.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/afghanistan-conflict-induced-displacements]'
details: The dataset is a snapshot as of 05 January 2023. Assessments are ongoing
  in the field and these numbers are subject to change as new information becomes
  available.
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Conflict-induced displacement figures are compiled by OCHA Afghanistan
    sub offices from inter-agency assessment results conducted by humanitarian partners
    in the field. Data is aggregated by displacement date and geographic origin/destination
    at provincial and district levels, with demographic disaggregation by individuals,
    families, and age/gender groups. The dataset represents a living compilation updated
    as new assessment figures become available.
  sources:
  - id: source_1
    license: null
    name: OCHA Afghanistan sub offices
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Humanitarian partners
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/afghanistan-conflict-induced-displacements
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons due to conflict violence, disaggregated
      by individuals, families, and demographic groups
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
purpose: Census
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Afghanistan - Conflict Induced Displacements (Excel)
  download_url: https://data.humdata.org/dataset/7695bdab-40cc-42ee-ab66-ddad667ee771/resource/a14afbc7-2b59-42e9-8642-abd9a7169ceb/download/afghanistan_conflict_displacements_2025.xlsx
  format: null
  id: resource_a14afbc7
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: afghanistan_conflict_displacements_2025.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Afghanistan - Conflict Induced Displacements (CSV)
  download_url: https://data.humdata.org/dataset/7695bdab-40cc-42ee-ab66-ddad667ee771/resource/86fbf0be-1f1a-4194-8d4f-a722706041d4/download/afghanistan_conflict_displacements_2025.csv
  format: null
  id: resource_86fbf0be
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: afghanistan_conflict_displacements_2025.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-afg_ochaafg_conflictinduceddisplaceme_2025
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
  end: '2025-03-03'
  start: '2025-02-28'
temporal_resolution: null
title: Afghanistan - Conflict Induced Displacements
version: null
vulnerability: null
---
