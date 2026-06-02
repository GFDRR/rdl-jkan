---
catalog: Zenodo
contact_point:
  email: null
  id: attribution_contact
  name: Tom Russell
  url: https://orcid.org/0000-0002-0081-400X
creator:
  email: null
  id: attribution_creator1
  name: Tom Russell
  url: https://orcid.org/0000-0002-0081-400X
dataset_id: rdls_he-and_nismod_sdkicra
description: Starter data kit collecting extracts from global, open datasets relating
  to climate hazards (coastal and river flooding, extreme heat and drought, tropical
  cyclone wind speeds) and infrastructure exposure systems (population, built-up area,
  roads, railways, power infrastructure) for Andorra. Derived from global datasets
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
  category: buildings, infrastructure, population
  dimension: population, structure
  quantity_kind: area, count, energy, length, power
  taxonomy: null
extra_attributions:
- email: fcdo.correspondence@fcdo.gov.uk
  id: attribution_funder
  name: UK Foreign, Commonwealth and Development Office (FCDO)
  role: funder
  url: https://www.gov.uk/government/organisations/foreign-commonwealth-development-office
hazard:
  calculation_method: simulated
  disaster_identifiers: ''
  hazard_analysis_type: probabilistic
  hazard_type: coastal_flood, drought, extreme_temperature, flood, strong_wind
  intensity: wd:m
  occurrence_range: 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600,
    700, 800, 900, 1000, 2000, 3000, 4000, 5000, 10000 year return periods, 2, 5,
    10, 25, 50, 100, 250, 500, 1000 year return periods, Annual probability of occurrence
  processes: coastal_flood, extreme_heat, fluvial_flood, meteorological_drought, tropical_cyclone
  seasonality: ''
license: CC-BY-SA-4.0
loss: null
project:
  name: Climate Compatible Growth (CCG)
  url: https://climatecompatiblegrowth.com/
publisher:
  email: info@zenodo.org
  id: attribution_publisher
  name: Zenodo
  url: https://zenodo.org/records/16540009
purpose: To kickstart climate risk analysis and act as a starting point for infrastructure
  resilience assessment, vulnerability analysis, and scenario development, particularly
  for low and middle-income countries where access to data is a barrier.
resources:
- coordinate_system: EPSG:4326
  description: 'Single ZIP archive containing all hazard and exposure datasets for
    Andorra, clipped from global sources. Contents: (1) Hazard - Coastal flood inundation
    maps (90 GeoTIFF, Aqueduct Floods, ~1km resolution, return periods 2-1000yr, scenarios:
    historical/RCP4.5/RCP8.5, periods: 2030/2050/2080); Riverine flood inundation
    maps (279 GeoTIFF, Aqueduct Floods, ~1km, 5 GCMs, return periods 2-1000yr); Extreme
    heat and drought probability maps (245 GeoTIFF + 1 CSV metadata, ISIMIP, ~55km,
    4 GCMs, scenarios: historical/RCP2.6/RCP6.0); Tropical cyclone wind speed return
    period maps (136 GeoTIFF + 1 CSV metadata, STORM, ~10km, 4 climate models, return
    periods 10-10000yr). (2) Exposure - Population grid (2 GeoTIFF, GHS-POP 2020/2025,
    ~1km); Built-up surface grid (2 GeoTIFF, GHS-BUILT-S 2020/2025, ~1km); Road network
    (GeoPackage + OSM PBF, OpenStreetMap tertiary+); Railway network (GeoPackage +
    OSM PBF, OpenStreetMap); Power plants (GeoPackage, Global Power Plant Database
    2018); Power transmission lines (GeoPackage, Gridfinder/predictive mapping); Power
    distribution lines (GeoPackage, Gridfinder). (3) Supporting files - National boundary
    (GeoJSON), analysis grid (GeoPackage), targets raster (GeoTIFF), datapackage descriptor
    (JSON), flood/heat/cyclone metadata (CSV). Data formats include GeoTIFF, GeoPackage,
    GeoJSON, CSV, JSON, and OSM PBF.'
  download_url: https://zenodo.org/records/16540009/files/AND.zip
  format: JSON (json)
  id: resource_sdkicra_and
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Starter Data Kit for Infrastructure Climate Resilience Assessment - Andorra
risk_data_type:
- hazard
- exposure
schema: rdl-03
slug: rdls_he-and_nismod_sdkicra
spatial:
  bbox:
  - 1.41
  - 42.43
  - 1.77
  - 42.65
  countries:
  - AND
  gazetteer_entries:
  - description: Geonames
    id: gazetteer_1
    scheme: GEONAMES
    uri: https://www.geonames.org/3041565/andorra.html
  scale: national
title: Infrastructure Climate Resilience Assessment Data Starter Kit for Andorra
version: 0.2.1
vulnerability: null
---
