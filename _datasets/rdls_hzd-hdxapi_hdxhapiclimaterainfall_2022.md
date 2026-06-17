---
attributions:
- entity:
    affiliation: null
    email: null
    name: Climate Hazards Center UC Santa Barbara
    url: https://data.humdata.org/dataset/hdx-hapi-rainfall
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: World Food Programme (WFP)
    url: https://data.humdata.org/dataset/hdx-hapi-rainfall
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX Humanitarian API Data
  url: https://data.humdata.org/dataset/hdx-hapi-rainfall
creator:
  affiliation: null
  email: null
  name: Climate Hazards Center UC Santa Barbara & WFP
  url: https://data.humdata.org/dataset/hdx-hapi-rainfall
dataset_id: rdls_hzd-hdxapi_hdxhapiclimaterainfall_2022
description: 'This dataset contains data obtained from the HDX Humanitarian API (HDX
  HAPI), which provides standardized humanitarian indicators designed for seamless
  interoperability from multiple sources. The data facilitates automated workflows
  and visualizations to support humanitarian decision making. For more information,
  please see the HDX HAPI landing page and documentation . Warnings typically indicate
  corrections have been made to the data or show things to look out for. Rows with
  only warnings are considered complete, and are made available via the API. Errors
  usually mean that the data is incomplete or unusable. Rows with any errors are not
  present in the API but are included here for transparency. Note that this dataset
  only contains admin one data for non HRP/GHO countries. For all other countries
  both admin one and two are present (where available). For the time being only the
  current year of rainfall data is included due to the size of the data. For the full
  set of data, please visit the source datasets .. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/hdx-hapi-rainfall]'
details: This dataset is refreshed every week, but the source datasets may have different
  update schedules. Please refer to the [source datasets](https://data.humdata.org/dataset/?dataseries_name=WFP+-+Rainfall+Indicators+at+Subnational+Level)
  to verify their specific update frequency.
exposure: []
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: rainfall:mm
      process: meteorological_drought
      trigger: null
      type: drought
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: drought
license: CC-BY-4.0
lineage:
  description: Rainfall observations from Climate Hazards Center UC Santa Barbara
    are aggregated by administrative boundaries and time periods. Long-term average
    rainfall is calculated from reference periods, and rainfall anomalies are computed
    as percentage deviations from the long-term mean. Data is standardized through
    the HDX HAPI framework for interoperable humanitarian climate monitoring.
  sources:
  - id: source_1
    license: null
    name: Climate Hazards Center UC Santa Barbara
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: World Food Programme (WFP)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/hdx-hapi-rainfall
  rel: source
loss: null
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
  description: Rainfall data (1 year(s) ago) from HDX HAPI, please see the documentation
    for more information
  download_url: https://data.humdata.org/dataset/5a97067f-52d8-49fe-8965-48dcdba2d037/resource/d6259d29-ccb6-48b5-aa18-0359e0b344e3/download/hdx_hapi_rainfall_global_1yr.csv
  format: null
  id: resource_d6259d29
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Global Climate: Rainfall (1 year(s) ago)'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Rainfall data (2 year(s) ago) from HDX HAPI, please see the documentation
    for more information
  download_url: https://data.humdata.org/dataset/5a97067f-52d8-49fe-8965-48dcdba2d037/resource/dcf676ba-e1cb-49ec-93f8-9f850b65babd/download/hdx_hapi_rainfall_global_2yr.csv
  format: null
  id: resource_dcf676ba
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Global Climate: Rainfall (2 year(s) ago)'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Rainfall data (3 year(s) ago) from HDX HAPI, please see the documentation
    for more information
  download_url: https://data.humdata.org/dataset/5a97067f-52d8-49fe-8965-48dcdba2d037/resource/5cf4558d-7a6c-4217-bea8-c3dfd6e2a856/download/hdx_hapi_rainfall_global_3yr.csv
  format: null
  id: resource_5cf4558d
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Global Climate: Rainfall (3 year(s) ago)'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Rainfall data (4 year(s) ago) from HDX HAPI, please see the documentation
    for more information
  download_url: https://data.humdata.org/dataset/5a97067f-52d8-49fe-8965-48dcdba2d037/resource/376a3021-7d66-4970-a684-c22867f38213/download/hdx_hapi_rainfall_global_4yr.csv
  format: null
  id: resource_376a3021
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Global Climate: Rainfall (4 year(s) ago)'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Rainfall data (5 year(s) ago) from HDX HAPI, please see the documentation
    for more information
  download_url: https://data.humdata.org/dataset/5a97067f-52d8-49fe-8965-48dcdba2d037/resource/46ab6b4f-0af3-4e3a-835c-18daedbc5bb6/download/hdx_hapi_rainfall_global_5yr.csv
  format: null
  id: resource_46ab6b4f
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Global Climate: Rainfall (5 year(s) ago)'
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-hdxapi_hdxhapiclimaterainfall_2022
spatial:
  bbox: null
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-31'
  start: '2022-01-01'
temporal_resolution: null
title: 'HDX HAPI - Climate: Rainfall'
version: null
vulnerability: null
---
