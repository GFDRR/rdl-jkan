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
dataset_id: rdls_hevl-mdg_grma_coastalerosionrisk
description: Comprehensive coastal erosion risk assessment for Madagascar, integrating
  hazard polygons delineating projected erosion extents, economic loss estimates (GDP),
  and population displacement impacts at the commune level (ADM3). The assessment
  covers future time horizons (2050 and 2085) under socioeconomic pathways SSP2 and
  SSP5, combining coastal erosion projections with spatially distributed economic
  and demographic exposure data and binary impact modelling.
details: 'This dataset merges three components of Madagascar''s coastal erosion risk
  profile. Hazard: Erosion footprints derived from post-processing of LISCOAST projections
  (Vousdoukas et al., 2019), accounting for ambient coastline dynamics, shoreline
  retreat due to sea-level rise, and storm-induced erosion (RP100). Erosion distances
  along coastal transects (~500 m spacing) were interpolated and combined with the
  baseline shoreline (OSM 2020) to generate polygons. Economic exposure: Spatial GDP
  distribution from LitPop (2020) for baseline and Wang et al. (2023) SSP-based 1
  km gridded GDP projections for future scenarios. Population exposure: WorldPop (2020)
  gridded population at 100 m resolution, validated against INSTAT administrative
  counts, with Wang et al. (2022) SSP-based 1 km population projections for future
  scenarios. Vulnerability: Binary impact model whereby all assets and population
  within projected erosion extents are considered fully affected.'
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
  calculation_method: ''
  disaster_identifiers: ''
  hazard_analysis_type: deterministic
  hazard_type: coastal_flood
  intensity: AA:km2
  occurrence_range: ''
  processes: coastal_flood
  seasonality: ''
license: CC-BY-4.0
loss:
  approach: ''
  base_data_type: ''
  category: ''
  description: Population displaced due to coastal erosion per commune, Total GDP
    lost within projected erosion extents per commune
  dimension: ''
  exposure_id: ''
  hazard_analysis_type: ''
  hazard_id: ''
  hazard_process: coastal_flood
  hazard_type: coastal_flood
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
  This project aimed at updating Madagascar's risk profile and assessing risk evolution
  under climate change.
resources:
- coordinate_system: EPSG:4326
  description: Polygons delineating projected coastal areas expected to undergo erosion
    under future time horizons (2050 and 2085) and socioeconomic pathways (SSP2 and
    SSP5), derived from LISCOAST projections.
  download_url: https://www.resiliencemada.gov.mg/catalogue/uuid/5d02d6ab-a914-4842-ac5c-349b14e0c7a9
  format: GeoPackage (gpkg)
  id: resource_ce_hazard_polygons
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Coastal Erosion - Hazard Polygons
- coordinate_system: EPSG:4326
  description: Aggregated economic loss (GDP) due to projected coastal erosion at
    the commune level (ADM3) in Madagascar, for different time horizons and socioeconomic
    pathways.
  download_url: https://www.resiliencemada.gov.mg/catalogue/uuid/5d02d6ab-a914-4842-ac5c-349b14e0c7a9
  format: GeoPackage (gpkg)
  id: resource_ce_economic_risk
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Coastal Erosion - Economic Risk per Commune
- coordinate_system: EPSG:4326
  description: Aggregated affected population due to projected coastal erosion at
    the commune level (ADM3) in Madagascar, for different time horizons and socioeconomic
    pathways.
  download_url: https://www.resiliencemada.gov.mg/catalogue/uuid/5d02d6ab-a914-4842-ac5c-349b14e0c7a9
  format: GeoPackage (gpkg)
  id: resource_ce_population_risk
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Coastal Erosion - Population Impacts per Commune
risk_data_type:
- hazard
- exposure
- vulnerability
- loss
schema: rdl-03
slug: rdls_hevl-mdg_grma_coastalerosionrisk
spatial:
  countries:
  - MDG
  scale: national
title: Coastal Erosion Risk Assessment for Madagascar
version: '1.0'
vulnerability:
  approach: empirical
  base_data_type: inferred, simulated
  category: economic_indicator, population
  dimension: ''
  function_type: ''
  hazard_analysis_type: deterministic
  hazard_primary: coastal_flood
  hazard_process_primary: ''
  hazard_process_secondary: ''
  hazard_secondary: ''
  intensity: ''
  metric: displaced_count, economic_loss_value
  relationship: discrete
  taxonomy: ''
  unit: ''
---
