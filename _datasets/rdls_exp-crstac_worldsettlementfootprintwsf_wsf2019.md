---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: German Aerospace Center (DLR)
  url: https://geoservice.dlr.de/web/maps
creator:
  affiliation: null
  email: null
  name: German Aerospace Center (DLR)
  url: https://geoservice.dlr.de/web/maps
dataset_id: rdls_exp-crstac_worldsettlementfootprintwsf_wsf2019
description: 'The World Settlement Footprint (WSF) 2019 is a 10m resolution binary
  mask outlining the extent of human settlements globally derived by means of 2019
  multitemporal Sentinel-1 (S1) and Sentinel-2 (S2) imagery [Source: This metadata
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
license: CC-BY-4.0
lineage:
  description: The World Settlement Footprint (WSF) is a 10m resolution binary mask
    outlining the extent of human settlements globally derived by means of multitemporal
    satellite imagery.
  sources:
  - id: source_underlying_1
    license: null
    name: Sentinel
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: German Aerospace Center (DLR)
  url: https://geoservice.dlr.de/web/maps
purpose: downloadable by tile
referenced_by:
- author_names: null
  date_published: null
  doi: 10.1553/giscience2021_01_s33
  id: ref_doi
  name: null
  url: https://doi.org/10.1553/giscience2021_01_s33
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/exposure-vulnerability/land-use/world-settlement-footprint-wsf/wsf-2019/wsf-2019.json
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
  title: 'STAC Item: World Settlement Footprint (WSF) - WSF 2019'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: World Settlement Footprint (WSF) - WSF 2019 - data file
  download_url: https://geoservice.dlr.de/web/maps
  format: null
  id: resource_data-file_1
  media_type: image/tiff; application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: World Settlement Footprint (WSF) - WSF 2019 - data file
- access_url: https://doi.org/10.1553/giscience2021_01_s33
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: World Settlement Footprint (WSF) - WSF 2019 (Web reference)
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
slug: rdls_exp-crstac_worldsettlementfootprintwsf_wsf2019
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
spatial_resolution: 10
temporal:
  central_year: null
  duration: null
  end: '2019'
  start: '2019'
temporal_resolution: null
title: World Settlement Footprint (WSF) - WSF 2019
version: null
vulnerability: null
---
