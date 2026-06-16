---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook/AI and Data for Good at Meta
    url: https://data.humdata.org/dataset/honduras-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/honduras-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/honduras-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/honduras-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-hnd_metad4g_highresolutionpopulationd_201906
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Honduras: (1) Overall population
  density (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly
  (ages 60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/honduras-high-resolution-population-density-maps-demographic-estimates]'
details: "To reference this data, please use the following citation: Facebook Connectivity\
  \ Lab and Center for International Earth Science Information Network - CIESIN -\
  \ Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery\
  \ for HRSL \xC2\xA9 2016 DigitalGlobe. Accessed DAY MONTH YEAR.' Please note that\
  \ as of 2024, Meta's high resolution population density maps are no longer being\
  \ updated."
exposure:
- asset_type:
    description: High-resolution gridded population density estimates for Honduras
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
license: CC-BY-4.0
lineage:
  description: High-resolution population density maps were created by applying machine
    learning algorithms to identify building footprints from commercial satellite
    imagery, then overlaying general population estimates derived from publicly available
    census data and demographic statistics. The resulting gridded datasets provide
    spatially explicit population distributions disaggregated by demographic groups
    at national scale for Honduras.
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
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/honduras-high-resolution-population-density-maps-demographic-estimates
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
  description: 'Honduras: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/12004697-1c31-487b-a49f-b96e8fd646c9/resource/6891777f-efe9-4f42-ae78-57fd7078fb22/download/population_hnd_2018-10-01.csv.zip
  format: null
  id: resource_6891777f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_hnd_2018-10-01.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Honduras: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/12004697-1c31-487b-a49f-b96e8fd646c9/resource/682d5372-d5eb-4175-9e54-b1dbf5834314/download/population_hnd_2018-10-01.zip
  format: null
  id: resource_682d5372
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_hnd_2018-10-01.geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Honduras: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/12004697-1c31-487b-a49f-b96e8fd646c9/resource/f03190c2-4fdd-4883-9485-010c4e6c40b2/download/hnd_children_under_five_2019-06-01_csv.zip
  format: null
  id: resource_f03190c2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: HND_children_under_five_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Honduras: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/12004697-1c31-487b-a49f-b96e8fd646c9/resource/c9988701-2741-425c-a9f8-aa87bed71eee/download/hnd_children_under_five_2019-06-01_geotiff.zip
  format: null
  id: resource_c9988701
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: HND_children_under_five_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Honduras: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/12004697-1c31-487b-a49f-b96e8fd646c9/resource/cec9e04a-cd02-4b7f-9745-2460312dc291/download/hnd_elderly_60_plus_2019-06-01_csv.zip
  format: null
  id: resource_cec9e04a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: HND_elderly_60_plus_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Honduras: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/12004697-1c31-487b-a49f-b96e8fd646c9/resource/811a32b6-de57-4c25-ab4e-c17d581e1057/download/hnd_elderly_60_plus_2019-06-01_geotiff.zip
  format: null
  id: resource_811a32b6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: HND_elderly_60_plus_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Honduras: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/12004697-1c31-487b-a49f-b96e8fd646c9/resource/f1ae015b-3612-447f-92d5-e743c16082a2/download/hnd_men_2019-06-01_csv.zip
  format: null
  id: resource_f1ae015b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: HND_men_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Honduras: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/12004697-1c31-487b-a49f-b96e8fd646c9/resource/f7932841-abd7-4595-8cc8-b69d9bf9d8e4/download/hnd_men_2019-06-01_geotiff.zip
  format: null
  id: resource_f7932841
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: HND_men_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Honduras: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/12004697-1c31-487b-a49f-b96e8fd646c9/resource/869728c2-37aa-4d6b-910a-25b32267eea0/download/hnd_women_2019-06-01_csv.zip
  format: null
  id: resource_869728c2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: HND_women_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Honduras: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/12004697-1c31-487b-a49f-b96e8fd646c9/resource/d4255592-c8ca-44f9-89d1-2c568fc6d365/download/hnd_women_2019-06-01_geotiff.zip
  format: null
  id: resource_d4255592
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: HND_women_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Honduras: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/12004697-1c31-487b-a49f-b96e8fd646c9/resource/21f23691-cc9d-4800-bba7-4f8e2badb7fc/download/hnd_women_of_reproductive_age_15_49_2019-06-01_csv.zip
  format: null
  id: resource_21f23691
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: HND_women_of_reproductive_age_15_49_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Honduras: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/12004697-1c31-487b-a49f-b96e8fd646c9/resource/2861411a-87f8-4adc-ab99-179f647edd2d/download/hnd_women_of_reproductive_age_15_49_2019-06-01_geotiff.zip
  format: null
  id: resource_2861411a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: HND_women_of_reproductive_age_15_49_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Honduras: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/12004697-1c31-487b-a49f-b96e8fd646c9/resource/4049a651-56d2-42d8-ae40-a0203522203a/download/hnd_youth_15_24_2019-06-01_csv.zip
  format: null
  id: resource_4049a651
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: HND_youth_15_24_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Honduras: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/12004697-1c31-487b-a49f-b96e8fd646c9/resource/b3815756-b287-4d41-acdf-628932004cb8/download/hnd_youth_15_24_2019-06-01_geotiff.zip
  format: null
  id: resource_b3815756
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: HND_youth_15_24_2019-06-01_geotiff.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-hnd_metad4g_highresolutionpopulationd_201906
spatial:
  bbox: null
  centroid: null
  countries:
  - HND
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2019-06-11'
  start: '2019-06-10'
temporal_resolution: null
title: 'Honduras: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
