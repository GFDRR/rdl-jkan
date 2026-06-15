---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook Data for Good
    url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-civ
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-civ
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-civ
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-civ
dataset_id: rdls_exp-civ_metad4g_highresolutionpopulationd_2019
description: "The world's most accurate population datasets. Seven maps/datasets for\
  \ the distribution of various populations in C\xF4te d'Ivoire: (1) Overall population\
  \ density (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly\
  \ (ages 60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata\
  \ record was automatically extracted from the Humanitarian Data Exchange (HDX);\
  \ Original dataset: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-civ]"
details: "To reference this data, please use the following citation: Facebook Connectivity\
  \ Lab and Center for International Earth Science Information Network - CIESIN -\
  \ Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery\
  \ for HRSL \xA9 2016 DigitalGlobe. Accessed DAY MONTH YEAR.' Please note that as\
  \ of 2024, Meta's high resolution population density maps are no longer being updated."
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
  description: "Machine learning algorithms identified building footprints from commercial\
    \ satellite imagery across C\xF4te d'Ivoire. Population estimates derived from\
    \ publicly available census data and demographic statistics were then spatially\
    \ allocated to building locations using Columbia University's methodology, producing\
    \ seven high-resolution gridded population density maps disaggregated by demographic\
    \ groups (overall, gender, age cohorts) at 2020 baseline."
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
- href: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-civ
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
  description: "C\xF4te d'Ivoire: High Resolution Population Density Maps + Demographic\
    \ Estimates (zip)"
  download_url: https://data.humdata.org/dataset/55da8db5-f23a-489d-8bf4-324fa309c87c/resource/f14b9e0e-c057-46e0-8732-30d14b9239ee/download/civ_general_2020_geotiff.zip
  format: zip
  id: resource_f14b9e0e
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_general_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire: High Resolution Population Density Maps + Demographic\
    \ Estimates (zip)"
  download_url: https://data.humdata.org/dataset/55da8db5-f23a-489d-8bf4-324fa309c87c/resource/422d1406-a774-4cd9-8ff6-161d975574b1/download/civ_general_2020_csv.zip
  format: zip
  id: resource_422d1406
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_general_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire: High Resolution Population Density Maps + Demographic\
    \ Estimates (zip)"
  download_url: https://data.humdata.org/dataset/55da8db5-f23a-489d-8bf4-324fa309c87c/resource/fb76a2c2-f4e1-4ac3-b127-0158aed2f921/download/civ_children_under_five_2020_csv.zip
  format: zip
  id: resource_fb76a2c2
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_children_under_five_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire: High Resolution Population Density Maps + Demographic\
    \ Estimates (zip)"
  download_url: https://data.humdata.org/dataset/55da8db5-f23a-489d-8bf4-324fa309c87c/resource/a84b1a28-46e2-4d33-b23d-1b19070082e5/download/civ_children_under_five_2020_geotiff.zip
  format: zip
  id: resource_a84b1a28
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_children_under_five_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire: High Resolution Population Density Maps + Demographic\
    \ Estimates (zip)"
  download_url: https://data.humdata.org/dataset/55da8db5-f23a-489d-8bf4-324fa309c87c/resource/77d1723b-d01e-4749-99cf-a6be2fe506b8/download/civ_elderly_60_plus_2020_csv.zip
  format: zip
  id: resource_77d1723b
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_elderly_60_plus_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire: High Resolution Population Density Maps + Demographic\
    \ Estimates (zip)"
  download_url: https://data.humdata.org/dataset/55da8db5-f23a-489d-8bf4-324fa309c87c/resource/6cfc1a7b-e9c7-4d52-8293-d849aa2ff8ec/download/civ_elderly_60_plus_2020_geotiff.zip
  format: zip
  id: resource_6cfc1a7b
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_elderly_60_plus_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire: High Resolution Population Density Maps + Demographic\
    \ Estimates (zip)"
  download_url: https://data.humdata.org/dataset/55da8db5-f23a-489d-8bf4-324fa309c87c/resource/185f8d31-76cf-450f-9bd8-c7134c28b04f/download/civ_men_2020_csv.zip
  format: zip
  id: resource_185f8d31
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_men_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire: High Resolution Population Density Maps + Demographic\
    \ Estimates (zip)"
  download_url: https://data.humdata.org/dataset/55da8db5-f23a-489d-8bf4-324fa309c87c/resource/844fa44d-31a4-47fc-8006-e522ba022dda/download/civ_men_2020_geotiff.zip
  format: zip
  id: resource_844fa44d
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_men_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire: High Resolution Population Density Maps + Demographic\
    \ Estimates (zip)"
  download_url: https://data.humdata.org/dataset/55da8db5-f23a-489d-8bf4-324fa309c87c/resource/aaf0725a-e1ab-4cc4-bad1-cbb1905c4467/download/civ_women_2020_csv.zip
  format: zip
  id: resource_aaf0725a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_women_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire: High Resolution Population Density Maps + Demographic\
    \ Estimates (zip)"
  download_url: https://data.humdata.org/dataset/55da8db5-f23a-489d-8bf4-324fa309c87c/resource/af3086b5-d090-4f22-b175-24796fe80a65/download/civ_women_2020_geotiff.zip
  format: zip
  id: resource_af3086b5
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_women_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire: High Resolution Population Density Maps + Demographic\
    \ Estimates (zip)"
  download_url: https://data.humdata.org/dataset/55da8db5-f23a-489d-8bf4-324fa309c87c/resource/51dc2de4-aecf-44b7-a89d-ea6ff4249a74/download/civ_women_of_reproductive_age_15_49_2020_csv.zip
  format: zip
  id: resource_51dc2de4
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_women_of_reproductive_age_15_49_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire: High Resolution Population Density Maps + Demographic\
    \ Estimates (zip)"
  download_url: https://data.humdata.org/dataset/55da8db5-f23a-489d-8bf4-324fa309c87c/resource/eaeb0e54-4606-4933-b252-904a0f6c4951/download/civ_women_of_reproductive_age_15_49_2020_geotiff.zip
  format: zip
  id: resource_eaeb0e54
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_women_of_reproductive_age_15_49_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire: High Resolution Population Density Maps + Demographic\
    \ Estimates (zip)"
  download_url: https://data.humdata.org/dataset/55da8db5-f23a-489d-8bf4-324fa309c87c/resource/ee176089-9470-4062-8f33-1182bd967590/download/civ_youth_15_24_2020_csv.zip
  format: zip
  id: resource_ee176089
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_youth_15_24_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire: High Resolution Population Density Maps + Demographic\
    \ Estimates (zip)"
  download_url: https://data.humdata.org/dataset/55da8db5-f23a-489d-8bf4-324fa309c87c/resource/2148ce08-7099-46ab-a655-c4a4e76c1807/download/civ_youth_15_24_2020_geotiff.zip
  format: zip
  id: resource_2148ce08
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_youth_15_24_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This file has information about the cloud cover percentage and capture
    data of the satellite images used.
  download_url: https://data.humdata.org/dataset/55da8db5-f23a-489d-8bf4-324fa309c87c/resource/7d4261d8-9025-4085-8e0b-aa220a7d6e3e/download/civ_dg_metadata.json.zip
  format: null
  id: resource_7d4261d8
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_dg_metadata.json.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-civ_metad4g_highresolutionpopulationd_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - CIV
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2022-08-15'
  start: '2019-05-20'
temporal_resolution: null
title: "C\xF4te d'Ivoire: High Resolution Population Density Maps + Demographic Estimates"
version: null
vulnerability: null
---
