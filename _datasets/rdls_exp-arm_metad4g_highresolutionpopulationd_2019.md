---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook/Meta AI and Data for Good
    url: https://data.humdata.org/dataset/armenia-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/armenia-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/armenia-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/armenia-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-arm_metad4g_highresolutionpopulationd_2019
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Armenia: (1) Overall population density
  (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly (ages
  60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/armenia-high-resolution-population-density-maps-demographic-estimates]'
details: "To reference this data, please use the following citation: Facebook Connectivity\
  \ Lab and Center for International Earth Science Information Network - CIESIN -\
  \ Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery\
  \ for HRSL \xC2\xA9 2016 DigitalGlobe. Accessed DAY MONTH YEAR.' Please note that\
  \ as of 2024, Meta's high resolution population density maps are no longer being\
  \ updated."
exposure:
- asset_type:
    description: High-resolution gridded population density estimates for Armenia
      disaggregated by age and gender demographics (overall, women, men, children
      0-5, youth 15-24, elderly 60+, women of reproductive age 15-49)
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
    imagery, then overlaying population estimates derived from census data and demographic
    statistics in partnership with Columbia University. The resulting gridded datasets
    provide spatially explicit population distributions disaggregated by demographic
    groups at national scale for Armenia.
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
- href: https://data.humdata.org/dataset/armenia-high-resolution-population-density-maps-demographic-estimates
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
  description: 'Armenia: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/b523d9cd-7167-49dd-b711-fe2033a63fc8/resource/9eb0f574-f634-4ec1-9468-c4857126948a/download/arm_children_under_five_2020_csv.zip
  format: zip
  id: resource_9eb0f574
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: arm_children_under_five_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Armenia: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/b523d9cd-7167-49dd-b711-fe2033a63fc8/resource/8b9122b3-5b54-42d4-ae42-1dfc9f208f9c/download/arm_elderly_60_plus_2020_csv.zip
  format: zip
  id: resource_8b9122b3
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: arm_elderly_60_plus_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Armenia: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/b523d9cd-7167-49dd-b711-fe2033a63fc8/resource/97b33dee-a9ba-459a-8229-2b4f15a0a6c7/download/arm_men_2020_csv.zip
  format: zip
  id: resource_97b33dee
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: arm_men_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Armenia: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/b523d9cd-7167-49dd-b711-fe2033a63fc8/resource/ad9666da-a07e-4771-a9cd-2865b05cf0e5/download/arm_women_2020_csv.zip
  format: zip
  id: resource_ad9666da
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: arm_women_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Armenia: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/b523d9cd-7167-49dd-b711-fe2033a63fc8/resource/7f68208a-6dde-49d9-aa6d-7ca305b57e5e/download/arm_women_of_reproductive_age_15_49_2020_csv.zip
  format: zip
  id: resource_7f68208a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: arm_women_of_reproductive_age_15_49_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Armenia: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/b523d9cd-7167-49dd-b711-fe2033a63fc8/resource/87868d1f-2c49-46e3-9f87-87813c34688e/download/arm_youth_15_24_2020_csv.zip
  format: zip
  id: resource_87868d1f
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: arm_youth_15_24_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Armenia: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/b523d9cd-7167-49dd-b711-fe2033a63fc8/resource/50b9e7d0-7009-487f-86ca-7a24f484df11/download/arm_children_under_five_2020_geotiff.zip
  format: zip
  id: resource_50b9e7d0
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: arm_children_under_five_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Armenia: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/b523d9cd-7167-49dd-b711-fe2033a63fc8/resource/38a844d1-9368-4af2-a422-703f116017bd/download/arm_elderly_60_plus_2020_geotiff.zip
  format: zip
  id: resource_38a844d1
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: arm_elderly_60_plus_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Armenia: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/b523d9cd-7167-49dd-b711-fe2033a63fc8/resource/f58fcde5-e948-4c13-a3f1-3936f9992cdd/download/arm_men_2020_geotiff.zip
  format: zip
  id: resource_f58fcde5
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: arm_men_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Armenia: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/b523d9cd-7167-49dd-b711-fe2033a63fc8/resource/dc640551-ed23-42af-95a1-4e72e502be74/download/arm_women_2020_geotiff.zip
  format: zip
  id: resource_dc640551
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: arm_women_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Armenia: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/b523d9cd-7167-49dd-b711-fe2033a63fc8/resource/8ba93824-f4a8-48b4-87f6-9368deb9c1e9/download/arm_women_of_reproductive_age_15_49_2020_geotiff.zip
  format: zip
  id: resource_8ba93824
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: arm_women_of_reproductive_age_15_49_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Armenia: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/b523d9cd-7167-49dd-b711-fe2033a63fc8/resource/39803540-1340-488c-9547-5984dec9347e/download/arm_youth_15_24_2020_geotiff.zip
  format: zip
  id: resource_39803540
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: arm_youth_15_24_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Armenia: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/b523d9cd-7167-49dd-b711-fe2033a63fc8/resource/70eebb9e-25e0-419a-ac3f-1089461ca45f/download/arm_general_2020_csv.zip
  format: zip
  id: resource_70eebb9e
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: arm_general_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Armenia: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/b523d9cd-7167-49dd-b711-fe2033a63fc8/resource/74af95f8-e6b5-449f-bc1e-4bf9a20e8136/download/arm_general_2020_geotiff.zip
  format: zip
  id: resource_74af95f8
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: arm_general_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This file has information about the cloud cover percentage and capture
    data of the satellite images used.
  download_url: https://data.humdata.org/dataset/b523d9cd-7167-49dd-b711-fe2033a63fc8/resource/b1f75a9b-38dd-4feb-8a8a-0edcec20b396/download/arm_dg_metadata.json.zip
  format: null
  id: resource_b1f75a9b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: arm_dg_metadata.json.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-arm_metad4g_highresolutionpopulationd_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - ARM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-04-05'
  start: '2019-09-19'
temporal_resolution: null
title: 'Armenia: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
