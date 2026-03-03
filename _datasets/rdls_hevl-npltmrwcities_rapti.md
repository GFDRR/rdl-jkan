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
dataset_id: rdls_hevl-npltmrwcities_rapti
description: 'Multi-hazard risk data package for Rapti Municipality, Lumbini Province,
  Nepal, providing earthquake hazard (3 scenario GeoTIFFs: Nepal-Bihar, 2015 Gorkha
  Mw 7.8, 1505 AD), flood hazard (20-year and 70-year return period future climate
  GeoTIFFs), landslide susceptibility (current and future with extended variants covering
  power nodes), synthetic future urban exposure datasets (buildings, households, individuals,
  land use, road networks, power networks) for six ethnicity-based community planning
  scenarios (Ethnic, Madhesi, Pahadi, Planners, Squatter, Tharu), vulnerability/fragility
  functions for earthquake, flood, and landslide, and comprehensive multi-hazard impact
  assessment results. Developed as part of the Tomorrow''s Cities GCRF Urban Disaster
  Risk Hub project for risk-informed decision making in urban planning.'
details: "The dataset includes: (i) earthquake hazard GeoTIFFs for three scenarios\
  \ \u2014 Nepal-Bihar earthquake, 2015 Gorkha Mw 7.8 replay, and historical 1505\
  \ AD earthquake \u2014 plus a composite multiband intensity raster; (ii) flood hazard\
  \ GeoTIFFs for 20-year and 70-year return periods under future climate conditions\
  \ (precipitation increases of +173mm and +212mm respectively); (iii) landslide susceptibility\
  \ rasters for current and future conditions, each with base and extended variants\
  \ (extended covers 3 power nodes); (iv) vulnerability/fragility functions: earthquake\
  \ fragility for 54 building typologies (period-dependent, 4 damage states), 18 power\
  \ types (HAZUS), road fragility; flood depth-damage vulnerability; and landslide\
  \ fragility for 51 entries (typology \xD7 susceptibility with minor/moderate/severe\
  \ damage); (v) six future exposure dataset variants representing ethnic/caste-based\
  \ planning scenarios, each containing building footprints (10,945 buildings, 352\
  \ typologies), household data (32,944 households), individual demographics, land\
  \ use plans (905 zones, 48 categories), road network (3,659 edges), and power network\
  \ (2 transmission lines, 3 substations); and (vi) impact results for all 7 hazard\
  \ combinations (3 EQ cases + 2 flood RPs + 2 landslide temporal) per scenario, with\
  \ zone-aggregated XLSX summaries."
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
  calculation_method: inferred, simulated
  disaster_identifiers: ''
  hazard_analysis_type: deterministic, probabilistic
  hazard_type: earthquake, flood, landslide
  intensity: PGA:g, susceptibility, wd:m
  occurrence_range: ''
  processes: fluvial_flood, ground_motion, landslide_general
  seasonality: ''
license: CC0-1.0
loss:
  approach: ''
  base_data_type: ''
  category: ''
  description: Building damage state results from earthquake impact assessment for
    3 scenarios (Nepal-Bihar, Gorkha, 1505 AD) and each community planning scenario
    (Ethnic, Madhesi, Pahadi, Planners, Squatter, Tharu)., Building damage state results
    from flood impact assessment for 20-year and 70-year return periods under future
    climate conditions., Building damage state results from landslide assessment for
    current and future susceptibility conditions., Casualty results from earthquake
    impact assessment for each scenario combination., Hospital accessibility and power
    availability impacts from earthquake, flood, and landslide hazards. Each building
    has hospital_access and has_power boolean attributes., Road and power network
    damage from earthquake assessment., Road network damage from flood impact assessment.
  dimension: ''
  exposure_id: ''
  hazard_analysis_type: ''
  hazard_id: ''
  hazard_process: fluvial_flood, ground_motion, landslide_general
  hazard_type: earthquake, flood, landslide
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
  decision making for Rapti Municipality by providing spatial hazard, synthetic future
  exposure, vulnerability functions, and impact assessment datasets for participatory
  community planning scenarios representing diverse ethnic/caste communities.
