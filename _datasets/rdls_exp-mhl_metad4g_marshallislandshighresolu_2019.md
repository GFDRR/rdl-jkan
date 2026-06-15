---
attributions:
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/marshall-islands-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/marshall-islands-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/marshall-islands-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-mhl_metad4g_marshallislandshighresolu_2019
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in the Marshall Islands: (1) Overall
  population density (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24)
  (6) Elderly (ages 60+) (7) Women of reproductive age (ages 15-49).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/marshall-islands-high-resolution-population-density-maps-demographic-estimates]'
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
    statistics in collaboration with Columbia University. The resulting gridded datasets
    represent population distribution at fine spatial resolution for the Marshall
    Islands in 2020, disaggregated by demographic groups.
  sources:
  - id: source_1
    license: null
    name: AI and Data for Good at Meta
    risk_data_type:
    - exposure
    type: model
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
- href: https://data.humdata.org/dataset/marshall-islands-high-resolution-population-density-maps-demographic-estimates
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
  description: 'Marshall Islands: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/c7673756-c2ea-4747-a3b3-18bc50dbdb34/resource/6e13fbd2-758b-46a8-a627-3e0992f34771/download/mhl_children_under_five_2020_csv.zip
  format: zip
  id: resource_6e13fbd2
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mhl_children_under_five_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Marshall Islands: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/c7673756-c2ea-4747-a3b3-18bc50dbdb34/resource/046b282c-b656-42f9-a653-dae8778adae0/download/mhl_children_under_five_2020_geotiff.zip
  format: zip
  id: resource_046b282c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mhl_children_under_five_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Marshall Islands: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/c7673756-c2ea-4747-a3b3-18bc50dbdb34/resource/1513c36c-2f76-489f-b175-d0a004d8074a/download/mhl_elderly_60_plus_2020_csv.zip
  format: zip
  id: resource_1513c36c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mhl_elderly_60_plus_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Marshall Islands: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/c7673756-c2ea-4747-a3b3-18bc50dbdb34/resource/44f4846c-a4ae-4863-9024-9e3cfe3ea05c/download/mhl_elderly_60_plus_2020_geotiff.zip
  format: zip
  id: resource_44f4846c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mhl_elderly_60_plus_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Marshall Islands: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/c7673756-c2ea-4747-a3b3-18bc50dbdb34/resource/57b3ec86-0f65-465a-b495-aca48b517506/download/mhl_men_2020_csv.zip
  format: zip
  id: resource_57b3ec86
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mhl_men_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Marshall Islands: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/c7673756-c2ea-4747-a3b3-18bc50dbdb34/resource/0adb344e-9b86-43ae-9d05-253840db7bc9/download/mhl_men_2020_geotiff.zip
  format: zip
  id: resource_0adb344e
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mhl_men_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Marshall Islands: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/c7673756-c2ea-4747-a3b3-18bc50dbdb34/resource/0a652670-3b4b-4ecf-a20b-81ccafe5a3cc/download/mhl_women_2020_csv.zip
  format: zip
  id: resource_0a652670
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mhl_women_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Marshall Islands: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/c7673756-c2ea-4747-a3b3-18bc50dbdb34/resource/b3245409-ae63-4764-b061-8917203c9a38/download/mhl_women_2020_geotiff.zip
  format: zip
  id: resource_b3245409
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mhl_women_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Marshall Islands: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/c7673756-c2ea-4747-a3b3-18bc50dbdb34/resource/79037207-151b-4913-9334-06fdd0ff67a0/download/mhl_women_of_reproductive_age_15_49_2020_csv.zip
  format: zip
  id: resource_79037207
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mhl_women_of_reproductive_age_15_49_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Marshall Islands: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/c7673756-c2ea-4747-a3b3-18bc50dbdb34/resource/ad4427bf-7f97-4845-9685-3136a9d81c2e/download/mhl_women_of_reproductive_age_15_49_2020_geotiff.zip
  format: zip
  id: resource_ad4427bf
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mhl_women_of_reproductive_age_15_49_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Marshall Islands: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/c7673756-c2ea-4747-a3b3-18bc50dbdb34/resource/ca515aa6-608f-4f04-96f9-5a5057740eb2/download/mhl_youth_15_24_2020_csv.zip
  format: zip
  id: resource_ca515aa6
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mhl_youth_15_24_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Marshall Islands: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/c7673756-c2ea-4747-a3b3-18bc50dbdb34/resource/d639251a-ea2f-4b93-82c7-5718ab8c6d47/download/mhl_youth_15_24_2020_geotiff.zip
  format: zip
  id: resource_d639251a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mhl_youth_15_24_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Marshall Islands: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/c7673756-c2ea-4747-a3b3-18bc50dbdb34/resource/2bd6498a-cd7e-495b-a1a1-3a482efeb367/download/mhl_general_2020_geotiff.zip
  format: zip
  id: resource_2bd6498a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mhl_general_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Marshall Islands: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/c7673756-c2ea-4747-a3b3-18bc50dbdb34/resource/a442c0de-df21-496e-9220-80e4d3360259/download/mhl_general_2020_csv.zip
  format: zip
  id: resource_a442c0de
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mhl_general_2020_csv.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-mhl_metad4g_marshallislandshighresolu_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - MHL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-03-11'
  start: '2019-06-19'
temporal_resolution: null
title: 'Marshall Islands: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
