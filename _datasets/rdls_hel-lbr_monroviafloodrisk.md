---
attributions:
- entity:
    affiliation: null
    email: sarias1@worldbank.org
    name: Santiago Ezequiel Arias
    url: https://www.worldbank.org
  id: attribution_ttl1
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
- asset_type:
    description: Residential and commercial building stock in Greater Monrovia using
      the Deltares FIAT building typology (formal/informal concrete, mud, zinc construction
      types).
    id: buildings
    scheme: null
    title: Building taxonomy
    uri: null
  category: buildings
  id: exposure_buildings
  metrics:
  - dimension: structure
    id: metric_building_value
    measurement:
      quantity_kind: currency
      unit: USD
  - dimension: structure
    id: metric_building_count
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Population density in Greater Monrovia derived from WorldPop data.
    id: population
    scheme: null
    title: Population taxonomy
    uri: null
  category: population
  id: exposure_population
  metrics:
  - dimension: population
    id: metric_population_density
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Health facilities in Greater Monrovia from OpenStreetMap and local
      survey data.
    id: health_facilities
    scheme: null
    title: Infrastructure taxonomy
    uri: null
  category: infrastructure
  id: exposure_infrastructure_health
  metrics:
  - dimension: structure
    id: metric_health_value
    measurement:
      quantity_kind: currency
      unit: USD
  - dimension: structure
    id: metric_health_units
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Education facilities in Greater Monrovia from OpenStreetMap and local
      survey data.
    id: education_facilities
    scheme: null
    title: Infrastructure taxonomy
    uri: null
  category: infrastructure
  id: exposure_infrastructure_education
  metrics:
  - dimension: structure
    id: metric_education_value
    measurement:
      quantity_kind: currency
      unit: USD
  - dimension: structure
    id: metric_education_units
    measurement:
      quantity_kind: count
      unit: count
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: simulated
    event_count: 15
    events:
    - calculation_method: simulated
      description: 'Coastal flood hazard - Historical baseline, 1-year return period.
        File: hmax_historical_01_coastal_RP001_regrid.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_coastal
        intensity_measure: wd:m
        process: coastal_flood
        trigger: null
        type: flood
      id: event_coastal_hist_RP001
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 1.0
          probability: null
          return_period: 1
    - calculation_method: simulated
      description: 'Coastal flood hazard - Historical baseline, 2-year return period.
        File: hmax_historical_01_coastal_RP002_regrid.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_coastal
        intensity_measure: wd:m
        process: coastal_flood
        trigger: null
        type: flood
      id: event_coastal_hist_RP002
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.5
          probability: null
          return_period: 2
    - calculation_method: simulated
      description: 'Coastal flood hazard - Historical baseline, 5-year return period.
        File: hmax_historical_01_coastal_RP005_regrid.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_coastal
        intensity_measure: wd:m
        process: coastal_flood
        trigger: null
        type: flood
      id: event_coastal_hist_RP005
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.2
          probability: null
          return_period: 5
    - calculation_method: simulated
      description: 'Coastal flood hazard - Historical baseline, 10-year return period.
        File: hmax_historical_01_coastal_RP010_regrid.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_coastal
        intensity_measure: wd:m
        process: coastal_flood
        trigger: null
        type: flood
      id: event_coastal_hist_RP010
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.1
          probability: null
          return_period: 10
    - calculation_method: simulated
      description: 'Coastal flood hazard - Historical baseline, 50-year return period.
        File: hmax_historical_01_coastal_RP050_regrid.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_coastal
        intensity_measure: wd:m
        process: coastal_flood
        trigger: null
        type: flood
      id: event_coastal_hist_RP050
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.02
          probability: null
          return_period: 50
    - calculation_method: simulated
      description: 'Coastal flood hazard - RCP4.5 scenario, 1-year return period.
        File: hmax_RCP45_01_coastal_RP001_regrid.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_coastal
        intensity_measure: wd:m
        process: coastal_flood
        trigger: null
        type: flood
      id: event_coastal_rcp45_RP001
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 1.0
          probability: null
          return_period: 1
    - calculation_method: simulated
      description: 'Coastal flood hazard - RCP4.5 scenario, 2-year return period.
        File: hmax_RCP45_01_coastal_RP002_regrid.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_coastal
        intensity_measure: wd:m
        process: coastal_flood
        trigger: null
        type: flood
      id: event_coastal_rcp45_RP002
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.5
          probability: null
          return_period: 2
    - calculation_method: simulated
      description: 'Coastal flood hazard - RCP4.5 scenario, 5-year return period.
        File: hmax_RCP45_01_coastal_RP005_regrid.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_coastal
        intensity_measure: wd:m
        process: coastal_flood
        trigger: null
        type: flood
      id: event_coastal_rcp45_RP005
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.2
          probability: null
          return_period: 5
    - calculation_method: simulated
      description: 'Coastal flood hazard - RCP4.5 scenario, 10-year return period.
        File: hmax_RCP45_01_coastal_RP010_regrid.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_coastal
        intensity_measure: wd:m
        process: coastal_flood
        trigger: null
        type: flood
      id: event_coastal_rcp45_RP010
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.1
          probability: null
          return_period: 10
    - calculation_method: simulated
      description: 'Coastal flood hazard - RCP4.5 scenario, 50-year return period.
        File: hmax_RCP45_01_coastal_RP050_regrid.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_coastal
        intensity_measure: wd:m
        process: coastal_flood
        trigger: null
        type: flood
      id: event_coastal_rcp45_RP050
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.02
          probability: null
          return_period: 50
    - calculation_method: simulated
      description: 'Coastal flood hazard - RCP8.5 scenario, 1-year return period.
        File: hmax_RCP85_01_coastal_RP001_regrid.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_coastal
        intensity_measure: wd:m
        process: coastal_flood
        trigger: null
        type: flood
      id: event_coastal_rcp85_RP001
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 1.0
          probability: null
          return_period: 1
    - calculation_method: simulated
      description: 'Coastal flood hazard - RCP8.5 scenario, 2-year return period.
        File: hmax_RCP85_01_coastal_RP002_regrid.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_coastal
        intensity_measure: wd:m
        process: coastal_flood
        trigger: null
        type: flood
      id: event_coastal_rcp85_RP002
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.5
          probability: null
          return_period: 2
    - calculation_method: simulated
      description: 'Coastal flood hazard - RCP8.5 scenario, 5-year return period.
        File: hmax_RCP85_01_coastal_RP005_regrid.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_coastal
        intensity_measure: wd:m
        process: coastal_flood
        trigger: null
        type: flood
      id: event_coastal_rcp85_RP005
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.2
          probability: null
          return_period: 5
    - calculation_method: simulated
      description: 'Coastal flood hazard - RCP8.5 scenario, 10-year return period.
        File: hmax_RCP85_01_coastal_RP010_regrid.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_coastal
        intensity_measure: wd:m
        process: coastal_flood
        trigger: null
        type: flood
      id: event_coastal_rcp85_RP010
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.1
          probability: null
          return_period: 10
    - calculation_method: simulated
      description: 'Coastal flood hazard - RCP8.5 scenario, 50-year return period.
        File: hmax_RCP85_01_coastal_RP050_regrid.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_coastal
        intensity_measure: wd:m
        process: coastal_flood
        trigger: null
        type: flood
      id: event_coastal_rcp85_RP050
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.02
          probability: null
          return_period: 50
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_coastal
      intensity_measure: wd:m
      process: coastal_flood
      trigger: null
      type: flood
    id: event_set_coastal_flood
    occurrence_range: Return periods of 1, 2, 5, 10, and 50 years under Historical,
      RCP4.5, and RCP8.5 scenarios
    seasonality: null
  - analysis_type: probabilistic
    calculation_method: simulated
    event_count: 15
    events:
    - calculation_method: simulated
      description: 'Pluvial (rainfall) flood hazard - Historical, RP1. File: hmax_historical_02_rain_RP001_regrid.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_pluvial
        intensity_measure: wd:m
        process: pluvial_flood
        trigger: null
        type: flood
      id: event_pluvial_hist_RP001
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 1.0
          probability: null
          return_period: 1
    - calculation_method: simulated
      description: 'Pluvial (rainfall) flood hazard - Historical, RP2. File: hmax_historical_02_rain_RP002_regrid.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_pluvial
        intensity_measure: wd:m
        process: pluvial_flood
        trigger: null
        type: flood
      id: event_pluvial_hist_RP002
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.5
          probability: null
          return_period: 2
    - calculation_method: simulated
      description: 'Pluvial (rainfall) flood hazard - Historical, RP5. File: hmax_historical_02_rain_RP005_regrid.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_pluvial
        intensity_measure: wd:m
        process: pluvial_flood
        trigger: null
        type: flood
      id: event_pluvial_hist_RP005
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.2
          probability: null
          return_period: 5
    - calculation_method: simulated
      description: 'Pluvial (rainfall) flood hazard - Historical, RP10. File: hmax_historical_02_rain_RP010_regrid.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_pluvial
        intensity_measure: wd:m
        process: pluvial_flood
        trigger: null
        type: flood
      id: event_pluvial_hist_RP010
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.1
          probability: null
          return_period: 10
    - calculation_method: simulated
      description: 'Pluvial (rainfall) flood hazard - Historical, RP50. File: hmax_historical_02_rain_RP050_regrid.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_pluvial
        intensity_measure: wd:m
        process: pluvial_flood
        trigger: null
        type: flood
      id: event_pluvial_hist_RP050
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.02
          probability: null
          return_period: 50
    - calculation_method: simulated
      description: 'Pluvial (rainfall) flood hazard - RCP4.5, RP1. File: hmax_RCP45_02_rain_RP001_regrid.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_pluvial
        intensity_measure: wd:m
        process: pluvial_flood
        trigger: null
        type: flood
      id: event_pluvial_rcp45_RP001
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 1.0
          probability: null
          return_period: 1
    - calculation_method: simulated
      description: 'Pluvial (rainfall) flood hazard - RCP4.5, RP2. File: hmax_RCP45_02_rain_RP002_regrid.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_pluvial
        intensity_measure: wd:m
        process: pluvial_flood
        trigger: null
        type: flood
      id: event_pluvial_rcp45_RP002
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.5
          probability: null
          return_period: 2
    - calculation_method: simulated
      description: 'Pluvial (rainfall) flood hazard - RCP4.5, RP5. File: hmax_RCP45_02_rain_RP005_regrid.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_pluvial
        intensity_measure: wd:m
        process: pluvial_flood
        trigger: null
        type: flood
      id: event_pluvial_rcp45_RP005
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.2
          probability: null
          return_period: 5
    - calculation_method: simulated
      description: 'Pluvial (rainfall) flood hazard - RCP4.5, RP10. File: hmax_RCP45_02_rain_RP010_regrid.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_pluvial
        intensity_measure: wd:m
        process: pluvial_flood
        trigger: null
        type: flood
      id: event_pluvial_rcp45_RP010
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.1
          probability: null
          return_period: 10
    - calculation_method: simulated
      description: 'Pluvial (rainfall) flood hazard - RCP4.5, RP50. File: hmax_RCP45_02_rain_RP050_regrid.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_pluvial
        intensity_measure: wd:m
        process: pluvial_flood
        trigger: null
        type: flood
      id: event_pluvial_rcp45_RP050
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.02
          probability: null
          return_period: 50
    - calculation_method: simulated
      description: 'Pluvial (rainfall) flood hazard - RCP8.5, RP1. File: hmax_RCP85_02_rain_RP001_regrid.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_pluvial
        intensity_measure: wd:m
        process: pluvial_flood
        trigger: null
        type: flood
      id: event_pluvial_rcp85_RP001
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 1.0
          probability: null
          return_period: 1
    - calculation_method: simulated
      description: 'Pluvial (rainfall) flood hazard - RCP8.5, RP2. File: hmax_RCP85_02_rain_RP002_regrid.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_pluvial
        intensity_measure: wd:m
        process: pluvial_flood
        trigger: null
        type: flood
      id: event_pluvial_rcp85_RP002
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.5
          probability: null
          return_period: 2
    - calculation_method: simulated
      description: 'Pluvial (rainfall) flood hazard - RCP8.5, RP5. File: hmax_RCP85_02_rain_RP005_regrid.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_pluvial
        intensity_measure: wd:m
        process: pluvial_flood
        trigger: null
        type: flood
      id: event_pluvial_rcp85_RP005
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.2
          probability: null
          return_period: 5
    - calculation_method: simulated
      description: 'Pluvial (rainfall) flood hazard - RCP8.5, RP10. File: hmax_RCP85_02_rain_RP010_regrid.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_pluvial
        intensity_measure: wd:m
        process: pluvial_flood
        trigger: null
        type: flood
      id: event_pluvial_rcp85_RP010
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.1
          probability: null
          return_period: 10
    - calculation_method: simulated
      description: 'Pluvial (rainfall) flood hazard - RCP8.5, RP50. File: hmax_RCP85_02_rain_RP050_regrid.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_pluvial
        intensity_measure: wd:m
        process: pluvial_flood
        trigger: null
        type: flood
      id: event_pluvial_rcp85_RP050
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.02
          probability: null
          return_period: 50
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_pluvial
      intensity_measure: wd:m
      process: pluvial_flood
      trigger: null
      type: flood
    id: event_set_pluvial_flood
    occurrence_range: Return periods of 1, 2, 5, 10, and 50 years under Historical,
      RCP4.5, and RCP8.5 scenarios
    seasonality: null
  - analysis_type: probabilistic
    calculation_method: simulated
    event_count: 15
    events:
    - calculation_method: simulated
      description: 'Fluvial (discharge) flood hazard - Historical, RP1. File: hmax_historical_03_discharge_RP001_regrid.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_fluvial
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_fluvial_hist_RP001
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 1.0
          probability: null
          return_period: 1
    - calculation_method: simulated
      description: 'Fluvial (discharge) flood hazard - Historical, RP2. File: hmax_historical_03_discharge_RP002_regrid.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_fluvial
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_fluvial_hist_RP002
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.5
          probability: null
          return_period: 2
    - calculation_method: simulated
      description: 'Fluvial (discharge) flood hazard - Historical, RP5. File: hmax_historical_03_discharge_RP005_regrid.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_fluvial
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_fluvial_hist_RP005
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.2
          probability: null
          return_period: 5
    - calculation_method: simulated
      description: 'Fluvial (discharge) flood hazard - Historical, RP10. File: hmax_historical_03_discharge_RP010_regrid.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_fluvial
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_fluvial_hist_RP010
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.1
          probability: null
          return_period: 10
    - calculation_method: simulated
      description: 'Fluvial (discharge) flood hazard - Historical, RP50. File: hmax_historical_03_discharge_RP050_regrid.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_fluvial
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_fluvial_hist_RP050
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.02
          probability: null
          return_period: 50
    - calculation_method: simulated
      description: 'Fluvial (discharge) flood hazard - RCP4.5, RP1. File: hmax_RCP45_03_discharge_RP001_regrid.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_fluvial
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_fluvial_rcp45_RP001
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 1.0
          probability: null
          return_period: 1
    - calculation_method: simulated
      description: 'Fluvial (discharge) flood hazard - RCP4.5, RP2. File: hmax_RCP45_03_discharge_RP002_regrid.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_fluvial
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_fluvial_rcp45_RP002
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.5
          probability: null
          return_period: 2
    - calculation_method: simulated
      description: 'Fluvial (discharge) flood hazard - RCP4.5, RP5. File: hmax_RCP45_03_discharge_RP005_regrid.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_fluvial
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_fluvial_rcp45_RP005
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.2
          probability: null
          return_period: 5
    - calculation_method: simulated
      description: 'Fluvial (discharge) flood hazard - RCP4.5, RP10. File: hmax_RCP45_03_discharge_RP010_regrid.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_fluvial
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_fluvial_rcp45_RP010
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.1
          probability: null
          return_period: 10
    - calculation_method: simulated
      description: 'Fluvial (discharge) flood hazard - RCP4.5, RP50. File: hmax_RCP45_03_discharge_RP050_regrid.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_fluvial
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_fluvial_rcp45_RP050
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.02
          probability: null
          return_period: 50
    - calculation_method: simulated
      description: 'Fluvial (discharge) flood hazard - RCP8.5, RP1. File: hmax_RCP85_03_discharge_RP001_regrid.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_fluvial
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_fluvial_rcp85_RP001
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 1.0
          probability: null
          return_period: 1
    - calculation_method: simulated
      description: 'Fluvial (discharge) flood hazard - RCP8.5, RP2. File: hmax_RCP85_03_discharge_RP002_regrid.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_fluvial
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_fluvial_rcp85_RP002
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.5
          probability: null
          return_period: 2
    - calculation_method: simulated
      description: 'Fluvial (discharge) flood hazard - RCP8.5, RP5. File: hmax_RCP85_03_discharge_RP005_regrid.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_fluvial
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_fluvial_rcp85_RP005
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.2
          probability: null
          return_period: 5
    - calculation_method: simulated
      description: 'Fluvial (discharge) flood hazard - RCP8.5, RP10. File: hmax_RCP85_03_discharge_RP010_regrid.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_fluvial
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_fluvial_rcp85_RP010
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.1
          probability: null
          return_period: 10
    - calculation_method: simulated
      description: 'Fluvial (discharge) flood hazard - RCP8.5, RP50. File: hmax_RCP85_03_discharge_RP050_regrid.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_fluvial
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_fluvial_rcp85_RP050
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.02
          probability: null
          return_period: 50
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_fluvial
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_fluvial_flood
    occurrence_range: Return periods of 1, 2, 5, 10, and 50 years under Historical,
      RCP4.5, and RCP8.5 scenarios
    seasonality: null
  - analysis_type: probabilistic
    calculation_method: simulated
    event_count: 3
    events:
    - calculation_method: simulated
      description: 'Compound flood hazard combining coastal surge, pluvial rainfall,
        and fluvial discharge at 50-year return period - Historical baseline. File:
        hmax_historical_04_compound_RP050_RP050_RP050_regrid.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_compound
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_compound_hist_RP050
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.02
          probability: null
          return_period: 50
    - calculation_method: simulated
      description: 'Compound flood hazard combining coastal surge, pluvial rainfall,
        and fluvial discharge at 50-year return period - RCP4.5 scenario. File: hmax_RCP45_04_compound_RP050_RP050_RP050_regrid.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_compound
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_compound_rcp45_RP050
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.02
          probability: null
          return_period: 50
    - calculation_method: simulated
      description: 'Compound flood hazard combining coastal surge, pluvial rainfall,
        and fluvial discharge at 50-year return period - RCP8.5 scenario. File: hmax_RCP85_04_compound_RP050_RP050_RP050_regrid.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_compound
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_compound_rcp85_RP050
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.02
          probability: null
          return_period: 50
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_compound
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_compound_flood
    occurrence_range: 50-year return period compound flood (coastal + pluvial + fluvial
      combined) under Historical, RCP4.5, and RCP8.5 scenarios
    seasonality: null
