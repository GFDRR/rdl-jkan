---
contact_point:
  email: mamadio@worldbank.org
  name: Mattia Amadio
creator:
  name: CIMA
  url: https://www.cimafoundation.org
dataset_id: rdls_hzd-CDRI-FL
description: Datasets containing probabilistic analysis of river flood maximum water
  depth (m) covering historical and future projections.
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
exposure: null
hazard:
  calculation_method: simulated
  disaster_identifiers: ''
  hazard_analysis_type: probabilistic
  hazard_type: flood
  intensity: fl_wd:m
  occurrence_range: Return period 2 to 1,000 years
  processes: fluvial_flood
license: CC-BY-4.0
loss: null
project: GIRI - Global Infrastructure Risk Model and Resilience Index
publisher:
  name: UNEP
  url: https://giri.unepgrid.ch/map
purpose: null
resources:
- coordinate_system: EPSG:4326
  description: Collection of historical hazard maps
  download_url: https://giri.unepgrid.ch/map
  format: geotiff
  id: HST
  spatial_resolution: 90
  title: Flood hazard (historical 1979-2016)
- coordinate_system: EPSG:4326
  description: Collection of projected hazard maps (SSP1)
  download_url: https://giri.unepgrid.ch/map
  format: geotiff
  id: PRJ_LB
  spatial_resolution: 90
  title: Flood hazard (projected SSP1)
- coordinate_system: EPSG:4326
  description: Collection of projected hazard maps (SSP5)
  download_url: https://giri.unepgrid.ch/map
  format: geotiff
  id: PRJ_UB
  spatial_resolution: 90
  title: Flood hazard (projected SSP5)
risk_data_type:
- hazard
schema: rdl-02
spatial:
  countries:
  - GLO
  scale: global
title: Global river flood hazard
version: '1'
vulnerability: null
---
