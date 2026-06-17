---
attributions: []
catalog: null
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
- asset_type: null
  category: natural_environment
  id: exposure_forest_001
  metrics:
  - dimension: content
    id: metric_forest_area
    measurement:
      quantity_kind: area
      unit: null
- asset_type: null
  category: population
  id: exposure_population_001
  metrics:
  - dimension: population
    id: metric_pop_count
    measurement:
      quantity_kind: count
      unit: count
- asset_type: null
  category: economic_indicator
  id: exposure_economic_001
  metrics:
  - dimension: product
    id: metric_gdp
    measurement:
      quantity_kind: currency
      unit: USD
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: simulated
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_wildfire_001
      intensity_measure: MHI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: event_set_wildfire_001
    occurrence_range: null
    seasonality: user_defined
  type: wildfire
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
- access_url: https://www.resiliencemada.gov.mg
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Daily fire frequency extracted from MODIS MOD14/MYD14 products, averaged
    over the annual fire season (September-November period) and simulated for historical
    and future scenarios by CLIMADA.
  download_url: null
  format: null
  id: resource_fire_frequency
  media_type: application/netcdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 1000
  temporal: null
  temporal_resolution: P1M
  title: Fire frequency
- access_url: https://www.resiliencemada.gov.mg
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Daily fire intensity extracted from MODIS MOD14/MYD14 products, averaged
    over the annual fire season (September-November period) and simulated for historical
    and future scenarios by CLIMADA.
  download_url: null
  format: null
  id: resource_fire_intensity
  media_type: application/netcdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 1000
  temporal: null
  temporal_resolution: P1M
  title: Fire intensity
- access_url: https://www.resiliencemada.gov.mg
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: The FWI was computed from the daily air temperature, wind speed, precipitation,
    and relative humidity. Daily FWI was averaged at annual fire season scale defined
    as the period from September to November.
  download_url: null
  format: null
  id: resource_fwi
  media_type: application/netcdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 25000
  temporal: null
  temporal_resolution: P1M
  title: Fire Weather Index (FWI)
- access_url: https://esa-worldcover.org/en
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: European Space Agency (ESA) WorldCover 10m 2020 v100, used to derive
    forest cover exposure for burned area estimation.
  download_url: null
  format: null
  id: resource_esa_landcover
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: 10m resolution grid cells (ESA WorldCover 2020)
  spatial_resolution: 10
  temporal: null
  temporal_resolution: null
  title: ESA WorldCover 10m 2020
- access_url: https://climada-petals.readthedocs.io/en/stable/tutorial/climada_exposures_LitPop.html
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: CLIMADA's economic dataset (LitPop) combines night light intensity
    and population density to spatially distribute macroeconomic indicators such as
    GDP, produced capital, or total asset value.
  download_url: null
  format: null
  id: resource_litpop_gdp
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 1000
  temporal: null
  temporal_resolution: null
  title: CLIMADA LitPop economic exposure
- access_url: https://hub.worldpop.org/geodata/summary?id=74234
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: WorldPop population count dataset for Madagascar at 100m resolution,
    upscaled at 4km resolution in the wildfire risk model.
  download_url: null
  format: null
  id: resource_worldpop
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: 4km resolution grid cells (upscaled from WorldPop 100m)
  spatial_resolution: 100
  temporal:
    central_year: null
    duration: null
    end: '2020'
    start: '2020'
  temporal_resolution: null
  title: WorldPop population count
- access_url: https://www.resiliencemada.gov.mg
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Daily climate variables (temperature, wind speed, precipitation, relative
    humidity) computed by AXA Climate from CMIP6 and ERA5 datasets, used as inputs
    for Fire Weather Index calculation.
  download_url: null
  format: null
  id: resource_cmip6_climate
  media_type: application/netcdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 25000
  temporal: null
  temporal_resolution: P1M
  title: CMIP6/ERA5 climate variables for FWI
risk_data_type:
- hazard
- exposure
- vulnerability
schema: rdls-10
slug: rdls_hev-mdg_grma_wildfirerisk
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
title: Wildfire Risk Assessment for Madagascar
version: '1.0'
vulnerability:
  functions:
    damage_to_loss: []
    engineering_demand: []
    fragility: []
    socio_economic: []
    vulnerability:
    - analysis_details: Binary vulnerability curve for burned area as a function of
        fire frequency
      approach: empirical
      category: natural_environment
      hazard_analysis_type: empirical
      hazard_primary:
        classification: null
        id: hazard_wildfire
        intensity_measure: MHI:-
        process: null
        trigger: null
        type: wildfire
      hazard_secondary: null
      id: vuln_burned_area
      impact:
        measurement:
          quantity_kind: dimensionless_ratio
          unit: percent
        metric: loss_ratio
        modelling: inferred
        type: direct
      relationship: math_parametric
      taxonomy: null
    - analysis_details: Vulnerability curve of average economic losses as a function
        of fire intensity, developed by Luthi et al.
      approach: empirical
      category: economic_indicator
      hazard_analysis_type: empirical
      hazard_primary:
        classification: null
        id: hazard_wildfire
        intensity_measure: MHI:-
        process: null
        trigger: null
        type: wildfire
      hazard_secondary: null
      id: vuln_economic_loss
      impact:
        measurement:
          quantity_kind: dimensionless_ratio
          unit: percent
        metric: loss_ratio
        modelling: inferred
        type: direct
      relationship: math_parametric
      taxonomy: null
    - analysis_details: Binary vulnerability curve of impacted population as a function
        of fire frequency
      approach: empirical
      category: population
      hazard_analysis_type: empirical
      hazard_primary:
        classification: null
        id: hazard_wildfire
        intensity_measure: MHI:-
        process: null
        trigger: null
        type: wildfire
      hazard_secondary: null
      id: vuln_population_impact
      impact:
        measurement:
          quantity_kind: dimensionless_ratio
          unit: percent
        metric: exposure
        modelling: inferred
        type: direct
      relationship: math_parametric
      taxonomy: null
---
