---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook/Meta AI and Data for Good
    url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-cod
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-cod
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-cod
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-cod
dataset_id: rdls_exp-cod_metad4g_highresolutionpopulationd_2019
description: 'The world''s most accurate population datasets. Seven maps/datasets
  for the distribution of various populations in the Democratic Republic of Congo:
  (1) Overall population density (2) Women (3) Men (4) Children (ages 0-5) (5) Youth
  (ages 15-24) (6) Elderly (ages 60+) (7) Women of reproductive age (ages 15-49)..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-cod]'
details: "To reference this data, please use the following citation: Facebook Connectivity\
  \ Lab and Center for International Earth Science Information Network - CIESIN -\
  \ Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery\
  \ for HRSL \xC2\xA9 2016 DigitalGlobe. Accessed DAY MONTH YEAR.' Please note that\
  \ as of 2024, Meta's high resolution population density maps are no longer being\
  \ updated."
exposure:
- asset_type:
    description: High-resolution gridded population density estimates for overall
      population and demographic subgroups (children 0-5, youth 15-24, elderly 60+,
      women, men, women of reproductive age 15-49)
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
    imagery, then overlaying general population estimates derived from census data
    and demographic statistics in partnership with Columbia University. The resulting
    gridded datasets provide spatial distribution of overall population and seven
    demographic subgroups across the Democratic Republic of Congo at high spatial
    resolution.
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
- href: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps-cod
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
  description: 'Democratic Republic of the Congo: High Resolution Population Density
    Maps + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/81932f5a-4aa5-4c72-b085-3bde5fef349c/resource/3ebb292c-ee44-48f9-9cb8-6d1e51b99553/download/cod_general_2020_csv.zip
  format: zip
  id: resource_3ebb292c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cod_general_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: High Resolution Population Density
    Maps + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/81932f5a-4aa5-4c72-b085-3bde5fef349c/resource/51687557-2934-4d90-98a6-f604a856fdaa/download/cod_general_2020_geotiff.zip
  format: zip
  id: resource_51687557
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cod_general_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: High Resolution Population Density
    Maps + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/81932f5a-4aa5-4c72-b085-3bde5fef349c/resource/966ed488-3282-45f8-a6f1-5abaadc41783/download/cod_children_under_five_2020_csv.zip
  format: zip
  id: resource_966ed488
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cod_children_under_five_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: High Resolution Population Density
    Maps + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/81932f5a-4aa5-4c72-b085-3bde5fef349c/resource/9c1d5c79-e9e3-4ac1-beda-b484f6d23688/download/cod_children_under_five_2020_geotiff.zip
  format: zip
  id: resource_9c1d5c79
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cod_children_under_five_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: High Resolution Population Density
    Maps + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/81932f5a-4aa5-4c72-b085-3bde5fef349c/resource/649cfd6a-3de1-43fb-a435-8a23473b4565/download/cod_elderly_60_plus_2020_csv.zip
  format: zip
  id: resource_649cfd6a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cod_elderly_60_plus_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: High Resolution Population Density
    Maps + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/81932f5a-4aa5-4c72-b085-3bde5fef349c/resource/b3127b71-cfac-49ac-ad12-6702368bd459/download/cod_elderly_60_plus_2020_geotiff.zip
  format: zip
  id: resource_b3127b71
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cod_elderly_60_plus_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: High Resolution Population Density
    Maps + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/81932f5a-4aa5-4c72-b085-3bde5fef349c/resource/89bcd8f9-2b32-4b61-9538-671f8e660123/download/cod_men_2020_csv.zip
  format: zip
  id: resource_89bcd8f9
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cod_men_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: High Resolution Population Density
    Maps + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/81932f5a-4aa5-4c72-b085-3bde5fef349c/resource/6cc2b973-fd23-4b16-a6f4-40d3e5d3194f/download/cod_men_2020_geotiff.zip
  format: zip
  id: resource_6cc2b973
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cod_men_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: High Resolution Population Density
    Maps + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/81932f5a-4aa5-4c72-b085-3bde5fef349c/resource/26481d5f-2d7b-433d-9679-eeadf44aa899/download/cod_women_2020_csv.zip
  format: zip
  id: resource_26481d5f
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cod_women_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: High Resolution Population Density
    Maps + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/81932f5a-4aa5-4c72-b085-3bde5fef349c/resource/815e5715-9d47-462a-810a-0dae2759dea0/download/cod_women_2020_geotiff.zip
  format: zip
  id: resource_815e5715
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cod_women_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: High Resolution Population Density
    Maps + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/81932f5a-4aa5-4c72-b085-3bde5fef349c/resource/e6d3accd-e6db-4ca4-ad55-56bb12b20754/download/cod_women_of_reproductive_age_15_49_2020_csv.zip
  format: zip
  id: resource_e6d3accd
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cod_women_of_reproductive_age_15_49_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: High Resolution Population Density
    Maps + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/81932f5a-4aa5-4c72-b085-3bde5fef349c/resource/53eb1909-4700-442c-ad55-ca023f69cce3/download/cod_women_of_reproductive_age_15_49_2020_geotiff.zip
  format: zip
  id: resource_53eb1909
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cod_women_of_reproductive_age_15_49_2020_geotiff.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: High Resolution Population Density
    Maps + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/81932f5a-4aa5-4c72-b085-3bde5fef349c/resource/f37ff34e-2e9f-4216-8669-a3d171cc1660/download/cod_youth_15_24_2020_csv.zip
  format: zip
  id: resource_f37ff34e
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cod_youth_15_24_2020_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: High Resolution Population Density
    Maps + Demographic Estimates (zip)'
  download_url: https://data.humdata.org/dataset/81932f5a-4aa5-4c72-b085-3bde5fef349c/resource/2662435d-346a-4c78-b07e-5d4a8db7aefe/download/cod_youth_15_24_2020_geotiff.zip
  format: zip
  id: resource_2662435d
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cod_youth_15_24_2020_geotiff.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-cod_metad4g_highresolutionpopulationd_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - COD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2021-11-25'
  start: '2019-05-20'
temporal_resolution: null
title: 'Democratic Republic of the Congo: High Resolution Population Density Maps
  + Demographic Estimates'
version: null
vulnerability: null
---
