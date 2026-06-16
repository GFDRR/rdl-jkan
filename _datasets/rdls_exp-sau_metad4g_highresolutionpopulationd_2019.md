---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook (satellite imagery and machine learning)
    url: https://data.humdata.org/dataset/saudi-arabia-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/saudi-arabia-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/saudi-arabia-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/saudi-arabia-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-sau_metad4g_highresolutionpopulationd_2019
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Saudi Arabia: (1) Overall population
  density (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly
  (ages 60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/saudi-arabia-high-resolution-population-density-maps-demographic-estimates]'
details: "To reference this data, please use the following citation: Facebook Connectivity\
  \ Lab and Center for International Earth Science Information Network - CIESIN -\
  \ Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery\
  \ for HRSL \xC2\xA9 2016 DigitalGlobe. Accessed DAY MONTH YEAR.' Please note that\
  \ as of 2024, Meta's high resolution population density maps are no longer being\
  \ updated."
exposure:
- asset_type:
    description: High-resolution gridded population density estimates for overall
      population and demographic subgroups (children 0-5, youth 15-24, elderly 60+,
      women, men, women of reproductive age 15-49)
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
    satellite imagery. Population estimates derived from publicly available census
    data and demographic statistics were spatially allocated to building locations
    using Columbia University's methodology, producing high-resolution gridded population
    density maps for Saudi Arabia at 100m resolution for 2020.
  sources:
  - id: source_1
    license: null
    name: Facebook (satellite imagery and machine learning)
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
- href: https://data.humdata.org/dataset/saudi-arabia-high-resolution-population-density-maps-demographic-estimates
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
  description: 'Saudi Arabia: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/14b288ca-1855-4025-9f01-41cba548e6f6/resource/44baa2f6-b6d8-4018-b9c6-fd81b493ec22/download/sau_general_2020_geotiff.zip
  format: zip
  id: resource_44baa2f6
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sau_general_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saudi Arabia: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/14b288ca-1855-4025-9f01-41cba548e6f6/resource/b2b30865-26b2-438e-b688-fc2322b6f926/download/sau_general_2020_csv.zip
  format: zip
  id: resource_b2b30865
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sau_general_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saudi Arabia: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/14b288ca-1855-4025-9f01-41cba548e6f6/resource/bfe7a324-a107-41d7-8125-8d4fff352186/download/sau_children_under_five_2020_geotiff.zip
  format: zip
  id: resource_bfe7a324
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sau_children_under_five_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saudi Arabia: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/14b288ca-1855-4025-9f01-41cba548e6f6/resource/eb9bd2b2-8a21-41c2-8701-833f5788d1d4/download/sau_elderly_60_plus_2020_geotiff.zip
  format: zip
  id: resource_eb9bd2b2
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sau_elderly_60_plus_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saudi Arabia: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/14b288ca-1855-4025-9f01-41cba548e6f6/resource/5539d569-5010-4f61-ac66-eda8618552a7/download/sau_men_2020_geotiff.zip
  format: zip
  id: resource_5539d569
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sau_men_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saudi Arabia: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/14b288ca-1855-4025-9f01-41cba548e6f6/resource/2d293b68-e2b8-4b56-be51-e96b45700660/download/sau_women_2020_geotiff.zip
  format: zip
  id: resource_2d293b68
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sau_women_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saudi Arabia: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/14b288ca-1855-4025-9f01-41cba548e6f6/resource/080ad8f0-c08f-4e9b-8779-5d159a6c352d/download/sau_women_of_reproductive_age_15_49_2020_geotiff.zip
  format: zip
  id: resource_080ad8f0
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sau_women_of_reproductive_age_15_49_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saudi Arabia: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/14b288ca-1855-4025-9f01-41cba548e6f6/resource/b7c22f0b-4a31-4091-bafc-98a906f822f4/download/sau_youth_15_24_2020_geotiff.zip
  format: zip
  id: resource_b7c22f0b
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sau_youth_15_24_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saudi Arabia: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/14b288ca-1855-4025-9f01-41cba548e6f6/resource/8b229280-0c71-4147-bc6f-8e445718d9a5/download/sau_children_under_five_2020_csv.zip
  format: zip
  id: resource_8b229280
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sau_children_under_five_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saudi Arabia: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/14b288ca-1855-4025-9f01-41cba548e6f6/resource/a5482a9e-ec6b-40d8-aac1-2e28d0b02938/download/sau_elderly_60_plus_2020_csv.zip
  format: zip
  id: resource_a5482a9e
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sau_elderly_60_plus_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saudi Arabia: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/14b288ca-1855-4025-9f01-41cba548e6f6/resource/9513a7a1-9fad-49c3-80af-3fcd9186ceda/download/sau_men_2020_csv.zip
  format: zip
  id: resource_9513a7a1
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sau_men_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saudi Arabia: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/14b288ca-1855-4025-9f01-41cba548e6f6/resource/65ef9ff7-b68e-4603-805e-86eb6a1c6860/download/sau_women_2020_csv.zip
  format: zip
  id: resource_65ef9ff7
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sau_women_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saudi Arabia: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/14b288ca-1855-4025-9f01-41cba548e6f6/resource/6f4d5393-d9f0-4e31-b376-96c9eb1391a3/download/sau_women_of_reproductive_age_15_49_2020_csv.zip
  format: zip
  id: resource_6f4d5393
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sau_women_of_reproductive_age_15_49_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saudi Arabia: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/14b288ca-1855-4025-9f01-41cba548e6f6/resource/e515d76c-2766-4a19-b228-e25ca6f925b8/download/sau_youth_15_24_2020_csv.zip
  format: zip
  id: resource_e515d76c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sau_youth_15_24_2020_csv.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-sau_metad4g_highresolutionpopulationd_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - SAU
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2022-12-02'
  start: '2019-09-19'
temporal_resolution: null
title: 'Saudi Arabia: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
