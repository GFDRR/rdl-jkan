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
dataset_id: rdls_hev-mdg_grma_agriculturaldroughtrisk
description: This dataset contains all drought-risk layers for maize, rice, cassava,
  peanut, and livestock (grassland proxy) in Madagascar, covering SSP2-4.5 and SSP5-8.5
  scenarios at baseline, 2050, and 2085 time horizons.
details: For maize, rice, cassava, and peanut, the risk indicator is composed of a
  combined drought-hazard index called the Crop-specific Drought Index (CsDI), developed
  by AXA Climate based on indicators of physical drought, water availability across
  the territory, and each crop's relative water requirements. Vulnerability for these
  crops is based on empirical impact curves of the average potential annual yield
  loss. For livestock (grassland proxy), the risk indicator uses a grassland production
  index developed by AXA Climate based on actual evapotranspiration and growing degree
  days, with vulnerability based on a theoretical impact curve of potential yield
  loss as a function of grazing events. Exposure is calculated over the entire territory
  for crops and over grassland territory (ESA World Cover 2021) for livestock.
exposure:
- category: agriculture
  dimension: content
  quantity_kind: area
  taxonomy: null
extra_attributions: []
hazard:
  calculation_method: inferred
  disaster_identifiers: ''
  hazard_analysis_type: deterministic
  hazard_type: drought
  intensity: MHI:-
  occurrence_range: ''
  processes: agricultural_drought
  seasonality: user_defined
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
  description: SPEI-6 intensity computed by AXA Climate based on monthly precipitation
    and potential evapotranspiration variables from CMIP6 and ERA5 datasets
  download_url: https://www.resiliencemada.gov.mg
  format: NetCDF (nc)
  id: resource_spei6
  media_type: null
  spatial_resolution: 25000
  temporal:
    duration: null
    end: null
    start: null
    temporal_resolution: P1M
  title: SPEI-6 Intensity (NetCDF format)
- coordinate_system: EPSG:4326
  description: Aridity Index computed by AXA Climate based on monthly precipitation
    and potential evapotranspiration variables from CMIP6 and ERA5 datasets
  download_url: https://www.resiliencemada.gov.mg
  format: GeoTIFF (tif)
  id: resource_aridity_idx
  media_type: null
  spatial_resolution: 25000
  temporal: null
  title: Aridity Index (GeoTIFF format)
- coordinate_system: EPSG:4326
  description: Potential water needs per crop computed by AXA Climate based on daily
    reference evapotranspiration and crop coefficient (daily Kc). Climate and meteorogological
    variables from CMIP6 and ERA5 datasets
  download_url: https://www.resiliencemada.gov.mg
  format: GeoTIFF (tif)
  id: resource_crop_water_needs
  media_type: null
  spatial_resolution: 25000
  temporal: null
  title: Potential water needs per crop (GeoTIFF format)
- coordinate_system: EPSG:4326
  description: Water Stress Index by World Resource Institute based HypflowsCI6 dataset
  download_url: https://www.wri.org/aqueduct
  format: GeoTIFF (tif)
  id: resource_water_stress
  media_type: null
  spatial_resolution: 25000
  temporal: null
  title: Water Stress Index (GeoTIFF format)
- coordinate_system: EPSG:4326
  description: Grassland production index computed by AXA Climate based on two intermediate
    indicators, namely standardized actual evapotranspiration and standardized growing
    degree days. Both indicators have been calculated using specific variety parameters
    (local grassland variety) and soil data (SoilGrids). Climate and meteorogological
    variables from CMIP6 and ERA5 datasets
  download_url: https://www.resiliencemada.gov.mg
  format: GeoTIFF (tif)
  id: resource_grassland_prod
  media_type: null
  spatial_resolution: 25000
  temporal: null
  title: Grassland production index (GeoTIFF format)
risk_data_type:
- hazard
- exposure
- vulnerability
schema: rdl-03
slug: rdls_hev-mdg_grma_agriculturaldroughtrisk
spatial:
  countries:
  - MDG
  scale: national
title: Agricultural Drought Risk Assessment for Madagascar
version: '1.0'
vulnerability:
  approach: judgement
  base_data_type: inferred
  category: agriculture
  dimension: ''
  function_type: ''
  hazard_analysis_type: empirical
  hazard_primary: drought
  hazard_process_primary: ''
  hazard_process_secondary: ''
  hazard_secondary: ''
  intensity: ''
  metric: loss_ratio
  relationship: math_parametric
  taxonomy: ''
  unit: ''
---
