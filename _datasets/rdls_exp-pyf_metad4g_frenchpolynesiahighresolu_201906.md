---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook/Meta AI and Data for Good
    url: https://data.humdata.org/dataset/french-polynesia-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/french-polynesia-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/french-polynesia-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/french-polynesia-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-pyf_metad4g_frenchpolynesiahighresolu_201906
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in French Polynesia: (1) Overall population
  density (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly
  (ages 60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/french-polynesia-high-resolution-population-density-maps-demographic-estimates]'
details: "To reference this data, please use the following citation: Facebook Connectivity\
  \ Lab and Center for International Earth Science Information Network - CIESIN -\
  \ Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery\
  \ for HRSL \xC2\xA9 2016 DigitalGlobe. Accessed DAY MONTH YEAR.' Please note that\
  \ as of 2024, Meta's high resolution population density maps are no longer being\
  \ updated."
exposure:
- asset_type:
    description: High-resolution gridded population density estimates disaggregated
      by age and sex (overall, women, men, children 0-5, youth 15-24, elderly 60+,
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
  description: High-resolution population density maps were created by applying machine
    learning algorithms to identify building footprints from commercial satellite
    imagery, then overlaying population estimates derived from census data and demographic
    statistics in partnership with Columbia University. The resulting gridded datasets
    provide disaggregated population counts by age group and sex across French Polynesia
    at fine spatial resolution.
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
- href: https://data.humdata.org/dataset/french-polynesia-high-resolution-population-density-maps-demographic-estimates
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
  description: 'French Polynesia: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/eef51122-205e-4141-8e00-ed30137b2254/resource/fb467766-44c7-48bb-8265-cfce25d76d74/download/pyf_children_under_five_2019-06-01_csv.zip
  format: null
  id: resource_fb467766
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PYF_children_under_five_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'French Polynesia: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/eef51122-205e-4141-8e00-ed30137b2254/resource/96659c01-e6a6-41cc-b5cc-0b7a376d98d3/download/pyf_children_under_five_2019-06-01_geotiff.zip
  format: null
  id: resource_96659c01
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PYF_children_under_five_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'French Polynesia: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/eef51122-205e-4141-8e00-ed30137b2254/resource/5825523e-a76a-4d61-a8ff-d68d30149d2a/download/pyf_elderly_60_plus_2019-06-01_csv.zip
  format: null
  id: resource_5825523e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PYF_elderly_60_plus_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'French Polynesia: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/eef51122-205e-4141-8e00-ed30137b2254/resource/dcabe618-e799-40ab-a122-e4f93094994b/download/pyf_elderly_60_plus_2019-06-01_geotiff.zip
  format: null
  id: resource_dcabe618
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PYF_elderly_60_plus_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'French Polynesia: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/eef51122-205e-4141-8e00-ed30137b2254/resource/d430fb22-3bf6-4f09-ad74-ffa3847a5ebc/download/pyf_men_2019-06-01_csv.zip
  format: null
  id: resource_d430fb22
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PYF_men_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'French Polynesia: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/eef51122-205e-4141-8e00-ed30137b2254/resource/8cc7521e-708f-4f32-b464-a59d1e4c5e67/download/pyf_men_2019-06-01_geotiff.zip
  format: null
  id: resource_8cc7521e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PYF_men_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'French Polynesia: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/eef51122-205e-4141-8e00-ed30137b2254/resource/8e63ea2b-c74e-44cd-8715-cf3c7b84fe60/download/pyf_women_2019-06-01_csv.zip
  format: null
  id: resource_8e63ea2b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PYF_women_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'French Polynesia: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/eef51122-205e-4141-8e00-ed30137b2254/resource/ee69fe7c-0a9b-4e4f-b9b6-eba9f71c91a9/download/pyf_women_2019-06-01_geotiff.zip
  format: null
  id: resource_ee69fe7c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PYF_women_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'French Polynesia: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/eef51122-205e-4141-8e00-ed30137b2254/resource/9fac09fe-6f7d-4a84-b13d-5722c72091d7/download/pyf_women_of_reproductive_age_15_49_2019-06-01_csv.zip
  format: null
  id: resource_9fac09fe
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PYF_women_of_reproductive_age_15_49_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'French Polynesia: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/eef51122-205e-4141-8e00-ed30137b2254/resource/3674fcc1-05b3-473a-89d1-66eabd9b8c4a/download/pyf_women_of_reproductive_age_15_49_2019-06-01_geotiff.zip
  format: null
  id: resource_3674fcc1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PYF_women_of_reproductive_age_15_49_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'French Polynesia: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/eef51122-205e-4141-8e00-ed30137b2254/resource/d5ff66de-7932-486e-a848-7c1d2e460701/download/pyf_youth_15_24_2019-06-01_csv.zip
  format: null
  id: resource_d5ff66de
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PYF_youth_15_24_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'French Polynesia: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/eef51122-205e-4141-8e00-ed30137b2254/resource/bae486a7-fa04-4049-b0c0-edfcc85f7c48/download/pyf_youth_15_24_2019-06-01_geotiff.zip
  format: null
  id: resource_bae486a7
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PYF_youth_15_24_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'French Polynesia: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/eef51122-205e-4141-8e00-ed30137b2254/resource/fe54280c-aae9-41c2-a5c3-aeec74bd6a0a/download/population_pyf_2018-10-01_geotiff.zip
  format: null
  id: resource_fe54280c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_pyf_2018-10-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'French Polynesia: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/eef51122-205e-4141-8e00-ed30137b2254/resource/77daec43-42ca-49d2-93f7-4463eeefe387/download/population_pyf_2018-10-01.csv.zip
  format: null
  id: resource_77daec43
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_pyf_2018-10-01.csv.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-pyf_metad4g_frenchpolynesiahighresolu_201906
spatial:
  bbox: null
  centroid: null
  countries:
  - PYF
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2019-06-21'
  start: '2019-06-19'
temporal_resolution: null
title: 'French Polynesia: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
