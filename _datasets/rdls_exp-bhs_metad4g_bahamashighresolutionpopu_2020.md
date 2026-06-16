---
attributions:
- entity:
    affiliation: null
    email: null
    name: Data for Good at Meta
    url: https://data.humdata.org/dataset/bahamas-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/bahamas-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/bahamas-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/bahamas-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-bhs_metad4g_bahamashighresolutionpopu_2020
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in the Bahamas: (1) Overall population
  density (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly
  (ages 60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/bahamas-high-resolution-population-density-maps-demographic-estimates]'
details: "To reference this data, please use the following citation: Facebook Connectivity\
  \ Lab and Center for International Earth Science Information Network - CIESIN -\
  \ Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery\
  \ for HRSL \xC2\xA9 2016 DigitalGlobe. Accessed DAY MONTH YEAR.' Please note that\
  \ as of 2024, Meta's high resolution population density maps are no longer being\
  \ updated."
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
  description: Machine learning algorithms identified building footprints from commercial
    satellite imagery across the Bahamas. Population estimates derived from publicly
    available census data were overlaid onto building-level spatial units using Columbia
    University's methodology to generate high-resolution gridded population density
    maps for seven demographic categories at approximately 100m resolution.
  sources:
  - id: source_1
    license: null
    name: Data for Good at Meta
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
- href: https://data.humdata.org/dataset/bahamas-high-resolution-population-density-maps-demographic-estimates
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
  description: 'Bahamas: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/f5dc6ef5-0776-429c-b78b-6419b00b275d/resource/e359c501-def9-46ec-a816-89026e71e5d8/download/bhs_children_under_five_2020_csv.zip
  format: null
  id: resource_e359c501
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bhs_children_under_five_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bahamas: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/f5dc6ef5-0776-429c-b78b-6419b00b275d/resource/3cdfb9b0-4df8-42e8-8ccb-3accc24df1a5/download/bhs_children_under_five_2020_geotiff.zip
  format: null
  id: resource_3cdfb9b0
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bhs_children_under_five_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bahamas: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/f5dc6ef5-0776-429c-b78b-6419b00b275d/resource/f08ce9b4-3982-4cc7-8f80-7f06e44a3347/download/bhs_elderly_60_plus_2020_csv.zip
  format: null
  id: resource_f08ce9b4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bhs_elderly_60_plus_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bahamas: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/f5dc6ef5-0776-429c-b78b-6419b00b275d/resource/a6c766fa-a613-44be-8d41-b04ccc21fce8/download/bhs_elderly_60_plus_2020_geotiff.zip
  format: null
  id: resource_a6c766fa
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bhs_elderly_60_plus_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bahamas: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/f5dc6ef5-0776-429c-b78b-6419b00b275d/resource/43884b22-bfbe-420b-8886-dfe4cde7d375/download/bhs_general_2020_csv.zip
  format: null
  id: resource_43884b22
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bhs_general_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bahamas: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/f5dc6ef5-0776-429c-b78b-6419b00b275d/resource/8f9301e0-8a2c-4af0-a79b-a4a139f63998/download/bhs_general_2020_geotiff.zip
  format: null
  id: resource_8f9301e0
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bhs_general_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bahamas: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/f5dc6ef5-0776-429c-b78b-6419b00b275d/resource/7593fec9-fb6c-4090-aa6f-a00f09086977/download/bhs_men_2020_csv.zip
  format: null
  id: resource_7593fec9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bhs_men_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bahamas: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/f5dc6ef5-0776-429c-b78b-6419b00b275d/resource/7b57cbc3-de05-408c-939f-6e5135268773/download/bhs_men_2020_geotiff.zip
  format: null
  id: resource_7b57cbc3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bhs_men_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bahamas: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/f5dc6ef5-0776-429c-b78b-6419b00b275d/resource/2e3a8aa7-72bc-4623-8c8b-34dae7809d62/download/bhs_women_2020_csv.zip
  format: null
  id: resource_2e3a8aa7
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bhs_women_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bahamas: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/f5dc6ef5-0776-429c-b78b-6419b00b275d/resource/6062ceb1-991e-4709-9dc9-fd7beb5f46e3/download/bhs_women_2020_geotiff.zip
  format: null
  id: resource_6062ceb1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bhs_women_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bahamas: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/f5dc6ef5-0776-429c-b78b-6419b00b275d/resource/10ed4665-6e37-48fe-98fb-ea8332b6b87e/download/bhs_women_of_reproductive_age_15_49_2020_csv.zip
  format: null
  id: resource_10ed4665
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bhs_women_of_reproductive_age_15_49_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bahamas: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/f5dc6ef5-0776-429c-b78b-6419b00b275d/resource/0cebfd8d-f1a8-4940-8afa-4b5f10c744d9/download/bhs_women_of_reproductive_age_15_49_2020_geotiff.zip
  format: null
  id: resource_0cebfd8d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bhs_women_of_reproductive_age_15_49_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bahamas: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/f5dc6ef5-0776-429c-b78b-6419b00b275d/resource/3d583e25-12ac-4585-9958-96c06a695a7d/download/bhs_youth_15_24_2020_csv.zip
  format: null
  id: resource_3d583e25
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bhs_youth_15_24_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bahamas: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/f5dc6ef5-0776-429c-b78b-6419b00b275d/resource/c51e7a23-8b42-425c-bab0-d66528ebe846/download/bhs_youth_15_24_2020_geotiff.zip
  format: null
  id: resource_c51e7a23
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bhs_youth_15_24_2020_geotiff.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-bhs_metad4g_bahamashighresolutionpopu_2020
spatial:
  bbox: null
  centroid: null
  countries:
  - BHS
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-03-14'
  start: '2020-01-01'
temporal_resolution: null
title: 'Bahamas: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
