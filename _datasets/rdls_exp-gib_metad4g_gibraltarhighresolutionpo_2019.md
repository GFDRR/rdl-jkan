---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook Data for Good
    url: https://data.humdata.org/dataset/gibraltar-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/gibraltar-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/gibraltar-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/gibraltar-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-gib_metad4g_gibraltarhighresolutionpo_2019
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Gibraltar: (1) Overall population
  density (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly
  (ages 60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/gibraltar-high-resolution-population-density-maps-demographic-estimates]'
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
    imagery, then overlaying general population estimates derived from publicly available
    census data and population statistics in collaboration with Columbia University.
    The resulting gridded datasets provide spatial distribution of overall population
    and seven demographic subgroups at fine resolution for Gibraltar.
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
- href: https://data.humdata.org/dataset/gibraltar-high-resolution-population-density-maps-demographic-estimates
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
  description: 'Gibraltar: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/2a4c0fa8-55f0-470d-8a1c-3ee2d355040e/resource/471dc72c-9632-4710-b7ed-7cc1975da37c/download/gib_children_under_five_2020_geotiff.zip
  format: null
  id: resource_471dc72c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gib_children_under_five_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Gibraltar: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/2a4c0fa8-55f0-470d-8a1c-3ee2d355040e/resource/5a47f16d-8a01-4439-ad9c-909c3a998412/download/gib_elderly_60_plus_2020_geotiff.zip
  format: null
  id: resource_5a47f16d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gib_elderly_60_plus_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Gibraltar: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/2a4c0fa8-55f0-470d-8a1c-3ee2d355040e/resource/6d4494b6-3f42-4cf3-809c-f78fcc6ef59f/download/gib_men_2020_geotiff.zip
  format: null
  id: resource_6d4494b6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gib_men_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Gibraltar: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/2a4c0fa8-55f0-470d-8a1c-3ee2d355040e/resource/2b4dd653-34c8-4651-a7bd-9236d229de1f/download/gib_women_2020_geotiff.zip
  format: null
  id: resource_2b4dd653
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gib_women_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Gibraltar: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/2a4c0fa8-55f0-470d-8a1c-3ee2d355040e/resource/1080d7e1-b197-4c27-b502-b4cbd21ee925/download/gib_women_of_reproductive_age_15_49_2020_geotiff.zip
  format: null
  id: resource_1080d7e1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gib_women_of_reproductive_age_15_49_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Gibraltar: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/2a4c0fa8-55f0-470d-8a1c-3ee2d355040e/resource/48f70940-8e08-43db-8350-8af386658948/download/gib_youth_15_24_2020_geotiff.zip
  format: null
  id: resource_48f70940
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gib_youth_15_24_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Gibraltar: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/2a4c0fa8-55f0-470d-8a1c-3ee2d355040e/resource/97a9da10-a61c-453d-8bfa-c9dd0fa06440/download/gib_children_under_five_2020_csv.zip
  format: null
  id: resource_97a9da10
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gib_children_under_five_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Gibraltar: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/2a4c0fa8-55f0-470d-8a1c-3ee2d355040e/resource/a51e94f4-9d21-44c6-a88b-267179f7a8b8/download/gib_elderly_60_plus_2020_csv.zip
  format: null
  id: resource_a51e94f4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gib_elderly_60_plus_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Gibraltar: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/2a4c0fa8-55f0-470d-8a1c-3ee2d355040e/resource/2f54bd29-0c5d-48dc-a6e0-38ecf832041d/download/gib_men_2020_csv.zip
  format: null
  id: resource_2f54bd29
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gib_men_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Gibraltar: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/2a4c0fa8-55f0-470d-8a1c-3ee2d355040e/resource/cefc0970-3838-4bce-a2bd-a314e5fbfb11/download/gib_women_2020_csv.zip
  format: null
  id: resource_cefc0970
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gib_women_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Gibraltar: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/2a4c0fa8-55f0-470d-8a1c-3ee2d355040e/resource/0b8ba02a-eb42-43d2-8530-8f4af7ac6a9b/download/gib_women_of_reproductive_age_15_49_2020_csv.zip
  format: null
  id: resource_0b8ba02a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gib_women_of_reproductive_age_15_49_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Gibraltar: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/2a4c0fa8-55f0-470d-8a1c-3ee2d355040e/resource/0a496dcd-7bd9-493b-9d57-a8206feb209d/download/gib_youth_15_24_2020_csv.zip
  format: null
  id: resource_0a496dcd
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gib_youth_15_24_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This file has information about the cloud cover percentage and capture
    data of the satellite images used.
  download_url: https://data.humdata.org/dataset/2a4c0fa8-55f0-470d-8a1c-3ee2d355040e/resource/ec8a2976-c1bc-445b-b675-c68e5c1a8d4f/download/gib_dg_metadata.json.zip
  format: null
  id: resource_ec8a2976
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gib_dg_metadata.json.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-gib_metad4g_gibraltarhighresolutionpo_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - GIB
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2021-05-11'
  start: '2019-09-19'
temporal_resolution: null
title: 'Gibraltar: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
