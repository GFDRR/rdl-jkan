---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook Data for Good
    url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-dji
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-dji
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-dji
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-dji
dataset_id: rdls_exp-dji_metad4g_highresolutionpopulationd_2019
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Djibouti: (1) Overall population
  density (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly
  (ages 60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-dji]'
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
  description: High-resolution population density maps were created by applying machine
    learning algorithms to identify building footprints from commercial satellite
    imagery, then overlaying population estimates derived from census data and demographic
    statistics in partnership with Columbia University. The resulting gridded datasets
    provide spatial distribution of total population and seven demographic subgroups
    across Djibouti at fine spatial resolution.
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
- href: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-dji
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
  description: 'Djibouti: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/f419e2e0-8f49-4c91-94d3-0b7a901aaef3/resource/101a1222-1a78-4ed4-af45-4af364bc5a05/download/dji_general_2020_geotiff.zip
  format: zip
  id: resource_101a1222
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dji_general_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Djibouti: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/f419e2e0-8f49-4c91-94d3-0b7a901aaef3/resource/f19a8335-9671-4f55-9dc7-62ea2772317d/download/dji_general_2020_csv.zip
  format: zip
  id: resource_f19a8335
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dji_general_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Djibouti: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/f419e2e0-8f49-4c91-94d3-0b7a901aaef3/resource/f3fafddd-94b4-4dec-af8c-bb40638ef0e7/download/dji_children_under_five_2020_csv.zip
  format: zip
  id: resource_f3fafddd
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dji_children_under_five_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Djibouti: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/f419e2e0-8f49-4c91-94d3-0b7a901aaef3/resource/e47e869b-f530-459c-a8b8-cfcc323f807a/download/dji_children_under_five_2020_geotiff.zip
  format: zip
  id: resource_e47e869b
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dji_children_under_five_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Djibouti: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/f419e2e0-8f49-4c91-94d3-0b7a901aaef3/resource/05c3dab9-03d6-49bf-addd-3a58d9cfcfd0/download/dji_elderly_60_plus_2020_csv.zip
  format: zip
  id: resource_05c3dab9
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dji_elderly_60_plus_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Djibouti: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/f419e2e0-8f49-4c91-94d3-0b7a901aaef3/resource/ef7c9650-3eef-4c5f-a882-b85d08980bcb/download/dji_elderly_60_plus_2020_geotiff.zip
  format: zip
  id: resource_ef7c9650
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dji_elderly_60_plus_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Djibouti: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/f419e2e0-8f49-4c91-94d3-0b7a901aaef3/resource/6b108b03-d31d-4086-bceb-3befc9f6ad41/download/dji_men_2020_csv.zip
  format: zip
  id: resource_6b108b03
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dji_men_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Djibouti: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/f419e2e0-8f49-4c91-94d3-0b7a901aaef3/resource/821f12f6-5d4c-4e9b-b754-e99b06a74d60/download/dji_men_2020_geotiff.zip
  format: zip
  id: resource_821f12f6
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dji_men_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Djibouti: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/f419e2e0-8f49-4c91-94d3-0b7a901aaef3/resource/a26848d3-8258-4d24-bf25-0250a5c735d6/download/dji_women_2020_csv.zip
  format: zip
  id: resource_a26848d3
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dji_women_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Djibouti: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/f419e2e0-8f49-4c91-94d3-0b7a901aaef3/resource/7383bec1-a4e8-49dc-b4fa-8c33b3a927cf/download/dji_women_2020_geotiff.zip
  format: zip
  id: resource_7383bec1
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dji_women_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Djibouti: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/f419e2e0-8f49-4c91-94d3-0b7a901aaef3/resource/d11da494-7349-4b38-9b40-4940c90e396e/download/dji_women_of_reproductive_age_15_49_2020_csv.zip
  format: zip
  id: resource_d11da494
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dji_women_of_reproductive_age_15_49_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Djibouti: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/f419e2e0-8f49-4c91-94d3-0b7a901aaef3/resource/e8e12cb6-2b16-4105-ad80-5e1b2410de76/download/dji_women_of_reproductive_age_15_49_2020_geotiff.zip
  format: zip
  id: resource_e8e12cb6
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dji_women_of_reproductive_age_15_49_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Djibouti: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/f419e2e0-8f49-4c91-94d3-0b7a901aaef3/resource/b3c77a5a-1f86-4a7c-8d96-20b716669216/download/dji_youth_15_24_2020_csv.zip
  format: zip
  id: resource_b3c77a5a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dji_youth_15_24_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Djibouti: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/f419e2e0-8f49-4c91-94d3-0b7a901aaef3/resource/89a55bca-a23b-4f6a-a0a5-00b91b872697/download/dji_youth_15_24_2020_geotiff.zip
  format: zip
  id: resource_89a55bca
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dji_youth_15_24_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This file has information about the cloud cover percentage and capture
    data of the satellite images used.
  download_url: https://data.humdata.org/dataset/f419e2e0-8f49-4c91-94d3-0b7a901aaef3/resource/aadfd0bf-7b11-422f-a97a-0630376d7d41/download/dji_dg_metadata.json.zip
  format: null
  id: resource_aadfd0bf
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dji_dg_metadata.json.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-dji_metad4g_highresolutionpopulationd_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - DJI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2022-10-21'
  start: '2019-05-20'
temporal_resolution: null
title: 'Djibouti: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
