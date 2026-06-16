---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook/Meta AI and Data for Good
    url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-nga
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-nga
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-nga
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-nga
dataset_id: rdls_exp-nga_metad4g_highresolutionpopulationd_2019
description: 'VERSION 1.5. The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Nigeria: (1) Overall population density
  (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly (ages
  60+) (7) Women of reproductive age (ages 15-49). There is also a tiled version of
  this dataset that may be easier to use if you are interested in many countries..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-nga]'
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
    description: High-resolution gridded population density estimates for Nigeria
      disaggregated by demographic groups (overall, women, men, children 0-5, youth
      15-24, elderly 60+, women of reproductive age 15-49)
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
    satellite imagery across Nigeria. Population estimates derived from publicly available
    census data and demographic statistics were then spatially allocated to these
    buildings using Columbia University's methodology, producing high-resolution gridded
    population density maps disaggregated by demographic cohorts for baseline exposure
    assessment.
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
- href: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-nga
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
  description: 'Nigeria: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/62ec6c48-2f23-476b-8c1e-e924ad79908d/resource/ec1ac1b2-616e-43a7-ba8c-29eaf3479f24/download/nga_general_2020_csv.zip
  format: zip
  id: resource_ec1ac1b2
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nga_general_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nigeria: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/62ec6c48-2f23-476b-8c1e-e924ad79908d/resource/6eff0694-8fda-4329-8ed3-c81b000b88d4/download/nga_general_2020_geotiff.zip
  format: zip
  id: resource_6eff0694
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nga_general_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nigeria: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/62ec6c48-2f23-476b-8c1e-e924ad79908d/resource/bf7f28a8-e49a-4d2a-99e4-354bc783eb6d/download/nga_children_under_five_2020_csv.zip
  format: zip
  id: resource_bf7f28a8
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nga_children_under_five_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nigeria: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/62ec6c48-2f23-476b-8c1e-e924ad79908d/resource/24a86279-ba51-410a-9e5e-443aecbb0edb/download/nga_children_under_five_2020_geotiff.zip
  format: zip
  id: resource_24a86279
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nga_children_under_five_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nigeria: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/62ec6c48-2f23-476b-8c1e-e924ad79908d/resource/e5006c78-ee45-4ec5-866b-edf22e07ccb0/download/nga_elderly_60_plus_2020_csv.zip
  format: zip
  id: resource_e5006c78
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nga_elderly_60_plus_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nigeria: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/62ec6c48-2f23-476b-8c1e-e924ad79908d/resource/663b8642-517a-4203-98f2-6e47da477376/download/nga_elderly_60_plus_2020_geotiff.zip
  format: zip
  id: resource_663b8642
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nga_elderly_60_plus_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nigeria: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/62ec6c48-2f23-476b-8c1e-e924ad79908d/resource/56b75eea-196a-4597-a561-77d1e226a5de/download/nga_men_2020_csv.zip
  format: zip
  id: resource_56b75eea
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nga_men_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nigeria: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/62ec6c48-2f23-476b-8c1e-e924ad79908d/resource/c0d13bc5-16eb-4885-953a-5e232de1bb0c/download/nga_men_2020_geotiff.zip
  format: zip
  id: resource_c0d13bc5
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nga_men_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nigeria: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/62ec6c48-2f23-476b-8c1e-e924ad79908d/resource/5c5a2da6-3f3f-4376-8cfc-15dc49e7be28/download/nga_women_2020_csv.zip
  format: zip
  id: resource_5c5a2da6
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nga_women_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nigeria: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/62ec6c48-2f23-476b-8c1e-e924ad79908d/resource/efa29efc-d921-410b-a0d8-f233f2496247/download/nga_women_2020_geotiff.zip
  format: zip
  id: resource_efa29efc
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nga_women_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nigeria: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/62ec6c48-2f23-476b-8c1e-e924ad79908d/resource/9f74ac83-4723-4c5e-aad3-0432e6f74f2e/download/nga_women_of_reproductive_age_15_49_2020_csv.zip
  format: zip
  id: resource_9f74ac83
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nga_women_of_reproductive_age_15_49_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nigeria: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/62ec6c48-2f23-476b-8c1e-e924ad79908d/resource/dc0fbb0a-04f7-4036-95f4-4b7413bffde6/download/nga_women_of_reproductive_age_15_49_2020_geotiff.zip
  format: zip
  id: resource_dc0fbb0a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nga_women_of_reproductive_age_15_49_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nigeria: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/62ec6c48-2f23-476b-8c1e-e924ad79908d/resource/46523605-752f-4084-bd6f-f12c5cb11f28/download/nga_youth_15_24_2020_csv.zip
  format: zip
  id: resource_46523605
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nga_youth_15_24_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nigeria: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/62ec6c48-2f23-476b-8c1e-e924ad79908d/resource/f20a1a6d-78a6-47d0-8d5e-398f71da3f3e/download/nga_youth_15_24_2020_geotiff.zip
  format: zip
  id: resource_f20a1a6d
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nga_youth_15_24_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This file has information about the cloud cover percentage and capture
    data of the satellite images used.
  download_url: https://data.humdata.org/dataset/62ec6c48-2f23-476b-8c1e-e924ad79908d/resource/e0c58181-7b90-46e3-b886-03dc47edcabb/download/nga_dg_metadata.json.zip
  format: null
  id: resource_e0c58181
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nga_dg_metadata.json.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-nga_metad4g_highresolutionpopulationd_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - NGA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2021-11-23'
  start: '2019-05-20'
temporal_resolution: null
title: 'Nigeria: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
