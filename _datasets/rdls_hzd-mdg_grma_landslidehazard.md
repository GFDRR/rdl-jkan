---
attributions: []
catalog: Copernicus Climate Data Store
contact_point:
  affiliation: null
  email: science@axaclimate.com
  name: AXA Climate
  url: https://climate.axa
creator:
  affiliation: null
  email: null
  name: AXA Climate
  url: https://climate.axa
dataset_id: rdls_hzd-mdg_grma_landslidehazard
description: Rainfall-induced landslide hazard index simulated by AXA Climate, for
  SSP2-4.5 and SSP5-8.5 scenarios across three time horizons (baseline, 2050, 2085).
details: The hazard index was built with BRGM landslide susceptibility map and daily
  precipitation dataset.
exposure: []
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: simulated
    event_count: 0
    events: []
    frequency_distribution: user_defined
    hazards:
    - classification: null
      id: hazard_pkvfr1xO
      intensity_measure: LSI:-
      process: landslide_general
      trigger:
        process: pluvial_flood
        type: flood
      type: landslide
    id: event_set_YhkW50SM
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
  This project aimed at updating Madagascar's risk profile, and study the risk's evolution
  under climate change.
referenced_by: []
resources:
- access_url: https://cds.climate.copernicus.eu/datasets/derived-era5-single-levels-daily-statistics?tab=download
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: "Daily precipitation from Copernicus ERA5 at 0.25\xC2\xB0 resolution\
    \ was used for baseline map."
  download_url: null
  format: null
  id: resource_xy57HqTY
  media_type: application/x-hdf5
  spatial: null
  spatial_aggregation: 0.25-degree resolution grid cells
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ERA5 precipitation
- access_url: https://climate.axa
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: GCM precipitation downscaled using AXA Climate proprietary algorithm
    to 0.25 degree resolution for future scenarios (SSP2-4.5 and SSP5-8.5).
  download_url: null
  format: null
  id: resource_downscaled_precip
  media_type: application/x-hdf5
  spatial: null
  spatial_aggregation: 0.25-degree resolution grid cells
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Downscaled precipitation on ERA5 dataset
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-mdg_grma_landslidehazard
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
title: Rainfall-induced landslide hazard
version: '1.0'
vulnerability: null
---
