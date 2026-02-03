---
contact_point:
  email: silvia.colombo@ouce.ox.ac.uk
  id: attribution_contact
  name: Silvia Colombo
  url: https://www.eci.ox.ac.uk/
creator:
  email: silvia.colombo@ouce.ox.ac.uk
  id: attribution_creator
  name: Silvia Colombo
  url: https://www.eci.ox.ac.uk/
dataset_id: rdls_exp-nismod_sdk_transport
description: 'The first comprehensive geolocated multi-modal transport database for
  the whole continent of Africa (AfTS-Db), including road, rail, aviation, maritime
  and inland waterway networks. The database contains standardized asset and network
  data across all transport modes, including inter-modal connections, attributes of
  road and rail corridors and estimated annual statistics for airports and ports.
  The database includes: 234 airports with airline routes, 179 maritime ports with
  inter-port connections, 132 inland ports and docking sites with river and lake connections,
  6,057 railway stations connected across 99,373 kilometers of rail lines, and 1,004,512
  kilometers of roads (motorways, trunk roads, primary and secondary routes, and connecting
  local roads). All datasets follow a standardized network specification with nodes
  and edges for each transport mode.'
details: The database is provided in Geopackage (gpkg) format for each transport mode,
  containing nodes (point features) and edges (line features) with associated attributes.
  Key data sources include OpenStreetMap for roads and railways, World Bank Global
  Airports database, PortWatch, Verschuur et al. (2023) for maritime data, and various
  AfDB reports and development corridor studies. The temporal coverage spans 2019-2025,
  with railway status classifications including operational, planned, proposed, under
  construction, and rehabilitation projects. Position accuracy of airports and ports
  has been validated to 100% using satellite imagery, while the railway network has
  been validated against CIA Factbook and World Population Review showing total length
  differences of -6% and 1% respectively, and the road network has been validated
  against the HeiGIT dataset. The database includes estimated construction, upgrading,
  and operation/maintenance costs for roads and railways through 2050, and identifies
  7 types of inter-modal connections (airport-railway, airport-road, inland waterway-railway,
  inland waterway-road, maritime port-railway, maritime port-road, and railway-road).
  All processing code is available on GitHub under MIT license, and the database is
  designed to be regularly updatable as source datasets such as OSM, PortWatch, and
  OurAirports are refreshed.
exposure:
- category: infrastructure
  dimension: product, structure
  quantity_kind: count, length, monetary, time, weight
  taxonomy: GED4ALL
extra_attributions: []
hazard: null
license: CC-BY-4.0
loss: null
project:
  name: Climate Compatible Growth (CCG)
  url: https://climatecompatiblegrowth.com/
publisher:
  email: info@zenodo.org
  id: attribution_publisher
  name: Zenodo
  url: https://zenodo.org/records/17593244
purpose: The AfTS-Db provides key information for transport planning, resilience assessments,
  asset management, and development of transport models and applications. The database
  is designed to support data-driven policy formulation, infrastructure development,
  and enhancement of trade and mobility across the African continent. It facilitates
  analysis of African value chains, strategic planning and decision-making, and supports
  applications ranging from economic analysis to environmental and climate risk and
  resilience impact assessments. The database addresses the critical need for open-access,
  standardized geospatial data on existing and planned transport networks to adequately
  assess and mitigate development impacts across Africa.
resources:
- coordinate_system: EPSG:4326
  description: Geopackage file containing 234 airports across Africa with network
    topology (nodes and edges). Includes airport locations, airline routes between
    airports, and annual seat capacity data (2019) as a proxy for passenger volumes.
    Contains flight connection routes represented as straight-line segments between
    airport pairs.
  download_url: https://zenodo.org/records/17593244/files/africa_airport_network.gpkg
  format: GeoPackage (gpkg)
  id: resource_airport_network
  media_type: null
  spatial_resolution: null
  temporal:
    duration: null
    end: null
    start: null
    temporal_resolution: Annual
  title: Africa Airport Network
