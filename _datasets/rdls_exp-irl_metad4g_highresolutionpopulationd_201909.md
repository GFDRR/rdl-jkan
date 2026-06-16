---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook/Meta AI and Data for Good
    url: https://data.humdata.org/dataset/ireland-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/ireland-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/ireland-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/ireland-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-irl_metad4g_highresolutionpopulationd_201909
description: 'These high-resolution maps estimate not only the number of people living
  within 30-meter grid tiles, but also provide insights on demographics at unprecedentedly
  high resolutions. These maps aren''t built using Facebook data and instead rely
  on combining the power of machine vision AI with satellite imagery and census information..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/ireland-high-resolution-population-density-maps-demographic-estimates]'
details: "To reference this data, please use the following citation: Facebook Connectivity\
  \ Lab and Center for International Earth Science Information Network - CIESIN -\
  \ Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery\
  \ for HRSL \xC2\xA9 2016 DigitalGlobe. Accessed DAY MONTH YEAR.'"
exposure:
- asset_type:
    description: High-resolution gridded population estimates at 30-meter resolution
      with demographic disaggregation by age and sex groups
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
    census data and demographic statistics. The resulting 30-meter gridded datasets
    provide population counts disaggregated by age groups (children under 5, youth
    15-24, women of reproductive age 15-49, elderly 60+) and sex, enabling demographic
    analysis at unprecedented spatial resolution for Ireland.
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
- href: https://data.humdata.org/dataset/ireland-high-resolution-population-density-maps-demographic-estimates
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
  description: 'Ireland: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/51bd8e7b-b7a2-4efa-8f1f-7e2361633945/resource/464597e8-a006-4f8c-b9ca-d1594d37f051/download/irl_children_under_five_geotiff.zip
  format: null
  id: resource_464597e8
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: IRL_children_under_five_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Ireland: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/51bd8e7b-b7a2-4efa-8f1f-7e2361633945/resource/7e0e632e-3f82-4c4a-bb88-032e10016463/download/irl_elderly_60_plus_geotiff.zip
  format: null
  id: resource_7e0e632e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: IRL_elderly_60_plus_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Ireland: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/51bd8e7b-b7a2-4efa-8f1f-7e2361633945/resource/34870206-1583-44c6-84f3-95d7daa2aca1/download/irl_men_geotiff.zip
  format: null
  id: resource_34870206
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: IRL_men_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Ireland: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/51bd8e7b-b7a2-4efa-8f1f-7e2361633945/resource/b2e53f84-ee35-4efa-8f8e-299fb317d183/download/irl_women_geotiff.zip
  format: null
  id: resource_b2e53f84
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: IRL_women_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Ireland: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/51bd8e7b-b7a2-4efa-8f1f-7e2361633945/resource/f5db6eb8-f68f-40ae-b87d-488b4d65c4f7/download/irl_women_of_reproductive_age_15_49_geotiff.zip
  format: null
  id: resource_f5db6eb8
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: IRL_women_of_reproductive_age_15_49_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Ireland: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/51bd8e7b-b7a2-4efa-8f1f-7e2361633945/resource/87c97c59-7f28-49fe-bd4a-68cb7a3e4fd8/download/irl_youth_15_24_geotiff.zip
  format: null
  id: resource_87c97c59
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: IRL_youth_15_24_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Ireland: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/51bd8e7b-b7a2-4efa-8f1f-7e2361633945/resource/82cd0497-b6da-4795-b923-072e488bc3a9/download/irl_children_under_five_2019-08-03_csv.zip
  format: null
  id: resource_82cd0497
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: IRL_children_under_five_2019-08-03_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Ireland: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/51bd8e7b-b7a2-4efa-8f1f-7e2361633945/resource/70b99845-7cb7-4e10-8126-52a9c90baf5e/download/irl_elderly_60_plus_2019-08-03_csv.zip
  format: null
  id: resource_70b99845
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: IRL_elderly_60_plus_2019-08-03_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Ireland: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/51bd8e7b-b7a2-4efa-8f1f-7e2361633945/resource/4966c7b5-399d-408c-9589-a0d1cd6e308c/download/irl_men_2019-08-03_csv.zip
  format: null
  id: resource_4966c7b5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: IRL_men_2019-08-03_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Ireland: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/51bd8e7b-b7a2-4efa-8f1f-7e2361633945/resource/609c83d6-6788-417e-af43-72521b8ecf85/download/irl_women_2019-08-03_csv.zip
  format: null
  id: resource_609c83d6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: IRL_women_2019-08-03_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Ireland: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/51bd8e7b-b7a2-4efa-8f1f-7e2361633945/resource/20521d1a-65b4-4fea-9344-31679375cfdc/download/irl_women_of_reproductive_age_15_49_2019-08-03_csv.zip
  format: null
  id: resource_20521d1a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: IRL_women_of_reproductive_age_15_49_2019-08-03_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Ireland: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/51bd8e7b-b7a2-4efa-8f1f-7e2361633945/resource/2a13311d-56ee-4e26-80a2-7c446ba92adc/download/irl_youth_15_24_2019-08-03_csv.zip
  format: null
  id: resource_2a13311d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: IRL_youth_15_24_2019-08-03_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Ireland: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/51bd8e7b-b7a2-4efa-8f1f-7e2361633945/resource/2e51dfe3-82c7-4ad2-91ba-42ebcd121dab/download/population_irl_2019-07-01_geotiff.zip
  format: null
  id: resource_2e51dfe3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_irl_2019-07-01_geotiff.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-irl_metad4g_highresolutionpopulationd_201909
spatial:
  bbox: null
  centroid: null
  countries:
  - IRL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2019-09-27'
  start: '2019-09-19'
temporal_resolution: null
title: 'Ireland: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
