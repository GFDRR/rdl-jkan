---
attributions:
- entity:
    affiliation: null
    email: null
    name: AI and Data for Good at Meta (Facebook)
    url: https://data.humdata.org/dataset/indonesia-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/indonesia-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/indonesia-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/indonesia-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-idn_metad4g_highresolutionpopulationd_2019
description: 'VERSION 1.5. The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Indonesia: (1) Overall population
  density (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly
  (ages 60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/indonesia-high-resolution-population-density-maps-demographic-estimates]'
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
    description: High-resolution gridded population density for the overall population
      of Indonesia, disaggregated by demographic groups including women, men, children
      under five, youth aged 15-24, elderly aged 60+, and women of reproductive age
      15-49
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
  description: Building footprints are extracted from commercial satellite imagery
    using machine learning techniques developed by Meta. These footprints are then
    combined with national census data and demographic statistics in partnership with
    Columbia University to produce high-resolution gridded population density estimates
    disaggregated by age and sex groups for Indonesia as of 2020.
  sources:
  - id: source_1
    license: null
    name: AI and Data for Good at Meta (Facebook)
    risk_data_type:
    - exposure
    type: model
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
- href: https://data.humdata.org/dataset/indonesia-high-resolution-population-density-maps-demographic-estimates
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
  description: 'Indonesia: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/0474df44-62b5-4a4c-a4fd-fd733979e2cc/resource/94e808ad-9a61-426a-9fa3-60db15ad9eee/download/idn_children_under_five_2020_csv.zip
  format: zip
  id: resource_94e808ad
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: idn_children_under_five_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Indonesia: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/0474df44-62b5-4a4c-a4fd-fd733979e2cc/resource/358825e9-bdac-4fa0-ae0e-07ec3f2fd1b4/download/idn_children_under_five_2020_geotiff.zip
  format: zip
  id: resource_358825e9
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: idn_children_under_five_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Indonesia: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/0474df44-62b5-4a4c-a4fd-fd733979e2cc/resource/90fecfaf-8861-4715-af8f-941a1cd3ef90/download/idn_elderly_60_plus_2020_csv.zip
  format: zip
  id: resource_90fecfaf
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: idn_elderly_60_plus_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Indonesia: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/0474df44-62b5-4a4c-a4fd-fd733979e2cc/resource/a64ca5fb-7f43-47dd-a238-a2ff13b8e912/download/idn_elderly_60_plus_2020_geotiff.zip
  format: zip
  id: resource_a64ca5fb
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: idn_elderly_60_plus_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Indonesia: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/0474df44-62b5-4a4c-a4fd-fd733979e2cc/resource/2ed67ff5-5f22-44b5-89cd-1bc8133b7440/download/idn_men_2020_csv.zip
  format: zip
  id: resource_2ed67ff5
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: idn_men_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Indonesia: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/0474df44-62b5-4a4c-a4fd-fd733979e2cc/resource/b1bf4b94-771c-44d2-8484-bad8c475621a/download/idn_men_2020_geotiff.zip
  format: zip
  id: resource_b1bf4b94
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: idn_men_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Indonesia: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/0474df44-62b5-4a4c-a4fd-fd733979e2cc/resource/fb4f26e7-6f15-4f1e-ae14-8800890c5340/download/idn_women_2020_csv.zip
  format: zip
  id: resource_fb4f26e7
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: idn_women_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Indonesia: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/0474df44-62b5-4a4c-a4fd-fd733979e2cc/resource/4258beb2-1579-475a-8fc2-2028289585dd/download/idn_women_2020_geotiff.zip
  format: zip
  id: resource_4258beb2
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: idn_women_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Indonesia: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/0474df44-62b5-4a4c-a4fd-fd733979e2cc/resource/5c97ebbe-e1b5-4991-9e32-154f9d1e4942/download/idn_women_of_reproductive_age_15_49_2020_csv.zip
  format: zip
  id: resource_5c97ebbe
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: idn_women_of_reproductive_age_15_49_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Indonesia: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/0474df44-62b5-4a4c-a4fd-fd733979e2cc/resource/6620dbe5-24fd-4820-ba8b-6e5dd568b3be/download/idn_women_of_reproductive_age_15_49_2020_geotiff.zip
  format: zip
  id: resource_6620dbe5
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: idn_women_of_reproductive_age_15_49_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Indonesia: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/0474df44-62b5-4a4c-a4fd-fd733979e2cc/resource/64907f8a-a9d3-4763-b7cf-6c41c926cefc/download/idn_youth_15_24_2020_csv.zip
  format: zip
  id: resource_64907f8a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: idn_youth_15_24_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Indonesia: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/0474df44-62b5-4a4c-a4fd-fd733979e2cc/resource/776d4ce4-8490-4d96-8cc8-05980c7eadde/download/idn_youth_15_24_2020_geotiff.zip
  format: zip
  id: resource_776d4ce4
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: idn_youth_15_24_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Indonesia: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/0474df44-62b5-4a4c-a4fd-fd733979e2cc/resource/2b5f1310-ef98-44cb-b8b6-0d314add751c/download/idn_general_2020_geotiff.zip
  format: zip
  id: resource_2b5f1310
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: idn_general_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Indonesia: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/0474df44-62b5-4a4c-a4fd-fd733979e2cc/resource/1951bdfe-df73-45a9-b1bb-14d72966666c/download/idn_general_2020_csv.zip
  format: zip
  id: resource_1951bdfe
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: idn_general_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This file has information about the cloud cover percentage and capture
    data of the satellite images used.
  download_url: https://data.humdata.org/dataset/0474df44-62b5-4a4c-a4fd-fd733979e2cc/resource/c14b694d-dc47-4654-b1bf-5ee4a63f98eb/download/idn_dg_metadata.json.zip
  format: null
  id: resource_c14b694d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: idn_dg_metadata.json.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-idn_metad4g_highresolutionpopulationd_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - IDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-02-18'
  start: '2019-06-19'
temporal_resolution: null
title: 'Indonesia: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
