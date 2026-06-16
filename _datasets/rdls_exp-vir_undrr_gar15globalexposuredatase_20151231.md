---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNEP-GRID
    url: https://data.humdata.org/dataset/gar15-global-exposure-dataset-for-virgin-islands-u-s
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WAPMERR (World Agency of Planetary Monitoring and Earthquake Risk Reduction)
    url: https://data.humdata.org/dataset/gar15-global-exposure-dataset-for-virgin-islands-u-s
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: EU Joint Research Center (JRC)
    url: https://data.humdata.org/dataset/gar15-global-exposure-dataset-for-virgin-islands-u-s
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Kokusai Kogyo
    url: https://data.humdata.org/dataset/gar15-global-exposure-dataset-for-virgin-islands-u-s
  id: attribution_4
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: https://data.humdata.org/dataset/gar15-global-exposure-dataset-for-virgin-islands-u-s
creator:
  affiliation: null
  email: null
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: https://data.humdata.org/dataset/gar15-global-exposure-dataset-for-virgin-islands-u-s
dataset_id: rdls_exp-vir_undrr_gar15globalexposuredatase_20151231
description: 'The GAR15 global exposure database is based on a top-down approach where
  statistical information including socio-economic, building type, and capital stock
  at a national level are transposed onto the grids of 5x5 or 1x1 using geographic
  distribution of population data and gross domestic product (GDP) as proxies.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/gar15-global-exposure-dataset-for-virgin-islands-u-s]'
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
    description: Economic value of building stock estimated using national capital
      stock statistics disaggregated to grid cells using GDP and population proxies
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
    description: Capital stock estimates at grid level derived from national socio-economic
      statistics and GDP distribution
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
    in which national-level socio-economic statistics, building type distributions,
    and capital stock data were disaggregated to 5x5 or 1x1 km grid cells using gridded
    population and GDP as spatial proxies. The database was produced by UNEP-GRID
    in collaboration with WAPMERR, EU JRC, and Kokusai Kogyo for the 2015 Global Assessment
    Report on Disaster Risk Reduction. The resulting dataset provides spatially explicit
    estimates of economic exposure for use in probabilistic disaster risk assessments.
  sources:
  - id: source_1
    license: null
    name: UNEP-GRID
    risk_data_type:
    - exposure
    type: model
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
- href: https://data.humdata.org/dataset/gar15-global-exposure-dataset-for-virgin-islands-u-s
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
  description: GAR15 Global Exposure Dataset for Virgin Islands (U.S.).zip
  download_url: https://data.humdata.org/dataset/028adb2b-aae4-4cdf-8946-dd64d499e0cb/resource/859d8a48-5621-49d0-9870-5c73ecbd9a73/download/vir.zip
  format: null
  id: resource_859d8a48
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GAR15 Global Exposure Dataset for Virgin Islands (U.S.).zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-vir_undrr_gar15globalexposuredatase_20151231
spatial:
  bbox: null
  centroid: null
  countries:
  - VIR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-12-31'
temporal_resolution: null
title: GAR15 Global Exposure Dataset for Virgin Islands (U.S.)
version: null
vulnerability: null
---
