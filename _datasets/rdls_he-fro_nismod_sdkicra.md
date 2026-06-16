---
attributions:
- entity:
    affiliation: null
    email: null
    name: Diana Jaramillo
    url: https://orcid.org/0009-0009-7747-4961
  id: attribution_creator2
  role: creator
- entity:
    affiliation: null
    email: null
    name: Chris Nicholas
    url: https://zenodo.org/search?q=metadata.creators.person_or_org.name:%22Nicholas,%20Chris%22
  id: attribution_creator3
  role: creator
- entity:
    affiliation: null
    email: null
    name: Fred Thomas
    url: https://orcid.org/0000-0002-8441-5638
  id: attribution_creator4
  role: creator
- entity:
    affiliation: null
    email: null
    name: Raghav Pant
    url: https://orcid.org/0000-0003-4648-5261
  id: attribution_creator5
  role: creator
- entity:
    affiliation: null
    email: null
    name: Jim W. Hall
    url: https://orcid.org/0000-0002-2024-9191
  id: attribution_creator6
  role: creator
- entity:
    affiliation: null
    email: fcdo.correspondence@fcdo.gov.uk
    name: UK Foreign, Commonwealth and Development Office (FCDO)
    url: https://www.gov.uk/government/organisations/foreign-commonwealth-development-office
  id: attribution_funder
  role: funder
catalog: Zenodo
contact_point:
  affiliation: null
  email: null
  name: Tom Russell
  url: https://orcid.org/0000-0002-0081-400X
creator:
  affiliation: null
  email: null
  name: Tom Russell
  url: https://orcid.org/0000-0002-0081-400X
dataset_id: rdls_he-fro_nismod_sdkicra
description: Starter data kit collecting extracts from global, open datasets relating
  to climate hazards (coastal and river flooding, extreme heat and drought, tropical
  cyclone wind speeds) and infrastructure exposure systems (population, built-up area,
  roads, railways, power infrastructure) for Faroe Islands. Derived from global datasets
  clipped to national boundaries to support climate risk analysis and infrastructure
  resilience assessment.
details: This data starter kit addresses barriers to climate risk analysis by collecting
  and processing global, open datasets. Extracts are clipped to national scale using
  Natural Earth (2023) boundaries. The spatial intersection of hazard and exposure
  datasets provides a foundation for analyzing vulnerability and risk to infrastructure
  and people. Related tools include snkit for network data cleaning and nismod-snail
  for infrastructure exposure and risk calculations. Funded by the FCDO Climate Compatible
  Growth Programme.
exposure:
- asset_type:
    description: Population exposure classified using the GEM GED4ALL schema, sourced
      from GHS-POP (Global Human Settlement Population Grid).
    id: sei-pop
    scheme: GED4ALL
    title: Population taxonomy
    uri: https://wiki.openstreetmap.org/wiki/GED4ALL
  category: population
  id: exposure_population
  metrics:
  - dimension: population
    id: metric_population_count
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Built-up surface area classified using the GEM GED4ALL schema, sourced
      from GHS-BUILT-S (Global Human Settlement Built-up Surface Grid).
    id: bui
    scheme: GED4ALL
    title: Building taxonomy
    uri: https://wiki.openstreetmap.org/wiki/GED4ALL
  category: buildings
  id: exposure_built_area
  metrics:
  - dimension: structure
    id: metric_built_surface_area
    measurement:
      quantity_kind: area
      unit: null
- asset_type:
    description: Road network classified using the GEM GED4ALL schema, sourced from
      OpenStreetMap and processed with the open-gira model.
    id: trs-rod
    scheme: GED4ALL
    title: Infrastructure taxonomy
    uri: https://wiki.openstreetmap.org/wiki/GED4ALL
  category: infrastructure
  id: exposure_roads
  metrics:
  - dimension: structure
    id: metric_road_length
    measurement:
      quantity_kind: length
      unit: kilometre
- asset_type:
    description: Railway network classified using the GEM GED4ALL schema, sourced
      from OpenStreetMap and processed with the open-gira model.
    id: trs-rwy
    scheme: GED4ALL
    title: Infrastructure taxonomy
    uri: https://wiki.openstreetmap.org/wiki/GED4ALL
  category: infrastructure
  id: exposure_railways
  metrics:
  - dimension: structure
    id: metric_railway_length
    measurement:
      quantity_kind: length
      unit: kilometre