resources:
- coordinate_system: EPSG:4326
  description: "Multi-hazard dataset containing: (1) 3 earthquake scenario GeoTIFFs\
    \ (Nepal-Bihar, Gorkha, 1505 AD) plus composite multiband raster; (2) 2 flood\
    \ GeoTIFFs for 20yr and 70yr return periods under future climate; (3) 4 landslide\
    \ susceptibility GeoTIFFs (current/future \xD7 base/extended); (4) Vulnerability/fragility\
    \ functions for earthquake (54 building + 18 power + road typologies), flood,\
    \ and landslide (51 entries). Data formats: GeoTIFF, XLSX, TXT."
  download_url: https://data.tomorrowscities.org/dataset/rapti-multi-hazard-dataset/resource/0c4b41ab-8e04-4073-83ad-a0bdcc313c34
  format: GeoTIFF (tif)
  id: resource_hazard_multihazard
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Rapti Multi Hazard Dataset
- coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Ethnic minority community planning
    scenario, including building footprints (10,945 buildings, 352 typologies) with
    rich attributes (OccBld, lrstype, CodeLevel, nstoreys, unit_price), household
    data (32,944 households), individual demographics, land use plan (905 zones, 48
    categories), road network (3,659 edges), and power network (2 edges, 3 nodes).
    Data formats: GeoJSON for spatial data, JSON for tabular data.'
  download_url: https://data.tomorrowscities.org/dataset/rapti-future-exposure-dataset-ethnic/resource/d0204033-f8ad-4afd-a944-a5b242db152a
  format: GeoJSON (geojson)
  id: resource_exposure_ethnic
  media_type: null
  spatial_resolution: null
  temporal:
    duration: P50Y
    end: null
    start: null
    temporal_resolution: null
  title: Rapti Future Exposure Dataset - Ethnic
- coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Madhesi community planning scenario.
    Data formats: GeoJSON, JSON.'
  download_url: https://data.tomorrowscities.org/dataset/rapti-future-exposure-dataset-madhesi/resource/e7d1489e-2776-4783-8bcc-4eaef7e8dc2a
  format: GeoJSON (geojson)
  id: resource_exposure_madhesi
  media_type: null
  spatial_resolution: null
  temporal:
    duration: P50Y
    end: null
    start: null
    temporal_resolution: null
  title: Rapti Future Exposure Dataset - Madhesi
- coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Pahadi community planning scenario.
    Data formats: GeoJSON, JSON.'
  download_url: https://data.tomorrowscities.org/dataset/rapti-future-exposure-dataset-pahadi/resource/628371c4-7b70-4be7-9b8d-d0e4338b60f2
  format: GeoJSON (geojson)
  id: resource_exposure_pahadi
  media_type: null
  spatial_resolution: null
  temporal:
    duration: P50Y
    end: null
    start: null
    temporal_resolution: null
  title: Rapti Future Exposure Dataset - Pahadi
- coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for urban Planners optimal scenario.
    Data formats: GeoJSON, JSON.'
  download_url: https://data.tomorrowscities.org/dataset/rapti-future-exposure-dataset-planners/resource/e8c5de85-f084-4fba-a2b9-e619207da873
  format: GeoJSON (geojson)
  id: resource_exposure_planners
  media_type: null
  spatial_resolution: null
  temporal:
    duration: P50Y
    end: null
    start: null
    temporal_resolution: null
  title: Rapti Future Exposure Dataset - Planners
- coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Squatter/informal settlement community
    planning scenario. Data formats: GeoJSON, JSON.'
  download_url: https://data.tomorrowscities.org/dataset/rapti-future-exposure-dataset-squatter/resource/757d3097-c837-48ee-ae49-53b0f0280f38
  format: GeoJSON (geojson)
  id: resource_exposure_squatter
  media_type: null
  spatial_resolution: null
  temporal:
    duration: P50Y
    end: null
    start: null
    temporal_resolution: null
  title: Rapti Future Exposure Dataset - Squatter
- coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Tharu indigenous community planning
    scenario. Data formats: GeoJSON, JSON.'
  download_url: https://data.tomorrowscities.org/dataset/rapti-future-exposure-dataset-tharu/resource/ad747579-6c20-444f-858d-7ac78ed78ef3
  format: GeoJSON (geojson)
  id: resource_exposure_tharu
  media_type: null
  spatial_resolution: null
  temporal:
    duration: P50Y
    end: null
    start: null
    temporal_resolution: null
  title: Rapti Future Exposure Dataset - Tharu
