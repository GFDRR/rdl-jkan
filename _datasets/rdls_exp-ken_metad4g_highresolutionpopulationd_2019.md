---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook Data for Good
    url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-ken
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-ken
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-ken
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-ken
dataset_id: rdls_exp-ken_metad4g_highresolutionpopulationd_2019
description: 'V1.5 The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Kenya: (1) Overall population density
  (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly (ages
  60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-ken]'
details: "To reference this data, please use the following citation: Facebook Connectivity\
  \ Lab and Center for International Earth Science Information Network - CIESIN -\
  \ Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery\
  \ for HRSL \xC2\xA9 2016 DigitalGlobe. Accessed DAY MONTH YEAR.' Please note that\
  \ as of 2024, Meta's high resolution population density maps are no longer being\
  \ updated."
exposure:
- asset_type:
    description: High-resolution gridded population density maps for Kenya disaggregated
      by demographic groups (overall, women, men, children 0-5, youth 15-24, elderly
      60+, women of reproductive age 15-49)
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
    imagery, then overlaying population estimates derived from census data and other
    publicly available demographic statistics. The resulting gridded datasets represent
    population distribution at fine spatial resolution for Kenya in 2020, disaggregated
    into seven demographic categories.
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
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-ken
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
  description: 'Kenya: High Resolution Population Density Maps (ZIP archive)'
  download_url: https://data.humdata.org/dataset/2964b369-c10c-4b55-94a8-495de3fc9858/resource/1271b53b-30be-4c4b-aa27-1bd104506636/download/ken_general_2020_geotiff.zip
  format: null
  id: resource_1271b53b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ken_general_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kenya: High Resolution Population Density Maps (ZIP archive)'
  download_url: https://data.humdata.org/dataset/2964b369-c10c-4b55-94a8-495de3fc9858/resource/728e9fe2-0707-491f-91d8-3dc8379d7a32/download/ken_general_2020_csv.zip
  format: null
  id: resource_728e9fe2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ken_general_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kenya: High Resolution Population Density Maps (ZIP archive)'
  download_url: https://data.humdata.org/dataset/2964b369-c10c-4b55-94a8-495de3fc9858/resource/20769f96-dc26-4342-8900-135e2e1e9b71/download/ken_youth_15_24_2020_csv.zip
  format: null
  id: resource_20769f96
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ken_youth_15_24_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kenya: High Resolution Population Density Maps (ZIP archive)'
  download_url: https://data.humdata.org/dataset/2964b369-c10c-4b55-94a8-495de3fc9858/resource/1cdc95e0-3ce4-4515-b08e-e260ee96275a/download/ken_elderly_60_plus_2020_csv.zip
  format: null
  id: resource_1cdc95e0
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ken_elderly_60_plus_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kenya: High Resolution Population Density Maps (ZIP archive)'
  download_url: https://data.humdata.org/dataset/2964b369-c10c-4b55-94a8-495de3fc9858/resource/ef425edf-4b59-4487-8a8f-6fa6fe78b494/download/ken_women_2020_csv.zip
  format: null
  id: resource_ef425edf
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ken_women_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kenya: High Resolution Population Density Maps (ZIP archive)'
  download_url: https://data.humdata.org/dataset/2964b369-c10c-4b55-94a8-495de3fc9858/resource/c262d93d-588a-4ef3-8422-bc72cd2d829e/download/ken_men_2020_csv.zip
  format: null
  id: resource_c262d93d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ken_men_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kenya: High Resolution Population Density Maps (ZIP archive)'
  download_url: https://data.humdata.org/dataset/2964b369-c10c-4b55-94a8-495de3fc9858/resource/ce0f1108-f863-40f7-b817-a6c552154d90/download/ken_children_under_five_2020_csv.zip
  format: null
  id: resource_ce0f1108
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ken_children_under_five_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kenya: High Resolution Population Density Maps (ZIP archive)'
  download_url: https://data.humdata.org/dataset/2964b369-c10c-4b55-94a8-495de3fc9858/resource/09e8d2e4-8656-422c-8167-b0327990235d/download/ken_women_of_reproductive_age_15_49_2020_csv.zip
  format: null
  id: resource_09e8d2e4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ken_women_of_reproductive_age_15_49_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kenya: High Resolution Population Density Maps (ZIP archive)'
  download_url: https://data.humdata.org/dataset/2964b369-c10c-4b55-94a8-495de3fc9858/resource/ae1a0b07-2234-4afb-b8c7-1b9f7c345635/download/ken_women_of_reproductive_age_15_49_2020_geotiff.zip
  format: null
  id: resource_ae1a0b07
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ken_women_of_reproductive_age_15_49_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kenya: High Resolution Population Density Maps (ZIP archive)'
  download_url: https://data.humdata.org/dataset/2964b369-c10c-4b55-94a8-495de3fc9858/resource/16a0ecc2-a06e-429b-919f-995f380d031c/download/ken_elderly_60_plus_2020_geotiff.zip
  format: null
  id: resource_16a0ecc2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ken_elderly_60_plus_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kenya: High Resolution Population Density Maps (ZIP archive)'
  download_url: https://data.humdata.org/dataset/2964b369-c10c-4b55-94a8-495de3fc9858/resource/cd45eb53-40ea-4294-8c6e-dcbaf1ae458a/download/ken_children_under_five_2020_geotiff.zip
  format: null
  id: resource_cd45eb53
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ken_children_under_five_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kenya: High Resolution Population Density Maps (ZIP archive)'
  download_url: https://data.humdata.org/dataset/2964b369-c10c-4b55-94a8-495de3fc9858/resource/0cf4348d-4700-4dce-974c-e1a6acdd25a6/download/ken_women_2020_geotiff.zip
  format: null
  id: resource_0cf4348d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ken_women_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kenya: High Resolution Population Density Maps (ZIP archive)'
  download_url: https://data.humdata.org/dataset/2964b369-c10c-4b55-94a8-495de3fc9858/resource/f718685a-e4fb-4a38-aab8-3de1d9d9c05e/download/ken_youth_15_24_2020_geotiff.zip
  format: null
  id: resource_f718685a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ken_youth_15_24_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kenya: High Resolution Population Density Maps (ZIP archive)'
  download_url: https://data.humdata.org/dataset/2964b369-c10c-4b55-94a8-495de3fc9858/resource/091ca881-6478-40ce-8113-d13579c07c11/download/ken_men_2020_geotiff.zip
  format: null
  id: resource_091ca881
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ken_men_2020_geotiff.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-ken_metad4g_highresolutionpopulationd_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - KEN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2021-08-07'
  start: '2019-05-20'
temporal_resolution: null
title: 'Kenya: High Resolution Population Density Maps'
version: null
vulnerability: null
---
