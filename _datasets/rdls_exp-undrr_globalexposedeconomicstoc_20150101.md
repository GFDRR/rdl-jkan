---
attributions:
- entity:
    affiliation: null
    email: null
    name: United Nations Environment Programme (UNEP-GRID)
    url: https://data.humdata.org/dataset/exposed-economic-stock
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: World Agency of Planetary Monitoring and Earthquake Risk Reduction (WAPMERR)
    url: https://data.humdata.org/dataset/exposed-economic-stock
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: EU Joint Research Center (JRC)
    url: https://data.humdata.org/dataset/exposed-economic-stock
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Kokusai Kogyo
    url: https://data.humdata.org/dataset/exposed-economic-stock
  id: attribution_4
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: https://data.humdata.org/dataset/exposed-economic-stock
creator:
  affiliation: null
  email: null
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: https://data.humdata.org/dataset/exposed-economic-stock
dataset_id: rdls_exp-undrr_globalexposedeconomicstoc_20150101
description: 'The Global Exposure Database for GAR: A Global exposure database was
  developed for GAR15 by UNEP-GRID with close collaboration and inputs from WAPMERR
  (World Agency of Planetary Monitoring and Earthquake Risk Reduction), EU Joint Research
  Center (JRC), and Kokusai Kogyo. This database includes estimation on the economic
  value of the exposed assets, as well as their physical characteristics in urban
  and rural agglomerations. This information is key to assess the potential damages
  from different hazards to each of the exposed elements. The global exposure database
  is developed at 1km spatial resolution at coastal areas and at 5km spatial resolution
  everywhere else on the globe. It includes economic value, number of residents, and
  construction type of residential, commercial and industrial buildings, as well as
  hospitals and schools (De Bono et al., 2015).. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/exposed-economic-stock]'
details: This dataset was generated using other global datasets; it should not be
  used for local applications (such as land use planning). The main purpose of GAR
  2015 datasets is to broadly identify high risk areas at global level and for identification
  of areas where more detailed data should be collected. Some areas may be underestimated
  or overestimated. Given this analysis was conducted using global datasets, the resolution
  of which is not sufficient for in-situ planning, it should not be used for critical
  (like life saving) decisions. UNISDR and collaborators should in no case be liable
  for misuse or misinterpretation of the presented results. The designations employed
  and the presentation of material on the maps do not imply the expression of any
  opinion whatsoever on the part of UNISDR or the Secretariat of the United Nations
  concerning the legal status of any country, territory, city or area or of its authorities,
  or concerning the delimitation of its frontiers or boundaries. The designations
  employed and the presentation of material on the maps do not imply the expression
  of any opinion whatsoever on the part of UNISDR or the Secretariat of the United
  Nations concerning the legal status of any country, territory, city or area or of
  its authorities, or concerning the delimitation of its frontiers or boundaries.
  This analysis was conducted using global datasets, the resolution of which is not
  relevant for in-situ planning and should not be used for life and death decisions.
  UNISDR and collaborators should in no case be liable for misuse of the presented
  results.
exposure:
- asset_type:
    description: Economic value of building stock classified by type and location
      in urban and rural areas
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
      quantity_kind: currency
      unit: null
- asset_type:
    description: Gross domestic product (GDP) and capital stock distributed at 1km
      spatial resolution
    id: economic_indicator
    scheme: null
    title: null
    uri: null
  category: economic_indicator
  id: exposure_2
  metrics:
  - dimension: index
    id: metric_1
    measurement:
      quantity_kind: currency
      unit: null
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: The GAR15 global exposure database was developed using a top-down approach
    that transposed national-level socio-economic, building type, and capital stock
    statistics onto 1km and 5km spatial grids using geographic distribution of population
    and GDP as spatial proxies. The dataset integrates multi-source inputs from UNEP-GRID,
    WAPMERR, JRC, and Kokusai Kogyo to estimate economic value and physical characteristics
    of exposed assets in urban and rural agglomerations globally.
  sources:
  - id: source_1
    license: null
    name: United Nations Environment Programme (UNEP-GRID)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: World Agency of Planetary Monitoring and Earthquake Risk Reduction (WAPMERR)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_3
    license: null
    name: EU Joint Research Center (JRC)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_4
    license: null
    name: Kokusai Kogyo
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/exposed-economic-stock
  rel: source
loss: null
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
  description: Global exposed economic stock (Zipped shapefiles of exposed economic
    stock (329,227 kb).)
  download_url: https://data.humdata.org/dataset/1c9cf1eb-c20a-4a06-8309-9416464af746/resource/e321d56d-022e-4070-80ac-f7860646408d/download/gar-exp.zip
  format: null
  id: resource_e321d56d
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gar_exp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Global exposed economic stock (Data Dictionary)
  download_url: https://data.humdata.org/dataset/1c9cf1eb-c20a-4a06-8309-9416464af746/resource/bf90aaad-b438-4570-8550-1cd6314599d5/download/please-read-metadata-exposure2015.pdf
  format: null
  id: resource_bf90aaad
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PLEASE READ - Metadata-Exposure2015.pdf
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-undrr_globalexposedeconomicstoc_20150101
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
  end: null
  start: '2015-01-01'
temporal_resolution: null
title: Global exposed economic stock
version: null
vulnerability: null
---
