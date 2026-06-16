---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook (Meta AI and Data for Good)
    url: https://data.humdata.org/dataset/argentina-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/argentina-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/argentina-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/argentina-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-arg_metad4g_highresolutionpopulationd_2019
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Argentina: (1) Overall population
  density (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly
  (ages 60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/argentina-high-resolution-population-density-maps-demographic-estimates]'
details: "To reference this data, please use the following citation: Facebook Connectivity\
  \ Lab and Center for International Earth Science Information Network - CIESIN -\
  \ Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery\
  \ for HRSL \xC2\xA9 2016 DigitalGlobe. Accessed DAY MONTH YEAR.' Please note that\
  \ as of 2024, Meta's high resolution population density maps are no longer being\
  \ updated."
exposure:
- asset_type:
    description: High-resolution gridded population density estimates for Argentina
      disaggregated by age and sex (overall, women, men, children 0-5, youth 15-24,
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
  description: High-resolution population density maps were created by applying machine
    learning algorithms to identify building footprints from commercial satellite
    imagery, then overlaying population estimates derived from publicly available
    census data and demographic statistics in partnership with Columbia University.
    The resulting gridded datasets provide disaggregated population counts by age
    and sex groups at fine spatial resolution across Argentina.
  sources:
  - id: source_1
    license: null
    name: Facebook (Meta AI and Data for Good)
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
- href: https://data.humdata.org/dataset/argentina-high-resolution-population-density-maps-demographic-estimates
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
  description: 'Argentina: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/6cf49080-1226-4eda-8700-a0093cbdfe4d/resource/5c62de88-0fa2-4b6f-81dc-e8c3bdb05cb6/download/arg_general_2020_geotiff.zip
  format: zip
  id: resource_5c62de88
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: arg_general_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Argentina: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/6cf49080-1226-4eda-8700-a0093cbdfe4d/resource/5737d87f-e17f-4c82-b1bd-d589ed631318/download/arg_general_2020_csv.zip
  format: zip
  id: resource_5737d87f
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: arg_general_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Argentina: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/6cf49080-1226-4eda-8700-a0093cbdfe4d/resource/1795ad97-e06a-4ca4-83aa-32ab612f55ba/download/arg_children_under_five_2020_csv.zip
  format: zip
  id: resource_1795ad97
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: arg_children_under_five_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Argentina: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/6cf49080-1226-4eda-8700-a0093cbdfe4d/resource/1f1e657f-5de3-4791-91d2-eeb66d24d3ff/download/arg_children_under_five_2020_geotiff.zip
  format: zip
  id: resource_1f1e657f
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: arg_children_under_five_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Argentina: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/6cf49080-1226-4eda-8700-a0093cbdfe4d/resource/8f1d9473-90f0-441f-b464-c76960e9e130/download/arg_elderly_60_plus_2020_csv.zip
  format: zip
  id: resource_8f1d9473
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: arg_elderly_60_plus_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Argentina: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/6cf49080-1226-4eda-8700-a0093cbdfe4d/resource/b081ed8f-39f3-4339-9335-f3328fec0b50/download/arg_elderly_60_plus_2020_geotiff.zip
  format: zip
  id: resource_b081ed8f
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: arg_elderly_60_plus_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Argentina: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/6cf49080-1226-4eda-8700-a0093cbdfe4d/resource/b89a0468-6591-46ff-b180-f81fc2237482/download/arg_men_2020_csv.zip
  format: zip
  id: resource_b89a0468
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: arg_men_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Argentina: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/6cf49080-1226-4eda-8700-a0093cbdfe4d/resource/d6a36b44-6eb8-4bb7-a33d-bee540070c9b/download/arg_men_2020_geotiff.zip
  format: zip
  id: resource_d6a36b44
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: arg_men_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Argentina: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/6cf49080-1226-4eda-8700-a0093cbdfe4d/resource/0a5c0fe6-ea06-4e05-aa30-9f01c07981b7/download/arg_women_2020_csv.zip
  format: zip
  id: resource_0a5c0fe6
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: arg_women_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Argentina: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/6cf49080-1226-4eda-8700-a0093cbdfe4d/resource/0c003193-f45d-43a8-8d72-b0d06d885ea5/download/arg_women_2020_geotiff.zip
  format: zip
  id: resource_0c003193
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: arg_women_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Argentina: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/6cf49080-1226-4eda-8700-a0093cbdfe4d/resource/0f7c7a18-2db4-497a-82f0-6688f4f1cf1e/download/arg_women_of_reproductive_age_15_49_2020_csv.zip
  format: zip
  id: resource_0f7c7a18
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: arg_women_of_reproductive_age_15_49_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Argentina: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/6cf49080-1226-4eda-8700-a0093cbdfe4d/resource/31c2f5aa-2772-4fe0-b6aa-1cedd992be82/download/arg_women_of_reproductive_age_15_49_2020_geotiff.zip
  format: zip
  id: resource_31c2f5aa
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: arg_women_of_reproductive_age_15_49_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Argentina: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/6cf49080-1226-4eda-8700-a0093cbdfe4d/resource/dff11b02-a356-4a4f-948c-5a7722ad7365/download/arg_youth_15_24_2020_csv.zip
  format: zip
  id: resource_dff11b02
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: arg_youth_15_24_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Argentina: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/6cf49080-1226-4eda-8700-a0093cbdfe4d/resource/fbb881fd-ef93-4a80-a01c-8bf1f52cda98/download/arg_youth_15_24_2020_geotiff.zip
  format: zip
  id: resource_fbb881fd
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: arg_youth_15_24_2020_geotiff.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-arg_metad4g_highresolutionpopulationd_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - ARG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2022-11-23'
  start: '2019-06-10'
temporal_resolution: null
title: 'Argentina: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
