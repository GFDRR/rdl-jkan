---
attributions:
- entity:
    affiliation: null
    email: null
    name: Raghav Pant
    url: https://orcid.org/0000-0003-4648-5261
  id: attribution_creator2
  role: creator
- entity:
    affiliation: null
    email: null
    name: Fred Thomas
    url: https://orcid.org/0000-0002-8441-5638
  id: attribution_creator3
  role: creator
- entity:
    affiliation: null
    email: null
    name: Tom Russell
    url: https://orcid.org/0000-0002-0081-400X
  id: attribution_creator4
  role: creator
- entity:
    affiliation: null
    email: null
    name: Jim W. Hall
    url: https://orcid.org/0000-0002-2024-9191
  id: attribution_creator5
  role: creator
- entity:
    affiliation: null
    email: null
    name: Marcus Young
    url: https://orcid.org/0000-0003-4627-1116
  id: attribution_creator6
  role: creator
- entity:
    affiliation: null
    email: null
    name: Jasper Verschuur
    url: https://orcid.org/0000-0002-5277-4353
  id: attribution_creator7
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
  name: Silvia Colombo
  url: https://orcid.org/0009-0000-8652-702X
creator:
  affiliation: null
  email: null
  name: Silvia Colombo
  url: https://orcid.org/0009-0000-8652-702X
