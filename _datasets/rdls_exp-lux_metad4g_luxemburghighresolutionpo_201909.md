---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook Data for Good
    url: https://data.humdata.org/dataset/luxemburg-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/luxemburg-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/luxemburg-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/luxemburg-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-lux_metad4g_luxemburghighresolutionpo_201909
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Luxemburg: (1) Overall population
  density (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly
  (ages 60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/luxemburg-high-resolution-population-density-maps-demographic-estimates]'
details: "To reference this data, please use the following citation: Facebook Connectivity\
  \ Lab and Center for International Earth Science Information Network - CIESIN -\
  \ Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery\
  \ for HRSL \xC2\xA9 2016 DigitalGlobe. Accessed DAY MONTH YEAR.' Please note that\
  \ as of 2024, Meta's high resolution population density maps are no longer being\
  \ updated."
exposure:
- asset_type:
    description: High-resolution gridded population density for overall population
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
  description: High-resolution population density maps were created by applying machine
    learning algorithms to identify building footprints from commercial satellite
    imagery, then overlaying population estimates derived from census data and other
    publicly available demographic statistics. The resulting gridded datasets provide
    spatial distributions of total population and demographic subgroups at fine resolution
    across Luxembourg.
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
- href: https://data.humdata.org/dataset/luxemburg-high-resolution-population-density-maps-demographic-estimates
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
  description: 'Luxembourg - Luxemburg: High Resolution Population Density Maps +
    Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/f2b1246b-2f88-4109-990d-46a3faf77e5f/resource/a737a8a2-493e-4eab-b8c4-9278970cc427/download/lux_children_under_five_geotiff.zip
  format: null
  id: resource_a737a8a2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: LUX_children_under_five_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Luxembourg - Luxemburg: High Resolution Population Density Maps +
    Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/f2b1246b-2f88-4109-990d-46a3faf77e5f/resource/8115f574-d0d4-4eaa-95a2-9253b44d0498/download/lux_elderly_60_plus_geotiff.zip
  format: null
  id: resource_8115f574
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: LUX_elderly_60_plus_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Luxembourg - Luxemburg: High Resolution Population Density Maps +
    Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/f2b1246b-2f88-4109-990d-46a3faf77e5f/resource/a37c28ba-114a-48fc-b69e-83c792e389b7/download/lux_men_geotiff.zip
  format: null
  id: resource_a37c28ba
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: LUX_men_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Luxembourg - Luxemburg: High Resolution Population Density Maps +
    Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/f2b1246b-2f88-4109-990d-46a3faf77e5f/resource/f8c163a4-5041-45e9-95f1-386bd4d70dc3/download/lux_women_geotiff.zip
  format: null
  id: resource_f8c163a4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: LUX_women_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Luxembourg - Luxemburg: High Resolution Population Density Maps +
    Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/f2b1246b-2f88-4109-990d-46a3faf77e5f/resource/12925c02-47f3-40d7-8832-ac07e9858567/download/lux_women_of_reproductive_age_15_49_geotiff.zip
  format: null
  id: resource_12925c02
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: LUX_women_of_reproductive_age_15_49_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Luxembourg - Luxemburg: High Resolution Population Density Maps +
    Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/f2b1246b-2f88-4109-990d-46a3faf77e5f/resource/f24695f9-d02d-4567-b74c-8341390997e0/download/lux_youth_15_24_geotiff.zip
  format: null
  id: resource_f24695f9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: LUX_youth_15_24_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Luxembourg - Luxemburg: High Resolution Population Density Maps +
    Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/f2b1246b-2f88-4109-990d-46a3faf77e5f/resource/9c552d6f-687f-458e-bf7a-55e83753108c/download/lux_children_under_five_2019-08-03.csv.zip
  format: null
  id: resource_9c552d6f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: LUX_children_under_five_2019-08-03.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Luxembourg - Luxemburg: High Resolution Population Density Maps +
    Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/f2b1246b-2f88-4109-990d-46a3faf77e5f/resource/6798a2e1-8077-481e-81fe-cc8c54657468/download/lux_elderly_60_plus_2019-08-03.csv.zip
  format: null
  id: resource_6798a2e1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: LUX_elderly_60_plus_2019-08-03.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Luxembourg - Luxemburg: High Resolution Population Density Maps +
    Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/f2b1246b-2f88-4109-990d-46a3faf77e5f/resource/7681f448-77dc-4818-953d-963d6c8e61cd/download/lux_men_2019-08-03.csv.zip
  format: null
  id: resource_7681f448
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: LUX_men_2019-08-03.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Luxembourg - Luxemburg: High Resolution Population Density Maps +
    Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/f2b1246b-2f88-4109-990d-46a3faf77e5f/resource/3afb0efe-2f89-4a3e-b5d9-5b7f15acd489/download/lux_women_2019-08-03.csv.zip
  format: null
  id: resource_3afb0efe
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: LUX_women_2019-08-03.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Luxembourg - Luxemburg: High Resolution Population Density Maps +
    Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/f2b1246b-2f88-4109-990d-46a3faf77e5f/resource/2d5ee6af-786f-408f-8fb6-fe77506fba37/download/lux_women_of_reproductive_age_15_49_2019-08-03.csv.zip
  format: null
  id: resource_2d5ee6af
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: LUX_women_of_reproductive_age_15_49_2019-08-03.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Luxembourg - Luxemburg: High Resolution Population Density Maps +
    Demographic Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/f2b1246b-2f88-4109-990d-46a3faf77e5f/resource/a7f03ed5-4ad2-488d-a3a8-9c0676d7c0b8/download/lux_youth_15_24_2019-08-03.csv.zip
  format: null
  id: resource_a7f03ed5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: LUX_youth_15_24_2019-08-03.csv.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-lux_metad4g_luxemburghighresolutionpo_201909
spatial:
  bbox: null
  centroid: null
  countries:
  - LUX
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2019-09-23'
  start: '2019-09-19'
temporal_resolution: null
title: 'Luxembourg - Luxemburg: High Resolution Population Density Maps + Demographic
  Estimates'
version: null
vulnerability: null
---
