---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook Data for Good
    url: https://data.humdata.org/dataset/aruba-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/aruba-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/aruba-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/aruba-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-abw_metad4g_arubahighresolutionpopula_2019
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Aruba: (1) Overall population density
  (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly (ages
  60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/aruba-high-resolution-population-density-maps-demographic-estimates]'
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
    learning to satellite imagery to identify building footprints, then overlaying
    population estimates derived from census data and demographic statistics at the
    building level. The resulting gridded datasets represent spatial distributions
    of total population and seven demographic subgroups across Aruba at approximately
    100m resolution.
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
- href: https://data.humdata.org/dataset/aruba-high-resolution-population-density-maps-demographic-estimates
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
  description: 'Aruba: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/5a6abd1f-9104-40bd-8ae4-5198ae5eacb3/resource/84479207-81df-4211-9e6f-cf4fbd39ce6e/download/abw_general_2020_csv.zip
  format: null
  id: resource_84479207
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: abw_general_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Aruba: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/5a6abd1f-9104-40bd-8ae4-5198ae5eacb3/resource/21bffed2-7cc2-4650-8107-0a0b892248ca/download/abw_general_2020_geotiff.zip
  format: null
  id: resource_21bffed2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: abw_general_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Aruba: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/5a6abd1f-9104-40bd-8ae4-5198ae5eacb3/resource/1c9eb17e-9fc7-4136-9a14-34a30608b177/download/abw_children_under_five_2020_csv.zip
  format: null
  id: resource_1c9eb17e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: abw_children_under_five_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Aruba: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/5a6abd1f-9104-40bd-8ae4-5198ae5eacb3/resource/64d514cd-d338-4c64-a279-0321a6acaed6/download/abw_children_under_five_2020_geotiff.zip
  format: null
  id: resource_64d514cd
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: abw_children_under_five_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Aruba: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/5a6abd1f-9104-40bd-8ae4-5198ae5eacb3/resource/a9bf468b-890e-437b-9215-9de4e93c4342/download/abw_elderly_60_plus_2020_csv.zip
  format: null
  id: resource_a9bf468b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: abw_elderly_60_plus_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Aruba: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/5a6abd1f-9104-40bd-8ae4-5198ae5eacb3/resource/1cffbf38-ffb6-46df-bfb2-5e868cfee1a1/download/abw_elderly_60_plus_2020_geotiff.zip
  format: null
  id: resource_1cffbf38
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: abw_elderly_60_plus_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Aruba: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/5a6abd1f-9104-40bd-8ae4-5198ae5eacb3/resource/fcb09837-45e0-44c4-af85-04891ee7ee57/download/abw_men_2020_csv.zip
  format: null
  id: resource_fcb09837
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: abw_men_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Aruba: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/5a6abd1f-9104-40bd-8ae4-5198ae5eacb3/resource/da91db7e-f11d-4a94-b86b-676eb96c001f/download/abw_men_2020_geotiff.zip
  format: null
  id: resource_da91db7e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: abw_men_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Aruba: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/5a6abd1f-9104-40bd-8ae4-5198ae5eacb3/resource/a12272bb-56ac-49f6-8139-f73ca27f0c48/download/abw_women_2020_csv.zip
  format: null
  id: resource_a12272bb
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: abw_women_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Aruba: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/5a6abd1f-9104-40bd-8ae4-5198ae5eacb3/resource/538c9151-6362-4832-89da-600fd246c033/download/abw_women_2020_geotiff.zip
  format: null
  id: resource_538c9151
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: abw_women_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Aruba: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/5a6abd1f-9104-40bd-8ae4-5198ae5eacb3/resource/9a4b9704-df00-46ab-a14a-de5aa5ad1a0b/download/abw_women_of_reproductive_age_15_49_2020_csv.zip
  format: null
  id: resource_9a4b9704
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: abw_women_of_reproductive_age_15_49_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Aruba: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/5a6abd1f-9104-40bd-8ae4-5198ae5eacb3/resource/7f002759-5a38-45e0-a1a5-6c76d2ef94ea/download/abw_women_of_reproductive_age_15_49_2020_geotiff.zip
  format: null
  id: resource_7f002759
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: abw_women_of_reproductive_age_15_49_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Aruba: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/5a6abd1f-9104-40bd-8ae4-5198ae5eacb3/resource/51d81443-7b96-4e30-a9b1-4cc7003bdee6/download/abw_youth_15_24_2020_csv.zip
  format: null
  id: resource_51d81443
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: abw_youth_15_24_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Aruba: High Resolution Population Density Maps + Demographic Estimates
    (ZIP archive)'
  download_url: https://data.humdata.org/dataset/5a6abd1f-9104-40bd-8ae4-5198ae5eacb3/resource/eca065bb-ff67-4a9a-af7c-a1e9e05a64f8/download/abw_youth_15_24_2020_geotiff.zip
  format: null
  id: resource_eca065bb
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: abw_youth_15_24_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This file has information about the cloud cover percentage and capture
    data of the satellite images used.
  download_url: https://data.humdata.org/dataset/5a6abd1f-9104-40bd-8ae4-5198ae5eacb3/resource/b7873b25-8f03-470d-a842-d9ec80afbf78/download/abw_dg_metadata.json.zip
  format: null
  id: resource_b7873b25
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: abw_dg_metadata.json.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-abw_metad4g_arubahighresolutionpopula_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - ABW
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2021-04-29'
  start: '2019-06-10'
temporal_resolution: null
title: 'Aruba: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
