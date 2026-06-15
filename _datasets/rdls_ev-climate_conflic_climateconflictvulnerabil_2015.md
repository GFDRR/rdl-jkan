---
attributions:
- entity:
    affiliation: null
    email: null
    name: University of the Bundeswehr Munich
    url: https://data.humdata.org/dataset/climate-conflict-vulnerability-index
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Potsdam Institute for Climate Impact Research
    url: https://data.humdata.org/dataset/climate-conflict-vulnerability-index
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Climate-Conflict-Vulnerability Index
  url: https://data.humdata.org/dataset/climate-conflict-vulnerability-index
creator:
  affiliation: null
  email: null
  name: Climate-Conflict-Vulnerability Index
  url: https://data.humdata.org/dataset/climate-conflict-vulnerability-index
dataset_id: rdls_ev-climate_conflic_climateconflictvulnerabil_2015
description: 'The Climate-Conflict-Vulnerability Index (CCVI) maps current global
  risks by integrating climate and conflict hazards with local vulnerabilities. The
  index comprises a harmonized set of data layers and a transparent scoring methodology
  to make regions globally comparable. The data is updated quarterly and gridded to
  0.5 degrees (ca. 55km by 55km at the equator). The CCVI metrics are organized hierarchically
  in three pillars - climate, conflict and vulnerability. Each pillar is based on
  indicators from publicly available sources, which are further grouped into dimensions.
  Following the IPCC definition, risk metrics are computed as a function of hazards,
  exposure and vulnerability. There are two sets of resources. One smaller set contains
  only the data from the latest quarter in tsv format, while the full dataset includes
  historical time series and reference data in parquet format.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/climate-conflict-vulnerability-index]'
