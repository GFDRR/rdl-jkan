---
catalog: null
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
dataset_id: rdls_lss-tmrwcities_coxsbazar
description: Multi-hazard risk data package for the Jaliya Palong area in Cox's Bazar,
  Bangladesh, providing earthquake and flood hazard layers, synthetic future urban
  exposure datasets (buildings, households, individuals, land use, road networks,
  power networks) for four community planning scenarios (Civil Society, Informal Working,
  Marginal, Women), vulnerability/fragility functions for buildings and infrastructure,
  and impact assessment results including cascading infrastructure effects. Developed
  as part of the Tomorrow's Cities GCRF Urban Disaster Risk Hub project for risk-informed
  decision making in urban planning.
details: 'The dataset includes: (i) earthquake hazard GeoTIFFs for two scenarios -
  Sc1 using NGA-West2 GMPEs (Abrahamson et al 2014, Boore et al 2014, Campbell & Bozorgnia
  2014, Chiou & Youngs 2014) representing active shallow crustal sources, and Sc2
  using subduction zone GMPEs (Atkinson & Boore, Zhao et al), each providing PGA and
  Spectral Acceleration at 0.3s, 0.7s, 1.0s periods in 32-bit and 64-bit precision
  (48 rasters total); (ii) probabilistic flood hazard rasters for 5, 10, 20, and 50-year
  return periods with water depth as intensity measure, plus additional flood maps
  and 1991 cyclone reference data; (iii) four future exposure dataset variants representing
  different community planning scenarios, each containing building footprints with
  structural taxonomy (including Steel buildings), household socio-economic attributes,
  individual demographic data, land use plans, road network topology, and power network
  infrastructure; (iv) fragility functions for earthquake (45 building typologies
  with 4 damage states) and depth-damage vulnerability functions for flood (1,521
  building typologies at 9 water depths); (v) infrastructure fragility for roads (HAZUS
  HWB including HWB19) and power networks (HAZUS ESS with 18 classes); and (vi) comprehensive
  impact results for earthquake and flood hazards by community scenario, including
  building damage, casualties, road network disruption, and cascading effects on hospital
  accessibility and power availability.'
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
- category: infrastructure
  dimension: structure
  quantity_kind: count
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
  hazard_analysis_type: deterministic, probabilistic
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
  description: Building damage state results from earthquake impact assessment for
    each community planning scenario (Civil Society, Informal Working, Marginal, Women).
    Damage states (DS1-DS4) derived by convolving spectral acceleration hazard with
    building fragility functions., Building damage state results from flood impact
    assessment for each community planning scenario (Civil Society, Informal Working,
    Marginal, Women). Damage states (DS0-DS1) derived by applying depth-damage vulnerability
    functions to flood water depth hazard., Casualty results from earthquake impact
    assessment for each community planning scenario, derived from building damage
    states and residential occupancy., Casualty results from flood impact assessment
    for each community planning scenario, derived from building inundation and residential
    occupancy., Hospital accessibility and power availability impacts from earthquake,
    derived from road network connectivity analysis and power network damage assessment.
    Each building has hospital_access and has_power boolean attributes., Hospital
    accessibility and power availability impacts from flood, derived from road network
    connectivity analysis (road edges damaged by flooding) and power network assessment.
    Flood causes significant road network disruption reducing hospital accessibility.,
    Road and power network damage state results from earthquake impact assessment,
    including edge and node damage for both infrastructure types., Road network damage
    state results from flood impact assessment, with road edges flagged as damaged/undamaged
    based on flood inundation.
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
  decision making for Cox's Bazar by providing spatial hazard, synthetic future exposure,
  vulnerability functions, and impact assessment datasets for participatory community
  planning scenarios.
