---
attributions:
- entity:
    affiliation: null
    email: rajan@lanl.gov
    name: Global Energy Observatory
    url: https://globalenergyobservatory.org
  id: attribution_collaborator1
  role: collaborator
- entity:
    affiliation: null
    email: info@kth.se
    name: KTH Royal Institute of Technology
    url: https://www.kth.se
  id: attribution_collaborator2
  role: collaborator
- entity:
    affiliation: null
    email: communicatie@rug.nl
    name: University of Groningen
    url: https://www.rug.nl
  id: attribution_collaborator3
  role: collaborator
- entity:
    affiliation: null
    email: geoforgood-info@google.com
    name: Google Earth Outreach
    url: https://earth.google.com/outreach
  id: attribution_funder
  role: funder
catalog: null
contact_point:
  affiliation: null
  email: logan.byers@wri.org
  name: World Resources Institute
  url: https://www.wri.org/research/global-database-power-plants
creator:
  affiliation: null
  email: logan.byers@wri.org
  name: World Resources Institute
  url: https://www.wri.org/research/global-database-power-plants
dataset_id: rdls_exp-nismod_powerplantdb
description: A comprehensive, open source database of power plants around the world.
  It centralizes power plant data to make it easier to navigate, compare and draw
  insights. The database covers approximately 30,000 power plants from 164 countries
  and includes thermal plants (coal, gas, oil, nuclear, biomass, waste, geothermal)
  and renewables (hydro, wind, solar). Each power plant is geolocated and entries
  contain information on plant capacity, generation, ownership, and fuel type.
details: The Global Power Plant Database leverages existing data sources and methodologies
  to build a comprehensive database covering all types of fuel, technical characteristics
  (fuel, technology, ownership), operational characteristics (generation), plant geolocation,
  and plants over 1 megawatt (MW). The database is built preferentially on data reported
  from trusted sources and uses more than 600 sources. The methodology involves matching
  plants across databases, automated and manual data collection, and geolocation verification
  through satellite imagery. The database is continuously updated as data becomes
  available.
exposure:
- asset_type:
    description: Global power generation facilities classified using the GEM GED4ALL
      schema, sourced from the Global Power Plant Database (WRI, 2021), covering approximately
      30,000 geolocated plants from 164 countries.
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
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Global Power Plant Database compiled by the World Resources Institute
    (WRI) by aggregating plant-level data from the Global Energy Observatory (GEO),
    Carbon Monitoring for Action (CARMA), Platts World Electric Power Plants Database
    (WEPP), IEA Statistics, over 600 national government sources, the Global Coal
    Plant Tracker, Enipedia, and a KTH Royal Institute of Technology crowdsourcing
    initiative. Records were harmonised to a common schema, duplicate facilities merged,
    and locations verified against satellite imagery where possible.
  sources:
  - id: source_1
    license: https://creativecommons.org/licenses/by/3.0/
    name: Global Energy Observatory (GEO)
    risk_data_type: null
    type: dataset
    url: http://globalenergyobservatory.org
    used_in: exposure
  - id: source_2
    license: null
    name: Carbon Monitoring for Action (CARMA)
    risk_data_type: null
    type: dataset
    url: http://carma.org
    used_in: exposure
  - id: source_3
    license: null
    name: Platts World Electric Power Plants Database (WEPP)
    risk_data_type: null
    type: dataset
    url: https://www.platts.com/products/world-electric-power-plants-database
    used_in: exposure
  - id: source_4
    license: null
    name: International Energy Agency (IEA) Statistics
    risk_data_type: null
    type: dataset
    url: https://www.iea.org/statistics/
    used_in: exposure
  - id: source_5
    license: null
    name: National Government Data Sources (600+ sources)
    risk_data_type: null
    type: dataset
    url: null
    used_in: exposure
  - id: source_6
    license: https://creativecommons.org/licenses/by/4.0/
    name: Global Coal Plant Tracker
    risk_data_type: null
    type: dataset
    url: globalenergymonitor.org/projects/global-coal-plant-tracker/
    used_in: exposure
  - id: source_7
    license: https://creativecommons.org/licenses/by/4.0/
    name: Enipedia
    risk_data_type: null
    type: dataset
    url: http://enipedia.tudelft.nl/wiki/Enipedia
    used_in: exposure
  - id: source_8
    license: null
    name: KTH Royal Institute of Technology Crowdsourcing
    risk_data_type: null
    type: dataset
    url: https://www.kth.se
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss:
  losses: []
project:
  name: Power Explorer
  url: https://www.wri.org/initiatives/power-explorer
publisher:
  affiliation: null
  email: logan.byers@wri.org
  name: World Resources Institute
  url: https://www.wri.org/research/global-database-power-plants
purpose: To create a comprehensive, open-access power sector database that centralizes
  power plant data globally, making it easier to navigate, compare, and draw insights
  for analysis. The database facilitates collaborative analysis of the power sector
  and supports research on climate change, water stress, and air quality impacts.
referenced_by:
- author_names:
  - Logan Byers
  - Johannes Friedrich
  - Roman Hennig
  - Aaron Kressig
  - Xinyue Li
  - Colin McCormick
  - Laura Malaguzzi Valeri
  date_published: '2021-03-01'
  doi: null
  id: reference_1
  name: A Global Database of Power Plants - Technical Note
  url: https://www.wri.org/publication/global-database-power-plants
resources:
- access_url: https://datasets.wri.org/dataset/globalpowerplantdatabase
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Comprehensive database file containing approximately 30,000 geolocated
    power plants from 164 countries. Includes thermal plants (coal, gas, oil, nuclear,
    biomass, waste, geothermal) and renewables (hydro, wind, solar). Each entry contains
    plant name, fuel type, capacity (MW), location (latitude/longitude), year of capacity,
    year of generation, data source, URL, annual generation (GWh), operational status,
    generator technology, owner, and commissioning year. Coverage represents 80.2%
    of global installed capacity.
  download_url: https://github.com/wri/global-power-plant-database
  format: null
  id: resource_1
  media_type: text/csv
  spatial: null
  spatial_aggregation: Individual power plant facility level
  spatial_resolution: null
  temporal:
    central_year: null
    duration: null
    end: '2019'
    start: '1892'
  temporal_resolution: P3M
  title: Global Power Plant Database
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-nismod_powerplantdb
spatial:
  bbox: null
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Global Power Plant Database
version: 1.3.0
vulnerability: null
---
