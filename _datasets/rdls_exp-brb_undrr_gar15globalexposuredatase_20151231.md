---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNEP-GRID
    url: https://data.humdata.org/dataset/gar15-global-exposure-dataset-for-barbados
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WAPMERR (World Agency of Planetary Monitoring and Earthquake Risk Reduction)
    url: https://data.humdata.org/dataset/gar15-global-exposure-dataset-for-barbados
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: EU Joint Research Center (JRC)
    url: https://data.humdata.org/dataset/gar15-global-exposure-dataset-for-barbados
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Kokusai Kogyo
    url: https://data.humdata.org/dataset/gar15-global-exposure-dataset-for-barbados
  id: attribution_4
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: https://data.humdata.org/dataset/gar15-global-exposure-dataset-for-barbados
creator:
  affiliation: null
  email: null
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: https://data.humdata.org/dataset/gar15-global-exposure-dataset-for-barbados
dataset_id: rdls_exp-brb_undrr_gar15globalexposuredatase_20151231
description: 'The GAR15 global exposure database is based on a top-down approach where
  statistical information including socio-economic, building type, and capital stock
  at a national level are transposed onto the grids of 5x5 or 1x1 using geographic
  distribution of population data and gross domestic product (GDP) as proxies.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/gar15-global-exposure-dataset-for-barbados]'
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
  or concerning the delimitation of its frontiers or boundaries. Please refer to the
  'PLEASE READ - Metadata-Exposure2015.pdf' file included in the zipped shapefile
  archive for additional important information and metadata.
exposure:
- asset_type:
    description: Economic value of building stock classified by type and distributed
      spatially at 5x5 km and 1x1 km grid resolution
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
    description: Gridded population distribution used as proxy for spatial allocation
      of socio-economic assets
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
- asset_type:
    description: Gross domestic product (GDP) distributed spatially to represent economic
      capital stock
    id: economic_indicator
    scheme: null
    title: null
    uri: null
  category: economic_indicator
  id: exposure_3
  metrics:
  - dimension: index
    id: metric_1
    measurement:
      quantity_kind: currency
      unit: null
hazard: null
license: CC-BY-4.0
lineage:
  description: National-level socio-economic and building stock statistics were transposed
    onto 5x5 km and 1x1 km gridded spatial frameworks using gridded population distribution
    and GDP as geographic proxies. The dataset represents the spatial distribution
    of economic capital and population exposure for Barbados developed under the Global
    Assessment Report on Disaster Risk Reduction (GAR15) framework.
  sources:
  - id: source_1
    license: null
    name: UNEP-GRID
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: WAPMERR (World Agency of Planetary Monitoring and Earthquake Risk Reduction)
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
- href: https://data.humdata.org/dataset/gar15-global-exposure-dataset-for-barbados
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
  description: GAR15 Global Exposure Dataset for Barbados.zip
  download_url: https://data.humdata.org/dataset/7f04ea35-cdfe-4114-9ac3-58bebf6103df/resource/756ecded-6c24-42ec-9c7e-ce4dae638c5e/download/brb.zip
  format: null
  id: resource_756ecded
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GAR15 Global Exposure Dataset for Barbados.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-brb_undrr_gar15globalexposuredatase_20151231
spatial:
  bbox: null
  centroid: null
  countries:
  - BRB
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-12-31'
temporal_resolution: null
title: GAR15 Global Exposure Dataset for Barbados
version: null
vulnerability: null
---
