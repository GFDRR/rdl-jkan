---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook (Meta)
    url: https://data.humdata.org/dataset/turkey-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/turkey-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/turkey-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/turkey-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-tur_metad4g_highresolutionpopulationd_2020
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Turkey: (1) Overall population density
  (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly (ages
  60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/turkey-high-resolution-population-density-maps-demographic-estimates]'
details: "To reference this data, please use the following citation: Facebook Connectivity\
  \ Lab and Center for International Earth Science Information Network - CIESIN -\
  \ Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery\
  \ for HRSL \xC2\xA9 2016 DigitalGlobe. Accessed DAY MONTH YEAR.'"
exposure:
- asset_type:
    description: High-resolution gridded population density for overall population
      and demographic subgroups (women, men, children 0-5, youth 15-24, elderly 60+,
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
    learning algorithms to commercially available satellite imagery to identify building
    footprints, then overlaying general population estimates derived from census data
    and demographic statistics in partnership with Columbia University. The resulting
    gridded datasets represent population distribution at fine spatial resolution
    for Turkey in 2020, disaggregated by demographic subgroups.
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
- href: https://data.humdata.org/dataset/turkey-high-resolution-population-density-maps-demographic-estimates
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
  description: 'Turkey: High Resolution Population Density Maps + Demographic Estimates
    (2020 population estimates)'
  download_url: https://data.humdata.org/dataset/dd6ae158-e35b-45e2-8eb8-dca248b8c3d6/resource/f724b3e0-4788-411c-81a5-2737ccada96e/download/population_turkey_2020_csv.zip
  format: null
  id: resource_f724b3e0
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_turkey_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Turkey: High Resolution Population Density Maps + Demographic Estimates
    (2020 population estimates)'
  download_url: https://data.humdata.org/dataset/dd6ae158-e35b-45e2-8eb8-dca248b8c3d6/resource/9a0963d3-60ad-40e7-83d0-d15d9f492fb4/download/population_turkey_2020_tif.zip
  format: null
  id: resource_9a0963d3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_turkey_2020_tif.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Turkey: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/dd6ae158-e35b-45e2-8eb8-dca248b8c3d6/resource/06cf6311-a894-4e37-8ae2-1ac9c3ac53ef/download/tur_children_under_five_2020_geotiff.zip
  format: null
  id: resource_06cf6311
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_children_under_five_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Turkey: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/dd6ae158-e35b-45e2-8eb8-dca248b8c3d6/resource/28781a77-958b-4b34-a293-6704c17bae28/download/tur_elderly_60_plus_2020_geotiff.zip
  format: null
  id: resource_28781a77
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_elderly_60_plus_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Turkey: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/dd6ae158-e35b-45e2-8eb8-dca248b8c3d6/resource/a0f1793b-440b-41ae-a702-e869de9bc012/download/tur_men_2020_geotiff.zip
  format: null
  id: resource_a0f1793b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_men_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Turkey: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/dd6ae158-e35b-45e2-8eb8-dca248b8c3d6/resource/d3ee498f-dc3c-46e5-a4ad-8168a8dce627/download/tur_women_2020_geotiff.zip
  format: null
  id: resource_d3ee498f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_women_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Turkey: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/dd6ae158-e35b-45e2-8eb8-dca248b8c3d6/resource/cf190ad2-fbed-425b-82e1-9cd74f998dae/download/tur_women_of_reproductive_age_15_49_2020_geotiff.zip
  format: null
  id: resource_cf190ad2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_women_of_reproductive_age_15_49_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Turkey: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/dd6ae158-e35b-45e2-8eb8-dca248b8c3d6/resource/8819843c-a94b-43f5-860d-6ea95471ff0c/download/tur_youth_15_24_2020_geotiff.zip
  format: null
  id: resource_8819843c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_youth_15_24_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Turkey: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/dd6ae158-e35b-45e2-8eb8-dca248b8c3d6/resource/5a003599-173a-4448-8c1f-dcc3d12f3d27/download/tur_children_under_five_2020_csv.zip
  format: null
  id: resource_5a003599
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_children_under_five_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Turkey: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/dd6ae158-e35b-45e2-8eb8-dca248b8c3d6/resource/523d8e62-dc2a-4c6d-9709-0a732e6025d3/download/tur_elderly_60_plus_2020_csv.zip
  format: null
  id: resource_523d8e62
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_elderly_60_plus_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Turkey: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/dd6ae158-e35b-45e2-8eb8-dca248b8c3d6/resource/eb335282-f921-42da-a144-ab3c5b863cff/download/tur_men_2020_csv.zip
  format: null
  id: resource_eb335282
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_men_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Turkey: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/dd6ae158-e35b-45e2-8eb8-dca248b8c3d6/resource/93c71bc8-08f6-44ca-bde3-628093f375d1/download/tur_women_2020_csv.zip
  format: null
  id: resource_93c71bc8
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_women_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Turkey: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/dd6ae158-e35b-45e2-8eb8-dca248b8c3d6/resource/d3b01629-45c1-48d7-831b-3dbc1034fc99/download/tur_women_of_reproductive_age_15_49_2020_csv.zip
  format: null
  id: resource_d3b01629
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_women_of_reproductive_age_15_49_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Turkey: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/dd6ae158-e35b-45e2-8eb8-dca248b8c3d6/resource/75292b09-b828-4679-9c9e-ed06c8d3863c/download/tur_youth_15_24_2020_csv.zip
  format: null
  id: resource_75292b09
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_youth_15_24_2020_csv.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-tur_metad4g_highresolutionpopulationd_2020
spatial:
  bbox: null
  centroid: null
  countries:
  - TUR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-10-23'
  start: '2020-01-01'
temporal_resolution: null
title: 'Turkey: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
