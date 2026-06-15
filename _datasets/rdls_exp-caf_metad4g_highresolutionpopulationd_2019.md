---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook/Meta AI and Data for Good
    url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-caf
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-caf
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-caf
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-caf
dataset_id: rdls_exp-caf_metad4g_highresolutionpopulationd_2019
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in the Central African Republic: (1)
  Overall population density (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages
  15-24) (6) Elderly (ages 60+) (7) Women of reproductive age (ages 15-49). There
  is also a tiled version of this dataset that may be easier to use if you are interested
  in many countries.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-caf]'
details: "To reference this data, please use the following citation: Facebook Connectivity\
  \ Lab and Center for International Earth Science Information Network - CIESIN -\
  \ Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery\
  \ for HRSL \xC2\xA9 2016 DigitalGlobe. Accessed DAY MONTH YEAR.' Please note that\
  \ as of 2024, Meta's high resolution population density maps are no longer being\
  \ updated."
exposure:
- asset_type:
    description: High-resolution gridded population density estimates disaggregated
      by demographic groups (overall, women, men, children 0-5, youth 15-24, elderly
      60+, women of reproductive age 15-49)
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
  description: Machine learning algorithms identified building footprints from commercial
    satellite imagery across Central African Republic. Population estimates derived
    from publicly available census data and demographic statistics were spatially
    allocated to building locations using Columbia University's methodology, producing
    seven disaggregated population density grids at high spatial resolution for baseline
    demographic profiling.
  sources:
  - id: source_1
    license: null
    name: Facebook/Meta AI and Data for Good
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: Columbia University
    risk_data_type:
    - exposure
    type: model
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-caf
  rel: source
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://dataforgood.fb.com/docs/methodology-high-resolution-population-density-maps-demographic-estimates/
- author_names: null
  date_published: null
  doi: null
  id: reference_2
  name: Methodology documentation
  url: https://dataforgood.fb.com/docs/high-resolution-population-density-maps-demographic-estimates-documentation/
- author_names: null
  date_published: null
  doi: null
  id: reference_3
  name: Methodology documentation
  url: https://dataforgood.fb.com/docs/census-information-for-high-resolution-population-density-maps/
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Central African Republic: High Resolution Population Density Maps
    + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/ca5041cf-abc1-4c74-93a0-17ee3a924f3e/resource/a588e3df-f100-4aee-b27e-3bc52dd1a1b8/download/caf_general_2020_geotiff.zip
  format: zip
  id: resource_a588e3df
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: caf_general_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Central African Republic: High Resolution Population Density Maps
    + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/ca5041cf-abc1-4c74-93a0-17ee3a924f3e/resource/184e496a-076d-4097-8bd8-d16d353dc224/download/caf_general_2020_csv.zip
  format: zip
  id: resource_184e496a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: caf_general_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Central African Republic: High Resolution Population Density Maps
    + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/ca5041cf-abc1-4c74-93a0-17ee3a924f3e/resource/c374845c-b0fc-453d-9fde-39c4d64d692a/download/caf_children_under_five_2020_csv.zip
  format: zip
  id: resource_c374845c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: caf_children_under_five_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Central African Republic: High Resolution Population Density Maps
    + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/ca5041cf-abc1-4c74-93a0-17ee3a924f3e/resource/e54014fd-aa6f-4860-aec5-c05738963ee8/download/caf_children_under_five_2020_geotiff.zip
  format: zip
  id: resource_e54014fd
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: caf_children_under_five_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Central African Republic: High Resolution Population Density Maps
    + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/ca5041cf-abc1-4c74-93a0-17ee3a924f3e/resource/0f0c6400-2041-426c-ba7c-02551001b0ac/download/caf_elderly_60_plus_2020_csv.zip
  format: zip
  id: resource_0f0c6400
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: caf_elderly_60_plus_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Central African Republic: High Resolution Population Density Maps
    + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/ca5041cf-abc1-4c74-93a0-17ee3a924f3e/resource/91a8d526-741f-4605-a4d5-8e9190d51e14/download/caf_elderly_60_plus_2020_geotiff.zip
  format: zip
  id: resource_91a8d526
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: caf_elderly_60_plus_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Central African Republic: High Resolution Population Density Maps
    + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/ca5041cf-abc1-4c74-93a0-17ee3a924f3e/resource/dc67904d-7c91-46a4-afa4-ab18b22f33d2/download/caf_men_2020_csv.zip
  format: zip
  id: resource_dc67904d
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: caf_men_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Central African Republic: High Resolution Population Density Maps
    + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/ca5041cf-abc1-4c74-93a0-17ee3a924f3e/resource/617c8195-f3e9-41dd-acab-c0d938a85380/download/caf_men_2020_geotiff.zip
  format: zip
  id: resource_617c8195
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: caf_men_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Central African Republic: High Resolution Population Density Maps
    + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/ca5041cf-abc1-4c74-93a0-17ee3a924f3e/resource/3a5eb2c6-b4e6-45b2-98d9-424df5fe8707/download/caf_women_2020_csv.zip
  format: zip
  id: resource_3a5eb2c6
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: caf_women_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Central African Republic: High Resolution Population Density Maps
    + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/ca5041cf-abc1-4c74-93a0-17ee3a924f3e/resource/10f8b04c-d963-4d39-8a71-c2168872b96f/download/caf_women_2020_geotiff.zip
  format: zip
  id: resource_10f8b04c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: caf_women_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Central African Republic: High Resolution Population Density Maps
    + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/ca5041cf-abc1-4c74-93a0-17ee3a924f3e/resource/e6f55933-6d89-43c2-8f4e-4577c36e3d25/download/caf_women_of_reproductive_age_15_49_2020_csv.zip
  format: zip
  id: resource_e6f55933
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: caf_women_of_reproductive_age_15_49_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Central African Republic: High Resolution Population Density Maps
    + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/ca5041cf-abc1-4c74-93a0-17ee3a924f3e/resource/02d60035-4109-4341-810e-cface147ba05/download/caf_women_of_reproductive_age_15_49_2020_geotiff.zip
  format: zip
  id: resource_02d60035
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: caf_women_of_reproductive_age_15_49_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Central African Republic: High Resolution Population Density Maps
    + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/ca5041cf-abc1-4c74-93a0-17ee3a924f3e/resource/2a5e3062-3de9-4658-b9af-7da5286a0456/download/caf_youth_15_24_2020_csv.zip
  format: zip
  id: resource_2a5e3062
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: caf_youth_15_24_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Central African Republic: High Resolution Population Density Maps
    + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/ca5041cf-abc1-4c74-93a0-17ee3a924f3e/resource/819ac1dc-94d7-4098-b871-ae2c9d386dfc/download/caf_youth_15_24_2020_geotiff.zip
  format: zip
  id: resource_819ac1dc
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: caf_youth_15_24_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This file has information about the cloud cover percentage and capture
    data of the satellite images used.
  download_url: https://data.humdata.org/dataset/ca5041cf-abc1-4c74-93a0-17ee3a924f3e/resource/2e08f4fe-2f52-4435-b08c-2386858d3b8a/download/caf_dg_metadata.json.zip
  format: null
  id: resource_2e08f4fe
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: caf_dg_metadata.json.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-caf_metad4g_highresolutionpopulationd_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - CAF
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2022-10-21'
  start: '2019-05-20'
temporal_resolution: null
title: 'Central African Republic: High Resolution Population Density Maps + Demographic
  Estimates'
version: null
vulnerability: null
---
