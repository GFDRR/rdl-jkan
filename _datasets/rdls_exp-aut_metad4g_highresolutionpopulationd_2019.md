---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook/Meta AI and Data for Good
    url: https://data.humdata.org/dataset/austria-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/austria-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/austria-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/austria-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-aut_metad4g_highresolutionpopulationd_2019
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Austria: (1) Overall population density
  (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly (ages
  60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/austria-high-resolution-population-density-maps-demographic-estimates]'
details: "To reference this data, please use the following citation: Facebook Connectivity\
  \ Lab and Center for International Earth Science Information Network - CIESIN -\
  \ Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery\
  \ for HRSL \xC2\xA9 2016 DigitalGlobe. Accessed DAY MONTH YEAR.' Please note that\
  \ as of 2024, Meta's high resolution population density maps are no longer being\
  \ updated."
exposure:
- asset_type:
    description: High-resolution gridded population density estimates for Austria
      disaggregated by age and gender demographics (overall, children 0-5, youth 15-24,
      elderly 60+, men, women, women of reproductive age 15-49)
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
    provide spatially-explicit population distributions disaggregated by age and gender
    for Austria at 2020.
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
- href: https://data.humdata.org/dataset/austria-high-resolution-population-density-maps-demographic-estimates
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
  description: 'Austria: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/66fa6572-0cf0-493d-8805-02a107169b29/resource/7b0ccb05-21bf-4b6a-9a56-6463e1f15d05/download/aut_general_2020_geotiff.zip
  format: null
  id: resource_7b0ccb05
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: aut_general_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Austria: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/66fa6572-0cf0-493d-8805-02a107169b29/resource/c168bb2f-6350-4d44-8789-3d2d22f5a2eb/download/aut_general_2020_csv.zip
  format: null
  id: resource_c168bb2f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: aut_general_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Austria: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/66fa6572-0cf0-493d-8805-02a107169b29/resource/05167d09-d4b8-4a70-a9b3-970811fe8e8d/download/aut_children_under_five_2020_geotiff.zip
  format: null
  id: resource_05167d09
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: aut_children_under_five_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Austria: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/66fa6572-0cf0-493d-8805-02a107169b29/resource/3c9d1436-1153-4671-96cb-5c5bfc3bb67e/download/aut_elderly_60_plus_2020_geotiff.zip
  format: null
  id: resource_3c9d1436
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: aut_elderly_60_plus_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Austria: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/66fa6572-0cf0-493d-8805-02a107169b29/resource/610f444a-b43c-4431-bbaf-f94d69fe6fd7/download/aut_men_2020_geotiff.zip
  format: null
  id: resource_610f444a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: aut_men_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Austria: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/66fa6572-0cf0-493d-8805-02a107169b29/resource/dd52dc4b-df82-4907-b315-718a4c4a921b/download/aut_women_2020_geotiff.zip
  format: null
  id: resource_dd52dc4b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: aut_women_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Austria: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/66fa6572-0cf0-493d-8805-02a107169b29/resource/3aedb713-ffa7-455c-88cb-74ce81afa742/download/aut_women_of_reproductive_age_15_49_2020_geotiff.zip
  format: null
  id: resource_3aedb713
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: aut_women_of_reproductive_age_15_49_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Austria: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/66fa6572-0cf0-493d-8805-02a107169b29/resource/d15d9d2f-070f-4588-95fd-df8545ca95cc/download/aut_youth_15_24_2020_geotiff.zip
  format: null
  id: resource_d15d9d2f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: aut_youth_15_24_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Austria: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/66fa6572-0cf0-493d-8805-02a107169b29/resource/81617a29-e3ed-49a8-9d00-c38142a82c7e/download/aut_children_under_five_2020_csv.zip
  format: null
  id: resource_81617a29
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: aut_children_under_five_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Austria: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/66fa6572-0cf0-493d-8805-02a107169b29/resource/b253b842-0f5e-4b2b-a81f-2fa21ad5c183/download/aut_elderly_60_plus_2020_csv.zip
  format: null
  id: resource_b253b842
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: aut_elderly_60_plus_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Austria: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/66fa6572-0cf0-493d-8805-02a107169b29/resource/97b215a8-35a0-4302-9c13-3cfde9a0f36e/download/aut_men_2020_csv.zip
  format: null
  id: resource_97b215a8
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: aut_men_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Austria: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/66fa6572-0cf0-493d-8805-02a107169b29/resource/be694512-3963-44a3-8dd3-fda720e808c8/download/aut_women_2020_csv.zip
  format: null
  id: resource_be694512
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: aut_women_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Austria: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/66fa6572-0cf0-493d-8805-02a107169b29/resource/d0da36bc-7271-4301-a9cd-2bf272542d0b/download/aut_women_of_reproductive_age_15_49_2020_csv.zip
  format: null
  id: resource_d0da36bc
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: aut_women_of_reproductive_age_15_49_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Austria: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/66fa6572-0cf0-493d-8805-02a107169b29/resource/b82538b4-aeb3-415d-9caa-11170363f760/download/aut_youth_15_24_2020_csv.zip
  format: null
  id: resource_b82538b4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: aut_youth_15_24_2020_csv.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-aut_metad4g_highresolutionpopulationd_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - AUT
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2021-04-30'
  start: '2019-09-19'
temporal_resolution: null
title: 'Austria: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