dataset_id: rdls_exp-nismod_aftsdb
description: We present the first comprehensive geolocated multi-modal transport database
  for the whole continent of Africa, the African Transport Systems Database (AfTS-Db),
  including road, rail, aviation, maritime and inland waterway networks. To do so,
  we created and standardized asset and network data across all transport modes, including
  inter-modal connections, attributes of road and rail corridors and estimated annual
  statistics for airports and ports. The African Transport Systems Database includes
  234 airports including their airline routes, 179 maritime ports and their connections
  with each other, 132 inland ports and docking sites with river and lake connections,  4,412
  railway stations connected across 99,373 kilometers of rail lines, and 1,004,512
  kilometers of roads mainly comprised of all motorways, trunk roads, primary and
  secondary routes across Africa and some local roads that connect to other transport
  modes. The AfTS-Db provides key information for transport planning, resilience assessments,
  asset management and development of transport models and applications. Furthermore,
  we expect the data will also be of relevance for environmental, health, social and
  economic studies.
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
- asset_type:
    description: African multi-modal transport infrastructure (airports, roads, railways,
      inland waterways, maritime ports) classified using the GEM GED4ALL schema, sourced
      from OpenStreetMap, World Bank, and other open datasets.
    id: multimodal_transport_network
    scheme: GED4ALL
    title: Infrastructure taxonomy
    uri: https://wiki.openstreetmap.org/wiki/GED4ALL
  category: infrastructure
  id: exposure_aftsdb
  metrics:
  - dimension: structure
    id: metric_airport_nodes
    measurement:
      quantity_kind: count
      unit: count
  - dimension: structure
    id: metric_airport_routes
    measurement:
      quantity_kind: count
      unit: count
  - dimension: product
    id: metric_airport_total_seats
    measurement:
      quantity_kind: count
      unit: count
  - dimension: structure
    id: metric_airport_reference_nodes
    measurement:
      quantity_kind: count
      unit: count
  - dimension: product
    id: metric_road_corridor_costs
    measurement:
      quantity_kind: currency
      unit: USD
  - dimension: structure
    id: metric_iww_nodes
    measurement:
      quantity_kind: count
      unit: count
  - dimension: structure
    id: metric_iww_edges
    measurement:
      quantity_kind: count
      unit: count
  - dimension: structure
    id: metric_iww_length
    measurement:
      quantity_kind: length
      unit: null
  - dimension: structure
    id: metric_maritime_nodes
    measurement:
      quantity_kind: count
      unit: count
  - dimension: structure
    id: metric_maritime_edges
    measurement:
      quantity_kind: count
      unit: count
  - dimension: structure
    id: metric_maritime_length
    measurement:
      quantity_kind: length
      unit: null
  - dimension: product
    id: metric_maritime_vessel_count
    measurement:
      quantity_kind: count
      unit: count
  - dimension: product
    id: metric_maritime_capacity_tons
    measurement:
      quantity_kind: mass
      unit: null
  - dimension: product
    id: metric_maritime_turnaround_time
    measurement:
      quantity_kind: time
      unit: null
  - dimension: structure
    id: metric_multimodal_connections
    measurement:
      quantity_kind: count
      unit: count
  - dimension: structure
    id: metric_multimodal_length
    measurement:
      quantity_kind: length
      unit: null
  - dimension: product
    id: metric_railway_costs
    measurement:
      quantity_kind: currency
      unit: USD
  - dimension: structure
    id: metric_rail_nodes
    measurement:
      quantity_kind: count
      unit: count
  - dimension: structure
    id: metric_rail_edges
    measurement:
      quantity_kind: count
      unit: count
  - dimension: structure
    id: metric_rail_length
    measurement:
      quantity_kind: length
      unit: kilometre
  - dimension: structure
    id: metric_road_nodes
    measurement:
      quantity_kind: count
      unit: count
  - dimension: structure
    id: metric_road_edges
    measurement:
      quantity_kind: count
      unit: count
  - dimension: structure
    id: metric_road_length
    measurement:
      quantity_kind: length
      unit: kilometre
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Africa Transport System Database (AFTSDB) compiled by integrating transport
    network data from multiple continental and national sources. OpenStreetMap road
    and rail networks were combined with georeferenced airport, port, and inland waterway
    data from global registries (OurAirports, Global Maritime Network, PortWatch,
    USGS Africa Infrastructure Database). Network gaps were filled using regional
    transport studies and development corridor reports from the African Union (AU-PIDA),
    African Development Bank, and the Nile Basin Initiative. Network topology was
    standardised and processed using the open-gira and snkit toolkits.
  sources:
  - id: source_osm
    license: https://opendatacommons.org/licenses/odbl/1-0/
    name: OpenStreetMap
    risk_data_type: null
    type: dataset
    url: https://www.openstreetmap.org/
    used_in: exposure
  - id: source_wb_airports
    license: https://creativecommons.org/licenses/by/4.0/
    name: World Bank Global Airports Database
    risk_data_type: null
    type: dataset
    url: https://datacatalog.worldbank.org/search/dataset/0038117/Global-Airports
    used_in: exposure
  - id: source_ourairports
    license: https://creativecommons.org/publicdomain/zero/1.0/
    name: OurAirports
    risk_data_type: null
    type: dataset
    url: https://ourairports.com/
    used_in: exposure
  - id: source_verschuur
    license: https://creativecommons.org/licenses/by/4.0/
    name: Global Maritime Network
    risk_data_type: null
    type: dataset
    url: https://doi.org/10.1038/s43247-022-00656-7
    used_in: exposure
  - id: source_portwatch
    license: https://creativecommons.org/licenses/by/4.0/
    name: PortWatch
    risk_data_type: null
    type: dataset
    url: https://portwatch.imf.org/
    used_in: exposure
  - id: source_usgs
    license: https://creativecommons.org/publicdomain/zero/1.0/
    name: USGS Africa Infrastructure Database
    risk_data_type: null
    type: dataset
    url: https://doi.org/10.5066/P97EQWXP
    used_in: exposure
  - id: source_thorn
    license: https://creativecommons.org/licenses/by/4.0/
    name: African Development Corridors Database
    risk_data_type: null
    type: dataset
    url: https://doi.org/10.1038/s41597-022-01771-y
    used_in: exposure
  - id: source_afdb_corridors
    license: null
    name: African Development Bank Cross-border Road Corridors Reports (2019, 2023)
    risk_data_type: null
    type: dataset
    url: https://www.afdb.org/
    used_in: exposure
  - id: source_aupida
    license: null
    name: AU-PIDA (African Union Programme for Infrastructure Development in Africa)
    risk_data_type: null
    type: dataset
    url: https://www.au-pida.org/pida-projects/
    used_in: exposure
  - id: source_tttfp
    license: null
    name: Tripartite Transport and Transit Facilitation Programme (TTTFP)
    risk_data_type: null
    type: dataset
    url: https://tttfp.org/corridors/all-corridors/
    used_in: exposure
  - id: source_nbi
    license: null
    name: Nile Basin Initiative (NBI) River Navigation Study
    risk_data_type: null
    type: dataset
    url: https://nilebasin.org/
    used_in: exposure
  - id: source_hydrorivers
    license: https://creativecommons.org/licenses/by/4.0/
    name: HydroRIVERS
    risk_data_type: null
    type: dataset
    url: https://www.hydrosheds.org/products/hydrorivers
    used_in: exposure
  - id: source_country_studies
    license: null
    name: Country-Specific Transport Infrastructure Studies
    risk_data_type: null
    type: dataset
    url: null
    used_in: exposure
  - id: source_cpcs_rail
    license: null
    name: CPCS East African Railways Master Plan Study (2009)
    risk_data_type: null
    type: dataset
    url: null
    used_in: exposure
  - id: source_trg_rail
    license: null
    name: Africa Rail Network Repository (TRG-Rail)
    risk_data_type: null
    type: dataset
    url: https://github.com/trg-rail/africa_rail_network
    used_in: exposure
  - id: source_aiddata
    license: https://creativecommons.org/licenses/by/4.0/
    name: AidData Chinese Development Finance
    risk_data_type: null
    type: dataset
    url: https://doi.org/10.1038/s41597-024-03341-w
    used_in: exposure
  - id: source_opengira
    license: https://opensource.org/licenses/MIT
    name: Open-GIRA
    risk_data_type: null
    type: model
    url: https://github.com/nismod/open-gira
    used_in: exposure
  - id: source_snkit
    license: https://opensource.org/licenses/MIT
    name: snkit
    risk_data_type: null
    type: model
    url: https://github.com/tomalrussell/snkit
    used_in: exposure
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
  url: https://zenodo.org
