---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook (AI and Data for Good at Meta)
    url: https://data.humdata.org/dataset/solomon-islands-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/solomon-islands-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/solomon-islands-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/solomon-islands-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-slb_metad4g_highresolutionpopulationd_201906
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in the Solomon Islands : (1) Overall
  population density (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24)
  (6) Elderly (ages 60+) (7) Women of reproductive age (ages 15-49).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/solomon-islands-high-resolution-population-density-maps-demographic-estimates]'
details: "To reference this data, please use the following citation: Facebook Connectivity\
  \ Lab and Center for International Earth Science Information Network - CIESIN -\
  \ Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery\
  \ for HRSL \xC2\xA9 2016 DigitalGlobe. Accessed DAY MONTH YEAR.' Please note that\
  \ as of 2024, Meta's high resolution population density maps are no longer being\
  \ updated."
exposure:
- asset_type:
    description: High-resolution gridded population density estimates disaggregated
      by age groups (children 0-5, youth 15-24, elderly 60+), sex (men, women), and
      reproductive status (women 15-49)
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
    satellite imagery across Solomon Islands. Population estimates from publicly available
    census data were spatially distributed to building locations and aggregated into
    high-resolution grids, with demographic disaggregation by age group and sex applied
    using census-based proportions.
  sources:
  - id: source_1
    license: null
    name: Facebook (AI and Data for Good at Meta)
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
- href: https://data.humdata.org/dataset/solomon-islands-high-resolution-population-density-maps-demographic-estimates
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
  description: 'Solomon Islands: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/edabfbfd-ae88-414d-acbc-cdeefda09b87/resource/cd0d903f-d3ad-4b35-8702-4aa5a1534666/download/slb_children_under_five_2019-06-01_csv.zip
  format: null
  id: resource_cd0d903f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SLB_children_under_five_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Solomon Islands: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/edabfbfd-ae88-414d-acbc-cdeefda09b87/resource/e6052c3f-6c7f-4ba8-b370-ac39d8086dd5/download/slb_children_under_five_2019-06-01_geotiff.zip
  format: null
  id: resource_e6052c3f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SLB_children_under_five_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Solomon Islands: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/edabfbfd-ae88-414d-acbc-cdeefda09b87/resource/7a53dbb4-b67e-4e74-9ddb-8e607c1b43d0/download/slb_elderly_60_plus_2019-06-01_csv.zip
  format: null
  id: resource_7a53dbb4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SLB_elderly_60_plus_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Solomon Islands: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/edabfbfd-ae88-414d-acbc-cdeefda09b87/resource/8c7f1c93-e459-46ec-adcc-dbcec61dffbe/download/slb_elderly_60_plus_2019-06-01_geotiff.zip
  format: null
  id: resource_8c7f1c93
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SLB_elderly_60_plus_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Solomon Islands: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/edabfbfd-ae88-414d-acbc-cdeefda09b87/resource/b0077cc3-8067-464f-a2b6-cd202628dcbc/download/slb_men_2019-06-01_csv.zip
  format: null
  id: resource_b0077cc3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SLB_men_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Solomon Islands: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/edabfbfd-ae88-414d-acbc-cdeefda09b87/resource/6458bb54-66a2-42be-9160-8071f941ed27/download/slb_men_2019-06-01_geotiff.zip
  format: null
  id: resource_6458bb54
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SLB_men_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Solomon Islands: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/edabfbfd-ae88-414d-acbc-cdeefda09b87/resource/de2a4aa4-735b-44c5-a8c1-32adc63d0e22/download/slb_women_2019-06-01_csv.zip
  format: null
  id: resource_de2a4aa4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SLB_women_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Solomon Islands: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/edabfbfd-ae88-414d-acbc-cdeefda09b87/resource/9e8b1392-f1c2-4fe8-9f1b-44749c33399a/download/slb_women_2019-06-01_geotiff.zip
  format: null
  id: resource_9e8b1392
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SLB_women_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Solomon Islands: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/edabfbfd-ae88-414d-acbc-cdeefda09b87/resource/dd6fd1ab-4dee-4806-9058-2b1e02afe34c/download/slb_women_of_reproductive_age_15_49_2019-06-01_csv.zip
  format: null
  id: resource_dd6fd1ab
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SLB_women_of_reproductive_age_15_49_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Solomon Islands: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/edabfbfd-ae88-414d-acbc-cdeefda09b87/resource/ca61cdf2-b27b-477d-8552-40a99ba618d5/download/slb_women_of_reproductive_age_15_49_2019-06-01_geotiff.zip
  format: null
  id: resource_ca61cdf2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SLB_women_of_reproductive_age_15_49_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Solomon Islands: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/edabfbfd-ae88-414d-acbc-cdeefda09b87/resource/1060b866-9285-4f48-b99a-288f07517e41/download/slb_youth_15_24_2019-06-01_csv.zip
  format: null
  id: resource_1060b866
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SLB_youth_15_24_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Solomon Islands: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/edabfbfd-ae88-414d-acbc-cdeefda09b87/resource/81ea1dfa-7ae1-47da-a6db-3b12d5d4f8bd/download/slb_youth_15_24_2019-06-01_geotiff.zip
  format: null
  id: resource_81ea1dfa
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SLB_youth_15_24_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Solomon Islands: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/edabfbfd-ae88-414d-acbc-cdeefda09b87/resource/b1d33bfb-0f9d-45c2-8883-562b42b5ffaa/download/population_slb_2018-10-01_geotiff.zip
  format: null
  id: resource_b1d33bfb
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_slb_2018-10-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Solomon Islands: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/edabfbfd-ae88-414d-acbc-cdeefda09b87/resource/50074929-02bd-414a-91ef-e8f3359cbbd4/download/population_slb_2018-10-01.csv.zip
  format: null
  id: resource_50074929
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_slb_2018-10-01.csv.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-slb_metad4g_highresolutionpopulationd_201906
spatial:
  bbox: null
  centroid: null
  countries:
  - SLB
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2019-06-21'
  start: '2019-06-19'
temporal_resolution: null
title: 'Solomon Islands: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
