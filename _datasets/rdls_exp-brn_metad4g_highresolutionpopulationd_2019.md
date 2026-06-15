---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook Data for Good
    url: https://data.humdata.org/dataset/brunei-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/brunei-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/brunei-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/brunei-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-brn_metad4g_highresolutionpopulationd_2019
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Brunei: (1) Overall population density
  (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly (ages
  60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/brunei-high-resolution-population-density-maps-demographic-estimates]'
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Machine learning algorithms identified building footprints from commercial
    satellite imagery. Population estimates derived from publicly available census
    data and demographic statistics were spatially allocated to building locations
    using Columbia University's methodology, producing high-resolution gridded population
    density maps for Brunei at the 2020 reference year, disaggregated by demographic
    cohorts.
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
- href: https://data.humdata.org/dataset/brunei-high-resolution-population-density-maps-demographic-estimates
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
  description: 'Brunei Darussalam - Brunei: High Resolution Population Density Maps
    + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/a4ecd606-4478-4469-8e96-b9b2245206be/resource/7eb0e0bc-f1fe-491b-aaf6-239c34350fc6/download/brn_children_under_five_2020_csv.zip
  format: zip
  id: resource_7eb0e0bc
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: brn_children_under_five_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Brunei Darussalam - Brunei: High Resolution Population Density Maps
    + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/a4ecd606-4478-4469-8e96-b9b2245206be/resource/5cc9cfeb-51f2-4dca-a24d-fdd4f3e452cf/download/brn_children_under_five_2020_geotiff.zip
  format: zip
  id: resource_5cc9cfeb
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: brn_children_under_five_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Brunei Darussalam - Brunei: High Resolution Population Density Maps
    + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/a4ecd606-4478-4469-8e96-b9b2245206be/resource/e36e60f4-5d2b-4cb0-9047-654bb9e1b4f3/download/brn_elderly_60_plus_2020_csv.zip
  format: zip
  id: resource_e36e60f4
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: brn_elderly_60_plus_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Brunei Darussalam - Brunei: High Resolution Population Density Maps
    + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/a4ecd606-4478-4469-8e96-b9b2245206be/resource/5c3a55f6-2884-449f-ad45-b0a2d2986aa3/download/brn_elderly_60_plus_2020_geotiff.zip
  format: zip
  id: resource_5c3a55f6
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: brn_elderly_60_plus_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Brunei Darussalam - Brunei: High Resolution Population Density Maps
    + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/a4ecd606-4478-4469-8e96-b9b2245206be/resource/aacde206-6c3b-4f7d-a9c2-5afb433d5610/download/brn_men_2020_csv.zip
  format: zip
  id: resource_aacde206
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: brn_men_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Brunei Darussalam - Brunei: High Resolution Population Density Maps
    + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/a4ecd606-4478-4469-8e96-b9b2245206be/resource/d587f2b1-6258-48c8-b99b-15940a3e0498/download/brn_men_2020_geotiff.zip
  format: zip
  id: resource_d587f2b1
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: brn_men_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Brunei Darussalam - Brunei: High Resolution Population Density Maps
    + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/a4ecd606-4478-4469-8e96-b9b2245206be/resource/b47911d3-974c-463c-88e3-5d6a0fa3d8e2/download/brn_women_2020_csv.zip
  format: zip
  id: resource_b47911d3
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: brn_women_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Brunei Darussalam - Brunei: High Resolution Population Density Maps
    + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/a4ecd606-4478-4469-8e96-b9b2245206be/resource/15d99e67-a875-4a23-a4ba-577d8961ddae/download/brn_women_2020_geotiff.zip
  format: zip
  id: resource_15d99e67
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: brn_women_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Brunei Darussalam - Brunei: High Resolution Population Density Maps
    + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/a4ecd606-4478-4469-8e96-b9b2245206be/resource/ce1a9b89-aca3-426e-bf35-7a139c0f1cac/download/brn_women_of_reproductive_age_15_49_2020_csv.zip
  format: zip
  id: resource_ce1a9b89
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: brn_women_of_reproductive_age_15_49_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Brunei Darussalam - Brunei: High Resolution Population Density Maps
    + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/a4ecd606-4478-4469-8e96-b9b2245206be/resource/0d58009a-6c1d-4172-87ee-c4a99eb4a38b/download/brn_women_of_reproductive_age_15_49_2020_geotiff.zip
  format: zip
  id: resource_0d58009a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: brn_women_of_reproductive_age_15_49_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Brunei Darussalam - Brunei: High Resolution Population Density Maps
    + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/a4ecd606-4478-4469-8e96-b9b2245206be/resource/2d736fe8-e08d-4dcd-b4c3-941a8e664a55/download/brn_youth_15_24_2020_csv.zip
  format: zip
  id: resource_2d736fe8
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: brn_youth_15_24_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Brunei Darussalam - Brunei: High Resolution Population Density Maps
    + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/a4ecd606-4478-4469-8e96-b9b2245206be/resource/34f18714-3b8e-431e-8f3f-a4b52ebe5828/download/brn_youth_15_24_2020_geotiff.zip
  format: zip
  id: resource_34f18714
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: brn_youth_15_24_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Brunei Darussalam - Brunei: High Resolution Population Density Maps
    + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/a4ecd606-4478-4469-8e96-b9b2245206be/resource/de4aa921-03e3-4125-91f7-8d86b1dc1060/download/brn_general_2020_geotiff.zip
  format: zip
  id: resource_de4aa921
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: brn_general_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Brunei Darussalam - Brunei: High Resolution Population Density Maps
    + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/a4ecd606-4478-4469-8e96-b9b2245206be/resource/38431dca-cae6-4d07-9d1d-e40f5e32ef2c/download/brn_general_2020_csv.zip
  format: zip
  id: resource_38431dca
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: brn_general_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Brunei Darussalam - Brunei: High Resolution Population Density Maps
    + Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/a4ecd606-4478-4469-8e96-b9b2245206be/resource/d9a453cc-79c5-4a9f-bf73-30da532fb974/download/brn_dg_metadata.json.zip
  format: null
  id: resource_d9a453cc
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: brn_dg_metadata.json.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-brn_metad4g_highresolutionpopulationd_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - BRN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-02-18'
  start: '2019-06-19'
temporal_resolution: null
title: 'Brunei Darussalam - Brunei: High Resolution Population Density Maps + Demographic
  Estimates'
version: null
vulnerability: null
---
