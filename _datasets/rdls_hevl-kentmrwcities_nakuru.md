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
dataset_id: rdls_hevl-kentmrwcities_nakuru
description: Flood risk data package for Nakuru, Kenya, providing a flood hazard map
  (image-only PNG, no numerical raster), synthetic future urban exposure datasets
  (buildings, households, individuals, land use, road networks) for four community
  planning scenarios (FBO, RES, SNG, WOM), and flood impact assessment results including
  building damage, road disruption, hospital accessibility, power availability, and
  casualties. Developed as part of the Tomorrow's Cities GCRF Urban Disaster Risk
  Hub project for risk-informed decision making in urban planning.
details: "The dataset includes: (i) flood hazard PNG map visualisation (13.5 MB) \u2014\
  \ critical limitation: no numerical flood depth raster or vector data is provided,\
  \ only an image; (ii) four future exposure dataset variants representing different\
  \ community planning scenarios (FBO: Faith-Based Organisations, RES: Residents,\
  \ SNG: Sub-National Government, WOM: Women), each containing building footprints\
  \ in GeoJSON and Shapefile (34,261 buildings, 255 typologies including Steel material)\
  \ with rich attributes (OccBld, lrstype, CodeLevel, nstoreys, unit_price), household\
  \ data (89,951 households), individual demographics, road network (642 edges with\
  \ bridge types), and land use plans (47 zones, 22 categories); and (iii) impact\
  \ results per scenario including building damage states, casualties, hospital accessibility,\
  \ power availability, and road edge damage. Note: WOM impact results appear to be\
  \ missing from the dataset."
exposure:
  category: buildings, economic_indicator, infrastructure, population
  dimension: population, structure
  quantity_kind: area, count, currency, length
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
  processes: fluvial_flood
  seasonality: ''
license: CC0-1.0
loss:
  approach: ''
  base_data_type: ''
  category: ''
  description: Building damage state results from flood impact assessment for community
    planning scenarios (FBO, RES, SNG). WOM impact results not available., Casualty
    results from flood impact assessment for each community planning scenario., Hospital
    accessibility and power availability impacts from flood. Each building has hospital_access
    and has_power boolean attributes., Road network damage from flood impact assessment
    (642 road edges with damage state and bridge type attributes).
  dimension: ''
  exposure_id: ''
  hazard_analysis_type: ''
  hazard_id: ''
  hazard_process: fluvial_flood
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
purpose: To support flood risk assessment and risk-informed urban planning decision
  making for Nakuru by providing spatial hazard visualisation, synthetic future exposure,
  and impact assessment datasets for participatory community planning scenarios.
resources:
- coordinate_system: null
  description: "Flood hazard dataset containing a flood hazard map image (FloodHazardMap.png,\
    \ 13.5 MB). Critical limitation: only PNG visualisation \u2014 no numerical GeoTIFF\
    \ or GeoJSON flood depth raster is available."
  download_url: https://data.tomorrowscities.org/dataset/nakuru-multi-hazard-dataset/resource/cd00fa68-8d74-409a-b757-0b39e144b119
  format: PDF (pdf)
  id: resource_hazard_multihazard
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Nakuru Multi Hazard Dataset
- coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Faith-Based Organisations planning
    scenario, including building footprints (34,261 buildings, 255 typologies) with
    rich attributes (OccBld, lrstype, CodeLevel, nstoreys, unit_price), household
    data (89,951 households), individual demographics, road network (642 edges), and
    land use plan (47 zones). Data formats: GeoJSON, Shapefile, JSON, XLSX, PNG.'
  download_url: https://data.tomorrowscities.org/dataset/nakuru-future-exposure-dataset-fbo/resource/c7b7189c-3527-4fef-be66-90477e727e11
  format: GeoJSON (geojson)
  id: resource_exposure_fbo
  media_type: null
  spatial_resolution: null
  temporal:
    duration: P50Y
    end: null
    start: null
    temporal_resolution: null
  title: Nakuru Future Exposure Dataset - FBO
- coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Residents planning scenario. Data
    formats: GeoJSON, Shapefile, JSON, XLSX.'
  download_url: https://data.tomorrowscities.org/dataset/nakuru-future-exposure-dataset-res/resource/cbfc7d35-95f6-41bd-8647-c847b41b0fcf
  format: GeoJSON (geojson)
  id: resource_exposure_res
  media_type: null
  spatial_resolution: null
  temporal:
    duration: P50Y
    end: null
    start: null
    temporal_resolution: null
  title: Nakuru Future Exposure Dataset - RES
- coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Single/Non-Governmental planning
    scenario. Data formats: GeoJSON, Shapefile, JSON, XLSX.'
  download_url: https://data.tomorrowscities.org/dataset/nakuru-future-exposure-dataset-sng/resource/5b21b5ad-2f47-4bcc-8014-6306f1659358
  format: GeoJSON (geojson)
  id: resource_exposure_sng
  media_type: null
  spatial_resolution: null
  temporal:
    duration: P50Y
    end: null
    start: null
    temporal_resolution: null
  title: Nakuru Future Exposure Dataset - SNG
- coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Women planning scenario. Data formats:
    GeoJSON, Shapefile, JSON, XLSX.'
  download_url: https://data.tomorrowscities.org/dataset/nakuru-future-exposure-dataset-wom/resource/a0f77693-86c5-4eee-b7f4-e5da246c7fe2
  format: GeoJSON (geojson)
  id: resource_exposure_wom
  media_type: null
  spatial_resolution: null
  temporal:
    duration: P50Y
    end: null
    start: null
    temporal_resolution: null
  title: Nakuru Future Exposure Dataset - WOM
- coordinate_system: EPSG:4326
  description: 'Flood impact results for Faith-Based Organisations scenario including
    building damage, casualties, hospital accessibility, power availability, and road
    damage. Data format: GeoJSON.'
  download_url: https://data.tomorrowscities.org/dataset/nakuru-impact-results-fbo/resource/bdc3f70b-4808-4665-a084-8225a6d5d7ec
  format: GeoJSON (geojson)
  id: resource_impact_fbo
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Nakuru Impact Results - FBO
- coordinate_system: EPSG:4326
  description: 'Flood impact results for Residents scenario. Data format: GeoJSON.'
  download_url: https://data.tomorrowscities.org/dataset/nakuru-impact-results-res/resource/c31c8e73-f934-4e62-81ad-3e6ce2a5e87f
  format: GeoJSON (geojson)
  id: resource_impact_res
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Nakuru Impact Results - RES
- coordinate_system: EPSG:4326
  description: 'Flood impact results for Sub-National Government scenario. Data format:
    GeoJSON.'
  download_url: https://data.tomorrowscities.org/dataset/nakuru-impact-results-sng/resource/9ec3523d-31bb-41dd-b8ee-7ae4b9b37437
  format: GeoJSON (geojson)
  id: resource_impact_sng
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Nakuru Impact Results - SNG
- coordinate_system: EPSG:4326
  description: 'Flood impact results for Women scenario. Data format: GeoJSON.'
  download_url: https://data.tomorrowscities.org/dataset/nakuru-impact-results-wom/resource/1643d851-7239-45e7-a47b-06dfdba11a4d
  format: GeoJSON (geojson)
  id: resource_impact_sng
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Nakuru Impact Results - WOM
risk_data_type:
- hazard
- exposure
- vulnerability
- loss
schema: rdl-03
slug: rdls_hevl-kentmrwcities_nakuru
spatial:
  bbox:
  - 36.05
  - -0.35
  - 36.15
  - -0.25
  countries:
  - KEN
  gazetteer_entries:
  - description: Kenya
    id: gazetteer_1
    scheme: GEONAMES
    uri: https://www.geonames.org/192950/kenya.html
  - description: Nakuru
    id: gazetteer_2
    scheme: GEONAMES
    uri: https://www.geonames.org/184622/nakuru.html
  scale: sub-national
title: Tomorrow's Cities Flood Risk Assessment Dataset for Nakuru, Kenya
version: '1'
vulnerability:
  approach: ''
  base_data_type: ''
  category: ''
  dimension: ''
  function_type: ''
  hazard_analysis_type: ''
  hazard_primary: ''
  hazard_process_primary: ''
  hazard_process_secondary: ''
  hazard_secondary: ''
  intensity: ''
  metric: ''
  relationship: ''
  taxonomy: ''
  unit: ''
---
