---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook/Meta AI and Data for Good
    url: https://data.humdata.org/dataset/puerto-rico-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/puerto-rico-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/puerto-rico-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/puerto-rico-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-pri_metad4g_puertoricohighresolutionp_201906
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Puerto Rico: (1) Overall population
  density (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly
  (ages 60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/puerto-rico-high-resolution-population-density-maps-demographic-estimates]'
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
license: CC-BY-4.0
lineage:
  description: Machine learning algorithms identified building footprints from commercial
    satellite imagery across Puerto Rico. Population estimates derived from publicly
    available census data were spatially disaggregated to building-level resolution
    using demographic modeling in collaboration with Columbia University, producing
    seven demographic layers (total population and six age/sex subgroups) at high
    spatial resolution.
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
- href: https://data.humdata.org/dataset/puerto-rico-high-resolution-population-density-maps-demographic-estimates
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
  description: 'Puerto Rico: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/ea41b712-e41e-4e84-9f5c-ed342b800355/resource/b613b97e-0f62-41f3-af41-295bbc28f443/download/population_pri_2018-10-01.csv.zip
  format: null
  id: resource_b613b97e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_pri_2018-10-01.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Puerto Rico: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/ea41b712-e41e-4e84-9f5c-ed342b800355/resource/119f796e-b54a-4161-ad0c-053f6a27c5f6/download/population_pri_2018-10-01.zip
  format: null
  id: resource_119f796e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_pri_2018-10-01.geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Puerto Rico: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/ea41b712-e41e-4e84-9f5c-ed342b800355/resource/0d11d071-a254-4a8a-a5fe-160585909573/download/pri_children_under_five_2019-06-01_csv.zip
  format: null
  id: resource_0d11d071
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PRI_children_under_five_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Puerto Rico: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/ea41b712-e41e-4e84-9f5c-ed342b800355/resource/b56f6c6e-fe47-47dd-9104-53b5a3e16094/download/pri_children_under_five_2019-06-01_geotiff.zip
  format: null
  id: resource_b56f6c6e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PRI_children_under_five_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Puerto Rico: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/ea41b712-e41e-4e84-9f5c-ed342b800355/resource/5b3a9de6-3058-49e4-88c5-effaba3c2883/download/pri_elderly_60_plus_2019-06-01_csv.zip
  format: null
  id: resource_5b3a9de6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PRI_elderly_60_plus_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Puerto Rico: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/ea41b712-e41e-4e84-9f5c-ed342b800355/resource/4fc5eda8-ae32-4286-bc2d-2067e03be2b2/download/pri_elderly_60_plus_2019-06-01_geotiff.zip
  format: null
  id: resource_4fc5eda8
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PRI_elderly_60_plus_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Puerto Rico: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/ea41b712-e41e-4e84-9f5c-ed342b800355/resource/e6a1bdd7-6b9f-4408-8eb6-f8b244b956ff/download/pri_men_2019-06-01_csv.zip
  format: null
  id: resource_e6a1bdd7
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PRI_men_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Puerto Rico: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/ea41b712-e41e-4e84-9f5c-ed342b800355/resource/6f16e59b-7e89-4399-99a4-eb5e5ccd18da/download/pri_men_2019-06-01_geotiff.zip
  format: null
  id: resource_6f16e59b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PRI_men_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Puerto Rico: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/ea41b712-e41e-4e84-9f5c-ed342b800355/resource/c7edcbc1-4032-40ec-8809-3d8c15ed345e/download/pri_women_2019-06-01_csv.zip
  format: null
  id: resource_c7edcbc1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PRI_women_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Puerto Rico: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/ea41b712-e41e-4e84-9f5c-ed342b800355/resource/da44f53f-cea1-44d8-bdb7-4359e4355f68/download/pri_women_2019-06-01_geotiff.zip
  format: null
  id: resource_da44f53f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PRI_women_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Puerto Rico: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/ea41b712-e41e-4e84-9f5c-ed342b800355/resource/b40deb43-8d80-401e-8f90-37c095a9aa54/download/pri_women_of_reproductive_age_15_49_2019-06-01_csv.zip
  format: null
  id: resource_b40deb43
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PRI_women_of_reproductive_age_15_49_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Puerto Rico: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/ea41b712-e41e-4e84-9f5c-ed342b800355/resource/254e99da-a459-49d1-a37f-611115b6f84f/download/pri_women_of_reproductive_age_15_49_2019-06-01_geotiff.zip
  format: null
  id: resource_254e99da
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PRI_women_of_reproductive_age_15_49_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Puerto Rico: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/ea41b712-e41e-4e84-9f5c-ed342b800355/resource/c05f54d2-11f8-4101-a2ad-eecaf4f8d44c/download/pri_youth_15_24_2019-06-01_csv.zip
  format: null
  id: resource_c05f54d2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PRI_youth_15_24_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Puerto Rico: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/ea41b712-e41e-4e84-9f5c-ed342b800355/resource/cc6c8b94-d99e-4e3f-86ed-f7418357aa87/download/pri_youth_15_24_2019-06-01_geotiff.zip
  format: null
  id: resource_cc6c8b94
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PRI_youth_15_24_2019-06-01_geotiff.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-pri_metad4g_puertoricohighresolutionp_201906
spatial:
  bbox: null
  centroid: null
  countries:
  - PRI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2019-06-11'
  start: '2019-06-10'
temporal_resolution: null
title: 'Puerto Rico: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
