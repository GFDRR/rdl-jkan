---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook Data for Good
    url: https://data.humdata.org/dataset/turks-and-caicos-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/turks-and-caicos-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/turks-and-caicos-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/turks-and-caicos-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-tca_metad4g_turkscaicoshighresolution_201906
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Turks and Caicos: (1) Overall population
  density (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly
  (ages 60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/turks-and-caicos-high-resolution-population-density-maps-demographic-estimates]'
details: "To reference this data, please use the following citation: Facebook Connectivity\
  \ Lab and Center for International Earth Science Information Network - CIESIN -\
  \ Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery\
  \ for HRSL \xC2\xA9 2016 DigitalGlobe. Accessed DAY MONTH YEAR.' Please note that\
  \ as of 2024, Meta's high resolution population density maps are no longer being\
  \ updated."
exposure:
- asset_type:
    description: High-resolution gridded population density estimates disaggregated
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
    satellite imagery. Population estimates derived from publicly available census
    data and demographic statistics were spatially allocated to building locations
    using Columbia University's population estimation methodology, producing seven
    demographic-disaggregated population density grids at high spatial resolution.
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
- href: https://data.humdata.org/dataset/turks-and-caicos-high-resolution-population-density-maps-demographic-estimates
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
  description: 'Turks and Caicos Islands - Turks and Caicos: High Resolution Population
    Density Maps + Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/9e522af0-abb1-4d72-8c00-5d1220419fa7/resource/47ced10b-870e-4d08-bb27-5b6726375bc6/download/population_tca_2018-10-01.csv.zip
  format: null
  id: resource_47ced10b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_tca_2018-10-01.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Turks and Caicos Islands - Turks and Caicos: High Resolution Population
    Density Maps + Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/9e522af0-abb1-4d72-8c00-5d1220419fa7/resource/a163a664-1ce1-437a-aec0-47f5a52b168c/download/population_tca_2018-10-01.zip
  format: null
  id: resource_a163a664
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_tca_2018-10-01.geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Turks and Caicos Islands - Turks and Caicos: High Resolution Population
    Density Maps + Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/9e522af0-abb1-4d72-8c00-5d1220419fa7/resource/a601632d-5cf2-459c-a214-9b2e659fbca6/download/tca_children_under_five_2019-06-01_csv.zip
  format: null
  id: resource_a601632d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TCA_children_under_five_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Turks and Caicos Islands - Turks and Caicos: High Resolution Population
    Density Maps + Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/9e522af0-abb1-4d72-8c00-5d1220419fa7/resource/4f2b37e0-057f-4030-9510-302b8f657db9/download/tca_children_under_five_2019-06-01_geotiff.zip
  format: null
  id: resource_4f2b37e0
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TCA_children_under_five_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Turks and Caicos Islands - Turks and Caicos: High Resolution Population
    Density Maps + Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/9e522af0-abb1-4d72-8c00-5d1220419fa7/resource/35c92fc7-f7c3-4dd4-bcca-f75e5b3fdd23/download/tca_elderly_60_plus_2019-06-01_csv.zip
  format: null
  id: resource_35c92fc7
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TCA_elderly_60_plus_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Turks and Caicos Islands - Turks and Caicos: High Resolution Population
    Density Maps + Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/9e522af0-abb1-4d72-8c00-5d1220419fa7/resource/929145da-6f65-4916-a08b-1c64d7184304/download/tca_elderly_60_plus_2019-06-01_geotiff.zip
  format: null
  id: resource_929145da
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TCA_elderly_60_plus_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Turks and Caicos Islands - Turks and Caicos: High Resolution Population
    Density Maps + Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/9e522af0-abb1-4d72-8c00-5d1220419fa7/resource/22d1a9b4-c64b-4d0e-9fde-a3eb5111979c/download/tca_men_2019-06-01_csv.zip
  format: null
  id: resource_22d1a9b4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TCA_men_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Turks and Caicos Islands - Turks and Caicos: High Resolution Population
    Density Maps + Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/9e522af0-abb1-4d72-8c00-5d1220419fa7/resource/b9e8c824-3c30-49d2-87fb-707434c5e56b/download/tca_men_2019-06-01_geotiff.zip
  format: null
  id: resource_b9e8c824
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TCA_men_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Turks and Caicos Islands - Turks and Caicos: High Resolution Population
    Density Maps + Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/9e522af0-abb1-4d72-8c00-5d1220419fa7/resource/5d069b8a-a43b-45f6-9c75-597ee52de7fb/download/tca_women_2019-06-01_csv.zip
  format: null
  id: resource_5d069b8a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TCA_women_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Turks and Caicos Islands - Turks and Caicos: High Resolution Population
    Density Maps + Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/9e522af0-abb1-4d72-8c00-5d1220419fa7/resource/5b9f2082-45ae-4799-ab19-7c448b9070a8/download/tca_women_2019-06-01_geotiff.zip
  format: null
  id: resource_5b9f2082
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TCA_women_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Turks and Caicos Islands - Turks and Caicos: High Resolution Population
    Density Maps + Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/9e522af0-abb1-4d72-8c00-5d1220419fa7/resource/ef9be961-18b4-4129-81a9-103e59bb6687/download/tca_women_of_reproductive_age_15_49_2019-06-01_csv.zip
  format: null
  id: resource_ef9be961
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TCA_women_of_reproductive_age_15_49_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Turks and Caicos Islands - Turks and Caicos: High Resolution Population
    Density Maps + Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/9e522af0-abb1-4d72-8c00-5d1220419fa7/resource/e0898831-3bdd-4f7a-9974-d2c364185993/download/tca_women_of_reproductive_age_15_49_2019-06-01_geotiff.zip
  format: null
  id: resource_e0898831
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TCA_women_of_reproductive_age_15_49_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Turks and Caicos Islands - Turks and Caicos: High Resolution Population
    Density Maps + Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/9e522af0-abb1-4d72-8c00-5d1220419fa7/resource/c207a84b-b010-4f40-8880-781427e9b2d7/download/tca_youth_15_24_2019-06-01_csv.zip
  format: null
  id: resource_c207a84b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TCA_youth_15_24_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Turks and Caicos Islands - Turks and Caicos: High Resolution Population
    Density Maps + Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/9e522af0-abb1-4d72-8c00-5d1220419fa7/resource/237cde14-d97a-453f-a8c2-440b783d8033/download/tca_youth_15_24_2019-06-01_geotiff.zip
  format: null
  id: resource_237cde14
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TCA_youth_15_24_2019-06-01_geotiff.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-tca_metad4g_turkscaicoshighresolution_201906
spatial:
  bbox: null
  centroid: null
  countries:
  - TCA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2019-06-11'
  start: '2019-06-10'
temporal_resolution: null
title: 'Turks and Caicos Islands - Turks and Caicos: High Resolution Population Density
  Maps + Demographic Estimates'
version: null
vulnerability: null
---
