---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook/Meta AI and Data for Good
    url: https://data.humdata.org/dataset/north-macedonia-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/north-macedonia-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/north-macedonia-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/north-macedonia-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-mkd_metad4g_highresolutionpopulationd_2019
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Macedonia: (1) Overall population
  density (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly
  (ages 60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/north-macedonia-high-resolution-population-density-maps-demographic-estimates]'
details: "To reference this data, please use the following citation: Facebook Connectivity\
  \ Lab and Center for International Earth Science Information Network - CIESIN -\
  \ Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery\
  \ for HRSL \xC2\xA9 2016 DigitalGlobe. Accessed DAY MONTH YEAR.' Please note that\
  \ as of 2024, Meta's high resolution population density maps are no longer being\
  \ updated."
exposure:
- asset_type:
    description: High-resolution gridded population density estimates for overall
      population and demographic subgroups (children 0-5, youth 15-24, elderly 60+,
      women, men, women of reproductive age 15-49)
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
    North Macedonia at fine spatial resolution.
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
- href: https://data.humdata.org/dataset/north-macedonia-high-resolution-population-density-maps-demographic-estimates
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
  description: 'North Macedonia: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/18d6003b-8cef-4962-a423-0c47cc83090c/resource/ddc7a805-94b0-45fb-8439-6c9144f4219e/download/population_mkd_2019-07-01_geotiff.zip
  format: null
  id: resource_ddc7a805
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_mkd.geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'North Macedonia: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/18d6003b-8cef-4962-a423-0c47cc83090c/resource/55c1b7c8-3821-43f2-8695-fb4bb1a439d3/download/mkd_children_under_five_geotiff.zip
  format: null
  id: resource_55c1b7c8
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MKD_children_under_five_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'North Macedonia: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/18d6003b-8cef-4962-a423-0c47cc83090c/resource/25eeb7eb-af53-4b59-8a10-393cbaf23603/download/population_mkd_2019-07-01.csv.zip
  format: null
  id: resource_25eeb7eb
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_mkd.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'North Macedonia: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/18d6003b-8cef-4962-a423-0c47cc83090c/resource/26b89714-4599-49cd-9e05-7e5365fbd4c0/download/mkd_elderly_60_plus_geotiff.zip
  format: null
  id: resource_26b89714
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MKD_elderly_60_plus_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'North Macedonia: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/18d6003b-8cef-4962-a423-0c47cc83090c/resource/afdb1461-d957-4c21-a8c9-e22aa11b9828/download/mkd_men_geotiff.zip
  format: null
  id: resource_afdb1461
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MKD_men_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'North Macedonia: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/18d6003b-8cef-4962-a423-0c47cc83090c/resource/e435fbb0-d36e-4363-88b9-d1d6ced7d1cb/download/mkd_women_geotiff.zip
  format: null
  id: resource_e435fbb0
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MKD_women_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'North Macedonia: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/18d6003b-8cef-4962-a423-0c47cc83090c/resource/19102979-6a9b-4110-aa75-d4518a69981a/download/mkd_women_of_reproductive_age_15_49_geotiff.zip
  format: null
  id: resource_19102979
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MKD_women_of_reproductive_age_15_49_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'North Macedonia: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/18d6003b-8cef-4962-a423-0c47cc83090c/resource/4479035b-f6f1-412b-abbb-dfdc10c13d76/download/mkd_youth_15_24_geotiff.zip
  format: null
  id: resource_4479035b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MKD_youth_15_24_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'North Macedonia: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/18d6003b-8cef-4962-a423-0c47cc83090c/resource/9187ed56-0528-4f4c-971d-e6a189b6789e/download/mkd_children_under_five_2020-02-01_csv.zip
  format: null
  id: resource_9187ed56
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MKD_children_under_five.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'North Macedonia: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/18d6003b-8cef-4962-a423-0c47cc83090c/resource/87a1330d-2bd1-4df5-9dfc-289ecab31e8d/download/mkd_elderly_60_plus_2020-02-01_csv.zip
  format: null
  id: resource_87a1330d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MKD_elderly_60_plus.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'North Macedonia: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/18d6003b-8cef-4962-a423-0c47cc83090c/resource/9e5c9b08-6d3c-4e2d-96a1-a5b33fd06a42/download/mkd_men_2020-02-01_csv.zip
  format: null
  id: resource_9e5c9b08
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MKD_men.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'North Macedonia: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/18d6003b-8cef-4962-a423-0c47cc83090c/resource/13de9017-903f-4e68-88a4-0e0b4c216c03/download/mkd_women_2020-02-01_csv.zip
  format: null
  id: resource_13de9017
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MKD_women.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'North Macedonia: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/18d6003b-8cef-4962-a423-0c47cc83090c/resource/dc1c038f-41cb-4e25-80ab-c896bc65c830/download/mkd_women_of_reproductive_age_15_49_2020-02-01_csv.zip
  format: null
  id: resource_dc1c038f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MKD_women_of_reproductive_age_15_49.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'North Macedonia: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/18d6003b-8cef-4962-a423-0c47cc83090c/resource/f83e8c7c-6947-41ee-abc6-cd1a960c4b8b/download/mkd_youth_15_24_2020-02-01_csv.zip
  format: null
  id: resource_f83e8c7c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MKD_youth_15_24.csv.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-mkd_metad4g_highresolutionpopulationd_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - MKD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-03-04'
  start: '2019-09-19'
temporal_resolution: null
title: 'North Macedonia: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