resources:
- coordinate_system: EPSG:4326
  description: 'Multi-hazard dataset containing: (1) Earthquake hazard rasters for
    two scenarios - Sc1 using NGA-West2 GMPEs (Abrahamson et al 2014, Boore et al
    2014, Campbell & Bozorgnia 2014, Chiou & Youngs 2014) for active shallow crustal
    sources, and Sc2 using subduction zone GMPEs (Atkinson & Boore, Zhao et al), each
    providing PGA and SA at 0.3s, 0.7s, 1.0s periods in 32-bit and 64-bit precision
    (48 rasters total); (2) Probabilistic flood hazard rasters for 5, 10, 20, 50-year
    return periods with water depth, plus additional flood maps and 1991 cyclone reference;
    (3) Vulnerability/fragility functions for buildings (45 earthquake, 1521 flood
    typologies), roads (HWB3, HWB5, HWB7, HWB19), and power networks (18 ESS/EPP/EDC/transformer
    classes). Data formats: GeoTIFF for hazard rasters, CSV for cyclone data, Excel
    (XLSX) for vulnerability/fragility functions.'
  download_url: https://data.tomorrowscities.org/dataset/66ca622a-822e-4f8d-8e56-e79833251d99/resource/673394a9-520c-4b6a-819d-04b564e37936/download/coxsbazaarhazarddataset.zip
  format: GeoTIFF (tif)
  id: resource_hazard_multihazard
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Cox's Bazar Hazard Dataset
- coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Civil Society community planning
    scenario, including building footprints with structural taxonomy (including Steel
    buildings), household socio-economic data, individual demographic data, land use
    plan, road network, and power network infrastructure. Data formats: GeoJSON for
    spatial data (buildings, landuse, road network, power network), JSON and XLSX
    for tabular data (households, individuals).'
  download_url: https://data.tomorrowscities.org/dataset/89b9c298-1d19-4b84-853f-8a76ac49c8b4/resource/98731ba2-c23c-470a-b50c-607bfd6330cb/download/coxsbazarexposuredataset_civil_society.zip
  format: GeoJSON (geojson)
  id: resource_exposure_civil_society
  media_type: null
  spatial_resolution: null
  temporal:
    duration: P50Y
    end: null
    start: null
    temporal_resolution: null
  title: Cox's Bazar Future Exposure Dataset - Civil Society
- coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Informal Working community planning
    scenario, including building footprints with structural taxonomy (including Steel
    buildings), household socio-economic data, individual demographic data, land use
    plan, road network, and power network infrastructure. Data formats: GeoJSON for
    spatial data (buildings, landuse, road network, power network), JSON and XLSX
    for tabular data (households, individuals).'
  download_url: https://data.tomorrowscities.org/dataset/618cfee1-13ed-4702-a57f-a44d902df75f/resource/23d68778-5dd7-47c0-b642-78c2b6194108/download/coxsbazarexposuredataset_informal_working.zip
  format: GeoJSON (geojson)
  id: resource_exposure_informal_working
  media_type: null
  spatial_resolution: null
  temporal:
    duration: P50Y
    end: null
    start: null
    temporal_resolution: null
  title: Cox's Bazar Future Exposure Dataset - Informal Working
- coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Marginal community planning scenario,
    including building footprints with structural taxonomy (including Steel buildings),
    household socio-economic data, individual demographic data, land use plan, road
    network, and power network infrastructure. Data formats: GeoJSON for spatial data
    (buildings, landuse, road network, power network), JSON and XLSX for tabular data
    (households, individuals), QMD for QGIS metadata.'
  download_url: https://data.tomorrowscities.org/dataset/e1b0423f-a5e8-437f-938f-b5368a09ada3/resource/9cc73da0-e710-4bbc-8317-3402d73b0e67/download/coxsbazarexposuredataset_marginal.zip
  format: GeoJSON (geojson)
  id: resource_exposure_marginal
  media_type: null
  spatial_resolution: null
  temporal:
    duration: P50Y
    end: null
    start: null
    temporal_resolution: null
  title: Cox's Bazar Future Exposure Dataset - Marginal
- coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Women community planning scenario,
    including building footprints with structural taxonomy (including Steel buildings),
    household socio-economic data, individual demographic data, land use plan, road
    network, and power network infrastructure. Data formats: GeoJSON for spatial data
    (buildings, landuse, road network, power network), JSON and XLSX for tabular data
    (households, individuals), QMD for QGIS metadata.'
  download_url: https://data.tomorrowscities.org/dataset/c0aa46d6-48bf-45e7-8406-e4e156e8eaa7/resource/9fb30762-19a6-4dc2-96ca-0a2c2ed0d796/download/coxsbazarexposuredataset_women.zip
  format: GeoJSON (geojson)
  id: resource_exposure_women
  media_type: null
  spatial_resolution: null
  temporal:
    duration: P50Y
    end: null
    start: null
    temporal_resolution: null
  title: Cox's Bazar Future Exposure Dataset - Women
