---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook/Meta AI and Data for Good
    url: https://data.humdata.org/dataset/bulgaria-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/bulgaria-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/bulgaria-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/bulgaria-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-bgr_metad4g_bulgariahighresolutionpop_2019
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Bulgaria: (1) Overall population
  density (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly
  (ages 60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/bulgaria-high-resolution-population-density-maps-demographic-estimates]'
details: "To reference this data, please use the following citation: Facebook Connectivity\
  \ Lab and Center for International Earth Science Information Network - CIESIN -\
  \ Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery\
  \ for HRSL \xC2\xA9 2016 DigitalGlobe. Accessed DAY MONTH YEAR.' Please note that\
  \ as of 2024, Meta's high resolution population density maps are no longer being\
  \ updated."
exposure:
- asset_type:
    description: High-resolution gridded population density estimates for Bulgaria
      disaggregated by age and sex groups (overall, children 0-5, youth 15-24, elderly
      60+, women, men, women of reproductive age 15-49)
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
    imagery, then overlaying general population estimates derived from publicly available
    census data and demographic statistics. The resulting gridded datasets provide
    spatially explicit population distributions disaggregated by age and sex groups
    at national scale for Bulgaria in 2020.
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
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/bulgaria-high-resolution-population-density-maps-demographic-estimates
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
  description: 'Bulgaria: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/bec879d6-31e4-43af-8316-6fe32a2bf860/resource/4472d3e4-65eb-40c5-8a7e-2c889f720592/download/bgr_general_2020_geotiff.zip
  format: null
  id: resource_4472d3e4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bgr_general_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bulgaria: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/bec879d6-31e4-43af-8316-6fe32a2bf860/resource/b60c725a-6953-4f73-b440-ee0cafa6ee20/download/bgr_general_2020_csv.zip
  format: null
  id: resource_b60c725a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bgr_general_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bulgaria: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/bec879d6-31e4-43af-8316-6fe32a2bf860/resource/61b7db5a-280f-4adf-bee2-e579ebfa7528/download/bgr_children_under_five_2020_geotiff.zip
  format: null
  id: resource_61b7db5a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bgr_children_under_five_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bulgaria: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/bec879d6-31e4-43af-8316-6fe32a2bf860/resource/639049e2-5fee-4d9b-984f-5c4ca15d943d/download/bgr_elderly_60_plus_2020_geotiff.zip
  format: null
  id: resource_639049e2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bgr_elderly_60_plus_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bulgaria: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/bec879d6-31e4-43af-8316-6fe32a2bf860/resource/9f2d27c5-2a9c-46d8-bd3a-66ba4c790435/download/bgr_men_2020_geotiff.zip
  format: null
  id: resource_9f2d27c5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bgr_men_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bulgaria: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/bec879d6-31e4-43af-8316-6fe32a2bf860/resource/ec5820d9-ec16-443a-afca-16bc8a3ac4b7/download/bgr_women_2020_geotiff.zip
  format: null
  id: resource_ec5820d9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bgr_women_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bulgaria: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/bec879d6-31e4-43af-8316-6fe32a2bf860/resource/05420ea7-61c9-4109-9f05-90d1a23dda1b/download/bgr_women_of_reproductive_age_15_49_2020_geotiff.zip
  format: null
  id: resource_05420ea7
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bgr_women_of_reproductive_age_15_49_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bulgaria: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/bec879d6-31e4-43af-8316-6fe32a2bf860/resource/c79752ec-9bfc-4c6f-ab98-e2ca67d198de/download/bgr_youth_15_24_2020_geotiff.zip
  format: null
  id: resource_c79752ec
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bgr_youth_15_24_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bulgaria: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/bec879d6-31e4-43af-8316-6fe32a2bf860/resource/08280d9c-bd57-4887-bf5e-a5a2998fedef/download/bgr_children_under_five_2020_csv.zip
  format: null
  id: resource_08280d9c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bgr_children_under_five_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bulgaria: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/bec879d6-31e4-43af-8316-6fe32a2bf860/resource/79588d2f-7a15-46db-bc2d-b9bfb4e583e9/download/bgr_elderly_60_plus_2020_csv.zip
  format: null
  id: resource_79588d2f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bgr_elderly_60_plus_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bulgaria: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/bec879d6-31e4-43af-8316-6fe32a2bf860/resource/55c6fed5-a513-4827-80ea-e2fd58515387/download/bgr_men_2020_csv.zip
  format: null
  id: resource_55c6fed5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bgr_men_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bulgaria: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/bec879d6-31e4-43af-8316-6fe32a2bf860/resource/b811ff06-20a7-43b0-a51b-65292d04362c/download/bgr_women_2020_csv.zip
  format: null
  id: resource_b811ff06
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bgr_women_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bulgaria: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/bec879d6-31e4-43af-8316-6fe32a2bf860/resource/b9090e93-a924-4165-8cad-7e29e8c747bd/download/bgr_women_of_reproductive_age_15_49_2020_csv.zip
  format: null
  id: resource_b9090e93
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bgr_women_of_reproductive_age_15_49_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bulgaria: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/bec879d6-31e4-43af-8316-6fe32a2bf860/resource/c22af82f-6e42-431c-bf68-2c03680ca613/download/bgr_youth_15_24_2020_csv.zip
  format: null
  id: resource_c22af82f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bgr_youth_15_24_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This file has information about the cloud cover percentage and capture
    data of the satellite images used.
  download_url: https://data.humdata.org/dataset/bec879d6-31e4-43af-8316-6fe32a2bf860/resource/34c3bf90-fe7e-4e6b-8d8b-349ffbf535a5/download/bgr_dg_metadata.zip
  format: null
  id: resource_34c3bf90
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bgr_dg_metadata.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-bgr_metad4g_bulgariahighresolutionpop_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - BGR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2021-05-05'
  start: '2019-09-19'
temporal_resolution: null
title: 'Bulgaria: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
