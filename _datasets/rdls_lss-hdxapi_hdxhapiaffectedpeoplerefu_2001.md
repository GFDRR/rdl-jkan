---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNHCR - The UN Refugee Agency
    url: https://data.humdata.org/dataset/hdx-hapi-refugees
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX Humanitarian API Data
  url: https://data.humdata.org/dataset/hdx-hapi-refugees
creator:
  affiliation: null
  email: null
  name: UNHCR - The UN Refugee Agency
  url: https://data.humdata.org/dataset/hdx-hapi-refugees
dataset_id: rdls_lss-hdxapi_hdxhapiaffectedpeoplerefu_2001
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
  dataset: https://data.humdata.org/dataset/hdx-hapi-refugees]'
details: HDX HAPI is refreshed daily, but the source datasets may have different update
  schedules. Please refer to the source datasets for each subcategory to verify their
  specific update frequency.
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: UNHCR registry data on refugee and person of concern populations aggregated
    through the HDX Humanitarian API (HDX HAPI) to provide standardized humanitarian
    indicators. Data spans 2000-2024 with disaggregation by origin/asylum location,
    demographics, and population group classification to support humanitarian decision-making.
  sources:
  - id: source_1
    license: null
    name: UNHCR - The UN Refugee Agency
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/hdx-hapi-refugees
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Refugee and person of concern populations displaced across origin
      and asylum locations
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
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
purpose: Registry
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Refugees and Persons of Concern data (2020-2024) from HDX HAPI, please
    see the documentation for more information
  download_url: https://data.humdata.org/dataset/40fe624f-bd3e-4a25-b26c-e1528ca98d93/resource/518e64d0-50f6-4cd6-9372-dc809545ae1c/download/hdx_hapi_refugees_global_2020_2024.csv
  format: null
  id: resource_518e64d0
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Global Affected People: Refugees & Persons of Concern (2020-2024)'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Refugees and Persons of Concern data (2015-2019) from HDX HAPI, please
    see the documentation for more information
  download_url: https://data.humdata.org/dataset/40fe624f-bd3e-4a25-b26c-e1528ca98d93/resource/d32bba02-31b5-409c-921a-a10905caef30/download/hdx_hapi_refugees_global_2015_2019.csv
  format: null
  id: resource_d32bba02
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Global Affected People: Refugees & Persons of Concern (2015-2019)'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Refugees and Persons of Concern data (2010-2014) from HDX HAPI, please
    see the documentation for more information
  download_url: https://data.humdata.org/dataset/40fe624f-bd3e-4a25-b26c-e1528ca98d93/resource/fd4e9e64-cf3b-42f2-9906-33f9e976d7ef/download/hdx_hapi_refugees_global_2010_2014.csv
  format: null
  id: resource_fd4e9e64
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Global Affected People: Refugees & Persons of Concern (2010-2014)'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Refugees and Persons of Concern data (2005-2009) from HDX HAPI, please
    see the documentation for more information
  download_url: https://data.humdata.org/dataset/40fe624f-bd3e-4a25-b26c-e1528ca98d93/resource/afc2fc6e-eae3-4c21-b335-6e720b1b1465/download/hdx_hapi_refugees_global_2005_2009.csv
  format: null
  id: resource_afc2fc6e
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Global Affected People: Refugees & Persons of Concern (2005-2009)'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Refugees and Persons of Concern data (2000-2004) from HDX HAPI, please
    see the documentation for more information
  download_url: https://data.humdata.org/dataset/40fe624f-bd3e-4a25-b26c-e1528ca98d93/resource/8be74dcd-b229-452d-89c5-03337138d807/download/hdx_hapi_refugees_global_2000_2004.csv
  format: null
  id: resource_8be74dcd
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Global Affected People: Refugees & Persons of Concern (2000-2004)'
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-hdxapi_hdxhapiaffectedpeoplerefu_2001
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
  end: '2024-12-31'
  start: '2001-01-01'
temporal_resolution: null
title: 'HDX HAPI - Affected People: Refugees & Persons of Concern'
version: null
vulnerability: null
---
