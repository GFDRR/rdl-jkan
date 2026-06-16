---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook/Meta AI and Data for Good
    url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-stp
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-stp
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-stp
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-stp
dataset_id: rdls_exp-stp_metad4g_saotomeprincipehighresolu_2019
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Sao Tome and Principe: (1) Overall
  population density (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24)
  (6) Elderly (ages 60+) (7) Women of reproductive age (ages 15-49).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-stp]'
details: "To reference this data, please use the following citation: Facebook Connectivity\
  \ Lab and Center for International Earth Science Information Network - CIESIN -\
  \ Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery\
  \ for HRSL \xC2\xA9 2016 DigitalGlobe. Accessed DAY MONTH YEAR.' Please note that\
  \ as of 2024, Meta's high resolution population density maps are no longer being\
  \ updated."
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: High-resolution population density maps were created by applying machine
    learning algorithms to identify building footprints from commercial satellite
    imagery, then overlaying publicly available census data and population statistics
    in partnership with Columbia University to distribute demographic estimates spatially
    across Sao Tome and Principe.
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
    type: model
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-stp
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
  download_url: https://data.humdata.org/dataset/f278f368-99a7-4dd1-a807-8d3655d9e2cc/resource/ce3f5db9-c3fe-49e9-b6cc-9ddf7fd3afda/download/population_stp_2019-07-01_geotiff.zip
  format: null
  id: resource_ce3f5db9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_stp.geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This is the second version of this dataset, and was uploaded on March
    25, 2020. The first version (no longer available for download) was uploaded on
    May 19, 2019.
  download_url: https://data.humdata.org/dataset/f278f368-99a7-4dd1-a807-8d3655d9e2cc/resource/cc7d26dc-ced5-4d2a-8c18-e29f41cc8f49/download/population_stp_2019-07-01.csv.zip
  format: null
  id: resource_cc7d26dc
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_stp.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sao Tome and Principe: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/f278f368-99a7-4dd1-a807-8d3655d9e2cc/resource/a1f6c763-7ab8-4fa9-b597-1a56a702f776/download/stp_children_under_five_csv.zip
  format: null
  id: resource_a1f6c763
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: STP_children_under_five_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sao Tome and Principe: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/f278f368-99a7-4dd1-a807-8d3655d9e2cc/resource/c33be124-8e46-4352-adf6-cc55e777b4d3/download/stp_children_under_five_geotiff.zip
  format: null
  id: resource_c33be124
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: STP_children_under_five_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sao Tome and Principe: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/f278f368-99a7-4dd1-a807-8d3655d9e2cc/resource/00d688fd-eaf8-45e6-9adb-cbb806880c37/download/stp_elderly_60_plus_csv.zip
  format: null
  id: resource_00d688fd
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: STP_elderly_60_plus_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sao Tome and Principe: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/f278f368-99a7-4dd1-a807-8d3655d9e2cc/resource/45361af9-860e-4706-8da7-9d5dbdd14f3f/download/stp_elderly_60_plus_geotiff.zip
  format: null
  id: resource_45361af9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: STP_elderly_60_plus_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sao Tome and Principe: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/f278f368-99a7-4dd1-a807-8d3655d9e2cc/resource/4c815006-773a-4c87-8907-cd50cb55d284/download/stp_men_csv.zip
  format: null
  id: resource_4c815006
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: STP_men_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sao Tome and Principe: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/f278f368-99a7-4dd1-a807-8d3655d9e2cc/resource/410cbf40-e04d-4297-8abc-fd012b685eff/download/stp_men_geotiff.zip
  format: null
  id: resource_410cbf40
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: STP_men_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sao Tome and Principe: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/f278f368-99a7-4dd1-a807-8d3655d9e2cc/resource/8a5bb60f-68ce-4f93-a7a8-d253f379b1f9/download/stp_women_csv.zip
  format: null
  id: resource_8a5bb60f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: STP_women_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sao Tome and Principe: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/f278f368-99a7-4dd1-a807-8d3655d9e2cc/resource/f56a287b-f8bb-4592-9763-3d3e002a20d2/download/stp_women_geotiff.zip
  format: null
  id: resource_f56a287b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: STP_women_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sao Tome and Principe: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/f278f368-99a7-4dd1-a807-8d3655d9e2cc/resource/59d9a097-f2a9-41c5-9188-aae9060a8026/download/stp_women_of_reproductive_age_15_49_csv.zip
  format: null
  id: resource_59d9a097
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: STP_women_of_reproductive_age_15_49_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sao Tome and Principe: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/f278f368-99a7-4dd1-a807-8d3655d9e2cc/resource/eba58890-83e1-4f21-a63d-37df20b5432e/download/stp_women_of_reproductive_age_15_49_geotiff.zip
  format: null
  id: resource_eba58890
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: STP_women_of_reproductive_age_15_49_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sao Tome and Principe: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/f278f368-99a7-4dd1-a807-8d3655d9e2cc/resource/24d7f6a2-bb28-4f68-962b-97c25834ebf0/download/stp_youth_15_24_csv.zip
  format: null
  id: resource_24d7f6a2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: STP_youth_15_24_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sao Tome and Principe: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/f278f368-99a7-4dd1-a807-8d3655d9e2cc/resource/5912e9c0-c42d-4f13-83cc-50da0c0f11bb/download/stp_youth_15_24_geotiff.zip
  format: null
  id: resource_5912e9c0
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: STP_youth_15_24_geotiff.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-stp_metad4g_saotomeprincipehighresolu_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - STP
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-03-28'
  start: '2019-05-20'
temporal_resolution: null
title: 'Sao Tome and Principe: High Resolution Population Density Maps + Demographic
  Estimates'
version: null
vulnerability: null
---