- coordinate_system: EPSG:4326
  description: 'Multi-hazard impact results for Ethnic scenario including 7 hazard
    GeoJSONs (3 EQ cases + 2 flood RPs + 2 landslide temporal) and zone-aggregated
    XLSX summaries. Data formats: GeoJSON, XLSX.'
  download_url: https://data.tomorrowscities.org/dataset/rapti-impact-results-ethnic/resource/c4469a4c-cc5d-4baf-a9d4-c03f40605d47
  format: GeoJSON (geojson)
  id: resource_impact_ethnic
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Rapti Impact Results - Ethnic
- coordinate_system: EPSG:4326
  description: 'Multi-hazard impact results for Madhesi scenario. Data formats: GeoJSON,
    XLSX.'
  download_url: https://data.tomorrowscities.org/dataset/rapti-impact-results-madhesi/resource/920c35e4-12c5-4c6f-bdf6-9a98f4aeb73d
  format: GeoJSON (geojson)
  id: resource_impact_madhesi
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Rapti Impact Results - Madhesi
- coordinate_system: EPSG:4326
  description: 'Multi-hazard impact results for Pahadi scenario. Data formats: GeoJSON,
    XLSX.'
  download_url: https://data.tomorrowscities.org/dataset/rapti-impact-results-pahadi/resource/63333717-81ba-4c8d-a01d-9361b114f31f
  format: GeoJSON (geojson)
  id: resource_impact_pahadi
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Rapti Impact Results - Pahadi
- coordinate_system: EPSG:4326
  description: 'Multi-hazard impact results for Planners scenario. Data formats: GeoJSON,
    XLSX.'
  download_url: https://data.tomorrowscities.org/dataset/rapti-impact-results-planners/resource/43b92857-26d8-45f2-891c-6cad599ef208
  format: GeoJSON (geojson)
  id: resource_impact_planners
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Rapti Impact Results - Planners
- coordinate_system: EPSG:4326
  description: 'Multi-hazard impact results for Squatter scenario. Data formats: GeoJSON,
    XLSX.'
  download_url: https://data.tomorrowscities.org/dataset/rapti-impact-results-squatter/resource/a1c0920e-2b90-41ab-8cf9-501d793e5911
  format: GeoJSON (geojson)
  id: resource_impact_squatter
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Rapti Impact Results - Squatter
- coordinate_system: EPSG:4326
  description: 'Multi-hazard impact results for Tharu scenario. Data formats: GeoJSON,
    XLSX.'
  download_url: https://data.tomorrowscities.org/dataset/rapti-impact-results-tharu/resource/240eec13-11e5-4e4d-85d8-ca3f3d3aa9d5
  format: GeoJSON (geojson)
  id: resource_impact_tharu
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Rapti Impact Results - Tharu
risk_data_type:
- hazard
- exposure
- vulnerability
- loss
schema: rdl-03
slug: rdls_hevl-npltmrwcities_rapti
spatial:
  bbox:
  - 82.6
  - 27.8
  - 82.75
  - 27.95
  countries:
  - NPL
  gazetteer_entries:
  - description: Nepal
    id: gazetteer_1
    scheme: GEONAMES
    uri: https://www.geonames.org/1282988/nepal.html
  - description: Lumbini Province
    id: gazetteer_2
    scheme: GEONAMES
    uri: https://www.geonames.org/12587039/lumbini-province.html
  - description: Rapti
    id: gazetteer_3
    scheme: GEONAMES
    uri: https://www.geonames.org/1282898/rapti.html
  scale: sub-national
title: Tomorrow's Cities Multi-Hazard Risk Assessment Dataset for Rapti Municipality,
  Nepal
version: '1'
vulnerability:
  approach: analytical, empirical
  base_data_type: simulated
  category: buildings, infrastructure
  dimension: ''
  function_type: ''
  hazard_analysis_type: deterministic, probabilistic
  hazard_primary: earthquake, flood, landslide
  hazard_process_primary: fluvial_flood, ground_motion, landslide_general
  hazard_process_secondary: ''
  hazard_secondary: ''
  intensity: ''
  metric: damage_ratio
  relationship: discrete, math_parametric
  taxonomy: Custom, HAZUS
  unit: ''
---
