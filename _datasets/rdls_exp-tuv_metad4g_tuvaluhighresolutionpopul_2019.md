---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook (Meta)
    url: https://data.humdata.org/dataset/tuvalu-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/tuvalu-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/tuvalu-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/tuvalu-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-tuv_metad4g_tuvaluhighresolutionpopul_2019
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Tuvalu: (1) Overall population density
  (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly (ages
  60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/tuvalu-high-resolution-population-density-maps-demographic-estimates]'
details: "To reference this data, please use the following citation: Facebook Connectivity\
  \ Lab and Center for International Earth Science Information Network - CIESIN -\
  \ Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery\
  \ for HRSL \xC2\xA9 2016 DigitalGlobe. Accessed DAY MONTH YEAR.' Please note that\
  \ as of 2024, Meta's high resolution population density maps are no longer being\
  \ updated."
exposure:
- asset_type:
    description: High-resolution gridded population density estimates for overall
      population and demographic subgroups (women, men, children 0-5, youth 15-24,
      elderly 60+, women of reproductive age 15-49)
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
license: CC-BY-4.0
lineage:
  description: Machine learning algorithms identified building footprints from commercial
    satellite imagery across Tuvalu. Population estimates derived from publicly available
    census data and demographic statistics were spatially allocated to building locations
    using a methodology developed in partnership with Columbia University, producing
    high-resolution gridded population density maps for seven demographic categories
    at the national scale.
  sources:
  - id: source_1
    license: null
    name: Facebook (Meta)
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
- href: https://data.humdata.org/dataset/tuvalu-high-resolution-population-density-maps-demographic-estimates
  rel: source
loss: null
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
  description: 'Tuvalu: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/4add55d4-62f4-43a4-b0c8-5bd039d00b41/resource/bda78f9a-d965-402f-bff5-426916da5bc0/download/tuv_children_under_five_2020_csv.zip
  format: zip
  id: resource_bda78f9a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tuv_children_under_five_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Tuvalu: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/4add55d4-62f4-43a4-b0c8-5bd039d00b41/resource/9e013939-2bf5-4f66-992f-c6310f952f08/download/tuv_children_under_five_2020_geotiff.zip
  format: zip
  id: resource_9e013939
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tuv_children_under_five_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Tuvalu: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/4add55d4-62f4-43a4-b0c8-5bd039d00b41/resource/e9c857f2-62d0-46b3-bd15-98748f12222d/download/tuv_elderly_60_plus_2020_csv.zip
  format: zip
  id: resource_e9c857f2
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tuv_elderly_60_plus_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Tuvalu: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/4add55d4-62f4-43a4-b0c8-5bd039d00b41/resource/45a5005a-1945-42a8-81e1-94b249ab1fff/download/tuv_elderly_60_plus_2020_geotiff.zip
  format: zip
  id: resource_45a5005a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tuv_elderly_60_plus_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Tuvalu: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/4add55d4-62f4-43a4-b0c8-5bd039d00b41/resource/262ef39b-6d8b-4d4e-abb2-1677a6bfadd0/download/tuv_men_2020_csv.zip
  format: zip
  id: resource_262ef39b
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tuv_men_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Tuvalu: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/4add55d4-62f4-43a4-b0c8-5bd039d00b41/resource/4d2814ff-891f-4694-b844-52c6829f700d/download/tuv_men_2020_geotiff.zip
  format: zip
  id: resource_4d2814ff
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tuv_men_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Tuvalu: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/4add55d4-62f4-43a4-b0c8-5bd039d00b41/resource/12cdf16b-cf28-4a83-b1bf-839f76d1d51b/download/tuv_women_2020_csv.zip
  format: zip
  id: resource_12cdf16b
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tuv_women_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Tuvalu: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/4add55d4-62f4-43a4-b0c8-5bd039d00b41/resource/c41ab07e-c408-4e6a-909c-b22bb24275a7/download/tuv_women_2020_geotiff.zip
  format: zip
  id: resource_c41ab07e
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tuv_women_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Tuvalu: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/4add55d4-62f4-43a4-b0c8-5bd039d00b41/resource/d2b54133-8fde-40ad-b922-1a3128fc75e3/download/tuv_women_of_reproductive_age_15_49_2020_csv.zip
  format: zip
  id: resource_d2b54133
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tuv_women_of_reproductive_age_15_49_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Tuvalu: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/4add55d4-62f4-43a4-b0c8-5bd039d00b41/resource/5414a33d-637d-4e32-9611-70beb6813443/download/tuv_women_of_reproductive_age_15_49_2020_geotiff.zip
  format: zip
  id: resource_5414a33d
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tuv_women_of_reproductive_age_15_49_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Tuvalu: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/4add55d4-62f4-43a4-b0c8-5bd039d00b41/resource/4f9b9c68-bfa4-4965-bcf8-588afab7db13/download/tuv_youth_15_24_2020_csv.zip
  format: zip
  id: resource_4f9b9c68
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tuv_youth_15_24_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Tuvalu: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/4add55d4-62f4-43a4-b0c8-5bd039d00b41/resource/a55dd5e2-5e1a-4750-9005-7b4b98656dca/download/tuv_youth_15_24_2020_geotiff.zip
  format: zip
  id: resource_a55dd5e2
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tuv_youth_15_24_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Tuvalu: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/4add55d4-62f4-43a4-b0c8-5bd039d00b41/resource/e39add10-804f-4b8c-af1e-a344d72c1426/download/tuv_general_2020_geotiff.zip
  format: zip
  id: resource_e39add10
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tuv_general_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Tuvalu: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/4add55d4-62f4-43a4-b0c8-5bd039d00b41/resource/46469723-7317-4031-8eba-d23c6334c249/download/tuv_general_2020_csv.zip
  format: zip
  id: resource_46469723
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tuv_general_2020_csv.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-tuv_metad4g_tuvaluhighresolutionpopul_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - TUV
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-04-05'
  start: '2019-06-19'
temporal_resolution: null
title: 'Tuvalu: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
