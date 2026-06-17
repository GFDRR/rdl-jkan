---
attributions:
- entity:
    affiliation: null
    email: admin@geosas.net
    name: GeoSAS
    url: https://www.geosas.net/
  id: attribution_collaborator
  role: collaborator
catalog: World Bank Data Catalog
contact_point:
  affiliation: null
  email: pchrzanowski@worldbank.org
  name: Pierre Chrzanowski
  url: https://www.gfdrr.org/en
creator:
  affiliation: null
  email: frivas@gmv.com
  name: GMV Innovating Solutions S.L.
  url: https://www.gmv.com/en-es
dataset_id: rdls_hzd-eth_climatedisasterriskdb
description: A comprehensive spatial database containing climate and disaster risk
  information for Ethiopian secondary cities (above 20,000 inhabitants), combining
  remote sensing data, earth observation methods, and geodata on climatic and non-climatic
  hazards to support disaster risk management and urban resilience planning.
details: 'This dataset was developed as part of the ACP-EU Disaster Risk Management
  Program (Component: Improve urban and peri-urban resilience mechanisms) from January
  2024 to June 2025. The database includes city-level hazard mapping, urban growth
  dynamics analysis, and disaster exposure assessments for all Ethiopian urban areas
  above 20,000 inhabitants. The data supports the establishment of an Urban Observatory
  and is used by the Ministry of Urban Development and Infrastructure, Ethiopia Space
  Science and Geospatial Institute, and Ethiopia Disaster Risk Management Commission
  for evidence-based decision-making on disaster risk reduction and climate adaptation
  investments.'
exposure:
- asset_type:
    description: Built-up surface area classified using the GEM GED4ALL schema, sourced
      from the World Bank Climate Disaster Risk Database.
    id: bui
    scheme: GED4ALL
    title: Building taxonomy
    uri: https://wiki.openstreetmap.org/wiki/GED4ALL
  category: buildings
  id: exposure_builtup_surface
  metrics:
  - dimension: structure
    id: metric_builtup_surface
    measurement:
      quantity_kind: area
      unit: null
- asset_type:
    description: Population exposure classified using the GEM GED4ALL schema, sourced
      from the World Bank Climate Disaster Risk Database.
    id: sei-pop
    scheme: GED4ALL
    title: Population taxonomy
    uri: https://wiki.openstreetmap.org/wiki/GED4ALL
  category: population
  id: exposure_population
  metrics:
  - dimension: population
    id: metric_population
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Built-up area and population exposed to 100-year return period flood,
      from the World Bank Climate Disaster Risk Database.
    id: bui
    scheme: GED4ALL
    title: Building taxonomy
    uri: https://wiki.openstreetmap.org/wiki/GED4ALL
  category: buildings
  id: exposure_flood_100rp
  metrics:
  - dimension: structure
    id: metric_flood_100rp_bus_exposure
    measurement:
      quantity_kind: area
      unit: null
  - dimension: population
    id: metric_flood_100rp_pop_exposure
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Built-up area and population exposed to 20-year return period flood,
      from the World Bank Climate Disaster Risk Database.
    id: bui
    scheme: GED4ALL
    title: Building taxonomy
    uri: https://wiki.openstreetmap.org/wiki/GED4ALL
  category: buildings
  id: exposure_flood_20rp
  metrics:
  - dimension: structure
    id: metric_flood_20rp_bus_exposure
    measurement:
      quantity_kind: area
      unit: null
  - dimension: population
    id: metric_flood_20rp_pop_exposure
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Built-up area and population exposed to 5-year return period flood,
      from the World Bank Climate Disaster Risk Database.
    id: bui
    scheme: GED4ALL
    title: Building taxonomy
    uri: https://wiki.openstreetmap.org/wiki/GED4ALL
  category: buildings
  id: exposure_flood_5rp
  metrics:
  - dimension: structure
    id: metric_flood_5rp_bus_exposure
    measurement:
      quantity_kind: area
      unit: null
  - dimension: population
    id: metric_flood_5rp_pop_exposure
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Built-up area and population exposed to landslide hazard, from the
      World Bank Climate Disaster Risk Database.
    id: bui
    scheme: GED4ALL
    title: Building taxonomy
    uri: https://wiki.openstreetmap.org/wiki/GED4ALL
  category: buildings
  id: exposure_landslide
  metrics:
  - dimension: structure
    id: metric_landslide_bus_exposure
    measurement:
      quantity_kind: area
      unit: null
  - dimension: population
    id: metric_landslide_pop_exposure
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Absolute growth in built-up surface area, from the World Bank Climate
      Disaster Risk Database.
    id: bui
    scheme: GED4ALL
    title: Building taxonomy
    uri: https://wiki.openstreetmap.org/wiki/GED4ALL
  category: buildings
  id: exposure_builtup_growth_abs
  metrics:
  - dimension: structure
    id: metric_builtup_growth_absolute
    measurement:
      quantity_kind: area
      unit: null
- asset_type:
    description: Share of growth in built-up surface area, from the World Bank Climate
      Disaster Risk Database.
    id: bui
    scheme: GED4ALL
    title: Building taxonomy
    uri: https://wiki.openstreetmap.org/wiki/GED4ALL
  category: buildings
  id: exposure_builtup_growth_share
  metrics:
  - dimension: structure
    id: metric_builtup_growth_share
    measurement:
      quantity_kind: dimensionless_ratio
      unit: null
- asset_type:
    description: Absolute growth in population, from the World Bank Climate Disaster
      Risk Database.
    id: sei-pop
    scheme: GED4ALL
    title: Population taxonomy
    uri: https://wiki.openstreetmap.org/wiki/GED4ALL
  category: population
  id: exposure_population_growth_abs
  metrics:
  - dimension: population
    id: metric_population_growth_absolute
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Share of growth in population, from the World Bank Climate Disaster
      Risk Database.
    id: sei-pop
    scheme: GED4ALL
    title: Population taxonomy
    uri: https://wiki.openstreetmap.org/wiki/GED4ALL
  category: population
  id: exposure_population_growth_share
  metrics:
  - dimension: population
    id: metric_population_growth_share
    measurement:
      quantity_kind: dimensionless_ratio
      unit: null
