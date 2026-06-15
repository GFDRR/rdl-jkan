---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook/Meta AI and Data for Good
    url: https://data.humdata.org/dataset/guyana-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/guyana-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/guyana-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/guyana-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-guy_metad4g_highresolutionpopulationd_2019
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Guyana: (1) Overall population density
  (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly (ages
  60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/guyana-high-resolution-population-density-maps-demographic-estimates]'
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
    satellite imagery across Guyana. Population estimates derived from publicly available
    census data and demographic statistics were spatially allocated to these buildings
    using a methodology developed in partnership with Columbia University, producing
    gridded population density maps for seven demographic categories at high spatial
    resolution for the year 2020.
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
- href: https://data.humdata.org/dataset/guyana-high-resolution-population-density-maps-demographic-estimates
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
  description: 'Guyana: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e8f61f7d-4c4b-40ae-bebe-370c2dd669da/resource/9f9502c1-02ae-4e74-a7dd-839930d2d639/download/guy_general_2020_csv.zip
  format: zip
  id: resource_9f9502c1
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guy_general_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guyana: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e8f61f7d-4c4b-40ae-bebe-370c2dd669da/resource/93172335-fd47-4991-8d39-33b95c262e1f/download/guy_general_2020_geotiff.zip
  format: zip
  id: resource_93172335
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guy_general_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guyana: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e8f61f7d-4c4b-40ae-bebe-370c2dd669da/resource/d90a33a4-6be9-4f68-9a28-0c8e0626b095/download/guy_children_under_five_2020_csv.zip
  format: zip
  id: resource_d90a33a4
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guy_children_under_five_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guyana: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e8f61f7d-4c4b-40ae-bebe-370c2dd669da/resource/61866ae2-e396-424f-909d-114040a7b648/download/guy_children_under_five_2020_geotiff.zip
  format: zip
  id: resource_61866ae2
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guy_children_under_five_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guyana: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e8f61f7d-4c4b-40ae-bebe-370c2dd669da/resource/de30eacf-dd7e-49aa-8b75-13d21c30a826/download/guy_elderly_60_plus_2020_csv.zip
  format: zip
  id: resource_de30eacf
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guy_elderly_60_plus_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guyana: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e8f61f7d-4c4b-40ae-bebe-370c2dd669da/resource/e3517392-e031-4595-9730-f5f016a00e38/download/guy_elderly_60_plus_2020_geotiff.zip
  format: zip
  id: resource_e3517392
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guy_elderly_60_plus_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guyana: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e8f61f7d-4c4b-40ae-bebe-370c2dd669da/resource/945a454c-a6ec-4fae-a94e-70f153728af6/download/guy_men_2020_csv.zip
  format: zip
  id: resource_945a454c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guy_men_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guyana: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e8f61f7d-4c4b-40ae-bebe-370c2dd669da/resource/5cef54b5-2585-4ffd-8688-ad5396631cb8/download/guy_men_2020_geotiff.zip
  format: zip
  id: resource_5cef54b5
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guy_men_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guyana: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e8f61f7d-4c4b-40ae-bebe-370c2dd669da/resource/4d6191bb-0fde-4750-a9a6-e6db4064e3f0/download/guy_women_2020_csv.zip
  format: zip
  id: resource_4d6191bb
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guy_women_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guyana: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e8f61f7d-4c4b-40ae-bebe-370c2dd669da/resource/e84d1a8d-862d-4b97-a939-1836f9414dbf/download/guy_women_2020_geotiff.zip
  format: zip
  id: resource_e84d1a8d
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guy_women_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guyana: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e8f61f7d-4c4b-40ae-bebe-370c2dd669da/resource/68edd521-6498-48ac-98c8-990445dff63d/download/guy_women_of_reproductive_age_15_49_2020_csv.zip
  format: zip
  id: resource_68edd521
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guy_women_of_reproductive_age_15_49_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guyana: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e8f61f7d-4c4b-40ae-bebe-370c2dd669da/resource/55b11afc-1489-4e2b-89b2-593d6593e14d/download/guy_women_of_reproductive_age_15_49_2020_geotiff.zip
  format: zip
  id: resource_55b11afc
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guy_women_of_reproductive_age_15_49_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guyana: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e8f61f7d-4c4b-40ae-bebe-370c2dd669da/resource/fff51b2f-d78c-4dd4-8950-9bef576a982a/download/guy_youth_15_24_2020_csv.zip
  format: zip
  id: resource_fff51b2f
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guy_youth_15_24_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guyana: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e8f61f7d-4c4b-40ae-bebe-370c2dd669da/resource/2a219601-03e4-4aaf-bae6-61edb8d63bca/download/guy_youth_15_24_2020_geotiff.zip
  format: zip
  id: resource_2a219601
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guy_youth_15_24_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This file has information about the cloud cover percentage and capture
    data of the satellite images used.
  download_url: https://data.humdata.org/dataset/e8f61f7d-4c4b-40ae-bebe-370c2dd669da/resource/bb71d4b8-ce26-4c3e-8ede-534625430230/download/guy_dg_metadata.json.zip
  format: null
  id: resource_bb71d4b8
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guy_dg_metadata.json.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-guy_metad4g_highresolutionpopulationd_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - GUY
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2022-09-01'
  start: '2019-06-10'
temporal_resolution: null
title: 'Guyana: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
