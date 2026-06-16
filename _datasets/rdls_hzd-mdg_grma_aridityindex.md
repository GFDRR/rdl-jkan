---
attributions: []
catalog: Copernicus Climate Data Store
contact_point:
  affiliation: null
  email: science@axaclimate.com
  name: AXA Climate
  url: null
creator:
  affiliation: null
  email: null
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
hazard:
  event_sets:
  - analysis_type: deterministic
    calculation_method: inferred
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_aridity_001
      intensity_measure: MHI:-
      process: meteorological_drought
      trigger: null
      type: drought
    id: event_set_aridity_001
    occurrence_range: null
    seasonality: null
license: CC-BY-4.0
lineage: null
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project:
  name: GRMA Madagascar - Phase 1
  url: https://www.resiliencemada.gov.mg
publisher:
  affiliation: null
  email: null
  name: Global Risk Modelling Alliance
  url: https://grma.global
purpose: This dataset was developed during the first phase of GRMA's project in Madagascar.
  This project aimed at updating Madagascar's risk profile, and see the risk evolution
  under climate change.
referenced_by:
- author_names:
  - Allen, R. G., Pereira, L. S., Raes, D. & Smith, M.
  date_published: null
  doi: ISBN 92-5-104219-5
  id: reference_cbmKA37P
  name: "Crop Evapotranspiration \xE2\u20AC\u201D Guidelines for Computing Crop Water\
    \ Requirements"
  url: https://www.fao.org/4/x0490e/x0490e00.htm#Contents
resources:
- access_url: https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: ECMWF's reanalysis data. The daily precipitation, temperature, relative
    humidity, solar radiation and wind are used to compute the aridity index.
  download_url: https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels
  format: null
  id: resource_era5_001
  media_type: application/netcdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 25000
  temporal:
    central_year: null
    duration: null
    end: '2014'
    start: '1985'
  temporal_resolution: null
  title: ERA5 reanalysis data
- access_url: https://esgf-node.ipsl.upmc.fr/projects/cmip6-ipsl/
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: High resolution statistically downscaled CMIP6 climate model data.
    The daily precipitation, temperature, relative humidity, solar radiation and wind
    are used to compute the aridity index.
  download_url: https://esgf-node.ipsl.upmc.fr/projects/cmip6-ipsl/
  format: null
  id: resource_cmip6_001
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 25000
  temporal:
    central_year: null
    duration: null
    end: '2100'
    start: '1985'
  temporal_resolution: null
  title: CMIP6 climate model data
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-mdg_grma_aridityindex
spatial:
  bbox: null
  centroid: null
  countries:
  - MDG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Tiomena Seasonal Aridity Index
version: '1.0'
vulnerability: null
---
