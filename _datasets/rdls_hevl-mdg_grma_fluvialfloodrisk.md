---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: alvaro.prida@axaclimate.com
  name: Alvaro Prida
  url: null
creator:
  affiliation: null
  email: null
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
- asset_type: null
  category: economic_indicator
  id: exposure_economic_001
  metrics:
  - dimension: product
    id: metric_gdp
    measurement:
      quantity_kind: currency
      unit: USD
- asset_type: null
  category: population
  id: exposure_population_001
  metrics:
  - dimension: population
    id: metric_pop
    measurement:
      quantity_kind: count
      unit: count
hazard:
  event_sets:
  - analysis_type: deterministic
    calculation_method: simulated
    event_count: 0
    events: []
    frequency_distribution: generalized_extreme_value
    hazards:
    - classification: null
      id: hazard_fl_001
      intensity_measure: wd:m
      process: fluvial_flood
      trigger:
        process: fluvial_flood
        type: flood
      type: flood
    id: event_set_fl_001
    occurrence_range: null
    seasonality: null
  type: flood
license: CC-BY-4.0
lineage:
  description: null
  sources:
  - id: source_fl_sfincs
    license: https://opensource.org/licenses/MIT
    name: SFINCS hydrodynamic model
    risk_data_type: null
    type: model
    url: https://sfincs.readthedocs.io/en/latest/
    used_in: hazard
  - id: source_fl_wflow
    license: https://opensource.org/licenses/MIT
    name: WFlow hydrological model
    risk_data_type: null
    type: model
    url: https://deltares.github.io/Wflow.jl/dev/
    used_in: hazard
  - id: source_fl_hazard_layers
    license: CC-BY-4.0
    name: Flood hazard layers for Madagascar
    risk_data_type: null
    type: dataset
    url: https://www.resiliencemada.gov.mg/catalogue/uuid/b5d5de9e-843a-4384-84f3-6b8d4e1baae9
    used_in: hazard
  - id: source_fl_litpop_gdp
    license: CC-BY-4.0
    name: LitPop GDP (2020)
    risk_data_type: null
    type: dataset
    url: https://climada-python.readthedocs.io/en/stable/user-guide/climada_entity_LitPop.html
    used_in: exposure
  - id: source_fl_projected_gdp
    license: CC-BY-4.0
    name: "Projected 1 km GDP distributions (2020\u20132100) under SSPs"
    risk_data_type: null
    type: dataset
    url: https://zenodo.org/records/7898409
    used_in: exposure
  - id: source_fl_worldpop
    license: CC-BY-4.0
    name: WorldPop Population (2020)
    risk_data_type: null
    type: dataset
    url: https://hub.worldpop.org/geodata/summary?id=49697
    used_in: exposure
  - id: source_fl_instat
    license: CC-BY-4.0
    name: INSTAT Population (Madagascar)
    risk_data_type: null
    type: dataset
    url: null
    used_in: exposure
  - id: source_fl_projected_pop
    license: CC-BY-4.0
    name: "Projected 1 km population distributions (2020\u20132100) under SSPs"
    risk_data_type: null
    type: dataset
    url: https://figshare.com/articles/dataset/Projecting_1_km-grid_population_distributions_from_2020_to_2100_globally_under_shared_socioeconomic_pathways/19608594
    used_in: exposure
  - id: source_fl_damage_curves
    license: CC-BY-4.0
    name: Flood damage curves for Sub-Saharan Africa
    risk_data_type: null
    type: dataset
    url: https://nhess.copernicus.org/articles/19/1703/2019/
    used_in: vulnerability
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss:
  losses:
  - asset_category: economic_indicator
    asset_dimension: product
    description: Annual average GDP loss from fluvial flooding per commune
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_fl_economic
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: USD
        metric: damage
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: deterministic
      loss_type: gross
  - asset_category: population
    asset_dimension: population
    description: Annual average affected population from fluvial flooding per commune
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_fl_population
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: deterministic
      loss_type: count
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
  - Prida, A. et al.
  date_published: null
  doi: null
  id: reference_fl_grma_report
  name: "Rapport m\xE9thodologique (GRMA) - English version"
  url: https://www.resiliencemada.gov.mg/catalogue/#/document/1290
- author_names:
  - Eberenz, S., et al.
  date_published: null
  doi: null
  id: reference_fl_litpop
  name: 'LitPop GDP: High-Resolution Gridded GDP Based on Lights and Population'
  url: https://climada-python.readthedocs.io/en/stable/user-guide/climada_entity_LitPop.html