license: CC-BY-4.0
lineage:
  description: Flood impact assessment for Greater Monrovia, Liberia, produced by
    Deltares using FIAT (Flood Impact Assessment Tool). Hydrodynamic flood inundation
    modelled for coastal, pluvial, fluvial, and compound flood scenarios under historical
    and climate change (RCP4.5, RCP8.5) conditions using the JAXA ALOS World 3D (AW3D)
    Digital Terrain Model at 5 m resolution as topographic input. Building exposure
    rasters distinguished five residential construction types (formal concrete, informal
    concrete, mud, zinc, other) plus commercial, industrial, and public facilities.
    Depth-damage vulnerability functions were calibrated for local conditions using
    FIAT configuration files. Risk metrics (direct damage, affected population, expected
    annual damage) were derived by integrating hazard, exposure, and vulnerability
    across return periods of 1 to 50 years.
  sources:
  - id: source_fiat
    license: null
    name: FIAT (Flood Impact Assessment Tool, Deltares)
    risk_data_type: null
    type: model
    url: https://www.deltares.nl/en/software-and-data/products/flood-impact-assessment-tool-fiat
    used_in: loss
  - id: source_aw3d_dtm
    license: null
    name: AW3D Digital Terrain Model (JAXA ALOS World 3D)
    risk_data_type: null
    type: dataset
    url: https://www.eorc.jaxa.jp/ALOS/en/aw3d30/
    used_in: hazard
  - id: source_flood_models
    license: null
    name: Hydrodynamic flood models
    risk_data_type: null
    type: model
    url: null
    used_in: hazard
  - id: source_vulnerability_functions
    license: null
    name: Depth-damage vulnerability functions
    risk_data_type: null
    type: model
    url: null
    used_in: vulnerability
  - id: source_climate_projections
    license: null
    name: Climate change projections (RCP4.5, RCP8.5)
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
    description: 'Total annual expected risk (EAD) for Greater Monrovia under Historical
      climate baseline, integrating all flood hazard types (coastal, pluvial, fluvial,
      compound) and return periods (1-50 years) across all asset categories. FIAT-computed
      from depth-damage vulnerability functions applied to exposure rasters. Raster
      file: FIATpostprocessing/Total_risk_historic.tif.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_annual_risk_historic
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
    description: 'Total annual expected risk (EAD) for Greater Monrovia under RCP4.5
      moderate emissions climate scenario. Raster file: FIATpostprocessing/Total_risk_RCP45.tif.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_annual_risk_rcp45
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
    description: 'Total annual expected risk (EAD) for Greater Monrovia under RCP8.5
      high emissions climate scenario. Raster file: FIATpostprocessing/Total_risk_RCP85.tif.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_annual_risk_rcp85
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
    description: 'Community-level aggregated annual expected risk for Greater Monrovia
      under Historical baseline. Shapefile: Shapefiles_risk/Current_Risk.shp. Enables
      community-level investment prioritization.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_community_risk_historic
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
    description: 'Community-level aggregated annual expected risk for Greater Monrovia
      under RCP4.5 scenario. Shapefile: Shapefiles_risk/RCP45_Risk.shp.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_community_risk_rcp45
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
    description: 'Community-level aggregated annual expected risk for Greater Monrovia
      under RCP8.5 scenario. Shapefile: Shapefiles_risk/RCP85_Risk.shp.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_community_risk_rcp85
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
project:
  name: WBG Urban Flood Risk Assessment (UFRA) - Liberia, Greater Monrovia
  url: https://www.worldbank.org