details: Please refer to the [CCVI Technical Documentation](https://climate-conflict.org/www/latest-data/docs/)
  for the full methodology, including limitations.
exposure:
- asset_type:
    description: Global population distribution at 0.5-degree grid resolution
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
- asset_type:
    description: Economic and development indicators integrated into vulnerability
      assessment
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
      quantity_kind: index
      unit: null
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: The CCVI integrates publicly available climate, conflict, and vulnerability
    data layers harmonized to a 0.5-degree global grid. Climate and conflict hazard
    indicators are combined with socioeconomic vulnerability dimensions using a transparent
    hierarchical scoring methodology to produce a composite index updated quarterly.
    The index enables global comparability of climate-conflict risk across regions.
  sources:
  - id: source_1
    license: null
    name: University of the Bundeswehr Munich
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: Potsdam Institute for Climate Impact Research
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/climate-conflict-vulnerability-index
  rel: source
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Dataset covers only the latest quarter. See LAST_QTR_README.md for
    file structure.
  download_url: https://data.humdata.org/dataset/664098ac-5745-46b3-89f9-70e9daed4c6d/resource/9dfd5db5-6df8-4f50-bfea-a5f258fefadf/download/ccvi-latest.tsv
  format: TSV
  id: resource_9dfd5db5
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: last_qtr_ccvi-latest.tsv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Dataset covers only the latest quarter. See LAST_QTR_README.md for
    file structure.
  download_url: https://data.humdata.org/dataset/664098ac-5745-46b3-89f9-70e9daed4c6d/resource/3e7381ee-a8cd-4ba8-b846-1b87fd341193/download/ccvi-structure.tsv
  format: TSV
  id: resource_3e7381ee
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: last_qtr_ccvi-structure.tsv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Dataset covers only the latest quarter. See LAST_QTR_README.md for
    file structure.
  download_url: https://data.humdata.org/dataset/664098ac-5745-46b3-89f9-70e9daed4c6d/resource/8d947ce1-8cb9-48b5-86fa-c14c922e4dc1/download/ccvi-data-sources.tsv
  format: TSV
  id: resource_8d947ce1
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: last_qtr_ccvi-data-sources.tsv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Dataset covers only the latest quarter. See LAST_QTR_README.md for
    file structure.
  download_url: https://data.humdata.org/dataset/664098ac-5745-46b3-89f9-70e9daed4c6d/resource/e51ebc79-9e36-4a1e-892e-7de6dafe06b3/download/ccvi-data-recency.tsv
  format: TSV
  id: resource_e51ebc79
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: last_qtr_ccvi-data-recency.tsv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Climate Conflict Vulnerability Index (File structures of last quarter
    dataset.)
  download_url: https://data.humdata.org/dataset/664098ac-5745-46b3-89f9-70e9daed4c6d/resource/1ca78b26-2f13-42d1-908f-5c5a5877fe73/download/readme.md
  format: null
  id: resource_1ca78b26
  media_type: text/plain
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: LAST_QTR_README.md
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Full dataset including historical time series and reference data. See
    FULL_README.md for file structure.
  download_url: https://data.humdata.org/dataset/664098ac-5745-46b3-89f9-70e9daed4c6d/resource/838bfcf9-7f6b-4ded-8e61-93411a365048/download/ccvi_scores.parquet
  format: null
  id: resource_838bfcf9
  media_type: application/vnd.apache.parquet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ccvi_scores.parquet
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Full dataset including historical time series and reference data. See
    FULL_README.md for file structure.
  download_url: https://data.humdata.org/dataset/664098ac-5745-46b3-89f9-70e9daed4c6d/resource/0adb6650-0dd5-45d0-95d4-fc1b9a9df163/download/index-full.parquet
  format: null
  id: resource_0adb6650
  media_type: application/vnd.apache.parquet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: index-full.parquet
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Full dataset including historical time series and reference data. See
    FULL_README.md for file structure.
  download_url: https://data.humdata.org/dataset/664098ac-5745-46b3-89f9-70e9daed4c6d/resource/6f4c03b8-f8a9-4b7b-9c8e-814a13a77368/download/exposure_layers.parquet
  format: null
  id: resource_6f4c03b8
  media_type: application/vnd.apache.parquet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: exposure_layers.parquet
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Full dataset including historical time series and reference data. See
    FULL_README.md for file structure.
  download_url: https://data.humdata.org/dataset/664098ac-5745-46b3-89f9-70e9daed4c6d/resource/b39e4281-b7ee-4a97-ab8c-6d2f1b889943/download/base_grid.parquet
  format: null
  id: resource_b39e4281
  media_type: application/vnd.apache.parquet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: base_grid.parquet
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Full dataset including historical time series and reference data. See
    FULL_README.md for file structure.
  download_url: https://data.humdata.org/dataset/664098ac-5745-46b3-89f9-70e9daed4c6d/resource/67120601-a6f6-4867-87aa-71bb8e67f5c3/download/vul_country_raw.parquet
  format: null
  id: resource_67120601
  media_type: application/vnd.apache.parquet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: vul_country_raw.parquet
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Full dataset including historical time series and reference data. See
    FULL_README.md for file structure.
  download_url: https://data.humdata.org/dataset/664098ac-5745-46b3-89f9-70e9daed4c6d/resource/ad4033c2-7b24-4719-a97f-947d1163058f/download/data_recency.parquet
  format: null
  id: resource_ad4033c2
  media_type: application/vnd.apache.parquet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: data_recency.parquet
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Full dataset including historical time series and reference data. See
    FULL_README.md for file structure.
  download_url: https://data.humdata.org/dataset/664098ac-5745-46b3-89f9-70e9daed4c6d/resource/08de0c55-46ea-4e5a-8da6-c98210d960ab/download/ccvi-structure.tsv
  format: TSV
  id: resource_08de0c55
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ccvi-structure.tsv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Full dataset including historical time series and reference data. See
    FULL_README.md for file structure.
  download_url: https://data.humdata.org/dataset/664098ac-5745-46b3-89f9-70e9daed4c6d/resource/20b445b7-a540-4036-813f-d0f43da1fef9/download/ccvi-data-sources.tsv
  format: TSV
  id: resource_20b445b7
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ccvi-data-sources.tsv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Climate Conflict Vulnerability Index (File structures of full dataset.)
  download_url: https://data.humdata.org/dataset/664098ac-5745-46b3-89f9-70e9daed4c6d/resource/bd10c8a4-d39e-456c-a9d8-ce9f745b723b/download/readme.md
  format: null
  id: resource_bd10c8a4
  media_type: text/plain
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FULL_README.md
risk_data_type:
- exposure
- vulnerability
schema: rdls-10
slug: rdls_ev-climate_conflic_climateconflictvulnerabil_2015
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
  end: '2025-09-30'
  start: '2015-01-01'
temporal_resolution: null
title: Climate Conflict Vulnerability Index
version: null
vulnerability: null
---
