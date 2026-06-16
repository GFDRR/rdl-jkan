---
attributions:
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-mwi
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-mwi
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-mwi
dataset_id: rdls_exp-mwi_metad4g_highresolutionpopulationd_2019
description: 'V1.5 The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Malawi: (1) Overall population density
  (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly (ages
  60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-mwi]'
details: "To reference this data, please use the following citation: Facebook Connectivity\
  \ Lab and Center for International Earth Science Information Network - CIESIN -\
  \ Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery\
  \ for HRSL \xC2\xA9 2016 DigitalGlobe. Accessed DAY MONTH YEAR.' Please note that\
  \ as of 2024, Meta's high resolution population density maps are no longer being\
  \ updated."
exposure:
- asset_type:
    description: High-resolution gridded population density for overall population
      and demographic subgroups (women, men, children 0-5, youth 15-24, elderly 60+,
      women of reproductive age 15-49)
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
    satellite imagery across Malawi. Population estimates derived from publicly available
    census data and demographic statistics were spatially distributed using Columbia
    University's methodology and overlaid onto the building-derived framework to create
    high-resolution gridded population density maps for seven demographic categories
    at the national scale.
  sources:
  - id: source_1
    license: null
    name: AI and Data for Good at Meta
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
- href: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-mwi
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
  description: 'Malawi: High Resolution Population Density Maps (ZIP archive)'
  download_url: https://data.humdata.org/dataset/8c2c0b1f-66af-4a8e-b30e-59ad2249ee24/resource/d83a3bad-b72a-4e4e-9be9-93b4c654ac0f/download/mwi_general_2020_geotiff.zip
  format: null
  id: resource_d83a3bad
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mwi_general_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Malawi: High Resolution Population Density Maps (ZIP archive)'
  download_url: https://data.humdata.org/dataset/8c2c0b1f-66af-4a8e-b30e-59ad2249ee24/resource/18dc65b1-f84f-4248-9068-5057e14e9fe9/download/mwi_general_2020_csv.zip
  format: null
  id: resource_18dc65b1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mwi_general_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Malawi: High Resolution Population Density Maps (ZIP archive)'
  download_url: https://data.humdata.org/dataset/8c2c0b1f-66af-4a8e-b30e-59ad2249ee24/resource/fee5c974-cc51-4e05-89df-c6df10c2fc60/download/mwi_youth_15_24_2020_csv.zip
  format: null
  id: resource_fee5c974
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mwi_youth_15_24_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Malawi: High Resolution Population Density Maps (ZIP archive)'
  download_url: https://data.humdata.org/dataset/8c2c0b1f-66af-4a8e-b30e-59ad2249ee24/resource/6bbe77b4-54df-4035-a8a0-7168f78b5bae/download/mwi_women_of_reproductive_age_15_49_2020_csv.zip
  format: null
  id: resource_6bbe77b4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mwi_women_of_reproductive_age_15_49_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Malawi: High Resolution Population Density Maps (ZIP archive)'
  download_url: https://data.humdata.org/dataset/8c2c0b1f-66af-4a8e-b30e-59ad2249ee24/resource/4675b46d-c5d5-43a9-9921-05dde646a2d4/download/mwi_men_2020_csv.zip
  format: null
  id: resource_4675b46d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mwi_men_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Malawi: High Resolution Population Density Maps (ZIP archive)'
  download_url: https://data.humdata.org/dataset/8c2c0b1f-66af-4a8e-b30e-59ad2249ee24/resource/809ba14a-8635-4aee-8a77-147f8f11c3bb/download/mwi_women_2020_csv.zip
  format: null
  id: resource_809ba14a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mwi_women_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Malawi: High Resolution Population Density Maps (ZIP archive)'
  download_url: https://data.humdata.org/dataset/8c2c0b1f-66af-4a8e-b30e-59ad2249ee24/resource/bb3bdf2c-924b-449e-969d-371c10c27d92/download/mwi_elderly_60_plus_2020_csv.zip
  format: null
  id: resource_bb3bdf2c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mwi_elderly_60_plus_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Malawi: High Resolution Population Density Maps (ZIP archive)'
  download_url: https://data.humdata.org/dataset/8c2c0b1f-66af-4a8e-b30e-59ad2249ee24/resource/23e0da95-a7bf-4454-af53-35059efeed69/download/mwi_children_under_five_2020_csv.zip
  format: null
  id: resource_23e0da95
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mwi_children_under_five_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Malawi: High Resolution Population Density Maps (ZIP archive)'
  download_url: https://data.humdata.org/dataset/8c2c0b1f-66af-4a8e-b30e-59ad2249ee24/resource/572791d1-3298-47b7-b299-ee3ed6d7ef12/download/mwi_women_of_reproductive_age_15_49_2020_geotiff.zip
  format: null
  id: resource_572791d1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mwi_women_of_reproductive_age_15_49_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Malawi: High Resolution Population Density Maps (ZIP archive)'
  download_url: https://data.humdata.org/dataset/8c2c0b1f-66af-4a8e-b30e-59ad2249ee24/resource/f214fabd-ffcf-48d2-9958-ddeb5def8664/download/mwi_men_2020_geotiff.zip
  format: null
  id: resource_f214fabd
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mwi_men_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Malawi: High Resolution Population Density Maps (ZIP archive)'
  download_url: https://data.humdata.org/dataset/8c2c0b1f-66af-4a8e-b30e-59ad2249ee24/resource/c6cc692e-084d-443f-9761-6f52a0331fd3/download/mwi_women_2020_geotiff.zip
  format: null
  id: resource_c6cc692e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mwi_women_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Malawi: High Resolution Population Density Maps (ZIP archive)'
  download_url: https://data.humdata.org/dataset/8c2c0b1f-66af-4a8e-b30e-59ad2249ee24/resource/6de83337-c289-437b-b81d-cb1a805c777a/download/mwi_youth_15_24_2020_geotiff.zip
  format: null
  id: resource_6de83337
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mwi_youth_15_24_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Malawi: High Resolution Population Density Maps (ZIP archive)'
  download_url: https://data.humdata.org/dataset/8c2c0b1f-66af-4a8e-b30e-59ad2249ee24/resource/be537dd2-258a-459b-b02c-cc3d67d4987c/download/mwi_elderly_60_plus_2020_geotiff.zip
  format: null
  id: resource_be537dd2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mwi_elderly_60_plus_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Malawi: High Resolution Population Density Maps (ZIP archive)'
  download_url: https://data.humdata.org/dataset/8c2c0b1f-66af-4a8e-b30e-59ad2249ee24/resource/a8a11a89-bf4e-4f7b-b077-dce67e9b1c27/download/mwi_children_under_five_2020_geotiff.zip
  format: null
  id: resource_a8a11a89
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mwi_children_under_five_2020_geotiff.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-mwi_metad4g_highresolutionpopulationd_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - MWI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2021-08-07'
  start: '2019-05-20'
temporal_resolution: null
title: 'Malawi: High Resolution Population Density Maps'
version: null
vulnerability: null
---
