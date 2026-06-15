---
attributions:
- entity:
    affiliation: null
    email: null
    name: OCHA DRC
    url: https://data.humdata.org/dataset/drc-congo-humanitarian-needs-overview
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX
  url: https://data.humdata.org/dataset/drc-congo-humanitarian-needs-overview
creator:
  affiliation: null
  email: null
  name: OCHA DRC
  url: https://data.humdata.org/dataset/drc-congo-humanitarian-needs-overview
dataset_id: rdls_lss-cod_hdx_humanitarianneedsoverview_202101
description: 'The Democratic republic of the Congo Humanitarian needs overview for
  2021. This data has been extracted from the published HRP document for DRC. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/drc-congo-humanitarian-needs-overview]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: The dataset was extracted from the published 2021 DRC Humanitarian
    Response Plan (HRP) document compiled by OCHA DRC through sample survey methodology.
    It aggregates humanitarian needs assessments across the country to quantify affected
    populations requiring assistance.
  sources:
  - id: source_1
    license: null
    name: OCHA DRC
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/drc-congo-humanitarian-needs-overview
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: People in need from flood-related humanitarian crisis in DRC
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
purpose: Sample Survey
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The Democratic republic of the Congo Humanitarian needs overview for
    2021. This data has been extracted from the published HRP document for DRC
  download_url: https://data.humdata.org/dataset/d294f0c8-23bf-4263-a0d9-92806a20425c/resource/77979098-1005-457f-b23b-708c7f12be26/download/drc-hno-2021_people-in-need.xlsx
  format: null
  id: resource_77979098
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DRC HNO 2021_People in Need.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-cod_hdx_humanitarianneedsoverview_202101
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
  end: '2021-01-31'
  start: '2021-01-01'
temporal_resolution: null
title: 'Democratic Republic of the Congo: Humanitarian needs overview'
version: null
vulnerability: null
---
