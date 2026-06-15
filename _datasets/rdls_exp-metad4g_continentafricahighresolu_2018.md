---
attributions:
- entity:
    affiliation: null
    email: null
    name: Columbia University
    url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps
creator:
  affiliation: null
  email: null
  name: AI and Data for Good at Meta
  url: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps
dataset_id: rdls_exp-metad4g_continentafricahighresolu_2018
description: 'This zip file contains 28 cloud optimized tiff files that cover the
  continent of Africa. Each of the 28 files represents a region or area - these are
  not divided by country. Notes: The country-by-country files that were previously
  hosted here have been moved into separate datasets. You can find all of them here
  . South Sudan, Sudan, Somalia and Ethiopia are intentionally omitted from this dataset.
  However, a country-level dataset for Ethiopia can be found here . These 28 tiff
  files represent 2015 population estimates. However, please note that many of the
  country-level files include 2020 population estimates including: Angola, Benin,
  Botswana, Burundi, Cameroon, Cabo Verde, Cote d''Ivoire, Djibouti, Eritrea, Eswatini,
  The Gambia, Ghana, Lesotho, Liberia, Mozambique, Namibia, Sao Tome & Principe, Sierra
  Leone, South Africa, Togo, Zambia, and Zimbabwe.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps]'
details: "To reference this data, please use the following citation: Facebook Connectivity\
  \ Lab and Center for International Earth Science Information Network - CIESIN -\
  \ Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery\
  \ for HRSL \xC2\xA9 2016 DigitalGlobe. Accessed DAY MONTH YEAR.'"
exposure:
- asset_type:
    description: High-resolution gridded population density estimates derived from
      satellite imagery and census data across Africa
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
    learning algorithms to identify buildings from commercial satellite imagery, then
    overlaying general population estimates derived from publicly available census
    data and demographic statistics. The resulting cloud-optimized GeoTIFF files provide
    gridded population density across 28 African regions at continental scale.
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
- href: https://data.humdata.org/dataset/highresolutionpopulationdensitymaps
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
  description: This zip file contains 28 cloud optimized tiff files that cover the
    continent of Africa. Each of the 28 files represents a region or area - these
    are not divided by country.
  download_url: https://data.humdata.org/dataset/dbd7b22d-7426-4eb0-b3c4-faa29a87f44b/resource/7b3ef0ae-a37d-4a42-a2c9-6b111e592c2c/download/population_af_2018-10-01.zip
  format: null
  id: resource_7b3ef0ae
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: All Files - Africa High Resolution Population Density.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-metad4g_continentafricahighresolu_2018
spatial:
  bbox: null
  centroid: null
  countries:
  - DZA
  - AGO
  - BEN
  - BWA
  - BFA
  - BDI
  - CMR
  - CPV
  - CAF
  - TCD
  - COM
  - COG
  - COD
  - CIV
  - DJI
  - EGY
  - GNQ
  - ERI
  - SWZ
  - ETH
  - GAB
  - GMB
  - GHA
  - GIN
  - GNB
  - KEN
  - LSO
  - LBR
  - LBY
  - MDG
  - MWI
  - MLI
  - MRT
  - MUS
  - MAR
  - MOZ
  - NAM
  - NER
  - NGA
  - RWA
  - STP
  - SEN
  - SYC
  - SLE
  - ZAF
  - SSD
  - TZA
  - TGO
  - TUN
  - UGA
  - ZMB
  - ZWE
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2019-04-08'
  start: '2018-10-01'
temporal_resolution: null
title: 'Continent of Africa: High Resolution Population Density Maps'
version: null
vulnerability: null
---
