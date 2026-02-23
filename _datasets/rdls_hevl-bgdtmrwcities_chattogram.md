---
contact_point:
  email: emin.mentese@anofa.co
  id: attribution_contact
  name: "Mente\u015Fe, E.Y. - Anofa Engineering, Planning and Informatics Ltd."
  url: https://orcid.org/0000-0002-7187-4384
creator:
  email: support@tomorrowscities.org
  id: attribution_creator
  name: Tomorrow's Cities
  url: https://data.tomorrowscities.org/
dataset_id: rdls_hevl-bgdtmrwcities_chattogram
description: Multi-hazard risk data package for the Bairag area in Chattogram, Bangladesh,
  providing earthquake and flood hazard layers, synthetic future urban exposure datasets
  (buildings, households, individuals, land use, road networks) for four community
  planning scenarios (Civil Society, Farmers/Fishermen, Informal Working, Landless),
  vulnerability/fragility functions for buildings and infrastructure, and impact assessment
  results. Developed as part of the Tomorrow's Cities GCRF Urban Disaster Risk Hub
  project for risk-informed decision making in urban planning.
details: 'The dataset includes: (i) earthquake hazard GeoTIFFs for two scenarios -
  Sc1 using NGA-West2 GMPEs (Abrahamson et al 2014, Boore et al 2014, Campbell & Bozorgnia
  2014, Chiou & Youngs 2014) representing active shallow crustal sources, and Sc2
  using subduction zone GMPEs (Atkinson & Boore, Zhao et al), each providing PGA and
  Spectral Acceleration at 0.3s, 0.7s, 1.0s periods in 32-bit and 64-bit precision
  (48 rasters total); (ii) flood hazard rasters for riverine and pluvial (rainfall)
  scenarios with water depth as intensity measure, plus NASADEM terrain; (iii) four
  future exposure dataset variants representing different community planning scenarios,
  each containing building footprints with structural taxonomy (lateral resistance
  system, code level, storeys, occupancy), household socio-economic attributes, individual
  demographic data, land use plans, and road network topology; (iv) fragility functions
  for earthquake (45 building typologies with 4 damage states) and depth-damage vulnerability
  functions for flood (495 building typologies at 9 water depths); (v) infrastructure
  fragility for roads (HAZUS HWB) and power networks (HAZUS ESS); and (vi) impact
  results for earthquake and flood hazards by community scenario.'
exposure:
- category: buildings
  dimension: structure
  quantity_kind: area, count, currency
  taxonomy: GED4ALL
- category: population
  dimension: population
  quantity_kind: count
  taxonomy: GED4ALL
- category: infrastructure
  dimension: structure
  quantity_kind: count, length
  taxonomy: GED4ALL
- category: economic_indicator
  dimension: structure
  quantity_kind: area
  taxonomy: GED4ALL
extra_attributions:
- email: press@ukri.org
  id: attribution_funder
  name: Natural Environment Research Council (NERC)
  role: funder
  url: https://www.ukri.org/councils/nerc/
- email: servicedesk@ucl.ac.uk
  id: attribution_collaborator
  name: University College London
  role: collaborator
  url: https://www.ucl.ac.uk/
hazard:
  calculation_method: simulated
  disaster_identifiers: ''
  hazard_analysis_type: deterministic
  hazard_type: earthquake, flood
  intensity: PGA:g, wd:m
  occurrence_range: ''
  processes: fluvial_flood, ground_motion
  seasonality: ''
license: CC0-1.0
loss:
  approach: ''
  base_data_type: ''
  category: ''
  description: Affected population results from earthquake impact assessment for each
    community planning scenario, derived from building damage states and residential
    occupancy., Affected population results from flood impact assessment for each
    community planning scenario, derived from building inundation and residential
    occupancy., Building damage ratio results from flood impact assessment for each
    community planning scenario (Civil Society, Farmers/Fishermen, Informal Working,
    Landless). Damage ratios derived by applying depth-damage vulnerability functions
    to flood water depth hazard., Building damage state results from earthquake impact
    assessment for each community planning scenario (Civil Society, Farmers/Fishermen,
    Informal Working, Landless). Damage states derived by convolving spectral acceleration
    hazard with building fragility functions.
  dimension: ''
  exposure_id: ''
  hazard_analysis_type: ''
  hazard_id: ''
  hazard_process: fluvial_flood, ground_motion
  hazard_type: earthquake, flood
  impact_metric: ''
  impact_type: ''
  impact_unit: ''
  type: ''
  vulnerability_id: ''
