---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: "ETH Z\xFCrich, Photogrammetry and Remote Sensing"
  url: https://data.humdata.org/dataset/pomelo-tanzania-high-resolution-population
creator:
  affiliation: null
  email: null
  name: "ETH Z\xFCrich, Photogrammetry and Remote Sensing"
  url: https://data.humdata.org/dataset/pomelo-tanzania-high-resolution-population
dataset_id: rdls_exp-tza_ethzprs_pomelohighresolutionpopul_2020
description: 'This dataset presents a fine-grained population map of Tanzania with
  a resolution of 100 meters for 2020, generated using the POMELO super-resolution
  technique that is based on deep learning. Please refer to our Nature Scientific
  Reports publication for more details. Background: Traditionally, many countries,
  including those in sub-Saharan Africa, rely on aggregated census data over expansive
  spatial units, which are not always timely or accurate. The need for detailed population
  maps is paramount in several sectors, including urban development, environmental
  supervision, public health, and humanitarian initiatives. Addressing this gap, the
  POMELO methodology leverages coarse census data in conjunction with open geodata
  to produce high precision population maps. Key Features: Resolution: The map offers
  a granular view with a 100m ground sampling distance, providing intricate details
  about population distributions in Tanzania. Data Sources: Utilizing a combination
  of projected admisistrative census data (UN), and supplementing it with open geodata.
  Reliability: In comparative experiments conducted in sub-Saharan Africa, POMELO''s
  ability to disaggregate coarse census counts achieved R2 values of 85-89%. Furthermore,
  its potential to predict population numbers without any census data reached accuracy
  levels of 48-69%.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/pomelo-tanzania-high-resolution-population]'
details: null
exposure:
- asset_type:
    description: High-resolution gridded population density map of Tanzania at 100m
      resolution for 2020
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
  description: Fine-grained population map generated using POMELO super-resolution
    deep learning technique applied to census and remote sensing data to produce 100-meter
    resolution population density grids for Tanzania in 2020, addressing the need
    for detailed spatial population data in sub-Saharan Africa.
  sources:
  - id: source_1
    license: null
    name: "ETH Z\xFCrich, Photogrammetry and Remote Sensing"
    risk_data_type:
    - exposure
    type: null
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/pomelo-tanzania-high-resolution-population
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
  url: https://www.nature.com/articles/s41598-022-24495-w
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: POMELO - Tanzania High Resolution Population Density (Georeferenced
    Tiff raster)
  download_url: https://data.humdata.org/dataset/b2146b6f-8267-464f-8bda-efdf2f62f41a/resource/08da2c38-c179-46a8-8ce3-6e7488b06720/download/tza_pomelo.tiff
  format: null
  id: resource_08da2c38
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tza_pomelo.tiff
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-tza_ethzprs_pomelohighresolutionpopul_2020
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
  end: '2020-12-31'
  start: '2020-01-01'
temporal_resolution: null
title: POMELO - Tanzania High Resolution Population Density
version: null
vulnerability: null
---
