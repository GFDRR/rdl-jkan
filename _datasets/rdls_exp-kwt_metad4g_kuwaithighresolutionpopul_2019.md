---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook Data for Good
    url: https://data.humdata.org/dataset/kuwait-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/kuwait-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/kuwait-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/kuwait-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-kwt_metad4g_kuwaithighresolutionpopul_2019
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Kuwait: (1) Overall population density
  (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly (ages
  60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/kuwait-high-resolution-population-density-maps-demographic-estimates]'
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
license: CC-BY-4.0
lineage:
  description: High-resolution population density maps were created by applying machine
    learning algorithms to identify building footprints from commercial satellite
    imagery, then overlaying population estimates derived from publicly available
    census data and demographic statistics. The resulting gridded datasets provide
    spatial distribution of overall population and seven demographic subgroups at
    fine resolution across Kuwait.
  sources:
  - id: source_1
    license: null
    name: Facebook Data for Good
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
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/kuwait-high-resolution-population-density-maps-demographic-estimates
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
  description: 'Kuwait: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/fa1f8ca3-1e68-4fbf-93ca-a35d7e9f8f6c/resource/eb1b784a-ed29-487b-a737-196fd9559a1b/download/kwt_general_2020_geotiff.zip
  format: zip
  id: resource_eb1b784a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kwt_general_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kuwait: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/fa1f8ca3-1e68-4fbf-93ca-a35d7e9f8f6c/resource/4997b88d-0075-4d3b-be69-45e890a3d4fa/download/kwt_general_2020_csv.zip
  format: zip
  id: resource_4997b88d
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kwt_general_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kuwait: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/fa1f8ca3-1e68-4fbf-93ca-a35d7e9f8f6c/resource/25ad5cb6-5626-4cb2-a12e-766edb98865a/download/kwt_children_under_five_2020_geotiff.zip
  format: zip
  id: resource_25ad5cb6
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kwt_children_under_five_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kuwait: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/fa1f8ca3-1e68-4fbf-93ca-a35d7e9f8f6c/resource/56b3eec8-b9db-49b1-b9b7-faa6481d3c68/download/kwt_elderly_60_plus_2020_geotiff.zip
  format: zip
  id: resource_56b3eec8
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kwt_elderly_60_plus_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kuwait: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/fa1f8ca3-1e68-4fbf-93ca-a35d7e9f8f6c/resource/576a8367-fec1-4972-86a6-e5955320b3e1/download/kwt_men_2020_geotiff.zip
  format: zip
  id: resource_576a8367
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kwt_men_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kuwait: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/fa1f8ca3-1e68-4fbf-93ca-a35d7e9f8f6c/resource/2eaf8dee-b9ed-4d77-8e0b-91fadaf3e45f/download/kwt_women_2020_geotiff.zip
  format: zip
  id: resource_2eaf8dee
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kwt_women_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kuwait: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/fa1f8ca3-1e68-4fbf-93ca-a35d7e9f8f6c/resource/3c0f7af9-10b3-479d-8b90-83f3b0a34e4d/download/kwt_women_of_reproductive_age_15_49_2020_geotiff.zip
  format: zip
  id: resource_3c0f7af9
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kwt_women_of_reproductive_age_15_49_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kuwait: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/fa1f8ca3-1e68-4fbf-93ca-a35d7e9f8f6c/resource/b61b064f-827f-4167-80a1-1370088297a9/download/kwt_youth_15_24_2020_geotiff.zip
  format: zip
  id: resource_b61b064f
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kwt_youth_15_24_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kuwait: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/fa1f8ca3-1e68-4fbf-93ca-a35d7e9f8f6c/resource/76c5c490-2d0c-4b5d-ad8f-48927b2d8df8/download/kwt_children_under_five_2020_csv.zip
  format: zip
  id: resource_76c5c490
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kwt_children_under_five_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kuwait: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/fa1f8ca3-1e68-4fbf-93ca-a35d7e9f8f6c/resource/f926a6da-5e5c-4b34-9fdb-c0e7a428e926/download/kwt_elderly_60_plus_2020_csv.zip
  format: zip
  id: resource_f926a6da
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kwt_elderly_60_plus_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kuwait: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/fa1f8ca3-1e68-4fbf-93ca-a35d7e9f8f6c/resource/6662a84a-c98a-4718-8401-e27eccef29cf/download/kwt_men_2020_csv.zip
  format: zip
  id: resource_6662a84a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kwt_men_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kuwait: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/fa1f8ca3-1e68-4fbf-93ca-a35d7e9f8f6c/resource/87686044-e619-48a5-b8cc-ec6f32c995e7/download/kwt_women_2020_csv.zip
  format: zip
  id: resource_87686044
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kwt_women_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kuwait: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/fa1f8ca3-1e68-4fbf-93ca-a35d7e9f8f6c/resource/83863c6e-d856-4322-8832-e3494d0c1889/download/kwt_women_of_reproductive_age_15_49_2020_csv.zip
  format: zip
  id: resource_83863c6e
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kwt_women_of_reproductive_age_15_49_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kuwait: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/fa1f8ca3-1e68-4fbf-93ca-a35d7e9f8f6c/resource/a97c185b-cd58-410d-8e08-877a52957bd8/download/kwt_youth_15_24_2020_csv.zip
  format: zip
  id: resource_a97c185b
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kwt_youth_15_24_2020_csv.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-kwt_metad4g_kuwaithighresolutionpopul_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - KWT
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2022-12-09'
  start: '2019-09-19'
temporal_resolution: null
title: 'Kuwait: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