- asset_type:
    description: Power transmission network classified using the GEM GED4ALL schema,
      sourced from predicted high-voltage lines (Arderne et al. 2020 gridfinder model).
    id: pwr-lin
    scheme: GED4ALL
    title: Infrastructure taxonomy
    uri: https://wiki.openstreetmap.org/wiki/GED4ALL
  category: infrastructure
  id: exposure_power_transmission
  metrics:
  - dimension: structure
    id: metric_transmission_length
    measurement:
      quantity_kind: length
      unit: kilometre
- asset_type:
    description: Power distribution network classified using the GEM GED4ALL schema,
      sourced from predicted medium-voltage lines (Arderne et al. 2020 gridfinder
      model).
    id: pwr-lin
    scheme: GED4ALL
    title: Infrastructure taxonomy
    uri: https://wiki.openstreetmap.org/wiki/GED4ALL
  category: infrastructure
  id: exposure_power_distribution
  metrics:
  - dimension: structure
    id: metric_distribution_length
    measurement:
      quantity_kind: length
      unit: kilometre
- asset_type:
    description: Power generation facilities classified using the GEM GED4ALL schema,
      sourced from the Global Power Plant Database (WRI, 2021).
    id: pwr-plt
    scheme: GED4ALL
    title: Infrastructure taxonomy
    uri: https://wiki.openstreetmap.org/wiki/GED4ALL
  category: infrastructure
  id: exposure_power_plants
  metrics:
  - dimension: structure
    id: metric_plant_count
    measurement:
      quantity_kind: count
      unit: count
  - dimension: structure
    id: metric_installed_capacity_mw
    measurement:
      quantity_kind: power
      unit: megawatt
  - dimension: structure
    id: metric_annual_generation_gwh
    measurement:
      quantity_kind: energy
      unit: gigawatt_hour
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: simulated
    event_count: 3
    events:
    - calculation_method: simulated
      description: 'Historical baseline coastal flood inundation with subsidence for
        multiple return periods (2, 5, 10, 25, 50, 100, 250, 500, 1000 years) across
        four time periods (hist, 2030, 2050, 2080). Source: Aqueduct Floods (Ward
        et al. 2020).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_coastal_flood
        intensity_measure: wd:m
        process: coastal_flood
        trigger: null
        type: flood
      id: event_coastal_flood_historical
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P100Y
            end: '2080'
            start: '1980'
        probabilistic: null
    - calculation_method: simulated
      description: 'RCP4.5 climate scenario coastal flood inundation with subsidence
        for multiple return periods (2, 5, 10, 25, 50, 100, 250, 500, 1000 years)
        for future time periods (2030, 2050, 2080). Source: Aqueduct Floods.'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_coastal_flood
        intensity_measure: wd:m
        process: coastal_flood
        trigger: null
        type: flood
      id: event_coastal_flood_rcp45
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P50Y
            end: '2080'
            start: '2030'
        probabilistic: null
    - calculation_method: simulated
      description: 'RCP8.5 climate scenario coastal flood inundation with subsidence
        for multiple return periods (2, 5, 10, 25, 50, 100, 250, 500, 1000 years)
        for future time periods (2030, 2050, 2080). Source: Aqueduct Floods.'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_coastal_flood
        intensity_measure: wd:m
        process: coastal_flood
        trigger: null
        type: flood
      id: event_coastal_flood_rcp85
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P50Y
            end: '2080'
            start: '2030'
        probabilistic: null
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_coastal_flood
      intensity_measure: wd:m
      process: coastal_flood
      trigger: null
      type: flood
    id: event_set_coastal_flood
    occurrence_range: 2, 5, 10, 25, 50, 100, 250, 500, 1000 year return periods
    seasonality: null
  - analysis_type: empirical
    calculation_method: simulated
    event_count: 3
    events:
    - calculation_method: simulated
      description: 'Historical baseline (1980) riverine flood inundation for multiple
        return periods (2, 5, 10, 25, 50, 100, 250, 500, 1000 years) using WATCH forcing
        data. Source: Aqueduct Floods (Ward et al. 2020).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_river_flood
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_river_flood_historical
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: null
            end: '1980'
            start: '1980'
        probabilistic: null
    - calculation_method: simulated
      description: 'RCP4.5 climate scenario riverine flood inundation for multiple
        return periods (2, 5, 10, 25, 50, 100, 250, 500, 1000 years) across five GCMs
        (GFDL-ESM2M, HadGEM2-ES, IPSL-CM5A-LR, MIROC-ESM-CHEM, NorESM1-M) for future
        time periods (2030, 2050, 2080). Source: Aqueduct Floods.'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_river_flood
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_river_flood_rcp45
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P50Y
            end: '2080'
            start: '2030'
        probabilistic: null
    - calculation_method: simulated
      description: 'RCP8.5 climate scenario riverine flood inundation for multiple
        return periods (2, 5, 10, 25, 50, 100, 250, 500, 1000 years) across five GCMs
        (GFDL-ESM2M, HadGEM2-ES, IPSL-CM5A-LR, MIROC-ESM-CHEM, NorESM1-M) for future
        time periods (2030, 2050, 2080). Source: Aqueduct Floods.'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_river_flood
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_river_flood_rcp85
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P50Y
            end: '2080'
            start: '2030'
        probabilistic: null
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_river_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_river_flood
    occurrence_range: 2, 5, 10, 25, 50, 100, 250, 500, 1000 year return periods
    seasonality: null
  - analysis_type: empirical
    calculation_method: simulated
    event_count: 3
    events:
    - calculation_method: simulated
      description: 'Historical baseline (1861-2005) annual probability of extreme
        heat occurrence derived from ISIMIP climate projections across multiple climate
        models (GFDL-ESM2M, HadGEM2-ES, IPSL-CM5A-LR, MIROC5) and hydrological models.
        Source: Russell et al. 2023, derived from Lange et al. 2020.'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_extreme_heat
        intensity_measure: AirTemp:C
        process: extreme_heat
        trigger: null
        type: extreme_temperature
      id: event_extreme_heat_historical
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P144Y
            end: '2005'
            start: '1861'
        probabilistic: null
    - calculation_method: simulated
      description: 'RCP2.6 climate scenario annual probability of extreme heat occurrence
        (2006-2099) for future time periods (2030, 2050, 2080) across multiple climate
        and hydrological models. Source: Russell et al. 2023, derived from Lange et
        al. 2020.'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_extreme_heat
        intensity_measure: AirTemp:C
        process: extreme_heat
        trigger: null
        type: extreme_temperature
      id: event_extreme_heat_rcp26
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P93Y
            end: '2099'
            start: '2006'
        probabilistic: null
    - calculation_method: simulated
      description: 'RCP6.0 climate scenario annual probability of extreme heat occurrence
        (2006-2099) for future time periods (2030, 2050, 2080) across multiple climate
        and hydrological models. Source: Russell et al. 2023, derived from Lange et
        al. 2020.'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_extreme_heat
        intensity_measure: AirTemp:C
        process: extreme_heat
        trigger: null
        type: extreme_temperature
      id: event_extreme_heat_rcp60
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P93Y
            end: '2099'
            start: '2006'
        probabilistic: null
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_extreme_heat
      intensity_measure: AirTemp:C
      process: extreme_heat
      trigger: null
      type: extreme_temperature
    id: event_set_extreme_heat
    occurrence_range: Annual probability of occurrence
    seasonality: null
  - analysis_type: empirical
    calculation_method: simulated
    event_count: 3
    events:
    - calculation_method: simulated
      description: 'Historical baseline (1861-2005) annual probability of drought
        occurrence derived from ISIMIP climate projections across multiple climate
        models (GFDL-ESM2M, HadGEM2-ES, IPSL-CM5A-LR, MIROC5) and hydrological models.
        Source: Russell et al. 2023, derived from Lange et al. 2020.'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_drought
        intensity_measure: SPI:-
        process: meteorological_drought
        trigger: null
        type: drought
      id: event_drought_historical
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P144Y
            end: '2005'
            start: '1861'
        probabilistic: null
    - calculation_method: simulated
      description: 'RCP2.6 climate scenario annual probability of drought occurrence
        (2006-2099) for future time periods (2030, 2050, 2080) across multiple climate
        and hydrological models. Source: Russell et al. 2023, derived from Lange et
        al. 2020.'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_drought
        intensity_measure: SPI:-
        process: meteorological_drought
        trigger: null
        type: drought
      id: event_drought_rcp26
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P93Y
            end: '2099'
            start: '2006'
        probabilistic: null
    - calculation_method: simulated
      description: 'RCP6.0 climate scenario annual probability of drought occurrence
        (2006-2099) for future time periods (2030, 2050, 2080) across multiple climate
        and hydrological models. Source: Russell et al. 2023, derived from Lange et
        al. 2020.'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_drought
        intensity_measure: SPI:-
        process: meteorological_drought
        trigger: null
        type: drought
      id: event_drought_rcp60
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P93Y
            end: '2099'
            start: '2006'
        probabilistic: null
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: meteorological_drought
      trigger: null
      type: drought
    id: event_set_drought
    occurrence_range: Annual probability of occurrence
    seasonality: null
  - analysis_type: empirical
    calculation_method: simulated
    event_count: 2
    events:
    - calculation_method: simulated
      description: 'Historical tropical cyclone wind speed return periods (10, 20,
        30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000,
        2000, 3000, 4000, 5000, 10000 years) from STORM dataset. Source: Russell 2022,
        derived from Bloemendaal et al. 2020.'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_tropical_cyclone
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: event_tropical_cyclone_historical
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: null
            end: '2017'
            start: '1980'
        probabilistic: null
    - calculation_method: simulated
      description: 'Climate change tropical cyclone wind speed return periods (10,
        20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900,
        1000, 2000, 3000, 4000, 5000, 10000 years) across four high-resolution climate
        models (CMCC-CM2-VHR4, CNRM-CM6-1-HR, EC-Earth3P-HR, HadGEM3-GC31-HM). Source:
        Russell 2022, derived from Bloemendaal et al. 2022.'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_tropical_cyclone
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: event_tropical_cyclone_climate_change
      occurrence:
        deterministic: null
        empirical:
          return_period: null
          temporal:
            central_year: null
            duration: P35Y
            end: '2050'
            start: '2015'
        probabilistic: null
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_tropical_cyclone
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: event_set_tropical_cyclone
    occurrence_range: 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500,
      600, 700, 800, 900, 1000, 2000, 3000, 4000, 5000, 10000 year return periods
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: Global multi-hazard infrastructure risk and resilience analysis produced
    using the open-gira pipeline (University of Oxford / NISMOD). Country extents
    from Natural Earth Admin 0 units were used to clip and aggregate global datasets.
    Flood hazard from Aqueduct Floods inundation return-period layers; tropical cyclone
    wind speed from STORM synthetic track simulations; extreme heat and drought probability
    from bias-corrected ISIMIP2b climate model outputs. Hazard layers were intersected
    with national infrastructure networks (OpenStreetMap roads and railways, Global
    Power Plant Database, gridfinder predictive power transmission model) using nismod-snail
    (Spatial Networks Impact Assessment Library). Population and built-up area from
    GHS-POP and GHS-BUILT-S grids were spatially aggregated using snkit.
  sources:
  - id: source_aqueduct_floods
    license: CC-BY-4.0
    name: Aqueduct Floods
    risk_data_type: null
    type: dataset
    url: https://www.wri.org/publication/aqueduct-floods-methodology
    used_in: hazard
  - id: source_extreme_heat_drought
    license: CC-BY-4.0
    name: Annual probability of extreme heat and drought events
    risk_data_type: null
    type: dataset
    url: https://doi.org/10.5281/zenodo.8147088
    used_in: hazard
  - id: source_storm_cyclone
    license: CC-BY-4.0
    name: STORM tropical cyclone wind speed return periods
    risk_data_type: null
    type: dataset
    url: https://doi.org/10.4121/12705164.v3
    used_in: hazard
  - id: source_storm_cyclone_cc
    license: CC-BY-4.0
    name: STORM climate change tropical cyclone wind speed return periods
    risk_data_type: null
    type: dataset
    url: https://doi.org/10.4121/14510817.v3
    used_in: hazard
  - id: source_ghs_pop
    license: CC-BY-4.0
    name: GHS-POP - Global Human Settlement Population Grid
    risk_data_type: null
    type: dataset
    url: https://human-settlement.emergency.copernicus.eu/ghs_pop2023.php
    used_in: exposure
  - id: source_ghs_built
    license: CC-BY-4.0
    name: GHS-BUILT-S - Global Human Settlement Built-up Surface Grid
    risk_data_type: null
    type: dataset
    url: https://human-settlement.emergency.copernicus.eu/ghs_buS2023.php
    used_in: exposure
  - id: source_osm_networks
    license: ODbL-1.0/
    name: OpenStreetMap road and rail networks
    risk_data_type: null
    type: dataset
    url: https://global.infrastructureresilience.org
    used_in: exposure
  - id: source_power_plants
    license: CC-BY-4.0
    name: Global Power Plant Database
    risk_data_type: null
    type: dataset
    url: https://resourcewatch.org/data/explore/Global-Power-Plant-Database
    used_in: exposure
  - id: source_power_transmission
    license: CC-BY-4.0
    name: Predictive mapping of the global power system
    risk_data_type: null
    type: dataset
    url: https://doi.org/10.5281/zenodo.3628142
    used_in: exposure
  - id: source_natural_earth
    license: CC0-1.0
    name: Natural Earth Admin 0 Map Units
    risk_data_type: null
    type: dataset
    url: https://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-admin-0-details
    used_in: exposure
  - id: source_model_snkit
    license: https://opensource.org/licenses/MIT
    name: snkit - Spatial Networks Toolkit
    risk_data_type: null
    type: model
    url: https://github.com/nismod/snkit
    used_in: exposure
  - id: source_model_snail
    license: https://opensource.org/licenses/MIT
    name: nismod-snail - Spatial Networks Impact Assessment Library
    risk_data_type: null
    type: model
    url: https://github.com/nismod/snail
    used_in: vulnerability
  - id: source_model_open_gira
    license: https://opensource.org/licenses/MIT
    name: open-gira - Global Infrastructure Risk and Resilience Analysis
    risk_data_type: null
    type: model
    url: https://github.com/nismod/open-gira
    used_in: null
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project:
  name: Climate Compatible Growth (CCG)
  url: https://climatecompatiblegrowth.com/
