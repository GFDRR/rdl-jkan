---
catalog: null
contact_point:
  email: mamadio@worldbank.org
  id: '3'
  name: Mattia Amadio
  url: null
creator:
  email: null
  id: '2'
  name: UNEP-GRID
  url: https://unepgrid.ch/en
dataset_id: rdls_exp-GIRI_BLD
description: Datasets containing building footprint distribution at high resolution
  for exposure analysis at the global scale, categorized as residential, non-residential,
  and total buildings.
details: Building exposure datasets provide spatial distribution of building footprints
  globally, classified by use type (residential vs. non-residential). These datasets
  are essential for assessing the built environment exposure to natural hazards and
  estimating potential losses.
exposure:
  category: buildings
  dimension: structure
  quantity_kind: area
  taxonomy: null
extra_attributions:
- email: null
  id: '4'
  name: CDRI
  role: resource_provider
  url: https://cdri.world/
hazard: null
license: CC-BY-4.0
loss: null
project:
  name: Global Infrastructure Risk Model and Resilience Index (GIRI)
  url: https://giri.unepgrid.ch/
publisher:
  email: null
  id: '1'
  name: UNEP-GRID
  url: https://unepgrid.ch/en
purpose: null
resources:
- coordinate_system: EPSG:4326
  description: Spatial distribution of residential building footprints
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF (tif)
  id: BLD_RES
  media_type: null
  spatial_resolution: 90
  temporal: null
  title: Residential buildings
- coordinate_system: EPSG:4326
  description: Spatial distribution of non-residential building footprints (commercial,
    industrial, institutional)
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF (tif)
  id: BLD_NONRES
  media_type: null
  spatial_resolution: 90
  temporal: null
  title: Non-residential buildings
- coordinate_system: EPSG:4326
  description: Spatial distribution of all building footprints (residential and non-residential
    combined)
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF (tif)
  id: BLD_TOTAL
  media_type: null
  spatial_resolution: 90
  temporal: null
  title: Total buildings
risk_data_type:
- exposure
schema: rdl-03
slug: rdls_exp-GIRI_BLD
spatial:
  countries:
  - GLO
  scale: global
title: Global building exposure
version: '1'
vulnerability: null
---
