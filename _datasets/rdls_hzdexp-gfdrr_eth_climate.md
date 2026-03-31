---
catalog: World Bank Data Catalog
contact_point:
  email: pchrzanowski@worldbank.org
  id: attribution_contact
  name: Pierre Chrzanowski
  url: https://www.gfdrr.org/en
creator:
  email: frivas@gmv.com
  id: attribution_creator
  name: GMV Innovating Solutions S.L.
  url: https://www.gmv.com/en-es
dataset_id: rdls_hzd.exp-gfdrr_eth_climate
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
  category: buildings, population
  dimension: index, population, structure
  quantity_kind: area, count, dimensionless, ratio
  taxonomy: GED4ALL
extra_attributions:
- email: admin@geosas.net
  id: attribution_collaborator
  name: GeoSAS
  role: collaborator
  url: https://www.geosas.net/
hazard:
  calculation_method: simulated
  disaster_identifiers: ''
  hazard_analysis_type: probabilistic
  hazard_type: drought, earthquake, extreme_temperature, flood, landslide, volcanic
  intensity: ash_thickness:cm
  occurrence_range: ''
  processes: ashfall, extreme_heat, ground_motion, landslide_general, meteorological_drought,
    pluvial_flood
  seasonality: ''
license: CC-BY-4.0
loss: null
project:
  name: Ethiopia - Strengthening the Understanding of Urban Disaster Risk in Secondary
    Cities
  url: https://www.worldbank.org
publisher:
  email: data@gfdrr.org
  id: attribution_publisher
  name: Global Facility for Disaster Reduction and Recovery (GFDRR)
  url: https://www.gfdrr.org/en
purpose: To identify and map disaster risk at the city level using remote sensing
  and earth observation methods in combination with the best available geodata for
  climatic and non-climatic hazards and disaster exposure.
resources:
- coordinate_system: EPSG:4326
  description: City-level indicators dataset (59 variables) covering built-up surface,
    population exposure, hazard levels (flood return periods, landslides, heat stress,
    drought, earthquakes, volcanic hazards), urban growth metrics, and composite exposure
    indices for Ethiopian cities.
  download_url: https://datacatalog.worldbank.org/search/dataset/0066935/Climate-and-Disaster-Risk-Database-at-the-City-Level-for-Ethiopia
  format: Excel (xlsx)
  id: resource_1
  media_type: null
  spatial_resolution: null
  temporal: null
  title: City-Level Hazard Exposure and Urban Growth Indicators for Ethiopia
- coordinate_system: EPSG:4326
  description: 'Drought hazard GeoTIFFs from CLARISSE for periods: 2000-2004, 2005-2009,
    2010-2014, 2015-2019, 2020-2024, and projection 2025-2029. Typical IDs: CLARISSE_DroughtHazard_Ethiopia_<period>_<yyyymmdd>.'
  download_url: https://datacatalog.worldbank.org/search/dataset/0066935/Climate-and-Disaster-Risk-Database-at-the-City-Level-for-Ethiopia
  format: GeoTIFF (tif)
  id: resource_2
  media_type: null
  spatial_resolution: 27500
  temporal: null
  title: Drought Hazard Maps for Ethiopia (Time-Sliced Series)
- coordinate_system: EPSG:4326
  description: 'Earthquake hazard GeoTIFFs for periods: 2000-2004, 2005-2009, 2010-2014,
    2015-2019, 2020-2024, and projection 2025-2029. Typical IDs: CLARISSE_EarthquakeHazard_Ethiopia_<period>_<yyyymmdd>.'
  download_url: https://datacatalog.worldbank.org/search/dataset/0066935/Climate-and-Disaster-Risk-Database-at-the-City-Level-for-Ethiopia
  format: GeoTIFF (tif)
  id: resource_3
  media_type: null
  spatial_resolution: 5600
  temporal: null
  title: Earthquake Hazard Maps for Ethiopia (Time-Sliced Series)
