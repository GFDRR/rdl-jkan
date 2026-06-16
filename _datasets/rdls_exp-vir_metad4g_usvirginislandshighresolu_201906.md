---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook/Meta AI and Data for Good
    url: https://data.humdata.org/dataset/us-virgin-islands-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/us-virgin-islands-high-resolution-population-density-maps-demographic-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/us-virgin-islands-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/us-virgin-islands-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-vir_metad4g_usvirginislandshighresolu_201906
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in US Virgin Islands: (1) Overall population
  density (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly
  (ages 60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/us-virgin-islands-high-resolution-population-density-maps-demographic-estimates]'
details: "To reference this data, please use the following citation: Facebook Connectivity\
  \ Lab and Center for International Earth Science Information Network - CIESIN -\
  \ Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery\
  \ for HRSL \xC2\xA9 2016 DigitalGlobe. Accessed DAY MONTH YEAR.' Please note that\
  \ as of 2024, Meta's high resolution population density maps are no longer being\
  \ updated."
exposure:
- asset_type:
    description: High-resolution gridded population density maps for overall population
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
license: CC-BY-4.0
lineage:
  description: High-resolution population density maps were created by applying machine
    learning algorithms to identify building footprints from commercial satellite
    imagery, then overlaying general population estimates derived from census data
    and demographic statistics in partnership with Columbia University. The resulting
    gridded datasets represent spatial distribution of overall population and seven
    demographic subgroups across US Virgin Islands.
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
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/us-virgin-islands-high-resolution-population-density-maps-demographic-estimates
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
  description: 'US Virgin Islands: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/181292bc-e289-4855-8b64-05655575117f/resource/04c30e5e-a70d-42f8-946c-cb971f81cad0/download/population_vir_2018-10-01.csv.zip
  format: null
  id: resource_04c30e5e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_vir_2018-10-01.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'US Virgin Islands: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/181292bc-e289-4855-8b64-05655575117f/resource/007396c5-724a-4c8f-a464-95bf35354a48/download/population_vir_2018-10-01.zip
  format: null
  id: resource_007396c5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: population_vir_2018-10-01.geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'US Virgin Islands: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/181292bc-e289-4855-8b64-05655575117f/resource/06ca6749-b635-4495-94ae-bad2b507a85b/download/vir_children_under_five_2019-06-01_csv.zip
  format: null
  id: resource_06ca6749
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VIR_children_under_five_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'US Virgin Islands: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/181292bc-e289-4855-8b64-05655575117f/resource/f578ae43-e725-40ec-aadb-25b85a1be8d8/download/vir_children_under_five_2019-06-01_geotiff.zip
  format: null
  id: resource_f578ae43
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VIR_children_under_five_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'US Virgin Islands: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/181292bc-e289-4855-8b64-05655575117f/resource/71cd9de7-2802-4b2e-8420-527b09a280e0/download/vir_elderly_60_plus_2019-06-01_csv.zip
  format: null
  id: resource_71cd9de7
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VIR_elderly_60_plus_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'US Virgin Islands: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/181292bc-e289-4855-8b64-05655575117f/resource/c718251a-575c-477b-b2da-08b5e2a526c9/download/vir_elderly_60_plus_2019-06-01_geotiff.zip
  format: null
  id: resource_c718251a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VIR_elderly_60_plus_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'US Virgin Islands: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/181292bc-e289-4855-8b64-05655575117f/resource/15b3e975-8328-4024-abba-cfd5f15094d5/download/vir_men_2019-06-01_csv.zip
  format: null
  id: resource_15b3e975
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VIR_men_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'US Virgin Islands: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/181292bc-e289-4855-8b64-05655575117f/resource/3339aa0a-45d4-4c8b-b9a8-91bc713a0a73/download/vir_men_2019-06-01_geotiff.zip
  format: null
  id: resource_3339aa0a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VIR_men_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'US Virgin Islands: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/181292bc-e289-4855-8b64-05655575117f/resource/46d878dc-bdfc-4e66-b25d-826b300e4741/download/vir_women_2019-06-01_csv.zip
  format: null
  id: resource_46d878dc
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VIR_women_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'US Virgin Islands: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/181292bc-e289-4855-8b64-05655575117f/resource/9f3096cf-1e67-44fd-831c-793d3946f476/download/vir_women_2019-06-01_geotiff.zip
  format: null
  id: resource_9f3096cf
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VIR_women_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'US Virgin Islands: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/181292bc-e289-4855-8b64-05655575117f/resource/363ed97e-437b-4a14-897c-2036d653e555/download/vir_women_of_reproductive_age_15_49_2019-06-01_csv.zip
  format: null
  id: resource_363ed97e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VIR_women_of_reproductive_age_15_49_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'US Virgin Islands: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/181292bc-e289-4855-8b64-05655575117f/resource/c094957c-ab96-44e0-aa93-18107d17b1ff/download/vir_women_of_reproductive_age_15_49_2019-06-01_geotiff.zip
  format: null
  id: resource_c094957c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VIR_women_of_reproductive_age_15_49_2019-06-01_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'US Virgin Islands: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/181292bc-e289-4855-8b64-05655575117f/resource/54e1464b-ec67-4a3a-9112-78db4ef02418/download/vir_youth_15_24_2019-06-01_csv.zip
  format: null
  id: resource_54e1464b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VIR_youth_15_24_2019-06-01_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'US Virgin Islands: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/181292bc-e289-4855-8b64-05655575117f/resource/08235436-d3a8-41c5-9ab7-d7502e8fd9a2/download/vir_youth_15_24_2019-06-01_geotiff.zip
  format: null
  id: resource_08235436
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VIR_youth_15_24_2019-06-01_geotiff.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-vir_metad4g_usvirginislandshighresolu_201906
spatial:
  bbox: null
  centroid: null
  countries:
  - VIR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2019-06-11'
  start: '2019-06-10'
temporal_resolution: null
title: 'US Virgin Islands: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
