---
contact_point:
  email: mamadio@worldbank.org
  id: '3'
  name: Mattia Amadio
  url: null
creator:
  email: null
  id: '2'
  name: CIMA
  url: https://www.cimafoundation.org
dataset_id: rdls_hzd-GIRI_LS
description: The landslides susceptibility map indicates the areas of the world that
  are more prone to landslides, both seismic and precipitation-induced.
details: The precipitation-induced landslides susceptibility map for the current climate
  classifies the terrain into five susceptibility classes by combining slope, vegetation,
  lithology, and antecedent rainfall information from global datasets. The susceptibility
  map has global coverage and a resolution of ~90 meters at the equator.
exposure: []
extra_attributions:
- email: null
  id: '4'
  name: CDRI
  role: resource_provider
  url: https://cdri.world/
hazard:
  calculation_method: inferred
  disaster_identifiers: ''
  hazard_analysis_type: deterministic
  hazard_type: ''
  intensity: ''
  occurrence_range: ''
  processes: ''
  seasonality: uniform
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
  description: The earthquake-induced landslides susceptibility map indicates the
    areas of the world that are more prone to landslides triggered by earthquakes.
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF (tif)
  id: EQ_trigger
  media_type: null
  spatial_resolution: 90
  temporal: null
  title: Landslide from earthquake trigger
- coordinate_system: EPSG:4326
  description: The precipitation-induced landslides susceptibility map for the existing
    climate indicates the areas of the world that are more prone to landslides according
    to current precipitation trends
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF (tif)
  id: RF_trigger-hst
  media_type: null
  spatial_resolution: 90
  temporal: null
  title: Landslide from precipitation trigger - Historical
- coordinate_system: EPSG:4326
  description: The precipitation-induced landslides susceptibility map for the existing
    climate indicates the areas of the world that are more prone to landslides according
    to future precipitation trends (lower bound)
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF (tif)
  id: RF_trigger-ssp1
  media_type: null
  spatial_resolution: 90
  temporal: null
  title: Landslide from precipitation trigger - SSP1
- coordinate_system: EPSG:4326
  description: The precipitation-induced landslides susceptibility map for the existing
    climate indicates the areas of the world that are more prone to landslides according
    to future precipitation trends (upper bound)
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF (tif)
  id: RF_trigger-ssp5
  media_type: null
  spatial_resolution: 90
  temporal: null
  title: Landslide from precipitation trigger - SSP5
risk_data_type:
- hazard
schema: rdl-03
slug: rdls_hzd-GIRI_LS
spatial:
  countries:
  - GLO
  scale: global
title: Global susceptibility class of landslides
version: '1'
vulnerability: null
---
