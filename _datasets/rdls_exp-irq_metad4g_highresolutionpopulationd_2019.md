---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook (Meta)
    url: https://data.humdata.org/dataset/iraq-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/iraq-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/iraq-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/iraq-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-irq_metad4g_highresolutionpopulationd_2019
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Iraq: (1) Overall population density
  (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly (ages
  60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/iraq-high-resolution-population-density-maps-demographic-estimates]'
details: "To reference this data, please use the following citation: Facebook Connectivity\
  \ Lab and Center for International Earth Science Information Network - CIESIN -\
  \ Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery\
  \ for HRSL \xC2\xA9 2016 DigitalGlobe. Accessed DAY MONTH YEAR.' Please note that\
  \ as of 2024, Meta's high resolution population density maps are no longer being\
  \ updated."
exposure:
- asset_type:
    description: High-resolution gridded population density maps for overall population
      and demographic subgroups (children 0-5, youth 15-24, elderly 60+, women, men,
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Machine learning algorithms identified building footprints from commercial
    satellite imagery across Iraq. Population estimates derived from publicly available
    census data and demographic statistics were spatially distributed to building
    locations using methodology developed in partnership with Columbia University,
    producing high-resolution gridded population density maps for 2020 at national
    scale.
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
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/iraq-high-resolution-population-density-maps-demographic-estimates
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
  description: 'Iraq: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/8ed6a074-e44e-4480-a405-8d6d4d4f672a/resource/89fdce6b-b8ed-4cfd-88e8-0d0c34209595/download/irq_general_2020_geotiff.zip
  format: zip
  id: resource_89fdce6b
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: irq_general_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Iraq: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/8ed6a074-e44e-4480-a405-8d6d4d4f672a/resource/426749b1-38fc-4282-baf7-ea23aab8df39/download/irq_general_2020_csv.zip
  format: zip
  id: resource_426749b1
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: irq_general_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Iraq: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/8ed6a074-e44e-4480-a405-8d6d4d4f672a/resource/5894440e-7bc7-4740-9b0a-fafcbea92a3c/download/irq_children_under_five_2020_geotiff.zip
  format: zip
  id: resource_5894440e
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: irq_children_under_five_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Iraq: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/8ed6a074-e44e-4480-a405-8d6d4d4f672a/resource/def6b223-7706-4b6c-a94c-fd3fbb46ce2a/download/irq_elderly_60_plus_2020_geotiff.zip
  format: zip
  id: resource_def6b223
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: irq_elderly_60_plus_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Iraq: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/8ed6a074-e44e-4480-a405-8d6d4d4f672a/resource/f5bcb346-36ca-41ed-a98a-e2307c395057/download/irq_men_2020_geotiff.zip
  format: zip
  id: resource_f5bcb346
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: irq_men_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Iraq: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/8ed6a074-e44e-4480-a405-8d6d4d4f672a/resource/6776120a-15ef-41de-84a3-bee6564be578/download/irq_women_2020_geotiff.zip
  format: zip
  id: resource_6776120a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: irq_women_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Iraq: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/8ed6a074-e44e-4480-a405-8d6d4d4f672a/resource/fcd5f0f5-c221-4ad9-943a-23829b49ab3e/download/irq_women_of_reproductive_age_15_49_2020_geotiff.zip
  format: zip
  id: resource_fcd5f0f5
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: irq_women_of_reproductive_age_15_49_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Iraq: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/8ed6a074-e44e-4480-a405-8d6d4d4f672a/resource/c795cff9-9213-4995-996b-b0b43b464c0b/download/irq_youth_15_24_2020_geotiff.zip
  format: zip
  id: resource_c795cff9
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: irq_youth_15_24_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Iraq: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/8ed6a074-e44e-4480-a405-8d6d4d4f672a/resource/a08bd61a-26ec-4ef7-98fe-442e015bda26/download/irq_children_under_five_2020_csv.zip
  format: zip
  id: resource_a08bd61a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: irq_children_under_five_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Iraq: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/8ed6a074-e44e-4480-a405-8d6d4d4f672a/resource/3203facc-d1e8-4e24-a84c-a1cc2bad454a/download/irq_elderly_60_plus_2019-08-03_csv.zip
  format: null
  id: resource_3203facc
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: IRQ_elderly_60.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Iraq: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/8ed6a074-e44e-4480-a405-8d6d4d4f672a/resource/d8825488-9e4f-4499-b0c9-fe6188641269/download/irq_men_2020_csv.zip
  format: zip
  id: resource_d8825488
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: irq_men_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Iraq: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/8ed6a074-e44e-4480-a405-8d6d4d4f672a/resource/f015512f-81df-4876-8e40-3fef0b531758/download/irq_women_2020_csv.zip
  format: zip
  id: resource_f015512f
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: irq_women_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Iraq: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/8ed6a074-e44e-4480-a405-8d6d4d4f672a/resource/62ec845d-39a1-4274-9aca-02bb656a9033/download/irq_women_of_reproductive_age_15_49_2020_csv.zip
  format: zip
  id: resource_62ec845d
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: irq_women_of_reproductive_age_15_49_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Iraq: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/8ed6a074-e44e-4480-a405-8d6d4d4f672a/resource/e0134b83-3688-4ca4-9021-b9f5367d5c52/download/irq_youth_15_24_2020_csv.zip
  format: zip
  id: resource_e0134b83
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: irq_youth_15_24_2020_csv.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-irq_metad4g_highresolutionpopulationd_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - IRQ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2022-12-02'
  start: '2019-09-19'
temporal_resolution: null
title: 'Iraq: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
