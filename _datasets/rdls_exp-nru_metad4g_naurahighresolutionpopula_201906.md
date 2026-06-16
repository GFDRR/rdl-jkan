---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook/Meta AI and Data for Good
    url: https://data.humdata.org/dataset/naura-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/naura-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/naura-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/naura-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-nru_metad4g_naurahighresolutionpopula_201906
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Nauru: (1) Overall population density
  (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly (ages
  60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/naura-high-resolution-population-density-maps-demographic-estimates]'
details: "To reference this data, please use the following citation: Facebook Connectivity\
  \ Lab and Center for International Earth Science Information Network - CIESIN -\
  \ Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery\
  \ for HRSL \xC2\xA9 2016 DigitalGlobe. Accessed DAY MONTH YEAR.' Please note that\
  \ as of 2024, Meta's high resolution population density maps are no longer being\
  \ updated."
exposure:
- asset_type:
    description: High-resolution gridded population density estimates disaggregated
      by age groups (children 0-5, youth 15-24, elderly 60+) and sex (men, women,
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
    provide spatially explicit population distributions disaggregated by age and sex
    for Nauru at sub-settlement resolution.
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
- href: https://data.humdata.org/dataset/naura-high-resolution-population-density-maps-demographic-estimates
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
  description: 'Nauru - Naura: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/ecb31702-827b-4a93-bd6e-149753df2349/resource/9db40245-1861-4b04-82ca-5e0c40c7fce0/download/nru_children_under_five_2019-06-01_csv.zip
  format: null
  id: resource_9db40245
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NRU_children_under_five_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nauru - Naura: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/ecb31702-827b-4a93-bd6e-149753df2349/resource/018b56fa-e677-447e-9d84-28193854b68b/download/nru_children_under_five_2019-06-01_geotiff.zip
  format: null
  id: resource_018b56fa
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NRU_children_under_five_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nauru - Naura: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/ecb31702-827b-4a93-bd6e-149753df2349/resource/1feffc6c-3ccf-4d01-a47b-1f524c2c29e9/download/nru_elderly_60_plus_2019-06-01_csv.zip
  format: null
  id: resource_1feffc6c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NRU_elderly_60_plus_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nauru - Naura: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/ecb31702-827b-4a93-bd6e-149753df2349/resource/820ff184-3b9d-412f-b541-26777b0713d3/download/nru_elderly_60_plus_2019-06-01_geotiff.zip
  format: null
  id: resource_820ff184
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NRU_elderly_60_plus_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nauru - Naura: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/ecb31702-827b-4a93-bd6e-149753df2349/resource/b6df81e9-5b86-46cb-a5f8-b8e66fa47fb2/download/nru_men_2019-06-01_csv.zip
  format: null
  id: resource_b6df81e9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NRU_men_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nauru - Naura: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/ecb31702-827b-4a93-bd6e-149753df2349/resource/7b14edbb-6bd0-4112-a404-53ad866c7a6d/download/nru_men_2019-06-01_geotiff.zip
  format: null
  id: resource_7b14edbb
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NRU_men_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nauru - Naura: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/ecb31702-827b-4a93-bd6e-149753df2349/resource/7a2d1a6f-d59d-43b0-8c81-c0b2538aa649/download/nru_women_2019-06-01_csv.zip
  format: null
  id: resource_7a2d1a6f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NRU_women_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nauru - Naura: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/ecb31702-827b-4a93-bd6e-149753df2349/resource/58bcdba1-2342-4149-ab6e-08879b6edc84/download/nru_women_2019-06-01_geotiff.zip
  format: null
  id: resource_58bcdba1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NRU_women_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nauru - Naura: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/ecb31702-827b-4a93-bd6e-149753df2349/resource/cc1b1e02-2f19-4e60-b012-3443df8888fa/download/nru_women_of_reproductive_age_15_49_2019-06-01_csv.zip
  format: null
  id: resource_cc1b1e02
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NRU_women_of_reproductive_age_15_49_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nauru - Naura: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/ecb31702-827b-4a93-bd6e-149753df2349/resource/421291f0-6aeb-47fc-9998-a8e2c3b3857b/download/nru_women_of_reproductive_age_15_49_2019-06-01_geotiff.zip
  format: null
  id: resource_421291f0
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NRU_women_of_reproductive_age_15_49_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nauru - Naura: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/ecb31702-827b-4a93-bd6e-149753df2349/resource/88b63cb5-815e-4a1d-9303-578e0dfb7ed0/download/nru_youth_15_24_2019-06-01_csv.zip
  format: null
  id: resource_88b63cb5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NRU_youth_15_24_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nauru - Naura: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/ecb31702-827b-4a93-bd6e-149753df2349/resource/762dfb69-d488-4e97-ba97-3792c83e4937/download/nru_youth_15_24_2019-06-01_geotiff.zip
  format: null
  id: resource_762dfb69
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NRU_youth_15_24_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nauru - Naura: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/ecb31702-827b-4a93-bd6e-149753df2349/resource/03cd9363-13eb-422c-bf72-4bc3504b6288/download/population_nru_2018-10-01_geotiff.zip
  format: null
  id: resource_03cd9363
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_nru_2018-10-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nauru - Naura: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/ecb31702-827b-4a93-bd6e-149753df2349/resource/655e9198-0719-438e-9ef1-d1cf1fef4bb1/download/population_nru_2018-10-01.csv.zip
  format: null
  id: resource_655e9198
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_nru_2018-10-01.csv.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-nru_metad4g_naurahighresolutionpopula_201906
spatial:
  bbox: null
  centroid: null
  countries:
  - NRU
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2019-06-21'
  start: '2019-06-19'
temporal_resolution: null
title: 'Nauru - Naura: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
