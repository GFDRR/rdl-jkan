---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Figshare
  url: https://doi.org/10.6084/m9.figshare.9696218
creator:
  affiliation: null
  email: null
  name: Figshare
  url: https://doi.org/10.6084/m9.figshare.9696218
dataset_id: rdls_exp-crstac_globalurbangrowth_y18702100
description: 'Data on global urban extent dynamics from 1870 to 2100, using a urban
  cellular automata (CA) model with consideration of historical trends of urban growth
  over a long temporal span and the satellite-derived urban extent time series data
  (1992-2013). Combination of historical hindcasting (1870-1990) using an urban shrink
  model and projected future (2020-2100) global urban land extent dynamics under the
  five Shared Socioeconomic Pathways (SSPs). Climate scenarios (as published): "SSPs"
  [Source: This metadata record was automatically extracted from the STAC catalog
  climate-risk-stac (https://climate-risk-data.github.io/climate-risk-stac/)]'
details: null
exposure:
- asset_type:
    description: population number
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
license: https://spdx.org/licenses/CC-BY-4.0.html
lineage:
  description: Data on global urban extent dynamics from 1870 to 2100, using a urban
    cellular automata (CA) model with consideration of historical trends of urban
    growth over a long temporal span and the satellite-derived urban extent time series
    data (1992-2013). Combination of historical hindcasting (1870-1990) using an urban
    shrink model and projected future (2020-2100) global urban land extent dynamics
    under the five Shared Socioeconomic Pathways (SSPs).
  sources:
  - id: source_underlying_1
    license: null
    name: HYDE3.2
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_underlying_2
    license: null
    name: nighttime lights data
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_underlying_3
    license: null
    name: WDPA
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_underlying_4
    license: null
    name: land cover
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Figshare
  url: https://doi.org/10.6084/m9.figshare.9696218
purpose: code available upon request
referenced_by:
- author_names: null
  date_published: null
  doi: 10.1038/s43247-021-00273-w
  id: ref_doi
  name: null
  url: https://doi.org/10.1038/s43247-021-00273-w
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/exposure-vulnerability/population/global-urban-growth/y1870-2100/y1870-2100.json
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Source STAC Item metadata record for this dataset, hosted as part of
    the climate-risk-stac catalogue. Conforms to STAC v1.0.0.
  download_url: null
  format: null
  id: resource_stac_item
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'STAC Item: Global urban growth - Y1870-2100'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Global urban growth - Y1870-2100 - data file
  download_url: https://figshare.com/ndownloader/articles/9696218/versions/1
  format: null
  id: resource_data-file_1
  media_type: image/tiff; application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global urban growth - Y1870-2100 - data file
- access_url: https://doi.org/10.1038/s43247-021-00273-w
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Global urban growth - Y1870-2100 (Web reference)
  download_url: null
  format: Web reference
  id: resource_link_reference
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Reference
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-crstac_globalurbangrowth_y18702100
spatial:
  bbox:
  - -180.0
  - -90.0
  - 180.0
  - 90.0
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: 926
temporal:
  central_year: null
  duration: null
  end: '2100'
  start: '1870'
temporal_resolution: P10Y
title: Global urban growth - Y1870-2100
version: null
vulnerability: null
---
