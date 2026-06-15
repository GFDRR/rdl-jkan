---
attributions:
- entity:
    affiliation: null
    email: null
    name: Water Point Data Exchange (WPdx)
    url: https://data.humdata.org/dataset/wpdx_tza
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Water Point Data Exchange
  url: https://data.humdata.org/dataset/wpdx_tza
creator:
  affiliation: null
  email: null
  name: Water Point Data Exchange
  url: https://data.humdata.org/dataset/wpdx_tza
dataset_id: rdls_exp-tza_wpdx_tza_1978
description: 'WPdx is a platform to compile crowdsourced data focused on rural water
  points (wells, springs, tapstands) with contributions from governments, NGOs, and
  researchers. Shared data is cleaned and harmonized using the WPdx Data Standard
  to create a robust analysis-ready dataset. There are two primary datasets available
  from WPdx. The first is WPdx-Basic, which includes all records shared with the platform.
  The second, WPdx-Plus is a subset of the Basic dataset which focuses on countries
  where district and/or national data is available and undergoes additional cleaning.
  WPdx-Plus is used as an input to the WPdx Decision Support tools and is the basis
  for the datasets posted here. The decision support tools provide insights on rural
  basic water service access and recommendations regarding prioritized water point
  repair, highlight areas with apparent service gaps, and identify water points which
  are at high risk of failure. For each country where WPdx data is available, there
  are two datasets available for download are described below. The wpdx_adm_region_analysis
  file provides an overview of the population served, unserved and uncharted for each
  available administrative level. The file also includes a data quality analysis based
  on water point record age. The wpdx_water_points file provides water point level
  details for each point shared with WPdx including all the WPdx data standard parameters
  plus results from the WPdx Rehab Priority, Service Gap/New Construction and Status
  Prediction analyses. A data dictionary describing each parameter included in each
  file is available in the Data and Resources section. To share data with the WPdx
  platform, please visit (www.waterpointdata.org/share-data) and/or reach out to info@waterpointdata.org.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/wpdx_tza]'
details: The dataset represents the best available information shared with the WPdx
  platform.
exposure:
- asset_type:
    description: Rural water point infrastructure (wells, springs, tapstands) with
      operational status, technology type, and management characteristics
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Local and assigned population served by water points, including rural
      population with and without basic water access
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_2
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Water point locations and attributes were collected through crowdsourced
    contributions from multiple organizations and harmonized using the WPdx Data Standard.
    Data was cleaned, geocoded, and integrated with administrative boundaries and
    population estimates to create a national-scale infrastructure inventory with
    derived metrics on service coverage, functionality status, and population access
    to basic water services.
  sources:
  - id: source_1
    license: null
    name: Water Point Data Exchange (WPdx)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/wpdx_tza
  rel: source
loss:
  losses: []
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
  description: Tanzania - Water Point Data Exchange (TZA) (Water Point Details for
    TZA)
  download_url: https://data.humdata.org/dataset/dd154b0d-8d0e-421e-8254-e37e38348167/resource/8d998957-fc14-48cc-942e-e3bd0d2fdfd1/download/wpdx_enhanced.csv
  format: null
  id: resource_8d998957
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: wpdx_water_points_tza
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Tanzania - Water Point Data Exchange (TZA) (Administrative Region Analysis
    for TZA)
  download_url: https://data.humdata.org/dataset/dd154b0d-8d0e-421e-8254-e37e38348167/resource/54eebd90-81fb-41c0-9ddd-ccfbd9420237/download/adm_analysis.csv
  format: null
  id: resource_54eebd90
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: wpdx_adm_region_analysis_tza
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-tza_wpdx_tza_1978
spatial:
  bbox: null
  centroid: null
  countries:
  - TZA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-05-10'
  start: '1978-10-27'
temporal_resolution: null
title: Tanzania - Water Point Data Exchange (TZA)
version: null
vulnerability: null
---
