---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook Data for Good
    url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-nam
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-nam
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-nam
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-nam
dataset_id: rdls_exp-nam_metad4g_highresolutionpopulationd_2019
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Namibia: (1) Overall population density
  (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly (ages
  60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-nam]'
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
    imagery, then overlaying population estimates derived from publicly available
    census data and demographic statistics in partnership with Columbia University.
    The resulting gridded datasets provide spatial distributions of total population
    and seven demographic subgroups at fine resolution across Namibia for 2020.
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
- href: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-nam
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
  description: 'Namibia: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e161c03f-d8c5-4f14-876a-1ae83e53b75f/resource/dfe6b44d-9cba-4250-8a02-95d9ea64d093/download/nam_general_2020_geotiff.zip
  format: zip
  id: resource_dfe6b44d
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nam_general_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Namibia: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e161c03f-d8c5-4f14-876a-1ae83e53b75f/resource/992bda80-a43a-442a-8858-03f45dd9155d/download/nam_general_2020_csv.zip
  format: zip
  id: resource_992bda80
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nam_general_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Namibia: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e161c03f-d8c5-4f14-876a-1ae83e53b75f/resource/be810cdf-a39a-43b9-8dac-e8f7dab6edb8/download/nam_children_under_five_2020_csv.zip
  format: zip
  id: resource_be810cdf
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nam_children_under_five_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Namibia: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e161c03f-d8c5-4f14-876a-1ae83e53b75f/resource/1179fb90-f416-4638-88aa-b273176f7d63/download/nam_children_under_five_2020_geotiff.zip
  format: zip
  id: resource_1179fb90
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nam_children_under_five_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Namibia: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e161c03f-d8c5-4f14-876a-1ae83e53b75f/resource/75454ea9-9a01-4d0c-9316-49a8d5d62bcb/download/nam_elderly_60_plus_2020_csv.zip
  format: zip
  id: resource_75454ea9
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nam_elderly_60_plus_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Namibia: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e161c03f-d8c5-4f14-876a-1ae83e53b75f/resource/039c3173-7cf6-4e93-8567-c64c0dd01893/download/nam_elderly_60_plus_2020_geotiff.zip
  format: zip
  id: resource_039c3173
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nam_elderly_60_plus_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Namibia: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e161c03f-d8c5-4f14-876a-1ae83e53b75f/resource/d6b206bc-acaa-45b1-9a9a-77b7068f5db2/download/nam_men_2020_csv.zip
  format: zip
  id: resource_d6b206bc
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nam_men_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Namibia: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e161c03f-d8c5-4f14-876a-1ae83e53b75f/resource/afcc671f-6edc-42ee-a9d6-f9f368216a26/download/nam_men_2020_geotiff.zip
  format: zip
  id: resource_afcc671f
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nam_men_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Namibia: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e161c03f-d8c5-4f14-876a-1ae83e53b75f/resource/74e54724-2608-4a7e-9a45-4eb4242af6c4/download/nam_women_2020_csv.zip
  format: zip
  id: resource_74e54724
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nam_women_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Namibia: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e161c03f-d8c5-4f14-876a-1ae83e53b75f/resource/2e25c534-f839-4929-906d-0e89efcd419c/download/nam_women_2020_geotiff.zip
  format: zip
  id: resource_2e25c534
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nam_women_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Namibia: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e161c03f-d8c5-4f14-876a-1ae83e53b75f/resource/614020bc-78e7-4c07-9b26-92b1265a47ec/download/nam_women_of_reproductive_age_15_49_2020_csv.zip
  format: zip
  id: resource_614020bc
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nam_women_of_reproductive_age_15_49_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Namibia: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e161c03f-d8c5-4f14-876a-1ae83e53b75f/resource/d0a318da-9de8-4152-9cc3-00d5e78dba27/download/nam_women_of_reproductive_age_15_49_2020_geotiff.zip
  format: zip
  id: resource_d0a318da
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nam_women_of_reproductive_age_15_49_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Namibia: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e161c03f-d8c5-4f14-876a-1ae83e53b75f/resource/89d63bbc-4aab-462a-8e00-479b014d0bdd/download/nam_youth_15_24_2020_csv.zip
  format: zip
  id: resource_89d63bbc
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nam_youth_15_24_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Namibia: High Resolution Population Density Maps + Demographic Estimates
    (zip)'
  download_url: https://data.humdata.org/dataset/e161c03f-d8c5-4f14-876a-1ae83e53b75f/resource/6df740f5-faec-4ccd-ae68-b00bd55590a2/download/nam_youth_15_24_2020_geotiff.zip
  format: zip
  id: resource_6df740f5
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nam_youth_15_24_2020_geotiff.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-nam_metad4g_highresolutionpopulationd_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - NAM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2022-10-06'
  start: '2019-05-20'
temporal_resolution: null
title: 'Namibia: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
