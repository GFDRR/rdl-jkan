---
catalog: null
contact_point:
  email: alvaro.prida@axaclimate.com
  id: attribution_contact_point_001
  name: Alvaro Prida
  url: null
creator:
  email: null
  id: attribution_creator_001
  name: AXA Climate
  url: https://climate.axa
dataset_id: rdls_hevl-mdg_grma_fluvialfloodrisk
description: Comprehensive fluvial flood risk assessment for Madagascar, integrating
  flood hazard maps (maximum depth rasters), economic loss estimates (GDP), and population
  impact assessments at the commune level (ADM3). The assessment covers historical
  conditions and projected future scenarios (2050 and 2085) under multiple socioeconomic
  pathways, combining hydrodynamic flood simulations with spatially distributed economic
  and demographic exposure data and flood damage functions.
details: 'This dataset merges three components of Madagascar''s fluvial flood risk
  profile. Hazard: Maximum flood depth rasters (30 m resolution) produced by simulating
  design flood events across eight return periods with the hydrodynamic model SFINCS,
  forced by boundary condition hydrographs from the hydrological model WFlow. Historical
  simulations (1998-2024) used observed GPM precipitation; future simulations used
  ISIMIP3b discharge projections. Economic exposure: Spatial GDP distribution from
  LitPop (2020) for baseline and Wang et al. (2023) SSP-based 1 km gridded GDP projections
  for future scenarios. Population exposure: WorldPop (2020) gridded population at
  100 m resolution, validated against INSTAT administrative counts, with Wang et al.
  (2022) SSP-based 1 km population projections for future scenarios. Vulnerability:
  Flood damage curves for Sub-Saharan Africa (Englhardt et al., 2019) linking flood
  depth to relative asset loss.'
exposure:
- category: economic_indicator
  dimension: product
  quantity_kind: monetary
  taxonomy: null
- category: population
  dimension: population
  quantity_kind: count
  taxonomy: null
extra_attributions: []
hazard:
  calculation_method: simulated
  disaster_identifiers: ''
  hazard_analysis_type: deterministic
  hazard_type: flood
  intensity: wd:m
  occurrence_range: ''
  processes: fluvial_flood
  seasonality: ''
license: CC-BY-4.0
loss:
  approach: ''
  base_data_type: ''
  category: ''
  description: Annual average GDP loss from fluvial flooding per commune, Annual average
    affected population from fluvial flooding per commune
  dimension: ''
  exposure_id: ''
  hazard_analysis_type: ''
  hazard_id: ''
  hazard_process: fluvial_flood
  hazard_type: flood
  impact_metric: ''
  impact_type: ''
  impact_unit: ''
  type: ''
  vulnerability_id: ''
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
  description: Maximum flood depth rasters (30-meter resolution) produced by simulating
    design flood events with the hydrodynamic model SFINCS, forced by boundary condition
    hydrographs from WFlow. Covers historical and projected conditions across eight
    return periods.
  download_url: https://www.resiliencemada.gov.mg/catalogue/uuid/b5d5de9e-843a-4384-84f3-6b8d4e1baae9
  format: GeoTIFF (tif)
  id: resource_fl_hazard_maps
  media_type: null
  spatial_resolution: 30
  temporal: null
  title: Fluvial Flood - Hazard Maps
- coordinate_system: EPSG:4326
  description: Aggregated annual average economic loss (GDP) due to fluvial flooding
    at the commune level (ADM3) in Madagascar, for different time horizons and socioeconomic
    pathways.
  download_url: https://www.resiliencemada.gov.mg/catalogue/uuid/b5d5de9e-843a-4384-84f3-6b8d4e1baae9
  format: GeoPackage (gpkg)
  id: resource_fl_economic_risk
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Fluvial Flood - Economic Risk per Commune
- coordinate_system: EPSG:4326
  description: Aggregated annual average affected population due to fluvial flooding
    at the commune level (ADM3) in Madagascar, for different time horizons and socioeconomic
    pathways.
  download_url: https://www.resiliencemada.gov.mg/catalogue/uuid/bdf20e69-7399-4079-8cdd-396f38176a36
  format: GeoPackage (gpkg)
  id: resource_fl_population_risk
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Fluvial Flood - Population Impacts per Commune
risk_data_type:
- hazard
- exposure
- vulnerability
- loss
schema: rdl-03
slug: rdls_hevl-mdg_grma_fluvialfloodrisk
spatial:
  countries:
  - MDG
  scale: national
title: Fluvial Flood Risk Assessment for Madagascar
version: '1.0'
vulnerability:
  approach: hybrid
  base_data_type: simulated
  category: economic_indicator, population
  dimension: ''
  function_type: ''
  hazard_analysis_type: deterministic
  hazard_primary: flood
  hazard_process_primary: fluvial_flood
  hazard_process_secondary: ''
  hazard_secondary: ''
  intensity: ''
  metric: damage_ratio, loss_annual_average_value
  relationship: math_bespoke
  taxonomy: ''
  unit: ''
---
