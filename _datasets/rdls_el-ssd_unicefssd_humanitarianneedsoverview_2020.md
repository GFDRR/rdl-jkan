---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: UNICEF South Sudan
  url: https://data.humdata.org/dataset/south-sudan-humanitarian-needs-overview-hno-2020
creator:
  affiliation: null
  email: null
  name: UNICEF South Sudan
  url: https://data.humdata.org/dataset/south-sudan-humanitarian-needs-overview-hno-2020
dataset_id: rdls_el-ssd_unicefssd_humanitarianneedsoverview_2020
description: 'South Sudan Humanitarian Needs Overview HNO 2020. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/south-sudan-humanitarian-needs-overview-hno-2020]'
details: null
exposure:
- asset_type:
    description: Host community, internally displaced persons, and returnee populations
      across South Sudan
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
  description: Population estimates for host communities, internally displaced persons,
    and returnees were compiled from census data and administrative records. These
    estimates were integrated into the 2020 Humanitarian Needs Overview to quantify
    populations affected by humanitarian crises including displacement and flood impacts
    across South Sudan.
  sources:
  - id: source_1
    license: null
    name: UNICEF South Sudan
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/south-sudan-humanitarian-needs-overview-hno-2020
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population in need due to humanitarian crisis including flood-affected
      populations
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
purpose: Census
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: South Sudan Humanitarian Needs Overview HNO 2020 (Excel)
  download_url: https://data.humdata.org/dataset/73f076d4-7bd1-41e7-83de-7d25ecbad789/resource/8ed30190-c94b-478b-8f92-bfab2711f4fb/download/20200110_ssd_pop_estimates_hc_idps_returnees_hxl.xlsx
  format: null
  id: resource_8ed30190
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20200110_ssd_pop_estimates_hc_idps_returnees_hxl.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: South Sudan Humanitarian Needs Overview HNO 2020 (Excel)
  download_url: https://data.humdata.org/dataset/73f076d4-7bd1-41e7-83de-7d25ecbad789/resource/ef4a4e92-c8dd-4e31-a68a-11ef5a230b5e/download/20200110_ssd_pop_estimates_hc_idps_returnees.xlsx
  format: null
  id: resource_ef4a4e92
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20200110_SSD_Pop_Estimates_HC_IDPs_Returnees.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: South Sudan Humanitarian Needs Overview HNO 2020 (PDF)
  download_url: https://data.humdata.org/dataset/73f076d4-7bd1-41e7-83de-7d25ecbad789/resource/15c1755f-e64b-4d0f-83a0-5f47b562b0e5/download/ss_20191120_south_sudan_humanitarian_needs_overview_2020.pdf
  format: null
  id: resource_15c1755f
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ss_20191120_south_sudan_humanitarian_needs_overview_2020.pdf
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-ssd_unicefssd_humanitarianneedsoverview_2020
spatial:
  bbox: null
  centroid: null
  countries:
  - SSD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-12-31'
  start: '2020-01-01'
temporal_resolution: null
title: South Sudan Humanitarian Needs Overview HNO 2020
version: null
vulnerability: null
---