purpose: The AfTS-Db provides key information for transport planning, resilience assessments,
  asset management, and development of transport models and applications. The database
  is designed to support data-driven policy formulation, infrastructure development,
  and enhancement of trade and mobility across the African continent. It facilitates
  analysis of African value chains, strategic planning and decision-making, and supports
  applications ranging from economic analysis to environmental and climate risk and
  resilience impact assessments. The database addresses the critical need for open-access,
  standardized geospatial data on existing and planned transport networks to adequately
  assess and mitigate development impacts across Africa.
referenced_by:
- author_names:
  - Silvia Colombo
  - Raghav Pant
  - Marcus Young
  - Fred Thomas
  - Tom Russell
  - Jasper Verschuur
  - Jim W. Hall
  date_published: '2025-12-24'
  doi: https://doi.org/10.1038/s41597-025-06483-7
  id: reference_1
  name: The African Transport Systems Database - a geospatial database of multi-modal
    connected networks
  url: https://www.nature.com/articles/s41597-025-06483-7
resources:
- access_url: https://zenodo.org/records/17861120
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Geopackage file containing 234 airports across Africa with network
    topology (nodes and edges). Includes airport locations, airline routes between
    airports, and annual seat capacity data (2019) as a proxy for passenger volumes.
    Contains flight connection routes represented as straight-line segments between
    airport pairs.
  download_url: https://zenodo.org/records/17861120/files/africa_airport_network.gpkg
  format: null
  id: resource_airport_network
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: Individual transport node and edge level
  spatial_resolution: null
  temporal: null
  temporal_resolution: Annual
  title: Africa Airport Network
