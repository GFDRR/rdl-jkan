---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook/Meta AI and Data for Good
    url: https://data.humdata.org/dataset/nicaragua-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/nicaragua-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/nicaragua-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/nicaragua-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-nic_metad4g_highresolutionpopulationd_201906
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Nicaragua: (1) Overall population
  density (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly
  (ages 60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/nicaragua-high-resolution-population-density-maps-demographic-estimates]'
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
    satellite imagery across Nicaragua. Population estimates derived from publicly
    available census data were spatially distributed using these building locations
    and demographic modeling in partnership with Columbia University, producing high-resolution
    gridded population density maps for overall population and seven demographic subgroups.
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
- href: https://data.humdata.org/dataset/nicaragua-high-resolution-population-density-maps-demographic-estimates
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
  description: 'Nicaragua: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/ce1b170e-132c-431e-b338-c536ec0408d9/resource/40eac4b2-c2af-4a64-8b28-03b299ee4d5f/download/population_nic_2018-10-01.zip
  format: null
  id: resource_40eac4b2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_nic_2018-10-01.geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nicaragua: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/ce1b170e-132c-431e-b338-c536ec0408d9/resource/645c4d1a-c651-4903-9890-2e82e9cbd19e/download/population_nic_2018-10-01.csv.zip
  format: null
  id: resource_645c4d1a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_nic_2018-10-01.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nicaragua: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/ce1b170e-132c-431e-b338-c536ec0408d9/resource/8b9abc77-793c-4374-9565-58051c10c1a1/download/nic_children_under_five_2019-06-01_csv.zip
  format: null
  id: resource_8b9abc77
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NIC_children_under_five_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nicaragua: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/ce1b170e-132c-431e-b338-c536ec0408d9/resource/7d0f3710-59ee-46de-9512-a709b8d3da51/download/nic_children_under_five_2019-06-01_geotiff.zip
  format: null
  id: resource_7d0f3710
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NIC_children_under_five_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nicaragua: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/ce1b170e-132c-431e-b338-c536ec0408d9/resource/ed662aeb-a12a-445e-a3c9-e4eb9d8e7088/download/nic_elderly_60_plus_2019-06-01_csv.zip
  format: null
  id: resource_ed662aeb
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NIC_elderly_60_plus_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nicaragua: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/ce1b170e-132c-431e-b338-c536ec0408d9/resource/dea46a8e-d774-436f-a744-0602aa93097f/download/nic_elderly_60_plus_2019-06-01_geotiff.zip
  format: null
  id: resource_dea46a8e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NIC_elderly_60_plus_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nicaragua: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/ce1b170e-132c-431e-b338-c536ec0408d9/resource/ca94fdc6-a8cf-4e86-9335-80ed3ffebbeb/download/nic_men_2019-06-01_csv.zip
  format: null
  id: resource_ca94fdc6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NIC_men_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nicaragua: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/ce1b170e-132c-431e-b338-c536ec0408d9/resource/0b847291-defb-4097-83ff-2a38a3eb7d1f/download/nic_men_2019-06-01_geotiff.zip
  format: null
  id: resource_0b847291
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NIC_men_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nicaragua: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/ce1b170e-132c-431e-b338-c536ec0408d9/resource/a6c846f0-6246-4dad-bd1e-b16a8e917040/download/nic_women_2019-06-01_csv.zip
  format: null
  id: resource_a6c846f0
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NIC_women_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nicaragua: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/ce1b170e-132c-431e-b338-c536ec0408d9/resource/88de717f-2c3d-4253-afd5-f55773b69672/download/nic_women_2019-06-01_geotiff.zip
  format: null
  id: resource_88de717f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NIC_women_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nicaragua: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/ce1b170e-132c-431e-b338-c536ec0408d9/resource/b7ef0170-f82c-4662-80fb-e2cedb01d464/download/nic_women_of_reproductive_age_15_49_2019-06-01_csv.zip
  format: null
  id: resource_b7ef0170
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NIC_women_of_reproductive_age_15_49_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nicaragua: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/ce1b170e-132c-431e-b338-c536ec0408d9/resource/9f08c2c4-7d64-4a1b-a71b-566efac8d0a6/download/nic_women_of_reproductive_age_15_49_2019-06-01_geotiff.zip
  format: null
  id: resource_9f08c2c4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NIC_women_of_reproductive_age_15_49_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nicaragua: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/ce1b170e-132c-431e-b338-c536ec0408d9/resource/0cf178f1-0a7d-4f6c-9990-c8df1302f283/download/nic_youth_15_24_2019-06-01_csv.zip
  format: null
  id: resource_0cf178f1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NIC_youth_15_24_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nicaragua: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/ce1b170e-132c-431e-b338-c536ec0408d9/resource/9435a193-0b19-48e3-bd7c-aa622e05a778/download/nic_youth_15_24_2019-06-01_geotiff.zip
  format: null
  id: resource_9435a193
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NIC_youth_15_24_2019-06-01_geotiff.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-nic_metad4g_highresolutionpopulationd_201906
spatial:
  bbox: null
  centroid: null
  countries:
  - NIC
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2019-06-11'
  start: '2019-06-10'
temporal_resolution: null
title: 'Nicaragua: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
