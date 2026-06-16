---
attributions:
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/guadeloupe-high-resolution-population-density-maps-demographic-estimates
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/guadeloupe-high-resolution-population-density-maps-demographic-estimates
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/guadeloupe-high-resolution-population-density-maps-demographic-estimates
dataset_id: rdls_exp-glp_metad4g_guadeloupehighresolutionp_2019
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in Guadeloupe: (1) Overall population
  density (2) Women (3) Men (4) Children (ages 0-5) (5) Youth (ages 15-24) (6) Elderly
  (ages 60+) (7) Women of reproductive age (ages 15-49).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/guadeloupe-high-resolution-population-density-maps-demographic-estimates]'
details: "To reference this data, please use the following citation: Facebook Connectivity\
  \ Lab and Center for International Earth Science Information Network - CIESIN -\
  \ Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery\
  \ for HRSL \xC2\xA9 2016 DigitalGlobe. Accessed DAY MONTH YEAR.' Please note that\
  \ as of 2024, Meta's high resolution population density maps are no longer being\
  \ updated."
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
license: CC-BY-4.0
lineage:
  description: High-resolution population density maps were created by applying machine
    learning algorithms to identify building footprints from commercial satellite
    imagery, then overlaying population estimates derived from census data and demographic
    statistics through partnership with Columbia University. The resulting gridded
    datasets represent population distribution at fine spatial resolution for Guadeloupe
    in 2020, disaggregated by demographic subgroups.
  sources:
  - id: source_1
    license: null
    name: AI and Data for Good at Meta
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
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/guadeloupe-high-resolution-population-density-maps-demographic-estimates
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
  description: 'Guadeloupe: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/48ae3cdf-2a66-45ec-9388-1144c10a2e44/resource/3b3842f2-7b47-4455-8041-6e7368203c58/download/glp_general_2020_csv.zip
  format: null
  id: resource_3b3842f2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: glp_general_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guadeloupe: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/48ae3cdf-2a66-45ec-9388-1144c10a2e44/resource/efa1e8a6-ab6c-4911-a947-273bb737d022/download/glp_general_2020_geotiff.zip
  format: null
  id: resource_efa1e8a6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: glp_general_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guadeloupe: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/48ae3cdf-2a66-45ec-9388-1144c10a2e44/resource/c8637485-be23-40e0-a4c8-c818d3f3284b/download/glp_children_under_five_2020_csv.zip
  format: null
  id: resource_c8637485
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: glp_children_under_five_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guadeloupe: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/48ae3cdf-2a66-45ec-9388-1144c10a2e44/resource/88bbf40a-e532-43fb-a4ed-259e891d2cd0/download/glp_children_under_five_2020_geotiff.zip
  format: null
  id: resource_88bbf40a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: glp_children_under_five_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guadeloupe: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/48ae3cdf-2a66-45ec-9388-1144c10a2e44/resource/9da5ee28-094e-4ecd-94a0-3b48bcf4149c/download/glp_general_2020_csv.zip
  format: null
  id: resource_9da5ee28
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: glp_general_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guadeloupe: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/48ae3cdf-2a66-45ec-9388-1144c10a2e44/resource/eb01ce7f-a43c-47be-8053-3bacb359ab3f/download/glp_elderly_60_plus_2020_geotiff.zip
  format: null
  id: resource_eb01ce7f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: glp_elderly_60_plus_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guadeloupe: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/48ae3cdf-2a66-45ec-9388-1144c10a2e44/resource/20944e24-2fc3-4cf8-b3ce-474a1fb436cc/download/glp_men_2020_csv.zip
  format: null
  id: resource_20944e24
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: glp_men_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guadeloupe: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/48ae3cdf-2a66-45ec-9388-1144c10a2e44/resource/f7f7a28b-579d-44df-bbe0-cbf075333872/download/glp_men_2020_geotiff.zip
  format: null
  id: resource_f7f7a28b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: glp_men_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guadeloupe: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/48ae3cdf-2a66-45ec-9388-1144c10a2e44/resource/ee392bda-98a4-4321-8273-94884a64b949/download/glp_women_2020_csv.zip
  format: null
  id: resource_ee392bda
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: glp_women_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guadeloupe: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/48ae3cdf-2a66-45ec-9388-1144c10a2e44/resource/00d52422-cda9-4d47-a696-b2d60c19ddb6/download/glp_women_2020_geotiff.zip
  format: null
  id: resource_00d52422
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: glp_women_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guadeloupe: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/48ae3cdf-2a66-45ec-9388-1144c10a2e44/resource/6488889e-63d6-4d39-b41a-10caeda70c87/download/glp_women_of_reproductive_age_15_49_2020_csv.zip
  format: null
  id: resource_6488889e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: glp_women_of_reproductive_age_15_49_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guadeloupe: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/48ae3cdf-2a66-45ec-9388-1144c10a2e44/resource/a4d5511d-667a-49ac-820b-e94e70e88250/download/glp_women_of_reproductive_age_15_49_2020_geotiff.zip
  format: null
  id: resource_a4d5511d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: glp_women_of_reproductive_age_15_49_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guadeloupe: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/48ae3cdf-2a66-45ec-9388-1144c10a2e44/resource/aea621c3-134c-4884-8c96-39465b67971d/download/glp_youth_15_24_2020_csv.zip
  format: null
  id: resource_aea621c3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: glp_youth_15_24_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guadeloupe: High Resolution Population Density Maps + Demographic
    Estimates (ZIP archive)'
  download_url: https://data.humdata.org/dataset/48ae3cdf-2a66-45ec-9388-1144c10a2e44/resource/708dc7be-7d99-4051-a858-41d73413893d/download/glp_youth_15_24_2020_geotiff.zip
  format: null
  id: resource_708dc7be
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: glp_youth_15_24_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This file has information about the cloud cover percentage and capture
    data of the satellite images used.
  download_url: https://data.humdata.org/dataset/48ae3cdf-2a66-45ec-9388-1144c10a2e44/resource/97e6d975-464b-4c42-84fb-fce5205c686a/download/glp_dg_metadata.json.zip
  format: null
  id: resource_97e6d975
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: glp_dg_metadata.json.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-glp_metad4g_guadeloupehighresolutionp_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - GLP
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2021-05-18'
  start: '2019-06-10'
temporal_resolution: null
title: 'Guadeloupe: High Resolution Population Density Maps + Demographic Estimates'
version: null
vulnerability: null
---
