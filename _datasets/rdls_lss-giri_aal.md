---
contact_point:
  email: mamadio@worldbank.org
  id: attribution_contact_point_1
  name: Mattia Amadio
  url: null
creator:
  email: null
  id: attribution_creator_1
  name: UNEP Grid Geneva
  url: https://www.unepgrid.ch
dataset_id: rdls_lss-GIRI_AAL
description: Values of average annual loss (AAL) including all hazards. The AAL provides
  an estimator of losses that are likely to occur every year due to a specific hazard.
  Values of AAL are calculated per country, sector (buildings, power, telecommunications,
  roads and railways, water and wastewater, oil and gas, ports and airports) and subsector.
  Global scale analysis, covering historical and future climate projections (SSP1,
  SSP5).
details: The multi-hazard average annual loss dataset integrates risk from multiple
  natural hazards (floods, cyclones, earthquakes, tsunamis, landslides, drought) to
  estimate expected annual economic losses to buildings and infrastructure. Estimates
  are provided for historical climate conditions and future climate scenarios (SSP1
  and SSP5) to assess climate change impacts on risk.
exposure: []
extra_attributions:
- email: null
  id: attribution_resource_provider_1
  name: CDRI
  role: resource_provider
  url: https://cdri.world/
hazard: null
license: CC-BY-4.0
loss:
  approach: ''
  base_data_type: ''
  category: ''
  description: ''
  dimension: ''
  exposure_id: ''
  hazard_analysis_type: ''
  hazard_id: ''
  hazard_process: fluvial_flood, ground_motion, landslide_general
  hazard_type: earthquake, flood, landslide
  impact_metric: ''
  impact_type: ''
  impact_unit: ''
  type: ''
  vulnerability_id: ''
project:
  name: Global Infrastructure Risk Model and Resilience Index (GIRI)
  url: https://giri.unepgrid.ch/
publisher:
  email: null
  id: attribution_publisher_1
  name: UNEP-GRID
  url: https://unepgrid.ch/en
purpose: null
resources:
- coordinate_system: EPSG:4326
  description: Total average annual loss for buildings and infrastructure under historical
    climate conditions (1979-2016)
  download_url: https://giri.unepgrid.ch/facts-figures/multi-hazards
  format: CSV (csv)
  id: AAL_HST
  media_type: null
  spatial_resolution: null
  temporal:
    duration: null
    end: '2016'
    start: '1979'
    temporal_resolution: null
  title: Multi-hazard AAL (Historical)
- coordinate_system: EPSG:4326
  description: Total average annual loss for buildings and infrastructure under SSP1
    climate projection (lower bound)
  download_url: https://giri.unepgrid.ch/facts-figures/multi-hazards
  format: CSV (csv)
  id: AAL_SSP1
  media_type: null
  spatial_resolution: null
  temporal:
    duration: null
    end: '2100'
    start: '2017'
    temporal_resolution: null
  title: Multi-hazard AAL (SSP1)
- coordinate_system: EPSG:4326
  description: Total average annual loss for buildings and infrastructure under SSP5
    climate projection (upper bound)
  download_url: https://giri.unepgrid.ch/facts-figures/multi-hazards
  format: CSV (csv)
  id: AAL_SSP5
  media_type: null
  spatial_resolution: null
  temporal:
    duration: null
    end: '2100'
    start: '2017'
    temporal_resolution: null
  title: Multi-hazard AAL (SSP5)
risk_data_type:
- loss
schema: rdl-03
slug: rdls_lss-GIRI_AAL
spatial:
  countries:
  - GLO
  scale: global
title: Global multi-hazard average annual loss
version: '1'
vulnerability: null
---