- coordinate_system: EPSG:4326
  description: 'Heat stress hazard GeoTIFFs for periods: 2000-2004, 2005-2009, 2010-2014,
    2015-2019, 2020-2024, and projection 2025-2029. Typical IDs: CLARISSE_HeatStressHazard_Ethiopia_<period>_<yyyymmdd>.'
  download_url: https://datacatalog.worldbank.org/search/dataset/0066935/Climate-and-Disaster-Risk-Database-at-the-City-Level-for-Ethiopia
  format: GeoTIFF (tif)
  id: resource_4
  media_type: null
  spatial_resolution: 27500
  temporal: null
  title: Heat Stress Hazard Maps for Ethiopia (Time-Sliced Series)
- coordinate_system: EPSG:4326
  description: 'Landslides hazard GeoTIFFs for periods: 2000-2004, 2005-2009, 2010-2014,
    2015-2019, 2020-2024, and projection 2025-2029. Typical IDs: CLARISSE_LandslidesHazard_Ethiopia_<period>_<yyyymmdd>.'
  download_url: https://datacatalog.worldbank.org/search/dataset/0066935/Climate-and-Disaster-Risk-Database-at-the-City-Level-for-Ethiopia
  format: GeoTIFF (tif)
  id: resource_5
  media_type: null
  spatial_resolution: 1000
  temporal: null
  title: Landslides Hazard Maps for Ethiopia (Time-Sliced Series)
- coordinate_system: EPSG:4326
  description: 'Volcanic hazard GeoTIFFs for periods: 2000-2004, 2005-2009, 2010-2014,
    2015-2019, 2020-2024, and projection 2025-2029. Typical IDs: CLARISSE_VolcanicHazard_Ethiopia_<period>_<yyyymmdd>.'
  download_url: https://datacatalog.worldbank.org/search/dataset/0066935/Climate-and-Disaster-Risk-Database-at-the-City-Level-for-Ethiopia
  format: GeoTIFF (tif)
  id: resource_6
  media_type: null
  spatial_resolution: 4600
  temporal: null
  title: Volcanic Hazard Maps for Ethiopia (Time-Sliced Series)
- coordinate_system: EPSG:4326
  description: 'Flood hazard GeoTIFFs (5-year return period) for periods: 2000-2004,
    2005-2009, 2010-2014, 2015-2019, 2020-2024, and projection 2025-2029. Typical
    IDs: CLARISSE_FloodHazard-5RP_Ethiopia_<period>_<yyyymmdd>.'
  download_url: https://datacatalog.worldbank.org/search/dataset/0066935/Climate-and-Disaster-Risk-Database-at-the-City-Level-for-Ethiopia
  format: GeoTIFF (tif)
  id: resource_7
  media_type: null
  spatial_resolution: 30
  temporal: null
  title: Flood Hazard Maps (5-Year Return Period) for Ethiopia (Time-Sliced Series)
- coordinate_system: EPSG:4326
  description: 'Flood hazard GeoTIFFs (20-year return period) for periods: 2000-2004,
    2005-2009, 2010-2014, 2015-2019, 2020-2024, and projection 2025-2029. Typical
    IDs: CLARISSE_FloodHazard-20RP_Ethiopia_<period>_<yyyymmdd>.'
  download_url: https://datacatalog.worldbank.org/search/dataset/0066935/Climate-and-Disaster-Risk-Database-at-the-City-Level-for-Ethiopia
  format: GeoTIFF (tif)
  id: resource_8
  media_type: null
  spatial_resolution: 30
  temporal: null
  title: Flood Hazard Maps (20-Year Return Period) for Ethiopia (Time-Sliced Series)
- coordinate_system: EPSG:4326
  description: 'Flood hazard GeoTIFFs (100-year return period) for periods: 2000-2004,
    2005-2009, 2010-2014, 2015-2019, 2020-2024, and projection 2025-2029. Typical
    IDs: CLARISSE_FloodHazard-100RP_Ethiopia_<period>_<yyyymmdd>.'
  download_url: https://datacatalog.worldbank.org/search/dataset/0066935/Climate-and-Disaster-Risk-Database-at-the-City-Level-for-Ethiopia
  format: GeoTIFF (tif)
  id: resource_9
  media_type: null
  spatial_resolution: 30
  temporal: null
  title: Flood Hazard Maps (100-Year Return Period) for Ethiopia (Time-Sliced Series)
