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
dataset_id: rdls_hevl-kentmrwcities_nairobi
description: Flood risk data package for Nairobi, Kenya, providing 100-year return
  period flood hazard (vector-based depth points), synthetic future urban exposure
  datasets (buildings, households, individuals, land use) for five community planning
  scenarios (Business, Elders, Women, Youth1, Youth2), flood depth-damage vulnerability
  functions for buildings, and flood impact assessment results. Developed as part
  of the Tomorrow's Cities GCRF Urban Disaster Risk Hub project for risk-informed
  decision making in urban planning.
details: 'The dataset includes: (i) 100-year return period flood hazard as vector
  point grid (127,422 point features) with water depth (IM) values in GeoJSON format,
  plus flood depth-damage vulnerability functions for 6,300 building typologies at
  9 water depths (0-6m) in JSON columnar format; (ii) five future exposure dataset
  variants representing different community planning scenarios, each containing building
  footprints (5,815 buildings, 116 typologies in MultiPolygon geometry) with structural
  taxonomy, household data, individual demographics, and land use plans (110 zones,
  25 categories); and (iii) flood impact results per scenario including building damage
  states, impact metrics, and nearest road node connectivity. Note: Only flood hazard
  is present despite the Multi Hazard Dataset naming. No road, power, or other infrastructure
  data in exposure datasets.'
exposure:
  category: buildings, economic_indicator, population
  dimension: population, structure
  quantity_kind: area, count, currency
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
  hazard_analysis_type: probabilistic
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
  description: Affected population results from flood impact assessment for each community
    planning scenario., Building damage state results from flood impact assessment
    for each community planning scenario (Business, Elders, Women, Youth1, Youth2).
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
  making for Nairobi by providing spatial hazard, synthetic future exposure, vulnerability
  functions, and impact assessment datasets for participatory community planning scenarios.
resources:
- coordinate_system: EPSG:4326
  description: 'Flood hazard dataset containing: (1) 100-year return period flood
    depth GeoJSON (127,422 point features with IM/depth values); (2) Flood depth-damage
    vulnerability functions for 6,300 building typologies in JSON columnar dict format.
    Note: Only flood hazard present despite Multi Hazard naming.'
  download_url: https://data.tomorrowscities.org/dataset/nairobi-multi-hazard-dataset/resource/e5f04bdc-5409-4558-874b-d79b3649a6b6
  format: GeoJSON (geojson)
  id: resource_hazard_multihazard
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Nairobi Multi Hazard Dataset
- coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Business community planning scenario,
    including building footprints (5,815 buildings, 116 typologies) with structural
    taxonomy, household data, individual demographics, and land use plan (110 zones).
    Data formats: GeoJSON for spatial data, XLSX for tabular data.'
  download_url: https://data.tomorrowscities.org/dataset/nairobi-future-exposure-dataset-business/resource/84f14e0d-0d20-42cd-9610-b79066e6e788
  format: GeoJSON (geojson)
  id: resource_exposure_business
  media_type: null
  spatial_resolution: null
  temporal:
    duration: P50Y
    end: null
    start: null
    temporal_resolution: null
  title: Nairobi Future Exposure Dataset - Business
- coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Elders community planning scenario.
    Data formats: GeoJSON, XLSX.'
  download_url: https://data.tomorrowscities.org/dataset/nairobi-future-exposure-dataset-elders/resource/8c58c990-b4ff-4067-b152-405258ddd001
  format: GeoJSON (geojson)
  id: resource_exposure_elders
  media_type: null
  spatial_resolution: null
  temporal:
    duration: P50Y
    end: null
    start: null
    temporal_resolution: null
  title: Nairobi Future Exposure Dataset - Elders
- coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Women community planning scenario.
    Data formats: GeoJSON, XLSX.'
  download_url: https://data.tomorrowscities.org/dataset/nairobi-future-exposure-dataset-women/resource/bc4e5e3e-b6bc-412c-974f-8fe33ac8f478
  format: GeoJSON (geojson)
  id: resource_exposure_women
  media_type: null
  spatial_resolution: null
  temporal:
    duration: P50Y
    end: null
    start: null
    temporal_resolution: null
  title: Nairobi Future Exposure Dataset - Women
- coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Youth Group 1 community planning
    scenario. Data formats: GeoJSON, XLSX.'
  download_url: https://data.tomorrowscities.org/dataset/nairobi-future-exposure-dataset-youth1/resource/86c505f3-95d4-4da5-bb2b-f15d85eb64c8
  format: GeoJSON (geojson)
  id: resource_exposure_youth1
  media_type: null
  spatial_resolution: null
  temporal:
    duration: P50Y
    end: null
    start: null
    temporal_resolution: null
  title: Nairobi Future Exposure Dataset - Youth1
- coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Youth Group 2 community planning
    scenario. Data formats: GeoJSON, XLSX.'
  download_url: https://data.tomorrowscities.org/dataset/nairobi-future-exposure-dataset-youth2/resource/a28e7d87-0f82-4658-80cf-ecfba8de3ad8
  format: GeoJSON (geojson)
  id: resource_exposure_youth2
  media_type: null
  spatial_resolution: null
  temporal:
    duration: P50Y
    end: null
    start: null
    temporal_resolution: null
  title: Nairobi Future Exposure Dataset - Youth2
- coordinate_system: EPSG:4326
  description: 'Flood impact assessment results for Business scenario, including building
    damage states and impact metrics. Data formats: GeoJSON, File Geodatabase (GDB).'
  download_url: https://data.tomorrowscities.org/dataset/nairobi-impact-results-business/resource/662f53c0-25b5-458a-8f8a-cbbd1eb46623
  format: File Geodatabase (gdb)
  id: resource_impact_business
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Nairobi Impact Results - Business
- coordinate_system: EPSG:4326
  description: 'Flood impact assessment results for Elders scenario. Data formats:
    GeoJSON, File Geodatabase (GDB).'
  download_url: https://data.tomorrowscities.org/dataset/nairobi-impact-results-elders/resource/7f442350-a96b-46bc-86d7-8c2646128032
  format: File Geodatabase (gdb)
  id: resource_impact_elders
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Nairobi Impact Results - Elders
- coordinate_system: EPSG:4326
  description: 'Flood impact assessment results for Women scenario. Data formats:
    GeoJSON, File Geodatabase (GDB).'
  download_url: https://data.tomorrowscities.org/dataset/nairobi-impact-results-women/resource/33925fbe-41fb-4df7-b52e-10563f421362
  format: File Geodatabase (gdb)
  id: resource_impact_women
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Nairobi Impact Results - Women
- coordinate_system: EPSG:4326
  description: 'Flood impact assessment results for Youth Group 1 scenario. Data formats:
    GeoJSON, File Geodatabase (GDB).'
  download_url: https://data.tomorrowscities.org/dataset/nairobi-impact-results-youth1/resource/5eb24c6b-9187-435e-b314-6f1e0bc28cab
  format: File Geodatabase (gdb)
  id: resource_impact_youth1
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Nairobi Impact Results - Youth1
- coordinate_system: EPSG:4326
  description: 'Flood impact assessment results for Youth Group 2 scenario. Data formats:
    GeoJSON, File Geodatabase (GDB).'
  download_url: https://data.tomorrowscities.org/dataset/nairobi-impact-results-youth2/resource/d01bba13-cd3f-4605-b518-fff9473f7bf4
  format: File Geodatabase (gdb)
  id: resource_impact_youth2
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Nairobi Impact Results - Youth2
risk_data_type:
- hazard
- exposure
- vulnerability
- loss
schema: rdl-03
slug: rdls_hevl-kentmrwcities_nairobi
spatial:
  bbox:
  - 36.8
  - -1.35
  - 36.9
  - -1.25
  countries:
  - KEN
  gazetteer_entries:
  - description: Kenya
    id: gazetteer_1
    scheme: GEONAMES
    uri: https://www.geonames.org/192950/kenya.html
  - description: Nairobi
    id: gazetteer_2
    scheme: GEONAMES
    uri: https://www.geonames.org/184745/nairobi.html
  scale: sub-national
title: Tomorrow's Cities Flood Risk Assessment Dataset for Nairobi, Kenya
version: '1'
vulnerability:
  approach: analytical
  base_data_type: simulated
  category: buildings
  dimension: ''
  function_type: ''
  hazard_analysis_type: probabilistic
  hazard_primary: flood
  hazard_process_primary: fluvial_flood
  hazard_process_secondary: ''
  hazard_secondary: ''
  intensity: ''
  metric: damage_ratio
  relationship: discrete
  taxonomy: Custom
  unit: ''
---
