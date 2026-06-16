---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook Data for Good
    url: https://data.humdata.org/dataset/singapore-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/singapore-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/singapore-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/singapore-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-sgp_metad4g_highresolutionpopulationd_2019
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Singapore: (1) Overall population
  density (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly
  (ages 60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/singapore-high-resolution-population-density-maps-demographic-estimates]'
details: "To reference this data, please use the following citation: Facebook Connectivity\
  \ Lab and Center for International Earth Science Information Network - CIESIN -\
  \ Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery\
  \ for HRSL \xC2\xA9 2016 DigitalGlobe. Accessed DAY MONTH YEAR.' Please note that\
  \ as of 2024, Meta's high resolution population density maps are no longer being\
  \ updated."
exposure:
- asset_type:
    description: High-resolution gridded population density estimates for Singapore
      disaggregated by demographic groups (overall, women, men, children 0-5, youth
      15-24, elderly 60+, women of reproductive age 15-49)
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
    high-resolution gridded population density maps disaggregated by demographic cohorts.
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
- href: https://data.humdata.org/dataset/singapore-high-resolution-population-density-maps-demographic-estimates
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
  description: 'Singapore: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/a9d030f7-c0be-4ecc-b0f1-9c9b30752095/resource/1e60943c-1cea-4719-9522-c20eb8fab25c/download/sgp_children_under_five_2020_csv.zip
  format: zip
  id: resource_1e60943c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sgp_children_under_five_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Singapore: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/a9d030f7-c0be-4ecc-b0f1-9c9b30752095/resource/267fd68d-d322-4fe0-be39-8c780960658a/download/sgp_children_under_five_2020_geotiff.zip
  format: zip
  id: resource_267fd68d
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sgp_children_under_five_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Singapore: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/a9d030f7-c0be-4ecc-b0f1-9c9b30752095/resource/228e8f2c-5510-4ffc-b5f3-94b32c7b39af/download/sgp_elderly_60_plus_2020_csv.zip
  format: zip
  id: resource_228e8f2c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sgp_elderly_60_plus_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Singapore: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/a9d030f7-c0be-4ecc-b0f1-9c9b30752095/resource/66617408-e796-420d-b8ff-a12af0e4db8e/download/sgp_elderly_60_plus_2020_geotiff.zip
  format: zip
  id: resource_66617408
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sgp_elderly_60_plus_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Singapore: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/a9d030f7-c0be-4ecc-b0f1-9c9b30752095/resource/5dbbd9cb-045c-465d-a10a-9f8352ef3f49/download/sgp_men_2020_csv.zip
  format: zip
  id: resource_5dbbd9cb
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sgp_men_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Singapore: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/a9d030f7-c0be-4ecc-b0f1-9c9b30752095/resource/c7030867-5d97-447a-9a60-3212663a3ab9/download/sgp_men_2020_geotiff.zip
  format: zip
  id: resource_c7030867
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sgp_men_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Singapore: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/a9d030f7-c0be-4ecc-b0f1-9c9b30752095/resource/eaf7f9c1-7148-468c-b2af-74319020b15a/download/sgp_women_2020_csv.zip
  format: zip
  id: resource_eaf7f9c1
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sgp_women_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Singapore: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/a9d030f7-c0be-4ecc-b0f1-9c9b30752095/resource/b0fec895-c508-4868-8927-ad193412cefd/download/sgp_women_2020_geotiff.zip
  format: zip
  id: resource_b0fec895
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sgp_women_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Singapore: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/a9d030f7-c0be-4ecc-b0f1-9c9b30752095/resource/e7eccf5a-b375-452c-a100-52ab4a286450/download/sgp_women_of_reproductive_age_15_49_2020_csv.zip
  format: zip
  id: resource_e7eccf5a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sgp_women_of_reproductive_age_15_49_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Singapore: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/a9d030f7-c0be-4ecc-b0f1-9c9b30752095/resource/da0c886e-0cbc-4987-9ffb-781b027fb7b7/download/sgp_women_of_reproductive_age_15_49_2020_geotiff.zip
  format: zip
  id: resource_da0c886e
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sgp_women_of_reproductive_age_15_49_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Singapore: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/a9d030f7-c0be-4ecc-b0f1-9c9b30752095/resource/1f257bfc-5de4-47ba-97c6-927c950fc81b/download/sgp_youth_15_24_2020_csv.zip
  format: zip
  id: resource_1f257bfc
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sgp_youth_15_24_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Singapore: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/a9d030f7-c0be-4ecc-b0f1-9c9b30752095/resource/b7ec3eef-8efd-4530-a2d9-7b181ccff168/download/sgp_youth_15_24_2020_geotiff.zip
  format: zip
  id: resource_b7ec3eef
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sgp_youth_15_24_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Singapore: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/a9d030f7-c0be-4ecc-b0f1-9c9b30752095/resource/156e8c21-7132-4038-8464-8e903bd9fc07/download/sgp_general_2020_geotiff.zip
  format: zip
  id: resource_156e8c21
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sgp_general_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Singapore: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/a9d030f7-c0be-4ecc-b0f1-9c9b30752095/resource/c94f3397-64a1-4361-b9b8-f7d399da22e2/download/sgp_general_2020_csv.zip
  format: zip
  id: resource_c94f3397
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sgp_general_2020_csv.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-sgp_metad4g_highresolutionpopulationd_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - SGP
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-03-11'
  start: '2019-06-19'
temporal_resolution: null
title: 'Singapore: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
