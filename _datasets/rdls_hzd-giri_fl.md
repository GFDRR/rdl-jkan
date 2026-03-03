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
  name: CIMA
  url: https://www.cimafoundation.org
dataset_id: rdls_hzd-GIRI_FL
description: Datasets containing probabilistic analysis of river flood maximum water
  depth (m) covering historical and future projections at the global scale.
details: The hydrological model used is the Continuum model (Silvestro et al. 2013
  and 2015). It is a continuous, distributed and physically based hydrological model
  able to reproduce the spatial-temporal evolution of soil moisture, energy fluxes,
  surface soil temperature, evapotranspiration and discharge. Climate dataset used
  for the simulation of basin response are the W5E5 Global Meteorological dataset
  for present climate, and the ISIMIP3b Global Meteorological reanalysis dataset for
  the futur climate. In order to generate flood hazard maps, resulting discharge estimates
  are input to an hydraulic model based on the Manning equation that compute channel
  uniform flow depth. This simplified approach fits to determine flood maps on large
  areas.
exposure: []
extra_attributions:
- email: null
  id: '4'
  name: CDRI
  role: resource_provider
  url: https://cdri.world/
hazard:
  calculation_method: simulated
  disaster_identifiers: ''
  hazard_analysis_type: probabilistic
  hazard_type: flood
  intensity: Wd:M
  occurrence_range: Return period 2 to 1,000 years
  processes: fluvial_flood
  seasonality: ''
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
  description: Collection of historical hazard maps
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF (tif)
  id: HST
  media_type: null
  spatial_resolution: 90
  temporal:
    duration: null
    end: '2016'
    start: '1979'
    temporal_resolution: null
  title: Flood hazard (historical 1979-2016)
- coordinate_system: EPSG:4326
  description: Collection of projected hazard maps (SSP1)
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF (tif)
  id: PRJ_LB
  media_type: null
  spatial_resolution: 90
  temporal:
    duration: null
    end: '2100'
    start: '2017'
    temporal_resolution: null
  title: Flood hazard (projected SSP1)
- coordinate_system: EPSG:4326
  description: Collection of projected hazard maps (SSP5)
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF (tif)
  id: PRJ_UB
  media_type: null
  spatial_resolution: 90
  temporal:
    duration: null
    end: '2100'
    start: '2017'
    temporal_resolution: null
  title: Flood hazard (projected SSP5)
risk_data_type:
- hazard
schema: rdl-03
slug: rdls_hzd-GIRI_FL
spatial:
  countries:
  - GLO
  scale: global
title: Global river flood hazard
version: '1'
vulnerability: null
---
