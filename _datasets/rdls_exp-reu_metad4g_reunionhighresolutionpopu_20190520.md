---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook/Meta AI and Data for Good
    url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-reu
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-reu
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-reu
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-reu
dataset_id: rdls_exp-reu_metad4g_reunionhighresolutionpopu_20190520
description: "The world's most accurate population datasets. Seven maps/datasets for\
  \ the distribution of various populations in R\xE9union: (1) Overall population\
  \ density (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly\
  \ (ages 60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata\
  \ record was automatically extracted from the Humanitarian Data Exchange (HDX);\
  \ Original dataset: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-reu]"
details: "To reference this data, please use the following citation: Facebook Connectivity\
  \ Lab and Center for International Earth Science Information Network - CIESIN -\
  \ Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery\
  \ for HRSL \xA9 2016 DigitalGlobe. Accessed DAY MONTH YEAR.' Please note that as\
  \ of 2024, Meta's high resolution population density maps are no longer being updated."
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
  description: "Machine learning algorithms identified building footprints from commercial\
    \ satellite imagery. Population estimates derived from publicly available census\
    \ data and demographic statistics were overlaid on building locations using Columbia\
    \ University methodology to create high-resolution gridded population density\
    \ maps for R\xE9union at multiple demographic stratifications."
  sources:
  - id: source_1
    license: null
    name: Facebook/Meta AI and Data for Good
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
- href: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-reu
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
  description: "R\xE9union: High Resolution Population Density Maps + Demographic\
    \ Estimates (ZIP archive)"
  download_url: https://data.humdata.org/dataset/348b69aa-bf08-40b0-ad32-0b735c58a10d/resource/bb06ab8a-ad60-4f18-9a71-bebd6ced5c72/download/population_reu_2018-10-01.zip
  format: null
  id: resource_bb06ab8a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_reu_2018-10-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union: High Resolution Population Density Maps + Demographic\
    \ Estimates (ZIP archive)"
  download_url: https://data.humdata.org/dataset/348b69aa-bf08-40b0-ad32-0b735c58a10d/resource/9af0125d-f1c7-4524-9ecd-60e8cb805b58/download/population_reu_2018-10-01.csv.zip
  format: null
  id: resource_9af0125d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_reu_2018-10-01.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union: High Resolution Population Density Maps + Demographic\
    \ Estimates (ZIP archive)"
  download_url: https://data.humdata.org/dataset/348b69aa-bf08-40b0-ad32-0b735c58a10d/resource/3dc2c0bb-a5a7-486b-974c-5f4b7d314deb/download/reu_children_under_five_csv.zip
  format: null
  id: resource_3dc2c0bb
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: REU_children_under_five_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union: High Resolution Population Density Maps + Demographic\
    \ Estimates (ZIP archive)"
  download_url: https://data.humdata.org/dataset/348b69aa-bf08-40b0-ad32-0b735c58a10d/resource/b50c6c73-8d51-47f0-b4ac-70511c951428/download/reu_children_under_five_geotiff.zip
  format: null
  id: resource_b50c6c73
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: REU_children_under_five_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union: High Resolution Population Density Maps + Demographic\
    \ Estimates (ZIP archive)"
  download_url: https://data.humdata.org/dataset/348b69aa-bf08-40b0-ad32-0b735c58a10d/resource/3a51ffa1-7704-4df4-83cf-1ed8fbe6086f/download/reu_elderly_60_plus_csv.zip
  format: null
  id: resource_3a51ffa1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: REU_elderly_60_plus_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union: High Resolution Population Density Maps + Demographic\
    \ Estimates (ZIP archive)"
  download_url: https://data.humdata.org/dataset/348b69aa-bf08-40b0-ad32-0b735c58a10d/resource/8cf51620-3c08-4376-830a-6ecb9973f142/download/reu_elderly_60_plus_geotiff.zip
  format: null
  id: resource_8cf51620
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: REU_elderly_60_plus_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union: High Resolution Population Density Maps + Demographic\
    \ Estimates (ZIP archive)"
  download_url: https://data.humdata.org/dataset/348b69aa-bf08-40b0-ad32-0b735c58a10d/resource/d641b146-cfc4-4cc0-be6a-94373804b754/download/reu_men_csv.zip
  format: null
  id: resource_d641b146
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: REU_men_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union: High Resolution Population Density Maps + Demographic\
    \ Estimates (ZIP archive)"
  download_url: https://data.humdata.org/dataset/348b69aa-bf08-40b0-ad32-0b735c58a10d/resource/41fc6615-fff8-4a58-b6e5-e1838577a8d0/download/reu_men_geotiff.zip
  format: null
  id: resource_41fc6615
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: REU_men_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union: High Resolution Population Density Maps + Demographic\
    \ Estimates (ZIP archive)"
  download_url: https://data.humdata.org/dataset/348b69aa-bf08-40b0-ad32-0b735c58a10d/resource/67acb4ab-6034-4136-9c9a-6bf7898f9f52/download/reu_women_csv.zip
  format: null
  id: resource_67acb4ab
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: REU_women_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union: High Resolution Population Density Maps + Demographic\
    \ Estimates (ZIP archive)"
  download_url: https://data.humdata.org/dataset/348b69aa-bf08-40b0-ad32-0b735c58a10d/resource/1b73aea9-d507-45a3-a5f2-03c335b98f04/download/reu_women_geotiff.zip
  format: null
  id: resource_1b73aea9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: REU_women_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union: High Resolution Population Density Maps + Demographic\
    \ Estimates (ZIP archive)"
  download_url: https://data.humdata.org/dataset/348b69aa-bf08-40b0-ad32-0b735c58a10d/resource/5d8cb95f-f7e5-4353-b53f-fecfafd695d2/download/reu_women_of_reproductive_age_15_49_csv.zip
  format: null
  id: resource_5d8cb95f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: REU_women_of_reproductive_age_15_49_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union: High Resolution Population Density Maps + Demographic\
    \ Estimates (ZIP archive)"
  download_url: https://data.humdata.org/dataset/348b69aa-bf08-40b0-ad32-0b735c58a10d/resource/3668e4ab-e7aa-40fb-a654-305cde58e5dd/download/reu_women_of_reproductive_age_15_49_geotiff.zip
  format: null
  id: resource_3668e4ab
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: REU_women_of_reproductive_age_15_49_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union: High Resolution Population Density Maps + Demographic\
    \ Estimates (ZIP archive)"
  download_url: https://data.humdata.org/dataset/348b69aa-bf08-40b0-ad32-0b735c58a10d/resource/e7ad383b-48af-4585-b1f5-56766eded137/download/reu_youth_15_24_csv.zip
  format: null
  id: resource_e7ad383b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: REU_youth_15_24_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union: High Resolution Population Density Maps + Demographic\
    \ Estimates (ZIP archive)"
  download_url: https://data.humdata.org/dataset/348b69aa-bf08-40b0-ad32-0b735c58a10d/resource/4eab6f8c-73e7-4f81-9734-e632f18f22eb/download/reu_youth_15_24_geotiff.zip
  format: null
  id: resource_4eab6f8c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: REU_youth_15_24_geotiff.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-reu_metad4g_reunionhighresolutionpopu_20190520
spatial:
  bbox: null
  centroid: null
  countries:
  - REU
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2019-05-20'
temporal_resolution: null
title: "R\xE9union: High Resolution Population Density Maps + Demographic Estimates"
version: null
vulnerability: null
---
