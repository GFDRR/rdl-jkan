---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM) Lilongwe
    url: https://data.humdata.org/dataset/malawi-flood-response-site-assessment-round-1
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/malawi-flood-response-site-assessment-round-1
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/malawi-flood-response-site-assessment-round-1
dataset_id: rdls_el-mwi_iom_floodresponseround1siteas_2015
description: 'Site Assessment conducted as the response to internal displacement due
  to Floods in 2015. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/malawi-flood-response-site-assessment-round-1]'
details: Census of sites based on interviews of key informants in sites.
exposure:
- asset_type:
    description: Internally displaced persons from flood-affected settlements in Malawi
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
license: CC-BY-4.0
lineage:
  description: Census-based site assessment conducted by IOM Lilongwe to enumerate
    internally displaced persons and characterize affected settlements following the
    2015 floods in Malawi. The dataset captures post-event displacement impacts across
    populated places.
  sources:
  - id: source_1
    license: null
    name: International Organization for Migration (IOM) Lilongwe
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/malawi-flood-response-site-assessment-round-1
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population displacement due to 2015 flooding in Malawi
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
  description: Malawi Flood Response Round 1 - Site assessment (Excel)
  download_url: https://data.humdata.org/dataset/f1128065-2a36-40df-8313-1f11b2834d43/resource/474b5e77-ec04-449e-ba98-8fe56c1342b8/download/malawi_sa_round1_final_dataset.xls
  format: null
  id: resource_474b5e77
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Malawi_SA_Round1_Final_Dataset.xls
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-mwi_iom_floodresponseround1siteas_2015
spatial:
  bbox: null
  centroid: null
  countries:
  - MWI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2015-03-15'
  start: '2015-01-12'
temporal_resolution: null
title: Malawi Flood Response Round 1 - Site assessment
version: null
vulnerability: null
---