project:
  name: Tomorrow's Cities - GCRF Urban Disaster Risk Hub
  url: https://tomorrowscities.org/
publisher:
  email: support@tomorrowscities.org
  id: attribution_publisher
  name: Tomorrow's Cities
  url: https://data.tomorrowscities.org/
purpose: To support multi-hazard risk assessment and risk-informed urban planning
  decision making for Chattogram by providing spatial hazard, synthetic future exposure,
  vulnerability functions, and impact assessment datasets for participatory community
  planning scenarios.
resources:
- coordinate_system: EPSG:4326
  description: 'Multi-hazard dataset containing: (1) Earthquake hazard rasters for
    two scenarios - Sc1 using NGA-West2 GMPEs (Abrahamson et al 2014, Boore et al
    2014, Campbell & Bozorgnia 2014, Chiou & Youngs 2014) for active shallow crustal
    sources, and Sc2 using subduction zone GMPEs (Atkinson & Boore, Zhao et al), each
    providing PGA and SA at 0.3s, 0.7s, 1.0s periods in 32-bit and 64-bit precision
    (48 rasters total); (2) Flood hazard rasters for riverine and pluvial scenarios
    with water depth; (3) Terrain DEM from NASADEM; (4) Vulnerability/fragility functions
    for buildings, roads, and power networks. Data formats: GeoTIFF for hazard rasters,
    Shapefile for vector flood data, Excel (XLSX) for vulnerability/fragility functions.'
  download_url: https://data.tomorrowscities.org/dataset/91fb3483-5f0b-4eba-8815-59c3abd30889/resource/c40ab1c3-07e4-4bb3-bd9d-6fbf1f7653cb/download/chattogrammultihazarddataset.zip
  format: GeoTIFF (tif)
  id: resource_hazard_multihazard
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Chattogram Multi Hazard Dataset
- coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Civil Society community planning
    scenario, including building footprints with structural taxonomy, household socio-economic
    data, individual demographic data, land use plan, and road network. Data formats:
    GeoJSON for spatial data (buildings, landuse, road network), JSON for tabular
    data (households, individuals).'
  download_url: https://data.tomorrowscities.org/dataset/ca37dabd-dd6a-4545-bae9-665943704205/resource/88f85d4b-97ed-49a8-adf7-a02fcd75b747/download/chattogramfutureexposuredataset_civil_society.zip
  format: GeoJSON (geojson)
  id: resource_exposure_civil_society
  media_type: null
  spatial_resolution: null
  temporal:
    duration: P50Y
    end: null
    start: null
    temporal_resolution: null
  title: Chattogram Future Exposure Dataset - Civil Society
- coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Farmers/Fishermen community planning
    scenario, including building footprints with structural taxonomy, household socio-economic
    data, individual demographic data, land use plan, and road network. Data formats:
    GeoJSON for spatial data (buildings, landuse, road network), JSON for tabular
    data (households, individuals).'
  download_url: https://data.tomorrowscities.org/dataset/6f46d7af-e3b0-4fd6-bb68-398213e4ec4f/resource/c4a37c18-022d-4e22-88c3-61ad0d05c775/download/chattogramfutureexposuredataset_farmers_fishermen.zip
  format: GeoJSON (geojson)
  id: resource_exposure_farmers_fishermen
  media_type: null
  spatial_resolution: null
  temporal:
    duration: P50Y
    end: null
    start: null
    temporal_resolution: null
  title: Chattogram Future Exposure Dataset - Farmers Fishermen
- coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Informal Working community planning
    scenario, including building footprints with structural taxonomy, household socio-economic
    data, individual demographic data, land use plan, and road network. Data formats:
    GeoJSON for spatial data (buildings, landuse, road network), JSON for tabular
    data (households, individuals).'
  download_url: https://data.tomorrowscities.org/dataset/07df0763-2441-4b7d-9252-dc209e78d81a/resource/41f36288-6e2f-4e04-9363-9f8bab0150e5/download/chattogramfutureexposuredataset_informal_working.zip
  format: GeoJSON (geojson)
  id: resource_exposure_informal_working
  media_type: null
  spatial_resolution: null
  temporal:
    duration: P50Y
    end: null
    start: null
    temporal_resolution: null
  title: Chattogram Future Exposure Dataset - Informal Working
- coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Landless community planning scenario,
    including building footprints with structural taxonomy, household socio-economic
    data, individual demographic data, land use plan, and road network. Data formats:
    GeoJSON for spatial data (buildings, landuse, road network), JSON for tabular
    data (households, individuals).'
  download_url: https://data.tomorrowscities.org/dataset/5940db5c-e04f-4855-8353-54f2cf2d3466/resource/aafc37fb-1258-466f-a30f-2559bdcc422b/download/chattogramfutureexposuredataset_landless.zip
  format: GeoJSON (geojson)
  id: resource_exposure_landless
  media_type: null
  spatial_resolution: null
  temporal:
    duration: P50Y
    end: null
    start: null
    temporal_resolution: null
  title: Chattogram Future Exposure Dataset - Landless
- coordinate_system: EPSG:4326
  description: 'Impact assessment results for earthquake and flood hazards under the
    Civil Society community planning scenario, including building damage states and
    affected population. Data formats: ESRI File Geodatabase (GDB) and GeoJSON.'
  download_url: https://data.tomorrowscities.org/dataset/ccde0b57-a447-4e15-a018-c2a0ab5eaaea/resource/afddc29c-6187-447c-87eb-60866603bc00/download/chattogramimpactresults_civil_society.zip
  format: File Geodatabase (gdb)
  id: resource_impact_civil_society
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Chattogram Impact Results - Civil Society
- coordinate_system: EPSG:4326
  description: 'Impact assessment results for earthquake and flood hazards under the
    Farmers/Fishermen community planning scenario, including building damage states
    and affected population. Data formats: ESRI File Geodatabase (GDB) and GeoJSON.'
  download_url: https://data.tomorrowscities.org/dataset/6f13c0b5-00c0-4bec-946d-e7644845478c/resource/5243bd1f-d134-4a14-88f6-b6f48a190748/download/chattogramimpactresults_farmers.zip
  format: File Geodatabase (gdb)
  id: resource_impact_farmers
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Chattogram Impact Results - Farmers
- coordinate_system: EPSG:4326
  description: 'Impact assessment results for earthquake and flood hazards under the
    Informal Working community planning scenario, including building damage states
    and affected population. Data formats: ESRI File Geodatabase (GDB) and GeoJSON.'
  download_url: https://data.tomorrowscities.org/dataset/618b12f3-4839-4b6d-ae50-42d7f09fd7de/resource/cba12127-cdf0-4abd-af8d-2c1babd8c55b/download/chattogramimpactresults_informal_working.zip
  format: File Geodatabase (gdb)
  id: resource_impact_informal_working
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Chattogram Impact Results - Informal Working
- coordinate_system: EPSG:4326
  description: 'Impact assessment results for earthquake and flood hazards under the
    Landless community planning scenario, including building damage states and affected
    population. Data formats: ESRI File Geodatabase (GDB) and GeoJSON.'
  download_url: https://data.tomorrowscities.org/dataset/3bc2f627-c16a-46ae-9e46-44a0fcc586b3/resource/d0a7a407-92ae-4db5-aabb-cec623611a7d/download/chattogramimpactresults_landless.zip
  format: File Geodatabase (gdb)
  id: resource_impact_landless
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Chattogram Impact Results - Landless
risk_data_type:
- hazard
- exposure
- vulnerability
- loss
schema: rdl-03
slug: rdls_hevl-bgdtmrwcities_chattogram
spatial:
  bbox:
  - 91.8134
  - 22.2096
  - 91.8681
  - 22.2534
  countries:
  - BGD
  gazetteer_entries:
  - description: Bangladesh
    id: gazetteer_1
    scheme: GEONAMES
    uri: https://www.geonames.org/1210997/bangladesh.html
  - description: Chattogram (Chittagong)
    id: gazetteer_2
    scheme: GEONAMES
    uri: https://www.geonames.org/1205733/chattogram.html
  - description: Bairag
    id: gazetteer_3
    scheme: GEONAMES
    uri: https://www.geonames.org/11282344/bairag.html
  scale: sub-national
title: Tomorrow's Cities Multi-Hazard Risk Assessment Dataset for Chattogram (Bairag),
  Bangladesh
version: '1'
vulnerability:
  approach: analytical, empirical
  base_data_type: simulated
  category: buildings, infrastructure
  dimension: ''
  function_type: ''
  hazard_analysis_type: deterministic
  hazard_primary: earthquake, flood
  hazard_process_primary: fluvial_flood, ground_motion
  hazard_process_secondary: ''
  hazard_secondary: ''
  intensity: ''
  metric: damage_ratio
  relationship: discrete, math_parametric
  taxonomy: Custom, HAZUS
  unit: ''
---
