---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook Data for Good
    url: https://data.humdata.org/dataset/oman-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/oman-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/oman-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/oman-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-omn_metad4g_omanhighresolutionpopulat_2019
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Oman: (1) Overall population density
  (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly (ages
  60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/oman-high-resolution-population-density-maps-demographic-estimates]'
details: "To reference this data, please use the following citation: Facebook Connectivity\
  \ Lab and Center for International Earth Science Information Network - CIESIN -\
  \ Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery\
  \ for HRSL \xC2\xA9 2016 DigitalGlobe. Accessed DAY MONTH YEAR.' Please note that\
  \ as of 2024, Meta's high resolution population density maps are no longer being\
  \ updated."
exposure:
- asset_type:
    description: High-resolution gridded population density maps for overall population
      and demographic subgroups (children 0-5, youth 15-24, elderly 60+, women, men,
      women of reproductive age 15-49)
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
    learning algorithms to identify building footprints from commercial satellite
    imagery, then overlaying population estimates derived from publicly available
    census data and demographic statistics in partnership with Columbia University.
    The resulting gridded datasets provide spatial distribution of overall population
    and seven demographic subgroups at fine resolution for Oman in 2020.
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
- href: https://data.humdata.org/dataset/oman-high-resolution-population-density-maps-demographic-estimates
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
  description: 'Oman: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/5baf0e2a-2fd5-4cf9-80d7-ca04daab2959/resource/2d999b26-7c4d-47ea-a5bb-71c197ef9110/download/omn_general_2020_geotiff.zip
  format: zip
  id: resource_2d999b26
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: omn_general_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Oman: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/5baf0e2a-2fd5-4cf9-80d7-ca04daab2959/resource/07a473ea-997a-442f-af72-49e392bf9603/download/omn_general_2020_csv.zip
  format: zip
  id: resource_07a473ea
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: omn_general_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Oman: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/5baf0e2a-2fd5-4cf9-80d7-ca04daab2959/resource/9872a159-45a4-46e8-a7b9-8146fbe28917/download/omn_children_under_five_2020_geotiff.zip
  format: zip
  id: resource_9872a159
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: omn_children_under_five_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Oman: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/5baf0e2a-2fd5-4cf9-80d7-ca04daab2959/resource/3881d9bd-44fa-46b1-8738-3a462d8c6405/download/omn_elderly_60_plus_2020_geotiff.zip
  format: zip
  id: resource_3881d9bd
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: omn_elderly_60_plus_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Oman: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/5baf0e2a-2fd5-4cf9-80d7-ca04daab2959/resource/6c10476c-3ae6-44ae-a41f-f8ae15f81749/download/omn_men_2020_geotiff.zip
  format: zip
  id: resource_6c10476c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: omn_men_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Oman: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/5baf0e2a-2fd5-4cf9-80d7-ca04daab2959/resource/b29a5f9b-e3bf-4f9c-8870-578ed28e5b9d/download/omn_women_2020_geotiff.zip
  format: zip
  id: resource_b29a5f9b
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: omn_women_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Oman: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/5baf0e2a-2fd5-4cf9-80d7-ca04daab2959/resource/323b1c24-e429-4c42-987d-bb32f77a6dc5/download/omn_women_of_reproductive_age_15_49_2020_geotiff.zip
  format: zip
  id: resource_323b1c24
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: omn_women_of_reproductive_age_15_49_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Oman: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/5baf0e2a-2fd5-4cf9-80d7-ca04daab2959/resource/bc1d7900-5b2a-44e9-bde5-8c21dec69441/download/omn_youth_15_24_2020_geotiff.zip
  format: zip
  id: resource_bc1d7900
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: omn_youth_15_24_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Oman: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/5baf0e2a-2fd5-4cf9-80d7-ca04daab2959/resource/917a4a72-f032-4b6b-9a26-f45119462ef0/download/omn_children_under_five_2020_csv.zip
  format: zip
  id: resource_917a4a72
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: omn_children_under_five_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Oman: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/5baf0e2a-2fd5-4cf9-80d7-ca04daab2959/resource/6d733c71-5cc4-4813-9284-5a97f9e53bbd/download/omn_elderly_60_plus_2020_csv.zip
  format: zip
  id: resource_6d733c71
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: omn_elderly_60_plus_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Oman: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/5baf0e2a-2fd5-4cf9-80d7-ca04daab2959/resource/385b291a-46cf-480b-b980-4d2fad1c0161/download/omn_men_2020_csv.zip
  format: zip
  id: resource_385b291a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: omn_men_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Oman: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/5baf0e2a-2fd5-4cf9-80d7-ca04daab2959/resource/26c90f14-8260-4267-b09f-5c187a7ec3f2/download/omn_women_2020_csv.zip
  format: zip
  id: resource_26c90f14
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: omn_women_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Oman: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/5baf0e2a-2fd5-4cf9-80d7-ca04daab2959/resource/53900542-1643-4eb8-a78c-f7ac42c2abf2/download/omn_women_of_reproductive_age_15_49_2020_csv.zip
  format: zip
  id: resource_53900542
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: omn_women_of_reproductive_age_15_49_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Oman: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/5baf0e2a-2fd5-4cf9-80d7-ca04daab2959/resource/2d715fe0-5c60-4418-a4d4-aabb5b4d7fba/download/omn_youth_15_24_2020_csv.zip
  format: zip
  id: resource_2d715fe0
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: omn_youth_15_24_2020_csv.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-omn_metad4g_omanhighresolutionpopulat_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - OMN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2022-12-16'
  start: '2019-09-19'
temporal_resolution: null
title: 'Oman: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
