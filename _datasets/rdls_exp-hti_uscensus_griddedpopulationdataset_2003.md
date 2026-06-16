---
attributions:
- entity:
    affiliation: null
    email: null
    name: Haiti 2003 National Census
    url: https://data.humdata.org/dataset/haiti-gridded-population-data
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: High- and medium-resolution satellite imagery
    url: https://data.humdata.org/dataset/haiti-gridded-population-data
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: U.S. Census Bureau
  url: https://data.humdata.org/dataset/haiti-gridded-population-data
creator:
  affiliation: null
  email: null
  name: U.S. Census Bureau
  url: https://data.humdata.org/dataset/haiti-gridded-population-data
dataset_id: rdls_exp-hti_uscensus_griddedpopulationdataset_2003
description: 'Haiti was chosen as the pilot country for developing our population
  mapping methods, based on its high frequency of hurricanes and other natural disasters
  in the recent past. We found a clear correlation between built-up area density derived
  from interpretation of high- and medium-resolution satellite imagery and data from
  the 2003 national census. The resulting 100-meter gridded population map is the
  finest-scale demographic map of the country ever produced. It was made available
  to the public the day after the devastating earthquake of January 2010, and has
  been used extensively for disaster relief. The methods used in the Haiti project
  are described in a paper published in the International Journal of Remote Sensing..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/haiti-gridded-population-data]'
details: null
exposure:
- asset_type:
    description: Gridded population estimates at 100-meter resolution derived from
      2003 census data and built-up area density from satellite imagery
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
  description: High- and medium-resolution satellite imagery was interpreted to derive
    built-up area density, which was correlated with 2003 national census data to
    produce a 100-meter gridded population map. Multiple spatial datasets were combined
    with census data and estimates to generate the final gridded population layer.
  sources:
  - id: source_1
    license: null
    name: Haiti 2003 National Census
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: High- and medium-resolution satellite imagery
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/haiti-gridded-population-data
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
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Haiti Gridded Population Dataset (100-meter spatial resolution gridded
    population dataset.)
  download_url: https://data.humdata.org/dataset/390c0013-9e21-4bbd-ba79-4439139d2086/resource/5b083aed-7642-4e6d-bc82-812ee35fd1b0/download/haiti-gridded-population-estimates-2003.zip
  format: null
  id: resource_5b083aed
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: haiti-gridded-population-estimates-2003.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-hti_uscensus_griddedpopulationdataset_2003
spatial:
  bbox: null
  centroid: null
  countries:
  - HTI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2003-12-31'
  start: '2003-01-01'
temporal_resolution: null
title: Haiti Gridded Population Dataset
version: null
vulnerability: null
---
