---
attributions:
- entity:
    affiliation: null
    email: null
    name: EGIS
    url: https://www.egis-group.com/
  id: attribution_creator_egis
  role: creator
- entity:
    affiliation: null
    email: hqaddumi@worldbank.org
    name: Halla Maher Qaddumi
    url: https://www.worldbank.org
  id: attribution_ttl
  role: world_bank_team_lead
- entity:
    affiliation: null
    email: data@gfdrr.org
    name: Global Facility for Disaster Reduction and Recovery (GFDRR)
    url: https://www.gfdrr.org/en
  id: attribution_funder
  role: funder
catalog: World Bank Data Catalog
contact_point:
  affiliation: null
  email: pchrzanowski@worldbank.org
  name: Pierre Chrzanowski
  url: https://www.gfdrr.org/en
creator:
  affiliation: null
  email: null
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
- asset_type:
    description: Building and land use classes in Phu Quoc using the Global Flood
      Risk Tool (GFRT) taxonomy.
    id: buildings
    scheme: null
    title: Building taxonomy
    uri: null
  category: buildings
  id: exposure_buildings_landuse
  metrics:
  - dimension: structure
    id: metric_building_count
    measurement:
      quantity_kind: count
      unit: count
  - dimension: content
    id: metric_building_economic_value
    measurement:
      quantity_kind: currency
      unit: USD
- asset_type:
    description: Residential and tourist population in Phu Quoc derived from project
      surveys and official statistics.
    id: population
    scheme: null
    title: Population taxonomy
    uri: null
  category: population
  id: exposure_population
  metrics:
  - dimension: population
    id: metric_population_residential
    measurement:
      quantity_kind: count
      unit: count
  - dimension: population
    id: metric_population_tourist
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Road network in Phu Quoc derived from project GIS vector data.
    id: road_network
    scheme: null
    title: Infrastructure taxonomy
    uri: null
  category: infrastructure
  id: exposure_infrastructure
  metrics:
  - dimension: structure
    id: metric_road_network
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Agricultural land area in Phu Quoc derived from project land use
      classification.
    id: agricultural_land
    scheme: null
    title: Agriculture taxonomy
    uri: null
  category: agriculture
  id: exposure_agriculture
  metrics:
  - dimension: structure
    id: metric_agriculture_area
    measurement:
      quantity_kind: area
      unit: null