- asset_type:
    description: Built-up area and population in major cities, from the World Bank
      Climate Disaster Risk Database.
    id: bui
    scheme: GED4ALL
    title: Building taxonomy
    uri: https://wiki.openstreetmap.org/wiki/GED4ALL
  category: buildings
  id: exposure_cities
  metrics:
  - dimension: structure
    id: metric_cities_builtup_exposure
    measurement:
      quantity_kind: area
      unit: null
  - dimension: population
    id: metric_cities_population_exposure
    measurement:
      quantity_kind: count
      unit: count
  - dimension: index
    id: metric_cities_multihazard_exposure
    measurement:
      quantity_kind: index
      unit: null
- asset_type:
    description: Growth in built-up area exposure in major cities, from the World
      Bank Climate Disaster Risk Database.
    id: bui
    scheme: GED4ALL
    title: Building taxonomy
    uri: https://wiki.openstreetmap.org/wiki/GED4ALL
  category: buildings
  id: exposure_cities_growth
  metrics:
  - dimension: index
    id: metric_cities_exposure_growth
    measurement:
      quantity_kind: index
      unit: null
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: simulated
    event_count: 6
    events:
    - calculation_method: simulated
      description: Spatial dataset showing drought hazard levels across Ethiopia for
        the period 2000-2004 from the CLARISSE Climate and Disaster Risk Database.
      disaster_identifiers: []
      hazard:
        classification: null
        id: drought_hazard_ref
        intensity_measure: SPI:dimensionless
        process: meteorological_drought
        trigger: null
        type: drought
      id: CLARISSE_DroughtHazard_Ethiopia_2000-2004_20250516
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P5Y
            end: '2004'
            start: '2000'
        probabilistic: null
    - calculation_method: simulated
      description: Spatial dataset showing drought hazard levels across Ethiopia for
        the period 2005-2009 from the CLARISSE Climate and Disaster Risk Database.
      disaster_identifiers: []
      hazard:
        classification: null
        id: drought_hazard_ref
        intensity_measure: SPI:dimensionless
        process: meteorological_drought
        trigger: null
        type: drought
      id: CLARISSE_DroughtHazard_Ethiopia_2005-2009_20250516
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P5Y
            end: '2009'
            start: '2005'
        probabilistic: null
    - calculation_method: simulated
      description: Spatial dataset showing drought hazard levels across Ethiopia for
        the period 2010-2014 from the CLARISSE Climate and Disaster Risk Database.
      disaster_identifiers: []
      hazard:
        classification: null
        id: drought_hazard_ref
        intensity_measure: SPI:dimensionless
        process: meteorological_drought
        trigger: null
        type: drought
      id: CLARISSE_DroughtHazard_Ethiopia_2010-2014_20250516
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P5Y
            end: '2014'
            start: '2010'
        probabilistic: null
    - calculation_method: simulated
      description: Spatial dataset showing drought hazard levels across Ethiopia for
        the period 2015-2019 from the CLARISSE Climate and Disaster Risk Database.
      disaster_identifiers: []
      hazard:
        classification: null
        id: drought_hazard_ref
        intensity_measure: SPI:dimensionless
        process: meteorological_drought
        trigger: null
        type: drought
      id: CLARISSE_DroughtHazard_Ethiopia_2015-2019_20250516
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P5Y
            end: '2019'
            start: '2015'
        probabilistic: null
    - calculation_method: simulated
      description: Spatial dataset showing drought hazard levels across Ethiopia for
        the period 2020-2024 from the CLARISSE Climate and Disaster Risk Database.
      disaster_identifiers: []
      hazard:
        classification: null
        id: drought_hazard_ref
        intensity_measure: SPI:dimensionless
        process: meteorological_drought
        trigger: null
        type: drought
      id: CLARISSE_DroughtHazard_Ethiopia_2020-2024_20250516
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P5Y
            end: '2024'
            start: '2020'
        probabilistic: null
    - calculation_method: simulated
      description: Spatial dataset showing drought hazard levels across Ethiopia for
        the period 2025-2029 from the CLARISSE Climate and Disaster Risk Database.
      disaster_identifiers: []
      hazard:
        classification: null
        id: drought_hazard_ref
        intensity_measure: SPI:dimensionless
        process: meteorological_drought
        trigger: null
        type: drought
      id: CLARISSE_DroughtHazard_Ethiopia_2025-2029_20250516
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P5Y
            end: '2029'
            start: '2025'
        probabilistic: null
    frequency_distribution: null
    hazards:
    - classification: null
      id: drought_hazard_ref
      intensity_measure: SPI:dimensionless
      process: meteorological_drought
      trigger: null
      type: drought
    id: event_set_drought
    occurrence_range: null
    seasonality: null
  - analysis_type: empirical
    calculation_method: simulated
    event_count: 6
    events:
    - calculation_method: simulated
      description: Spatial dataset showing earthquake hazard levels across Ethiopia
        for the period 2000-2004 from the CLARISSE Climate and Disaster Risk Database.
      disaster_identifiers: []
      hazard:
        classification: null
        id: earthquake_hazard_ref
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      id: CLARISSE_EarthquakeHazard_Ethiopia_2000-2004_20250516
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P5Y
            end: '2004'
            start: '2000'
        probabilistic: null
    - calculation_method: simulated
      description: Spatial dataset showing earthquake hazard levels across Ethiopia
        for the period 2005-2009 from the CLARISSE Climate and Disaster Risk Database.
      disaster_identifiers: []
      hazard:
        classification: null
        id: earthquake_hazard_ref
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      id: CLARISSE_EarthquakeHazard_Ethiopia_2005-2009_20250516
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P5Y
            end: '2009'
            start: '2005'
        probabilistic: null
    - calculation_method: simulated
      description: Spatial dataset showing earthquake hazard levels across Ethiopia
        for the period 2010-2014 from the CLARISSE Climate and Disaster Risk Database.
      disaster_identifiers: []
      hazard:
        classification: null
        id: earthquake_hazard_ref
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      id: CLARISSE_EarthquakeHazard_Ethiopia_2010-2014_20250516
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P5Y
            end: '2014'
            start: '2010'
        probabilistic: null
    - calculation_method: simulated
      description: Spatial dataset showing earthquake hazard levels across Ethiopia
        for the period 2015-2019 from the CLARISSE Climate and Disaster Risk Database.
      disaster_identifiers: []
      hazard:
        classification: null
        id: earthquake_hazard_ref
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      id: CLARISSE_EarthquakeHazard_Ethiopia_2015-2019_20250516
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P5Y
            end: '2019'
            start: '2015'
        probabilistic: null
    - calculation_method: simulated
      description: Spatial dataset showing earthquake hazard levels across Ethiopia
        for the period 2020-2024 from the CLARISSE Climate and Disaster Risk Database.
      disaster_identifiers: []
      hazard:
        classification: null
        id: earthquake_hazard_ref
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      id: CLARISSE_EarthquakeHazard_Ethiopia_2020-2024_20250516
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P5Y
            end: '2024'
            start: '2020'
        probabilistic: null
    - calculation_method: simulated
      description: Spatial dataset showing projected earthquake hazard levels across
        Ethiopia for the period 2025-2029 from the CLARISSE Climate and Disaster Risk
        Database.
      disaster_identifiers: []
      hazard:
        classification: null
        id: earthquake_hazard_ref
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      id: CLARISSE_EarthquakeHazard_Ethiopia_2025-2029_20250516
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P5Y
            end: '2029'
            start: '2025'
        probabilistic: null
    frequency_distribution: null
    hazards:
    - classification: null
      id: earthquake_hazard_ref
      intensity_measure: PGA:g
      process: ground_motion
      trigger: null
      type: earthquake
    id: event_set_earthquake
    occurrence_range: null
    seasonality: null
  - analysis_type: probabilistic
    calculation_method: simulated
    event_count: 6
    events:
    - calculation_method: simulated
      description: Spatial dataset showing flood hazard zones with a 5-year return
        period across Ethiopia for the period 2000-2004 from the CLARISSE Climate
        and Disaster Risk Database.
      disaster_identifiers: []
      hazard:
        classification: null
        id: flood_5rp_hazard_ref
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: CLARISSE_FloodHazard-5RP_Ethiopia_2000-2004_20250516
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P5Y
            end: '2004'
            start: '2000'
        probabilistic:
          event_rate: null
          probability: null
          return_period: 5
    - calculation_method: simulated
      description: Spatial dataset showing flood hazard zones with a 5-year return
        period across Ethiopia for the period 2005-2009 from the CLARISSE Climate
        and Disaster Risk Database.
      disaster_identifiers: []
      hazard:
        classification: null
        id: flood_5rp_hazard_ref
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: CLARISSE_FloodHazard-5RP_Ethiopia_2005-2009_20250516
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P5Y
            end: '2009'
            start: '2005'
        probabilistic:
          event_rate: null
          probability: null
          return_period: 5
    - calculation_method: simulated
      description: Spatial dataset showing flood hazard zones with a 5-year return
        period across Ethiopia for the period 2010-2014 from the CLARISSE Climate
        and Disaster Risk Database.
      disaster_identifiers: []
      hazard:
        classification: null
        id: flood_5rp_hazard_ref
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: CLARISSE_FloodHazard-5RP_Ethiopia_2010-2014_20250516
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P5Y
            end: '2014'
            start: '2010'
        probabilistic:
          event_rate: null
          probability: null
          return_period: 5
    - calculation_method: simulated
      description: Spatial dataset showing flood hazard zones with a 5-year return
        period across Ethiopia for the period 2015-2019 from the CLARISSE Climate
        and Disaster Risk Database.
      disaster_identifiers: []
      hazard:
        classification: null
        id: flood_5rp_hazard_ref
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: CLARISSE_FloodHazard-5RP_Ethiopia_2015-2019_20250516
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P5Y
            end: '2019'
            start: '2015'
        probabilistic:
          event_rate: null
          probability: null
          return_period: 5
    - calculation_method: simulated
      description: Spatial dataset showing flood hazard zones with a 5-year return
        period across Ethiopia for the period 2020-2024 from the CLARISSE Climate
        and Disaster Risk Database.
      disaster_identifiers: []
      hazard:
        classification: null
        id: flood_5rp_hazard_ref
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: CLARISSE_FloodHazard-5RP_Ethiopia_2020-2024_20250516
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P5Y
            end: '2024'
            start: '2020'
        probabilistic:
          event_rate: null
          probability: null
          return_period: 5
    - calculation_method: simulated
      description: Spatial dataset showing projected flood hazard zones with a 5-year
        return period across Ethiopia for the period 2025-2029 from the CLARISSE Climate
        and Disaster Risk Database.
      disaster_identifiers: []
      hazard:
        classification: null
        id: flood_5rp_hazard_ref
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: CLARISSE_FloodHazard-5RP_Ethiopia_2025-2029_20250516
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P5Y
            end: '2029'
            start: '2025'
        probabilistic:
          event_rate: null
          probability: null
          return_period: 5
    frequency_distribution: null
    hazards:
    - classification: null
      id: flood_5rp_hazard_ref
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_flood_5rp
    occurrence_range: null
    seasonality: null
  - analysis_type: probabilistic
    calculation_method: simulated
    event_count: 6
    events:
    - calculation_method: simulated
      description: Spatial dataset showing flood hazard zones with a 20-year return
        period across Ethiopia for the period 2000-2004 from the CLARISSE Climate
        and Disaster Risk Database.
      disaster_identifiers: []
      hazard:
        classification: null
        id: flood_20rp_hazard_ref
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: CLARISSE_FloodHazard-20RP_Ethiopia_2000-2004_20250516
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P5Y
            end: '2004'
            start: '2000'
        probabilistic:
          event_rate: null
          probability: null
          return_period: 20
    - calculation_method: simulated
      description: Spatial dataset showing flood hazard zones with a 20-year return
        period across Ethiopia for the period 2005-2009 from the CLARISSE Climate
        and Disaster Risk Database.
      disaster_identifiers: []
      hazard:
        classification: null
        id: flood_20rp_hazard_ref
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: CLARISSE_FloodHazard-20RP_Ethiopia_2005-2009_20250516
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P5Y
            end: '2009'
            start: '2005'
        probabilistic:
          event_rate: null
          probability: null
          return_period: 20
    - calculation_method: simulated
      description: Spatial dataset showing flood hazard zones with a 20-year return
        period across Ethiopia for the period 2010-2014 from the CLARISSE Climate
        and Disaster Risk Database.
      disaster_identifiers: []
      hazard:
        classification: null
        id: flood_20rp_hazard_ref
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: CLARISSE_FloodHazard-20RP_Ethiopia_2010-2014_20250516
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P5Y
            end: '2014'
            start: '2010'
        probabilistic:
          event_rate: null
          probability: null
          return_period: 20
    - calculation_method: simulated
      description: Spatial dataset showing flood hazard zones with a 20-year return
        period across Ethiopia for the period 2015-2019 from the CLARISSE Climate
        and Disaster Risk Database.
      disaster_identifiers: []
      hazard:
        classification: null
        id: flood_20rp_hazard_ref
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: CLARISSE_FloodHazard-20RP_Ethiopia_2015-2019_20250516
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P5Y
            end: '2019'
            start: '2015'
        probabilistic:
          event_rate: null
          probability: null
          return_period: 20
    - calculation_method: simulated
      description: Spatial dataset showing flood hazard zones with a 20-year return
        period across Ethiopia for the period 2020-2024 from the CLARISSE Climate
        and Disaster Risk Database.
      disaster_identifiers: []
      hazard:
        classification: null
        id: flood_20rp_hazard_ref
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: CLARISSE_FloodHazard-20RP_Ethiopia_2020-2024_20250516
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P5Y
            end: '2024'
            start: '2020'
        probabilistic:
          event_rate: null
          probability: null
          return_period: 20
    - calculation_method: simulated
      description: Spatial dataset showing projected flood hazard zones with a 20-year
        return period across Ethiopia for the period 2025-2029 from the CLARISSE Climate
        and Disaster Risk Database.
      disaster_identifiers: []
      hazard:
        classification: null
        id: flood_20rp_hazard_ref
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: CLARISSE_FloodHazard-20RP_Ethiopia_2025-2029_20250516
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P5Y
            end: '2029'
            start: '2025'
        probabilistic:
          event_rate: null
          probability: null
          return_period: 20
    frequency_distribution: null
    hazards:
    - classification: null
      id: flood_20rp_hazard_ref
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_flood_20rp
    occurrence_range: null
    seasonality: null
  - analysis_type: probabilistic
    calculation_method: simulated
    event_count: 6
    events:
    - calculation_method: simulated
      description: Spatial dataset showing flood hazard zones with a 100-year return
        period across Ethiopia for the period 2000-2004 from the CLARISSE Climate
        and Disaster Risk Database.
      disaster_identifiers: []
      hazard:
        classification: null
        id: flood_100rp_hazard_ref
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: CLARISSE_FloodHazard-100RP_Ethiopia_2000-2004_20250516
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P5Y
            end: '2004'
            start: '2000'
        probabilistic:
          event_rate: null
          probability: null
          return_period: 100
    - calculation_method: simulated
      description: Spatial dataset showing flood hazard zones with a 100-year return
        period across Ethiopia for the period 2005-2009 from the CLARISSE Climate
        and Disaster Risk Database.
      disaster_identifiers: []
      hazard:
        classification: null
        id: flood_100rp_hazard_ref
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: CLARISSE_FloodHazard-100RP_Ethiopia_2005-2009_20250516
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P5Y
            end: '2009'
            start: '2005'
        probabilistic:
          event_rate: null
          probability: null
          return_period: 100
    - calculation_method: simulated
      description: Spatial dataset showing flood hazard zones with a 100-year return
        period across Ethiopia for the period 2010-2014 from the CLARISSE Climate
        and Disaster Risk Database.
      disaster_identifiers: []
      hazard:
        classification: null
        id: flood_100rp_hazard_ref
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: CLARISSE_FloodHazard-100RP_Ethiopia_2010-2014_20250516
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P5Y
            end: '2014'
            start: '2010'
        probabilistic:
          event_rate: null
          probability: null
          return_period: 100
    - calculation_method: simulated
      description: Spatial dataset showing flood hazard zones with a 100-year return
        period across Ethiopia for the period 2015-2019 from the CLARISSE Climate
        and Disaster Risk Database.
      disaster_identifiers: []
      hazard:
        classification: null
        id: flood_100rp_hazard_ref
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: CLARISSE_FloodHazard-100RP_Ethiopia_2015-2019_20250516
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P5Y
            end: '2019'
            start: '2015'
        probabilistic:
          event_rate: null
          probability: null
          return_period: 100
    - calculation_method: simulated
      description: Spatial dataset showing flood hazard zones with a 100-year return
        period across Ethiopia for the period 2020-2024 from the CLARISSE Climate
        and Disaster Risk Database.
      disaster_identifiers: []
      hazard:
        classification: null
        id: flood_100rp_hazard_ref
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: CLARISSE_FloodHazard-100RP_Ethiopia_2020-2024_20250516
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P5Y
            end: '2024'
            start: '2020'
        probabilistic:
          event_rate: null
          probability: null
          return_period: 100
    - calculation_method: simulated
      description: Spatial dataset showing projected flood hazard zones with a 100-year
        return period across Ethiopia for the period 2025-2029 from the CLARISSE Climate
        and Disaster Risk Database.
      disaster_identifiers: []
      hazard:
        classification: null
        id: flood_100rp_hazard_ref
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: CLARISSE_FloodHazard-100RP_Ethiopia_2025-2029_20250516
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P5Y
            end: '2029'
            start: '2025'
        probabilistic:
          event_rate: null
          probability: null
          return_period: 100
    frequency_distribution: null
    hazards:
    - classification: null
      id: flood_100rp_hazard_ref
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_flood_100rp
    occurrence_range: null
    seasonality: null
  - analysis_type: empirical
    calculation_method: simulated
    event_count: 6
    events:
    - calculation_method: simulated
      description: Spatial dataset showing heat stress hazard levels across Ethiopia
        for the period 2000-2004 from the CLARISSE Climate and Disaster Risk Database.
      disaster_identifiers: []
      hazard:
        classification: null
        id: heat_stress_hazard_ref
        intensity_measure: T:C
        process: extreme_heat
        trigger: null
        type: extreme_temperature
      id: CLARISSE_HeatStressHazard_Ethiopia_2000-2004_20250516
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P5Y
            end: '2004'
            start: '2000'
        probabilistic: null
    - calculation_method: simulated
      description: Spatial dataset showing heat stress hazard levels across Ethiopia
        for the period 2005-2009 from the CLARISSE Climate and Disaster Risk Database.
      disaster_identifiers: []
      hazard:
        classification: null
        id: heat_stress_hazard_ref
        intensity_measure: T:C
        process: extreme_heat
        trigger: null
        type: extreme_temperature
      id: CLARISSE_HeatStressHazard_Ethiopia_2005-2009_20250516
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P5Y
            end: '2009'
            start: '2005'
        probabilistic: null
    - calculation_method: simulated
      description: Spatial dataset showing heat stress hazard levels across Ethiopia
        for the period 2010-2014 from the CLARISSE Climate and Disaster Risk Database.
      disaster_identifiers: []
      hazard:
        classification: null
        id: heat_stress_hazard_ref
        intensity_measure: T:C
        process: extreme_heat
        trigger: null
        type: extreme_temperature
      id: CLARISSE_HeatStressHazard_Ethiopia_2010-2014_20250516
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P5Y
            end: '2014'
            start: '2010'
        probabilistic: null
    - calculation_method: simulated
      description: Spatial dataset showing heat stress hazard levels across Ethiopia
        for the period 2015-2019 from the CLARISSE Climate and Disaster Risk Database.
      disaster_identifiers: []
      hazard:
        classification: null
        id: heat_stress_hazard_ref
        intensity_measure: T:C
        process: extreme_heat
        trigger: null
        type: extreme_temperature
      id: CLARISSE_HeatStressHazard_Ethiopia_2015-2019_20250516
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P5Y
            end: '2019'
            start: '2015'
        probabilistic: null
    - calculation_method: simulated
      description: Spatial dataset showing heat stress hazard levels across Ethiopia
        for the period 2020-2024 from the CLARISSE Climate and Disaster Risk Database.
      disaster_identifiers: []
      hazard:
        classification: null
        id: heat_stress_hazard_ref
        intensity_measure: T:C
        process: extreme_heat
        trigger: null
        type: extreme_temperature
      id: CLARISSE_HeatStressHazard_Ethiopia_2020-2024_20250516
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P5Y
            end: '2024'
            start: '2020'
        probabilistic: null
    - calculation_method: simulated
      description: Spatial dataset showing projected heat stress hazard levels across
        Ethiopia for the period 2025-2029 from the CLARISSE Climate and Disaster Risk
        Database.
      disaster_identifiers: []
      hazard:
        classification: null
        id: heat_stress_hazard_ref
        intensity_measure: T:C
        process: extreme_heat
        trigger: null
        type: extreme_temperature
      id: CLARISSE_HeatStressHazard_Ethiopia_2025-2029_20250516
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P5Y
            end: '2029'
            start: '2025'
        probabilistic: null
    frequency_distribution: null
    hazards:
    - classification: null
      id: heat_stress_hazard_ref
      intensity_measure: T:C
      process: extreme_heat
      trigger: null
      type: extreme_temperature
    id: event_set_heat_stress
    occurrence_range: null
    seasonality: null
  - analysis_type: empirical
    calculation_method: simulated
    event_count: 6
    events:
    - calculation_method: simulated
      description: Spatial dataset showing landslide hazard levels across Ethiopia
        for the period 2000-2004 from the CLARISSE Climate and Disaster Risk Database.
      disaster_identifiers: []
      hazard:
        classification: null
        id: landslide_hazard_ref
        intensity_measure: LSI:-
        process: landslide_general
        trigger: null
        type: landslide
      id: CLARISSE_LandslideHazard_Ethiopia_2000-2004_20250516
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P5Y
            end: '2004'
            start: '2000'
        probabilistic: null
    - calculation_method: simulated
      description: Spatial dataset showing landslide hazard levels across Ethiopia
        for the period 2005-2009 from the CLARISSE Climate and Disaster Risk Database.
      disaster_identifiers: []
      hazard:
        classification: null
        id: landslide_hazard_ref
        intensity_measure: LSI:-
        process: landslide_general
        trigger: null
        type: landslide
      id: CLARISSE_LandslideHazard_Ethiopia_2005-2009_20250516
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P5Y
            end: '2009'
            start: '2005'
        probabilistic: null
    - calculation_method: simulated
      description: Spatial dataset showing landslide hazard levels across Ethiopia
        for the period 2010-2014 from the CLARISSE Climate and Disaster Risk Database.
      disaster_identifiers: []
      hazard:
        classification: null
        id: landslide_hazard_ref
        intensity_measure: LSI:-
        process: landslide_general
        trigger: null
        type: landslide
      id: CLARISSE_LandslideHazard_Ethiopia_2010-2014_20250516
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P5Y
            end: '2014'
            start: '2010'
        probabilistic: null
    - calculation_method: simulated
      description: Spatial dataset showing landslide hazard levels across Ethiopia
        for the period 2015-2019 from the CLARISSE Climate and Disaster Risk Database.
      disaster_identifiers: []
      hazard:
        classification: null
        id: landslide_hazard_ref
        intensity_measure: LSI:-
        process: landslide_general
        trigger: null
        type: landslide
      id: CLARISSE_LandslideHazard_Ethiopia_2015-2019_20250516
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P5Y
            end: '2019'
            start: '2015'
        probabilistic: null
    - calculation_method: simulated
      description: Spatial dataset showing landslide hazard levels across Ethiopia
        for the period 2020-2024 from the CLARISSE Climate and Disaster Risk Database.
      disaster_identifiers: []
      hazard:
        classification: null
        id: landslide_hazard_ref
        intensity_measure: LSI:-
        process: landslide_general
        trigger: null
        type: landslide
      id: CLARISSE_LandslideHazard_Ethiopia_2020-2024_20250516
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P5Y
            end: '2024'
            start: '2020'
        probabilistic: null
    - calculation_method: simulated
      description: Spatial dataset showing projected landslide hazard levels across
        Ethiopia for the period 2025-2029 from the CLARISSE Climate and Disaster Risk
        Database.
      disaster_identifiers: []
      hazard:
        classification: null
        id: landslide_hazard_ref
        intensity_measure: LSI:-
        process: landslide_general
        trigger: null
        type: landslide
      id: CLARISSE_LandslideHazard_Ethiopia_2025-2029_20250516
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P5Y
            end: '2029'
            start: '2025'
        probabilistic: null
    frequency_distribution: null
    hazards:
    - classification: null
      id: landslide_hazard_ref
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: event_set_landslide
    occurrence_range: null
    seasonality: null
  - analysis_type: empirical
    calculation_method: simulated
    event_count: 6
    events:
    - calculation_method: simulated
      description: Spatial dataset showing volcanic hazard levels across Ethiopia
        for the period 2000-2004 from the CLARISSE Climate and Disaster Risk Database.
      disaster_identifiers: []
      hazard:
        classification: null
        id: volcanic_hazard_ref
        intensity_measure: ash_thickness:cm
        process: ashfall
        trigger: null
        type: volcanic
      id: CLARISSE_VolcanicHazard_Ethiopia_2000-2004_20250516
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P5Y
            end: '2004'
            start: '2000'
        probabilistic: null
    - calculation_method: simulated
      description: Spatial dataset showing volcanic hazard levels across Ethiopia
        for the period 2005-2009 from the CLARISSE Climate and Disaster Risk Database.
      disaster_identifiers: []
      hazard:
        classification: null
        id: volcanic_hazard_ref
        intensity_measure: ash_thickness:cm
        process: ashfall
        trigger: null
        type: volcanic
      id: CLARISSE_VolcanicHazard_Ethiopia_2005-2009_20250516
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P5Y
            end: '2009'
            start: '2005'
        probabilistic: null
    - calculation_method: simulated
      description: Spatial dataset showing volcanic hazard levels across Ethiopia
        for the period 2010-2014 from the CLARISSE Climate and Disaster Risk Database.
      disaster_identifiers: []
      hazard:
        classification: null
        id: volcanic_hazard_ref
        intensity_measure: ash_thickness:cm
        process: ashfall
        trigger: null
        type: volcanic
      id: CLARISSE_VolcanicHazard_Ethiopia_2010-2014_20250516
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P5Y
            end: '2014'
            start: '2010'
        probabilistic: null
    - calculation_method: simulated
      description: Spatial dataset showing volcanic hazard levels across Ethiopia
        for the period 2015-2019 from the CLARISSE Climate and Disaster Risk Database.
      disaster_identifiers: []
      hazard:
        classification: null
        id: volcanic_hazard_ref
        intensity_measure: ash_thickness:cm
        process: ashfall
        trigger: null
        type: volcanic
      id: CLARISSE_VolcanicHazard_Ethiopia_2015-2019_20250516
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P5Y
            end: '2019'
            start: '2015'
        probabilistic: null
    - calculation_method: simulated
      description: Spatial dataset showing volcanic hazard levels across Ethiopia
        for the period 2020-2024 from the CLARISSE Climate and Disaster Risk Database.
      disaster_identifiers: []
      hazard:
        classification: null
        id: volcanic_hazard_ref
        intensity_measure: ash_thickness:cm
        process: ashfall
        trigger: null
        type: volcanic
      id: CLARISSE_VolcanicHazard_Ethiopia_2020-2024_20250516
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P5Y
            end: '2024'
            start: '2020'
        probabilistic: null
    - calculation_method: simulated
      description: Spatial dataset showing projected volcanic hazard levels across
        Ethiopia for the period 2025-2029 from the CLARISSE Climate and Disaster Risk
        Database.
      disaster_identifiers: []
      hazard:
        classification: null
        id: volcanic_hazard_ref
        intensity_measure: ash_thickness:cm
        process: ashfall
        trigger: null
        type: volcanic
      id: CLARISSE_VolcanicHazard_Ethiopia_2025-2029_20250516
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P5Y
            end: '2029'
            start: '2025'
        probabilistic: null
    frequency_distribution: null
    hazards:
    - classification: null
      id: volcanic_hazard_ref
      intensity_measure: ash_thickness:cm
      process: ashfall
      trigger: null
      type: volcanic
    id: event_set_volcanic
    occurrence_range: null
    seasonality: null
  type: drought, earthquake, flood, extreme_temperature, landslide, volcanic