publisher:
  affiliation: null
  email: data@gfdrr.org
  name: Global Facility for Disaster Reduction and Recovery (GFDRR)
  url: https://www.gfdrr.org/en
purpose: To support the Government of Liberia and Monrovia city authorities in understanding
  multi-hazard flood risk under current and future climate conditions, enabling evidence-based
  investment prioritization for flood risk reduction in Greater Monrovia's communities.
referenced_by: []
resources:
- access_url: https://datacatalog.worldbank.org/search/dataset/0067049/multi-hazard-flood-risk-assessment-for-greater-monrovia-liberia
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
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
  format: null
  id: resource_hazard_layers
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Flood Hazard Inundation Layers - Greater Monrovia
- access_url: https://datacatalog.worldbank.org/search/dataset/0067049/multi-hazard-flood-risk-assessment-for-greater-monrovia-liberia
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
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
  format: null
  id: resource_risk_layers
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Flood Risk Layers - Exposure, Vulnerability, Loss, and Risk Outputs
risk_data_type:
- hazard
- exposure
- vulnerability
- loss
schema: rdls-10
slug: rdls_hel-lbr_monroviafloodrisk
spatial:
  bbox:
  - -10.85
  - 6.25
  - -10.7
  - 6.4
  centroid: null
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
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Multi-Hazard Flood Risk Assessment for Greater Monrovia, Liberia
version: '1.0'
vulnerability:
  functions:
    damage_to_loss: []
    engineering_demand: []
    fragility: []
    socio_economic: []
    vulnerability:
    - analysis_details: FIAT depth-damage function 1 (Functions/1.csv) - assigned
        to formal/standard building structures in Greater Monrovia. Defines discrete
        depth vs. damage-factor relationship.
      approach: empirical
      category: buildings
      hazard_analysis_type: probabilistic
      hazard_primary:
        classification: null
        id: hazard_flood
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      hazard_secondary: null
      id: vuln_func_1
      impact:
        measurement:
          quantity_kind: dimensionless_ratio
          unit: null
        metric: damage
        modelling: simulated
        type: direct
      relationship: discrete
      taxonomy: Custom
    - analysis_details: FIAT depth-damage function 2 (Functions/2.csv) - assigned
        to informal/basic building structures in Greater Monrovia. Defines discrete
        depth vs. damage-factor relationship.
      approach: empirical
      category: buildings
      hazard_analysis_type: probabilistic
      hazard_primary:
        classification: null
        id: hazard_flood
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      hazard_secondary: null
      id: vuln_func_2
      impact:
        measurement:
          quantity_kind: dimensionless_ratio
          unit: null
        metric: damage
        modelling: simulated
        type: direct
      relationship: discrete
      taxonomy: Custom
    - analysis_details: FIAT depth-damage function 6 (Functions/6.csv) - assigned
        to specific asset categories (commercial, industrial, public facilities) in
        Greater Monrovia. Defines discrete depth vs. damage-factor relationship.
      approach: empirical
      category: buildings
      hazard_analysis_type: probabilistic
      hazard_primary:
        classification: null
        id: hazard_flood
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      hazard_secondary: null
      id: vuln_func_6
      impact:
        measurement:
          quantity_kind: dimensionless_ratio
          unit: null
        metric: damage
        modelling: simulated
        type: direct
      relationship: discrete
      taxonomy: Custom
---
