---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook (Meta)
    url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-syc
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-syc
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-syc
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-syc
dataset_id: rdls_exp-syc_metad4g_highresolutionpopulationd_20190520
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Bangladesh: (1) Overall population
  density (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly
  (ages 60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-syc]'
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
    satellite imagery across Seychelles. Population estimates derived from publicly
    available census data and demographic statistics were spatially allocated to buildings
    and aggregated into high-resolution gridded maps for seven population categories
    (total, gender, age groups, reproductive age women).
  sources:
  - id: source_1
    license: null
    name: Facebook (Meta)
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
- href: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-syc
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
  description: 'Seychelles: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/1bcbfcc8-b5c8-4995-aac0-37d9c7ab7f0d/resource/29128f22-9176-4c41-beef-23c8fefcf6b8/download/population_syc_2018-10-01.zip
  format: null
  id: resource_29128f22
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_syc_2018-10-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Seychelles: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/1bcbfcc8-b5c8-4995-aac0-37d9c7ab7f0d/resource/e30ba71a-f6ef-400a-b1f6-4dca6dd22be7/download/population_syc_2018-10-01.csv.zip
  format: null
  id: resource_e30ba71a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_syc_2018-10-01.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Seychelles: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/1bcbfcc8-b5c8-4995-aac0-37d9c7ab7f0d/resource/57f53d5b-e817-480e-ab2e-3642a1a89aae/download/syc_children_under_five_csv.zip
  format: null
  id: resource_57f53d5b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SYC_children_under_five_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Seychelles: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/1bcbfcc8-b5c8-4995-aac0-37d9c7ab7f0d/resource/041d3754-f670-44d0-b753-d3e5f1dc9c6f/download/syc_children_under_five_geotiff.zip
  format: null
  id: resource_041d3754
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SYC_children_under_five_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Seychelles: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/1bcbfcc8-b5c8-4995-aac0-37d9c7ab7f0d/resource/f3ca8c90-eb56-4d8e-b0e0-68ee6d69aeba/download/syc_elderly_60_plus_csv.zip
  format: null
  id: resource_f3ca8c90
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SYC_elderly_60_plus_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Seychelles: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/1bcbfcc8-b5c8-4995-aac0-37d9c7ab7f0d/resource/b9520c71-8412-4d6a-b0ec-efe57798bcfa/download/syc_elderly_60_plus_geotiff.zip
  format: null
  id: resource_b9520c71
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SYC_elderly_60_plus_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Seychelles: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/1bcbfcc8-b5c8-4995-aac0-37d9c7ab7f0d/resource/462ea419-59b8-4643-8ba2-6460a3cfcda1/download/syc_men_csv.zip
  format: null
  id: resource_462ea419
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SYC_men_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Seychelles: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/1bcbfcc8-b5c8-4995-aac0-37d9c7ab7f0d/resource/009ca8a9-2931-4f9c-8e94-0a85b3b17ad4/download/syc_men_geotiff.zip
  format: null
  id: resource_009ca8a9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SYC_men_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Seychelles: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/1bcbfcc8-b5c8-4995-aac0-37d9c7ab7f0d/resource/3cd7404e-cd56-423e-aa0c-8abac862972f/download/syc_women_csv.zip
  format: null
  id: resource_3cd7404e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SYC_women_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Seychelles: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/1bcbfcc8-b5c8-4995-aac0-37d9c7ab7f0d/resource/b8c2822f-bd04-4d84-9456-36389c339142/download/syc_women_geotiff.zip
  format: null
  id: resource_b8c2822f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SYC_women_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Seychelles: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/1bcbfcc8-b5c8-4995-aac0-37d9c7ab7f0d/resource/db738875-1083-4894-bc29-6b3d0c038d7d/download/syc_women_of_reproductive_age_15_49_csv.zip
  format: null
  id: resource_db738875
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SYC_women_of_reproductive_age_15_49_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Seychelles: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/1bcbfcc8-b5c8-4995-aac0-37d9c7ab7f0d/resource/5b7706fd-33a0-4bd6-9e24-a014cbde32cf/download/syc_women_of_reproductive_age_15_49_geotiff.zip
  format: null
  id: resource_5b7706fd
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SYC_women_of_reproductive_age_15_49_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Seychelles: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/1bcbfcc8-b5c8-4995-aac0-37d9c7ab7f0d/resource/b8b0749c-d53a-44d8-ad9b-b366723e58f8/download/syc_youth_15_24_csv.zip
  format: null
  id: resource_b8b0749c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SYC_youth_15_24_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Seychelles: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/1bcbfcc8-b5c8-4995-aac0-37d9c7ab7f0d/resource/90c32099-fb30-473f-aea6-8dd98306cf13/download/syc_youth_15_24_geotiff.zip
  format: null
  id: resource_90c32099
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SYC_youth_15_24_geotiff.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-syc_metad4g_highresolutionpopulationd_20190520
spatial:
  bbox: null
  centroid: null
  countries:
  - SYC
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2019-05-20'
temporal_resolution: null
title: 'Seychelles: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