- coordinate_system: EPSG:4326
  description: 'Impact assessment results for earthquake and flood hazards under the
    Civil Society community planning scenario, including building damage states, casualties,
    road network disruption, power network impacts, hospital accessibility, and power
    availability per building. Data formats: ESRI File Geodatabase (GDB) and GeoJSON.'
  download_url: https://data.tomorrowscities.org/dataset/1515bb10-af96-40e3-8ea5-1b2b9b9b1cbf/resource/01b8fc60-f6a2-4fc8-b7f5-974d2120b333/download/coxsbazarimpactresults_civil_society.zip
  format: File Geodatabase (gdb)
  id: resource_impact_civil_society
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Cox's Bazar Impact Results - Civil Society
- coordinate_system: EPSG:4326
  description: 'Impact assessment results for earthquake and flood hazards under the
    Informal Working community planning scenario, including building damage states,
    casualties, road network disruption, power network impacts, hospital accessibility,
    and power availability per building. Data formats: ESRI File Geodatabase (GDB)
    and GeoJSON.'
  download_url: https://data.tomorrowscities.org/dataset/64489c05-9af4-49b4-aea8-85d951ff1630/resource/95b40d12-e65a-4778-abe6-43468667db89/download/coxsbazarimpactresults_informal_working.zip
  format: File Geodatabase (gdb)
  id: resource_impact_informal_working
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Cox's Bazar Impact Results - Informal Working
- coordinate_system: EPSG:4326
  description: 'Impact assessment results for earthquake and flood hazards under the
    Marginal community planning scenario, including building damage states, casualties,
    road network disruption, power network impacts, hospital accessibility, and power
    availability per building. Data formats: ESRI File Geodatabase (GDB) and GeoJSON,
    QMD for QGIS metadata.'
  download_url: https://data.tomorrowscities.org/dataset/36d4d669-c16a-4aca-a17f-a4a178a4d5ef/resource/1618e2c9-7c0b-4024-ba25-ae47ff04b94a/download/coxsbazarimpactresults_marginal.zip
  format: File Geodatabase (gdb)
  id: resource_impact_marginal
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Cox's Bazar Impact Results - Marginal
- coordinate_system: EPSG:4326
  description: 'Impact assessment results for earthquake and flood hazards under the
    Women community planning scenario, including building damage states, casualties,
    road network disruption, power network impacts, hospital accessibility, and power
    availability per building. Data formats: ESRI File Geodatabase (GDB) and GeoJSON.'
  download_url: https://data.tomorrowscities.org/dataset/05faed28-08b3-4086-b1ee-316e06eaa1a1/resource/cbcd212f-60c8-45dd-9111-9fa096443175/download/coxsbazarimpactresults_women.zip
  format: File Geodatabase (gdb)
  id: resource_impact_women
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Cox's Bazar Impact Results - Women
risk_data_type:
- hazard
- exposure
- vulnerability
- loss
schema: rdl-03
slug: rdls_lss-tmrwcities_coxsbazar
spatial:
  bbox:
  - 92.0428
  - 21.078
  - 92.138
  - 21.303
  countries:
  - BGD
  gazetteer_entries:
  - description: Bangladesh
    id: gazetteer_1
    scheme: GEONAMES
    uri: https://www.geonames.org/1210997/bangladesh.html
  - description: Cox's Bazar
    id: gazetteer_2
    scheme: GEONAMES
    uri: https://www.geonames.org/1337202/cox-s-bazar.html
  - description: Jaliya Palong
    id: gazetteer_3
    scheme: GEONAMES
    uri: https://www.geonames.org/11282628/jalia-palong.html
  scale: sub-national
title: Tomorrow's Cities Multi-Hazard Risk Assessment Dataset for Cox's Bazar (Jaliya
  Palong), Bangladesh
version: '1'
vulnerability:
  approach: analytical, empirical
  base_data_type: simulated
  category: buildings, infrastructure
  dimension: ''
  function_type: ''
  hazard_analysis_type: deterministic, probabilistic
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