- author_names:
  - Wang, T., Sun, F.
  date_published: '2022-10-07'
  doi: https://doi.org/10.1038/s41597-022-01300-x
  id: reference_fl_wang_gdp
  name: Projecting 1 km-grid GDP distributions from 2020 to 2100 under Shared Socioeconomic
    Pathways
  url: https://www.nature.com/articles/s41597-022-01300-x
- author_names:
  - Englhardt et al.
  date_published: null
  doi: https://doi.org/10.5194/nhess-19-1703-2019
  id: reference_fl_englhardt
  name: Enhancement of large-scale flood risk assessments using building-material-based
    vulnerability curves for an object-based approach in urban and rural areas
  url: https://nhess.copernicus.org/articles/19/1703/2019/
- author_names:
  - WorldPop Project
  date_published: null
  doi: null
  id: reference_fl_worldpop
  name: WorldPop Population Count Dataset, Madagascar 2020
  url: https://hub.worldpop.org/geodata/summary?id=49697
- author_names:
  - Wang, T., Sun, F.
  date_published: '2022-04-20'
  doi: https://doi.org/10.1038/s41597-022-01675-x
  id: reference_fl_wang_pop
  name: Projecting 1 km-grid population distributions from 2020 to 2100 globally under
    shared socioeconomic pathways
  url: https://www.nature.com/articles/s41597-022-01675-x
resources:
- access_url: https://www.resiliencemada.gov.mg/catalogue/uuid/b5d5de9e-843a-4384-84f3-6b8d4e1baae9
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Maximum flood depth rasters (30-meter resolution) produced by simulating
    design flood events with the hydrodynamic model SFINCS, forced by boundary condition
    hydrographs from WFlow. Covers historical and projected conditions across eight
    return periods.
  download_url: null
  format: null
  id: resource_fl_hazard_maps
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: 30-metre resolution grid cells
  spatial_resolution: 30
  temporal: null
  temporal_resolution: null
  title: Fluvial Flood - Hazard Maps
- access_url: https://www.resiliencemada.gov.mg/catalogue/uuid/b5d5de9e-843a-4384-84f3-6b8d4e1baae9
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Aggregated annual average economic loss (GDP) due to fluvial flooding
    at the commune level (ADM3) in Madagascar, for different time horizons and socioeconomic
    pathways.
  download_url: null
  format: null
  id: resource_fl_economic_risk
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: Commune level (administrative level 3, ADM3)
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Fluvial Flood - Economic Risk per Commune
- access_url: https://www.resiliencemada.gov.mg/catalogue/uuid/bdf20e69-7399-4079-8cdd-396f38176a36
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Aggregated annual average affected population due to fluvial flooding
    at the commune level (ADM3) in Madagascar, for different time horizons and socioeconomic
    pathways.
  download_url: null
  format: null
  id: resource_fl_population_risk
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: Commune level (administrative level 3, ADM3)
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Fluvial Flood - Population Impacts per Commune
risk_data_type:
- hazard
- exposure
- vulnerability
- loss
schema: rdls-10
slug: rdls_hevl-mdg_grma_fluvialfloodrisk
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
title: Fluvial Flood Risk Assessment for Madagascar
version: '1.0'
vulnerability:
  functions:
    damage_to_loss: []
    engineering_demand: []
    fragility: []
    socio_economic: []
    vulnerability:
    - analysis_details: Flood damage curves for Sub-Saharan Africa (Englhardt et al.,
        2019)
      approach: hybrid
      category: economic_indicator
      hazard_analysis_type: deterministic
      hazard_primary:
        classification: null
        id: hazard_flood
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      hazard_secondary: null
      id: vuln_fl_economic
      impact:
        measurement:
          quantity_kind: currency
          unit: null
        metric: loss
        modelling: simulated
        type: direct
      relationship: math_bespoke
      taxonomy: null
    - analysis_details: Flood damage curves for Sub-Saharan Africa (Englhardt et al.,
        2019)
      approach: hybrid
      category: population
      hazard_analysis_type: deterministic
      hazard_primary:
        classification: null
        id: hazard_flood
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      hazard_secondary: null
      id: vuln_fl_population
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: damage
        modelling: simulated
        type: direct
      relationship: math_bespoke
      taxonomy: null
---
