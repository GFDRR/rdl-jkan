---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook Data for Good
    url: https://data.humdata.org/dataset/malta-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/malta-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/malta-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/malta-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-mlt_metad4g_maltahighresolutionpopula_2019
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Malta: (1) Overall population density
  (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly (ages
  60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/malta-high-resolution-population-density-maps-demographic-estimates]'
details: "To reference this data, please use the following citation: Facebook Connectivity\
  \ Lab and Center for International Earth Science Information Network - CIESIN -\
  \ Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery\
  \ for HRSL \xC2\xA9 2016 DigitalGlobe. Accessed DAY MONTH YEAR.' Please note that\
  \ as of 2024, Meta's high resolution population density maps are no longer being\
  \ updated."
exposure:
- asset_type:
    description: High-resolution gridded population density maps for overall population
      and demographic subgroups (children, youth, elderly, women, reproductive-age
      women)
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
    statistics in partnership with Columbia University. The resulting gridded datasets
    provide spatially explicit population distributions for Malta disaggregated by
    demographic groups.
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
- href: https://data.humdata.org/dataset/malta-high-resolution-population-density-maps-demographic-estimates
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
  description: 'Malta: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/d14c4c1e-b105-46a9-93c6-e7fa56e92ee6/resource/896a452e-7c12-48b2-93f0-e8b93bf8f66d/download/population_mlt_2019-07-01.csv.zip
  format: null
  id: resource_896a452e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_mlt.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Malta: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/d14c4c1e-b105-46a9-93c6-e7fa56e92ee6/resource/7c9f62cc-6891-4c53-b030-99b607576f2f/download/population_mlt_2019-07-01_geotiff.zip
  format: null
  id: resource_7c9f62cc
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_mlt.geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Malta: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/d14c4c1e-b105-46a9-93c6-e7fa56e92ee6/resource/58e5550f-c278-4b8f-ae71-1f1f39fc0cc6/download/mlt_children_under_five_geotiff.zip
  format: null
  id: resource_58e5550f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MLT_children_under_five_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Malta: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/d14c4c1e-b105-46a9-93c6-e7fa56e92ee6/resource/b2dbabf1-08c0-4f8b-8486-ab7cb9286527/download/mlt_elderly_60_plus_geotiff.zip
  format: null
  id: resource_b2dbabf1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MLT_elderly_60_plus_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Malta: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/d14c4c1e-b105-46a9-93c6-e7fa56e92ee6/resource/1875d22f-4ff6-4e17-95a2-54c7ce832730/download/mlt_men_geotiff.zip
  format: null
  id: resource_1875d22f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MLT_men_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Malta: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/d14c4c1e-b105-46a9-93c6-e7fa56e92ee6/resource/0dca8943-6d23-409f-95ee-1e3a84963bb1/download/mlt_women_geotiff.zip
  format: null
  id: resource_0dca8943
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MLT_women_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Malta: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/d14c4c1e-b105-46a9-93c6-e7fa56e92ee6/resource/811bc951-9c9d-4b1a-8686-eb1739cac2e5/download/mlt_women_of_reproductive_age_15_49_geotiff.zip
  format: null
  id: resource_811bc951
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MLT_women_of_reproductive_age_15_49_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Malta: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/d14c4c1e-b105-46a9-93c6-e7fa56e92ee6/resource/b5d8e34d-782b-4313-b278-e244fb0e78d1/download/mlt_youth_15_24_geotiff.zip
  format: null
  id: resource_b5d8e34d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MLT_youth_15_24_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Malta: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/d14c4c1e-b105-46a9-93c6-e7fa56e92ee6/resource/a7210531-bf17-4fdb-8e29-1e89b44bebb9/download/mlt_children_under_five_2019-08-03_csv.zip
  format: null
  id: resource_a7210531
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MLT_children_under_five.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Malta: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/d14c4c1e-b105-46a9-93c6-e7fa56e92ee6/resource/88cdced8-2f03-40cb-a489-a01218a03b26/download/mlt_elderly_60_plus_2019-08-03_csv.zip
  format: null
  id: resource_88cdced8
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MLT_elderly_60_plus.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Malta: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/d14c4c1e-b105-46a9-93c6-e7fa56e92ee6/resource/65f31e05-8ca6-475f-afa2-c781c38a0bc3/download/mlt_men_2019-08-03_csv.zip
  format: null
  id: resource_65f31e05
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MLT_men.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Malta: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/d14c4c1e-b105-46a9-93c6-e7fa56e92ee6/resource/c27ba2db-99d6-450b-be5e-9835cf2aef2b/download/mlt_women_2019-08-03_csv.zip
  format: null
  id: resource_c27ba2db
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MLT_women.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Malta: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/d14c4c1e-b105-46a9-93c6-e7fa56e92ee6/resource/13d35de5-43af-4cfc-9179-20e814d55aed/download/mlt_women_of_reproductive_age_15_49_2019-08-03_csv.zip
  format: null
  id: resource_13d35de5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MLT_women_of_reproductive_age_15_49.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Malta: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/d14c4c1e-b105-46a9-93c6-e7fa56e92ee6/resource/f63a713f-3a9b-43c7-b7f4-13dae4990b5f/download/mlt_youth_15_24_2019-08-03_csv.zip
  format: null
  id: resource_f63a713f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MLT_youth_15_24.csv.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-mlt_metad4g_maltahighresolutionpopula_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - MLT
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-03-04'
  start: '2019-09-19'
temporal_resolution: null
title: 'Malta: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
