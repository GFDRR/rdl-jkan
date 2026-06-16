---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook Data for Good
    url: https://data.humdata.org/dataset/netherlands-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/netherlands-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/netherlands-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/netherlands-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-nld_metad4g_highresolutionpopulationd_2019
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in the Netherlands: (1) Overall population
  density (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly
  (ages 60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/netherlands-high-resolution-population-density-maps-demographic-estimates]'
details: "To reference this data, please use the following citation: Facebook Connectivity\
  \ Lab and Center for International Earth Science Information Network - CIESIN -\
  \ Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery\
  \ for HRSL \xC2\xA9 2016 DigitalGlobe. Accessed DAY MONTH YEAR.' Please note that\
  \ as of 2024, Meta's high resolution population density maps are no longer being\
  \ updated."
exposure:
- asset_type:
    description: High-resolution gridded population density for overall population
      and demographic segments (children 0-5, youth 15-24, elderly 60+, women, men,
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
    imagery, then overlaying general population estimates derived from census data
    and demographic statistics in partnership with Columbia University. The resulting
    gridded datasets represent spatial distribution of total population and demographic
    segments across the Netherlands.
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
- href: https://data.humdata.org/dataset/netherlands-high-resolution-population-density-maps-demographic-estimates
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
  description: 'Netherlands: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/f678db99-269d-4244-9db8-a85c8042a27e/resource/058cb979-c1c3-4fad-b85f-29c5e879548c/download/population_nld_2019-07-01_geotiff.zip
  format: null
  id: resource_058cb979
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_nld.geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Netherlands: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/f678db99-269d-4244-9db8-a85c8042a27e/resource/c110e93e-5d02-467c-bcdb-1b0cc0b37acb/download/population_nld_2019-07-01.csv.zip
  format: null
  id: resource_c110e93e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_nld.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Netherlands: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/f678db99-269d-4244-9db8-a85c8042a27e/resource/8f4c3185-5f45-4040-b8a1-24db0a6b0922/download/nld_children_under_five_geotiff.zip
  format: null
  id: resource_8f4c3185
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NLD_children_under_five_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Netherlands: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/f678db99-269d-4244-9db8-a85c8042a27e/resource/d96e976e-71f0-48e0-866f-1259a2559875/download/nld_elderly_60_plus_geotiff.zip
  format: null
  id: resource_d96e976e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NLD_elderly_60_plus_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Netherlands: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/f678db99-269d-4244-9db8-a85c8042a27e/resource/a0032606-540f-4c14-b73e-5a8da0195f4d/download/nld_men_geotiff.zip
  format: null
  id: resource_a0032606
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NLD_men_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Netherlands: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/f678db99-269d-4244-9db8-a85c8042a27e/resource/1bc42d5f-784c-4b41-af67-d89e91002c9d/download/nld_women_geotiff.zip
  format: null
  id: resource_1bc42d5f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NLD_women_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Netherlands: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/f678db99-269d-4244-9db8-a85c8042a27e/resource/4277756c-a057-4f07-af30-116a29f3a93a/download/nld_women_of_reproductive_age_15_49_geotiff.zip
  format: null
  id: resource_4277756c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NLD_women_of_reproductive_age_15_49_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Netherlands: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/f678db99-269d-4244-9db8-a85c8042a27e/resource/a58a9066-d329-4bb1-97fc-941988f77ff1/download/nld_youth_15_24_geotiff.zip
  format: null
  id: resource_a58a9066
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NLD_youth_15_24_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Netherlands: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/f678db99-269d-4244-9db8-a85c8042a27e/resource/6f90f793-bbc7-4fe3-94c1-981ef5e6effc/download/nld_children_under_five_2019-08-03_csv.zip
  format: null
  id: resource_6f90f793
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NLD_children_under_five.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Netherlands: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/f678db99-269d-4244-9db8-a85c8042a27e/resource/0e65c998-a582-4f96-b814-d90f414e573f/download/nld_elderly_60_plus_2019-08-03_csv.zip
  format: null
  id: resource_0e65c998
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NLD_elderly_60_plus.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Netherlands: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/f678db99-269d-4244-9db8-a85c8042a27e/resource/479e1055-a03c-4e95-9d3b-a04bfab0bf00/download/nld_men_2019-08-03_csv.zip
  format: null
  id: resource_479e1055
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NLD_men.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Netherlands: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/f678db99-269d-4244-9db8-a85c8042a27e/resource/a417c3a8-79b3-4e4e-a5db-d65899a4b28f/download/nld_women_2019-08-03_csv.zip
  format: null
  id: resource_a417c3a8
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NLD_women.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Netherlands: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/f678db99-269d-4244-9db8-a85c8042a27e/resource/6b1909c9-402a-4b03-b96a-6bdb0545dbb4/download/nld_women_of_reproductive_age_15_49_2019-08-03_csv.zip
  format: null
  id: resource_6b1909c9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NLD_women_of_reproductive_age_15_49.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Netherlands: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/f678db99-269d-4244-9db8-a85c8042a27e/resource/883b841f-cf9a-458d-8bd9-e33e40a60994/download/nld_youth_15_24_2019-08-03_csv.zip
  format: null
  id: resource_883b841f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NLD_youth_15_24.csv.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-nld_metad4g_highresolutionpopulationd_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - NLD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-03-05'
  start: '2019-09-19'
temporal_resolution: null
title: 'Netherlands: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
