---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Education Cluster Yemen
  url: https://data.humdata.org/dataset/affected-schools-september-2017-included-july-2021-updated
creator:
  affiliation: null
  email: null
  name: Education Cluster Yemen
  url: https://data.humdata.org/dataset/affected-schools-september-2017-included-july-2021-updated
dataset_id: rdls_el-yem_edclyem_affectedschools_20210702
description: 'Affected Schools July 2021 updated. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/affected-schools-september-2017-included-july-2021-updated]'
details: null
exposure:
- asset_type:
    description: School buildings and educational infrastructure across Yemen
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: School-level impact data collected through sample survey methodology
    by the Education Cluster Yemen, documenting affected educational facilities and
    their status during the humanitarian crisis in July 2021.
  sources:
  - id: source_1
    license: null
    name: Education Cluster Yemen
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/affected-schools-september-2017-included-july-2021-updated
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Schools affected by conflict and hazards in Yemen as of July 2021
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
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
  description: 'Yemen: Affected Schools (Affected Schools included July_ 2021_updated.xlsx)'
  download_url: https://data.humdata.org/dataset/b8f67170-cfa6-4acc-9fe0-988a0766182d/resource/afb24d5e-b855-4feb-8066-2100ddf0ba54/download/affected-schools-updated-september-2017-included-july_-2021_updated.xlsx
  format: null
  id: resource_afb24d5e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Affected Schools included July_ 2021_updated.xlsx
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-yem_edclyem_affectedschools_20210702
spatial:
  bbox: null
  centroid: null
  countries:
  - YEM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2021-07-02'
temporal_resolution: null
title: 'Yemen: Affected Schools'
version: null
vulnerability: null
---
