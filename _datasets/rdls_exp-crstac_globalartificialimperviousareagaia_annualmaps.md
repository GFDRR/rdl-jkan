---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Star Cloud Data Service Platform
  url: https://data-starcloud.pcl.ac.cn/resource/13
creator:
  affiliation: null
  email: null
  name: Star Cloud Data Service Platform
  url: https://data-starcloud.pcl.ac.cn/resource/13
dataset_id: rdls_exp-crstac_globalartificialimperviousareagaia_annualmaps
description: 'Annual maps of artificial impervious area, a predominant indicator of
  human settlement. Values range from 0 to 34. 0 represents non-human settlements,
  1 represents increased human settlements in 2017, 2 represents increased settlements
  in 2016, ..., 33 represents new settlements in 1985 and before [Source: This metadata
  record was automatically extracted from the STAC catalog climate-risk-stac (https://climate-risk-data.github.io/climate-risk-stac/)]'
details: null
exposure:
- asset_type:
    description: urban/built-up footprints
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: area
      unit: square_metre
hazard: null
license: https://spdx.org/licenses/CC-BY-4.0.html
lineage:
  description: Annual maps of artificial impervious area, a predominant indicator
    of human settlement. Values range from 0 to 34. 0 represents non-human settlements,
    1 represents increased human settlements in 2017, 2 represents increased settlements
    in 2016, ..., 33 represents new settlements in 1985 and before.
  sources:
  - id: source_underlying_1
    license: null
    name: Nighttime lights
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_underlying_2
    license: null
    name: Sentinel 1
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_underlying_3
    license: null
    name: Landsat
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
  name: Star Cloud Data Service Platform
  url: https://data-starcloud.pcl.ac.cn/resource/13
purpose: user account needed; data doanloadable by tile
referenced_by:
- author_names: null
  date_published: null
  doi: 10.1016/j.rse.2019.111510
  id: ref_doi
  name: null
  url: https://doi.org/10.1016/j.rse.2019.111510
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/exposure-vulnerability/land-use/global-artificial-impervious-area-gaia/annual-maps/annual-maps.json
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
  title: 'STAC Item: Global Artificial Impervious Area (GAIA) - Annual maps'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Global Artificial Impervious Area (GAIA) - Annual maps - data file
  download_url: https://data-starcloud.pcl.ac.cn/resource/13
  format: null
  id: resource_data-file_1
  media_type: image/tiff; application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global Artificial Impervious Area (GAIA) - Annual maps - data file
- access_url: https://doi.org/10.1016/j.rse.2019.111510
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Global Artificial Impervious Area (GAIA) - Annual maps (Web reference)
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
slug: rdls_exp-crstac_globalartificialimperviousareagaia_annualmaps
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
spatial_resolution: 31
temporal:
  central_year: null
  duration: null
  end: '2018'
  start: '1985'
temporal_resolution: P1Y
title: Global Artificial Impervious Area (GAIA) - Annual maps
version: null
vulnerability: null
---
