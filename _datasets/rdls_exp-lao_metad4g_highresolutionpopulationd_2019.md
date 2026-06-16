---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook Data for Good
    url: https://data.humdata.org/dataset/laos-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/laos-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/laos-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/laos-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-lao_metad4g_highresolutionpopulationd_2019
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Laos: (1) Overall population density
  (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly (ages
  60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/laos-high-resolution-population-density-maps-demographic-estimates]'
details: "This data contains population data from multiple countries. We are moving\
  \ to using larger envelopes for countries so that users can define their own boundaries\
  \ and to simplify our production pipeline to only pull from a single cloud-optimized\
  \ geotiff. To reference this data, please use the following citation: 'Facebook\
  \ Connectivity Lab and Center for International Earth Science Information Network\
  \ - CIESIN - Columbia University. 2016. High Resolution Settlement Layer (HRSL).\
  \ Source imagery for HRSL \xC2\xA9 2016 DigitalGlobe. Accessed DAY MONTH YEAR.'\
  \ Please note that as of 2024, Meta's high resolution population density maps are\
  \ no longer being updated."
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: High-resolution population density maps were created by applying machine
    learning algorithms to identify building footprints from commercial satellite
    imagery, then overlaying population estimates derived from census data and demographic
    statistics in partnership with Columbia University. The resulting gridded datasets
    provide spatial distributions of total population and seven demographic subgroups
    at fine resolution across Laos.
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
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/laos-high-resolution-population-density-maps-demographic-estimates
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
  description: 'Laos: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/2d9c5596-151a-4c8d-af6d-4ab3492c6cc7/resource/2edfd243-107d-4594-b577-eeb95079356c/download/lao_children_under_five_2020_csv.zip
  format: zip
  id: resource_2edfd243
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lao_children_under_five_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Laos: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/2d9c5596-151a-4c8d-af6d-4ab3492c6cc7/resource/381c5f32-c542-4453-ba28-52fc49de8593/download/lao_children_under_five_2020_geotiff.zip
  format: zip
  id: resource_381c5f32
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lao_children_under_five_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Laos: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/2d9c5596-151a-4c8d-af6d-4ab3492c6cc7/resource/d25cba69-3808-4991-9f6a-9efe88db54a5/download/lao_elderly_60_plus_2020_csv.zip
  format: zip
  id: resource_d25cba69
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lao_elderly_60_plus_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Laos: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/2d9c5596-151a-4c8d-af6d-4ab3492c6cc7/resource/3a7f60b2-e997-445e-a446-1532f8eee4bd/download/lao_elderly_60_plus_2020_geotiff.zip
  format: zip
  id: resource_3a7f60b2
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lao_elderly_60_plus_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Laos: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/2d9c5596-151a-4c8d-af6d-4ab3492c6cc7/resource/2df00628-e629-4425-a3a6-0f6a5ce01262/download/lao_men_2020_csv.zip
  format: zip
  id: resource_2df00628
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lao_men_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Laos: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/2d9c5596-151a-4c8d-af6d-4ab3492c6cc7/resource/6090446c-bcbe-4e5d-8cae-adf50a077978/download/lao_men_2020_geotiff.zip
  format: zip
  id: resource_6090446c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lao_men_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Laos: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/2d9c5596-151a-4c8d-af6d-4ab3492c6cc7/resource/efbeccd3-42b3-42f7-af26-28055dca018e/download/lao_women_2020_csv.zip
  format: zip
  id: resource_efbeccd3
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lao_women_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Laos: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/2d9c5596-151a-4c8d-af6d-4ab3492c6cc7/resource/98cf70ea-87cb-4562-9674-e554cdf55b67/download/lao_women_2020_geotiff.zip
  format: zip
  id: resource_98cf70ea
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lao_women_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Laos: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/2d9c5596-151a-4c8d-af6d-4ab3492c6cc7/resource/498aa8ab-6740-4b82-8ad2-912afe409875/download/lao_women_of_reproductive_age_15_49_2020_csv.zip
  format: zip
  id: resource_498aa8ab
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lao_women_of_reproductive_age_15_49_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Laos: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/2d9c5596-151a-4c8d-af6d-4ab3492c6cc7/resource/3c81efec-9946-4e61-9f1b-a4959cc1fd69/download/lao_women_of_reproductive_age_15_49_2020_geotiff.zip
  format: zip
  id: resource_3c81efec
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lao_women_of_reproductive_age_15_49_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Laos: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/2d9c5596-151a-4c8d-af6d-4ab3492c6cc7/resource/02269cff-adfa-4e4a-b1c7-812a82a891c5/download/lao_youth_15_24_2020_csv.zip
  format: zip
  id: resource_02269cff
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lao_youth_15_24_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Laos: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/2d9c5596-151a-4c8d-af6d-4ab3492c6cc7/resource/101250e0-4841-40f3-a6aa-bf67813f960d/download/lao_youth_15_24_2020_geotiff.zip
  format: zip
  id: resource_101250e0
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lao_youth_15_24_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Laos: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/2d9c5596-151a-4c8d-af6d-4ab3492c6cc7/resource/82bc4e2a-f916-47fc-b725-adf02784b6fb/download/lao_general_2020_csv.zip
  format: zip
  id: resource_82bc4e2a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lao_general_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Laos: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/2d9c5596-151a-4c8d-af6d-4ab3492c6cc7/resource/70c7a422-1716-4f92-849f-c3a1cd3e8368/download/lao_general_2020_geotiff.zip
  format: zip
  id: resource_70c7a422
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lao_general_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This file has information about the cloud cover percentage and capture
    data of the satellite images used.
  download_url: https://data.humdata.org/dataset/2d9c5596-151a-4c8d-af6d-4ab3492c6cc7/resource/ca16ddaa-9f5c-474d-a522-0dd8ab4806ef/download/lao_dg_metadata.zip
  format: null
  id: resource_ca16ddaa
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lao_dg_metadata.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-lao_metad4g_highresolutionpopulationd_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - LAO
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-02-18'
  start: '2019-06-19'
temporal_resolution: null
title: 'Laos: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
