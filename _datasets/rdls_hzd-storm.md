---
catalog: null
contact_point:
  email: nadia.bloemendaal@vu.nl
  id: attribution_contact_point_migrated_1767801294813
  name: Nadia Bloemendaal
  url: https://vu.nl/en/about-vu/research-institutes/ivm
creator:
  email: nadia.bloemendaal@vu.nl
  id: attribution_creator_migrated_1767801294813
  name: Nadia Bloemendaal
  url: https://data.4tu.nl/authors/8a084c6a-3315-4ba7-9768-dd1ba1825dbc
dataset_id: rdls_hzd-STORM
description: Datasets containing probabilistic analysis of tropical cyclone maximum
  wind speed (in m/s) at fixed return periods and return periods at fixed wind speeds
  for present climate (1980-2018) and climate change scenarios (1979-2014 baseline
  and 2015-2050 projections); gridded products are ~10 km per basin, and city/island
  tables summarize conditions within 100 km. Climate change datasets incorporate signals
  from four GCMs (CMCC-CM2-VHR4, CNRM-CM6-1-HR, EC-Earth3P-HR, HadGEM3-GC31-HM).
details: "Datasets were generated with the statistical STORM algorithm. Present climate\
  \ dataset uses IBTrACS historical tracks (1980-2018) with ERA5 monthly-mean environmental\
  \ conditions. Climate change datasets add signals from four GCMs (CMCC-CM2-VHR4,\
  \ CNRM-CM6-1-HR, EC-Earth3P-HR, HadGEM3-GC31-HM) to project future conditions. A\
  \ 2-D parametric wind model was applied to produce ~10 km fields, and return periods\
  \ (or wind speeds) were derived empirically with Weibull's plotting formula. Datasets\
  \ include, for each grid cell (or city/island entry), the mean, standard deviation,\
  \ and 5-95% confidence intervals across 1,000 realizations; basin IDs (EP, NA, NI,\
  \ SI, SP, WP) and fixed value sets for return periods (10-10,000 yr) and wind speeds\
  \ (20-75 m s\u207B\xB9 with additional threshold values) are provided."
exposure: null
extra_attributions:
- email: null
  id: '1'
  name: 4TU.Centre for Research Data
  role: resource_provider
  url: https://data.4tu.nl/
- email: null
  id: '3'
  name: Tom Russell
  role: processor
  url: https://www.eci.ox.ac.uk/person/tom-russell
- email: info@deltares.nl
  id: attribution_1767801783793
  name: Deltares
  role: collaborator
  url: https://www.deltares.nl/en
hazard:
  calculation_method: simulated
  disaster_identifiers: ''
  hazard_analysis_type: probabilistic
  hazard_type: strong_wind
  intensity: sws_10m:m/s
  occurrence_range: 1/10 to 1/10000 years
  processes: tropical_cyclone
  seasonality: uniform
license: CC0-1.0
loss: null
project:
  name: STORM - Synthetic Tropical cyclOne geneRation Model
  url: https://data.4tu.nl/datasets/0ea98bdd-5772-4da8-ae97-99735e891aff
publisher:
  email: null
  id: attribution_publisher_migrated_1767801294813
  name: 4TU.Centre for Research Data
  url: https://data.4tu.nl/
purpose: To supply consistent, high-resolution tropical-cyclone wind hazard metrics
  for present climate and climate change scenarios that support risk assessment, engineering
  design, and adaptation planning using a common methodology (Weibull plotting) across
  basins and for selected cities and islands.
resources:
- coordinate_system: EPSG:4326
  description: The GeoTIFFs provided in the original STORM datasets have been mosaicked
    into single files with global extent for each climate model/return period. STORM_FIXED_RETURN_PERIODS_{STORM_MODEL}_{STORM_RP}_YR_RP.tif
  download_url: https://data.4tu.nl/datasets/0ea98bdd-5772-4da8-ae97-99735e891aff/4
  format: GeoTIFF (tif)
  id: HST
  media_type: null
  spatial_resolution: 10000
  temporal:
    duration: null
    end: '2014'
    start: '1979'
    temporal_resolution: null
  title: Global tropical cyclone wind speed maps by return period (historical 1979-2014)
- coordinate_system: EPSG:4326
  description: The GeoTIFFs provided in the original STORM datasets have been mosaicked
    into single files with global extent for each climate model/return period. STORM_FIXED_RETURN_PERIODS_{STORM_MODEL}_{STORM_RP}_YR_RP.tif
  download_url: https://data.4tu.nl/datasets/504c838e-2bd8-4d61-85a1-d495bdc560c3/4
  format: GeoTIFF (tif)
  id: PRJ_MEDIAN
  media_type: null
  spatial_resolution: 10000
  temporal:
    duration: null
    end: '2050'
    start: '2015'
    temporal_resolution: null
  title: Global tropical cyclone wind speed maps by return period (median projections
    2015-2050)
risk_data_type:
- hazard
schema: rdl-03
slug: rdls_hzd-STORM
spatial:
  countries:
  - GLO
  scale: global
title: Global tropical cyclone (wind speed) hazard, historical and projections
version: '4'
vulnerability: null
---
