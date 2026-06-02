---
catalog: World Bank Data Catalog
contact_point:
  email: pchrzanowski@worldbank.org
  id: attribution_contact
  name: Pierre Chrzanowski
  url: https://www.gfdrr.org/en
creator:
  email: null
  id: attribution_creator_rhdhv
  name: Royal HaskoningDHV
  url: https://www.royalhaskoningdhv.com/
dataset_id: rdls_hel-vnm_phuquocfloodrisk
description: 'Multi-hazard flood risk assessment for Phu Quoc Island covering fluvial/pluvial,
  coastal, and compound flooding across current climate and climate change 2050 scenarios.
  Includes probabilistic hazard maps (5 return periods: 5-100 years), land use and
  population exposure data, depth-damage vulnerability assessment, and spatial loss
  outputs (damage rasters, annual expected losses, affected population). Commissioned
  by World Bank/GFDRR to support the Phu Quoc Sustainable Water Management Project
  (SWMP).'
details: 'This flood risk assessment combines: (1) HEC-RAS 2D hydraulic modeling of
  fluvial/pluvial (G1), coastal (G2), and compound (G3) flood hazards at 5m resolution
  across 5 return periods (5, 10, 20, 50, 100 years); (2) Current and projected (2050
  climate change) scenarios with four intervention strategies: Do Nothing (S0), Planned
  Reservoirs (Future Baseline), Protective grey infrastructure (S1), and Adaptive
  nature-based solutions (S2); (3) Land use exposure data with economic values (USD/m2)
  for residential, commercial, industrial, and critical infrastructure; (4) Population
  exposure distinguishing residential and tourist populations; (5) Depth-damage vulnerability
  curves applied via the Global Flood Risk Tool (GFRT); (6) Spatial loss outputs including
  probabilistic damage rasters, annual expected losses, and affected population counts.
  Key findings: Current climate Expected Annual Damage is USD 37M (total), projected
  to increase ~5x to USD 175M by 2050 under climate change. The Adaptive strategy
  (S2) achieves ~59% reduction in expected annual damage.'
exposure:
  category: agriculture, buildings, infrastructure, population
  dimension: content, population, structure
  quantity_kind: area, count, currency
  taxonomy: Custom
extra_attributions:
- email: hqaddumi@worldbank.org
  id: attribution_ttl
  name: Halla Maher Qaddumi
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
  occurrence_range: Return periods of 5, 10, 20, 50, and 100 years
  processes: coastal_flood, fluvial_flood
  seasonality: ''
license: CC-BY-4.0
loss:
  approach: ''
  base_data_type: ''
  category: ''
  description: 'Expected Annual Damage (EAD) for combined flooding (G3) on Phu Quoc
    Island under 2050 climate change conditions. Do Nothing (S0): direct USD 129.54M,
    total USD 174.88M. Future Baseline: total USD 164.19M. Protective strategy (S1):
    total USD 110.08M (~33% reduction). Adaptive strategy (S2): total USD 68.05M (~59%
    reduction). Represents ~5x increase from current climate baseline., Expected Annual
    Damage (EAD) for combined flooding (G3) on Phu Quoc Island under current climate
    conditions. Direct damage EAD: USD 27M; Total (direct + indirect): USD 37M. Calculated
    using Global Flood Risk Tool (GFRT) combining flood inundation depth, land use
    exposure with economic values (USD/m2), and depth-damage vulnerability curves.
    Integrates losses across all 5 return periods (5, 10, 20, 50, 100 years). Raster
    file: G3_S0_BL_annual.tif., Flood damage from the August 2019 event on Phu Quoc
    Island, modeled using observed flood extent and depth. 3,874 houses affected,
    inundation depths exceeding 1.5m in some areas, estimated total damage USD 4.3
    million. File: Depth_Max_2019_damage.tif., Probabilistic flood damage rasters
    for each hazard group (G1 fluvial/pluvial, G2 coastal, G3 combined) and return
    period (5, 10, 20, 50, 100 years) across all scenarios. Current climate: 10-year
    flood direct damage USD 125M, 100-year flood USD 212M. CC2050: 10-year flood USD
    602M, 100-year flood USD 948M. File naming: G[group]_S[scenario]_[CC50]_[return_period]_damage.tif.,
    Residential population affected by flooding for each hazard group and return period.
    Current climate annual affected population: ~9,500; projected 2050: ~36,000 (~4x
    increase). Files: Residential_G[group]_S[scenario]_[return_period]_affected_population.tif
    and annual aggregates., Tourist population affected by flooding for each hazard
    group and return period. Phu Quoc is a major tourism destination; tourist population
    exposure is assessed separately from residential. Files: Tourist_G[group]_S[scenario]_[return_period]_affected_population.tif
    and annual aggregates.'
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
  name: Flood Risk Management Services for Phu Quoc Island (BJ7114-HAS-XX-VN-RP-WM-0001)
  url: https://www.worldbank.org
