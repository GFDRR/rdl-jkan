---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook/Meta AI and Data for Good
    url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-dza
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-dza
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-dza
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-dza
dataset_id: rdls_exp-dza_metad4g_highresolutionpopulationd_2019
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Algeria: (1) Overall population density
  (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly (ages
  60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-dza]'
details: "To reference this data, please use the following citation: Facebook Connectivity\
  \ Lab and Center for International Earth Science Information Network - CIESIN -\
  \ Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery\
  \ for HRSL \xC2\xA9 2016 DigitalGlobe. Accessed DAY MONTH YEAR.' Please note that\
  \ as of 2024, Meta's high resolution population density maps are no longer being\
  \ updated."
exposure:
- asset_type:
    description: High-resolution gridded population density estimates for Algeria
      disaggregated by demographic groups (overall, women, men, children 0-5, youth
      15-24, elderly 60+, women of reproductive age 15-49)
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
    satellite imagery across Algeria. Population estimates derived from publicly available
    census data and demographic statistics were spatially distributed using these
    building locations and processed with Columbia University partners to generate
    high-resolution gridded population density maps disaggregated by demographic cohorts.
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
- href: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-dza
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
  description: 'Algeria: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e86baac1-074a-448b-8e53-3a94eadf2fb9/resource/7e58fbb0-2ca3-4ec3-935e-56df40b01395/download/dza_general_2020_geotiff.zip
  format: zip
  id: resource_7e58fbb0
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dza_general_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Algeria: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e86baac1-074a-448b-8e53-3a94eadf2fb9/resource/45621e43-a578-4dca-9381-52b265da35cd/download/dza_general_2020_csv.zip
  format: zip
  id: resource_45621e43
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dza_general_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Algeria: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e86baac1-074a-448b-8e53-3a94eadf2fb9/resource/846058d6-eba3-469b-a4a8-8751fde5e491/download/dza_children_under_five_2020_csv.zip
  format: zip
  id: resource_846058d6
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dza_children_under_five_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Algeria: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e86baac1-074a-448b-8e53-3a94eadf2fb9/resource/2280c9bc-000a-4930-a3fd-65e8c97f8799/download/dza_children_under_five_2020_geotiff.zip
  format: zip
  id: resource_2280c9bc
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dza_children_under_five_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Algeria: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e86baac1-074a-448b-8e53-3a94eadf2fb9/resource/cdc57f79-0c4d-4b5f-b4f1-9862c3c24465/download/dza_elderly_60_plus_2020_csv.zip
  format: zip
  id: resource_cdc57f79
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dza_elderly_60_plus_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Algeria: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e86baac1-074a-448b-8e53-3a94eadf2fb9/resource/07878d7c-10e1-43fa-a6ba-7ecb03a3eb00/download/dza_elderly_60_plus_2020_geotiff.zip
  format: zip
  id: resource_07878d7c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dza_elderly_60_plus_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Algeria: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e86baac1-074a-448b-8e53-3a94eadf2fb9/resource/66cb4ddc-4535-462a-abc5-4ef86d86779b/download/dza_men_2020_csv.zip
  format: zip
  id: resource_66cb4ddc
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dza_men_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Algeria: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e86baac1-074a-448b-8e53-3a94eadf2fb9/resource/5e848ae5-a4c1-458f-af1e-2c400456c646/download/dza_men_2020_geotiff.zip
  format: zip
  id: resource_5e848ae5
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dza_men_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Algeria: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e86baac1-074a-448b-8e53-3a94eadf2fb9/resource/a852d45c-308d-4134-9804-bf98c0018bc3/download/dza_women_2020_csv.zip
  format: zip
  id: resource_a852d45c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dza_women_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Algeria: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e86baac1-074a-448b-8e53-3a94eadf2fb9/resource/af1c7fd1-f832-4fdd-b49a-4c49b89c7e54/download/dza_women_2020_geotiff.zip
  format: zip
  id: resource_af1c7fd1
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dza_women_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Algeria: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e86baac1-074a-448b-8e53-3a94eadf2fb9/resource/4fa19471-4268-4437-8101-1b4b5b947959/download/dza_women_of_reproductive_age_15_49_2020_csv.zip
  format: zip
  id: resource_4fa19471
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dza_women_of_reproductive_age_15_49_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Algeria: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e86baac1-074a-448b-8e53-3a94eadf2fb9/resource/20378194-def4-4e88-aa93-001950d7cb74/download/dza_women_of_reproductive_age_15_49_2020_geotiff.zip
  format: zip
  id: resource_20378194
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dza_women_of_reproductive_age_15_49_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Algeria: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e86baac1-074a-448b-8e53-3a94eadf2fb9/resource/dda46fb3-a6dd-44fb-b9c5-c47bd40e1285/download/dza_youth_15_24_2020_csv.zip
  format: zip
  id: resource_dda46fb3
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dza_youth_15_24_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Algeria: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e86baac1-074a-448b-8e53-3a94eadf2fb9/resource/0b0ee87f-d3d5-436c-a549-715bbc34f40b/download/dza_youth_15_24_2020_geotiff.zip
  format: zip
  id: resource_0b0ee87f
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dza_youth_15_24_2020_geotiff.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-dza_metad4g_highresolutionpopulationd_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - DZA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2022-01-25'
  start: '2019-05-20'
temporal_resolution: null
title: 'Algeria: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