hazard:
  event_sets_by_hazard_type:
    flood:
    - analysis_type: probabilistic
      calculation_method: simulated
      event_count: 5
      events:
      - calculation_method: simulated
        description: 'Fluvial/pluvial flood hazard map showing water depth for a 1-in-5
          year return period event on Phu Quoc Island. Current climate baseline, Do
          Nothing (S0) scenario. File: G1_S0_05.tif.'
        disaster_identifiers: []
        hazard:
          classification: null
          id: hazard_fluvial_pluvial
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: event_G1_S0_RP5
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability: null
            return_period: 5
      - calculation_method: simulated
        description: 'Fluvial/pluvial flood hazard map showing water depth for a 1-in-10
          year return period event on Phu Quoc Island. Current climate baseline, Do
          Nothing (S0) scenario. File: G1_S0_10.tif.'
        disaster_identifiers: []
        hazard:
          classification: null
          id: hazard_fluvial_pluvial
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: event_G1_S0_RP10
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability: null
            return_period: 10
      - calculation_method: simulated
        description: 'Fluvial/pluvial flood hazard map showing water depth for a 1-in-20
          year return period event on Phu Quoc Island. Current climate baseline, Do
          Nothing (S0) scenario. File: G1_S0_20.tif.'
        disaster_identifiers: []
        hazard:
          classification: null
          id: hazard_fluvial_pluvial
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: event_G1_S0_RP20
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.05
            probability: null
            return_period: 20
      - calculation_method: simulated
        description: 'Fluvial/pluvial flood hazard map showing water depth for a 1-in-50
          year return period event on Phu Quoc Island. Current climate baseline, Do
          Nothing (S0) scenario. File: G1_S0_50.tif.'
        disaster_identifiers: []
        hazard:
          classification: null
          id: hazard_fluvial_pluvial
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: event_G1_S0_RP50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability: null
            return_period: 50
      - calculation_method: simulated
        description: 'Fluvial/pluvial flood hazard map showing water depth for a 1-in-100
          year return period event on Phu Quoc Island. Current climate baseline, Do
          Nothing (S0) scenario. File: G1_S0_100.tif.'
        disaster_identifiers: []
        hazard:
          classification: null
          id: hazard_fluvial_pluvial
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: event_G1_S0_RP100
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability: null
            return_period: 100
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_fluvial_flood
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      - classification: null
        id: hazard_pluvial_flood
        intensity_measure: wd:m
        process: pluvial_flood
        trigger: null
        type: flood
      id: event_set_fluvial_pluvial
      occurrence_range: Return periods of 5, 10, 20, 50, and 100 years
      seasonality: null
    - analysis_type: probabilistic
      calculation_method: simulated
      event_count: 5
      events:
      - calculation_method: simulated
        description: 'Coastal flood hazard map showing water depth for a 1-in-5 year
          return period event on Phu Quoc Island. Storm surge and tidal flooding.
          Current climate baseline, Do Nothing (S0) scenario. File: G2_S0_05.tif.'
        disaster_identifiers: []
        hazard:
          classification: null
          id: hazard_coastal
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: event_G2_S0_RP5
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability: null
            return_period: 5
      - calculation_method: simulated
        description: 'Coastal flood hazard map showing water depth for a 1-in-10 year
          return period event on Phu Quoc Island. Current climate baseline, Do Nothing
          (S0) scenario. File: G2_S0_10.tif.'
        disaster_identifiers: []
        hazard:
          classification: null
          id: hazard_coastal
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: event_G2_S0_RP10
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability: null
            return_period: 10
      - calculation_method: simulated
        description: 'Coastal flood hazard map showing water depth for a 1-in-20 year
          return period event on Phu Quoc Island. Current climate baseline, Do Nothing
          (S0) scenario. File: G2_S0_20.tif.'
        disaster_identifiers: []
        hazard:
          classification: null
          id: hazard_coastal
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: event_G2_S0_RP20
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.05
            probability: null
            return_period: 20
      - calculation_method: simulated
        description: 'Coastal flood hazard map showing water depth for a 1-in-50 year
          return period event on Phu Quoc Island. Current climate baseline, Do Nothing
          (S0) scenario. File: G2_S0_50.tif.'
        disaster_identifiers: []
        hazard:
          classification: null
          id: hazard_coastal
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: event_G2_S0_RP50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability: null
            return_period: 50
      - calculation_method: simulated
        description: 'Coastal flood hazard map showing water depth for a 1-in-100
          year return period event on Phu Quoc Island. Current climate baseline, Do
          Nothing (S0) scenario. File: G2_S0_100.tif.'
        disaster_identifiers: []
        hazard:
          classification: null
          id: hazard_coastal
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: event_G2_S0_RP100
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability: null
            return_period: 100
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_coastal
        intensity_measure: wd:m
        process: coastal_flood
        trigger: null
        type: flood
      id: event_set_coastal
      occurrence_range: Return periods of 5, 10, 20, 50, and 100 years
      seasonality: null
    - analysis_type: probabilistic
      calculation_method: simulated
      event_count: 5
      events:
      - calculation_method: simulated
        description: 'Combined (compound) flood hazard map showing water depth for
          a 1-in-5 year return period event on Phu Quoc Island. Combines fluvial,
          pluvial, and coastal flooding. Current climate baseline, Do Nothing (S0)
          scenario. File: G3_S0_05.tif.'
        disaster_identifiers: []
        hazard:
          classification: null
          id: hazard_combined
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: event_G3_S0_RP5
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.2
            probability: null
            return_period: 5
      - calculation_method: simulated
        description: 'Combined (compound) flood hazard map showing water depth for
          a 1-in-10 year return period event on Phu Quoc Island. Combines fluvial,
          pluvial, and coastal flooding. Current climate baseline, Do Nothing (S0)
          scenario. File: G3_S0_10.tif.'
        disaster_identifiers: []
        hazard:
          classification: null
          id: hazard_combined
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: event_G3_S0_RP10
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability: null
            return_period: 10
      - calculation_method: simulated
        description: 'Combined (compound) flood hazard map showing water depth for
          a 1-in-20 year return period event on Phu Quoc Island. Combines fluvial,
          pluvial, and coastal flooding. Current climate baseline, Do Nothing (S0)
          scenario. File: G3_S0_20.tif.'
        disaster_identifiers: []
        hazard:
          classification: null
          id: hazard_combined
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: event_G3_S0_RP20
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.05
            probability: null
            return_period: 20
      - calculation_method: simulated
        description: 'Combined (compound) flood hazard map showing water depth for
          a 1-in-50 year return period event on Phu Quoc Island. Combines fluvial,
          pluvial, and coastal flooding. Current climate baseline, Do Nothing (S0)
          scenario. File: G3_S0_50.tif.'
        disaster_identifiers: []
        hazard:
          classification: null
          id: hazard_combined
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: event_G3_S0_RP50
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.02
            probability: null
            return_period: 50
      - calculation_method: simulated
        description: 'Combined (compound) flood hazard map showing water depth for
          a 1-in-100 year return period event on Phu Quoc Island. Combines fluvial,
          pluvial, and coastal flooding. Current climate baseline, Do Nothing (S0)
          scenario. File: G3_S0_100.tif.'
        disaster_identifiers: []
        hazard:
          classification: null
          id: hazard_combined
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: event_G3_S0_RP100
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability: null
            return_period: 100
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_fluvial_flood
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      - classification: null
        id: hazard_pluvial_flood
        intensity_measure: wd:m
        process: pluvial_flood
        trigger: null
        type: flood
      - classification: null
        id: hazard_coastal_flood
        intensity_measure: wd:m
        process: coastal_flood
        trigger: null
        type: flood
      id: event_set_combined
      occurrence_range: Return periods of 5, 10, 20, 50, and 100 years
      seasonality: null
  event_sets_count: 3
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Flood risk assessment for Phu Quoc Island, Kien Giang Province, Viet
    Nam, produced by Royal HaskoningDHV and EGIS under the GFDRR-financed Phu Quoc
    Sustainable Water Management Project. A HEC-RAS 2D hydrodynamic model was calibrated
    against historical flood events (including the August 2019 event) using a 5 m
    Intermap DTM as topographic input. Fluvial/pluvial, coastal, and compound flood
    scenarios were simulated for current climate and 2050 climate change conditions
    across four management strategies (do-nothing, planned reservoirs, protective,
    adaptive). Flood damage was computed using the Global Flood Risk Tool (GFRT) by
    applying depth-damage vulnerability curves and land-use-based maximum damage values
    (USD/m2) to inundation depths. Population exposure distinguished residential and
    tourist populations from current and projected density datasets.
  sources:
  - id: source_hecras
    license: https://creativecommons.org/publicdomain/zero/1.0/
    name: HEC-RAS 2D hydraulic model
    risk_data_type: null
    type: model
    url: null
    used_in: hazard
  - id: source_intermap_dtm
    license: null
    name: Intermap DTM (1m pixel, 3m vertical accuracy)
    risk_data_type: null
    type: dataset
    url: https://www.intermap.com/
    used_in: hazard
  - id: source_gfrt
    license: null
    name: Global Flood Risk Tool (GFRT)
    risk_data_type: null
    type: model
    url: null
    used_in: vulnerability
  - id: source_landuse_population
    license: null
    name: Phu Quoc land use and population data
    risk_data_type: null
    type: dataset
    url: null
    used_in: exposure
  - id: source_climate_projections
    license: null
    name: Climate change projections (2050)
    risk_data_type: null
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: 'Expected Annual Damage (EAD) for combined flooding (G3) on Phu Quoc
      Island under current climate conditions. Direct damage EAD: USD 27M; Total (direct
      + indirect): USD 37M. Calculated using Global Flood Risk Tool (GFRT) combining
      flood inundation depth, land use exposure with economic values (USD/m2), and
      depth-damage vulnerability curves. Integrates losses across all 5 return periods
      (5, 10, 20, 50, 100 years). Raster file: G3_S0_BL_annual.tif.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: null
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_aal_combined_current
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: USD
        metric: loss
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: 'Expected Annual Damage (EAD) for combined flooding (G3) on Phu Quoc
      Island under 2050 climate change conditions. Do Nothing (S0): direct USD 129.54M,
      total USD 174.88M. Future Baseline: total USD 164.19M. Protective strategy (S1):
      total USD 110.08M (~33% reduction). Adaptive strategy (S2): total USD 68.05M
      (~59% reduction). Represents ~5x increase from current climate baseline.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: null
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_aal_combined_cc2050
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: USD
        metric: loss
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: 'Probabilistic flood damage rasters for each hazard group (G1 fluvial/pluvial,
      G2 coastal, G3 combined) and return period (5, 10, 20, 50, 100 years) across
      all scenarios. Current climate: 10-year flood direct damage USD 125M, 100-year
      flood USD 212M. CC2050: 10-year flood USD 602M, 100-year flood USD 948M. File
      naming: G[group]_S[scenario]_[CC50]_[return_period]_damage.tif.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: null
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_probabilistic_damage
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: USD
        metric: loss
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: 'Flood damage from the August 2019 event on Phu Quoc Island, modeled
      using observed flood extent and depth. 3,874 houses affected, inundation depths
      exceeding 1.5m in some areas, estimated total damage USD 4.3 million. File:
      Depth_Max_2019_damage.tif.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: null
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_empirical_2019
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: USD
        metric: loss
        modelling: simulated
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Residential population affected by flooding for each hazard group
      and return period. Current climate annual affected population: ~9,500; projected
      2050: ~36,000 (~4x increase). Files: Residential_G[group]_S[scenario]_[return_period]_affected_population.tif
      and annual aggregates.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: null
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_affected_population_residential
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Tourist population affected by flooding for each hazard group and
      return period. Phu Quoc is a major tourism destination; tourist population exposure
      is assessed separately from residential. Files: Tourist_G[group]_S[scenario]_[return_period]_affected_population.tif
      and annual aggregates.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: null
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_affected_population_tourist
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
      loss_type: ground_up