license: CC-BY-4.0
lineage:
  description: Multi-hazard exposure and risk indicator dataset compiled from global
    sources by the World Bank Group for Ethiopia urban risk assessment. Flood inundation
    depths for 5, 20, and 100-year return periods sourced from Fathom 3.0 global flood
    hazard model. Extreme heat projections (daily maximum temperature) downscaled
    from CMIP6 via the World Bank Climate Change Knowledge Portal (CCKP). Drought
    probability computed from SPI-3 indices derived from ERA5-Land rainfall via the
    Global Drought Observatory. Landslide susceptibility from the World Bank Global
    Landslide Hazard Map; seismic hazard from the GEM Global Seismic Hazard Map; volcanic
    hazard from the Global Volcano Frequency and Distribution dataset. Population
    exposure computed by overlaying hazard layers with GHS-POP-R2023A population grids
    and GHS-BUILT-S-R2023A built-up surface grids. Topographic input from the Copernicus
    DEM; rainfall climatology from CHIRPS daily precipitation.
  sources:
  - id: source_1
    license: null
    name: Fathom 3.0 global flood hazard (RP5, RP20, RP100)
    risk_data_type: null
    type: dataset
    url: https://www.fathom.global/
    used_in: hazard
  - id: source_2
    license: CC-BY-4.0
    name: Downscaled CMIP6 daily maximum temperature (CCKP)
    risk_data_type: null
    type: dataset
    url: https://climateknowledgeportal.worldbank.org/download-data
    used_in: hazard
  - id: source_3
    license: CC-BY-4.0
    name: SPI-3 drought index from ERA5-Land via Global Drought Observatory
    risk_data_type: null
    type: dataset
    url: https://drought.emergency.copernicus.eu/tumbo/gdo/map/
    used_in: hazard
  - id: source_4
    license: CC-BY-4.0
    name: World Bank Global Landslide Hazard Map
    risk_data_type: null
    type: dataset
    url: https://datacatalog.worldbank.org/search/dataset/0037584/Global-landslide-hazard-map
    used_in: hazard
  - id: source_5
    license: CC-BY-4.0
    name: Global Seismic Hazard Map (GEM)
    risk_data_type: null
    type: dataset
    url: https://www.globalquakemodel.org/product/global-seismic-hazard-map
    used_in: hazard
  - id: source_6
    license: CC-BY-4.0
    name: Global Volcano Hazard Frequency and Distribution
    risk_data_type: null
    type: dataset
    url: https://www.earthdata.nasa.gov/data/catalog/sedac-ciesin-chrr-ndh-volcano-hfd-1.0
    used_in: hazard
  - id: source_7
    license: CC-BY-4.0
    name: GHS-POP-R2023A Global Human Settlement Population
    risk_data_type: null
    type: dataset
    url: https://human-settlement.emergency.copernicus.eu/ghs_pop.php
    used_in: exposure
  - id: source_8
    license: CC-BY-4.0
    name: GHS-BUILT-S-R2023A Global Human Settlement Built-up Surface
    risk_data_type: null
    type: dataset
    url: https://human-settlement.emergency.copernicus.eu/ghs_bu.php
    used_in: exposure
  - id: source_9
    license: CC-BY-4.0
    name: Copernicus Digital Elevation Model (DEM)
    risk_data_type: null
    type: dataset
    url: https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM
    used_in: hazard
  - id: source_10
    license: CC-BY-4.0
    name: CHIRPS daily rainfall
    risk_data_type: null
    type: dataset
    url: https://www.chc.ucsb.edu/data/chirps
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project:
  name: Ethiopia - Strengthening the Understanding of Urban Disaster Risk in Secondary
    Cities
  url: https://www.worldbank.org
