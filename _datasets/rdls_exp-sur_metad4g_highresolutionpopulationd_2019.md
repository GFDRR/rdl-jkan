---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook (Meta)
    url: https://data.humdata.org/dataset/suriname-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/suriname-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/suriname-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/suriname-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-sur_metad4g_highresolutionpopulationd_2019
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Suriname: (1) Overall population
  density (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly
  (ages 60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/suriname-high-resolution-population-density-maps-demographic-estimates]'
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
license: CC-BY-4.0
lineage:
  description: High-resolution population density maps were created by applying machine
    learning algorithms to commercially available satellite imagery to identify building
    footprints, then overlaying population estimates derived from census data and
    demographic statistics in partnership with Columbia University. The resulting
    gridded datasets provide spatial distribution of total population and seven demographic
    subgroups across Suriname at fine spatial resolution.
  sources:
  - id: source_1
    license: null
    name: Facebook (Meta)
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
- href: https://data.humdata.org/dataset/suriname-high-resolution-population-density-maps-demographic-estimates
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
  description: 'Suriname: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/cf175051-1680-4ae1-adff-ba6a59b5f4ba/resource/fbe68e1a-f64f-4ffd-96bc-1880a16ae7a8/download/sur_general_2020_geotiff.zip
  format: zip
  id: resource_fbe68e1a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sur_general_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Suriname: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/cf175051-1680-4ae1-adff-ba6a59b5f4ba/resource/24468348-e720-492e-9c1f-c1149fb4148c/download/sur_general_2020_csv.zip
  format: zip
  id: resource_24468348
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sur_general_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Suriname: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/cf175051-1680-4ae1-adff-ba6a59b5f4ba/resource/13d7b3cd-0b75-444f-9aad-5818fc784fcb/download/sur_children_under_five_2020_csv.zip
  format: zip
  id: resource_13d7b3cd
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sur_children_under_five_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Suriname: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/cf175051-1680-4ae1-adff-ba6a59b5f4ba/resource/2d37e16b-e444-4193-8228-52852b98d762/download/sur_children_under_five_2020_geotiff.zip
  format: zip
  id: resource_2d37e16b
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sur_children_under_five_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Suriname: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/cf175051-1680-4ae1-adff-ba6a59b5f4ba/resource/7e700bf4-09f8-443a-a131-d0b64065fa5f/download/sur_elderly_60_plus_2020_csv.zip
  format: zip
  id: resource_7e700bf4
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sur_elderly_60_plus_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Suriname: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/cf175051-1680-4ae1-adff-ba6a59b5f4ba/resource/917651b1-64d7-42db-a5de-649628b9e1fb/download/sur_elderly_60_plus_2020_geotiff.zip
  format: zip
  id: resource_917651b1
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sur_elderly_60_plus_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Suriname: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/cf175051-1680-4ae1-adff-ba6a59b5f4ba/resource/f56a7f8d-2d97-413d-bded-53b8d7343c81/download/sur_men_2020_csv.zip
  format: zip
  id: resource_f56a7f8d
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sur_men_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Suriname: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/cf175051-1680-4ae1-adff-ba6a59b5f4ba/resource/cbb5943b-23c6-4bf9-89ee-4c9511ac63d2/download/sur_men_2020_geotiff.zip
  format: zip
  id: resource_cbb5943b
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sur_men_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Suriname: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/cf175051-1680-4ae1-adff-ba6a59b5f4ba/resource/a0a4a460-6b38-47a7-bb07-eb931fec0eaf/download/sur_women_2020_csv.zip
  format: zip
  id: resource_a0a4a460
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sur_women_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Suriname: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/cf175051-1680-4ae1-adff-ba6a59b5f4ba/resource/38c383c2-e59c-4b26-bf20-e4ecd9e20e8f/download/sur_women_2020_geotiff.zip
  format: zip
  id: resource_38c383c2
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sur_women_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Suriname: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/cf175051-1680-4ae1-adff-ba6a59b5f4ba/resource/4f318502-b411-4d68-9c56-d7f24699b482/download/sur_women_of_reproductive_age_15_49_2020_csv.zip
  format: zip
  id: resource_4f318502
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sur_women_of_reproductive_age_15_49_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Suriname: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/cf175051-1680-4ae1-adff-ba6a59b5f4ba/resource/2d14f282-77b1-45d8-b951-3264e740d932/download/sur_women_of_reproductive_age_15_49_2020_geotiff.zip
  format: zip
  id: resource_2d14f282
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sur_women_of_reproductive_age_15_49_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Suriname: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/cf175051-1680-4ae1-adff-ba6a59b5f4ba/resource/030b2035-315c-4a86-908f-83d541fd61b1/download/sur_youth_15_24_2020_csv.zip
  format: zip
  id: resource_030b2035
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sur_youth_15_24_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Suriname: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/cf175051-1680-4ae1-adff-ba6a59b5f4ba/resource/aa876ef3-b647-4f6b-8ec7-5e87d4ccb1c8/download/sur_youth_15_24_2020_geotiff.zip
  format: zip
  id: resource_aa876ef3
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sur_youth_15_24_2020_geotiff.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-sur_metad4g_highresolutionpopulationd_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - SUR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2022-09-01'
  start: '2019-06-10'
temporal_resolution: null
title: 'Suriname: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
