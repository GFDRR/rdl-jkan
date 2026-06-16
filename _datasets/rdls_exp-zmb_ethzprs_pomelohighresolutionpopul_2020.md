---
attributions:
- entity:
    affiliation: null
    email: null
    name: "ETH Z\u7AEFrich Photogrammetry and Remote Sensing"
    url: https://data.humdata.org/dataset/pomelo-zambia-high-resolution-population
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: "ETH Z\u7AEFrich, Photogrammetry and Remote Sensing"
  url: https://data.humdata.org/dataset/pomelo-zambia-high-resolution-population
creator:
  affiliation: null
  email: null
  name: "ETH Z\u7AEFrich, Photogrammetry and Remote Sensing"
  url: https://data.humdata.org/dataset/pomelo-zambia-high-resolution-population
dataset_id: rdls_exp-zmb_ethzprs_pomelohighresolutionpopul_2020
description: 'This dataset presents a fine-grained population map of Zambiawith a
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
  in Zambia. Data Sources: Utilizing a combination of projected admisistrative census
  data (UN), and supplementing it with open geodata. Reliability: In comparative experiments
  conducted in sub-Saharan Africa, POMELO''s ability to disaggregate coarse census
  counts achieved R2 values of 85-89%. Furthermore, its potential to predict population
  numbers without any census data reached accuracy levels of 48-69%.. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/pomelo-zambia-high-resolution-population]'
details: null
exposure:
- asset_type:
    description: High-resolution gridded population density map at 100m resolution
      for Zambia in 2020
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
  description: High-resolution population density map generated using the POMELO super-resolution
    deep learning technique applied to Zambian census data and remote sensing imagery,
    producing a 100-meter resolution gridded population dataset for 2020 to address
    the lack of timely and spatially detailed population data in sub-Saharan Africa.
  sources:
  - id: source_1
    license: null
    name: "ETH Z\u7AEFrich Photogrammetry and Remote Sensing"
    risk_data_type:
    - exposure
    type: model
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/pomelo-zambia-high-resolution-population
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
  description: POMELO - Zambia High Resolution Population Density (Georeferenced Tiff
    raster)
  download_url: https://data.humdata.org/dataset/e65907b1-36c3-45eb-9d11-12cb03da8817/resource/c315dd19-1be0-42d2-94cd-3c7489a85e36/download/zmb_pomelo.tiff
  format: null
  id: resource_c315dd19
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: zmb_pomelo.tiff
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-zmb_ethzprs_pomelohighresolutionpopul_2020
spatial:
  bbox: null
  centroid: null
  countries:
  - ZMB
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-12-31'
  start: '2020-01-01'
temporal_resolution: null
title: POMELO - Zambia High Resolution Population Density
version: null
vulnerability: null
---
