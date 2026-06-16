---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook Data for Good
    url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-moz
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-moz
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-moz
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-moz
dataset_id: rdls_exp-moz_metad4g_highresolutionpopulationd_2019
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Mozambique: (1) Overall population
  density (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly
  (ages 60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-moz]'
details: "To reference this data, please use the following citation: Facebook Connectivity\
  \ Lab and Center for International Earth Science Information Network - CIESIN -\
  \ Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery\
  \ for HRSL \xC2\xA9 2016 DigitalGlobe. Accessed DAY MONTH YEAR.' Please note that\
  \ as of 2024, Meta's high resolution population density maps are no longer being\
  \ updated."
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
license: CC-BY-4.0
lineage:
  description: Machine learning algorithms identified building footprints from commercial
    satellite imagery across Mozambique. Population estimates derived from publicly
    available census data and demographic statistics were then spatially allocated
    to buildings using Columbia University's methodology, generating seven high-resolution
    gridded population density maps for 2020 disaggregated by demographic groups.
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
    type: model
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-moz
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
  description: 'Mozambique: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/fa47f9e0-ee19-4081-b325-f4672cada57d/resource/8debf6d1-970f-4c05-b075-e256e52b14b9/download/moz_general_2020_geotiff.zip
  format: zip
  id: resource_8debf6d1
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: moz_general_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mozambique: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/fa47f9e0-ee19-4081-b325-f4672cada57d/resource/b82f3bc2-a379-4230-a2e3-442a35b23ca7/download/moz_general_2020_csv.zip
  format: zip
  id: resource_b82f3bc2
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: moz_general_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mozambique: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/fa47f9e0-ee19-4081-b325-f4672cada57d/resource/ee342b3a-d418-40a9-ae29-812fb118e648/download/moz_children_under_five_2020_csv.zip
  format: zip
  id: resource_ee342b3a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: moz_children_under_five_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mozambique: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/fa47f9e0-ee19-4081-b325-f4672cada57d/resource/c73d781e-985c-48ab-ac5e-50a003fa52dc/download/moz_children_under_five_2020_geotiff.zip
  format: zip
  id: resource_c73d781e
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: moz_children_under_five_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mozambique: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/fa47f9e0-ee19-4081-b325-f4672cada57d/resource/cb877103-6129-4fe1-ba92-f15ca0f03050/download/moz_elderly_60_plus_2020_csv.zip
  format: zip
  id: resource_cb877103
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: moz_elderly_60_plus_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mozambique: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/fa47f9e0-ee19-4081-b325-f4672cada57d/resource/a461bebf-5cc0-4cb1-9755-da1f9bd0328a/download/moz_elderly_60_plus_2020_geotiff.zip
  format: zip
  id: resource_a461bebf
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: moz_elderly_60_plus_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mozambique: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/fa47f9e0-ee19-4081-b325-f4672cada57d/resource/67fff4d4-d94b-4736-b6c7-bf8e10b8b66d/download/moz_men_2020_csv.zip
  format: zip
  id: resource_67fff4d4
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: moz_men_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mozambique: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/fa47f9e0-ee19-4081-b325-f4672cada57d/resource/6624e88a-d394-4d15-8154-3f77c1d5a17f/download/moz_men_2020_geotiff.zip
  format: zip
  id: resource_6624e88a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: moz_men_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mozambique: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/fa47f9e0-ee19-4081-b325-f4672cada57d/resource/5e009706-12f3-42d5-900c-ae592c77023a/download/moz_women_2020_csv.zip
  format: zip
  id: resource_5e009706
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: moz_women_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mozambique: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/fa47f9e0-ee19-4081-b325-f4672cada57d/resource/ade6718e-b3cf-4fb5-bce4-e1f539b0b3b9/download/moz_women_2020_geotiff.zip
  format: zip
  id: resource_ade6718e
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: moz_women_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mozambique: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/fa47f9e0-ee19-4081-b325-f4672cada57d/resource/860dda84-a9a2-424d-bb53-8fd2c5f50d83/download/moz_women_of_reproductive_age_15_49_2020_csv.zip
  format: zip
  id: resource_860dda84
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: moz_women_of_reproductive_age_15_49_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mozambique: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/fa47f9e0-ee19-4081-b325-f4672cada57d/resource/5d2c7522-acb9-4416-828a-21c1c5cbec1d/download/moz_women_of_reproductive_age_15_49_2020_geotiff.zip
  format: zip
  id: resource_5d2c7522
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: moz_women_of_reproductive_age_15_49_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mozambique: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/fa47f9e0-ee19-4081-b325-f4672cada57d/resource/754462ec-34db-413d-b89c-d103b742c7d4/download/moz_youth_15_24_2020_csv.zip
  format: zip
  id: resource_754462ec
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: moz_youth_15_24_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mozambique: High Resolution Population Density Maps + Demographic
    Estimates (zip)'
  download_url: https://data.humdata.org/dataset/fa47f9e0-ee19-4081-b325-f4672cada57d/resource/070bdac1-181f-4563-a43a-96db1e811d7e/download/moz_youth_15_24_2020_geotiff.zip
  format: zip
  id: resource_070bdac1
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: moz_youth_15_24_2020_geotiff.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-moz_metad4g_highresolutionpopulationd_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - MOZ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2022-10-06'
  start: '2019-05-20'
temporal_resolution: null
title: 'Mozambique: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
