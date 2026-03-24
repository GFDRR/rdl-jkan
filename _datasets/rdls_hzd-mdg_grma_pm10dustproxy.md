---
catalog: null
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
dataset_id: rdls_hzd-mdg_grma_pm10dustproxy
description: This dataset provides the sub-daily atmospheric concentrations of particulate
  matter with a diameter smaller than 10 micrometers (PM10).
details: "This dataset is used as a proxy for dust storms occurence, it is extracted\
  \ over Madagascar from the CAMS global reanalysis EAC4 (ECMWF Atmospheric Composition\
  \ Reanalysis 4) at a 0.75\xB0 resolution, available from 2003 to 2023 (Inness et\
  \ al., 2019). Daily average values were computed to produce the statistics."
exposure: []
extra_attributions: []
hazard:
  calculation_method: inferred
  disaster_identifiers: ''
  hazard_analysis_type: empirical
  hazard_type: strong_wind
  intensity: MHI:-
  occurrence_range: ''
  processes: extratropical_cyclone
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
  description: CAMS global reanalysis EAC4 (ECMWF Atmospheric Composition Reanalysis
    4) in netcdf format.
  download_url: https://ads.atmosphere.copernicus.eu/datasets/cams-global-reanalysis-eac4
  format: NetCDF (nc)
  id: resource_jb84s2Hu
  media_type: null
  spatial_resolution: 75000
  temporal:
    duration: null
    end: '2023'
    start: '2003'
    temporal_resolution: null
  title: CAMS Reanalysis
- coordinate_system: EPSG:4326
  description: High resolution land cover from ESA's WorldCover data v200. The field
    crops grid points are extracted to describe agricultural regions that could be
    exposed to Tiomena.
  download_url: https://www.resiliencemada.gov.mg/catalogue/#/dataset/1162
  format: GeoTIFF (tif)
  id: resource_ouyEI56f
  media_type: null
  spatial_resolution: 10
  temporal:
    duration: null
    end: '2021'
    start: '2021'
    temporal_resolution: null
  title: Crops location
- coordinate_system: EPSG:4326
  description: WordPop population count dataset for Madagascar (2020). The original
    dataset was aggregated to 10km resolution.
  download_url: https://www.worldpop.org/
  format: GeoTIFF (tif)
  id: resource_eIpuXA7j
  media_type: null
  spatial_resolution: 10000
  temporal:
    duration: null
    end: '2020'
    start: '2020'
    temporal_resolution: null
  title: Population exposure dataset
risk_data_type:
- hazard
schema: rdl-03
slug: rdls_hzd-mdg_grma_pm10dustproxy
spatial:
  countries:
  - MDG
  scale: national
title: Tiomena Particulate Matter PM10 (CAMS)
version: '1.0'
vulnerability: null
---
