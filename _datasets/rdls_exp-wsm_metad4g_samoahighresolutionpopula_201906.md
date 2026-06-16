---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook (satellite imagery and machine learning)
    url: https://data.humdata.org/dataset/samoa-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/samoa-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/samoa-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/samoa-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-wsm_metad4g_samoahighresolutionpopula_201906
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Samoa: (1) Overall population density
  (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly (ages
  60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/samoa-high-resolution-population-density-maps-demographic-estimates]'
details: "To reference this data, please use the following citation: Facebook Connectivity\
  \ Lab and Center for International Earth Science Information Network - CIESIN -\
  \ Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery\
  \ for HRSL \xC2\xA9 2016 DigitalGlobe. Accessed DAY MONTH YEAR.' Please note that\
  \ as of 2024, Meta's high resolution population density maps are no longer being\
  \ updated."
exposure:
- asset_type:
    description: High-resolution gridded population density estimates for overall
      population and demographic subgroups (children 0-5, youth 15-24, elderly 60+,
      women, men, women of reproductive age 15-49)
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
    satellite imagery across Samoa. Population estimates derived from publicly available
    census data and demographic statistics were spatially allocated to building locations
    using methodology developed with Columbia University partners, producing high-resolution
    gridded population density maps for overall population and seven demographic subgroups
    at the national scale.
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
- href: https://data.humdata.org/dataset/samoa-high-resolution-population-density-maps-demographic-estimates
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
  description: 'Samoa: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/693a4f64-eeca-4ae6-aa89-b7dd56748dc9/resource/965b98b6-427a-4966-8f17-70cc1d1c1d08/download/wsm_children_under_five_2019-06-01_csv.zip
  format: null
  id: resource_965b98b6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: WSM_children_under_five_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Samoa: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/693a4f64-eeca-4ae6-aa89-b7dd56748dc9/resource/af0ab5b3-6cd1-4a82-a9c9-e00b44c6a8ea/download/wsm_children_under_five_2019-06-01_geotiff.zip
  format: null
  id: resource_af0ab5b3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: WSM_children_under_five_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Samoa: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/693a4f64-eeca-4ae6-aa89-b7dd56748dc9/resource/a2ba2afd-85cb-4614-96e8-5775599a033b/download/wsm_elderly_60_plus_2019-06-01_csv.zip
  format: null
  id: resource_a2ba2afd
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: WSM_elderly_60_plus_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Samoa: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/693a4f64-eeca-4ae6-aa89-b7dd56748dc9/resource/a4f140f4-e00a-4c8e-822f-fc1fa6c26eac/download/wsm_elderly_60_plus_2019-06-01_geotiff.zip
  format: null
  id: resource_a4f140f4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: WSM_elderly_60_plus_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Samoa: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/693a4f64-eeca-4ae6-aa89-b7dd56748dc9/resource/e37958da-20cc-41d8-a919-098662779c55/download/wsm_men_2019-06-01_csv.zip
  format: null
  id: resource_e37958da
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: WSM_men_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Samoa: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/693a4f64-eeca-4ae6-aa89-b7dd56748dc9/resource/ed870453-e424-4eca-9609-7a18477b1033/download/wsm_men_2019-06-01_geotiff.zip
  format: null
  id: resource_ed870453
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: WSM_men_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Samoa: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/693a4f64-eeca-4ae6-aa89-b7dd56748dc9/resource/ce9199e4-3a0a-4184-8895-c6a0c98c4565/download/wsm_women_2019-06-01_csv.zip
  format: null
  id: resource_ce9199e4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: WSM_women_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Samoa: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/693a4f64-eeca-4ae6-aa89-b7dd56748dc9/resource/848bb702-8ad5-45c3-b1e3-3cb64fd9bf02/download/wsm_women_2019-06-01_geotiff.zip
  format: null
  id: resource_848bb702
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: WSM_women_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Samoa: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/693a4f64-eeca-4ae6-aa89-b7dd56748dc9/resource/a45277b2-ad8e-44a6-904f-ab9e89f1cb52/download/wsm_women_of_reproductive_age_15_49_2019-06-01_csv.zip
  format: null
  id: resource_a45277b2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: WSM_women_of_reproductive_age_15_49_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Samoa: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/693a4f64-eeca-4ae6-aa89-b7dd56748dc9/resource/8cc142c0-9d62-4727-a814-d5e6f00db30f/download/wsm_women_of_reproductive_age_15_49_2019-06-01_geotiff.zip
  format: null
  id: resource_8cc142c0
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: WSM_women_of_reproductive_age_15_49_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Samoa: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/693a4f64-eeca-4ae6-aa89-b7dd56748dc9/resource/3853eee2-f530-41a9-9f58-9cb9cf12e6b4/download/wsm_youth_15_24_2019-06-01_csv.zip
  format: null
  id: resource_3853eee2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: WSM_youth_15_24_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Samoa: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/693a4f64-eeca-4ae6-aa89-b7dd56748dc9/resource/5d04290b-43f9-4e3a-a258-edab4c5789d0/download/wsm_youth_15_24_2019-06-01_geotiff.zip
  format: null
  id: resource_5d04290b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: WSM_youth_15_24_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Samoa: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/693a4f64-eeca-4ae6-aa89-b7dd56748dc9/resource/7d107d22-fffc-4cd9-b678-fd1f52d63e02/download/population_wsm_2018-10-01_geotiff.zip
  format: null
  id: resource_7d107d22
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_wsm_2018-10-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Samoa: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/693a4f64-eeca-4ae6-aa89-b7dd56748dc9/resource/112da746-8937-4d7c-80a8-2b37a6e69ed1/download/population_wsm_2018-10-01.csv.zip
  format: null
  id: resource_112da746
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_wsm_2018-10-01.csv.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-wsm_metad4g_samoahighresolutionpopula_201906
spatial:
  bbox: null
  centroid: null
  countries:
  - WSM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2019-06-21'
  start: '2019-06-19'
temporal_resolution: null
title: 'Samoa: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
