---
attributions:
- entity:
    affiliation: null
    email: null
    name: MINISTERE DE LA SANTE ET DU DEVELOPPEMENT SOCIAL - DIRECTION NATIONALE DU
      DEVELOPPEMENT SOCIAL
    url: https://data.humdata.org/dataset/mali-situation-des-inondations
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Mali WASH Cluster
  url: https://data.humdata.org/dataset/mali-situation-des-inondations
creator:
  affiliation: null
  email: null
  name: Mali WASH Cluster
  url: https://data.humdata.org/dataset/mali-situation-des-inondations
dataset_id: rdls_lss-mli_mali_wash_clust_situationdesinondations_20241231
description: 'This dataset outlines the population and household figures affected
  by flooding, categorized by gender, in Mali for the year 2024 at the administrative
  level 1.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/mali-situation-des-inondations]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: "Post-event impact data collected through direct observation and anecdotal\
    \ reporting by Mali's Direction Nationale du D\xC3\xA9veloppement Social documenting\
    \ population and household figures affected by flooding in 2024, disaggregated\
    \ by gender at administrative level 1."
  sources:
  - id: source_1
    license: null
    name: MINISTERE DE LA SANTE ET DU DEVELOPPEMENT SOCIAL - DIRECTION NATIONALE DU
      DEVELOPPEMENT SOCIAL
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/mali-situation-des-inondations
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by flooding in Mali, disaggregated by gender
      at administrative level 1
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
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mali: Situation des inondations (Flooding impacts in 2024 at admin
    1)'
  download_url: https://data.humdata.org/dataset/d6f5da02-9b35-4c03-9917-67587f4621f9/resource/d167dd1e-d0ff-4874-b018-f89ad90c332f/download/mali-situation-des-inondations-2024-dnds-xlsx.xlsx
  format: null
  id: resource_d167dd1e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Mali Situation des inondations 2024 DNDS.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-mli_mali_wash_clust_situationdesinondations_20241231
spatial:
  bbox: null
  centroid: null
  countries:
  - MLI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-12-31'
temporal_resolution: null
title: 'Mali: Situation des inondations'
version: null
vulnerability: null
---
