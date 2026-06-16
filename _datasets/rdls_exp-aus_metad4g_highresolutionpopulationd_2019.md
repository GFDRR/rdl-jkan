---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook Data for Good
    url: https://data.humdata.org/dataset/australia-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/australia-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/australia-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/australia-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-aus_metad4g_highresolutionpopulationd_2019
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Australia: (1) Overall population
  density (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly
  (ages 60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/australia-high-resolution-population-density-maps-demographic-estimates]'
details: "To reference this data, please use the following citation: Facebook Connectivity\
  \ Lab and Center for International Earth Science Information Network - CIESIN -\
  \ Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery\
  \ for HRSL \xC2\xA9 2016 DigitalGlobe. Accessed DAY MONTH YEAR.' Please note that\
  \ as of 2024, Meta's high resolution population density maps are no longer being\
  \ updated."
exposure:
- asset_type:
    description: High-resolution gridded population density estimates disaggregated
      by age groups (children 0-5, youth 15-24, elderly 60+, women of reproductive
      age 15-49) and sex
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
    learning to satellite imagery to identify building footprints, then overlaying
    population estimates derived from census data and demographic statistics in partnership
    with Columbia University. The resulting gridded datasets provide spatially explicit
    population distributions disaggregated by demographic characteristics across Australia.
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
- href: https://data.humdata.org/dataset/australia-high-resolution-population-density-maps-demographic-estimates
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
  description: 'Australia: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/5ac850be-31be-4b6d-848c-c477b89b1c85/resource/2f519769-1c2c-429c-80e3-c5547a94b1b4/download/aus_elderly_60_plus_2019-06-01_csv.zip
  format: null
  id: resource_2f519769
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: AUS_elderly_60_plus_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Australia: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/5ac850be-31be-4b6d-848c-c477b89b1c85/resource/9d9a6648-d474-4663-ac76-21b0b294ea2c/download/aus_men_2019-06-01_csv.zip
  format: null
  id: resource_9d9a6648
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: AUS_men_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Australia: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/5ac850be-31be-4b6d-848c-c477b89b1c85/resource/df882ab4-90f3-461b-933b-7be88ca3508e/download/aus_northeast_children_under_five_2019-06-01_geotiff.zip
  format: null
  id: resource_df882ab4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: AUS_northeast_children_under_five_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Australia: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/5ac850be-31be-4b6d-848c-c477b89b1c85/resource/b95d3746-7461-492f-a100-65320d246b7a/download/aus_northeast_elderly_60_plus_2019-06-01_geotiff.zip
  format: null
  id: resource_b95d3746
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: AUS_northeast_elderly_60_plus_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Australia: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/5ac850be-31be-4b6d-848c-c477b89b1c85/resource/bfb7809f-da79-4184-bba1-8e7c5c38beaa/download/aus_northeast_men_2019-06-01_geotiff.zip
  format: null
  id: resource_bfb7809f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: AUS_northeast_men_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Australia: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/5ac850be-31be-4b6d-848c-c477b89b1c85/resource/fe5d0fc6-96a2-4bb9-9e61-fcff2eaf69f9/download/aus_northeast_women_2019-06-01_geotiff.zip
  format: null
  id: resource_fe5d0fc6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: AUS_northeast_women_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Australia: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/5ac850be-31be-4b6d-848c-c477b89b1c85/resource/719700f7-e449-482c-8315-4e98923867b8/download/aus_northeast_women_of_reproductive_age_15_49_2019-06-01_geotiff.zip
  format: null
  id: resource_719700f7
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: AUS_northeast_women_of_reproductive_age_15_49_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Australia: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/5ac850be-31be-4b6d-848c-c477b89b1c85/resource/56c3e808-b281-4712-b168-d8f3080e66be/download/aus_northeast_youth_15_24_2019-06-01_geotiff.zip
  format: null
  id: resource_56c3e808
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: AUS_northeast_youth_15_24_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Australia: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/5ac850be-31be-4b6d-848c-c477b89b1c85/resource/b2c29a00-1ec5-458b-b437-3acb4d364c99/download/aus_northwest_children_under_five_2019-06-01_geotiff.zip
  format: null
  id: resource_b2c29a00
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: AUS_northwest_children_under_five_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Australia: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/5ac850be-31be-4b6d-848c-c477b89b1c85/resource/6816c7d2-4cd6-4429-8317-4f549a6ae2ce/download/aus_northwest_elderly_60_plus_2019-06-01_geotiff.zip
  format: null
  id: resource_6816c7d2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: AUS_northwest_elderly_60_plus_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Australia: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/5ac850be-31be-4b6d-848c-c477b89b1c85/resource/61f7c3e6-3402-4adc-bbc1-bfeef972fd0a/download/aus_northwest_men_2019-06-01_geotiff.zip
  format: null
  id: resource_61f7c3e6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: AUS_northwest_men_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Australia: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/5ac850be-31be-4b6d-848c-c477b89b1c85/resource/1beb5241-d500-45cf-bf28-d60034cb4a67/download/aus_northwest_women_2019-06-01_geotiff.zip
  format: null
  id: resource_1beb5241
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: AUS_northwest_women_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Australia: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/5ac850be-31be-4b6d-848c-c477b89b1c85/resource/1c6a578c-0f8f-4d49-a0eb-586890a367dc/download/aus_northwest_women_of_reproductive_age_15_49_2019-06-01_geotiff.zip
  format: null
  id: resource_1c6a578c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: AUS_northwest_women_of_reproductive_age_15_49_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Australia: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/5ac850be-31be-4b6d-848c-c477b89b1c85/resource/6255f92a-d48e-49bd-9b83-ca864f5dd045/download/aus_northwest_youth_15_24_2019-06-01_geotiff.zip
  format: null
  id: resource_6255f92a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: AUS_northwest_youth_15_24_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Australia: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/5ac850be-31be-4b6d-848c-c477b89b1c85/resource/78e8fa17-69af-406e-95b9-f376264cbe9b/download/aus_southeast_children_under_five_2019-06-01_geotiff.zip
  format: null
  id: resource_78e8fa17
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: AUS_southeast_children_under_five_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Australia: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/5ac850be-31be-4b6d-848c-c477b89b1c85/resource/93b177ee-3430-4433-a563-8e693d1e271d/download/aus_southeast_elderly_60_plus_2019-06-01_geotiff.zip
  format: null
  id: resource_93b177ee
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: AUS_southeast_elderly_60_plus_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Australia: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/5ac850be-31be-4b6d-848c-c477b89b1c85/resource/6e1a803a-6250-45b2-9161-139f80f4189d/download/aus_southeast_men_2019-06-01_geotiff.zip
  format: null
  id: resource_6e1a803a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: AUS_southeast_men_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Australia: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/5ac850be-31be-4b6d-848c-c477b89b1c85/resource/b753531f-1f71-4894-8141-053287eaaa37/download/aus_southeast_women_2019-06-01_geotiff.zip
  format: null
  id: resource_b753531f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: AUS_southeast_women_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Australia: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/5ac850be-31be-4b6d-848c-c477b89b1c85/resource/e382cf41-113f-489c-9a95-d6410d10b4e4/download/aus_southeast_women_of_reproductive_age_15_49_2019-06-01_geotiff.zip
  format: null
  id: resource_e382cf41
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: AUS_southeast_women_of_reproductive_age_15_49_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Australia: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/5ac850be-31be-4b6d-848c-c477b89b1c85/resource/298212f6-fe86-44e2-ad86-083e6bbdcb13/download/aus_southeast_youth_15_24_2019-06-01_geotiff.zip
  format: null
  id: resource_298212f6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: AUS_southeast_youth_15_24_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Australia: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/5ac850be-31be-4b6d-848c-c477b89b1c85/resource/151ee16f-84a5-4c14-a904-03090d483688/download/aus_southwest_children_under_five_2019-06-01_geotiff.zip
  format: null
  id: resource_151ee16f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: AUS_southwest_children_under_five_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Australia: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/5ac850be-31be-4b6d-848c-c477b89b1c85/resource/2e05e697-4585-4fd8-9461-56e30b5948ee/download/aus_southwest_elderly_60_plus_2019-06-01_geotiff.zip
  format: null
  id: resource_2e05e697
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: AUS_southwest_elderly_60_plus_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Australia: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/5ac850be-31be-4b6d-848c-c477b89b1c85/resource/1611d9da-f017-4fa7-a7a2-6f74672e67ac/download/aus_southwest_men_2019-06-01_geotiff.zip
  format: null
  id: resource_1611d9da
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: AUS_southwest_men_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Australia: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/5ac850be-31be-4b6d-848c-c477b89b1c85/resource/4f9ba992-8750-41cc-aa6f-000ed64ddf07/download/aus_southwest_women_2019-06-01_geotiff.zip
  format: null
  id: resource_4f9ba992
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: AUS_southwest_women_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Australia: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/5ac850be-31be-4b6d-848c-c477b89b1c85/resource/bd17bd7e-68be-4e4f-9e28-5445a48692f3/download/aus_southwest_women_of_reproductive_age_15_49_2019-06-01_geotiff.zip
  format: null
  id: resource_bd17bd7e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: AUS_southwest_women_of_reproductive_age_15_49_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Australia: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/5ac850be-31be-4b6d-848c-c477b89b1c85/resource/48046d11-40e8-4e1a-a57c-fdbb23a28605/download/aus_southwest_youth_15_24_2019-06-01_geotiff.zip
  format: null
  id: resource_48046d11
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: AUS_southwest_youth_15_24_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Australia: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/5ac850be-31be-4b6d-848c-c477b89b1c85/resource/5b3f9f96-72b2-4e1d-a4e5-2009408a5e22/download/aus_women_2019-06-01_csv.zip
  format: null
  id: resource_5b3f9f96
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: AUS_women_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Australia: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/5ac850be-31be-4b6d-848c-c477b89b1c85/resource/23891e5a-30f7-4470-ba22-68cf55d1025b/download/aus_women_of_reproductive_age_15_49_2019-06-01_csv.zip
  format: null
  id: resource_23891e5a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: AUS_women_of_reproductive_age_15_49_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Australia: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/5ac850be-31be-4b6d-848c-c477b89b1c85/resource/91d665ca-21f4-4da0-9d89-05da5000b236/download/aus_youth_15_24_2019-06-01_csv.zip
  format: null
  id: resource_91d665ca
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: AUS_youth_15_24_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Australia: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/5ac850be-31be-4b6d-848c-c477b89b1c85/resource/b36cce9b-d707-4328-96a8-240b1b26781f/download/population_aus_2018-10-01.csv.zip
  format: null
  id: resource_b36cce9b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_aus_2018-10-01.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Australia: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/5ac850be-31be-4b6d-848c-c477b89b1c85/resource/6a8d9dcb-2c3f-4575-bac0-856d07aaea1c/download/population_aus_northeast_2018-10-01_geotiff.zip
  format: null
  id: resource_6a8d9dcb
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_aus_northeast_2018-10-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Australia: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/5ac850be-31be-4b6d-848c-c477b89b1c85/resource/61323523-034a-4228-82ed-204b16d2eb11/download/population_aus_northwest_2018-10-01_geotiff.zip
  format: null
  id: resource_61323523
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_aus_northwest_2018-10-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Australia: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/5ac850be-31be-4b6d-848c-c477b89b1c85/resource/cd0ab7f5-b59e-48ca-b8dc-6042fff6b61f/download/population_aus_southeast_2018-10-01_geotiff.zip
  format: null
  id: resource_cd0ab7f5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_aus_southeast_2018-10-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Australia: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/5ac850be-31be-4b6d-848c-c477b89b1c85/resource/960374ef-1b47-4723-a78c-1bd5a296b262/download/population_aus_southwest_2018-10-01_geotiff.zip
  format: null
  id: resource_960374ef
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_aus_southwest_2018-10-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Australia: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/5ac850be-31be-4b6d-848c-c477b89b1c85/resource/20485bdc-797c-480a-ab66-9712538b3a70/download/aus_children_under_five_2019-06-01_csv.zip
  format: null
  id: resource_20485bdc
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: AUS_children_under_five_2019-06-01_csv.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-aus_metad4g_highresolutionpopulationd_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - AUS
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2019-11-06'
  start: '2019-06-19'
temporal_resolution: null
title: 'Australia: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
