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
  name: Ingeniar
  url: https://ingeniar-risk.com
dataset_id: rdls_hzd-GIRI_TC
description: Datasets containing probabilistic analysis of tropical cyclone wind speed
  (km/h) covering historical and climate change projections at the global scale.
details: The tropical cyclone wind hazard model uses historical track data and climate
  projections to generate probabilistic wind speed footprints at global scale. Climate
  change scenarios incorporate projected changes in cyclone frequency and intensity
  based on climate models.
exposure: null
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
  hazard_type: strong_wind
  intensity: sws_3s:km/h
  occurrence_range: Return period 50 to 1,000 years
  processes: tropical_cyclone
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
  description: Collection of historical tropical cyclone wind hazard maps
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF (tif)
  id: HST
  media_type: null
  spatial_resolution: 11100
  temporal: null
  title: Tropical cyclone wind hazard (historical)
- coordinate_system: EPSG:4326
  description: Collection of projected tropical cyclone wind hazard maps under climate
    change scenarios
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF (tif)
  id: CC
  media_type: null
  spatial_resolution: 11100
  temporal: null
  title: Tropical cyclone wind hazard (climate change)
risk_data_type:
- hazard
schema: rdl-03
slug: rdls_hzd-GIRI_TC
spatial:
  countries:
  - GLO
  scale: global
title: Global tropical cyclone wind hazard
version: '1'
vulnerability: null
---