publisher:
  affiliation: null
  email: data@gfdrr.org
  name: Global Facility for Disaster Reduction and Recovery (GFDRR)
  url: https://www.gfdrr.org/en
purpose: To identify and map disaster risk at the city level using remote sensing
  and earth observation methods in combination with the best available geodata for
  climatic and non-climatic hazards and disaster exposure.
referenced_by: []
resources:
- access_url: https://datacatalog.worldbank.org/search/dataset/0066935/Climate-and-Disaster-Risk-Database-at-the-City-Level-for-Ethiopia
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: City-level indicators dataset (59 variables) covering built-up surface,
    population exposure, hazard levels (flood return periods, landslides, heat stress,
    drought, earthquakes, volcanic hazards), urban growth metrics, and composite exposure
    indices for Ethiopian cities.
  download_url: https://datacatalog.worldbank.org/search/dataset/0066935/Climate-and-Disaster-Risk-Database-at-the-City-Level-for-Ethiopia
  format: null
  id: resource_1
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: City-Level Hazard Exposure and Urban Growth Indicators for Ethiopia
- access_url: https://datacatalog.worldbank.org/search/dataset/0066935/Climate-and-Disaster-Risk-Database-at-the-City-Level-for-Ethiopia
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Drought hazard GeoTIFFs from CLARISSE for periods: 2000-2004, 2005-2009,
    2010-2014, 2015-2019, 2020-2024, and projection 2025-2029. Typical IDs: CLARISSE_DroughtHazard_Ethiopia_<period>_<yyyymmdd>.'
  download_url: https://datacatalog.worldbank.org/search/dataset/0066935/Climate-and-Disaster-Risk-Database-at-the-City-Level-for-Ethiopia
  format: null
  id: resource_2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 27500
  temporal: null
  temporal_resolution: null
  title: Drought Hazard Maps for Ethiopia (Time-Sliced Series)
