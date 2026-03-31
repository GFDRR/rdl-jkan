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
dataset_id: rdls_hev-mdg_grma_wildfirerisk
description: Comprehensive wildfire risk assessment including fire frequency, fire
  intensity, Fire Weather Index (FWI), burned area, population exposure, and economic
  losses, for SSP2-4.5 and SSP5-8.5 at baseline, 2050, and 2085.
details: Fire frequency and intensity were extracted from MODIS MOD14/MYD14 products,
  averaged over the annual fire season (September-November period), and simulated
  for historical and future scenarios by CLIMADA in Madagascar. The Fire Weather Index
  (FWI) was computed from daily air temperature, wind speed, precipitation, and relative
  humidity. Burned area was estimated from fire frequency hazard combined with forest
  cover exposure (ESA WorldCover). Economic losses were estimated using fire intensity
  hazard combined with CLIMADA's LitPop economic exposure dataset and a vulnerability
  curve developed by Luthi et al. Population exposure was estimated using fire frequency
  hazard combined with WorldPop population count data and a binary vulnerability curve.
exposure:
- category: natural_environment
  dimension: content
  quantity_kind: area
  taxonomy: null
- category: population
  dimension: population
  quantity_kind: count
  taxonomy: null
- category: economic_indicator
  dimension: product
  quantity_kind: monetary
  taxonomy: null
extra_attributions: []
hazard:
  calculation_method: simulated
  disaster_identifiers: ''
  hazard_analysis_type: probabilistic
  hazard_type: wildfire
  intensity: MHI:-
  occurrence_range: ''
  processes: wildfire
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
  description: Daily fire frequency extracted from MODIS MOD14/MYD14 products, averaged
    over the annual fire season (September-November period) and simulated for historical
    and future scenarios by CLIMADA.
  download_url: https://www.resiliencemada.gov.mg
  format: NetCDF (nc)
  id: resource_fire_frequency
  media_type: null
  spatial_resolution: 1000
  temporal:
    duration: null
    end: null
    start: null
    temporal_resolution: P1M
  title: Fire frequency
- coordinate_system: EPSG:4326
  description: Daily fire intensity extracted from MODIS MOD14/MYD14 products, averaged
    over the annual fire season (September-November period) and simulated for historical
    and future scenarios by CLIMADA.
  download_url: https://www.resiliencemada.gov.mg
  format: NetCDF (nc)
  id: resource_fire_intensity
  media_type: null
  spatial_resolution: 1000
  temporal:
    duration: null
    end: null
    start: null
    temporal_resolution: P1M
  title: Fire intensity
- coordinate_system: EPSG:4326
  description: The FWI was computed from the daily air temperature, wind speed, precipitation,
    and relative humidity. Daily FWI was averaged at annual fire season scale defined
    as the period from September to November.
  download_url: https://www.resiliencemada.gov.mg
  format: NetCDF (nc)
  id: resource_fwi
  media_type: null
  spatial_resolution: 25000
  temporal:
    duration: null
    end: null
    start: null
    temporal_resolution: P1M
  title: Fire Weather Index (FWI)
- coordinate_system: EPSG:4326
  description: European Space Agency (ESA) WorldCover 10m 2020 v100, used to derive
    forest cover exposure for burned area estimation.
  download_url: https://esa-worldcover.org/en
  format: GeoTIFF (tif)
  id: resource_esa_landcover
  media_type: null
  spatial_resolution: 10
  temporal: null
  title: ESA WorldCover 10m 2020
- coordinate_system: EPSG:4326
  description: CLIMADA's economic dataset (LitPop) combines night light intensity
    and population density to spatially distribute macroeconomic indicators such as
    GDP, produced capital, or total asset value.
  download_url: https://climada-petals.readthedocs.io/en/stable/tutorial/climada_exposures_LitPop.html
  format: GeoTIFF (tif)
  id: resource_litpop_gdp
  media_type: null
  spatial_resolution: 1000
  temporal: null
  title: CLIMADA LitPop economic exposure
- coordinate_system: EPSG:4326
  description: WorldPop population count dataset for Madagascar at 100m resolution,
    upscaled at 4km resolution in the wildfire risk model.
  download_url: https://hub.worldpop.org/geodata/summary?id=74234
  format: GeoTIFF (tif)
  id: resource_worldpop
  media_type: null
  spatial_resolution: 100
  temporal:
    duration: null
    end: '2020'
    start: '2020'
    temporal_resolution: null
  title: WorldPop population count
- coordinate_system: EPSG:4326
  description: Daily climate variables (temperature, wind speed, precipitation, relative
    humidity) computed by AXA Climate from CMIP6 and ERA5 datasets, used as inputs
    for Fire Weather Index calculation.
  download_url: https://www.resiliencemada.gov.mg
  format: NetCDF (nc)
  id: resource_cmip6_climate
  media_type: null
  spatial_resolution: 25000
  temporal:
    duration: null
    end: null
    start: null
    temporal_resolution: P1M
  title: CMIP6/ERA5 climate variables for FWI
risk_data_type:
- hazard
- exposure
- vulnerability
schema: rdl-03
slug: rdls_hev-mdg_grma_wildfirerisk
spatial:
  countries:
  - MDG
  scale: national
title: Wildfire Risk Assessment for Madagascar
version: '1.0'
vulnerability:
  approach: empirical
  base_data_type: inferred
  category: economic_indicator, natural_environment, population
  dimension: ''
  function_type: ''
  hazard_analysis_type: empirical
  hazard_primary: wildfire
  hazard_process_primary: ''
  hazard_process_secondary: ''
  hazard_secondary: ''
  intensity: ''
  metric: exposure_to_hazard, loss_ratio
  relationship: math_parametric
  taxonomy: ''
  unit: ''
---
