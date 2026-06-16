---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook/Meta AI and Data for Good
    url: https://data.humdata.org/dataset/kyrgyzstan-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/kyrgyzstan-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/kyrgyzstan-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/kyrgyzstan-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-kgz_metad4g_highresolutionpopulationd_2019
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Kyrgyzstan: (1) Overall population
  density (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly
  (ages 60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/kyrgyzstan-high-resolution-population-density-maps-demographic-estimates]'
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Machine learning algorithms identified building footprints from commercial
    satellite imagery across Kyrgyzstan. Population estimates from publicly available
    census data were overlaid and distributed to building locations using Columbia
    University's demographic estimation methodology, producing high-resolution gridded
    population density maps for overall population and seven demographic subgroups
    at 100m resolution.
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
- href: https://data.humdata.org/dataset/kyrgyzstan-high-resolution-population-density-maps-demographic-estimates
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
  description: 'Kyrgyzstan: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/5d8b12a0-1f37-4b03-b1a2-d1c9f88f502b/resource/ef99a059-2ffe-4370-8929-daa1d0f3142e/download/kgz_children_under_five_2020_csv.zip
  format: zip
  id: resource_ef99a059
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kgz_children_under_five_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kyrgyzstan: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/5d8b12a0-1f37-4b03-b1a2-d1c9f88f502b/resource/ef187e28-7643-4111-9155-857d56e71716/download/kgz_children_under_five_2020_geotiff.zip
  format: zip
  id: resource_ef187e28
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kgz_children_under_five_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kyrgyzstan: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/5d8b12a0-1f37-4b03-b1a2-d1c9f88f502b/resource/064c588c-9614-4061-969e-4b2d8a44f86f/download/kgz_elderly_60_plus_2020_csv.zip
  format: zip
  id: resource_064c588c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kgz_elderly_60_plus_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kyrgyzstan: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/5d8b12a0-1f37-4b03-b1a2-d1c9f88f502b/resource/9668aedf-fabe-43e2-b828-d5322d3d7da9/download/kgz_elderly_60_plus_2020_geotiff.zip
  format: zip
  id: resource_9668aedf
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kgz_elderly_60_plus_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kyrgyzstan: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/5d8b12a0-1f37-4b03-b1a2-d1c9f88f502b/resource/56086ae4-d969-400c-95b0-f18c2a69f7ee/download/kgz_men_2020_csv.zip
  format: zip
  id: resource_56086ae4
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kgz_men_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kyrgyzstan: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/5d8b12a0-1f37-4b03-b1a2-d1c9f88f502b/resource/c0f97a59-a74b-4877-b221-99a07e65c37c/download/kgz_men_2020_geotiff.zip
  format: zip
  id: resource_c0f97a59
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kgz_men_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kyrgyzstan: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/5d8b12a0-1f37-4b03-b1a2-d1c9f88f502b/resource/c14e2164-93bd-4686-8037-a8c56b1bf2f6/download/kgz_women_2020_csv.zip
  format: zip
  id: resource_c14e2164
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kgz_women_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kyrgyzstan: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/5d8b12a0-1f37-4b03-b1a2-d1c9f88f502b/resource/9a0798c9-f896-40e8-a23e-f84795485d84/download/kgz_women_2020_geotiff.zip
  format: zip
  id: resource_9a0798c9
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kgz_women_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kyrgyzstan: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/5d8b12a0-1f37-4b03-b1a2-d1c9f88f502b/resource/d09a165a-cee4-4348-9560-b74f2f12071c/download/kgz_women_of_reproductive_age_15_49_2020_csv.zip
  format: zip
  id: resource_d09a165a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kgz_women_of_reproductive_age_15_49_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kyrgyzstan: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/5d8b12a0-1f37-4b03-b1a2-d1c9f88f502b/resource/1498640a-5ea7-4c09-840e-c37e0f33ae8d/download/kgz_women_of_reproductive_age_15_49_2020_geotiff.zip
  format: zip
  id: resource_1498640a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kgz_women_of_reproductive_age_15_49_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kyrgyzstan: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/5d8b12a0-1f37-4b03-b1a2-d1c9f88f502b/resource/b6f6b85a-9628-4d1b-9b7f-72eddf75a171/download/kgz_youth_15_24_2020_csv.zip
  format: zip
  id: resource_b6f6b85a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kgz_youth_15_24_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kyrgyzstan: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/5d8b12a0-1f37-4b03-b1a2-d1c9f88f502b/resource/876b56e2-1a04-4067-814f-47ea7837449b/download/kgz_youth_15_24_2020_geotiff.zip
  format: zip
  id: resource_876b56e2
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kgz_youth_15_24_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kyrgyzstan: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/5d8b12a0-1f37-4b03-b1a2-d1c9f88f502b/resource/5ac43bee-1250-46bf-8f05-f4379e3c4c40/download/kgz_general_2020_geotiff.zip
  format: zip
  id: resource_5ac43bee
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kgz_general_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kyrgyzstan: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/5d8b12a0-1f37-4b03-b1a2-d1c9f88f502b/resource/8777a4bb-6c49-4386-b3c5-b9ffa9e57fbc/download/kgz_general_2020_csv.zip
  format: zip
  id: resource_8777a4bb
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kgz_general_2020_csv.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-kgz_metad4g_highresolutionpopulationd_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - KGZ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-03-18'
  start: '2019-06-19'
temporal_resolution: null
title: 'Kyrgyzstan: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
