---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook (Meta)
    url: https://data.humdata.org/dataset/guam-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/guam-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/guam-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/guam-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-gum_metad4g_guamhighresolutionpopulat_2019
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Guam: (1) Overall population density
  (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly (ages
  60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/guam-high-resolution-population-density-maps-demographic-estimates]'
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
    using a methodology developed in partnership with Columbia University, producing
    high-resolution gridded population density maps for Guam at multiple demographic
    stratifications.
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
- href: https://data.humdata.org/dataset/guam-high-resolution-population-density-maps-demographic-estimates
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
  description: 'Guam: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/ec4b463e-f79c-4d21-8de1-7207c6f78282/resource/d1482623-7bdf-4adb-b5f1-955b4fee205b/download/gum_children_under_five_2020_csv.zip
  format: zip
  id: resource_d1482623
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gum_children_under_five_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guam: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/ec4b463e-f79c-4d21-8de1-7207c6f78282/resource/a2f3fe8d-25a5-400c-96ea-3c48ef5a2610/download/gum_children_under_five_2020_geotiff.zip
  format: zip
  id: resource_a2f3fe8d
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gum_children_under_five_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guam: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/ec4b463e-f79c-4d21-8de1-7207c6f78282/resource/9bc80ad9-3b4e-4eb6-bed4-153bb6c8fe83/download/gum_elderly_60_plus_2020_csv.zip
  format: zip
  id: resource_9bc80ad9
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gum_elderly_60_plus_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guam: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/ec4b463e-f79c-4d21-8de1-7207c6f78282/resource/f13af1a2-f13f-4355-8b31-f3e451240f29/download/gum_elderly_60_plus_2020_geotiff.zip
  format: zip
  id: resource_f13af1a2
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gum_elderly_60_plus_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guam: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/ec4b463e-f79c-4d21-8de1-7207c6f78282/resource/0b4680b9-7fb6-4217-9f1d-25d5a0dc8cdc/download/gum_men_2020_csv.zip
  format: zip
  id: resource_0b4680b9
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gum_men_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guam: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/ec4b463e-f79c-4d21-8de1-7207c6f78282/resource/c88523b5-d0db-4165-a713-20976041b972/download/gum_men_2020_geotiff.zip
  format: zip
  id: resource_c88523b5
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gum_men_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guam: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/ec4b463e-f79c-4d21-8de1-7207c6f78282/resource/f98e34c5-ffdb-45fa-ad70-09905ecec570/download/gum_women_2020_csv.zip
  format: zip
  id: resource_f98e34c5
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gum_women_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guam: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/ec4b463e-f79c-4d21-8de1-7207c6f78282/resource/97fb8e6c-c365-4f3d-bb32-53c411090d03/download/gum_women_2020_geotiff.zip
  format: zip
  id: resource_97fb8e6c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gum_women_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guam: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/ec4b463e-f79c-4d21-8de1-7207c6f78282/resource/0cae243e-8d74-4217-bb5f-03c85bc595d8/download/gum_women_of_reproductive_age_15_49_2020_csv.zip
  format: zip
  id: resource_0cae243e
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gum_women_of_reproductive_age_15_49_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guam: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/ec4b463e-f79c-4d21-8de1-7207c6f78282/resource/d5fcda53-354d-41ec-8bb4-06f0c29b61da/download/gum_women_of_reproductive_age_15_49_2020_geotiff.zip
  format: zip
  id: resource_d5fcda53
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gum_women_of_reproductive_age_15_49_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guam: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/ec4b463e-f79c-4d21-8de1-7207c6f78282/resource/3034d2bc-e947-4a76-8d4c-064517ee205d/download/gum_youth_15_24_2020_csv.zip
  format: zip
  id: resource_3034d2bc
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gum_youth_15_24_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guam: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/ec4b463e-f79c-4d21-8de1-7207c6f78282/resource/54d89cd4-9757-4abe-88ee-f7244c29318e/download/gum_youth_15_24_2020_geotiff.zip
  format: zip
  id: resource_54d89cd4
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gum_youth_15_24_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guam: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/ec4b463e-f79c-4d21-8de1-7207c6f78282/resource/5da60322-4b62-49af-8d07-062ee48972d5/download/gum_general_2020_geotiff.zip
  format: zip
  id: resource_5da60322
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gum_general_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guam: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/ec4b463e-f79c-4d21-8de1-7207c6f78282/resource/691297a8-9c24-4886-bb86-cadb1b2f530b/download/gum_general_2020_csv.zip
  format: zip
  id: resource_691297a8
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gum_general_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This file has information about the cloud cover percentage and capture
    data of the satellite images used.
  download_url: https://data.humdata.org/dataset/ec4b463e-f79c-4d21-8de1-7207c6f78282/resource/3dd7b7dd-652f-4f77-866e-d1f5cd44e748/download/gum_dg_metadata.json.zip
  format: null
  id: resource_3dd7b7dd
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gum_dg_metadata.json.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-gum_metad4g_guamhighresolutionpopulat_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - GUM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-03-22'
  start: '2019-06-19'
temporal_resolution: null
title: 'Guam: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
