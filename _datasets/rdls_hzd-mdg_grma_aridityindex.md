---
catalog: Copernicus Climate Data Store
contact_point:
  email: science@axaclimate.com
  id: attribution_contact_point_001
  name: AXA Climate
  url: null
creator:
  email: null
  id: attribution_creator_001
  name: AXA Climate
  url: https://climate.axa
dataset_id: rdls_hzd-mdg_grma_aridityindex
description: This dataset provides the seasonal aridity index values for Madagascar,
  covering the historical baseline period (1985-2014) and projected time horizons
  (2050 and 2085) under the SSP2-4.5 and SSP5-8.5 emission scenarios, to identify
  regions most prone to droughts and assess their evolution under climate change.
details: The aridity index is determined as the ratio of seasonal precipitation (P)
  to potential evapotranspiration (PET). PET is estimated using the Penman-Monteith
  equation. The baseline period relies on ERA5 reanalysis data, while projected periods
  (2050 and 2085) under SSP2-4.5 and SSP5-8.5 scenarios rely on high-resolution statistically
  downscaled CMIP6 climate model data. Daily precipitation, temperature, relative
  humidity, solar radiation and wind are used to compute the index.
exposure: []
extra_attributions: []
hazard:
  calculation_method: inferred
  disaster_identifiers: ''
  hazard_analysis_type: deterministic
  hazard_type: drought
  intensity: MHI:-
  occurrence_range: ''
  processes: meteorological_drought
  seasonality: ''
license: CC-BY-4.0
loss: null
project:
  name: GRMA Madagascar - Phase 1
  url: https://www.resiliencemada.gov.mg
publisher:
  email: null
  id: attribution_publisher_001
  name: Global Risk Modelling Alliance
  url: https://grma.global
purpose: This dataset was developed during the first phase of GRMA's project in Madagascar.
  This project aimed at updating Madagascar's risk profile, and see the risk evolution
  under climate change.
resources:
- coordinate_system: EPSG:4326
  description: ECMWF's reanalysis data. The daily precipitation, temperature, relative
    humidity, solar radiation and wind are used to compute the aridity index.
  download_url: https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels
  format: NetCDF (nc)
  id: resource_era5_001
  media_type: null
  spatial_resolution: 25000
  temporal:
    duration: null
    end: '2014'
    start: '1985'
    temporal_resolution: null
  title: ERA5 reanalysis data
- coordinate_system: EPSG:4326
  description: High resolution statistically downscaled CMIP6 climate model data.
    The daily precipitation, temperature, relative humidity, solar radiation and wind
    are used to compute the aridity index.
  download_url: https://esgf-node.ipsl.upmc.fr/projects/cmip6-ipsl/
  format: GeoTIFF (tif)
  id: resource_cmip6_001
  media_type: null
  spatial_resolution: 25000
  temporal:
    duration: null
    end: '2100'
    start: '1985'
    temporal_resolution: null
  title: CMIP6 climate model data
risk_data_type:
- hazard
schema: rdl-03
slug: rdls_hzd-mdg_grma_aridityindex
spatial:
  countries:
  - MDG
  scale: national
title: Tiomena Seasonal Aridity Index
version: '1.0'
vulnerability: null
---