publisher:
  affiliation: null
  email: info@zenodo.org
  name: Zenodo
  url: https://zenodo.org/records/16540003
purpose: To kickstart climate risk analysis and act as a starting point for infrastructure
  resilience assessment, vulnerability analysis, and scenario development, particularly
  for low and middle-income countries where access to data is a barrier.
referenced_by: []
resources:
- access_url: https://zenodo.org/records/16540003
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Single ZIP archive containing all hazard and exposure datasets for
    Faroe Islands, clipped from global sources. Contents: (1) Hazard - Coastal flood
    inundation maps (90 GeoTIFF, Aqueduct Floods, ~1km resolution, return periods
    2-1000yr, scenarios: historical/RCP4.5/RCP8.5, periods: 2030/2050/2080); Riverine
    flood inundation maps (279 GeoTIFF, Aqueduct Floods, ~1km, 5 GCMs, return periods
    2-1000yr); Extreme heat and drought probability maps (245 GeoTIFF + 1 CSV metadata,
    ISIMIP, ~55km, 4 GCMs, scenarios: historical/RCP2.6/RCP6.0); Tropical cyclone
    wind speed return period maps (136 GeoTIFF + 1 CSV metadata, STORM, ~10km, 4 climate
    models, return periods 10-10000yr). (2) Exposure - Population grid (2 GeoTIFF,
    GHS-POP 2020/2025, ~1km); Built-up surface grid (2 GeoTIFF, GHS-BUILT-S 2020/2025,
    ~1km); Road network (GeoPackage + OSM PBF, OpenStreetMap tertiary+); Railway network
    (GeoPackage + OSM PBF, OpenStreetMap); Power plants (GeoPackage, Global Power
    Plant Database 2018); Power transmission lines (GeoPackage, Gridfinder/predictive
    mapping); Power distribution lines (GeoPackage, Gridfinder). (3) Supporting files
    - National boundary (GeoJSON), analysis grid (GeoPackage), targets raster (GeoTIFF),
    datapackage descriptor (JSON), flood/heat/cyclone metadata (CSV). Data formats
    include GeoTIFF, GeoPackage, GeoJSON, CSV, JSON, and OSM PBF.'
  download_url: https://zenodo.org/records/16540003/files/FRO.zip
  format: null
  id: resource_sdkicra_fro
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Starter Data Kit for Infrastructure Climate Resilience Assessment - Faroe
    Islands
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-fro_nismod_sdkicra
spatial:
  bbox:
  - -7.64
  - 61.39
  - -6.28
  - 62.4
  centroid: null
  countries:
  - FRO
  gazetteer_entries:
  - description: Geonames
    id: gazetteer_1
    scheme: GEONAMES
    uri: https://www.geonames.org/2622320/faroe-islands.html
  scale: national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Infrastructure Climate Resilience Assessment Data Starter Kit for Faroe Islands
version: 0.1.0
vulnerability: null
---
