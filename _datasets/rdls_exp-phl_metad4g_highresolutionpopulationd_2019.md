---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook
    url: https://data.humdata.org/dataset/philippines-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/philippines-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/philippines-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/philippines-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-phl_metad4g_highresolutionpopulationd_2019
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in the Philippines: (1) Overall population
  density (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly
  (ages 60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/philippines-high-resolution-population-density-maps-demographic-estimates]'
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
license: CC-BY-4.0
lineage:
  description: High-resolution population density maps were created by applying machine
    learning algorithms to commercially available satellite imagery to identify building
    footprints, then overlaying general population estimates derived from publicly
    available census data and demographic statistics in partnership with Columbia
    University. The resulting gridded datasets provide spatial distribution of overall
    population and seven demographic subgroups across the Philippines at fine spatial
    resolution.
  sources:
  - id: source_1
    license: null
    name: Facebook
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
- href: https://data.humdata.org/dataset/philippines-high-resolution-population-density-maps-demographic-estimates
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
  description: 'Philippines: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/6d9f35c0-4764-49ee-b364-329db0b7a47d/resource/ce2fe08c-ed2c-493f-a5a1-c1b5e578f7c3/download/phl_children_under_five_2020_csv.zip
  format: zip
  id: resource_ce2fe08c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: phl_children_under_five_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Philippines: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/6d9f35c0-4764-49ee-b364-329db0b7a47d/resource/6ec111d4-900d-47cf-a7ad-39899c8a6fdc/download/phl_children_under_five_2020_geotiff.zip
  format: zip
  id: resource_6ec111d4
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: phl_children_under_five_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Philippines: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/6d9f35c0-4764-49ee-b364-329db0b7a47d/resource/5e79ee23-7f1c-492e-9a7a-659c072ea42a/download/phl_elderly_60_plus_2020_csv.zip
  format: zip
  id: resource_5e79ee23
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: phl_elderly_60_plus_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Philippines: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/6d9f35c0-4764-49ee-b364-329db0b7a47d/resource/c032d20a-aaba-4cf4-8c2d-f356d5862fc3/download/phl_elderly_60_plus_2020_geotiff.zip
  format: zip
  id: resource_c032d20a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: phl_elderly_60_plus_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Philippines: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/6d9f35c0-4764-49ee-b364-329db0b7a47d/resource/741affc2-9f8a-42db-bcb3-64ca367806c5/download/phl_men_2020_csv.zip
  format: zip
  id: resource_741affc2
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: phl_men_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Philippines: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/6d9f35c0-4764-49ee-b364-329db0b7a47d/resource/5a13bb60-4506-42a5-a08a-7ccf20413179/download/phl_men_2020_geotiff.zip
  format: zip
  id: resource_5a13bb60
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: phl_men_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Philippines: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/6d9f35c0-4764-49ee-b364-329db0b7a47d/resource/fed7e3cd-244c-41d9-8ba5-3b39b3588746/download/phl_women_2020_csv.zip
  format: zip
  id: resource_fed7e3cd
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: phl_women_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Philippines: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/6d9f35c0-4764-49ee-b364-329db0b7a47d/resource/4aff438c-43d9-47d0-853f-5a6b6ae28223/download/phl_women_2020_geotiff.zip
  format: zip
  id: resource_4aff438c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: phl_women_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Philippines: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/6d9f35c0-4764-49ee-b364-329db0b7a47d/resource/2800496c-995b-4fb6-abed-d0cb01184255/download/phl_women_of_reproductive_age_15_49_2020_csv.zip
  format: zip
  id: resource_2800496c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: phl_women_of_reproductive_age_15_49_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Philippines: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/6d9f35c0-4764-49ee-b364-329db0b7a47d/resource/1e837a18-1283-4cce-8a86-b72dad87d5de/download/phl_women_of_reproductive_age_15_49_2020_geotiff.zip
  format: zip
  id: resource_1e837a18
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: phl_women_of_reproductive_age_15_49_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Philippines: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/6d9f35c0-4764-49ee-b364-329db0b7a47d/resource/afea01e2-2f33-44c9-b424-a4ab11f90b29/download/phl_youth_15_24_2020_csv.zip
  format: zip
  id: resource_afea01e2
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: phl_youth_15_24_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Philippines: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/6d9f35c0-4764-49ee-b364-329db0b7a47d/resource/b315daae-f323-435e-a22d-62bcaecddc89/download/phl_youth_15_24_2020_geotiff.zip
  format: zip
  id: resource_b315daae
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: phl_youth_15_24_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Philippines: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/6d9f35c0-4764-49ee-b364-329db0b7a47d/resource/4a178155-b746-4f04-8f1b-2a79cc6f5153/download/phl_general_2020_geotiff.zip
  format: zip
  id: resource_4a178155
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: phl_general_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Philippines: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/6d9f35c0-4764-49ee-b364-329db0b7a47d/resource/0b35adea-5104-4598-868f-d4266d05c55a/download/phl_general_2020_csv.zip
  format: zip
  id: resource_0b35adea
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: phl_general_2020_csv.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-phl_metad4g_highresolutionpopulationd_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - PHL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2022-12-16'
  start: '2019-06-19'
temporal_resolution: null
title: 'Philippines: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
