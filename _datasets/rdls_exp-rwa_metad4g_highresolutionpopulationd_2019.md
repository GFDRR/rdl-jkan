---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook Data for Good
    url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-rwa
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-rwa
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-rwa
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-rwa
dataset_id: rdls_exp-rwa_metad4g_highresolutionpopulationd_2019
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Rwanda: (1) Overall population density
  (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly (ages
  60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-rwa]'
details: "To reference this data, please use the following citation: Facebook Connectivity\
  \ Lab and Center for International Earth Science Information Network - CIESIN -\
  \ Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery\
  \ for HRSL \xC2\xA9 2016 DigitalGlobe. Accessed DAY MONTH YEAR.' Please note that\
  \ as of 2024, Meta's high resolution population density maps are no longer being\
  \ updated."
exposure:
- asset_type:
    description: High-resolution gridded population density estimates for Rwanda disaggregated
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
license: CC-BY-4.0
lineage:
  description: Building footprints were automatically extracted from commercial satellite
    imagery using machine learning techniques. Population estimates derived from publicly
    available census data and demographic statistics were then spatially allocated
    to building locations using a dasymetric mapping approach developed in partnership
    with Columbia University, resulting in high-resolution gridded population density
    maps disaggregated by demographic cohorts for Rwanda in 2020.
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
- href: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-rwa
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
  description: 'Rwanda: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/0ee1affc-6a90-4ad3-b7eb-166645668fc3/resource/be8af0ca-f3f6-4049-a2b6-13a5547527d9/download/rwa_general_2020_csv.zip
  format: zip
  id: resource_be8af0ca
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rwa_general_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Rwanda: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/0ee1affc-6a90-4ad3-b7eb-166645668fc3/resource/a9013c82-cee9-43aa-a741-75a7595ca4fb/download/rwa_general_2020_geotiff.zip
  format: zip
  id: resource_a9013c82
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rwa_general_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Rwanda: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/0ee1affc-6a90-4ad3-b7eb-166645668fc3/resource/d9fe7d2b-ff7c-44eb-8352-4c4a7b029588/download/rwa_children_under_five_2020_csv.zip
  format: zip
  id: resource_d9fe7d2b
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rwa_children_under_five_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Rwanda: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/0ee1affc-6a90-4ad3-b7eb-166645668fc3/resource/c52c86b9-7bf1-4138-9f7f-c7b6dba3aa38/download/rwa_children_under_five_2020_geotiff.zip
  format: zip
  id: resource_c52c86b9
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rwa_children_under_five_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Rwanda: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/0ee1affc-6a90-4ad3-b7eb-166645668fc3/resource/343d8fc0-821e-482a-b393-33600881df2a/download/rwa_elderly_60_plus_2020_csv.zip
  format: zip
  id: resource_343d8fc0
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rwa_elderly_60_plus_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Rwanda: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/0ee1affc-6a90-4ad3-b7eb-166645668fc3/resource/5d6fca76-25ef-48fd-92ab-86c94692fded/download/rwa_elderly_60_plus_2020_geotiff.zip
  format: zip
  id: resource_5d6fca76
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rwa_elderly_60_plus_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Rwanda: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/0ee1affc-6a90-4ad3-b7eb-166645668fc3/resource/893854a2-afde-459c-b4a3-e3b7db5225d4/download/rwa_men_2020_csv.zip
  format: zip
  id: resource_893854a2
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rwa_men_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Rwanda: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/0ee1affc-6a90-4ad3-b7eb-166645668fc3/resource/191b90a0-1354-4d19-8b68-9f648e28548a/download/rwa_men_2020_geotiff.zip
  format: zip
  id: resource_191b90a0
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rwa_men_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Rwanda: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/0ee1affc-6a90-4ad3-b7eb-166645668fc3/resource/523b0a92-21a0-4971-ae94-2eb69f48e1b7/download/rwa_women_2020_csv.zip
  format: zip
  id: resource_523b0a92
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rwa_women_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Rwanda: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/0ee1affc-6a90-4ad3-b7eb-166645668fc3/resource/581f9f57-5cf3-43a9-9ce0-aba4a9a1e8c5/download/rwa_women_2020_geotiff.zip
  format: zip
  id: resource_581f9f57
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rwa_women_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Rwanda: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/0ee1affc-6a90-4ad3-b7eb-166645668fc3/resource/689258c1-549e-4e2f-9fc5-eb3709ef7606/download/rwa_women_of_reproductive_age_15_49_2020_csv.zip
  format: zip
  id: resource_689258c1
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rwa_women_of_reproductive_age_15_49_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Rwanda: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/0ee1affc-6a90-4ad3-b7eb-166645668fc3/resource/36c64ab0-013b-4995-88f5-1fbc5b43fc76/download/rwa_women_of_reproductive_age_15_49_2020_geotiff.zip
  format: zip
  id: resource_36c64ab0
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rwa_women_of_reproductive_age_15_49_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Rwanda: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/0ee1affc-6a90-4ad3-b7eb-166645668fc3/resource/d74e47db-def5-4c32-bc33-091b136d19b0/download/rwa_youth_15_24_2020_csv.zip
  format: zip
  id: resource_d74e47db
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rwa_youth_15_24_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Rwanda: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/0ee1affc-6a90-4ad3-b7eb-166645668fc3/resource/5b6e4343-97b3-48a1-94a4-564518e2256f/download/rwa_youth_15_24_2020_geotiff.zip
  format: zip
  id: resource_5b6e4343
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rwa_youth_15_24_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This file has information about the cloud cover percentage and capture
    data of the satellite images used.
  download_url: https://data.humdata.org/dataset/0ee1affc-6a90-4ad3-b7eb-166645668fc3/resource/c2af6294-f6a0-473c-bbb5-acd06187f112/download/rwa_dg_metadata.zip
  format: null
  id: resource_c2af6294
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rwa_dg_metadata.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-rwa_metad4g_highresolutionpopulationd_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - RWA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2022-07-22'
  start: '2019-05-20'
temporal_resolution: null
title: 'Rwanda: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
