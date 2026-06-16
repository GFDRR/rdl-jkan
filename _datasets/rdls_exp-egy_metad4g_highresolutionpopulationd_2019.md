---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook Data for Good
    url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-egy
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-egy
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-egy
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-egy
dataset_id: rdls_exp-egy_metad4g_highresolutionpopulationd_2019
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Egypt: (1) Overall population density
  (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly (ages
  60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-egy]'
details: "To reference this data, please use the following citation: Facebook Connectivity\
  \ Lab and Center for International Earth Science Information Network - CIESIN -\
  \ Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery\
  \ for HRSL \xC2\xA9 2016 DigitalGlobe. Accessed DAY MONTH YEAR.' Please note that\
  \ as of 2024, Meta's high resolution population density maps are no longer being\
  \ updated."
exposure:
- asset_type:
    description: High-resolution gridded population density estimates for Egypt disaggregated
      by demographic groups (overall, women, men, children 0-5, youth 15-24, elderly
      60+, women of reproductive age 15-49)
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
    satellite imagery across Egypt. Population estimates derived from publicly available
    census data and demographic statistics were then spatially allocated to these
    building-level units using Columbia University's methodology, producing seven
    high-resolution gridded population density maps disaggregated by demographic cohorts
    for 2020.
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
- href: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-egy
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
  description: 'Egypt: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e5987778-99d2-4243-9cca-2b32f539df86/resource/6fe9955c-5fec-4b6d-8102-5129d1aada3f/download/egy_general_2020_geotiff.zip
  format: zip
  id: resource_6fe9955c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: egy_general_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Egypt: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e5987778-99d2-4243-9cca-2b32f539df86/resource/51c3e599-11e4-4097-a4d5-0e02c39467dd/download/egy_general_2020_csv.zip
  format: zip
  id: resource_51c3e599
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: egy_general_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Egypt: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e5987778-99d2-4243-9cca-2b32f539df86/resource/f7e04365-8f3f-4268-a29d-d2f54075bc6d/download/egy_children_under_five_2020_csv.zip
  format: zip
  id: resource_f7e04365
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: egy_children_under_five_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Egypt: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e5987778-99d2-4243-9cca-2b32f539df86/resource/5803d9de-423c-4456-bcd4-6c5b6850ace3/download/egy_children_under_five_2020_geotiff.zip
  format: zip
  id: resource_5803d9de
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: egy_children_under_five_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Egypt: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e5987778-99d2-4243-9cca-2b32f539df86/resource/607d78b7-c839-464b-ad78-69d619240469/download/egy_elderly_60_plus_2020_csv.zip
  format: zip
  id: resource_607d78b7
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: egy_elderly_60_plus_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Egypt: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e5987778-99d2-4243-9cca-2b32f539df86/resource/44cf3679-732e-4efc-b335-c80f2d7bb588/download/egy_elderly_60_plus_2020_geotiff.zip
  format: zip
  id: resource_44cf3679
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: egy_elderly_60_plus_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Egypt: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e5987778-99d2-4243-9cca-2b32f539df86/resource/cb4fae09-1b31-4f59-9cb3-b1cf5e21025e/download/egy_men_2020_csv.zip
  format: zip
  id: resource_cb4fae09
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: egy_men_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Egypt: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e5987778-99d2-4243-9cca-2b32f539df86/resource/c85ad5c8-36e3-4b89-a0f2-9a5fec477a64/download/egy_men_2020_geotiff.zip
  format: zip
  id: resource_c85ad5c8
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: egy_men_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Egypt: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e5987778-99d2-4243-9cca-2b32f539df86/resource/aa5f5287-53e8-4cc9-8828-7e586a00871f/download/egy_women_2020_csv.zip
  format: zip
  id: resource_aa5f5287
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: egy_women_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Egypt: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e5987778-99d2-4243-9cca-2b32f539df86/resource/9812374b-44ed-4a0e-afc5-b7bcfd1f483c/download/egy_women_2020_geotiff.zip
  format: zip
  id: resource_9812374b
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: egy_women_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Egypt: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e5987778-99d2-4243-9cca-2b32f539df86/resource/3b52d3da-fa4f-421f-bd6d-d97316304943/download/egy_women_of_reproductive_age_15_49_2020_csv.zip
  format: zip
  id: resource_3b52d3da
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: egy_women_of_reproductive_age_15_49_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Egypt: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e5987778-99d2-4243-9cca-2b32f539df86/resource/b6025119-fb16-4f95-8382-6685c968b5f9/download/egy_women_of_reproductive_age_15_49_2020_geotiff.zip
  format: zip
  id: resource_b6025119
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: egy_women_of_reproductive_age_15_49_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Egypt: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e5987778-99d2-4243-9cca-2b32f539df86/resource/c6984ee9-2458-4af2-b99d-6bb8eb97d78f/download/egy_youth_15_24_2020_csv.zip
  format: zip
  id: resource_c6984ee9
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: egy_youth_15_24_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Egypt: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e5987778-99d2-4243-9cca-2b32f539df86/resource/9e8c101c-cd5e-4b1a-90f2-3a5d9b949c61/download/egy_youth_15_24_2020_geotiff.zip
  format: zip
  id: resource_9e8c101c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: egy_youth_15_24_2020_geotiff.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-egy_metad4g_highresolutionpopulationd_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - EGY
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2022-08-26'
  start: '2019-05-20'
temporal_resolution: null
title: 'Egypt: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
