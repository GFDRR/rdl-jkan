---
attributions:
- entity:
    affiliation: null
    email: null
    name: CIESIN Gridded Population of the World
    url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-swz
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Digital Globe satellite imagery
    url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-swz
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Census data and population statistics
    url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-swz
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-swz
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-swz
dataset_id: rdls_exp-swz_metad4g_kingdomhighresolutionpopu_2018
description: 'The population of the world, allocated to 1 arcsecond blocks. This refines
  CIESIN''s Gridded Population of the World project, using machine learning models
  on high-resolution worldwide Digital Globe satellite imagery. More information .
  There is also a tiled version of this dataset that may be easier to use if you are
  interested in many countries.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-swz]'
details: "To reference this data, please use the following citation: Facebook Connectivity\
  \ Lab and Center for International Earth Science Information Network - CIESIN -\
  \ Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery\
  \ for HRSL \xC2\xA9 2016 DigitalGlobe. Accessed DAY MONTH YEAR.' Please note that\
  \ as of 2024, Meta's high resolution population density maps are no longer being\
  \ updated."
exposure:
- asset_type:
    description: High-resolution gridded population density estimates for Eswatini
      disaggregated by age and gender demographics (general population, children under
      5, elderly 60+, men, women, women of reproductive age 15-49, youth 15-24)
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
  description: Machine learning models trained on high-resolution Digital Globe satellite
    imagery were used to identify building footprints across Eswatini. These building-level
    estimates were then combined with publicly available census data and population
    statistics through partnership with Columbia University to allocate population
    counts to 1 arcsecond grid cells. The resulting dataset provides gridded population
    density estimates disaggregated by demographic categories (age groups and gender)
    for baseline exposure assessment.
  sources:
  - id: source_1
    license: null
    name: CIESIN Gridded Population of the World
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: Digital Globe satellite imagery
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_3
    license: null
    name: Census data and population statistics
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-swz
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
  description: 'Kingdom of Eswatini: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/5c2e6e10-51a3-4bbb-8353-3d1d95420926/resource/9db48134-b76a-4411-8f0c-8f17a2b389e5/download/swz_general_2020_geotiff.zip
  format: zip
  id: resource_9db48134
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swz_general_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kingdom of Eswatini: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/5c2e6e10-51a3-4bbb-8353-3d1d95420926/resource/659498e0-978f-43bb-b96b-e2330f9c62d2/download/swz_general_2020_csv.zip
  format: zip
  id: resource_659498e0
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swz_general_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kingdom of Eswatini: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/5c2e6e10-51a3-4bbb-8353-3d1d95420926/resource/6cf79ddf-c37d-4370-b185-bf72ef77f95d/download/swz_children_under_five_2020_csv.zip
  format: zip
  id: resource_6cf79ddf
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swz_children_under_five_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kingdom of Eswatini: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/5c2e6e10-51a3-4bbb-8353-3d1d95420926/resource/c9d77ea5-6d56-4265-90ca-ec9a3a7e8495/download/swz_children_under_five_2020_geotiff.zip
  format: zip
  id: resource_c9d77ea5
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swz_children_under_five_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kingdom of Eswatini: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/5c2e6e10-51a3-4bbb-8353-3d1d95420926/resource/1fa08ce3-9534-4542-95df-993bebd5507f/download/swz_elderly_60_plus_2020_csv.zip
  format: zip
  id: resource_1fa08ce3
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swz_elderly_60_plus_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kingdom of Eswatini: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/5c2e6e10-51a3-4bbb-8353-3d1d95420926/resource/c1fca34a-172c-41e6-92fb-44baab74b46c/download/swz_elderly_60_plus_2020_geotiff.zip
  format: zip
  id: resource_c1fca34a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swz_elderly_60_plus_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kingdom of Eswatini: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/5c2e6e10-51a3-4bbb-8353-3d1d95420926/resource/67fc8aaf-56f7-4216-a138-80aa2ce6f7f4/download/swz_men_2020_csv.zip
  format: zip
  id: resource_67fc8aaf
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swz_men_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kingdom of Eswatini: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/5c2e6e10-51a3-4bbb-8353-3d1d95420926/resource/01bf1344-62b3-430d-b565-21ee537fa6b2/download/swz_men_2020_geotiff.zip
  format: zip
  id: resource_01bf1344
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swz_men_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kingdom of Eswatini: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/5c2e6e10-51a3-4bbb-8353-3d1d95420926/resource/b30d50f7-984b-4316-a1c4-39dd645732c3/download/swz_women_2020_csv.zip
  format: zip
  id: resource_b30d50f7
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swz_women_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kingdom of Eswatini: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/5c2e6e10-51a3-4bbb-8353-3d1d95420926/resource/ddc849d2-884a-4307-95d5-3942eff45d89/download/swz_women_2020_geotiff.zip
  format: zip
  id: resource_ddc849d2
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swz_women_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kingdom of Eswatini: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/5c2e6e10-51a3-4bbb-8353-3d1d95420926/resource/bd4e16e5-cb4b-4ffd-90b5-c4e115a9b7ba/download/swz_women_of_reproductive_age_15_49_2020_csv.zip
  format: zip
  id: resource_bd4e16e5
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swz_women_of_reproductive_age_15_49_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kingdom of Eswatini: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/5c2e6e10-51a3-4bbb-8353-3d1d95420926/resource/f53e7e54-c36a-4008-9a97-62e32e58d49c/download/swz_women_of_reproductive_age_15_49_2020_geotiff.zip
  format: zip
  id: resource_f53e7e54
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swz_women_of_reproductive_age_15_49_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kingdom of Eswatini: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/5c2e6e10-51a3-4bbb-8353-3d1d95420926/resource/bd8d2ec2-4745-49b4-ae71-59192842742b/download/swz_youth_15_24_2020_csv.zip
  format: zip
  id: resource_bd8d2ec2
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swz_youth_15_24_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kingdom of Eswatini: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/5c2e6e10-51a3-4bbb-8353-3d1d95420926/resource/f1675beb-ca89-4d2b-a96d-44638e49b4be/download/swz_youth_15_24_2020_geotiff.zip
  format: zip
  id: resource_f1675beb
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swz_youth_15_24_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kingdom of Eswatini: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/5c2e6e10-51a3-4bbb-8353-3d1d95420926/resource/81c27372-1eaf-436b-92b2-cd687f58fe70/download/swz_dg_metadata.json.zip
  format: null
  id: resource_81c27372
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swz_dg_metadata.json.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-swz_metad4g_kingdomhighresolutionpopu_2018
spatial:
  bbox: null
  centroid: null
  countries:
  - SWZ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2021-12-07'
  start: '2018-10-01'
temporal_resolution: null
title: 'Kingdom of Eswatini: High Resolution Population Density Maps + Demographic
  Estimates'
version: null
vulnerability: null
---
