---
attributions:
- entity:
    affiliation: null
    email: null
    name: HDX Humanitarian API (HDX HAPI)
    url: https://data.humdata.org/dataset/hdx-hapi-population
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX Humanitarian API Data
  url: https://data.humdata.org/dataset/hdx-hapi-population
creator:
  affiliation: null
  email: null
  name: HDX Humanitarian API Data
  url: https://data.humdata.org/dataset/hdx-hapi-population
dataset_id: rdls_exp-hdxapi_hdxhapigeographyinfrastru_2001
description: 'This dataset contains data obtained from the HDX Humanitarian API (HDX
  HAPI), which provides standardized humanitarian indicators designed for seamless
  interoperability from multiple sources. The data facilitates automated workflows
  and visualizations to support humanitarian decision making. For more information,
  please see the HDX HAPI landing page and documentation . Warnings typically indicate
  corrections have been made to the data or show things to look out for. Rows with
  only warnings are considered complete, and are made available via the API. Errors
  usually mean that the data is incomplete or unusable. Rows with any errors are not
  present in the API but are included here for transparency.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/hdx-hapi-population]'
details: This dataset is refreshed daily, but the source datasets have different update
  schedules. Please refer to the [source datasets](https://data.humdata.org/dataset/?dataseries_name=COD+-+Subnational+Population+Statistics)
  to verify their specific update frequency.
exposure:
- asset_type:
    description: Baseline population disaggregated by administrative level, gender,
      and age range from multiple sources
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
  description: Baseline population data aggregated from multiple sources via the HDX
    Humanitarian API, standardized and disaggregated by administrative level (admin1/admin2),
    gender, and age range to support humanitarian needs assessment and planning workflows.
  sources:
  - id: source_1
    license: null
    name: HDX Humanitarian API (HDX HAPI)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/hdx-hapi-population
  rel: source
loss:
  losses: []
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
  description: Baseline Population data from HDX HAPI for HRP countries, please see
    the documentation for more information
  download_url: https://data.humdata.org/dataset/9b2e1d5b-0d0b-49a7-9668-c8f5e2ee9081/resource/7c19c43f-c9ee-4039-a0cd-99b3914eff1b/download/hdx_hapi_population_global_hrp.csv
  format: null
  id: resource_7c19c43f
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Global Geography & Infrastructure: Baseline Population (HRP countries)'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Baseline Population data from HDX HAPI for non-HRP countries, please
    see the documentation for more information
  download_url: https://data.humdata.org/dataset/9b2e1d5b-0d0b-49a7-9668-c8f5e2ee9081/resource/dc73bc7d-5487-45a7-b614-bd17dec75569/download/hdx_hapi_population_global_non_hrp.csv
  format: null
  id: resource_dc73bc7d
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Global Geography & Infrastructure: Baseline Population (Non-HRP countries)'
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-hdxapi_hdxhapigeographyinfrastru_2001
spatial:
  bbox: null
  centroid: null
  countries:
  - COD
  - CPV
  - FSM
  - IRN
  - IRQ
  - MAF
  - MHL
  - PSE
  - STP
  - SWZ
  - SXM
  - TKL
  - TLS
  - VEN
  - VIR
  - VNM
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-12-31'
  start: '2001-01-01'
temporal_resolution: null
title: 'HDX HAPI - Geography & Infrastructure: Baseline Population'
version: null
vulnerability: null
---
