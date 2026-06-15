---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: CCCM Cluster Somalia
  url: https://data.humdata.org/dataset/cccm-somalia-idp-site-master-list-q2-2024
creator:
  affiliation: null
  email: null
  name: CCCM Cluster Somalia
  url: https://data.humdata.org/dataset/cccm-somalia-idp-site-master-list-q2-2024
dataset_id: rdls_el-som_cccmsom_idpsitemasterlist_2024
description: 'Households and population estinamtes in IDP site locations in Somalia
  as verified in the District wide site verification exercises across Somalia and
  supplemented by Detailed Site Assessment surveys where site verification coverage
  is not current.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/cccm-somalia-idp-site-master-list-q2-2024]'
details: null
exposure:
- asset_type:
    description: Internally displaced population residing in IDP sites across Somalia
      with household and individual counts
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
  description: IDP population data collected through direct site visits and community
    representative interviews, verified via district-wide site verification exercises
    and supplemented by Detailed Site Assessment surveys. GPS-referenced site locations
    enable spatial analysis of displacement patterns and population distribution across
    Somalia.
  sources:
  - id: source_1
    license: null
    name: CCCM Cluster Somalia
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/cccm-somalia-idp-site-master-list-q2-2024
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced population from flood-related displacement in
      Somalia
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
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia CCCM IDP Site Master List (IDP Site Master List - 4th Quarter
    2024.xlsx)
  download_url: https://data.humdata.org/dataset/5c334c3d-3b40-4819-ae8d-450f7e5fc104/resource/1519fb91-f1a8-4723-bdaa-0d6f5f768e1d/download/idp-site-master-list-4th-quarter-2024.xlsx
  format: null
  id: resource_1519fb91
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: IDP Site Master List - 4th Quarter 2024.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia CCCM IDP Site Master List (IDP Site Master List - 3rd Quarter
    2024.xlsx)
  download_url: https://data.humdata.org/dataset/5c334c3d-3b40-4819-ae8d-450f7e5fc104/resource/4e529083-9305-49e7-b679-931351f6e28d/download/idp-site-master-list-3rd-quarter-2024.xlsx
  format: null
  id: resource_4e529083
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: IDP Site Master List - 3rd Quarter 2024.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia CCCM IDP Site Master List (IDP Site Master List -2nd Quarter
    2024.xlsx)
  download_url: https://data.humdata.org/dataset/5c334c3d-3b40-4819-ae8d-450f7e5fc104/resource/1ad45641-8088-4506-85bf-434c7768c9af/download/idp-site-master-list-2nd-quarter-2024.xlsx
  format: null
  id: resource_1ad45641
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: IDP Site Master List -2nd Quarter 2024.xlsx
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-som_cccmsom_idpsitemasterlist_2024
spatial:
  bbox: null
  centroid: null
  countries:
  - SOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-12-31'
  start: '2024-04-01'
temporal_resolution: null
title: Somalia CCCM IDP Site Master List
version: null
vulnerability: null
---
