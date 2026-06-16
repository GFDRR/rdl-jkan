---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook/Meta AI and Data for Good
    url: https://data.humdata.org/dataset/northern-mariana-islands-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/northern-mariana-islands-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/northern-mariana-islands-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/northern-mariana-islands-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-mnp_metad4g_northernmarianaislandshig_201906
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in the Northern Mariana Islands: (1)
  Overall population density (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages
  15-24) (6) Elderly (ages 60+) (7) Women of reproductive age (ages 15-49).. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/northern-mariana-islands-high-resolution-population-density-maps-demographic-estimates]'
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
  description: High-resolution population density maps were created by applying machine
    learning algorithms to identify buildings from commercial satellite imagery, then
    overlaying population estimates derived from publicly available census data and
    demographic statistics in partnership with Columbia University. The resulting
    gridded datasets represent spatial distribution of total population and demographic
    subgroups at fine spatial resolution for disaster risk exposure assessment.
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
- href: https://data.humdata.org/dataset/northern-mariana-islands-high-resolution-population-density-maps-demographic-estimates
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
  description: 'Northern Mariana Islands: High Resolution Population Density Maps
    + Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/83175901-d4c9-4662-8492-5fe17e8035e5/resource/cfed2acb-8bdb-41d2-b262-6d8f355b471d/download/mnp_children_under_five_2019-06-01_csv.zip
  format: null
  id: resource_cfed2acb
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MNP_children_under_five_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Northern Mariana Islands: High Resolution Population Density Maps
    + Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/83175901-d4c9-4662-8492-5fe17e8035e5/resource/5209f625-4dc2-4584-bd1f-0cb58770a39e/download/mnp_children_under_five_2019-06-01_geotiff.zip
  format: null
  id: resource_5209f625
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MNP_children_under_five_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Northern Mariana Islands: High Resolution Population Density Maps
    + Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/83175901-d4c9-4662-8492-5fe17e8035e5/resource/a665d023-4d18-4286-9463-fd8399c7fd78/download/mnp_elderly_60_plus_2019-06-01_csv.zip
  format: null
  id: resource_a665d023
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MNP_elderly_60_plus_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Northern Mariana Islands: High Resolution Population Density Maps
    + Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/83175901-d4c9-4662-8492-5fe17e8035e5/resource/c1d78ab2-e015-4c5a-87b0-709bf8ed2c9d/download/mnp_elderly_60_plus_2019-06-01_geotiff.zip
  format: null
  id: resource_c1d78ab2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MNP_elderly_60_plus_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Northern Mariana Islands: High Resolution Population Density Maps
    + Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/83175901-d4c9-4662-8492-5fe17e8035e5/resource/2d1d9711-23e3-4745-8493-d4b450cb31f0/download/mnp_men_2019-06-01_csv.zip
  format: null
  id: resource_2d1d9711
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MNP_men_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Northern Mariana Islands: High Resolution Population Density Maps
    + Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/83175901-d4c9-4662-8492-5fe17e8035e5/resource/ef1e0ad3-d986-4ed9-9f8c-83c29e21cd78/download/mnp_men_2019-06-01_geotiff.zip
  format: null
  id: resource_ef1e0ad3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MNP_men_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Northern Mariana Islands: High Resolution Population Density Maps
    + Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/83175901-d4c9-4662-8492-5fe17e8035e5/resource/41893e27-4475-48e1-a746-2d8b5d170380/download/mnp_women_2019-06-01_csv.zip
  format: null
  id: resource_41893e27
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MNP_women_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Northern Mariana Islands: High Resolution Population Density Maps
    + Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/83175901-d4c9-4662-8492-5fe17e8035e5/resource/3dd86743-e04f-42c0-9fd5-86764a6ea4e2/download/mnp_women_2019-06-01_geotiff.zip
  format: null
  id: resource_3dd86743
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MNP_women_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Northern Mariana Islands: High Resolution Population Density Maps
    + Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/83175901-d4c9-4662-8492-5fe17e8035e5/resource/12b4d7d4-ceb4-40d9-889d-91fc60c5cd44/download/mnp_women_of_reproductive_age_15_49_2019-06-01_csv.zip
  format: null
  id: resource_12b4d7d4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MNP_women_of_reproductive_age_15_49_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Northern Mariana Islands: High Resolution Population Density Maps
    + Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/83175901-d4c9-4662-8492-5fe17e8035e5/resource/f45b79c1-7686-4595-baeb-5d10a3d8617c/download/mnp_women_of_reproductive_age_15_49_2019-06-01_geotiff.zip
  format: null
  id: resource_f45b79c1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MNP_women_of_reproductive_age_15_49_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Northern Mariana Islands: High Resolution Population Density Maps
    + Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/83175901-d4c9-4662-8492-5fe17e8035e5/resource/6dbefb31-6a33-44bf-a497-b6283d0fe2f0/download/mnp_youth_15_24_2019-06-01_csv.zip
  format: null
  id: resource_6dbefb31
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MNP_youth_15_24_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Northern Mariana Islands: High Resolution Population Density Maps
    + Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/83175901-d4c9-4662-8492-5fe17e8035e5/resource/baa02fce-c28c-4dae-ae1f-18707daa5d2f/download/mnp_youth_15_24_2019-06-01_geotiff.zip
  format: null
  id: resource_baa02fce
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MNP_youth_15_24_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Northern Mariana Islands: High Resolution Population Density Maps
    + Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/83175901-d4c9-4662-8492-5fe17e8035e5/resource/a111413a-19db-4032-b567-57ef8f19f1ce/download/population_mnp_2018-10-01_geotiff.zip
  format: null
  id: resource_a111413a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_mnp_2018-10-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Northern Mariana Islands: High Resolution Population Density Maps
    + Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/83175901-d4c9-4662-8492-5fe17e8035e5/resource/4369a34c-4e9d-41fa-8c2c-0e73d871e450/download/population_mnp_2018-10-01.csv.zip
  format: null
  id: resource_4369a34c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_mnp_2018-10-01.csv.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-mnp_metad4g_northernmarianaislandshig_201906
spatial:
  bbox: null
  centroid: null
  countries:
  - MNP
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2019-06-21'
  start: '2019-06-19'
temporal_resolution: null
title: 'Northern Mariana Islands: High Resolution Population Density Maps + Demographic
  Estimates'
version: null
vulnerability: null
---