- access_url: https://datacatalog.worldbank.org/search/dataset/0066935/Climate-and-Disaster-Risk-Database-at-the-City-Level-for-Ethiopia
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Earthquake hazard GeoTIFFs for periods: 2000-2004, 2005-2009, 2010-2014,
    2015-2019, 2020-2024, and projection 2025-2029. Typical IDs: CLARISSE_EarthquakeHazard_Ethiopia_<period>_<yyyymmdd>.'
  download_url: https://datacatalog.worldbank.org/search/dataset/0066935/Climate-and-Disaster-Risk-Database-at-the-City-Level-for-Ethiopia
  format: null
  id: resource_3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 5600
  temporal: null
  temporal_resolution: null
  title: Earthquake Hazard Maps for Ethiopia (Time-Sliced Series)
- access_url: https://datacatalog.worldbank.org/search/dataset/0066935/Climate-and-Disaster-Risk-Database-at-the-City-Level-for-Ethiopia
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Heat stress hazard GeoTIFFs for periods: 2000-2004, 2005-2009, 2010-2014,
    2015-2019, 2020-2024, and projection 2025-2029. Typical IDs: CLARISSE_HeatStressHazard_Ethiopia_<period>_<yyyymmdd>.'
  download_url: https://datacatalog.worldbank.org/search/dataset/0066935/Climate-and-Disaster-Risk-Database-at-the-City-Level-for-Ethiopia
  format: null
  id: resource_4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 27500
  temporal: null
  temporal_resolution: null
  title: Heat Stress Hazard Maps for Ethiopia (Time-Sliced Series)
