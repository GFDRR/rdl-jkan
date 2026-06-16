---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook Data for Good
    url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-zaf
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-zaf
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-zaf
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-zaf
dataset_id: rdls_exp-zaf_metad4g_highresolutionpopulationd_2019
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in South Africa: (1) Overall population
  density (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly
  (ages 60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-zaf]'
details: "To reference this data, please use the following citation: Facebook Connectivity\
  \ Lab and Center for International Earth Science Information Network - CIESIN -\
  \ Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery\
  \ for HRSL \xC2\xA9 2016 DigitalGlobe. Accessed DAY MONTH YEAR.' Please note that\
  \ as of 2024, Meta's high resolution population density maps are no longer being\
  \ updated."
exposure:
- asset_type:
    description: High-resolution gridded population density estimates for South Africa
      disaggregated by age groups and gender (overall, children 0-5, youth 15-24,
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
license: CC-BY-4.0
lineage:
  description: Machine learning algorithms identified building footprints from commercial
    satellite imagery across South Africa. Population estimates derived from publicly
    available census data and demographic statistics were then spatially allocated
    to building locations using Columbia University's methodology, generating seven
    disaggregated population density grids (overall population and six demographic
    subgroups) at high spatial resolution for 2020.
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
    type: model
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-zaf
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
  description: 'South Africa: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/cbfc4206-35c8-42d4-a096-b2dd0aec983d/resource/d0ff7101-ba3e-490a-8fe9-57b9b6a0aa1f/download/zaf_general_2020_geotiff.zip
  format: zip
  id: resource_d0ff7101
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: zaf_general_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'South Africa: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/cbfc4206-35c8-42d4-a096-b2dd0aec983d/resource/ee4fbe8f-c75e-4f1b-8302-489b33e42426/download/zaf_general_2020_csv.zip
  format: zip
  id: resource_ee4fbe8f
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: zaf_general_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'South Africa: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/cbfc4206-35c8-42d4-a096-b2dd0aec983d/resource/3a65f31c-516a-49b2-a918-fba8ed6eb4d3/download/zaf_children_under_five_2020_csv.zip
  format: zip
  id: resource_3a65f31c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: zaf_children_under_five_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'South Africa: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/cbfc4206-35c8-42d4-a096-b2dd0aec983d/resource/4ad49175-0a0a-48d3-9135-196b14e01422/download/zaf_children_under_five_2020_geotiff.zip
  format: zip
  id: resource_4ad49175
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: zaf_children_under_five_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'South Africa: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/cbfc4206-35c8-42d4-a096-b2dd0aec983d/resource/25082ab6-22b1-47e1-b21b-c5e7b9d95fc2/download/zaf_elderly_60_plus_2020_csv.zip
  format: zip
  id: resource_25082ab6
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: zaf_elderly_60_plus_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'South Africa: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/cbfc4206-35c8-42d4-a096-b2dd0aec983d/resource/73ca9444-d68a-44ec-9c58-f9eb88cf6bc6/download/zaf_elderly_60_plus_2020_geotiff.zip
  format: zip
  id: resource_73ca9444
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: zaf_elderly_60_plus_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'South Africa: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/cbfc4206-35c8-42d4-a096-b2dd0aec983d/resource/53781f7c-6e0d-4b60-a3f5-21d93537c1b5/download/zaf_men_2020_csv.zip
  format: zip
  id: resource_53781f7c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: zaf_men_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'South Africa: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/cbfc4206-35c8-42d4-a096-b2dd0aec983d/resource/aef457b4-8104-4658-be0f-049478d336bd/download/zaf_men_2020_geotiff.zip
  format: zip
  id: resource_aef457b4
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: zaf_men_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'South Africa: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/cbfc4206-35c8-42d4-a096-b2dd0aec983d/resource/02e76c2e-a073-4b9b-8da0-7b5c7cd93d8c/download/zaf_women_2020_csv.zip
  format: zip
  id: resource_02e76c2e
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: zaf_women_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'South Africa: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/cbfc4206-35c8-42d4-a096-b2dd0aec983d/resource/27f8c8c2-026c-4824-b3f5-a3c49436b39c/download/zaf_women_2020_geotiff.zip
  format: zip
  id: resource_27f8c8c2
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: zaf_women_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'South Africa: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/cbfc4206-35c8-42d4-a096-b2dd0aec983d/resource/7ad761e9-096c-403a-a509-044566a518cc/download/zaf_women_of_reproductive_age_15_49_2020_csv.zip
  format: zip
  id: resource_7ad761e9
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: zaf_women_of_reproductive_age_15_49_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'South Africa: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/cbfc4206-35c8-42d4-a096-b2dd0aec983d/resource/43f8ee90-c287-40a3-8a2c-60af723750bf/download/zaf_women_of_reproductive_age_15_49_2020_geotiff.zip
  format: zip
  id: resource_43f8ee90
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: zaf_women_of_reproductive_age_15_49_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'South Africa: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/cbfc4206-35c8-42d4-a096-b2dd0aec983d/resource/083bf93b-4a26-44ac-9a3d-db405634fb9f/download/zaf_youth_15_24_2020_csv.zip
  format: zip
  id: resource_083bf93b
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: zaf_youth_15_24_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'South Africa: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/cbfc4206-35c8-42d4-a096-b2dd0aec983d/resource/fc4389c5-64c1-413d-9fd8-928f930af298/download/zaf_youth_15_24_2020_geotiff.zip
  format: zip
  id: resource_fc4389c5
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: zaf_youth_15_24_2020_geotiff.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-zaf_metad4g_highresolutionpopulationd_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - ZAF
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2022-06-09'
  start: '2019-05-20'
temporal_resolution: null
title: 'South Africa: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