- access_url: https://zenodo.org/records/17861120
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Reference geopackage file containing airport location data from OurAirports
    database used for positional accuracy validation and coordinate correction of
    the World Bank Global Airports database. Provides high-accuracy airport terminal
    locations.
  download_url: https://zenodo.org/records/17861120/files/africa_airport_ourairport.gpkg
  format: null
  id: resource_airport_ourairport
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: Individual transport node and edge level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Africa Airport OurAirport Reference Data
- access_url: https://zenodo.org/records/17861120
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: CSV file containing estimated construction, upgrading, operation and
    maintenance costs for 41 major road corridors across Africa. Includes minimum,
    median, and maximum cost estimates per kilometer per lane based on road type and
    condition (paved/unpaved), with projections through 2050.
  download_url: https://zenodo.org/records/17861120/files/africa_corridors_costs.csv
  format: null
  id: resource_corridors_costs
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Africa Road Corridors Investment Costs
- access_url: https://zenodo.org/records/17861120
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Geopackage file containing inland waterway network including 60 inland
    ports and 132 total docking points (ports, piers, docks, landing sites, yacht
    clubs) with navigable routes. Covers Lakes Victoria, Tanganyika, Malawi, Kivu
    and waterways along the Congo and Nile river systems. Includes network topology
    with nodes (ports/docking points) and edges (navigable routes).
  download_url: https://zenodo.org/records/17861120/files/africa_iww_network.gpkg
  format: null
  id: resource_iww_network
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: Individual transport node and edge level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Africa Inland Waterways Network
- access_url: https://zenodo.org/records/17861120
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Geopackage file containing maritime port network with 179 ports and
    shipping routes between African ports. Includes port-to-port navigable routes,
    port usage statistics (2019-2024) from AIS data including annual vessel counts
    by cargo type (container, dry bulk, tankers, RoRo, general), cargo weights, vessel
    dwell times, and proportion of country exports/imports handled at each port.
  download_url: https://zenodo.org/records/17861120/files/africa_maritime_network.gpkg
  format: null
  id: resource_maritime_network
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: Individual transport node and edge level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Africa Maritime Network
- access_url: https://zenodo.org/records/17861120
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Geopackage file containing multimodal connections between different
    transport modes. Includes 7 types of inter-modal connections: airport-railway,
    airport-road, inland waterway-railway, inland waterway-road, maritime port-railway,
    maritime port-road, and railway-road. Each connection represented as directional
    edges linking nodes across transport networks.'
  download_url: https://zenodo.org/records/17861120/files/africa_multimodal.gpkg
  format: null
  id: resource_multimodal
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: Individual transport node and edge level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Africa Multimodal Network
- access_url: https://zenodo.org/records/17861120
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: CSV file containing estimated construction, upgrading, operation and
    maintenance costs for railway lines across Africa. Includes minimum, median, and
    maximum cost estimates per kilometer based on railway status (planned, proposed,
    rehabilitation), with projections through 2050.
  download_url: https://zenodo.org/records/17861120/files/africa_rails_costs.csv
  format: null
  id: resource_rails_costs
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Africa Railways Investment Costs
- access_url: https://zenodo.org/records/17861120
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Geopackage file containing comprehensive railway network with 6,057
    railway stations connected across 99,373 kilometers of rail lines. Includes 986
    named railway corridors with attributes for operational status (abandoned, under
    construction, disused, open, planned, proposed, razed, under rehabilitation, suspended),
    gauge widths, line names, and facility types (mines, ports, freight terminals,
    manufacturing, etc.). Network topology includes nodes (stations/junctions) and
    edges (rail line segments).
  download_url: https://zenodo.org/records/17861120/files/africa_railways_network.gpkg
  format: null
  id: resource_railways_network
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: Individual railway station and track segment level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Africa Railways Network
- access_url: https://zenodo.org/records/17861120
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Geopackage file containing comprehensive road network with 1,004,512
    kilometers of roads including motorways, trunk roads, primary and secondary routes,
    and connecting local roads. Includes 41 named major road corridors across Africa
    with attributes for highway classification, surface type (paved/unpaved), number
    of lanes, bridge indicators, and speed limits. Network topology includes nodes
    (junctions/endpoints) and edges (road segments).
  download_url: https://zenodo.org/records/17861120/files/africa_roads_network.gpkg
  format: null
  id: resource_roads_network
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: Individual road segment level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Africa Roads Network
- access_url: https://zenodo.org/records/17861120
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Excel spreadsheet containing comprehensive metadata documentation for
    the African Transport Systems Database. Describes each dataset component, column
    names, attributes, data sources, processing methods, and quality assessments.
    Provides detailed explanation of the database structure and content.
  download_url: https://zenodo.org/records/17861120/files/METADATA.xlsx
  format: null
  id: resource_metadata
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Africa Transport Database Metadata
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-nismod_aftsdb
spatial:
  bbox: null
  centroid: null
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
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal: null
temporal_resolution: null
title: 'The African Transport Systems Database: an open geospatial database of multi-modal
  connected networks'
version: '3'
vulnerability: null
---