- access_url: https://datacatalog.worldbank.org/search/dataset/0066935/Climate-and-Disaster-Risk-Database-at-the-City-Level-for-Ethiopia
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Landslides hazard GeoTIFFs for periods: 2000-2004, 2005-2009, 2010-2014,
    2015-2019, 2020-2024, and projection 2025-2029. Typical IDs: CLARISSE_LandslidesHazard_Ethiopia_<period>_<yyyymmdd>.'
  download_url: https://datacatalog.worldbank.org/search/dataset/0066935/Climate-and-Disaster-Risk-Database-at-the-City-Level-for-Ethiopia
  format: null
  id: resource_5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 1000
  temporal: null
  temporal_resolution: null
  title: Landslides Hazard Maps for Ethiopia (Time-Sliced Series)
- access_url: https://datacatalog.worldbank.org/search/dataset/0066935/Climate-and-Disaster-Risk-Database-at-the-City-Level-for-Ethiopia
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Volcanic hazard GeoTIFFs for periods: 2000-2004, 2005-2009, 2010-2014,
    2015-2019, 2020-2024, and projection 2025-2029. Typical IDs: CLARISSE_VolcanicHazard_Ethiopia_<period>_<yyyymmdd>.'
  download_url: https://datacatalog.worldbank.org/search/dataset/0066935/Climate-and-Disaster-Risk-Database-at-the-City-Level-for-Ethiopia
  format: null
  id: resource_6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 4600
  temporal: null
  temporal_resolution: null
  title: Volcanic Hazard Maps for Ethiopia (Time-Sliced Series)
