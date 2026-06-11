---
catalog: World Bank Data Catalog
contact_point:
  email: pchrzanowski@worldbank.org
  id: attribution_contact1
  name: Pierre Chrzanowski
  url: https://www.gfdrr.org/en
creator:
  email: null
  id: attribution_creator_deltares
  name: Deltares
  url: https://www.deltares.nl/en
dataset_id: rdls_hel-lbr_monroviafloodrisk
description: FIAT-based (Flood Impact Assessment Tool, Deltares) multi-hazard flood
  risk assessment for Greater Monrovia covering coastal, pluvial (rainfall), fluvial
  (river discharge), and compound flooding under three climate scenarios (Historical,
  RCP4.5, RCP8.5) with return periods of 1, 2, 5, 10, and 50 years. Includes probabilistic
  flood hazard maps (48 GeoTIFFs), raster-based exposure data for buildings, population,
  health and education facilities, depth-damage vulnerability functions (3 CSV curves),
  and FIAT-computed loss outputs including aggregated annual expected risk rasters
  and community-level risk shapefiles. Commissioned by GFDRR/World Bank as part of
  the Urban Flood Risk Assessment program.
details: 'This flood risk assessment uses Deltares'' FIAT (Flood Impact Assessment
  Tool) to combine: (1) Hydrodynamic flood hazard maps at ~62 MB resolution per raster
  for four flood sources - coastal surge (01_coastal), pluvial/rainfall (02_rain),
  fluvial/river discharge (03_discharge), and compound (04_compound, all sources combined
  at RP50); (2) Three climate scenarios: Historical baseline, RCP4.5 (moderate warming),
  and RCP8.5 (high warming); (3) Five return periods per individual hazard type (1,
  2, 5, 10, 50 years), totaling 48 hazard maps; (4) Raster-based exposure data covering
  formal and informal housing (5 construction sub-types: formal concrete, informal
  concrete, mud, zinc/corrugated iron, others), commercial, industrial, public, and
  kitchen facilities, plus health facilities, schools, and population density; (5)
  Three depth-damage vulnerability curves (CSV format) mapping inundation depth to
  damage factors; (6) FIAT-computed risk outputs including per-scenario damage rasters,
  aggregated annual expected risk rasters (Total_risk_historic.tif, Total_risk_RCP45.tif,
  Total_risk_RCP85.tif), and community-level risk shapefiles for investment prioritization.
  The AW3D (ALOS World 3D, JAXA) Digital Terrain Model provides the foundational topographic
  input.'
exposure:
  category: buildings, infrastructure, population
  dimension: population, structure
  quantity_kind: count, currency
  taxonomy: Custom
extra_attributions:
- email: sarias1@worldbank.org
  id: attribution_ttl1
  name: Santiago Ezequiel Arias
  role: world_bank_team_lead
  url: https://www.worldbank.org
- email: data@gfdrr.org
  id: attribution_funder
  name: Global Facility for Disaster Reduction and Recovery (GFDRR)
  role: funder
  url: https://www.gfdrr.org/en
hazard:
  calculation_method: simulated
  disaster_identifiers: ''
  hazard_analysis_type: probabilistic
  hazard_type: coastal_flood, flood
  intensity: wd:m
  occurrence_range: 50-year return period compound flood (coastal + pluvial + fluvial
    combined) under Historical, RCP4.5, and RCP8.5 scenarios, Return periods of 1,
    2, 5, 10, and 50 years under Historical, RCP4.5, and RCP8.5 scenarios
  processes: coastal_flood, fluvial_flood, pluvial_flood
  seasonality: ''
license: CC-BY-4.0
loss:
  approach: ''
  base_data_type: ''
  category: ''
  description: 'Community-level aggregated annual expected risk for Greater Monrovia
    under Historical baseline. Shapefile: Shapefiles_risk/Current_Risk.shp. Enables
    community-level investment prioritization., Community-level aggregated annual
    expected risk for Greater Monrovia under RCP4.5 scenario. Shapefile: Shapefiles_risk/RCP45_Risk.shp.,
    Community-level aggregated annual expected risk for Greater Monrovia under RCP8.5
    scenario. Shapefile: Shapefiles_risk/RCP85_Risk.shp., Total annual expected risk
    (EAD) for Greater Monrovia under Historical climate baseline, integrating all
    flood hazard types (coastal, pluvial, fluvial, compound) and return periods (1-50
    years) across all asset categories. FIAT-computed from depth-damage vulnerability
    functions applied to exposure rasters. Raster file: FIATpostprocessing/Total_risk_historic.tif.,
    Total annual expected risk (EAD) for Greater Monrovia under RCP4.5 moderate emissions
    climate scenario. Raster file: FIATpostprocessing/Total_risk_RCP45.tif., Total
    annual expected risk (EAD) for Greater Monrovia under RCP8.5 high emissions climate
    scenario. Raster file: FIATpostprocessing/Total_risk_RCP85.tif.'
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
  name: WBG Urban Flood Risk Assessment (UFRA) - Liberia, Greater Monrovia
  url: https://www.worldbank.org
