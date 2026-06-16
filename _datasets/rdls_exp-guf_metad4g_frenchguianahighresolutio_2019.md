---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook/Meta AI and Data for Good
    url: https://data.humdata.org/dataset/french-guiana-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/french-guiana-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/french-guiana-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/french-guiana-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-guf_metad4g_frenchguianahighresolutio_2019
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in French Guiana: (1) Overall population
  density (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly
  (ages 60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/french-guiana-high-resolution-population-density-maps-demographic-estimates]'
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
  description: High-resolution population density maps were created by applying machine
    learning algorithms to identify building footprints from commercial satellite
    imagery, then overlaying general population estimates derived from publicly available
    census data and demographic statistics. The resulting gridded datasets provide
    spatially explicit population distributions for seven demographic categories at
    fine spatial resolution across French Guiana.
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
- href: https://data.humdata.org/dataset/french-guiana-high-resolution-population-density-maps-demographic-estimates
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
  description: 'French Guiana: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/6030db92-b637-403b-8aa9-155655e7f8f0/resource/cd121160-fc65-4041-87de-b11bf85a8b14/download/guf_general_2020_csv.zip
  format: zip
  id: resource_cd121160
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_general_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'French Guiana: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/6030db92-b637-403b-8aa9-155655e7f8f0/resource/270b4447-ebee-4ead-a594-ba232f3acf4d/download/guf_general_2020_geotiff.zip
  format: zip
  id: resource_270b4447
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_general_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'French Guiana: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/6030db92-b637-403b-8aa9-155655e7f8f0/resource/3b53fa94-4dc9-4b11-90ca-354b8e481f30/download/guf_children_under_five_2020_csv.zip
  format: zip
  id: resource_3b53fa94
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_children_under_five_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'French Guiana: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/6030db92-b637-403b-8aa9-155655e7f8f0/resource/279cde29-7b00-4b8e-bf77-924a346bdfb8/download/guf_children_under_five_2020_geotiff.zip
  format: zip
  id: resource_279cde29
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_children_under_five_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'French Guiana: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/6030db92-b637-403b-8aa9-155655e7f8f0/resource/ba52e890-bee5-483c-83f4-aeb9173fb757/download/guf_elderly_60_plus_2020_csv.zip
  format: zip
  id: resource_ba52e890
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_elderly_60_plus_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'French Guiana: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/6030db92-b637-403b-8aa9-155655e7f8f0/resource/1b536723-cc52-41e1-8472-279212236680/download/guf_elderly_60_plus_2020_geotiff.zip
  format: zip
  id: resource_1b536723
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_elderly_60_plus_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'French Guiana: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/6030db92-b637-403b-8aa9-155655e7f8f0/resource/b1e47b37-edb0-4201-915b-8ab789e81837/download/guf_men_2020_csv.zip
  format: zip
  id: resource_b1e47b37
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_men_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'French Guiana: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/6030db92-b637-403b-8aa9-155655e7f8f0/resource/3fd48a97-91fa-4e23-8a35-f5fb29fa1bb2/download/guf_men_2020_geotiff.zip
  format: zip
  id: resource_3fd48a97
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_men_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'French Guiana: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/6030db92-b637-403b-8aa9-155655e7f8f0/resource/4ab273be-e53c-4b8c-a6b0-ce9717973619/download/guf_women_2020_csv.zip
  format: zip
  id: resource_4ab273be
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_women_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'French Guiana: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/6030db92-b637-403b-8aa9-155655e7f8f0/resource/c88bface-9279-4578-8514-1a193f567518/download/guf_women_2020_geotiff.zip
  format: zip
  id: resource_c88bface
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_women_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'French Guiana: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/6030db92-b637-403b-8aa9-155655e7f8f0/resource/eb4e4f00-9830-4f14-9641-4c623a448c11/download/guf_women_of_reproductive_age_15_49_2020_csv.zip
  format: zip
  id: resource_eb4e4f00
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_women_of_reproductive_age_15_49_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'French Guiana: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/6030db92-b637-403b-8aa9-155655e7f8f0/resource/78e66194-7304-4abc-b269-41f16787c78d/download/guf_women_of_reproductive_age_15_49_2020_geotiff.zip
  format: zip
  id: resource_78e66194
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_women_of_reproductive_age_15_49_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'French Guiana: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/6030db92-b637-403b-8aa9-155655e7f8f0/resource/19f32c42-f546-4ac0-ac19-2b27f5084e24/download/guf_youth_15_24_2020_csv.zip
  format: zip
  id: resource_19f32c42
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_youth_15_24_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'French Guiana: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/6030db92-b637-403b-8aa9-155655e7f8f0/resource/1725f549-d48e-4f20-b943-e2a514a681dd/download/guf_youth_15_24_2020_geotiff.zip
  format: zip
  id: resource_1725f549
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_youth_15_24_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This file has information about the cloud cover percentage and capture
    data of the satellite images used.
  download_url: https://data.humdata.org/dataset/6030db92-b637-403b-8aa9-155655e7f8f0/resource/bdcc316b-ad72-41a9-bd8c-8d05f131afb7/download/guf_dg_metadata.json.zip
  format: null
  id: resource_bdcc316b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_dg_metadata.json.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-guf_metad4g_frenchguianahighresolutio_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - GUF
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2022-09-01'
  start: '2019-06-10'
temporal_resolution: null
title: 'French Guiana: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
