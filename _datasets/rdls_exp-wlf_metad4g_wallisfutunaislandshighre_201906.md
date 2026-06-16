---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook/AI and Data for Good at Meta
    url: https://data.humdata.org/dataset/wallis-and-futuna-islands-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/wallis-and-futuna-islands-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/wallis-and-futuna-islands-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/wallis-and-futuna-islands-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-wlf_metad4g_wallisfutunaislandshighre_201906
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in the Wallis and Futuna Islands: (1)
  Overall population density (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages
  15-24) (6) Elderly (ages 60+) (7) Women of reproductive age (ages 15-49).. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/wallis-and-futuna-islands-high-resolution-population-density-maps-demographic-estimates]'
details: "To reference this data, please use the following citation: Facebook Connectivity\
  \ Lab and Center for International Earth Science Information Network - CIESIN -\
  \ Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery\
  \ for HRSL \xC2\xA9 2016 DigitalGlobe. Accessed DAY MONTH YEAR.' Please note that\
  \ as of 2024, Meta's high resolution population density maps are no longer being\
  \ updated."
exposure:
- asset_type:
    description: High-resolution gridded population density maps for overall population
      and demographic subgroups (children 0-5, youth 15-24, elderly 60+, women, men,
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: High-resolution population density maps were created by applying machine
    learning algorithms to identify buildings from commercial satellite imagery, then
    overlaying population estimates derived from publicly available census data and
    demographic statistics in partnership with Columbia University. The resulting
    gridded datasets represent population distribution at fine spatial resolution
    for Wallis and Futuna Islands as of 2018-2019.
  sources:
  - id: source_1
    license: null
    name: Facebook/AI and Data for Good at Meta
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
- href: https://data.humdata.org/dataset/wallis-and-futuna-islands-high-resolution-population-density-maps-demographic-estimates
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
  description: 'Wallis and Futuna Islands: High Resolution Population Density Maps
    + Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/6f03111f-7f16-4e1e-a9c3-a07b6ce1478b/resource/23d01c6e-f0bd-4357-acf9-6e6a12298706/download/wlf_children_under_five_2019-06-01_csv.zip
  format: null
  id: resource_23d01c6e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: WLF_children_under_five_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Wallis and Futuna Islands: High Resolution Population Density Maps
    + Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/6f03111f-7f16-4e1e-a9c3-a07b6ce1478b/resource/51532add-fa08-428a-8f02-74e41fa607a9/download/wlf_children_under_five_2019-06-01_geotiff.zip
  format: null
  id: resource_51532add
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: WLF_children_under_five_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Wallis and Futuna Islands: High Resolution Population Density Maps
    + Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/6f03111f-7f16-4e1e-a9c3-a07b6ce1478b/resource/bbe9d05c-1813-478f-b7ba-ec0cca47dcd9/download/wlf_elderly_60_plus_2019-06-01_csv.zip
  format: null
  id: resource_bbe9d05c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: WLF_elderly_60_plus_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Wallis and Futuna Islands: High Resolution Population Density Maps
    + Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/6f03111f-7f16-4e1e-a9c3-a07b6ce1478b/resource/fcfb4a06-50da-4ccf-a111-0cf74ecb0a21/download/wlf_elderly_60_plus_2019-06-01_geotiff.zip
  format: null
  id: resource_fcfb4a06
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: WLF_elderly_60_plus_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Wallis and Futuna Islands: High Resolution Population Density Maps
    + Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/6f03111f-7f16-4e1e-a9c3-a07b6ce1478b/resource/198af9a3-5b98-4f8e-b984-72a439b64c7a/download/wlf_men_2019-06-01_csv.zip
  format: null
  id: resource_198af9a3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: WLF_men_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Wallis and Futuna Islands: High Resolution Population Density Maps
    + Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/6f03111f-7f16-4e1e-a9c3-a07b6ce1478b/resource/92b56548-86ef-4b94-ad22-7d8562a3d58c/download/wlf_men_2019-06-01_geotiff.zip
  format: null
  id: resource_92b56548
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: WLF_men_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Wallis and Futuna Islands: High Resolution Population Density Maps
    + Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/6f03111f-7f16-4e1e-a9c3-a07b6ce1478b/resource/0e8b02aa-1ef3-48be-885c-9046c0afa99f/download/wlf_women_2019-06-01_csv.zip
  format: null
  id: resource_0e8b02aa
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: WLF_women_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Wallis and Futuna Islands: High Resolution Population Density Maps
    + Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/6f03111f-7f16-4e1e-a9c3-a07b6ce1478b/resource/28940ce7-3cc7-4c0c-bb8d-f4671840b7ba/download/wlf_women_2019-06-01_geotiff.zip
  format: null
  id: resource_28940ce7
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: WLF_women_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Wallis and Futuna Islands: High Resolution Population Density Maps
    + Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/6f03111f-7f16-4e1e-a9c3-a07b6ce1478b/resource/2af42214-15c3-4b28-97b9-3a62cabccf8a/download/wlf_women_of_reproductive_age_15_49_2019-06-01_csv.zip
  format: null
  id: resource_2af42214
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: WLF_women_of_reproductive_age_15_49_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Wallis and Futuna Islands: High Resolution Population Density Maps
    + Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/6f03111f-7f16-4e1e-a9c3-a07b6ce1478b/resource/d140f959-f0d3-4116-a9cc-3a5830831392/download/wlf_women_of_reproductive_age_15_49_2019-06-01_geotiff.zip
  format: null
  id: resource_d140f959
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: WLF_women_of_reproductive_age_15_49_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Wallis and Futuna Islands: High Resolution Population Density Maps
    + Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/6f03111f-7f16-4e1e-a9c3-a07b6ce1478b/resource/1c03b6bd-35fd-4567-b10d-f719ad8d47f8/download/wlf_youth_15_24_2019-06-01_csv.zip
  format: null
  id: resource_1c03b6bd
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: WLF_youth_15_24_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Wallis and Futuna Islands: High Resolution Population Density Maps
    + Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/6f03111f-7f16-4e1e-a9c3-a07b6ce1478b/resource/1672af57-047d-4650-bd87-3f72f04a2429/download/wlf_youth_15_24_2019-06-01_geotiff.zip
  format: null
  id: resource_1672af57
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: WLF_youth_15_24_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Wallis and Futuna Islands: High Resolution Population Density Maps
    + Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/6f03111f-7f16-4e1e-a9c3-a07b6ce1478b/resource/a5b4e955-18dd-4166-b2e7-df0e4117c116/download/population_wlf_2018-10-01_geotiff.zip
  format: null
  id: resource_a5b4e955
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_wlf_2018-10-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Wallis and Futuna Islands: High Resolution Population Density Maps
    + Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/6f03111f-7f16-4e1e-a9c3-a07b6ce1478b/resource/48ebee50-1cf2-4791-826f-c277ce05cdcd/download/population_wlf_2018-10-01.csv.zip
  format: null
  id: resource_48ebee50
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_wlf_2018-10-01.csv.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-wlf_metad4g_wallisfutunaislandshighre_201906
spatial:
  bbox: null
  centroid: null
  countries:
  - WLF
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2019-06-21'
  start: '2019-06-19'
temporal_resolution: null
title: 'Wallis and Futuna Islands: High Resolution Population Density Maps + Demographic
  Estimates'
version: null
vulnerability: null
---
