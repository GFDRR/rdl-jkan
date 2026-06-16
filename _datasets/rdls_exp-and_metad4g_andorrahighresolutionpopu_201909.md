---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook/Meta AI and Data for Good
    url: https://data.humdata.org/dataset/andorra-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/andorra-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/andorra-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/andorra-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-and_metad4g_andorrahighresolutionpopu_201909
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Andorra: (1) Overall population density
  (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly (ages
  60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/andorra-high-resolution-population-density-maps-demographic-estimates]'
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
    imagery, then overlaying population estimates derived from census data and demographic
    statistics in partnership with Columbia University. The resulting gridded datasets
    provide spatial distribution of total population and demographic subgroups at
    fine resolution across Andorra.
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
- href: https://data.humdata.org/dataset/andorra-high-resolution-population-density-maps-demographic-estimates
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
  description: 'Andorra: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/6fe3d563-d1ed-425e-b6f4-f45bc95c75f2/resource/0d3896ed-92d9-4c27-99b8-04d00804fb5a/download/anr_children_under_five_geotiff.zip
  format: null
  id: resource_0d3896ed
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ANR_children_under_five_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Andorra: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/6fe3d563-d1ed-425e-b6f4-f45bc95c75f2/resource/0427089b-b4fb-4bc9-ad31-e6991e575941/download/anr_elderly_60_plus_geotiff.zip
  format: null
  id: resource_0427089b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ANR_elderly_60_plus_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Andorra: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/6fe3d563-d1ed-425e-b6f4-f45bc95c75f2/resource/0788487c-efd2-4bee-a72e-f09b00edd349/download/anr_men_geotiff.zip
  format: null
  id: resource_0788487c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ANR_men_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Andorra: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/6fe3d563-d1ed-425e-b6f4-f45bc95c75f2/resource/c64583da-6d33-4da8-9a8b-2e775e9a8147/download/anr_women_geotiff.zip
  format: null
  id: resource_c64583da
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ANR_women_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Andorra: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/6fe3d563-d1ed-425e-b6f4-f45bc95c75f2/resource/a432ccfb-dda8-4282-95da-31b309a61894/download/anr_women_of_reproductive_age_15_49_geotiff.zip
  format: null
  id: resource_a432ccfb
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ANR_women_of_reproductive_age_15_49_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Andorra: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/6fe3d563-d1ed-425e-b6f4-f45bc95c75f2/resource/ce607aee-c27b-452c-badd-5420e35b4a84/download/anr_youth_15_24_geotiff.zip
  format: null
  id: resource_ce607aee
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ANR_youth_15_24_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Andorra: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/6fe3d563-d1ed-425e-b6f4-f45bc95c75f2/resource/41a4174c-7240-4755-a645-58586853cdaa/download/anr_children_under_five_2019-08-03_csv.zip
  format: null
  id: resource_41a4174c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ANR_children_under_five_2019-08-03_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Andorra: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/6fe3d563-d1ed-425e-b6f4-f45bc95c75f2/resource/4030634b-e273-432f-b33d-bed00ecdb4e6/download/anr_elderly_60_plus_2019-08-03_csv.zip
  format: null
  id: resource_4030634b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ANR_elderly_60_plus_2019-08-03_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Andorra: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/6fe3d563-d1ed-425e-b6f4-f45bc95c75f2/resource/5f1df672-b8be-4e3f-91d0-ac15cf9116ac/download/anr_men_2019-08-03_csv.zip
  format: null
  id: resource_5f1df672
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ANR_men_2019-08-03_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Andorra: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/6fe3d563-d1ed-425e-b6f4-f45bc95c75f2/resource/9bea72b0-67b2-47b1-9783-c4ff739030bb/download/anr_women_2019-08-03_csv.zip
  format: null
  id: resource_9bea72b0
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ANR_women_2019-08-03_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Andorra: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/6fe3d563-d1ed-425e-b6f4-f45bc95c75f2/resource/ae3636c2-bdbe-46fd-bb93-515382ed70f7/download/anr_women_of_reproductive_age_15_49_2019-08-03_csv.zip
  format: null
  id: resource_ae3636c2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ANR_women_of_reproductive_age_15_49_2019-08-03_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Andorra: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/6fe3d563-d1ed-425e-b6f4-f45bc95c75f2/resource/382262c1-2f0b-4e9e-854b-083f5d09bda2/download/anr_youth_15_24_2019-08-03_csv.zip
  format: null
  id: resource_382262c1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ANR_youth_15_24_2019-08-03_csv.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-and_metad4g_andorrahighresolutionpopu_201909
spatial:
  bbox: null
  centroid: null
  countries:
  - AND
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2019-09-23'
  start: '2019-09-19'
temporal_resolution: null
title: 'Andorra: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