- access_url: https://datacatalog.worldbank.org/search/dataset/0066935/Climate-and-Disaster-Risk-Database-at-the-City-Level-for-Ethiopia
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Flood hazard GeoTIFFs (5-year return period) for periods: 2000-2004,
    2005-2009, 2010-2014, 2015-2019, 2020-2024, and projection 2025-2029. Typical
    IDs: CLARISSE_FloodHazard-5RP_Ethiopia_<period>_<yyyymmdd>.'
  download_url: https://datacatalog.worldbank.org/search/dataset/0066935/Climate-and-Disaster-Risk-Database-at-the-City-Level-for-Ethiopia
  format: null
  id: resource_7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 30
  temporal: null
  temporal_resolution: null
  title: Flood Hazard Maps (5-Year Return Period) for Ethiopia (Time-Sliced Series)
- access_url: https://datacatalog.worldbank.org/search/dataset/0066935/Climate-and-Disaster-Risk-Database-at-the-City-Level-for-Ethiopia
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Flood hazard GeoTIFFs (20-year return period) for periods: 2000-2004,
    2005-2009, 2010-2014, 2015-2019, 2020-2024, and projection 2025-2029. Typical
    IDs: CLARISSE_FloodHazard-20RP_Ethiopia_<period>_<yyyymmdd>.'
  download_url: https://datacatalog.worldbank.org/search/dataset/0066935/Climate-and-Disaster-Risk-Database-at-the-City-Level-for-Ethiopia
  format: null
  id: resource_8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 30
  temporal: null
  temporal_resolution: null
  title: Flood Hazard Maps (20-Year Return Period) for Ethiopia (Time-Sliced Series)
