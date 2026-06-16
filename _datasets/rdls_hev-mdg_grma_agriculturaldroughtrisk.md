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
- asset_type: null
  category: agriculture
  id: exposure_agriculture_001
  metrics:
  - dimension: content
    id: metric_area_001
    measurement:
      quantity_kind: area
      unit: null
hazard:
  event_sets:
  - analysis_type: deterministic
    calculation_method: inferred
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_drought_001
      intensity_measure: MHI:-
      process: agricultural_drought
      trigger: null
      type: drought
    id: event_set_drought_001
    occurrence_range: null
    seasonality: user_defined
license: https://creativecommons.org/licenses/by/4.0/
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
  description: SPEI-6 intensity computed by AXA Climate based on monthly precipitation
    and potential evapotranspiration variables from CMIP6 and ERA5 datasets
  download_url: null
  format: null
  id: resource_spei6
  media_type: application/netcdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 25000
  temporal: null
  temporal_resolution: P1M
  title: SPEI-6 Intensity (NetCDF format)
- access_url: https://www.resiliencemada.gov.mg
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Aridity Index computed by AXA Climate based on monthly precipitation
    and potential evapotranspiration variables from CMIP6 and ERA5 datasets
  download_url: null
  format: null
  id: resource_aridity_idx
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 25000
  temporal: null
  temporal_resolution: null
  title: Aridity Index (GeoTIFF format)
- access_url: https://www.resiliencemada.gov.mg
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Potential water needs per crop computed by AXA Climate based on daily
    reference evapotranspiration and crop coefficient (daily Kc). Climate and meteorogological
    variables from CMIP6 and ERA5 datasets
  download_url: null
  format: null
  id: resource_crop_water_needs
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 25000
  temporal: null
  temporal_resolution: null
  title: Potential water needs per crop (GeoTIFF format)
- access_url: https://www.wri.org/aqueduct
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Agricultural Drought Risk Assessment for Madagascar (Water Stress Index
    by World Resource Institute based HypflowsCI6 dataset)
  download_url: null
  format: null
  id: resource_water_stress
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 25000
  temporal: null
  temporal_resolution: null
  title: Water Stress Index (GeoTIFF format)
- access_url: https://www.resiliencemada.gov.mg
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Grassland production index computed by AXA Climate based on two intermediate
    indicators, namely standardized actual evapotranspiration and standardized growing
    degree days. Both indicators have been calculated using specific variety parameters
    (local grassland variety) and soil data (SoilGrids). Climate and meteorogological
    variables from CMIP6 and ERA5 datasets
  download_url: null
  format: null
  id: resource_grassland_prod
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 25000
  temporal: null
  temporal_resolution: null
  title: Grassland production index (GeoTIFF format)
risk_data_type:
- hazard
- exposure
- vulnerability
schema: rdls-10
slug: rdls_hev-mdg_grma_agriculturaldroughtrisk
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
title: Agricultural Drought Risk Assessment for Madagascar
version: '1.0'
vulnerability:
  functions:
    damage_to_loss: []
    engineering_demand: []
    fragility: []
    socio_economic: []
    vulnerability:
    - analysis_details: Empirical vulnerability curves of average potential yield
        loss per year for maize, rice, cassava, and peanut, as a function of the Crop-specific
        Drought Index (CsDI)
      approach: judgement
      category: agriculture
      hazard_analysis_type: empirical
      hazard_primary:
        classification: null
        id: hazard_drought
        intensity_measure: MHI:-
        process: null
        trigger: null
        type: drought
      hazard_secondary: null
      id: vuln_crop_yield_loss
      impact:
        measurement:
          quantity_kind: dimensionless_ratio
          unit: percent
        metric: loss_ratio
        modelling: inferred
        type: direct
      relationship: math_parametric
      taxonomy: null
    - analysis_details: Empirical vulnerability curve of average potential production
        loss per year for livestock (grassland proxy), as a function of grazing events
      approach: judgement
      category: agriculture
      hazard_analysis_type: empirical
      hazard_primary:
        classification: null
        id: hazard_drought
        intensity_measure: DSCI:-
        process: null
        trigger: null
        type: drought
      hazard_secondary: null
      id: vuln_livestock_prod_loss
      impact:
        measurement:
          quantity_kind: dimensionless_ratio
          unit: percent
        metric: loss_ratio
        modelling: inferred
        type: indirect
      relationship: math_parametric
      taxonomy: null
---
