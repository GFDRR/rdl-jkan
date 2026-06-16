---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook Data for Good
    url: https://data.humdata.org/dataset/bahrain-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/bahrain-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/bahrain-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/bahrain-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-bhr_metad4g_bahrainhighresolutionpopu_2019
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Bahrain: (1) Overall population density
  (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly (ages
  60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/bahrain-high-resolution-population-density-maps-demographic-estimates]'
details: "To reference this data, please use the following citation: Facebook Connectivity\
  \ Lab and Center for International Earth Science Information Network - CIESIN -\
  \ Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery\
  \ for HRSL \xC2\xA9 2016 DigitalGlobe. Accessed DAY MONTH YEAR.' Please note that\
  \ as of 2024, Meta's high resolution population density maps are no longer being\
  \ updated."
exposure:
- asset_type:
    description: High-resolution gridded population density maps for overall population
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: High-resolution population density maps were created by applying machine
    learning algorithms to identify building footprints from commercial satellite
    imagery, then overlaying population estimates derived from census data and demographic
    statistics in collaboration with Columbia University. The resulting gridded datasets
    provide spatial distribution of total population and demographic subgroups at
    fine resolution across Bahrain.
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
- href: https://data.humdata.org/dataset/bahrain-high-resolution-population-density-maps-demographic-estimates
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
  description: 'Bahrain: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/f4e79ce8-c2f3-43b1-90dc-780f71cbc1b9/resource/8be75c35-7dc6-4404-bdd9-a392a3487a21/download/bhr_general_2020_geotiff.zip
  format: zip
  id: resource_8be75c35
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bhr_general_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bahrain: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/f4e79ce8-c2f3-43b1-90dc-780f71cbc1b9/resource/b5a655fb-4c6d-417c-9cf5-e29d4e596934/download/bhr_general_2020_csv.zip
  format: zip
  id: resource_b5a655fb
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bhr_general_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bahrain: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/f4e79ce8-c2f3-43b1-90dc-780f71cbc1b9/resource/39e187bb-b494-4c17-a56c-fdd2be0b6afc/download/bhr_children_under_five_2020_geotiff.zip
  format: zip
  id: resource_39e187bb
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bhr_children_under_five_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bahrain: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/f4e79ce8-c2f3-43b1-90dc-780f71cbc1b9/resource/6d3d5488-c36d-470c-9b66-b3c4e63f6034/download/bhr_elderly_60_plus_2020_geotiff.zip
  format: zip
  id: resource_6d3d5488
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bhr_elderly_60_plus_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bahrain: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/f4e79ce8-c2f3-43b1-90dc-780f71cbc1b9/resource/a39d0930-0c06-49d5-b0e2-a37462297345/download/bhr_men_2020_geotiff.zip
  format: zip
  id: resource_a39d0930
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bhr_men_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bahrain: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/f4e79ce8-c2f3-43b1-90dc-780f71cbc1b9/resource/7475f518-9fb3-4e94-8678-ada6ab247224/download/bhr_women_2020_geotiff.zip
  format: zip
  id: resource_7475f518
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bhr_women_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bahrain: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/f4e79ce8-c2f3-43b1-90dc-780f71cbc1b9/resource/3a1399ba-abd6-426f-b103-1cfe1ca84500/download/bhr_women_of_reproductive_age_15_49_2020_geotiff.zip
  format: zip
  id: resource_3a1399ba
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bhr_women_of_reproductive_age_15_49_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bahrain: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/f4e79ce8-c2f3-43b1-90dc-780f71cbc1b9/resource/c0f6db76-6ba1-45c1-a4fc-81d4573a6a70/download/bhr_youth_15_24_2020_geotiff.zip
  format: zip
  id: resource_c0f6db76
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bhr_youth_15_24_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bahrain: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/f4e79ce8-c2f3-43b1-90dc-780f71cbc1b9/resource/36b0c0ab-b470-485e-95a7-3922c6660459/download/bhr_children_under_five_2020_csv.zip
  format: zip
  id: resource_36b0c0ab
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bhr_children_under_five_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bahrain: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/f4e79ce8-c2f3-43b1-90dc-780f71cbc1b9/resource/c300bcb6-d0d4-43a7-9eaa-b72badd2ba6e/download/bhr_elderly_60_plus_2020_csv.zip
  format: zip
  id: resource_c300bcb6
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bhr_elderly_60_plus_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bahrain: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/f4e79ce8-c2f3-43b1-90dc-780f71cbc1b9/resource/d8d0e58a-f01f-4d56-971e-7a5489d8db2f/download/bhr_men_2020_csv.zip
  format: zip
  id: resource_d8d0e58a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bhr_men_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bahrain: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/f4e79ce8-c2f3-43b1-90dc-780f71cbc1b9/resource/b3ab26ec-27ad-4fcc-8074-082834850ab7/download/bhr_women_2020_csv.zip
  format: zip
  id: resource_b3ab26ec
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bhr_women_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bahrain: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/f4e79ce8-c2f3-43b1-90dc-780f71cbc1b9/resource/1e457998-8b1f-465c-851e-cfd62196187a/download/bhr_women_of_reproductive_age_15_49_2020_csv.zip
  format: zip
  id: resource_1e457998
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bhr_women_of_reproductive_age_15_49_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bahrain: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/f4e79ce8-c2f3-43b1-90dc-780f71cbc1b9/resource/bc2a60cd-6612-4959-8617-9467c78452d7/download/bhr_youth_15_24_2020_csv.zip
  format: zip
  id: resource_bc2a60cd
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bhr_youth_15_24_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This file has information about the cloud cover percentage and capture
    data of the satellite images used.
  download_url: https://data.humdata.org/dataset/f4e79ce8-c2f3-43b1-90dc-780f71cbc1b9/resource/1b335a69-3868-4152-856a-1f20e8b4214c/download/bhr_dg_metadata.json
  format: null
  id: resource_1b335a69
  media_type: application/json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bhr_dg_metadata.json
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-bhr_metad4g_bahrainhighresolutionpopu_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - BHR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2022-12-09'
  start: '2019-09-19'
temporal_resolution: null
title: 'Bahrain: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
