---
contact_point:
  email: logan.byers@wri.org
  id: attribution_contact
  name: World Resources Institute
  url: https://www.wri.org/research/global-database-power-plants
creator:
  email: logan.byers@wri.org
  id: attribution_creator
  name: World Resources Institute
  url: https://www.wri.org/research/global-database-power-plants
dataset_id: rdls_hzd-nismod_sdk_powerplantdb
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
- category: infrastructure
  dimension: structure
  quantity_kind: count, energy, power
  taxonomy: GED4ALL
extra_attributions:
- email: rajan@lanl.gov
  id: attribution_collaborator1
  name: Global Energy Observatory
  role: collaborator
  url: https://globalenergyobservatory.org
- email: info@kth.se
  id: attribution_collaborator2
  name: KTH Royal Institute of Technology
  role: collaborator
  url: https://www.kth.se
- email: communicatie@rug.nl
  id: attribution_collaborator3
  name: University of Groningen
  role: collaborator
  url: https://www.rug.nl
- email: geoforgood-info@google.com
  id: attribution_funder
  name: Google Earth Outreach
  role: funder
  url: https://earth.google.com/outreach
hazard: null
license: CC-BY-4.0
loss: null
project:
  name: Power Explorer
  url: https://www.wri.org/initiatives/power-explorer
publisher:
  email: logan.byers@wri.org
  id: attribution_publisher
  name: World Resources Institute
  url: https://www.wri.org/research/global-database-power-plants
purpose: To create a comprehensive, open-access power sector database that centralizes
  power plant data globally, making it easier to navigate, compare, and draw insights
  for analysis. The database facilitates collaborative analysis of the power sector
  and supports research on climate change, water stress, and air quality impacts.
resources:
- coordinate_system: EPSG:4326
  description: Comprehensive database file containing approximately 30,000 geolocated
    power plants from 164 countries. Includes thermal plants (coal, gas, oil, nuclear,
    biomass, waste, geothermal) and renewables (hydro, wind, solar). Each entry contains
    plant name, fuel type, capacity (MW), location (latitude/longitude), year of capacity,
    year of generation, data source, URL, annual generation (GWh), operational status,
    generator technology, owner, and commissioning year. Coverage represents 80.2%
    of global installed capacity.
  download_url: https://github.com/wri/global-power-plant-database
  format: CSV (csv)
  id: resource_1
  media_type: null
  spatial_resolution: null
  temporal:
    duration: null
    end: '2019'
    start: '1892'
    temporal_resolution: P3M
  title: Global Power Plant Database
risk_data_type:
- exposure
schema: rdl-03
slug: rdls_hzd-nismod_sdk_powerplantdb
spatial:
  countries:
  - GLO
  scale: global
title: Global Power Plant Database
version: 1.3.0
vulnerability: null
---