- access_url: https://datacatalog.worldbank.org/search/dataset/0066935/Climate-and-Disaster-Risk-Database-at-the-City-Level-for-Ethiopia
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Flood hazard GeoTIFFs (100-year return period) for periods: 2000-2004,
    2005-2009, 2010-2014, 2015-2019, 2020-2024, and projection 2025-2029. Typical
    IDs: CLARISSE_FloodHazard-100RP_Ethiopia_<period>_<yyyymmdd>.'
  download_url: https://datacatalog.worldbank.org/search/dataset/0066935/Climate-and-Disaster-Risk-Database-at-the-City-Level-for-Ethiopia
  format: null
  id: resource_9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 30
  temporal: null
  temporal_resolution: null
  title: Flood Hazard Maps (100-Year Return Period) for Ethiopia (Time-Sliced Series)
- access_url: https://datacatalog.worldbank.org/search/dataset/0066935/Climate-and-Disaster-Risk-Database-at-the-City-Level-for-Ethiopia
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Built-up surface GeoTIFFs for periods: 2000-2004, 2005-2009, 2010-2014,
    2015-2019, 2020-2024, and projection 2025-2029. Typical IDs: CLARISSE_BuiltUpSurface_Ethiopia_<period>_<yyyymmdd>.'
  download_url: https://datacatalog.worldbank.org/search/dataset/0066935/Climate-and-Disaster-Risk-Database-at-the-City-Level-for-Ethiopia
  format: null
  id: resource_10
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 100
  temporal: null
  temporal_resolution: null
  title: Built-up Surface Maps for Ethiopia (Time-Sliced Series)
- access_url: https://datacatalog.worldbank.org/search/dataset/0066935/Climate-and-Disaster-Risk-Database-at-the-City-Level-for-Ethiopia
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Population distribution GeoTIFFs for periods: 2000-2004, 2005-2009,
    2010-2014, 2015-2019, 2020-2024, and projection 2025-2029. Typical IDs: CLARISSE_Population_Ethiopia_<period>_<yyyymmdd>.'
  download_url: https://datacatalog.worldbank.org/search/dataset/0066935/Climate-and-Disaster-Risk-Database-at-the-City-Level-for-Ethiopia
  format: null
  id: resource_11
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 100
  temporal: null
  temporal_resolution: null
  title: Population Distribution Maps for Ethiopia (Time-Sliced Series)
- access_url: https://datacatalog.worldbank.org/search/dataset/0066935/Climate-and-Disaster-Risk-Database-at-the-City-Level-for-Ethiopia
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'City-level multi-hazard exposure GeoPackage outputs for periods: 2000-2004,
    2005-2009, 2010-2014, 2015-2019, 2020-2024, and projection 2025-2029. Typical
    IDs: CLARISSE_Cities_Exposure_Ethiopia_<period>_<yyyymmdd>.'
  download_url: https://datacatalog.worldbank.org/search/dataset/0066935/Climate-and-Disaster-Risk-Database-at-the-City-Level-for-Ethiopia
  format: null
  id: resource_12
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: City-Level Multi-Hazard Exposure (GPKG) for Ethiopia (Time-Sliced Series)
- access_url: https://datacatalog.worldbank.org/search/dataset/0066935/Climate-and-Disaster-Risk-Database-at-the-City-Level-for-Ethiopia
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'DEM GeoTIFF for Ethiopia (2023). Typical ID: CLARISSE_DEM_Ethiopia_2023_<yyyymmdd>.'
  download_url: https://datacatalog.worldbank.org/search/dataset/0066935/Climate-and-Disaster-Risk-Database-at-the-City-Level-for-Ethiopia
  format: null
  id: resource_13
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 30
  temporal: null
  temporal_resolution: null
  title: Digital Elevation Model for Ethiopia (2023)
- access_url: https://datacatalog.worldbank.org/search/dataset/0066935/Climate-and-Disaster-Risk-Database-at-the-City-Level-for-Ethiopia
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Annual precipitation GeoTIFFs including single-period layers (e.g.,
    2000-2004, 2005-2009, 2010-2014, 2015-2019, 2020-2024) and an aggregated layer
    (2000-2024). Typical IDs: CLARISSE_YearlyPrecipitation_Ethiopia_<period>_<yyyymmdd>.'
  download_url: https://datacatalog.worldbank.org/search/dataset/0066935/Climate-and-Disaster-Risk-Database-at-the-City-Level-for-Ethiopia
  format: null
  id: resource_14
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 5600
  temporal: null
  temporal_resolution: null
  title: Annual Precipitation for Ethiopia (GeoTIFF Series)
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_hzd-eth_climatedisasterriskdb
spatial:
  bbox: null
  centroid: null
  countries:
  - ETH
  gazetteer_entries: []
  scale: sub-national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Climate and Disaster Risk Database at the City-Level for Ethiopia
version: '1'
vulnerability: null
---
