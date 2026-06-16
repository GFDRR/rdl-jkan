---
attributions:
- entity:
    affiliation: null
    email: null
    name: OCHA and Clusters
    url: https://data.humdata.org/dataset/humanitarian-needs-overview-classification-tool
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Democratic Republic of the Congo (DRC)
  url: https://data.humdata.org/dataset/humanitarian-needs-overview-classification-tool
creator:
  affiliation: null
  email: null
  name: OCHA Democratic Republic of the Congo (DRC)
  url: https://data.humdata.org/dataset/humanitarian-needs-overview-classification-tool
dataset_id: rdls_lss-cod_ochacod_humanitarianneedsoverview_20140630
description: 'Classification tool used for the Humanitarian Needs Overview 2015..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/humanitarian-needs-overview-classification-tool]'
details: Data is being extended to cover Jan to Sept. 2014
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: The Humanitarian Needs Overview 2015 classification tool aggregates
    direct observational and anecdotal data from OCHA and humanitarian clusters across
    DRC to document population-level impacts including displacement and humanitarian
    access constraints. The dataset compiles needs assessment data from the first
    semester of 2014 to inform humanitarian response prioritization.
  sources:
  - id: source_1
    license: null
    name: OCHA and Clusters
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/humanitarian-needs-overview-classification-tool
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by humanitarian needs including displacement
      and access constraints
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
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The needs analysis presented here is based on a vulnerability analysis
    tool. This tool has been simplified and improved compared to 2014, with indicators
    based on four types of crises (conflicts with violence, nutrition, epidemics,
    natural disasters) rather than sectoral indicators. Each province for each type
    of crisis was assigned a score that is based on the values of indicators (two
    for each type of crisis but one for nutritional crises), and the score shown is
    the average by crisis of values obtained by indicator.
  download_url: https://data.humdata.org/dataset/5bacb214-20f3-4b69-bff7-5c761ad65e58/resource/69f247c5-8588-406b-b291-377e0323c8e9/download/hno-compilation-nationale-semestre1-2014.xlsx
  format: null
  id: resource_69f247c5
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: HNO_COMPILATION_NATIONALE_SEMESTRE1_2014.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-cod_ochacod_humanitarianneedsoverview_20140630
spatial:
  bbox: null
  centroid: null
  countries:
  - COD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2014-06-30'
temporal_resolution: null
title: DR Congo - Humanitarian Needs Overview Classification Tool
version: null
vulnerability: null
---
