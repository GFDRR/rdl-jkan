---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook/Meta AI and Data for Good
    url: https://data.humdata.org/dataset/united-states-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/united-states-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: US Census Data
    url: https://data.humdata.org/dataset/united-states-high-resolution-population-density-maps-demographic-estimates
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/united-states-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/united-states-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-usa_metad4g_highresolutionpopulationd_2019
description: 'These high-resolution maps estimate not only the number of people living
  within 30-meter grid tiles, but also provide insights on demographics at unprecedentedly
  high resolutions. These maps aren''t built using Facebook data and instead rely
  on combining the power of machine vision AI with satellite imagery and census information..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/united-states-high-resolution-population-density-maps-demographic-estimates]'
details: "To reference this data, please use the following citation: Facebook Connectivity\
  \ Lab and Center for International Earth Science Information Network - CIESIN -\
  \ Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery\
  \ for HRSL \xC2\xA9 2016 DigitalGlobe. Accessed DAY MONTH YEAR.' Please note that\
  \ as of 2024, Meta's high resolution population density maps are no longer being\
  \ updated."
exposure:
- asset_type:
    description: High-resolution gridded population estimates (30-meter resolution)
      disaggregated by demographic groups including children under five, elderly 60+,
      women, men, and youth
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
    footprints, then overlaying population estimates derived from US Census data and
    other public demographic sources. The resulting 30-meter gridded dataset provides
    population counts disaggregated by age groups (children under five, elderly 60+)
    and gender (women, men, youth) across the United States.
  sources:
  - id: source_1
    license: null
    name: Facebook/Meta AI and Data for Good
    risk_data_type:
    - exposure
    type: model
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
  - id: source_3
    license: null
    name: US Census Data
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/united-states-high-resolution-population-density-maps-demographic-estimates
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
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/d5553a2f-f043-4960-abe6-54d3d950ae0c/download/usa_lat_24_lon_-81_children_under_five_geotiff.zip
  format: null
  id: resource_d5553a2f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: USA_lat_24_lon_-81_children_under_five_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/0cd39fc5-67f6-44e4-81a8-36d43b782f31/download/usa_lat_24_lon_-111_children_under_five_geotiff.zip
  format: null
  id: resource_0cd39fc5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: USA_lat_24_lon_-111_children_under_five_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/29c0d810-0832-40ea-88b5-66c459fa21fc/download/usa_lat_24_lon_-141_children_under_five_geotiff.zip
  format: null
  id: resource_29c0d810
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: USA_lat_24_lon_-141_children_under_five_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/9e549970-3834-446f-a047-3524a7f88cf2/download/usa_lat_54_lon_-141_children_under_five_geotiff.zip
  format: null
  id: resource_9e549970
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: USA_lat_54_lon_-141_children_under_five_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/5e65a2b1-db6d-412c-828d-2fa478edfa59/download/usa_lat_54_lon_-171_children_under_five_geotiff.zip
  format: null
  id: resource_5e65a2b1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: USA_lat_54_lon_-171_children_under_five_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/ab84b4da-a370-4684-bfd9-627231f87e12/download/usa_lat_24_lon_-81_elderly_60_plus_geotiff.zip
  format: null
  id: resource_ab84b4da
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: USA_lat_24_lon_-81_elderly_60_plus_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/9f500491-488d-48bc-8ddc-6e4561419175/download/usa_lat_24_lon_-111_elderly_60_plus_geotiff.zip
  format: null
  id: resource_9f500491
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: USA_lat_24_lon_-111_elderly_60_plus_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/67f17448-ba63-4461-98e1-556d36422eb2/download/usa_lat_24_lon_-141_elderly_60_plus_geotiff.zip
  format: null
  id: resource_67f17448
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: USA_lat_24_lon_-141_elderly_60_plus_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/e256cc5b-2f50-4b77-b809-737176e21c0d/download/usa_lat_54_lon_-141_elderly_60_plus_geotiff.zip
  format: null
  id: resource_e256cc5b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: USA_lat_54_lon_-141_elderly_60_plus_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/de121a45-da2c-4386-9fc9-c57c954b85c0/download/usa_lat_54_lon_-171_elderly_60_plus_geotiff.zip
  format: null
  id: resource_de121a45
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: USA_lat_54_lon_-171_elderly_60_plus_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/512a64fa-83cf-4590-92ef-d700fecbf1ad/download/usa_lat_24_lon_-81_men_geotiff.zip
  format: null
  id: resource_512a64fa
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: USA_lat_24_lon_-81_men_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/561a505b-afd4-487d-83eb-c7efdbf4f945/download/usa_lat_24_lon_-111_men_geotiff.zip
  format: null
  id: resource_561a505b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: USA_lat_24_lon_-111_men_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/3ebe7740-c537-4bec-95d0-4d0bce9932c0/download/usa_lat_24_lon_-141_men_geotiff.zip
  format: null
  id: resource_3ebe7740
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: USA_lat_24_lon_-141_men_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/c0cc7344-4f55-4bf8-90cb-d0d99705267d/download/usa_lat_54_lon_-141_men_geotiff.zip
  format: null
  id: resource_c0cc7344
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: USA_lat_54_lon_-141_men_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/3dc0b8af-9ac0-476a-bb78-64034244c80a/download/usa_lat_54_lon_-171_men_geotiff.zip
  format: null
  id: resource_3dc0b8af
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: USA_lat_54_lon_-171_men_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/e430ddf2-9cdd-48a4-932f-e58c3da88f6a/download/usa_lat_24_lon_-81_women_geotiff.zip
  format: null
  id: resource_e430ddf2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: USA_lat_24_lon_-81_women_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/ad28f6be-303b-4f1c-82ff-df9b67072453/download/usa_lat_24_lon_-111_women_geotiff.zip
  format: null
  id: resource_ad28f6be
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: USA_lat_24_lon_-111_women_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/cf6ecb3e-6d7a-4e36-b04c-bc5b9f67191b/download/usa_lat_24_lon_-141_women_geotiff.zip
  format: null
  id: resource_cf6ecb3e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: USA_lat_24_lon_-141_women_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/27c39706-c98a-422c-892d-f3d4ee3dc568/download/usa_lat_54_lon_-141_women_geotiff.zip
  format: null
  id: resource_27c39706
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: USA_lat_54_lon_-141_women_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/536d1ec5-4ebb-4242-89ab-f0ed4c2202de/download/usa_lat_54_lon_-171_women_geotiff.zip
  format: null
  id: resource_536d1ec5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: USA_lat_54_lon_-171_women_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/704b3c9d-2f6f-4cf9-8de9-bc40617096d0/download/usa_lat_24_lon_-81_women_of_reproductive_age_15_49_geotiff.zip
  format: null
  id: resource_704b3c9d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: USA_lat_24_lon_-81_women_of_reproductive_age_15_49_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/6ee06784-220d-49c0-b40b-2e406bc0a746/download/usa_lat_24_lon_-111_women_of_reproductive_age_15_49_geotiff.zip
  format: null
  id: resource_6ee06784
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: USA_lat_24_lon_-111_women_of_reproductive_age_15_49_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/a795af88-e4b8-4fe9-b085-cf487ba14408/download/usa_lat_24_lon_-141_women_of_reproductive_age_15_49_geotiff.zip
  format: null
  id: resource_a795af88
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: USA_lat_24_lon_-141_women_of_reproductive_age_15_49_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/3ec532c0-cded-4714-91ad-2fe5241aefc2/download/usa_lat_54_lon_-141_women_of_reproductive_age_15_49_geotiff.zip
  format: null
  id: resource_3ec532c0
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: USA_lat_54_lon_-141_women_of_reproductive_age_15_49_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/c0aefe69-cbb4-4f5f-8637-3ca0ab203cfa/download/usa_lat_54_lon_-171_women_of_reproductive_age_15_49_geotiff.zip
  format: null
  id: resource_c0aefe69
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: USA_lat_54_lon_-171_women_of_reproductive_age_15_49_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/3486653b-5ea6-44dc-a0ad-ed27ab520cac/download/usa_lat_24_lon_-81_youth_15_24_geotiff.zip
  format: null
  id: resource_3486653b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: USA_lat_24_lon_-81_youth_15_24_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/ef16d014-b308-411b-aada-5902c9f2635f/download/usa_lat_24_lon_-111_youth_15_24_geotiff.zip
  format: null
  id: resource_ef16d014
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: USA_lat_24_lon_-111_youth_15_24_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/60d485de-1de8-40f1-bde7-ece18128aa31/download/usa_lat_24_lon_-141_youth_15_24_geotiff.zip
  format: null
  id: resource_60d485de
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: USA_lat_24_lon_-141_youth_15_24_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/cbdc06c3-7489-4872-8e27-863316e2223a/download/usa_lat_54_lon_-141_youth_15_24_geotiff.zip
  format: null
  id: resource_cbdc06c3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: USA_lat_54_lon_-141_youth_15_24_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/a884f137-3ff5-45ad-80cb-d1169ee5cbd3/download/usa_lat_54_lon_-171_youth_15_24_geotiff.zip
  format: null
  id: resource_a884f137
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: USA_lat_54_lon_-171_youth_15_24_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Because the US is so large, we've split the US into 10 by 10 degree
    chunks and combined them into a single VRT file . The 10 by 10 degree chunks are
    represented by the Geotiff files named 'population_usa'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/e6219fb1-3093-4170-ae79-b4469729d10e/download/population_usa_2019-07-01.vrt
  format: GDAL Virtual Format
  id: resource_e6219fb1
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_usa_2019-07-01.vrt
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (total population)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/45c596b5-a8fd-4b7a-97f0-245235f68cbd/download/population_usa18_-90_2019-07-01.tif.zip
  format: null
  id: resource_45c596b5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_usa18_-90.tif.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (total population)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/0ccda306-9f61-47f9-99e6-6b733e09c534/download/population_usa18_-100_2019-07-01.tif.zip
  format: null
  id: resource_0ccda306
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_usa18_-100.tif.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (total population)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/573c8249-86eb-482f-8474-cd6a785d2799/download/population_usa18_-110_2019-07-01.tif.zip
  format: null
  id: resource_573c8249
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_usa18_-110.tif.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (total population)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/c6d830a9-b608-4aaa-816a-cc70a2ba1065/download/population_usa18_-160_2019-07-01.tif.zip
  format: null
  id: resource_c6d830a9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_usa18_-160.tif.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (total population)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/7342cb9f-8f16-4112-83a6-d6f977e0b272/download/population_usa18_-170_2019-07-01.tif.zip
  format: null
  id: resource_7342cb9f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_usa18_-170.tif.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (total population)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/8b8f142a-0f3c-40ae-8bb5-268df8f0ad39/download/population_usa18_-180_2019-07-01.tif.zip
  format: null
  id: resource_8b8f142a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_usa18_-180.tif.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (total population)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/114f921c-a821-4067-974f-0482c58b90f7/download/population_usa28_-80_2019-07-01.tif.zip
  format: null
  id: resource_114f921c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_usa28_-80.tif.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (total population)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/42fbf8eb-cf6b-4f52-8d9d-5f2edc2aed8a/download/population_usa28_-90_2019-07-01.tif.zip
  format: null
  id: resource_42fbf8eb
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_usa28_-90..tif.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (total population)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/706c6d80-5b5b-4e0a-b78d-947dbfa9d2c2/download/population_usa28_-100_2019-07-01.tif.zip
  format: null
  id: resource_706c6d80
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_usa28_-100.tif.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (total population)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/34fdc010-726e-4585-b78f-d38162e254f9/download/population_usa28_-110_2019-07-01.tif.zip
  format: null
  id: resource_34fdc010
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_usa28_-110.tif.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (total population)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/58b480a3-afbd-4d1e-bd9f-5ef480bffb61/download/population_usa28_-120_2019-07-01.tif.zip
  format: null
  id: resource_58b480a3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_usa28_-120.tif.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (total population)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/619aef38-7ab3-4dff-bcc6-35d4ddef0a26/download/population_usa28_-130_2019-07-01.tif.zip
  format: null
  id: resource_619aef38
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_usa28_-130.tif.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (total population)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/6f0b12da-ba9c-4a54-8dc9-f6c3beb71547/download/population_usa38_-70_2019-07-01.tif.zip
  format: null
  id: resource_6f0b12da
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_usa38_-70.tif.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (total population)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/35a6f8c3-4234-4143-9016-103af7c50876/download/population_usa38_-80_2019-07-01.tif.zip
  format: null
  id: resource_35a6f8c3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_usa38_-80.tif.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (total population)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/2f888946-e654-4c17-8885-fa1c09992fc2/download/population_usa38_-90_2019-07-01.tif.zip
  format: null
  id: resource_2f888946
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_usa38_-90.tif.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (total population)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/5432da52-fe0c-4817-98ad-f315d64b7f46/download/population_usa38_-100_2019-07-01.tif.zip
  format: null
  id: resource_5432da52
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_usa38_-100.tif.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (total population)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/d3e68448-261f-4be6-8b4d-4c4e4b1dbc7a/download/population_usa38_-110_2019-07-01.tif.zip
  format: null
  id: resource_d3e68448
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_usa38_-110.tif.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (total population)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/d68537c2-c0d3-41b1-9c9d-3aabd59ef783/download/population_usa38_-120_2019-07-01.tif.zip
  format: null
  id: resource_d68537c2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_usa38_-120.tif.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (total population)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/94169896-44c8-436b-bbb0-4b56d5ed9e17/download/population_usa38_-130_2019-07-01.tif.zip
  format: null
  id: resource_94169896
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_usa38_-130.tif.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (total population)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/be92a7f3-a505-4e3c-aa20-4ca7e3ef4d3d/download/population_usa48_-100_2019-07-01.tif.zip
  format: null
  id: resource_be92a7f3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_usa48_-100.tif.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (total population)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/9fdac93d-9648-410a-ba0f-b77e9225e75e/download/population_usa48_-110_2019-07-01.tif.zip
  format: null
  id: resource_9fdac93d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_usa48_-110.tif.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (total population)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/1fbe6572-5a4b-4af0-87df-fbc363bd2d22/download/population_usa48_-120_2019-07-01.tif.zip
  format: null
  id: resource_1fbe6572
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_usa48_-120.tif.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (total population)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/032b05a1-dcdf-4505-be5b-8b33ce62d4d7/download/population_usa48_-130_2019-07-01.tif.zip
  format: null
  id: resource_032b05a1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_usa48_-130.tif.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (total population)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/5494d5dc-00bb-4f2d-ba02-eb3f72b764bb/download/population_usa48_-140_2019-07-01.tif.zip
  format: null
  id: resource_5494d5dc
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_usa48_-140.tif.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (total population)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/1b954076-fc89-4824-8fe5-e18da4bf7213/download/population_usa48_177_2019-07-01.tif.zip
  format: null
  id: resource_1b954076
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_usa48_177.tif.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (total population)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/66367c0c-34ac-4216-8408-f25db464682e/download/population_usa58_-140_2019-07-01.tif.zip
  format: null
  id: resource_66367c0c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_usa58_-140.tif.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (total population)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/34d243c4-4cc6-49ef-a129-b07702bccd58/download/population_usa58_-150_2019-07-01.tif.zip
  format: null
  id: resource_34d243c4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_usa58_-150.tif.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (total population)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/11b59394-81d6-4c60-9881-4f785999f35a/download/population_usa58_-160_2019-07-01.tif.zip
  format: null
  id: resource_11b59394
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_usa58_-160.tif.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (total population)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/f2cab162-8f04-4ac7-9d0f-d96c191f1fe6/download/population_usa58_-170_2019-07-01.tif.zip
  format: null
  id: resource_f2cab162
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_usa58_-170.tif.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (total population)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/837b68f3-5e1e-4884-bfad-1557f7345bda/download/population_usa68_-150_2019-07-01.tif.zip
  format: null
  id: resource_837b68f3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_usa68_-150.tif.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (total population)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/c2bdebaa-56d2-4c47-a27a-b341e9b71216/download/population_usa68_-160_2019-07-01.tif.zip
  format: null
  id: resource_c2bdebaa
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_usa68_-160.tif.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (total population)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/787d86c0-c37e-4541-8104-4ab67e99c0d3/download/population_usa68_-170_2019-07-01.tif.zip
  format: null
  id: resource_787d86c0
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_usa68_-170.tif.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/b2ddc964-4df9-4d96-8c13-73128ecebf8d/download/usa_children_under_five_2020-03-07_csv.zip
  format: null
  id: resource_b2ddc964
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: USA_children_under_five.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/2266523b-fa34-4975-80bc-ef8b6e5fe918/download/usa_elderly_60_plus_2020-03-07_csv.zip
  format: null
  id: resource_2266523b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: USA_elderly_60_plus.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/f26d5628-f06c-483b-a18f-f12a9e922bed/download/usa_youth_15_24_2020-03-07_csv.zip
  format: null
  id: resource_f26d5628
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: USA_youth_15_24.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/3b81373e-88d5-461e-9655-842dbaec51ae/download/usa_men_2020-03-07_part_1_of_2.csv.zip
  format: null
  id: resource_3b81373e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: USA_men.part_1_of_2.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/d8fb6565-c140-457b-bac5-bc0d5fa1078c/download/usa_men_2020-03-07_part_2_of_2.csv.zip
  format: null
  id: resource_d8fb6565
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: USA_men.part_2_of_2.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/97806ee2-8992-45ef-92a9-457159a2331c/download/usa_women_2020-03-07_part_1_of_2.csv.zip
  format: null
  id: resource_97806ee2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: USA_women.part_1_of_2.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/41109122-0b19-496d-9385-d814b8a1bf5c/download/usa_women_2020-03-07_part_2_of_2.csv.zip
  format: null
  id: resource_41109122
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: USA_women.part_2_of_2.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/5ca1fc62-ab77-4760-8b4f-cb30efb3a48c/download/usa_women_of_reproductive_age_15_49_2020-03-07_part_1_of_2.csv.zip
  format: null
  id: resource_5ca1fc62
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: USA_women_of_reproductive_age_15_49.part_1_of_2.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/fa75836f-f7fd-42fe-b0a9-09964c212721/download/usa_women_of_reproductive_age_15_49_2020-03-07_part_2_of_2.csv.zip
  format: null
  id: resource_fa75836f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: USA_women_of_reproductive_age_15_49.part_2_of_2.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (total population)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/bfaf3b10-ee9a-44c0-9754-79f534704c80/download/population_usa_2019-07-01_part_1_of_6.csv.zip
  format: null
  id: resource_bfaf3b10
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_usa.part_1_of_6.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (total population)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/4a30bd5c-c896-4486-922d-1dffc0d98dd2/download/population_usa_2019-07-01_part_2_of_6.csv.zip
  format: null
  id: resource_4a30bd5c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_usa.part_2_of_6.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (total population)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/9f61c00b-d577-42cd-9bdd-67b4fa5ddd4f/download/population_usa_2019-07-01_part_3_of_6.csv.zip
  format: null
  id: resource_9f61c00b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_usa.part_3_of_6.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (total population)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/024f8957-c593-459e-b46b-8d037e7d268f/download/population_usa_2019-07-01_part_4_of_6.csv.zip
  format: null
  id: resource_024f8957
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_usa.part_4_of_6.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (total population)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/f7fb92d0-3974-4b50-ae6e-445b21d6a005/download/population_usa_2019-07-01_part_5_of_6.csv.zip
  format: null
  id: resource_f7fb92d0
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_usa.part_5_of_6.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States: High Resolution Population Density Maps + Demographic
    Estimates (total population)'
  download_url: https://data.humdata.org/dataset/eec3a01f-5237-4896-8059-a6be193ca964/resource/96605291-a317-4214-9c0a-4d78443542bc/download/population_usa_2019-07-01_part_6_of_6.csv.zip
  format: null
  id: resource_96605291
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_usa.part_6_of_6.csv.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-usa_metad4g_highresolutionpopulationd_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - USA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-04-17'
  start: '2019-09-19'
temporal_resolution: null
title: 'United States: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
