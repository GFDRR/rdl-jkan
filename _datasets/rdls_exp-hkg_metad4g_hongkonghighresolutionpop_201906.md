---
attributions:
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/hong-kong-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/hong-kong-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/hong-kong-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-hkg_metad4g_hongkonghighresolutionpop_201906
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Hong Kong: (1) Overall population
  density (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly
  (ages 60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/hong-kong-high-resolution-population-density-maps-demographic-estimates]'
details: "To reference this data, please use the following citation: Facebook Connectivity\
  \ Lab and Center for International Earth Science Information Network - CIESIN -\
  \ Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery\
  \ for HRSL \xC2\xA9 2016 DigitalGlobe. Accessed DAY MONTH YEAR.' Please note that\
  \ as of 2024, Meta's high resolution population density maps are no longer being\
  \ updated."
exposure:
- asset_type:
    description: High-resolution gridded population density estimates disaggregated
      by age and gender (overall, women, men, children 0-5, youth 15-24, elderly 60+,
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
    imagery, then overlaying general population estimates derived from publicly available
    census data and demographic statistics. The resulting gridded datasets provide
    spatially explicit population counts disaggregated by age and gender cohorts for
    Hong Kong.
  sources:
  - id: source_1
    license: null
    name: AI and Data for Good at Meta
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
- href: https://data.humdata.org/dataset/hong-kong-high-resolution-population-density-maps-demographic-estimates
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
  description: 'Hong Kong: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/dfd44ffe-bf3e-4a00-b69d-889e020918f7/resource/2a213b30-f49b-419c-bc7b-6c4e6c9ca506/download/hkg_children_under_five_2019-06-01_csv.zip
  format: null
  id: resource_2a213b30
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: HKG_children_under_five_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Hong Kong: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/dfd44ffe-bf3e-4a00-b69d-889e020918f7/resource/a4aa0000-edc5-4b70-97f8-883a65a49a9d/download/hkg_children_under_five_2019-06-01_geotiff.zip
  format: null
  id: resource_a4aa0000
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: HKG_children_under_five_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Hong Kong: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/dfd44ffe-bf3e-4a00-b69d-889e020918f7/resource/c83666b0-153d-436e-b182-0a00a682e335/download/hkg_elderly_60_plus_2019-06-01_csv.zip
  format: null
  id: resource_c83666b0
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: HKG_elderly_60_plus_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Hong Kong: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/dfd44ffe-bf3e-4a00-b69d-889e020918f7/resource/05b96479-2648-4fff-8db6-55c812cb61b6/download/hkg_elderly_60_plus_2019-06-01_geotiff.zip
  format: null
  id: resource_05b96479
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: HKG_elderly_60_plus_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Hong Kong: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/dfd44ffe-bf3e-4a00-b69d-889e020918f7/resource/37c3bce4-e39d-4be8-ac2a-de882f13a6a8/download/hkg_men_2019-06-01_csv.zip
  format: null
  id: resource_37c3bce4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: HKG_men_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Hong Kong: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/dfd44ffe-bf3e-4a00-b69d-889e020918f7/resource/e0bcdaca-5bd3-45b8-9d4a-cdc461f14eb7/download/hkg_men_2019-06-01_geotiff.zip
  format: null
  id: resource_e0bcdaca
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: HKG_men_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Hong Kong: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/dfd44ffe-bf3e-4a00-b69d-889e020918f7/resource/b71c82f5-0999-4b77-bd64-a4bde60e3dc1/download/hkg_women_2019-06-01_csv.zip
  format: null
  id: resource_b71c82f5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: HKG_women_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Hong Kong: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/dfd44ffe-bf3e-4a00-b69d-889e020918f7/resource/c4e72fda-0c51-487f-a4f6-5a0ab079a6a6/download/hkg_women_2019-06-01_geotiff.zip
  format: null
  id: resource_c4e72fda
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: HKG_women_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Hong Kong: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/dfd44ffe-bf3e-4a00-b69d-889e020918f7/resource/8179b44e-5403-4e3d-98c0-ba6ae5648c0d/download/hkg_women_of_reproductive_age_15_49_2019-06-01_csv.zip
  format: null
  id: resource_8179b44e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: HKG_women_of_reproductive_age_15_49_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Hong Kong: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/dfd44ffe-bf3e-4a00-b69d-889e020918f7/resource/0f468165-ad5d-4d7f-ae42-18572e681849/download/hkg_women_of_reproductive_age_15_49_2019-06-01_geotiff.zip
  format: null
  id: resource_0f468165
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: HKG_women_of_reproductive_age_15_49_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Hong Kong: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/dfd44ffe-bf3e-4a00-b69d-889e020918f7/resource/b686c10c-35e8-4b89-85a2-5d97fdcf32dd/download/hkg_youth_15_24_2019-06-01_csv.zip
  format: null
  id: resource_b686c10c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: HKG_youth_15_24_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Hong Kong: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/dfd44ffe-bf3e-4a00-b69d-889e020918f7/resource/f4ef66b9-e38d-4468-8b5a-9d2c99efdb96/download/hkg_youth_15_24_2019-06-01_geotiff.zip
  format: null
  id: resource_f4ef66b9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: HKG_youth_15_24_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Hong Kong: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/dfd44ffe-bf3e-4a00-b69d-889e020918f7/resource/995ea9ac-51b4-4f31-b41c-cd6c20524f0a/download/population_hkg_2018-10-01_geotiff.zip
  format: null
  id: resource_995ea9ac
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_hkg_2018-10-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Hong Kong: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/dfd44ffe-bf3e-4a00-b69d-889e020918f7/resource/32894741-d587-4d31-9abc-baa235fcde64/download/population_hkg_2018-10-01.csv.zip
  format: null
  id: resource_32894741
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_hkg_2018-10-01.csv.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-hkg_metad4g_hongkonghighresolutionpop_201906
spatial:
  bbox: null
  centroid: null
  countries:
  - HKG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2019-06-21'
  start: '2019-06-19'
temporal_resolution: null
title: 'Hong Kong: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
