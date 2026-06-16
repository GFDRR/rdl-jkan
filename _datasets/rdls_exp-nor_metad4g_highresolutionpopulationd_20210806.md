---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook (Meta)
    url: https://data.humdata.org/dataset/norway-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/norway-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/norway-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/norway-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-nor_metad4g_highresolutionpopulationd_20210806
description: 'VERSION 1.5. The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Norway: (1) Overall population density
  (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly (ages
  60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/norway-high-resolution-population-density-maps-demographic-estimates]'
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
  \ come from OpenStreetMap Please note that as of 2024, Meta's high resolution population\
  \ density maps are no longer being updated."
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: High-resolution population density maps were created by applying machine
    learning algorithms to commercially available satellite imagery to identify building
    footprints, then overlaying general population estimates derived from publicly
    available census data and demographic statistics in partnership with Columbia
    University. The resulting gridded datasets provide spatial distribution of total
    population and seven demographic subgroups at fine resolution across Norway.
  sources:
  - id: source_1
    license: null
    name: Facebook (Meta)
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
- href: https://data.humdata.org/dataset/norway-high-resolution-population-density-maps-demographic-estimates
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
  description: 'Norway: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/1c1a90c0-17ee-4ee7-bb30-aeca9bd92f51/resource/3bc0d743-edf6-42aa-a699-177569e29270/download/nor_children_under_five_2020_csv.zip
  format: null
  id: resource_3bc0d743
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nor_children_under_five_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Norway: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/1c1a90c0-17ee-4ee7-bb30-aeca9bd92f51/resource/b38c8908-7684-4fa3-933c-4950481891b3/download/nor_women_of_reproductive_age_15_49_2020_csv.zip
  format: null
  id: resource_b38c8908
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nor_women_of_reproductive_age_15_49_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Norway: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/1c1a90c0-17ee-4ee7-bb30-aeca9bd92f51/resource/03cbb189-c0ad-47d5-ae52-365313531b97/download/nor_women_2020_csv.zip
  format: null
  id: resource_03cbb189
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nor_women_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Norway: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/1c1a90c0-17ee-4ee7-bb30-aeca9bd92f51/resource/057f3486-9f0b-430a-a33b-f1850d7db67b/download/nor_men_2020_csv.zip
  format: null
  id: resource_057f3486
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nor_men_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Norway: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/1c1a90c0-17ee-4ee7-bb30-aeca9bd92f51/resource/ca64f990-b3ed-4043-a4b4-8067363750d0/download/nor_youth_15_24_2020_csv.zip
  format: null
  id: resource_ca64f990
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nor_youth_15_24_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Norway: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/1c1a90c0-17ee-4ee7-bb30-aeca9bd92f51/resource/8d05f760-a08c-4fac-a1bf-6c973069dc16/download/nor_general_2020_csv.zip
  format: null
  id: resource_8d05f760
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nor_general_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Norway: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/1c1a90c0-17ee-4ee7-bb30-aeca9bd92f51/resource/0fde0909-67a2-4f66-8e6d-9cd4e56813be/download/nor_elderly_60_plus_2020_csv.zip
  format: null
  id: resource_0fde0909
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nor_elderly_60_plus_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Norway: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/1c1a90c0-17ee-4ee7-bb30-aeca9bd92f51/resource/65ef3c3b-0735-4c09-a9d3-3b8c3ba55c03/download/nor_general_2020_geotiff.zip
  format: null
  id: resource_65ef3c3b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nor_general_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Norway: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/1c1a90c0-17ee-4ee7-bb30-aeca9bd92f51/resource/fe37ae0b-486c-481f-8d08-1b989c05fe30/download/nor_men_2020_geotiff.zip
  format: null
  id: resource_fe37ae0b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nor_men_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Norway: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/1c1a90c0-17ee-4ee7-bb30-aeca9bd92f51/resource/b830fbe3-8cc2-4fbb-b142-21e8858e2791/download/nor_women_of_reproductive_age_15_49_2020_geotiff.zip
  format: null
  id: resource_b830fbe3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nor_women_of_reproductive_age_15_49_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Norway: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/1c1a90c0-17ee-4ee7-bb30-aeca9bd92f51/resource/69c9c131-6d8d-4df3-9464-34b7a00237e4/download/nor_women_2020_geotiff.zip
  format: null
  id: resource_69c9c131
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nor_women_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Norway: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/1c1a90c0-17ee-4ee7-bb30-aeca9bd92f51/resource/8a72f77f-628b-4454-a038-9a1554bffb32/download/nor_children_under_five_2020_geotiff.zip
  format: null
  id: resource_8a72f77f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nor_children_under_five_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Norway: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/1c1a90c0-17ee-4ee7-bb30-aeca9bd92f51/resource/af378fd2-7941-478b-881a-60daf62b5081/download/nor_youth_15_24_2020_geotiff.zip
  format: null
  id: resource_af378fd2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nor_youth_15_24_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Norway: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/1c1a90c0-17ee-4ee7-bb30-aeca9bd92f51/resource/8e8296f6-a8c9-4be2-8624-5f50eac14405/download/nor_elderly_60_plus_2020_geotiff.zip
  format: null
  id: resource_8e8296f6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nor_elderly_60_plus_2020_geotiff.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-nor_metad4g_highresolutionpopulationd_20210806
spatial:
  bbox: null
  centroid: null
  countries:
  - NOR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2021-08-06'
temporal_resolution: null
title: 'Norway: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
