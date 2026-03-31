---
catalog: Copernicus Climate Data Store
contact_point:
  email: science@axaclimate.com
  id: attribution_contact_point_001
  name: AXA Climate
  url: https://climate.axa
creator:
  email: null
  id: attribution_creator_001
  name: AXA Climate
  url: https://climate.axa
dataset_id: rdls_hzd-mdg_grma_landslidehazard
description: Rainfall-induced landslide hazard index simulated by AXA Climate, for
  SSP2-4.5 and SSP5-8.5 scenarios across three time horizons (baseline, 2050, 2085).
details: The hazard index was built with BRGM landslide susceptibility map and daily
  precipitation dataset.
exposure: []
extra_attributions: []
hazard:
  calculation_method: simulated
  disaster_identifiers: ''
  hazard_analysis_type: empirical
  hazard_type: landslide
  intensity: LSI:-
  occurrence_range: ''
  processes: landslide_general
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
  This project aimed at updating Madagascar's risk profile, and study the risk's evolution
  under climate change.
resources:
- coordinate_system: EPSG:4326
  description: "Daily precipitation from Copernicus ERA5 at 0.25\xC2\xB0 resolution\
    \ was used for baseline map."
  download_url: https://cds.climate.copernicus.eu/datasets/derived-era5-single-levels-daily-statistics?tab=download
  format: HDF5 (hdf5)
  id: resource_xy57HqTY
  media_type: null
  spatial_resolution: null
  temporal: null
  title: ERA5 precipitation
- coordinate_system: EPSG:4326
  description: GCM precipitation downscaled using AXA Climate proprietary algorithm
    to 0.25 degree resolution for future scenarios (SSP2-4.5 and SSP5-8.5).
  download_url: https://climate.axa
  format: HDF5 (hdf5)
  id: resource_downscaled_precip
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Downscaled precipitation on ERA5 dataset
risk_data_type:
- hazard
schema: rdl-03
slug: rdls_hzd-mdg_grma_landslidehazard
spatial:
  countries:
  - MDG
  scale: national
title: Rainfall-induced landslide hazard
version: '1.0'
vulnerability: null
---
