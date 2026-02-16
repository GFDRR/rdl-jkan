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
dataset_id: rdls_lss-tmrwcities_daressalaam
description: Multi-hazard risk data package for Dar es Salaam, Tanzania, providing
  flood hazard layers (two pluvial scenarios), synthetic future urban exposure datasets
  (buildings, households, individuals, land use, road networks, power networks) for
  four community planning scenarios (Elderly, Leaders, Residents, Youth), vulnerability/fragility
  functions for buildings and infrastructure (flood and landslide), and impact assessment
  results. Developed as part of the Tomorrow's Cities GCRF Urban Disaster Risk Hub
  project for risk-informed decision making in urban planning.
details: "The dataset includes: (i) flood hazard GeoTIFFs for two deterministic pluvial\
  \ scenarios - Scenario 1 (7mm over 24 hours) and Scenario 2 (19mm/hr for 6 hours)\
  \ - simulated using high-resolution solver with 5m DTM and Manning's n=0.06; (ii)\
  \ four future exposure dataset variants representing different community planning\
  \ scenarios (Elderly, Leaders, Residents, Youth), each containing building footprints\
  \ with structural taxonomy (lateral resistance system including Adobe, code level,\
  \ storeys, occupancy, income level), household socio-economic attributes, individual\
  \ demographic data, land use plans (115 zones, 29 categories), road network topology\
  \ (106 edges with degree classification), and power network infrastructure (2 substations,\
  \ 2 transmission lines); (iii) depth-damage vulnerability functions for flood (7,354\
  \ building typologies at 9 water depths) and fragility functions for landslide (60\
  \ entries: 20 typologies \xD7 3 susceptibility levels with minor/moderate/severe\
  \ damage states); and (iv) impact results for both flood scenarios by community\
  \ scenario, including building damage, hospital accessibility, and road network\
  \ disruption."
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
  hazard_analysis_type: deterministic
  hazard_type: flood
  intensity: wd:m
  occurrence_range: ''
  processes: pluvial_flood
  seasonality: ''
license: CC0-1.0
loss:
  approach: ''
  base_data_type: ''
  category: ''
  description: Building damage state results from flood impact assessment for each
    community planning scenario (Elderly, Leaders, Residents, Youth) and both flood
    scenarios. Damage states (DS0=undamaged, DS1=damaged) derived by applying depth-damage
    vulnerability functions to flood water depth hazard., Casualty results from flood
    impact assessment for each community planning scenario, derived from building
    inundation and residential occupancy., Hospital accessibility and power availability
    impacts from flood, derived from road network connectivity analysis (road edges
    damaged by flooding) and power network assessment. Each building has hospital_access
    and has_power boolean attributes., Road network damage state results from flood
    impact assessment, with road edges flagged as damaged/undamaged based on flood
    inundation.
  dimension: ''
  exposure_id: ''
  hazard_analysis_type: ''
  hazard_id: ''
  hazard_process: pluvial_flood
  hazard_type: flood
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
  decision making for Dar es Salaam by providing spatial hazard, synthetic future
  exposure, vulnerability functions, and impact assessment datasets for participatory
  community planning scenarios.
resources:
- coordinate_system: EPSG:4326
  description: 'Multi-hazard dataset containing: (1) Flood hazard rasters for two
    deterministic pluvial scenarios - Scenario 1 (7mm/24hr) and Scenario 2 (19mm/hr
    for 6hr) with water depth in WGS84 projection; (2) Vulnerability/fragility functions
    for buildings (7,354 flood typologies) and landslide (60 entries for buildings
    and infrastructure). Data formats: GeoTIFF for hazard rasters, Excel (XLSX) for
    vulnerability/fragility functions.'
  download_url: https://data.tomorrowscities.org/dataset/1069bf2e-b3d2-466e-bc24-306b262f475c/resource/5a8e8fc1-be1b-434f-8e34-e1a7f88b3b31/download/darmultihazarddataset.zip
  format: GeoTIFF (tif)
  id: resource_hazard_multihazard
  media_type: null
  spatial_resolution: 5
  temporal: null
  title: Dar es Salaam Multi Hazard Dataset
- coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Elderly community planning scenario,
    including building footprints with structural taxonomy (including Adobe and income
    levels), household socio-economic data, individual demographic data, land use
    plan (115 zones), road network (106 edges), and power network infrastructure (2
    substations). Data formats: GeoJSON for spatial data, XLSX for tabular data (households,
    individuals).'
  download_url: https://data.tomorrowscities.org/dataset/abde7716-e686-477c-8b86-792de010d3af/resource/aeeb8a8b-d98a-4e4b-a7b6-fbc18bd79673/download/darfutureexposuredataset_elderly.zip
  format: GeoJSON (geojson)
  id: resource_exposure_elderly
  media_type: null
  spatial_resolution: null
  temporal:
    duration: P50Y
    end: null
    start: null
    temporal_resolution: null
  title: Dar es Salaam Future Exposure Dataset - Elderly
- coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Leaders community planning scenario,
    including building footprints with structural taxonomy (including Adobe and income
    levels), household socio-economic data, individual demographic data, land use
    plan, road network, and power network infrastructure. Data formats: GeoJSON for
    spatial data, XLSX for tabular data (households, individuals).'
  download_url: https://data.tomorrowscities.org/dataset/aafcabf8-1a11-47ce-b5e8-e543e63efe63/resource/f59a4029-f566-4362-9c24-c5d16719fa03/download/darfutureexposuredataset_leaders.zip
  format: GeoJSON (geojson)
  id: resource_exposure_leaders
  media_type: null
  spatial_resolution: null
  temporal:
    duration: P50Y
    end: null
    start: null
    temporal_resolution: null
  title: Dar es Salaam Future Exposure Dataset - Leaders
- coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Residents community planning scenario,
    including building footprints with structural taxonomy (including Adobe and income
    levels), household socio-economic data, individual demographic data, land use
    plan, road network, and power network infrastructure. Data formats: GeoJSON for
    spatial data, XLSX for tabular data (households, individuals).'
  download_url: https://data.tomorrowscities.org/dataset/3b4809d3-da30-4cfd-87fe-f1b1c81bd855/resource/d87afb73-a1fc-46ea-8d1b-aac8fdb1995d/download/darfutureexposuredataset_residents.zip
  format: GeoJSON (geojson)
  id: resource_exposure_residents
  media_type: null
  spatial_resolution: null
  temporal:
    duration: P50Y
    end: null
    start: null
    temporal_resolution: null
  title: Dar es Salaam Future Exposure Dataset - Residents
- coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Youth community planning scenario,
    including building footprints with structural taxonomy (including Adobe and income
    levels), household socio-economic data, individual demographic data, land use
    plan, road network, and power network infrastructure. Data formats: GeoJSON for
    spatial data, XLSX for tabular data (households, individuals).'
  download_url: https://data.tomorrowscities.org/dataset/60fa9b22-6c55-48d5-98e4-826ffee8923f/resource/c984310e-bdec-4051-b79e-0fd0495c7082/download/darfutureexposuredataset_youth.zip
  format: GeoJSON (geojson)
  id: resource_exposure_youth
  media_type: null
  spatial_resolution: null
  temporal:
    duration: P50Y
    end: null
    start: null
    temporal_resolution: null
  title: Dar es Salaam Future Exposure Dataset - Youth
- coordinate_system: EPSG:4326
  description: 'Impact assessment results for flood hazards (both scenarios) under
    the Elderly community planning scenario, including building damage states, casualties,
    hospital accessibility, power availability, and road network disruption. Data
    formats: ESRI File Geodatabase (GDB) and GeoJSON.'
  download_url: https://data.tomorrowscities.org/dataset/c4da084d-0c38-426b-8beb-f9abc21b7e33/resource/c986fb15-8350-4d60-913d-03657dccb0b2/download/darimpactresults_elderly.zip
  format: File Geodatabase (gdb)
  id: resource_impact_elderly
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Dar es Salaam Impact Results - Elderly
- coordinate_system: EPSG:4326
  description: 'Impact assessment results for flood hazards (both scenarios) under
    the Leaders community planning scenario, including building damage states, casualties,
    hospital accessibility, power availability, and road network disruption. Data
    formats: ESRI File Geodatabase (GDB) and GeoJSON.'
  download_url: https://data.tomorrowscities.org/dataset/a79d86bd-4ecb-475a-b7c5-5933abcd7d00/resource/a0d509ae-29aa-4fbe-b40d-f0d6535e6479/download/darimpactresults_leaders.zip
  format: File Geodatabase (gdb)
  id: resource_impact_leaders
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Dar es Salaam Impact Results - Leaders
- coordinate_system: EPSG:4326
  description: 'Impact assessment results for flood hazards (both scenarios) under
    the Residents community planning scenario, including building damage states, casualties,
    hospital accessibility, power availability, and road network disruption. Data
    formats: ESRI File Geodatabase (GDB) and GeoJSON.'
  download_url: https://data.tomorrowscities.org/dataset/10097ffd-2638-4bdb-bd60-f0b2bb9f73ee/resource/836134a2-9da3-43db-941a-292a57fa5dd5/download/darimpactresults_residents.zip
  format: File Geodatabase (gdb)
  id: resource_impact_residents
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Dar es Salaam Impact Results - Residents
- coordinate_system: EPSG:4326
  description: 'Impact assessment results for flood hazards (both scenarios) under
    the Youth community planning scenario, including building damage states, casualties,
    hospital accessibility, power availability, and road network disruption. Data
    formats: ESRI File Geodatabase (GDB) and GeoJSON.'
  download_url: https://data.tomorrowscities.org/dataset/3b530d66-9e8b-425d-9c19-d7b2266560ed/resource/83594a76-6c24-4281-8784-13c336427d81/download/darimpactresults_youth.zip
  format: File Geodatabase (gdb)
  id: resource_impact_youth
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Dar es Salaam Impact Results - Youth
risk_data_type:
- hazard
- exposure
- vulnerability
- loss
schema: rdl-03
slug: rdls_lss-tmrwcities_daressalaam
spatial:
  bbox:
  - 39.2378
  - -6.95
  - 39.274
  - -6.9207
  countries:
  - TZA
  gazetteer_entries:
  - description: Tanzania
    id: gazetteer_1
    scheme: GEONAMES
    uri: https://www.geonames.org/149590/tanzania.html
  - description: Dar es Salaam
    id: gazetteer_2
    scheme: GEONAMES
    uri: https://www.geonames.org/160263/dar-es-salaam.html
  scale: sub-national
title: Tomorrow's Cities Multi-Hazard Risk Assessment Dataset for Dar es Salaam, Tanzania
version: '1'
vulnerability:
  approach: analytical, empirical
  base_data_type: simulated
  category: buildings, infrastructure
  dimension: ''
  function_type: ''
  hazard_analysis_type: deterministic
  hazard_primary: flood, landslide
  hazard_process_primary: landslide_general, pluvial_flood
  hazard_process_secondary: ''
  hazard_secondary: ''
  intensity: ''
  metric: damage_ratio
  relationship: discrete, math_parametric
  taxonomy: Custom, HAZUS
  unit: ''
---
