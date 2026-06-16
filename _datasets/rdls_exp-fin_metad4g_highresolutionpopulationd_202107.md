---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook/Meta AI and Data for Good
    url: https://data.humdata.org/dataset/finland-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/finland-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/finland-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/finland-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-fin_metad4g_highresolutionpopulationd_202107
description: 'VERSION 1.5. The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Finland: (1) Overall population density
  (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly (ages
  60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/finland-high-resolution-population-density-maps-demographic-estimates]'
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
    description: High-resolution gridded population density estimates disaggregated
      by age groups (children 0-5, youth 15-24, elderly 60+), sex (men, women), and
      reproductive status (women 15-49)
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
    learning algorithms to identify building footprints from commercial satellite
    imagery, then overlaying population estimates derived from census data and other
    public demographic sources in partnership with Columbia University. The resulting
    gridded datasets provide disaggregated population counts by age group, sex, and
    reproductive status at fine spatial resolution across Finland.
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
- href: https://data.humdata.org/dataset/finland-high-resolution-population-density-maps-demographic-estimates
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
  description: 'Finland: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/91be6b97-c32f-49b9-9e2d-aa620f05adb4/resource/c1df0a2d-16b3-4794-84ca-cb9e32775100/download/fin_children_under_five_2020_csv.zip
  format: null
  id: resource_c1df0a2d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fin_children_under_five_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Finland: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/91be6b97-c32f-49b9-9e2d-aa620f05adb4/resource/9bfbd288-1a02-49c4-b9ec-bbf40a21534c/download/fin_children_under_five_2020_geotiff.zip
  format: null
  id: resource_9bfbd288
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fin_children_under_five_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Finland: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/91be6b97-c32f-49b9-9e2d-aa620f05adb4/resource/7b8876f7-67d1-4273-a78c-1a7e0bc6e18a/download/fin_elderly_60_plus_2020_csv.zip
  format: null
  id: resource_7b8876f7
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fin_elderly_60_plus_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Finland: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/91be6b97-c32f-49b9-9e2d-aa620f05adb4/resource/844065ec-650a-46b2-a087-c4d49287ce46/download/fin_elderly_60_plus_2020_geotiff.zip
  format: null
  id: resource_844065ec
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fin_elderly_60_plus_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Finland: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/91be6b97-c32f-49b9-9e2d-aa620f05adb4/resource/02f45862-d570-452f-bc9b-fb4dccbb7b03/download/fin_general_2020_csv.zip
  format: null
  id: resource_02f45862
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fin_general_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Finland: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/91be6b97-c32f-49b9-9e2d-aa620f05adb4/resource/eafe3401-0df2-4745-a3c3-32977aceb87d/download/fin_general_2020_geotiff.zip
  format: null
  id: resource_eafe3401
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fin_general_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Finland: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/91be6b97-c32f-49b9-9e2d-aa620f05adb4/resource/7819b7f8-c9c9-459f-b33e-f5db1f96f97f/download/fin_men_2020_csv.zip
  format: null
  id: resource_7819b7f8
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fin_men_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Finland: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/91be6b97-c32f-49b9-9e2d-aa620f05adb4/resource/ea750d05-535c-4192-9c2f-931fa6431f84/download/fin_men_2020_geotiff.zip
  format: null
  id: resource_ea750d05
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fin_men_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Finland: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/91be6b97-c32f-49b9-9e2d-aa620f05adb4/resource/001c84f7-f46e-4b5a-9551-a95e96276a12/download/fin_women_2020_csv.zip
  format: null
  id: resource_001c84f7
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fin_women_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Finland: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/91be6b97-c32f-49b9-9e2d-aa620f05adb4/resource/97a4a7e8-4553-48fe-acbf-27888ba262b6/download/fin_women_2020_geotiff.zip
  format: null
  id: resource_97a4a7e8
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fin_women_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Finland: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/91be6b97-c32f-49b9-9e2d-aa620f05adb4/resource/cd1356c6-c9c4-4cb2-b9ff-018a22118c3b/download/fin_women_of_reproductive_age_15_49_2020_csv.zip
  format: null
  id: resource_cd1356c6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fin_women_of_reproductive_age_15_49_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Finland: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/91be6b97-c32f-49b9-9e2d-aa620f05adb4/resource/93fb8bbf-caff-4ed2-9210-542ab5f4c3f6/download/fin_women_of_reproductive_age_15_49_2020_geotiff.zip
  format: null
  id: resource_93fb8bbf
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fin_women_of_reproductive_age_15_49_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Finland: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/91be6b97-c32f-49b9-9e2d-aa620f05adb4/resource/2dccbb38-3f3b-4902-baa6-62772f7c5c90/download/fin_youth_15_24_2020_csv.zip
  format: null
  id: resource_2dccbb38
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fin_youth_15_24_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Finland: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/91be6b97-c32f-49b9-9e2d-aa620f05adb4/resource/6b7bfbe8-2235-4cba-be4f-92611c3a4fde/download/fin_youth_15_24_2020_geotiff.zip
  format: null
  id: resource_6b7bfbe8
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fin_youth_15_24_2020_geotiff.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-fin_metad4g_highresolutionpopulationd_202107
spatial:
  bbox: null
  centroid: null
  countries:
  - FIN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2021-07-14'
  start: '2021-07-13'
temporal_resolution: null
title: 'Finland: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
