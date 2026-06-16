---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook/Meta AI and Data for Good
    url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-myt
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-myt
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-myt
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-myt
dataset_id: rdls_exp-myt_metad4g_mayottehighresolutionpopu_2019
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Mayotte: (1) Overall population density
  (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly (ages
  60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-myt]'
details: "To reference this data, please use the following citation: Facebook Connectivity\
  \ Lab and Center for International Earth Science Information Network - CIESIN -\
  \ Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery\
  \ for HRSL \xC2\xA9 2016 DigitalGlobe. Accessed DAY MONTH YEAR.' Please note that\
  \ as of 2024, Meta's high resolution population density maps are no longer being\
  \ updated."
exposure:
- asset_type:
    description: High-resolution gridded population density for overall population
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
    learning algorithms to identify building footprints from commercial satellite
    imagery, then overlaying population estimates derived from census data and demographic
    statistics in partnership with Columbia University. The resulting gridded datasets
    provide spatial distribution of total population and demographic subgroups across
    Mayotte at fine resolution.
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
- href: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-myt
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
  description: This is the second version of this dataset, and was uploaded on March
    25, 2020. The first version (no longer available for download) was uploaded on
    May 19, 2019.
  download_url: https://data.humdata.org/dataset/3c1e01a8-17bd-4b22-96d2-3057eb54c1e6/resource/24a6ae66-fd63-49b5-86da-e329fd853901/download/population_myt_2019-07-01_geotiff.zip
  format: null
  id: resource_24a6ae66
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_myt.geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This is the second version of this dataset, and was uploaded on March
    25, 2020. The first version (no longer available for download) was uploaded on
    May 19, 2019.
  download_url: https://data.humdata.org/dataset/3c1e01a8-17bd-4b22-96d2-3057eb54c1e6/resource/39056a88-87c4-4eb8-a131-a0801c96a9a4/download/population_myt_2019-07-01.csv.zip
  format: null
  id: resource_39056a88
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_myt.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mayotte: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/3c1e01a8-17bd-4b22-96d2-3057eb54c1e6/resource/9a207e27-d619-4928-9340-ebf0284dc225/download/myt_children_under_five_csv.zip
  format: null
  id: resource_9a207e27
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MYT_children_under_five_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mayotte: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/3c1e01a8-17bd-4b22-96d2-3057eb54c1e6/resource/13c949b5-b004-421a-b11d-524a36d57a27/download/myt_children_under_five_geotiff.zip
  format: null
  id: resource_13c949b5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MYT_children_under_five_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mayotte: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/3c1e01a8-17bd-4b22-96d2-3057eb54c1e6/resource/ec7e9a88-35d9-4c87-b5bb-bb6ee1f33575/download/myt_elderly_60_plus_csv.zip
  format: null
  id: resource_ec7e9a88
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MYT_elderly_60_plus_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mayotte: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/3c1e01a8-17bd-4b22-96d2-3057eb54c1e6/resource/28bd1353-dba5-414c-8b3c-e81378b29e7e/download/myt_elderly_60_plus_geotiff.zip
  format: null
  id: resource_28bd1353
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MYT_elderly_60_plus_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mayotte: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/3c1e01a8-17bd-4b22-96d2-3057eb54c1e6/resource/c25f40a3-e505-4c6b-ab85-e94afe440585/download/myt_men_csv.zip
  format: null
  id: resource_c25f40a3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MYT_men_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mayotte: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/3c1e01a8-17bd-4b22-96d2-3057eb54c1e6/resource/3fd41292-b0c4-46da-a7f2-ef920d587d40/download/myt_men_geotiff.zip
  format: null
  id: resource_3fd41292
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MYT_men_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mayotte: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/3c1e01a8-17bd-4b22-96d2-3057eb54c1e6/resource/301d3ed8-7078-4c6e-9786-bcc97d0c070b/download/myt_women_csv.zip
  format: null
  id: resource_301d3ed8
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MYT_women_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mayotte: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/3c1e01a8-17bd-4b22-96d2-3057eb54c1e6/resource/9a8a561a-d8b0-436d-996f-c327298f3dd9/download/myt_women_geotiff.zip
  format: null
  id: resource_9a8a561a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MYT_women_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mayotte: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/3c1e01a8-17bd-4b22-96d2-3057eb54c1e6/resource/acb226c0-e7f0-443b-916c-e0cb0eb30889/download/myt_women_of_reproductive_age_15_49_csv.zip
  format: null
  id: resource_acb226c0
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MYT_women_of_reproductive_age_15_49_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mayotte: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/3c1e01a8-17bd-4b22-96d2-3057eb54c1e6/resource/781c61d3-5467-4abf-82c9-26199084fe08/download/myt_women_of_reproductive_age_15_49_geotiff.zip
  format: null
  id: resource_781c61d3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MYT_women_of_reproductive_age_15_49_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mayotte: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/3c1e01a8-17bd-4b22-96d2-3057eb54c1e6/resource/aae71c47-523e-46fd-9cbc-db2f4d129f8a/download/myt_youth_15_24_csv.zip
  format: null
  id: resource_aae71c47
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MYT_youth_15_24_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mayotte: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/3c1e01a8-17bd-4b22-96d2-3057eb54c1e6/resource/31fede3f-d018-4afc-9080-d853b9bf2317/download/myt_youth_15_24_geotiff.zip
  format: null
  id: resource_31fede3f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MYT_youth_15_24_geotiff.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-myt_metad4g_mayottehighresolutionpopu_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - MYT
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-03-28'
  start: '2019-05-20'
temporal_resolution: null
title: 'Mayotte: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
