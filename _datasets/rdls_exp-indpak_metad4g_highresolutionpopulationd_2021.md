---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook Data for Good
    url: https://data.humdata.org/dataset/pakistan-india_all-files-high-resolution-population-density-maps
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University CIESIN
    url: https://data.humdata.org/dataset/pakistan-india_all-files-high-resolution-population-density-maps
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/pakistan-india_all-files-high-resolution-population-density-maps
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/pakistan-india_all-files-high-resolution-population-density-maps
dataset_id: rdls_exp-indpak_metad4g_highresolutionpopulationd_2021
description: 'Facebook and Columbia University - CIESIN provide the High Resolution
  Settlement Layer as the world''s most accurate population datasets. More info can
  be found here: https://dataforgood.fb.com/tools/population-density-maps/ These maps
  are the distribution of human population spanning Pakistan and India. Each of the
  13 TIFF files is a 10 x 10 degree tile (the lower latitude coordinate and longitude
  coordinates are in the file name). A VRT file is also included.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/pakistan-india_all-files-high-resolution-population-density-maps]'
details: "To reference this data, please use the following citation: 'Facebook Connectivity\
  \ Lab and Center for International Earth Science Information Network - CIESIN -\
  \ Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery\
  \ for HRSL \xA9 2016 DigitalGlobe. Accessed DAY MONTH YEAR.' Please note that as\
  \ of 2024, Meta's high resolution population density maps are no longer being updated."
exposure:
- asset_type:
    description: High-resolution gridded population density maps for general population
      and demographic subgroups (women, men, children under 5, women of reproductive
      age 15-49, youth 15-24, elderly 60+)
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
  description: "High-resolution population density maps were created by applying machine\
    \ learning algorithms to commercially available satellite imagery to identify\
    \ building footprints, then overlaying population estimates derived from census\
    \ data and demographic statistics in partnership with Columbia University CIESIN.\
    \ The resulting gridded datasets represent spatial distribution of total and demographic-stratified\
    \ population across Pakistan and India at 10\xD710 degree tiles."
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
    name: Columbia University CIESIN
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/pakistan-india_all-files-high-resolution-population-density-maps
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
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Pakistan & India: High Resolution Population Density Maps (ZIP archive)'
  download_url: https://data.humdata.org/dataset/2c8cfe67-448f-4a27-94b3-aaa944598cba/resource/e3dbe673-4117-4243-93a8-3366c6e6396b/download/population_ind_pak_general.zip
  format: null
  id: resource_e3dbe673
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_ind_pak_general.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Pakistan & India: High Resolution Population Density Maps (ZIP archive)'
  download_url: https://data.humdata.org/dataset/2c8cfe67-448f-4a27-94b3-aaa944598cba/resource/ae9d489f-0808-4a1f-b3be-4d08ad2f1fa5/download/population_ind_pak_women.zip
  format: null
  id: resource_ae9d489f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_ind_pak_women.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Pakistan & India: High Resolution Population Density Maps (ZIP archive)'
  download_url: https://data.humdata.org/dataset/2c8cfe67-448f-4a27-94b3-aaa944598cba/resource/34198f61-8b4e-4622-a4d7-929e88b5a2d9/download/population_ind_pak_children_under_five.zip
  format: null
  id: resource_34198f61
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_ind_pak_children_under_five.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Pakistan & India: High Resolution Population Density Maps (ZIP archive)'
  download_url: https://data.humdata.org/dataset/2c8cfe67-448f-4a27-94b3-aaa944598cba/resource/d61aa052-1fd8-47a1-bc87-a1ca14a115ff/download/population_ind_pak_men.zip
  format: null
  id: resource_d61aa052
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_ind_pak_men.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Pakistan & India: High Resolution Population Density Maps (ZIP archive)'
  download_url: https://data.humdata.org/dataset/2c8cfe67-448f-4a27-94b3-aaa944598cba/resource/af46c07b-e8a7-4aba-9fd2-72ef189c19f7/download/population_ind_pak_women_of_reproductive_age_15_49.zip
  format: null
  id: resource_af46c07b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_ind_pak_women_of_reproductive_age_15_49.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Pakistan & India: High Resolution Population Density Maps (ZIP archive)'
  download_url: https://data.humdata.org/dataset/2c8cfe67-448f-4a27-94b3-aaa944598cba/resource/925bb929-d535-48f3-a94e-3a9cef0fed93/download/population_ind_pak_youth_15_24.zip
  format: null
  id: resource_925bb929
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_ind_pak_youth_15_24.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Pakistan & India: High Resolution Population Density Maps (ZIP archive)'
  download_url: https://data.humdata.org/dataset/2c8cfe67-448f-4a27-94b3-aaa944598cba/resource/14377c01-d4b8-4492-b478-6bc1da6faa46/download/population_ind_pak_elderly_60_plus.zip
  format: null
  id: resource_14377c01
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_ind_pak_elderly_60_plus.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-indpak_metad4g_highresolutionpopulationd_2021
spatial:
  bbox: null
  centroid: null
  countries:
  - PAK
  - IND
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2021-08-31'
  start: '2021-03-24'
temporal_resolution: null
title: 'Pakistan & India: High Resolution Population Density Maps'
version: null
vulnerability: null
---
