---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook (satellite imagery and machine learning)
    url: https://data.humdata.org/dataset/bangladesh-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/bangladesh-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/bangladesh-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/bangladesh-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-bgd_metad4g_highresolutionpopulationd_2019
description: 'VERSION 1.5. The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Bangladesh : (1) Overall population
  density (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly
  (ages 60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/bangladesh-high-resolution-population-density-maps-demographic-estimates]'
details: "Citation To reference this data, please use the following citation: Facebook\
  \ and Center for International Earth Science Information Network - CIESIN - Columbia\
  \ University. 2021. High Resolution Settlement Layer (HRSL). Source imagery for\
  \ HRSL \xC2\xA9 2021 Maxar. Accessed DAY MONTH YEAR. Acknowledgements CIESIN contributions\
  \ to the development of this work were supported by funding provided by Facebook.\
  \ Population estimates are based on data from the Gridded Population of the World\
  \ data collection. Imagery used to identify settlements is from the Maxar Basemap\
  \ +Vivid. Data for the surface model relies on digital surface model produced with\
  \ the data from the Panchromatic Remote-sensing Instrument for Stereo Mapping (PRISM)\
  \ on board the Advanced Land Observing Satellite (ALOS); additional house locations\
  \ come from OpenStreetMap Please note that as of 2024, Meta's high resolution population\
  \ density maps are no longer being updated."
exposure:
- asset_type:
    description: High-resolution gridded population density maps for overall population
      and demographic subgroups (children 0-5, youth 15-24, elderly 60+, women, men,
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
    satellite imagery across Bangladesh. Population estimates derived from publicly
    available census data and demographic statistics were spatially distributed to
    these building locations using Columbia University's methodology, producing high-resolution
    gridded population density maps disaggregated by demographic subgroups (age, sex,
    reproductive status).
  sources:
  - id: source_1
    license: null
    name: Facebook (satellite imagery and machine learning)
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
- href: https://data.humdata.org/dataset/bangladesh-high-resolution-population-density-maps-demographic-estimates
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
  description: 'Bangladesh: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/8c5e9740-68aa-446e-9e28-9803d5c0b39c/resource/f8cb147b-c288-402d-b98f-f0cfa7457009/download/bgd_children_under_five_2020_csv.zip
  format: zip
  id: resource_f8cb147b
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bgd_children_under_five_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bangladesh: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/8c5e9740-68aa-446e-9e28-9803d5c0b39c/resource/94880740-601a-4b4d-9c07-14455996e652/download/bgd_children_under_five_2020_geotiff.zip
  format: zip
  id: resource_94880740
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bgd_children_under_five_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bangladesh: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/8c5e9740-68aa-446e-9e28-9803d5c0b39c/resource/f9f2193e-ed65-4d4a-bb2e-9815893c4290/download/bgd_elderly_60_plus_2020_csv.zip
  format: zip
  id: resource_f9f2193e
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bgd_elderly_60_plus_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bangladesh: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/8c5e9740-68aa-446e-9e28-9803d5c0b39c/resource/9323109b-c593-4b5d-85ec-c0f07c195eea/download/bgd_elderly_60_plus_2020_geotiff.zip
  format: zip
  id: resource_9323109b
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bgd_elderly_60_plus_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bangladesh: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/8c5e9740-68aa-446e-9e28-9803d5c0b39c/resource/709a4200-3007-4872-92b2-e152f5feddd8/download/bgd_men_2020_csv.zip
  format: zip
  id: resource_709a4200
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bgd_men_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bangladesh: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/8c5e9740-68aa-446e-9e28-9803d5c0b39c/resource/97028aa6-fe50-4248-9dc1-3d0fc67f4ff1/download/bgd_men_2020_geotiff.zip
  format: zip
  id: resource_97028aa6
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bgd_men_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bangladesh: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/8c5e9740-68aa-446e-9e28-9803d5c0b39c/resource/8e8754b1-0302-4ddc-bf11-c80702e02760/download/bgd_women_2020_csv.zip
  format: zip
  id: resource_8e8754b1
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bgd_women_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bangladesh: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/8c5e9740-68aa-446e-9e28-9803d5c0b39c/resource/30215ebc-1419-4d5c-b7b0-8598efe09f96/download/bgd_women_2020_geotiff.zip
  format: zip
  id: resource_30215ebc
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bgd_women_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bangladesh: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/8c5e9740-68aa-446e-9e28-9803d5c0b39c/resource/b1e302bc-5ad9-4f8d-a31c-4cce446b33cd/download/bgd_women_of_reproductive_age_15_49_2020_csv.zip
  format: zip
  id: resource_b1e302bc
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bgd_women_of_reproductive_age_15_49_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bangladesh: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/8c5e9740-68aa-446e-9e28-9803d5c0b39c/resource/b9a9f696-26a4-4386-9ca0-9b2ab7a4ba03/download/bgd_women_of_reproductive_age_15_49_2020_geotiff.zip
  format: zip
  id: resource_b9a9f696
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bgd_women_of_reproductive_age_15_49_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bangladesh: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/8c5e9740-68aa-446e-9e28-9803d5c0b39c/resource/7a4d4600-4a4b-42ad-8be2-768de54d8c39/download/bgd_youth_15_24_2020_csv.zip
  format: zip
  id: resource_7a4d4600
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bgd_youth_15_24_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bangladesh: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/8c5e9740-68aa-446e-9e28-9803d5c0b39c/resource/7eb428d6-9b0a-4f48-a564-3d16853aaaf6/download/bgd_youth_15_24_2020_geotiff.zip
  format: zip
  id: resource_7eb428d6
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bgd_youth_15_24_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bangladesh: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/8c5e9740-68aa-446e-9e28-9803d5c0b39c/resource/a87a3d80-5563-4e1f-a1b2-5215d216ec1e/download/bgd_general_2020_geotiff.zip
  format: zip
  id: resource_a87a3d80
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bgd_general_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bangladesh: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/8c5e9740-68aa-446e-9e28-9803d5c0b39c/resource/ff1cf446-859e-46d8-b3fa-7e0771092156/download/bgd_general_2020_csv.zip
  format: zip
  id: resource_ff1cf446
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bgd_general_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This file has information about the cloud cover percentage and capture
    data of the satellite images used.
  download_url: https://data.humdata.org/dataset/8c5e9740-68aa-446e-9e28-9803d5c0b39c/resource/0bf929d3-7cb0-4e3d-b0d5-c81b8e0ce907/download/bgd_dg_metadata.json.zip
  format: null
  id: resource_0bf929d3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bgd_dg_metadata.json.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-bgd_metad4g_highresolutionpopulationd_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - BGD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2021-10-25'
  start: '2019-06-19'
temporal_resolution: null
title: 'Bangladesh: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
