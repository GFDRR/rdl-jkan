---
attributions:
- entity:
    affiliation: null
    email: null
    name: POMELO super-resolution technique
    url: https://data.humdata.org/dataset/pomelo-rwanda-high-resolution-population
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: "ETH Z\xFCrich, Photogrammetry and Remote Sensing"
  url: https://data.humdata.org/dataset/pomelo-rwanda-high-resolution-population
creator:
  affiliation: null
  email: null
  name: "ETH Z\xFCrich, Photogrammetry and Remote Sensing"
  url: https://data.humdata.org/dataset/pomelo-rwanda-high-resolution-population
dataset_id: rdls_exp-rwa_ethzprs_pomelohighresolutionpopul_2020
description: 'This dataset presents a fine-grained population map of Rwanda with a
  resolution of 100 meters for 2020, generated using the POMELO super-resolution technique
  that is based on deep learning. Please refer to our Nature Scientific Reports publication
  for more details. Background: Traditionally, many countries, including those in
  sub-Saharan Africa, rely on aggregated census data over expansive spatial units,
  which are not always timely or accurate. The need for detailed population maps is
  paramount in several sectors, including urban development, environmental supervision,
  public health, and humanitarian initiatives. Addressing this gap, the POMELO methodology
  leverages coarse census data in conjunction with open geodata to produce high precision
  population maps. Key Features: Resolution: The map offers a granular view with a
  100m ground sampling distance, providing intricate details about population distributions
  in Rwanda. Data Sources: Utilizing a combination of projected admisistrative census
  data (UN), and supplementing it with open geodata. Reliability: In comparative experiments
  conducted in sub-Saharan Africa, POMELO''s ability to disaggregate coarse census
  counts achieved R2 values of 85-89%. Furthermore, its potential to predict population
  numbers without any census data reached accuracy levels of 48-69%.. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/pomelo-rwanda-high-resolution-population]'
details: null
exposure:
- asset_type:
    description: High-resolution gridded population density map of Rwanda at 100-meter
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Rwanda census data and remote sensing imagery were processed using
    the POMELO deep learning super-resolution technique to generate a 100-meter resolution
    population density map for 2020. The methodology disaggregates aggregated census
    data into fine-grained spatial units suitable for disaster risk assessment and
    urban planning applications.
  sources:
  - id: source_1
    license: null
    name: POMELO super-resolution technique
    risk_data_type:
    - exposure
    type: model
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/pomelo-rwanda-high-resolution-population
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
  url: https://www.nature.com/articles/s41598-022-24495-w
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: POMELO - Rwanda High Resolution Population Density (Georeferenced Tiff
    raster)
  download_url: https://data.humdata.org/dataset/55b4e34a-3016-47d7-9d1e-db9dde7f1f97/resource/eeca5520-a1b3-4a42-b43d-e415bb8bb953/download/rwa_pomelo.tiff
  format: null
  id: resource_eeca5520
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rwa_pomelo.tiff
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-rwa_ethzprs_pomelohighresolutionpopul_2020
spatial:
  bbox: null
  centroid: null
  countries:
  - RWA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-12-31'
  start: '2020-01-01'
temporal_resolution: null
title: POMELO - Rwanda High Resolution Population Density
version: null
vulnerability: null
---