publisher:
  email: data@gfdrr.org
  id: attribution_publisher
  name: Global Facility for Disaster Reduction and Recovery (GFDRR)
  url: https://www.gfdrr.org/en
purpose: To support the Government of Viet Nam and Phu Quoc authorities in understanding
  comprehensive flood risk under current and future climate conditions, enabling evidence-based
  investment decisions for flood risk management interventions including protective
  (grey infrastructure) and adaptive (nature-based) strategies.
resources:
- coordinate_system: EPSG:4326
  description: Zip archive containing a 5-meter resolution DEM for Phu Quoc Island
    (DEM_PhuQuoc_5m.tif, 135.6 MB). Resampled from Intermap DTM (1m pixel, 3m vertical
    accuracy). Serves as the foundational topographic input for all HEC-RAS 2D flood
    inundation modeling across the island.
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0067048/DR0095913/1_DEM_PhuQuoc.zip
  format: GeoTIFF (tif)
  id: resource_dem
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Digital Elevation Model - Phu Quoc Island
- coordinate_system: EPSG:4326
  description: 'Zip archive containing flood modeling outputs for the current climate
    baseline under the Do Nothing (S0) scenario. Includes: (1) Inundation rasters
    - 15 GeoTIFF files for three hazard groups (G1 fluvial/pluvial, G2 coastal, G3
    combined) across 5 return periods (5, 10, 20, 50, 100 years), showing water depth
    in meters at 5m resolution; (2) Flood damage rasters - probabilistic damage GeoTIFFs
    for each hazard group and return period, annual expected loss rasters (G3_S0_BL_annual.tif),
    and empirical 2019 flood event damage (Depth_Max_2019_damage.tif based on August
    2019 flooding affecting 3,874 houses with USD 4.3M estimated damage); (3) Affected
    population rasters - residential and tourist population affected per hazard group
    and return period, plus annual expected affected population. File naming convention:
    G[group]_S0_[return_period].tif for hazard, G[group]_S0_[return_period]_damage.tif
    for loss.'
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0067048/DR0095914/2_CurrentClimate_Baseline_DoNothing.zip
  format: GeoTIFF (tif)
  id: resource_current_climate_s0
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Current Climate Baseline - Do Nothing Scenario (S0)
- coordinate_system: EPSG:4326
  description: 'Zip archive containing flood modeling outputs for the climate change
    2050 projection under the Do Nothing (S0) scenario, with adjusted rainfall intensities
    and sea level rise but no flood interventions. Includes: (1) Inundation rasters
    - 15 GeoTIFF files for three hazard groups (G1 fluvial/pluvial, G2 coastal, G3
    combined) across 5 return periods (5, 10, 20, 50, 100 years); (2) Flood damage
    rasters - probabilistic damage for each hazard group and return period, plus annual
    expected loss rasters; (3) Affected population rasters - residential and tourist
    population affected per scenario. CC2050 Do Nothing projects total expected annual
    damage of USD 174.88M (direct USD 129.54M) and annual affected population of ~36,000.
    File naming: G[group]_S0_CC50_[return_period].tif.'
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0067048/DR0095915/3_ClimateChange2050_Baseline_DoNothing.zip
  format: GeoTIFF (tif)
  id: resource_cc2050_s0
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Climate Change 2050 Baseline - Do Nothing Scenario (S0 CC2050)
- coordinate_system: EPSG:4326
  description: 'Zip archive containing flood modeling outputs for the climate change
    2050 projection with planned reservoir structures (Future Baseline scenario).
    Development Plan implemented with planned reservoirs for water supply and flood
    reduction. Includes: (1) Inundation rasters - GeoTIFF files for three hazard groups
    (G1 fluvial/pluvial, G2 coastal, G3 combined) across 5 return periods; (2) Flood
    damage rasters - probabilistic damage and annual expected loss rasters; (3) Affected
    population rasters. Total expected annual damage under this scenario: USD 164.19M.
    File naming: G[group]_FutureBaseline_CC50_[return_period].tif.'
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0067048/DR0095912/4_ClimateChange2050_Planned_Structures.zip
  format: GeoTIFF (tif)
  id: resource_cc2050_futurebaseline
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Climate Change 2050 - Planned Structures / Future Baseline
- coordinate_system: EPSG:4326
  description: 'Zip archive containing flood modeling outputs for the climate change
    2050 projection with the Protective strategy (S1) of grey structural measures
    including dikes, embankments, pumping stations, and land grading. Includes: (1)
    Inundation rasters - GeoTIFF files for three hazard groups (G1 fluvial/pluvial,
    G2 coastal, G3 combined) across 5 return periods; (2) Flood damage rasters - probabilistic
    damage and annual expected loss rasters; (3) Affected population rasters. The
    Protective strategy achieves ~33% reduction in expected annual damage compared
    to the Future Baseline, with total EAD of USD 110.08M. File naming: G[group]_S1_CC50_[return_period].tif.'
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0067048/DR0095916/5_ClimateChange2050_Planned_Structures_Intervention.zip
  format: GeoTIFF (tif)
  id: resource_cc2050_s1_protective
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Climate Change 2050 - Protective Strategy (S1) with Interventions
- coordinate_system: EPSG:4326
  description: "Zip archive containing flood modeling outputs for the climate change\
    \ 2050 projection with the Adaptive strategy (S2) of nature-based solutions and\
    \ non-structural measures (Living with Water approach). Includes: (1) Inundation\
    \ rasters - GeoTIFF files for three hazard groups (G1 fluvial/pluvial, G2 coastal,\
    \ G3 combined) across 5 return periods; (2) Flood damage rasters - probabilistic\
    \ damage and annual expected loss rasters; (3) Affected population rasters. The\
    \ Adaptive strategy achieves ~59% reduction in expected annual damage compared\
    \ to the Future Baseline, with total EAD of USD 68.05M \xE2\u20AC\u201D the most\
    \ effective risk reduction strategy assessed. File naming: G[group]_S2_CC50_[return_period].tif."
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0067048/DR0095917/6_ClimateChange2050_Planned_Structures_LivingwithWater.zip
  format: GeoTIFF (tif)
  id: resource_cc2050_s2_adaptive
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Climate Change 2050 - Adaptive Strategy (S2) Living with Water
- coordinate_system: EPSG:4326
  description: Zip archive containing flood modeling outputs for the Duong Dong dam
    break scenario. Simulates the consequences of a dam failure event at the Duong
    Dong reservoir on Phu Quoc Island, including downstream inundation mapping, flood
    damage assessment, and affected population estimates. This scenario provides critical
    information for emergency preparedness and dam safety planning.
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0067048/DR0095918/7_DuongDong_DamBreak.zip
  format: GeoTIFF (tif)
  id: resource_dambreak
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Duong Dong Dam Break Scenario
- coordinate_system: EPSG:4326
  description: 'Zip archive containing exposure datasets in Shapefile format for Phu
    Quoc Island. Includes: (1) Land use classification - PhuQuoc_Landuse_Current.shp
    (current conditions), PhuQuoc_Landuse_Planning.shp (future planned 2050), PhuQuoc_Landuse_Planning_LivingWithWater.shp
    (Adaptive S2 scenario); (2) Population density - PhuQuoc_Current_Population_Density.shp
    (current residential and tourist) and PhuQuoc_Planning_Population_Density.shp
    (projected scenarios); (3) Infrastructure - PhuQuoc_Road.shp (road network) and
    PhuQuoc_PlanningOpenWater.shp (planned water infrastructure); (4) Catchment boundaries
    - PhuQuoc_MainCatchments_withOthers.shp and PhuQuoc_SubOtherCatchments.shp. Land
    use types include residential, commercial, industrial, critical infrastructure,
    agriculture, forest, and open water, each with associated economic values (USD/m2)
    used in damage calculations.'
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0067048/DR0095919/Vector_data.zip
  format: Shapefile (shp)
  id: resource_exposure_vector
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Exposure Vector Data - Land Use, Population, Infrastructure
risk_data_type:
- hazard
- exposure
- loss
schema: rdl-03
slug: rdls_hel-vnm_phuquocfloodrisk
spatial:
  bbox:
  - 103.8
  - 9.8
  - 104.1
  - 10.45
  countries:
  - VNM
  gazetteer_entries:
  - description: Viet Nam
    id: gazetteer_vietnam
    scheme: GEONAMES
    uri: https://www.geonames.org/1562822/socialist-republic-of-vietnam.html
  - description: Phu Quoc Island
    id: gazetteer_phuquoc
    scheme: GEONAMES
    uri: https://www.geonames.org/1571067/phu-quoc.html
  scale: sub-national
title: Comprehensive Flood Risk Assessment for Phu Quoc Island, Viet Nam
version: '1.0'
vulnerability: null
---