publisher:
  email: data@gfdrr.org
  id: attribution_publisher
  name: Global Facility for Disaster Reduction and Recovery (GFDRR)
  url: https://www.gfdrr.org/en
purpose: To support the Government of Liberia and Monrovia city authorities in understanding
  multi-hazard flood risk under current and future climate conditions, enabling evidence-based
  investment prioritization for flood risk reduction in Greater Monrovia's communities.
resources:
- coordinate_system: EPSG:4326
  description: 'Zip archive containing 48 probabilistic flood inundation GeoTIFF rasters
    for Greater Monrovia. Variable: hmax (maximum water depth in meters). Four hazard
    types: 01_coastal (storm surge and tidal flooding), 02_rain (pluvial/direct rainfall
    flooding), 03_discharge (fluvial/river discharge flooding), 04_compound (all three
    sources combined at RP50). Three climate scenarios: Historical baseline, RCP4.5
    (moderate emissions), RCP8.5 (high emissions). Five return periods per individual
    hazard type: 1, 2, 5, 10, 50 years; compound scenarios at RP50 only with triple
    notation (RP050_RP050_RP050). File naming convention: hmax_[SCENARIO]_[HAZARD_CODE]_RP[XXX]_regrid.tif.
    Each file approximately 62 MB with associated .aux.xml and .ovr sidecar files.
    Hydrodynamic modeling based on ALOS World 3D (AW3D) Digital Terrain Model from
    JAXA.'
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0067049/DR0095933/01_Flood_hazard_layers.zip
  format: GeoTIFF (tif)
  id: resource_hazard_layers
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Flood Hazard Inundation Layers - Greater Monrovia
- coordinate_system: EPSG:4326
  description: 'Zip archive containing the full FIAT-based (Flood Impact Assessment
    Tool, Deltares) risk assessment outputs for Greater Monrovia. Includes: (1) Exposure
    rasters - 30 GeoTIFF files of asset economic values and unit counts covering formal
    concrete and informal housing (~63.5 MB each), commercial (8 files), industrial
    (7 files), kitchen (1 file), public facilities (5 files), health facilities (value
    + units), schools (value + units), and population density, with numeric suffixes
    corresponding to FIAT damage function class IDs; (2) Community boundaries - Greater_Monrovia_Comm.shp
    polygon shapefile for spatial aggregation; (3) Vulnerability functions - 3 CSV
    files with depth-damage curves (1.csv for formal/standard structures, 2.csv for
    informal/basic structures, 6.csv for specific asset categories), plus FIAT_configuration.xls
    mapping exposure classes to damage functions and Risk-explanation_v3.xlsx methodology
    documentation; (4) FIAT results - per-scenario damage outputs for 15 scenario
    combinations (4 hazard types x 3 climate scenarios plus 3 initial events), each
    containing per-asset damage rasters, total damage, road damage, and population/facility
    unit impacts; (5) Aggregated risk rasters - Total_risk_historic.tif, Total_risk_RCP45.tif,
    Total_risk_RCP85.tif (~63.5 MB each) integrating all hazard types, return periods,
    and asset categories into annual expected damage; (6) Community risk shapefiles
    - Current_Risk.shp, RCP45_Risk.shp, RCP85_Risk.shp with community-level aggregated
    risk metrics; (7) Summary spreadsheets - Results_Monrovia_Maps(scenario1).xlsx
    and Summary Risk results per scenario.xlsx for cross-scenario comparison.'
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0067049/DR0095934/02_Flood_risk_layers.zip
  format: GeoTIFF (tif)
  id: resource_risk_layers
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Flood Risk Layers - Exposure, Vulnerability, Loss, and Risk Outputs
risk_data_type:
- hazard
- exposure
- vulnerability
- loss
schema: rdl-03
slug: rdls_hel-lbr_monroviafloodrisk
spatial:
  bbox:
  - -10.85
  - 6.25
  - -10.7
  - 6.4
  countries:
  - LBR
  gazetteer_entries:
  - description: Liberia
    id: gazetteer_liberia
    scheme: GEONAMES
    uri: https://www.geonames.org/2275384/republic-of-liberia.html
  - description: Monrovia
    id: gazetteer_monrovia
    scheme: GEONAMES
    uri: https://www.geonames.org/2274895/monrovia.html
  scale: sub-national
title: Multi-Hazard Flood Risk Assessment for Greater Monrovia, Liberia
version: '1.0'
vulnerability:
  approach: empirical
  base_data_type: simulated
  category: buildings
  dimension: ''
  function_type: ''
  hazard_analysis_type: probabilistic
  hazard_primary: flood
  hazard_process_primary: fluvial_flood
  hazard_process_secondary: ''
  hazard_secondary: ''
  intensity: ''
  metric: damage_ratio
  relationship: discrete
  taxonomy: Custom
  unit: ''
---
