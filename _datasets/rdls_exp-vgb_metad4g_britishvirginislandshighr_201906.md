---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook Data for Good
    url: https://data.humdata.org/dataset/british-virgin-islands-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/british-virgin-islands-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/british-virgin-islands-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/british-virgin-islands-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-vgb_metad4g_britishvirginislandshighr_201906
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in the British Virgin Islands: (1) Overall
  population density (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24)
  (6) Elderly (ages 60+) (7) Women of reproductive age (ages 15-49).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/british-virgin-islands-high-resolution-population-density-maps-demographic-estimates]'
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: High-resolution population density maps were created by applying machine
    learning algorithms to identify building footprints from commercial satellite
    imagery, then overlaying population estimates derived from census data and demographic
    statistics in partnership with Columbia University. The resulting gridded datasets
    provide spatial distribution of total population and seven demographic subgroups
    across the British Virgin Islands.
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
- href: https://data.humdata.org/dataset/british-virgin-islands-high-resolution-population-density-maps-demographic-estimates
  rel: source
loss:
  losses: []
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
  description: 'British Virgin Islands: High Resolution Population Density Maps +
    Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/0b8ad901-2b8f-4a45-ab7e-81fc3962fa0b/resource/e568d75b-baac-4239-83e8-0c8c95e5084e/download/population_vgb_2018-10-01.csv.zip
  format: null
  id: resource_e568d75b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_vgb_2018-10-01.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'British Virgin Islands: High Resolution Population Density Maps +
    Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/0b8ad901-2b8f-4a45-ab7e-81fc3962fa0b/resource/7361550c-ee24-4367-bcae-20decaa4f2e1/download/population_vgb_2018-10-01.zip
  format: null
  id: resource_7361550c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_vgb_2018-10-01.geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'British Virgin Islands: High Resolution Population Density Maps +
    Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/0b8ad901-2b8f-4a45-ab7e-81fc3962fa0b/resource/45fb24cf-74ce-4cd5-bc21-2d3295868269/download/vgb_children_under_five_2019-06-01_csv.zip
  format: null
  id: resource_45fb24cf
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VGB_children_under_five_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'British Virgin Islands: High Resolution Population Density Maps +
    Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/0b8ad901-2b8f-4a45-ab7e-81fc3962fa0b/resource/4534743e-d4ea-426c-be5c-ec72aa2acf11/download/vgb_children_under_five_2019-06-01_geotiff.zip
  format: null
  id: resource_4534743e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VGB_children_under_five_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'British Virgin Islands: High Resolution Population Density Maps +
    Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/0b8ad901-2b8f-4a45-ab7e-81fc3962fa0b/resource/e7dc0cb9-6bf4-4440-a5b0-221ac8bf0d6b/download/vgb_elderly_60_plus_2019-06-01_csv.zip
  format: null
  id: resource_e7dc0cb9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VGB_elderly_60_plus_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'British Virgin Islands: High Resolution Population Density Maps +
    Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/0b8ad901-2b8f-4a45-ab7e-81fc3962fa0b/resource/cf37c378-4554-479f-acbb-0797945b026f/download/vgb_elderly_60_plus_2019-06-01_geotiff.zip
  format: null
  id: resource_cf37c378
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VGB_elderly_60_plus_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'British Virgin Islands: High Resolution Population Density Maps +
    Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/0b8ad901-2b8f-4a45-ab7e-81fc3962fa0b/resource/61e11c1f-2c87-4df4-a57a-e1f24cb672fb/download/vgb_men_2019-06-01_csv.zip
  format: null
  id: resource_61e11c1f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VGB_men_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'British Virgin Islands: High Resolution Population Density Maps +
    Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/0b8ad901-2b8f-4a45-ab7e-81fc3962fa0b/resource/d3f60ee1-cae4-4ed8-aee3-2056369c8be7/download/vgb_men_2019-06-01_geotiff.zip
  format: null
  id: resource_d3f60ee1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VGB_men_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'British Virgin Islands: High Resolution Population Density Maps +
    Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/0b8ad901-2b8f-4a45-ab7e-81fc3962fa0b/resource/644ca8b3-9882-43c4-97fd-987ac5c89795/download/vgb_women_2019-06-01_csv.zip
  format: null
  id: resource_644ca8b3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VGB_women_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'British Virgin Islands: High Resolution Population Density Maps +
    Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/0b8ad901-2b8f-4a45-ab7e-81fc3962fa0b/resource/3458fe78-f5cf-49a6-9411-e229d29946a3/download/vgb_women_2019-06-01_geotiff.zip
  format: null
  id: resource_3458fe78
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VGB_women_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'British Virgin Islands: High Resolution Population Density Maps +
    Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/0b8ad901-2b8f-4a45-ab7e-81fc3962fa0b/resource/7a0ead7c-f04e-47d8-b583-172e78c6949e/download/vgb_women_of_reproductive_age_15_49_2019-06-01_csv.zip
  format: null
  id: resource_7a0ead7c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VGB_women_of_reproductive_age_15_49_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'British Virgin Islands: High Resolution Population Density Maps +
    Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/0b8ad901-2b8f-4a45-ab7e-81fc3962fa0b/resource/0549ab90-ef4d-40e3-ae94-4886d59af776/download/vgb_women_of_reproductive_age_15_49_2019-06-01_geotiff.zip
  format: null
  id: resource_0549ab90
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VGB_women_of_reproductive_age_15_49_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'British Virgin Islands: High Resolution Population Density Maps +
    Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/0b8ad901-2b8f-4a45-ab7e-81fc3962fa0b/resource/737a9709-fb0f-49e0-97cb-2c879149fce6/download/vgb_youth_15_24_2019-06-01_csv.zip
  format: null
  id: resource_737a9709
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VGB_youth_15_24_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'British Virgin Islands: High Resolution Population Density Maps +
    Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/0b8ad901-2b8f-4a45-ab7e-81fc3962fa0b/resource/d01b3e57-a647-4878-8321-de0d023bbbed/download/vgb_youth_15_24_2019-06-01_geotiff.zip
  format: null
  id: resource_d01b3e57
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VGB_youth_15_24_2019-06-01_geotiff.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-vgb_metad4g_britishvirginislandshighr_201906
spatial:
  bbox: null
  centroid: null
  countries:
  - VGB
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2019-06-11'
  start: '2019-06-10'
temporal_resolution: null
title: 'British Virgin Islands: High Resolution Population Density Maps + Demographic
  Estimates'
version: null
vulnerability: null
---
