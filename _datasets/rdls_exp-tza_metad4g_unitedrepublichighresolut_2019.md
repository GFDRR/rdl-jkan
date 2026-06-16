---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook/Meta AI and Data for Good
    url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-tza
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-tza
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-tza
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-tza
dataset_id: rdls_exp-tza_metad4g_unitedrepublichighresolut_2019
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in the United Republic of Tanzania:
  (1) Overall population density (2) Women (3) Men (4) Children (ages 0-5) (5) Youth
  (ages 15-24) (6) Elderly (ages 60+) (7) Women of reproductive age (ages 15-49).
  There is also a tiled version of this dataset that may be easier to use if you are
  interested in many countries.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-tza]'
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
    imagery, then overlaying general population estimates derived from publicly available
    census data and demographic statistics in partnership with Columbia University.
    The resulting gridded datasets provide spatially explicit population distributions
    for Tanzania at 100m resolution for 2020, disaggregated by demographic subgroups.
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
- href: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-tza
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
  description: 'United Republic of Tanzania: High Resolution Population Density Maps
    + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/385d61e2-e5bf-4dc2-87b4-a31030fdb334/resource/73b7df87-b9dc-4d08-988d-07ab8a79581d/download/tza_general_2020_geotiff.zip
  format: zip
  id: resource_73b7df87
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tza_general_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Republic of Tanzania: High Resolution Population Density Maps
    + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/385d61e2-e5bf-4dc2-87b4-a31030fdb334/resource/bdd35287-f32b-481e-af0c-d1b44cfe06d4/download/tza_general_2020_csv.zip
  format: zip
  id: resource_bdd35287
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tza_general_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Republic of Tanzania: High Resolution Population Density Maps
    + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/385d61e2-e5bf-4dc2-87b4-a31030fdb334/resource/8bf0e800-b69f-4181-b03a-b5f64a70a25b/download/tza_children_under_five_2020_csv.zip
  format: zip
  id: resource_8bf0e800
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tza_children_under_five_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Republic of Tanzania: High Resolution Population Density Maps
    + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/385d61e2-e5bf-4dc2-87b4-a31030fdb334/resource/7d7b8e88-c440-4952-95f1-44e75a0af855/download/tza_children_under_five_2020_geotiff.zip
  format: zip
  id: resource_7d7b8e88
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tza_children_under_five_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Republic of Tanzania: High Resolution Population Density Maps
    + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/385d61e2-e5bf-4dc2-87b4-a31030fdb334/resource/351d8fd7-e2f4-40b1-8712-42ab5aabff1f/download/tza_elderly_60_plus_2020_csv.zip
  format: zip
  id: resource_351d8fd7
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tza_elderly_60_plus_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Republic of Tanzania: High Resolution Population Density Maps
    + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/385d61e2-e5bf-4dc2-87b4-a31030fdb334/resource/8ae68240-385b-404e-95fb-baf4af24db76/download/tza_elderly_60_plus_2020_geotiff.zip
  format: zip
  id: resource_8ae68240
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tza_elderly_60_plus_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Republic of Tanzania: High Resolution Population Density Maps
    + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/385d61e2-e5bf-4dc2-87b4-a31030fdb334/resource/e108b1c8-384d-4b1d-8d5a-163d265878af/download/tza_men_2020_csv.zip
  format: zip
  id: resource_e108b1c8
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tza_men_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Republic of Tanzania: High Resolution Population Density Maps
    + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/385d61e2-e5bf-4dc2-87b4-a31030fdb334/resource/f66318ec-3537-4bc0-8bba-febf8bc7b0a6/download/tza_men_2020_geotiff.zip
  format: zip
  id: resource_f66318ec
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tza_men_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Republic of Tanzania: High Resolution Population Density Maps
    + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/385d61e2-e5bf-4dc2-87b4-a31030fdb334/resource/993bac8d-aaf1-4a13-b90b-33a87e1469dc/download/tza_women_2020_csv.zip
  format: zip
  id: resource_993bac8d
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tza_women_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Republic of Tanzania: High Resolution Population Density Maps
    + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/385d61e2-e5bf-4dc2-87b4-a31030fdb334/resource/f01bbce4-b878-48d6-a89d-5702d0a9d05d/download/tza_women_2020_geotiff.zip
  format: zip
  id: resource_f01bbce4
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tza_women_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Republic of Tanzania: High Resolution Population Density Maps
    + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/385d61e2-e5bf-4dc2-87b4-a31030fdb334/resource/a4ba0893-d4c2-474a-a948-5c382064e939/download/tza_women_of_reproductive_age_15_49_2020_csv.zip
  format: zip
  id: resource_a4ba0893
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tza_women_of_reproductive_age_15_49_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Republic of Tanzania: High Resolution Population Density Maps
    + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/385d61e2-e5bf-4dc2-87b4-a31030fdb334/resource/bf4a1dc3-3690-4ad6-abda-662f66c49fa6/download/tza_women_of_reproductive_age_15_49_2020_geotiff.zip
  format: zip
  id: resource_bf4a1dc3
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tza_women_of_reproductive_age_15_49_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Republic of Tanzania: High Resolution Population Density Maps
    + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/385d61e2-e5bf-4dc2-87b4-a31030fdb334/resource/bfd4eba1-5606-495d-b8ec-730ad46a3f6c/download/tza_youth_15_24_2020_csv.zip
  format: zip
  id: resource_bfd4eba1
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tza_youth_15_24_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Republic of Tanzania: High Resolution Population Density Maps
    + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/385d61e2-e5bf-4dc2-87b4-a31030fdb334/resource/df4f96e7-3f4f-473f-9478-0d1495698132/download/tza_youth_15_24_2020_geotiff.zip
  format: zip
  id: resource_df4f96e7
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tza_youth_15_24_2020_geotiff.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-tza_metad4g_unitedrepublichighresolut_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - TZA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2022-07-22'
  start: '2019-05-20'
temporal_resolution: null
title: 'United Republic of Tanzania: High Resolution Population Density Maps + Demographic
  Estimates'
version: null
vulnerability: null
---
