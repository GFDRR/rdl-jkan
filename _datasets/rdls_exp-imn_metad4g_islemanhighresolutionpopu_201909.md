---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook/Meta AI and Data for Good
    url: https://data.humdata.org/dataset/isle-of-man-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/isle-of-man-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/isle-of-man-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/isle-of-man-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-imn_metad4g_islemanhighresolutionpopu_201909
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in the Isle of Man: (1) Overall population
  density (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly
  (ages 60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/isle-of-man-high-resolution-population-density-maps-demographic-estimates]'
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
    satellite imagery for the Isle of Man. Population estimates derived from publicly
    available census data were spatially distributed across identified buildings using
    Columbia University's population modeling approach, generating high-resolution
    demographic density maps for seven population subgroups.
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
- href: https://data.humdata.org/dataset/isle-of-man-high-resolution-population-density-maps-demographic-estimates
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
  description: 'Isle of Man: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/4f1863ce-ef39-4f6a-b608-0e5206652231/resource/d6ac5b85-1b11-467f-bad4-1dc6c8b56b49/download/imn_children_under_five_2019-08-03_csv.zip
  format: null
  id: resource_d6ac5b85
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: IMN_children_under_five_2019-08-03_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Isle of Man: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/4f1863ce-ef39-4f6a-b608-0e5206652231/resource/137526a1-7a8e-4850-9b3e-57d143981cc3/download/imn_elderly_60_plus_2019-08-03_csv.zip
  format: null
  id: resource_137526a1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: IMN_elderly_60_plus_2019-08-03_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Isle of Man: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/4f1863ce-ef39-4f6a-b608-0e5206652231/resource/a9e921c5-6105-4e8c-8249-2e322beef477/download/imn_men_2019-08-03_csv.zip
  format: null
  id: resource_a9e921c5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: IMN_men_2019-08-03_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Isle of Man: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/4f1863ce-ef39-4f6a-b608-0e5206652231/resource/67a68690-951b-4ed7-aedd-f03a06f5ed6c/download/imn_women_2019-08-03_csv.zip
  format: null
  id: resource_67a68690
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: IMN_women_2019-08-03_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Isle of Man: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/4f1863ce-ef39-4f6a-b608-0e5206652231/resource/db2c4e3f-711b-4c61-af53-2b86351faab8/download/imn_women_of_reproductive_age_15_49_2019-08-03_csv.zip
  format: null
  id: resource_db2c4e3f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: IMN_women_of_reproductive_age_15_49_2019-08-03_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Isle of Man: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/4f1863ce-ef39-4f6a-b608-0e5206652231/resource/d79e947c-ca89-48cf-a289-a1adfdf0f0ef/download/imn_youth_15_24_2019-08-03_csv.zip
  format: null
  id: resource_d79e947c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: IMN_youth_15_24_2019-08-03_csv.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-imn_metad4g_islemanhighresolutionpopu_201909
spatial:
  bbox: null
  centroid: null
  countries:
  - IMN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2019-09-23'
  start: '2019-09-19'
temporal_resolution: null
title: 'Isle of Man: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
