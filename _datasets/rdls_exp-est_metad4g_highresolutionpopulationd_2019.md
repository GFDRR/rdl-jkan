---
attributions:
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/estonia-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/estonia-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/estonia-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-est_metad4g_highresolutionpopulationd_2019
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Estonia: (1) Overall population density
  (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly (ages
  60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/estonia-high-resolution-population-density-maps-demographic-estimates]'
details: "To reference this data, please use the following citation: Facebook Connectivity\
  \ Lab and Center for International Earth Science Information Network - CIESIN -\
  \ Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery\
  \ for HRSL \xC2\xA9 2016 DigitalGlobe. Accessed DAY MONTH YEAR.' Please note that\
  \ as of 2024, Meta's high resolution population density maps are no longer being\
  \ updated."
exposure:
- asset_type:
    description: High-resolution gridded population density estimates disaggregated
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: High-resolution population density maps were created by applying machine
    learning algorithms to identify building footprints from commercial satellite
    imagery, then overlaying population estimates derived from census data and demographic
    statistics in partnership with Columbia University. The resulting gridded datasets
    provide spatial distribution of total population and seven demographic subgroups
    at fine resolution across Estonia for 2020.
  sources:
  - id: source_1
    license: null
    name: AI and Data for Good at Meta
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
- href: https://data.humdata.org/dataset/estonia-high-resolution-population-density-maps-demographic-estimates
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
  description: 'Estonia: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/e53a33d3-c0c3-47b8-b99a-0605ba08deb7/resource/6b980ac1-a3fa-4c05-ae89-62a740bc97b5/download/est_general_2020_geotiff.zip
  format: null
  id: resource_6b980ac1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: est_general_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Estonia: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/e53a33d3-c0c3-47b8-b99a-0605ba08deb7/resource/0c5e0819-ce6e-4419-8fdb-067537c0789c/download/est_general_2020_csv.zip
  format: null
  id: resource_0c5e0819
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: est_general_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Estonia: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/e53a33d3-c0c3-47b8-b99a-0605ba08deb7/resource/10ead078-ca2f-4f14-8d31-1c5c271695e6/download/est_children_under_five_2020_csv.zip
  format: null
  id: resource_10ead078
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: est_children_under_five_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Estonia: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/e53a33d3-c0c3-47b8-b99a-0605ba08deb7/resource/5cdff6e3-baf0-4407-89cf-f559019cb762/download/est_children_under_five_2020_geotiff.zip
  format: null
  id: resource_5cdff6e3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: est_children_under_five_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Estonia: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/e53a33d3-c0c3-47b8-b99a-0605ba08deb7/resource/b267f6cd-cd9a-4c05-a401-9e9540142215/download/est_elderly_60_plus_2020_geotiff.zip
  format: null
  id: resource_b267f6cd
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: est_elderly_60_plus_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Estonia: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/e53a33d3-c0c3-47b8-b99a-0605ba08deb7/resource/9b7645b5-4aec-4fed-862a-5b7cefc6bbbb/download/est_elderly_60_plus_2020_csv.zip
  format: null
  id: resource_9b7645b5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: est_elderly_60_plus_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Estonia: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/e53a33d3-c0c3-47b8-b99a-0605ba08deb7/resource/b7f14f4a-2ba3-49a0-8fd9-96c77e6cb194/download/est_men_2020_csv.zip
  format: null
  id: resource_b7f14f4a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: est_men_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Estonia: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/e53a33d3-c0c3-47b8-b99a-0605ba08deb7/resource/6943d544-097c-4cfa-ba41-17f04df77296/download/est_men_2020_geotiff.zip
  format: null
  id: resource_6943d544
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: est_men_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Estonia: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/e53a33d3-c0c3-47b8-b99a-0605ba08deb7/resource/460e74a6-52af-4987-aaa7-c125cdc68887/download/est_women_2020_csv.zip
  format: null
  id: resource_460e74a6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: est_women_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Estonia: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/e53a33d3-c0c3-47b8-b99a-0605ba08deb7/resource/8d040ca7-a094-499a-9605-3d3adf4446ae/download/est_women_2020_geotiff.zip
  format: null
  id: resource_8d040ca7
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: est_women_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Estonia: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/e53a33d3-c0c3-47b8-b99a-0605ba08deb7/resource/73204e79-8ad1-4964-87cc-d8ae6fb617c5/download/est_women_of_reproductive_age_15_49_2020_csv.zip
  format: null
  id: resource_73204e79
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: est_women_of_reproductive_age_15_49_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Estonia: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/e53a33d3-c0c3-47b8-b99a-0605ba08deb7/resource/78dcc0bc-8331-4066-8be3-5671bea4a811/download/est_women_of_reproductive_age_15_49_2020_geotiff.zip
  format: null
  id: resource_78dcc0bc
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: est_women_of_reproductive_age_15_49_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Estonia: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/e53a33d3-c0c3-47b8-b99a-0605ba08deb7/resource/6637801e-545e-44bd-8518-3f59b3a74ed7/download/est_youth_15_24_2020_geotiff.zip
  format: null
  id: resource_6637801e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: est_youth_15_24_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Estonia: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/e53a33d3-c0c3-47b8-b99a-0605ba08deb7/resource/0e744c0a-633e-4577-9fe1-f3f866ae2356/download/est_youth_15_24_2020_csv.zip
  format: null
  id: resource_0e744c0a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: est_youth_15_24_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This file has information about the cloud cover percentage and capture
    data of the satellite images used.
  download_url: https://data.humdata.org/dataset/e53a33d3-c0c3-47b8-b99a-0605ba08deb7/resource/d09585d3-c8e8-4857-8a46-657b6a8bc828/download/est_dg_metadata.json.zip
  format: null
  id: resource_d09585d3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: est_dg_metadata.json.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-est_metad4g_highresolutionpopulationd_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - EST
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2021-05-11'
  start: '2019-09-19'
temporal_resolution: null
title: 'Estonia: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
