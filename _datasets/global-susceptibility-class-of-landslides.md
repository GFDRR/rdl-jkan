---
contact_point:
  email: mamadio@worldbank.org
  name: Mattia Amadio
creator:
  name: CIMA
  url: https://www.cimafoundation.org
dataset_id: CDRI_LS
slug: CDRI_LS
description: The landslides susceptibility map indicates the areas of the world that
  are more prone to landslides, both seismic and precipitation-induced.
details: The precipitation-induced landslides susceptibility map for the current climate
  classifies the terrain into five susceptibility classes by combining slope, vegetation,
  lithology, and antecedent rainfall information from global datasets. The susceptibility
  map has global coverage and a resolution of ~90 meters at the equator.
exposure: null
hazard:
  calculation_method: inferred
  disaster_identifiers: ''
  hazard_analysis_type: deterministic
  hazard_type: landslide
  intensity: ls_hzd:-
  occurrence_range: ''
  processes: landslide_general
license: CC-BY-4.0
loss: null
project: null
publisher:
  name: UNEP
  url: https://giri.unepgrid.ch/map
purpose: null
resources:
- coordinate_system: EPSG:4326
  description: The earthquake-induced landslides susceptibility map indicates the
    areas of the world that are more prone to landslides triggered by earthquakes.
  download_url: https://giri.unepgrid.ch/map
  format: geotiff
  id: EQ_trigger
  spatial_resolution: 90
  title: Landslide from earthquake trigger
- coordinate_system: EPSG:4326
  description: The precipitation-induced landslides susceptibility map for the existing
    climate indicates the areas of the world that are more prone to landslides according
    to current precipitation trends
  download_url: https://giri.unepgrid.ch/map
  format: geotiff
  id: RF_trigger-hst
  spatial_resolution: 90
  title: Landslide from precipitation trigger - Historical
- coordinate_system: EPSG:4326
  description: The precipitation-induced landslides susceptibility map for the existing
    climate indicates the areas of the world that are more prone to landslides according
    to future precipitation trends (lower bound)
  download_url: https://giri.unepgrid.ch/map
  format: geotiff
  id: RF_trigger-ssp1
  spatial_resolution: 90
  title: Landslide from precipitation trigger - SSP1
- coordinate_system: EPSG:4326
  description: The precipitation-induced landslides susceptibility map for the existing
    climate indicates the areas of the world that are more prone to landslides according
    to future precipitation trends (upper bound)
  download_url: https://giri.unepgrid.ch/map
  format: geotiff
  id: RF_trigger-ssp5
  spatial_resolution: 90
  title: Landslide from precipitation trigger - SSP5
risk_data_type:
- hazard
schema: rdl-02
spatial:
  countries:
  - GLO
  scale: global
title: Susceptibility class of landslides
version: '1'
vulnerability: null
---
