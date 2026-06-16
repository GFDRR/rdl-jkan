---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook (AI and Data for Good at Meta)
    url: https://data.humdata.org/dataset/uzbekistan-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/uzbekistan-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/uzbekistan-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/uzbekistan-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-uzb_metad4g_highresolutionpopulationd_201906
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Uzbekistan: (1) Overall population
  density (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly
  (ages 60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/uzbekistan-high-resolution-population-density-maps-demographic-estimates]'
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
  description: Machine learning algorithms identified building footprints from commercial
    satellite imagery across Uzbekistan. Population estimates derived from publicly
    available census data and demographic statistics were overlaid onto building locations
    using methodology developed with Columbia University partners. Seven separate
    gridded datasets were generated representing overall population density and demographic
    subgroups (age and gender cohorts) at high spatial resolution.
  sources:
  - id: source_1
    license: null
    name: Facebook (AI and Data for Good at Meta)
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
- href: https://data.humdata.org/dataset/uzbekistan-high-resolution-population-density-maps-demographic-estimates
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
  description: 'Uzbekistan: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/fe85f110-9b9d-42b8-884f-6add14ec7bb0/resource/5fad67eb-65f2-45de-9e55-31d1537dd14a/download/uzb_children_under_five_2019-06-01_csv.zip
  format: null
  id: resource_5fad67eb
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UZB_children_under_five_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Uzbekistan: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/fe85f110-9b9d-42b8-884f-6add14ec7bb0/resource/c75196ce-0275-470a-b9ec-9c08e6c04d5c/download/uzb_children_under_five_2019-06-01_geotiff.zip
  format: null
  id: resource_c75196ce
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UZB_children_under_five_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Uzbekistan: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/fe85f110-9b9d-42b8-884f-6add14ec7bb0/resource/8fbd9ed1-b91d-4c7a-bc7b-15062e97b89e/download/uzb_elderly_60_plus_2019-06-01_csv.zip
  format: null
  id: resource_8fbd9ed1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UZB_elderly_60_plus_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Uzbekistan: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/fe85f110-9b9d-42b8-884f-6add14ec7bb0/resource/2646276b-2145-4d88-8d0a-191e891dc882/download/uzb_elderly_60_plus_2019-06-01_geotiff.zip
  format: null
  id: resource_2646276b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UZB_elderly_60_plus_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Uzbekistan: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/fe85f110-9b9d-42b8-884f-6add14ec7bb0/resource/690c3b91-b9ad-473c-a59c-22ee895fa741/download/uzb_men_2019-06-01_csv.zip
  format: null
  id: resource_690c3b91
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UZB_men_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Uzbekistan: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/fe85f110-9b9d-42b8-884f-6add14ec7bb0/resource/f53aef5d-37f3-4f2c-ba96-022dc5dc02dc/download/uzb_men_2019-06-01_geotiff.zip
  format: null
  id: resource_f53aef5d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UZB_men_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Uzbekistan: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/fe85f110-9b9d-42b8-884f-6add14ec7bb0/resource/b9eaa4ab-5f2c-4b47-9ddc-acc35e22237e/download/uzb_women_2019-06-01_csv.zip
  format: null
  id: resource_b9eaa4ab
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UZB_women_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Uzbekistan: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/fe85f110-9b9d-42b8-884f-6add14ec7bb0/resource/29879b8c-2c80-45c8-a554-2dbb7c38d6be/download/uzb_women_2019-06-01_geotiff.zip
  format: null
  id: resource_29879b8c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UZB_women_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Uzbekistan: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/fe85f110-9b9d-42b8-884f-6add14ec7bb0/resource/dc2ceffd-375b-4af7-93d3-04fe7f78d0fc/download/uzb_women_of_reproductive_age_15_49_2019-06-01_csv.zip
  format: null
  id: resource_dc2ceffd
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UZB_women_of_reproductive_age_15_49_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Uzbekistan: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/fe85f110-9b9d-42b8-884f-6add14ec7bb0/resource/73266940-a2a9-4da3-b3f2-d6a15d56a6b7/download/uzb_women_of_reproductive_age_15_49_2019-06-01_geotiff.zip
  format: null
  id: resource_73266940
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UZB_women_of_reproductive_age_15_49_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Uzbekistan: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/fe85f110-9b9d-42b8-884f-6add14ec7bb0/resource/e3873737-57ba-4d12-841a-6f39e8f5c310/download/uzb_youth_15_24_2019-06-01_csv.zip
  format: null
  id: resource_e3873737
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UZB_youth_15_24_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Uzbekistan: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/fe85f110-9b9d-42b8-884f-6add14ec7bb0/resource/50c3e02b-1248-43fc-9bba-becc1571aa00/download/uzb_youth_15_24_2019-06-01_geotiff.zip
  format: null
  id: resource_50c3e02b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UZB_youth_15_24_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Uzbekistan: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/fe85f110-9b9d-42b8-884f-6add14ec7bb0/resource/8a2d743a-801d-4215-8b2d-8793672d3f1b/download/population_uzb_2018-10-01_geotiff.zip
  format: null
  id: resource_8a2d743a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_uzb_2018-10-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Uzbekistan: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/fe85f110-9b9d-42b8-884f-6add14ec7bb0/resource/b4352861-98db-49a2-afe2-38658946d47d/download/population_uzb_2018-10-01.csv.zip
  format: null
  id: resource_b4352861
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_uzb_2018-10-01.csv.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-uzb_metad4g_highresolutionpopulationd_201906
spatial:
  bbox: null
  centroid: null
  countries:
  - UZB
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2019-06-21'
  start: '2019-06-19'
temporal_resolution: null
title: 'Uzbekistan: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
