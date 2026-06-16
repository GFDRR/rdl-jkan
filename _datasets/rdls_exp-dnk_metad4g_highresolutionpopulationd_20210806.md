---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook
    url: https://data.humdata.org/dataset/denmark-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/denmark-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/denmark-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/denmark-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-dnk_metad4g_highresolutionpopulationd_20210806
description: 'VERSION 1.5. The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Denmark: (1) Overall population density
  (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly (ages
  60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/denmark-high-resolution-population-density-maps-demographic-estimates]'
details: "Citation To reference this data, please use the following citation: Facebook\
  \ and Center for International Earth Science Information Network - CIESIN - Columbia\
  \ University. 2021. High Resolution Settlement Layer (HRSL). Source imagery for\
  \ HRSL \xC2\xA9 2021 Maxar. Accessed DAY MONTH YEAR. Acknowledgements CIESIN contributions\
  \ to the development of this work were supported by funding provided by Facebook.\
  \ Population estimates are based on data from the Gridded Population of the World\
  \ data collection. Imagery used to identify settlements is from the Maxar Basemap\
  \ +Vivid. Data for the surface model relies on digital surface model produced with\
  \ the data from the Panchromatic Remote-sensing Instrument for Stereo Mapping (PRISM)\
  \ on board the Advanced Land Observing Satellite (ALOS); additional house locations\
  \ come from OpenStreetMap"
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: High-resolution population density maps were created by applying machine
    learning algorithms to commercially available satellite imagery to identify building
    footprints, then overlaying general population estimates derived from census data
    and demographic statistics in partnership with Columbia University. The resulting
    gridded datasets provide spatial distribution of overall population and seven
    demographic subgroups at fine resolution across Denmark.
  sources:
  - id: source_1
    license: null
    name: Facebook
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
- href: https://data.humdata.org/dataset/denmark-high-resolution-population-density-maps-demographic-estimates
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
  description: 'Denmark: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/c846d97b-4363-469a-b66b-1ac2674913b0/resource/2fd09cc4-74f3-4f07-a89a-6572e3c2949c/download/dnk_men_2020_csv.zip
  format: null
  id: resource_2fd09cc4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dnk_men_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Denmark: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/c846d97b-4363-469a-b66b-1ac2674913b0/resource/a02bf5bb-e8ac-4387-8e95-cb7801b75feb/download/dnk_youth_15_24_2020_csv.zip
  format: null
  id: resource_a02bf5bb
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dnk_youth_15_24_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Denmark: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/c846d97b-4363-469a-b66b-1ac2674913b0/resource/3a889df5-0a5d-4b10-a84f-95ff55499ee6/download/dnk_elderly_60_plus_2020_csv.zip
  format: null
  id: resource_3a889df5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dnk_elderly_60_plus_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Denmark: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/c846d97b-4363-469a-b66b-1ac2674913b0/resource/4e4e7ad4-580c-42b9-88c8-1811d1b7c2a3/download/dnk_women_2020_csv.zip
  format: null
  id: resource_4e4e7ad4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dnk_women_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Denmark: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/c846d97b-4363-469a-b66b-1ac2674913b0/resource/8ba23dc4-c3e9-455e-8b36-8bfee59aee3d/download/dnk_children_under_five_2020_csv.zip
  format: null
  id: resource_8ba23dc4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dnk_children_under_five_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Denmark: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/c846d97b-4363-469a-b66b-1ac2674913b0/resource/bd381bea-efa6-4765-ab21-ab9cd0dca9d1/download/dnk_women_of_reproductive_age_15_49_2020_csv.zip
  format: null
  id: resource_bd381bea
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dnk_women_of_reproductive_age_15_49_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Denmark: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/c846d97b-4363-469a-b66b-1ac2674913b0/resource/cd2c4503-053a-4006-9d0f-efd985e2188f/download/dnk_general_2020_csv.zip
  format: null
  id: resource_cd2c4503
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dnk_general_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Denmark: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/c846d97b-4363-469a-b66b-1ac2674913b0/resource/6b8f1b74-8960-4342-9c0d-a5b0099a95da/download/dnk_general_2020_geotiff.zip
  format: null
  id: resource_6b8f1b74
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dnk_general_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Denmark: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/c846d97b-4363-469a-b66b-1ac2674913b0/resource/132b8afb-9d2c-4c8c-a4c3-86ab1ab550e1/download/dnk_men_2020_geotiff.zip
  format: null
  id: resource_132b8afb
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dnk_men_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Denmark: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/c846d97b-4363-469a-b66b-1ac2674913b0/resource/31da48f3-b1cd-4f67-a048-9241e4cd5d2d/download/dnk_women_of_reproductive_age_15_49_2020_geotiff.zip
  format: null
  id: resource_31da48f3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dnk_women_of_reproductive_age_15_49_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Denmark: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/c846d97b-4363-469a-b66b-1ac2674913b0/resource/c2212c33-4782-491b-915b-f250cc79c540/download/dnk_women_2020_geotiff.zip
  format: null
  id: resource_c2212c33
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dnk_women_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Denmark: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/c846d97b-4363-469a-b66b-1ac2674913b0/resource/809c744c-fc1e-4d24-a737-4df3bfa6d8d3/download/dnk_children_under_five_2020_geotiff.zip
  format: null
  id: resource_809c744c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dnk_children_under_five_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Denmark: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/c846d97b-4363-469a-b66b-1ac2674913b0/resource/6cd208b5-1c85-4844-abff-a3317336411e/download/dnk_youth_15_24_2020_geotiff.zip
  format: null
  id: resource_6cd208b5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dnk_youth_15_24_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Denmark: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/c846d97b-4363-469a-b66b-1ac2674913b0/resource/93f27890-3bdd-437e-8739-36406ebd0a11/download/dnk_elderly_60_plus_2020_geotiff.zip
  format: null
  id: resource_93f27890
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dnk_elderly_60_plus_2020_geotiff.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-dnk_metad4g_highresolutionpopulationd_20210806
spatial:
  bbox: null
  centroid: null
  countries:
  - DNK
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2021-08-06'
temporal_resolution: null
title: 'Denmark: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