project:
  name: Flood Risk Management Services for Phu Quoc Island (BJ7114-HAS-XX-VN-RP-WM-0001)
  url: https://www.worldbank.org
publisher:
  affiliation: null
  email: data@gfdrr.org
  name: Global Facility for Disaster Reduction and Recovery (GFDRR)
  url: https://www.gfdrr.org/en
purpose: To support the Government of Viet Nam and Phu Quoc authorities in understanding
  comprehensive flood risk under current and future climate conditions, enabling evidence-based
  investment decisions for flood risk management interventions including protective
  (grey infrastructure) and adaptive (nature-based) strategies.
referenced_by: []
resources:
- access_url: https://datacatalog.worldbank.org/search/dataset/0067048/multihazard_flood_risk_assessment_for_phu_quoc_island_viet_nam
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Zip archive containing a 5-meter resolution DEM for Phu Quoc Island
    (DEM_PhuQuoc_5m.tif, 135.6 MB). Resampled from Intermap DTM (1m pixel, 3m vertical
    accuracy). Serves as the foundational topographic input for all HEC-RAS 2D flood
    inundation modeling across the island.
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0067048/DR0095913/1_DEM_PhuQuoc.zip
  format: null
  id: resource_dem
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Digital Elevation Model - Phu Quoc Island
- access_url: https://datacatalog.worldbank.org/search/dataset/0067048/multihazard_flood_risk_assessment_for_phu_quoc_island_viet_nam
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
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
  format: null
  id: resource_current_climate_s0
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Current Climate Baseline - Do Nothing Scenario (S0)
- access_url: https://datacatalog.worldbank.org/search/dataset/0067048/multihazard_flood_risk_assessment_for_phu_quoc_island_viet_nam
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
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
  format: null
  id: resource_cc2050_s0
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Climate Change 2050 Baseline - Do Nothing Scenario (S0 CC2050)
- access_url: https://datacatalog.worldbank.org/search/dataset/0067048/multihazard_flood_risk_assessment_for_phu_quoc_island_viet_nam
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Zip archive containing flood modeling outputs for the climate change
    2050 projection with planned reservoir structures (Future Baseline scenario).
    Development Plan implemented with planned reservoirs for water supply and flood
    reduction. Includes: (1) Inundation rasters - GeoTIFF files for three hazard groups
    (G1 fluvial/pluvial, G2 coastal, G3 combined) across 5 return periods; (2) Flood
    damage rasters - probabilistic damage and annual expected loss rasters; (3) Affected
    population rasters. Total expected annual damage under this scenario: USD 164.19M.
    File naming: G[group]_FutureBaseline_CC50_[return_period].tif.'
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0067048/DR0095912/4_ClimateChange2050_Planned_Structures.zip
  format: null
  id: resource_cc2050_futurebaseline
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Climate Change 2050 - Planned Structures / Future Baseline
- access_url: https://datacatalog.worldbank.org/search/dataset/0067048/multihazard_flood_risk_assessment_for_phu_quoc_island_viet_nam
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Zip archive containing flood modeling outputs for the climate change
    2050 projection with the Protective strategy (S1) of grey structural measures
    including dikes, embankments, pumping stations, and land grading. Includes: (1)
    Inundation rasters - GeoTIFF files for three hazard groups (G1 fluvial/pluvial,
    G2 coastal, G3 combined) across 5 return periods; (2) Flood damage rasters - probabilistic
    damage and annual expected loss rasters; (3) Affected population rasters. The
    Protective strategy achieves ~33% reduction in expected annual damage compared
    to the Future Baseline, with total EAD of USD 110.08M. File naming: G[group]_S1_CC50_[return_period].tif.'
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0067048/DR0095916/5_ClimateChange2050_Planned_Structures_Intervention.zip
  format: null
  id: resource_cc2050_s1_protective
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Climate Change 2050 - Protective Strategy (S1) with Interventions
- access_url: https://datacatalog.worldbank.org/search/dataset/0067048/multihazard_flood_risk_assessment_for_phu_quoc_island_viet_nam
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
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
  format: null
  id: resource_cc2050_s2_adaptive
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Climate Change 2050 - Adaptive Strategy (S2) Living with Water
- access_url: https://datacatalog.worldbank.org/search/dataset/0067048/multihazard_flood_risk_assessment_for_phu_quoc_island_viet_nam
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Zip archive containing flood modeling outputs for the Duong Dong dam
    break scenario. Simulates the consequences of a dam failure event at the Duong
    Dong reservoir on Phu Quoc Island, including downstream inundation mapping, flood
    damage assessment, and affected population estimates. This scenario provides critical
    information for emergency preparedness and dam safety planning.
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0067048/DR0095918/7_DuongDong_DamBreak.zip
  format: null
  id: resource_dambreak
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Duong Dong Dam Break Scenario
- access_url: https://datacatalog.worldbank.org/search/dataset/0067048/multihazard_flood_risk_assessment_for_phu_quoc_island_viet_nam
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
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
  format: null
  id: resource_exposure_vector
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Exposure Vector Data - Land Use, Population, Infrastructure
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-vnm_phuquocfloodrisk
spatial:
  bbox:
  - 103.8
  - 9.8
  - 104.1
  - 10.45
  centroid: null
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
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Comprehensive Flood Risk Assessment for Phu Quoc Island, Viet Nam
version: '1.0'
vulnerability: null
---
