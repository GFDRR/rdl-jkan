---
contact_point:
  email: nadia.bloemendaal@vu.nl
  id: attribution_contact
  name: Nadia Bloemendaal
  url: https://vu.nl/en/about-vu/research-institutes/ivm
creator:
  email: nadia.bloemendaal@vu.nl
  id: attribution_creator
  name: Nadia Bloemendaal
  url: https://vu.nl/en/about-vu/research-institutes/ivm
dataset_id: rdls_hzd-nismod_sdk_stormtcwindspeedpresent
description: Gridded and table-based tropical-cyclone wind-hazard datasets for the
  present climate, providing maximum wind speeds at fixed return periods and return
  periods at fixed wind speeds; gridded products are ~10 km per basin, and city/island
  tables summarize conditions within 100 km.
details: "Synthetic tracks were generated with the statistical STORM algorithm; a\
  \ 2-D parametric wind model was applied to produce ~10 km fields, and return periods\
  \ (or wind speeds) were derived empirically with Weibulls plotting formula. Datasets\
  \ include, for each grid cell (or city/island entry), the mean, standard deviation,\
  \ and 5-95% confidence intervals across 1,000 realizations; basin IDs (EP, NA, NI,\
  \ SI, SP, WP) and fixed value sets for return periods (10-10,000 yr) and wind speeds\
  \ (20-75 m s\u207B\xB9 with additional threshold values) are provided."
exposure: []
extra_attributions:
- email: info@deltares.nl
  id: attribution_collaborator_1
  name: Deltares,Delft, The Netherlands
  role: collaborator
  url: https://www.deltares.nl/en
- email: pers@knmi.nl
  id: attribution_collaborator_2
  name: Royal Netherlands Meteorological Institute (KNMI), De Bilt, The Netherlands
  role: collaborator
  url: https://www.knmi.nl/over-het-knmi/about
- email: enquiries@bodc.ac.uk
  id: attribution_collaborator_3
  name: University of Southampton, National Oceanography Centre, School of Ocean and
    Earth Science
  role: collaborator
  url: https://noc.ac.uk/
- email: info.ivm@vu.nl
  id: attribution_collaborator_4
  name: Vrije Universiteit Amsterdam, Institute for Environmental Studies (IVM)
  role: collaborator
  url: https://vu.nl/en/about-vu/research-institutes/ivm
hazard:
  calculation_method: simulated
  disaster_identifiers: ''
  hazard_analysis_type: probabilistic
  hazard_type: ''
  intensity: ''
  occurrence_range: 1/10 to 1/10000 years
  processes: ''
  seasonality: ''
license: CC0-1.0
loss: null
project: null
publisher:
  email: researchdata@4tu.nl
  id: attribution_publisher
  name: 4TU.ResearchData
  url: https://data.4tu.nl/
purpose: To supply consistent, high-resolution tropical-cyclone wind hazard metrics
  that support risk assessment, engineering design, and adaptation planning-using
  a common methodology (Weibull plotting) across basins and for selected cities and
  islands.
resources:
- coordinate_system: EPSG:4326
  description: 'Basin reference layer listing the six TC basins used across the STORM
    products: EP (Eastern Pacific), NA (North Atlantic), NI (North Indian), SI (South
    Indian), SP (South Pacific), WP (Western Pacific)'
  download_url: https://data.4tu.nl/file/0ea98bdd-5772-4da8-ae97-99735e891aff/e4d92161-214a-4df7-a2fb-533825b1d46e
  format: KML (kml)
  id: resource_1
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Basins of STORM IBTrACS dataset (KML)
- coordinate_system: EPSG:4326
  description: 'Workbook with two sheets for events within 100 km of 18 predefined
    coastal cities: (1) wind speed at fixed return periods, and (2) return period
    at fixed wind speeds (5 m/s steps plus Saffir-Simpson thresholds).'
  download_url: https://data.4tu.nl/file/0ea98bdd-5772-4da8-ae97-99735e891aff/d08e9a54-a5bf-442a-ac3c-69ec1f9a0f59
  format: Excel (xlsx)
  id: resource_2
  media_type: null
  spatial_resolution: null
  temporal: null
  title: 'STORM Cities: TC wind-speed return periods (present)'
- coordinate_system: EPSG:4326
  description: Per-basin ~10 km grids of maximum wind speed (m/s) at fixed return
    periods (10-10,000 yr), including mean, standard deviation, and 5-95% confidence
    intervals over 1,000 realizations.
  download_url: https://data.4tu.nl/file/0ea98bdd-5772-4da8-ae97-99735e891aff/0b98c6f5-c7af-45bb-bb6e-dac53e1b8d55
  format: GeoTIFF (tif)
  id: resource_3
  media_type: null
  spatial_resolution: 10000
  temporal: null
  title: STORM Fixed Return Periods (present, gridded)
- coordinate_system: EPSG:4326
  description: Per-basin ~10 km grids of return period (years) at fixed wind speeds
    (20-75 m/s at 5 m/s steps, plus 18, 33, 42, 58 m/s), including mean, standard
    deviation, and 5-95% confidence intervals over 1,000 realizations.
  download_url: https://data.4tu.nl/file/0ea98bdd-5772-4da8-ae97-99735e891aff/3c839d73-e6c0-4d63-ae03-c0d05e734d57
  format: GeoTIFF (tif)
  id: resource_4
  media_type: null
  spatial_resolution: 10000
  temporal: null
  title: STORM Fixed Wind Speeds (present, gridded)
- coordinate_system: EPSG:4326
  description: 'Workbook with two sheets for events within 100 km of island capitals
    (SIDS and others): (1) wind speed at fixed return periods, and (2) return period
    at fixed wind speeds (5 m/s steps plus Saffir-Simpson thresholds).'
  download_url: https://data.4tu.nl/file/0ea98bdd-5772-4da8-ae97-99735e891aff/f537c00b-4019-42da-bd13-e4bcb49c8aa3
  format: Excel (xlsx)
  id: resource_5
  media_type: null
  spatial_resolution: null
  temporal: null
  title: 'STORM Islands: TC wind-speed return periods (present)'
risk_data_type:
- hazard
schema: rdl-03
slug: rdls_hzd-nismod_sdk_stormtcwindspeedpresent
spatial:
  countries:
  - GLO
  scale: global
title: STORM tropical cyclone wind speed return periods
version: '4'
vulnerability: null
---
