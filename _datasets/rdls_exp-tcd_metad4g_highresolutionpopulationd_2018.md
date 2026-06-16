---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook/Meta AI and Data for Good
    url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-tcd
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-tcd
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-tcd
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-tcd
dataset_id: rdls_exp-tcd_metad4g_highresolutionpopulationd_2018
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Chad: (1) Overall population density
  (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly (ages
  60+) (7) Women of reproductive age (ages 15-49). There is also a tiled version of
  this dataset that may be easier to use if you are interested in many countries..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-tcd]'
details: "To reference this data, please use the following citation: Facebook Connectivity\
  \ Lab and Center for International Earth Science Information Network - CIESIN -\
  \ Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery\
  \ for HRSL \xC2\xA9 2016 DigitalGlobe. Accessed DAY MONTH YEAR.' Please note that\
  \ as of 2024, Meta's high resolution population density maps are no longer being\
  \ updated."
exposure:
- asset_type:
    description: High-resolution gridded population density maps for Chad disaggregated
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
license: CC-BY-4.0
lineage:
  description: Machine learning algorithms identified building footprints from commercial
    satellite imagery across Chad. Population estimates derived from publicly available
    census data and demographic statistics were spatially distributed using the building
    framework and overlaid with Columbia University's population estimation methodology
    to produce high-resolution gridded population density maps disaggregated by demographic
    cohorts for 2020.
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
- href: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-tcd
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
  description: 'Chad: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/99769693-aa51-406b-881d-dc35884bac45/resource/033ca651-b8dc-4ee1-87a5-7ef7aab2d6ad/download/tcd_general_2020_geotiff.zip
  format: zip
  id: resource_033ca651
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tcd_general_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Chad: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/99769693-aa51-406b-881d-dc35884bac45/resource/fe87be46-460f-4417-afdf-684d7627f3e7/download/tcd_general_2020_csv.zip
  format: zip
  id: resource_fe87be46
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tcd_general_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Chad: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/99769693-aa51-406b-881d-dc35884bac45/resource/1bcb7440-edcf-4173-97a5-5ef224054c8b/download/tcd_children_under_five_2020_csv.zip
  format: zip
  id: resource_1bcb7440
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tcd_children_under_five_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Chad: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/99769693-aa51-406b-881d-dc35884bac45/resource/3fcb9fd5-c71e-4d75-972e-26abf1ed6e14/download/tcd_children_under_five_2020_geotiff.zip
  format: zip
  id: resource_3fcb9fd5
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tcd_children_under_five_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Chad: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/99769693-aa51-406b-881d-dc35884bac45/resource/eb5a5d65-3219-4c40-84ee-7ef38e57ffb6/download/tcd_elderly_60_plus_2020_csv.zip
  format: zip
  id: resource_eb5a5d65
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tcd_elderly_60_plus_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Chad: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/99769693-aa51-406b-881d-dc35884bac45/resource/0764a746-2bc4-4ee6-afb7-f0002ab461e6/download/tcd_elderly_60_plus_2020_geotiff.zip
  format: zip
  id: resource_0764a746
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tcd_elderly_60_plus_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Chad: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/99769693-aa51-406b-881d-dc35884bac45/resource/8702d3ed-5f9e-404b-9135-a888fd7e8e5c/download/tcd_men_2020_csv.zip
  format: zip
  id: resource_8702d3ed
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tcd_men_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Chad: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/99769693-aa51-406b-881d-dc35884bac45/resource/83537b04-6853-402a-a3f7-ab142d4931ee/download/tcd_men_2020_geotiff.zip
  format: zip
  id: resource_83537b04
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tcd_men_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Chad: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/99769693-aa51-406b-881d-dc35884bac45/resource/1a69e8b7-322e-4509-add2-91c38082ecfa/download/tcd_women_2020_csv.zip
  format: zip
  id: resource_1a69e8b7
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tcd_women_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Chad: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/99769693-aa51-406b-881d-dc35884bac45/resource/7ae2fc9b-d655-4bac-8294-fcf2dccfcd30/download/tcd_women_2020_geotiff.zip
  format: zip
  id: resource_7ae2fc9b
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tcd_women_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Chad: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/99769693-aa51-406b-881d-dc35884bac45/resource/39e4a698-d7c9-4acf-ab95-3c604e796e0e/download/tcd_women_of_reproductive_age_15_49_2020_csv.zip
  format: zip
  id: resource_39e4a698
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tcd_women_of_reproductive_age_15_49_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Chad: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/99769693-aa51-406b-881d-dc35884bac45/resource/617e1155-9cf9-4624-999f-2b81b77e4b1b/download/tcd_women_of_reproductive_age_15_49_2020_geotiff.zip
  format: zip
  id: resource_617e1155
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tcd_women_of_reproductive_age_15_49_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Chad: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/99769693-aa51-406b-881d-dc35884bac45/resource/6ef8b368-3441-4ca3-9fbf-ce1762242742/download/tcd_youth_15_24_2020_csv.zip
  format: zip
  id: resource_6ef8b368
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tcd_youth_15_24_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Chad: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/99769693-aa51-406b-881d-dc35884bac45/resource/edf89f02-b03a-476b-9b5d-be5d6fba8999/download/tcd_youth_15_24_2020_geotiff.zip
  format: zip
  id: resource_edf89f02
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tcd_youth_15_24_2020_geotiff.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-tcd_metad4g_highresolutionpopulationd_2018
spatial:
  bbox: null
  centroid: null
  countries:
  - TCD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2022-10-21'
  start: '2018-05-20'
temporal_resolution: null
title: 'Chad: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
