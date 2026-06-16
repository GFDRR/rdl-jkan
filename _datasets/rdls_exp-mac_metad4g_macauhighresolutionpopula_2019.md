---
attributions:
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/macau-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/macau-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/macau-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-mac_metad4g_macauhighresolutionpopula_2019
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Macau: (1) Overall population density
  (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly (ages
  60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/macau-high-resolution-population-density-maps-demographic-estimates]'
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
  description: High-resolution population density maps were created by applying machine
    learning algorithms to identify building footprints from commercial satellite
    imagery, then overlaying population estimates derived from publicly available
    census data and demographic statistics in partnership with Columbia University.
    The resulting gridded datasets represent spatial distribution of total population
    and seven demographic subgroups at fine resolution for disaster risk exposure
    assessment.
  sources:
  - id: source_1
    license: null
    name: AI and Data for Good at Meta
    risk_data_type:
    - exposure
    type: model
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
- href: https://data.humdata.org/dataset/macau-high-resolution-population-density-maps-demographic-estimates
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
  description: 'Macao - Macau: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/a822e0e9-275f-4c0e-b14f-5feae3de848c/resource/c9160d3b-8a46-46af-99a0-064ce6f5b417/download/mac_children_under_five_2020_csv.zip
  format: zip
  id: resource_c9160d3b
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_children_under_five_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Macao - Macau: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/a822e0e9-275f-4c0e-b14f-5feae3de848c/resource/148bc4f5-dcb1-4ca9-be40-b9d08a5ade9a/download/mac_children_under_five_2020_geotiff.zip
  format: zip
  id: resource_148bc4f5
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_children_under_five_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Macao - Macau: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/a822e0e9-275f-4c0e-b14f-5feae3de848c/resource/ae1440ad-0d01-44c3-8f5e-b9a3adcd7263/download/mac_elderly_60_plus_2020_csv.zip
  format: zip
  id: resource_ae1440ad
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_elderly_60_plus_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Macao - Macau: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/a822e0e9-275f-4c0e-b14f-5feae3de848c/resource/d7efbe9e-df56-4686-bb73-e77518c8f471/download/mac_elderly_60_plus_2020_geotiff.zip
  format: zip
  id: resource_d7efbe9e
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_elderly_60_plus_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Macao - Macau: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/a822e0e9-275f-4c0e-b14f-5feae3de848c/resource/1c3d2bfb-32e8-4909-a7c5-019a1dea3e9a/download/mac_men_2020_csv.zip
  format: zip
  id: resource_1c3d2bfb
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_men_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Macao - Macau: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/a822e0e9-275f-4c0e-b14f-5feae3de848c/resource/8efb98d7-c6a3-4053-b9ef-6dd7c0cb921f/download/mac_men_2020_geotiff.zip
  format: zip
  id: resource_8efb98d7
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_men_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Macao - Macau: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/a822e0e9-275f-4c0e-b14f-5feae3de848c/resource/ae38e71a-9472-4c25-bd49-b9d19fa46eb5/download/mac_women_2020_csv.zip
  format: zip
  id: resource_ae38e71a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_women_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Macao - Macau: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/a822e0e9-275f-4c0e-b14f-5feae3de848c/resource/3b9126ac-ca8c-43c3-8a38-bc63d41493db/download/mac_women_2020_geotiff.zip
  format: zip
  id: resource_3b9126ac
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_women_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Macao - Macau: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/a822e0e9-275f-4c0e-b14f-5feae3de848c/resource/3a08f8f9-87f9-4223-ab91-29668e039aef/download/mac_women_of_reproductive_age_15_49_2020_csv.zip
  format: zip
  id: resource_3a08f8f9
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_women_of_reproductive_age_15_49_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Macao - Macau: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/a822e0e9-275f-4c0e-b14f-5feae3de848c/resource/417d9219-1e0a-44fa-9695-89855653953c/download/mac_women_of_reproductive_age_15_49_2020_geotiff.zip
  format: zip
  id: resource_417d9219
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_women_of_reproductive_age_15_49_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Macao - Macau: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/a822e0e9-275f-4c0e-b14f-5feae3de848c/resource/09b4c472-0fd4-4339-b0bc-5e259afda18e/download/mac_youth_15_24_2020_csv.zip
  format: zip
  id: resource_09b4c472
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_youth_15_24_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Macao - Macau: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/a822e0e9-275f-4c0e-b14f-5feae3de848c/resource/6136504d-52a5-428f-8b42-4b4490fca929/download/mac_youth_15_24_2020_geotiff.zip
  format: zip
  id: resource_6136504d
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_youth_15_24_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Macao - Macau: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/a822e0e9-275f-4c0e-b14f-5feae3de848c/resource/2c123801-2e21-4a4b-9136-b32e374a16c7/download/mac_general_2020_geotiff.zip
  format: zip
  id: resource_2c123801
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_general_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Macao - Macau: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/a822e0e9-275f-4c0e-b14f-5feae3de848c/resource/eba6e007-7603-4afb-89d2-951e53c35ca8/download/mac_general_2020_csv.zip
  format: zip
  id: resource_eba6e007
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_general_2020_csv.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-mac_metad4g_macauhighresolutionpopula_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - MAC
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-03-22'
  start: '2019-06-19'
temporal_resolution: null
title: 'Macao - Macau: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
