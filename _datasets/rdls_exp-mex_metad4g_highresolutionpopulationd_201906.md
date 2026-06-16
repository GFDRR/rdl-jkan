---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook Data for Good
    url: https://data.humdata.org/dataset/mexico-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/mexico-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/mexico-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/mexico-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-mex_metad4g_highresolutionpopulationd_201906
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Mexico: (1) Overall population density
  (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly (ages
  60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/mexico-high-resolution-population-density-maps-demographic-estimates]'
details: "To reference this data, please use the following citation: Facebook Connectivity\
  \ Lab and Center for International Earth Science Information Network - CIESIN -\
  \ Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery\
  \ for HRSL \xC2\xA9 2016 DigitalGlobe. Accessed DAY MONTH YEAR.' Please note that\
  \ as of 2024, Meta's high resolution population density maps are no longer being\
  \ updated."
exposure:
- asset_type:
    description: High-resolution gridded population density estimates for overall
      population and demographic subgroups (children, youth, elderly, women, reproductive-age
      women)
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
    census data and demographic statistics in partnership with Columbia University.
    The resulting gridded datasets represent spatial distributions of total population
    and demographic subgroups (age and gender cohorts) at fine spatial resolution
    across Mexico.
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
- href: https://data.humdata.org/dataset/mexico-high-resolution-population-density-maps-demographic-estimates
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
  description: 'Mexico: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/66ef8eab-b09e-4092-8d0f-2a9bd0727bdd/resource/eacb83a7-8306-4905-a0ad-677ab3b12e3e/download/population_mex_2018-10-01.csv.zip
  format: null
  id: resource_eacb83a7
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_mex_2018-10-01.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mexico: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/66ef8eab-b09e-4092-8d0f-2a9bd0727bdd/resource/003a8bf3-f618-4bba-953e-144731593473/download/population_mex_2018-10-01.zip
  format: null
  id: resource_003a8bf3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_mex_2018-10-01.geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mexico: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/66ef8eab-b09e-4092-8d0f-2a9bd0727bdd/resource/168530c5-0838-43eb-9a1e-0691a830a87a/download/mex_children_under_five_2019-06-01_csv.zip
  format: null
  id: resource_168530c5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MEX_children_under_five_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mexico: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/66ef8eab-b09e-4092-8d0f-2a9bd0727bdd/resource/0f52c45c-620c-4f68-80ee-809f7072bb50/download/mex_children_under_five_2019-06-01_geotiff.zip
  format: null
  id: resource_0f52c45c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MEX_children_under_five_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mexico: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/66ef8eab-b09e-4092-8d0f-2a9bd0727bdd/resource/a882e4ae-94a7-4eb2-a93f-0675c9a067ba/download/mex_elderly_60_plus_2019-06-01_csv.zip
  format: null
  id: resource_a882e4ae
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MEX_elderly_60_plus_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mexico: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/66ef8eab-b09e-4092-8d0f-2a9bd0727bdd/resource/c53a6a9f-50bd-4d72-a88e-9ec2df6736aa/download/mex_elderly_60_plus_2019-06-01_geotiff.zip
  format: null
  id: resource_c53a6a9f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MEX_elderly_60_plus_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mexico: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/66ef8eab-b09e-4092-8d0f-2a9bd0727bdd/resource/d0b9cc03-2ae7-4269-a5fe-51ce7b78d18b/download/mex_men_2019-06-01_csv.zip
  format: null
  id: resource_d0b9cc03
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MEX_men_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mexico: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/66ef8eab-b09e-4092-8d0f-2a9bd0727bdd/resource/c32b4460-0cf3-40a5-9d92-45c1c7606af7/download/mex_men_2019-06-01_geotiff.zip
  format: null
  id: resource_c32b4460
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MEX_men_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mexico: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/66ef8eab-b09e-4092-8d0f-2a9bd0727bdd/resource/450d86eb-0d1d-4f57-be39-12570cb40a61/download/mex_women_2019-06-01_csv.zip
  format: null
  id: resource_450d86eb
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MEX_women_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mexico: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/66ef8eab-b09e-4092-8d0f-2a9bd0727bdd/resource/813e1565-6fc9-4131-98cc-8eaa62c274ab/download/mex_women_2019-06-01_geotiff.zip
  format: null
  id: resource_813e1565
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MEX_women_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mexico: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/66ef8eab-b09e-4092-8d0f-2a9bd0727bdd/resource/ac7ebb85-99cf-46b9-9b0c-2ee0789879cd/download/mex_women_of_reproductive_age_15_49_2019-06-01_csv.zip
  format: null
  id: resource_ac7ebb85
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MEX_women_of_reproductive_age_15_49_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mexico: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/66ef8eab-b09e-4092-8d0f-2a9bd0727bdd/resource/65296439-5857-4001-9638-d507bd3fc162/download/mex_women_of_reproductive_age_15_49_2019-06-01_geotiff.zip
  format: null
  id: resource_65296439
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MEX_women_of_reproductive_age_15_49_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mexico: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/66ef8eab-b09e-4092-8d0f-2a9bd0727bdd/resource/a9fd6e5f-65cc-48da-aee7-29b7d50e7e18/download/mex_youth_15_24_2019-06-01_csv.zip
  format: null
  id: resource_a9fd6e5f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MEX_youth_15_24_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mexico: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/66ef8eab-b09e-4092-8d0f-2a9bd0727bdd/resource/61d8c8ef-51c9-488f-8cee-22612987ab9f/download/mex_youth_15_24_2019-06-01_geotiff.zip
  format: null
  id: resource_61d8c8ef
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MEX_youth_15_24_2019-06-01_geotiff.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-mex_metad4g_highresolutionpopulationd_201906
spatial:
  bbox: null
  centroid: null
  countries:
  - MEX
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2019-06-11'
  start: '2019-06-10'
temporal_resolution: null
title: 'Mexico: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