- coordinate_system: EPSG:4326
  description: Reference geopackage file containing airport location data from OurAirports
    database used for positional accuracy validation and coordinate correction of
    the World Bank Global Airports database. Provides high-accuracy airport terminal
    locations.
  download_url: https://zenodo.org/records/17593244/files/africa_airport_ourairport.gpkg
  format: GeoPackage (gpkg)
  id: resource_airport_ourairport
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Africa Airport OurAirport Reference Data
- coordinate_system: null
  description: CSV file containing estimated construction, upgrading, operation and
    maintenance costs for 41 major road corridors across Africa. Includes minimum,
    median, and maximum cost estimates per kilometer per lane based on road type and
    condition (paved/unpaved), with projections through 2050.
  download_url: https://zenodo.org/records/17593244/files/africa_corridors_costs.csv
  format: CSV (csv)
  id: resource_corridors_costs
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Africa Road Corridors Investment Costs
- coordinate_system: EPSG:4326
  description: Geopackage file containing inland waterway network including 60 inland
    ports and 132 total docking points (ports, piers, docks, landing sites, yacht
    clubs) with navigable routes. Covers Lakes Victoria, Tanganyika, Malawi, Kivu
    and waterways along the Congo and Nile river systems. Includes network topology
    with nodes (ports/docking points) and edges (navigable routes).
  download_url: https://zenodo.org/records/17593244/files/africa_iww_network.gpkg
  format: GeoPackage (gpkg)
  id: resource_iww_network
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Africa Inland Waterways Network
- coordinate_system: EPSG:4326
  description: Geopackage file containing maritime port network with 179 ports and
    shipping routes between African ports. Includes port-to-port navigable routes,
    port usage statistics (2019-2024) from AIS data including annual vessel counts
    by cargo type (container, dry bulk, tankers, RoRo, general), cargo weights, vessel
    dwell times, and proportion of country exports/imports handled at each port.
  download_url: https://zenodo.org/records/17593244/files/africa_maritime_network.gpkg
  format: GeoPackage (gpkg)
  id: resource_maritime_network
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Africa Maritime Network
- coordinate_system: EPSG:4326
  description: 'Geopackage file containing multimodal connections between different
    transport modes. Includes 7 types of inter-modal connections: airport-railway,
    airport-road, inland waterway-railway, inland waterway-road, maritime port-railway,
    maritime port-road, and railway-road. Each connection represented as directional
    edges linking nodes across transport networks.'
  download_url: https://zenodo.org/records/17593244/files/africa_multimodal.gpkg
  format: GeoPackage (gpkg)
  id: resource_multimodal
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Africa Multimodal Network
- coordinate_system: null
  description: CSV file containing estimated construction, upgrading, operation and
    maintenance costs for railway lines across Africa. Includes minimum, median, and
    maximum cost estimates per kilometer based on railway status (planned, proposed,
    rehabilitation), with projections through 2050.
  download_url: https://zenodo.org/records/17593244/files/africa_rails_costs.csv
  format: CSV (csv)
  id: resource_rails_costs
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Africa Railways Investment Costs
- coordinate_system: EPSG:4326
  description: Geopackage file containing comprehensive railway network with 6,057
    railway stations connected across 99,373 kilometers of rail lines. Includes 986
    named railway corridors with attributes for operational status (abandoned, under
    construction, disused, open, planned, proposed, razed, under rehabilitation, suspended),
    gauge widths, line names, and facility types (mines, ports, freight terminals,
    manufacturing, etc.). Network topology includes nodes (stations/junctions) and
    edges (rail line segments).
  download_url: https://zenodo.org/records/17593244/files/africa_railways_network.gpkg
  format: GeoPackage (gpkg)
  id: resource_railways_network
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Africa Railways Network
- coordinate_system: EPSG:4326
  description: Geopackage file containing comprehensive road network with 1,004,512
    kilometers of roads including motorways, trunk roads, primary and secondary routes,
    and connecting local roads. Includes 41 named major road corridors across Africa
    with attributes for highway classification, surface type (paved/unpaved), number
    of lanes, bridge indicators, and speed limits. Network topology includes nodes
    (junctions/endpoints) and edges (road segments).
  download_url: https://zenodo.org/records/17593244/files/africa_roads_network.gpkg
  format: GeoPackage (gpkg)
  id: resource_roads_network
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Africa Roads Network
- coordinate_system: null
  description: Excel spreadsheet containing comprehensive metadata documentation for
    the African Transport Systems Database. Describes each dataset component, column
    names, attributes, data sources, processing methods, and quality assessments.
    Provides detailed explanation of the database structure and content.
  download_url: https://zenodo.org/records/17593244/files/METADATA.xlsx
  format: Excel (xlsx)
  id: resource_metadata
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Africa Transport Database Metadata
risk_data_type:
- exposure
schema: rdl-03
slug: rdls_exp-nismod_sdk_transport
spatial:
  countries:
  - DZA
  - AGO
  - BEN
  - BWA
  - BFA
  - BDI
  - CPV
  - CMR
  - CAF
  - TCD
  - COM
  - COG
  - COD
  - CIV
  - DJI
  - EGY
  - GNQ
  - ERI
  - SWZ
  - ETH
  - GAB
  - GMB
  - GHA
  - GIN
  - GNB
  - KEN
  - LSO
  - LBR
  - LBY
  - MDG
  - MWI
  - MLI
  - MRT
  - MUS
  - MAR
  - MOZ
  - NAM
  - NER
  - NGA
  - RWA
  - STP
  - SEN
  - SYC
  - SLE
  - SOM
  - ZAF
  - SSD
  - SDN
  - TZA
  - TGO
  - TUN
  - UGA
  - ZMB
  - ZWE
  scale: regional
title: 'The African Transport Systems Database: an open geospatial database of multi-modal
  connected networks'
version: '2'
vulnerability: null
---