- coordinate_system: EPSG:4326
  description: 'Built-up surface GeoTIFFs for periods: 2000-2004, 2005-2009, 2010-2014,
    2015-2019, 2020-2024, and projection 2025-2029. Typical IDs: CLARISSE_BuiltUpSurface_Ethiopia_<period>_<yyyymmdd>.'
  download_url: https://datacatalog.worldbank.org/search/dataset/0066935/Climate-and-Disaster-Risk-Database-at-the-City-Level-for-Ethiopia
  format: GeoTIFF (tif)
  id: resource_10
  media_type: null
  spatial_resolution: 100
  temporal: null
  title: Built-up Surface Maps for Ethiopia (Time-Sliced Series)
- coordinate_system: EPSG:4326
  description: 'Population distribution GeoTIFFs for periods: 2000-2004, 2005-2009,
    2010-2014, 2015-2019, 2020-2024, and projection 2025-2029. Typical IDs: CLARISSE_Population_Ethiopia_<period>_<yyyymmdd>.'
  download_url: https://datacatalog.worldbank.org/search/dataset/0066935/Climate-and-Disaster-Risk-Database-at-the-City-Level-for-Ethiopia
  format: GeoTIFF (tif)
  id: resource_11
  media_type: null
  spatial_resolution: 100
  temporal: null
  title: Population Distribution Maps for Ethiopia (Time-Sliced Series)
- coordinate_system: EPSG:4326
  description: 'City-level multi-hazard exposure GeoPackage outputs for periods: 2000-2004,
    2005-2009, 2010-2014, 2015-2019, 2020-2024, and projection 2025-2029. Typical
    IDs: CLARISSE_Cities_Exposure_Ethiopia_<period>_<yyyymmdd>.'
  download_url: https://datacatalog.worldbank.org/search/dataset/0066935/Climate-and-Disaster-Risk-Database-at-the-City-Level-for-Ethiopia
  format: GeoPackage (gpkg)
  id: resource_12
  media_type: null
  spatial_resolution: null
  temporal: null
  title: City-Level Multi-Hazard Exposure (GPKG) for Ethiopia (Time-Sliced Series)
- coordinate_system: EPSG:4326
  description: 'DEM GeoTIFF for Ethiopia (2023). Typical ID: CLARISSE_DEM_Ethiopia_2023_<yyyymmdd>.'
  download_url: https://datacatalog.worldbank.org/search/dataset/0066935/Climate-and-Disaster-Risk-Database-at-the-City-Level-for-Ethiopia
  format: GeoTIFF (tif)
  id: resource_13
  media_type: null
  spatial_resolution: 30
  temporal: null
  title: Digital Elevation Model for Ethiopia (2023)
- coordinate_system: EPSG:4326
  description: 'Annual precipitation GeoTIFFs including single-period layers (e.g.,
    2000-2004, 2005-2009, 2010-2014, 2015-2019, 2020-2024) and an aggregated layer
    (2000-2024). Typical IDs: CLARISSE_YearlyPrecipitation_Ethiopia_<period>_<yyyymmdd>.'
  download_url: https://datacatalog.worldbank.org/search/dataset/0066935/Climate-and-Disaster-Risk-Database-at-the-City-Level-for-Ethiopia
  format: GeoTIFF (tif)
  id: resource_14
  media_type: null
  spatial_resolution: 5600
  temporal: null
  title: Annual Precipitation for Ethiopia (GeoTIFF Series)
risk_data_type:
- hazard
schema: rdl-03
slug: rdls_hzd.exp-gfdrr_eth_climate
spatial:
  countries:
  - ETH
  scale: sub-national
title: Climate and Disaster Risk Database at the City-Level for Ethiopia
version: '1'
vulnerability: null
---
