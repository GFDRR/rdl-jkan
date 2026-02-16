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
dataset_id: rdls_hevl-psetmrwcities_nablus
description: Multi-hazard risk data package for Nablus, West Bank, Palestine, providing
  earthquake hazard (single rupture scenario rup4 with multiband ground motion raster),
  flood hazard (future high-emission climate scenario depth map), earthquake-triggered
  landslide hazard, synthetic future urban exposure datasets (buildings, households,
  individuals, land use) for five community planning scenarios (Apartment Buildings,
  Civil Societies, Community Service, Women, Youth), vulnerability/fragility functions
  for buildings, roads, and power infrastructure (OpenQuake NRML format), and multi-hazard
  impact assessment results. Developed as part of the Tomorrow's Cities GCRF Urban
  Disaster Risk Hub project for risk-informed decision making in urban planning.
details: 'The dataset includes: (i) earthquake hazard multiband GeoTIFF (multi-band-rup4.tif)
  with ground motion intensity measures for rupture scenario 4, structural fragility
  in OpenQuake NRML 0.5 discrete format with PGA intensity measure and 4 damage states
  (slight, moderate, extensive, complete) using GEM Building Taxonomy v2.0, power
  fragility for 18 infrastructure types, and road fragility for 29 types; (ii) flood
  depth GeoTIFF (future high-emission climate scenario YVS) with depth-damage vulnerability
  functions for 91 building typologies at 9 water depths; (iii) earthquake-triggered
  landslide raster (eq-landslide-rup4.tif); (iv) five future exposure dataset variants
  representing different community planning scenarios, each containing building footprints
  (3,631 buildings, 80 typologies in GEM Taxonomy v2.0 format), household data, individual
  demographics, and land use plans (35 zones, 15 categories); and (v) multi-hazard
  impact results for earthquake, flood, and landslide per scenario including building
  damage states, casualties, hospital accessibility, power availability, and road
  network disruption.'
exposure:
- category: buildings
  dimension: structure
  quantity_kind: area, count, currency
  taxonomy: Custom
- category: population
  dimension: population
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
  description: 'Building damage state results from earthquake impact assessment for
    each community planning scenario (Apartment Buildings, Civil Societies, Community
    Service, Women, Youth)., Building damage state results from earthquake-triggered
    landslide assessment. Note: All buildings currently show DS=0 (no landslide damage)
    in available results., Building damage state results from flood impact assessment
    for each community planning scenario., Casualty results from earthquake impact
    assessment for each community planning scenario., Hospital accessibility and power
    availability impacts from earthquake and flood, derived from road network connectivity
    analysis and power network damage assessment. Each building has hospital_access
    and has_power boolean attributes., Road network and power infrastructure damage
    from earthquake impact assessment, including road edge and node damage states.,
    Road network damage from flood impact assessment, with road edges flagged as damaged/undamaged
    based on flood inundation.'
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
  decision making for Nablus by providing spatial hazard, synthetic future exposure,
  vulnerability functions, and impact assessment datasets for participatory community
  planning scenarios.
resources:
- coordinate_system: EPSG:4326
  description: 'Multi-hazard dataset containing: (1) Earthquake multiband GeoTIFF
    for rup4 scenario with ground motion IMs; (2) OpenQuake NRML structural fragility
    XML (discrete, PGA, 4 DS), power fragility (18 types), road fragility (29 types);
    (3) Future high-emission flood depth GeoTIFF (YVS scenario) with vulnerability
    functions for 91 typologies; Data formats: GeoTIFF, XML, XLSX.'
  download_url: https://data.tomorrowscities.org/dataset/nablus-multi-hazard-dataset/resource/a4aac9d1-7ccb-4dcf-af98-234641fbdc75
  format: GeoTIFF (tif)
  id: resource_hazard_multihazard
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Nablus Multi Hazard Dataset
- coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Apartment Buildings community planning
    scenario, including building footprints (3,631 buildings, 80 typologies in GEM
    Taxonomy v2.0) with structural attributes, household data (9,704 households),
    individual demographics (59,580 individuals), and land use plan (35 zones). Data
    formats: GeoJSON for spatial data, JSON and XLSX for tabular data.'
  download_url: https://data.tomorrowscities.org/dataset/nablus-future-exposure-dataset-apartment-buildings/resource/b9a2a521-4b99-48b2-ba16-fc50ba9dc279
  format: GeoJSON (geojson)
  id: resource_exposure_apartment_buildings
  media_type: null
  spatial_resolution: null
  temporal:
    duration: P50Y
    end: null
    start: null
    temporal_resolution: null
  title: Nablus Future Exposure Dataset - Apartment Buildings
- coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Civil Societies community planning
    scenario, including building footprints with structural taxonomy, household data,
    individual demographics, and land use plan. Data formats: GeoJSON, JSON, XLSX.'
  download_url: https://data.tomorrowscities.org/dataset/nablus-future-exposure-dataset-civil-societies/resource/76a0adc4-947a-4037-8cc2-a20f78540d45
  format: GeoJSON (geojson)
  id: resource_exposure_civil_societies
  media_type: null
  spatial_resolution: null
  temporal:
    duration: P50Y
    end: null
    start: null
    temporal_resolution: null
  title: Nablus Future Exposure Dataset - Civil Societies
- coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Community Service planning scenario,
    including building footprints with structural taxonomy, household data, individual
    demographics, and land use plan. Data formats: GeoJSON, JSON, XLSX.'
  download_url: https://data.tomorrowscities.org/dataset/nablus-future-exposure-dataset-community-service/resource/7663f6dd-b8f5-4e20-8450-1705fab1f992
  format: GeoJSON (geojson)
  id: resource_exposure_community_service
  media_type: null
  spatial_resolution: null
  temporal:
    duration: P50Y
    end: null
    start: null
    temporal_resolution: null
  title: Nablus Future Exposure Dataset - Community Service
- coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Women community planning scenario,
    including building footprints with structural taxonomy, household data, individual
    demographics, and land use plan. Data formats: GeoJSON, JSON, XLSX.'
  download_url: https://data.tomorrowscities.org/dataset/nablus-future-exposure-dataset-women/resource/b4558674-4acf-43b3-b7ef-02b6ff6a63f0
  format: GeoJSON (geojson)
  id: resource_exposure_women
  media_type: null
  spatial_resolution: null
  temporal:
    duration: P50Y
    end: null
    start: null
    temporal_resolution: null
  title: Nablus Future Exposure Dataset - Women
- coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Youth community planning scenario,
    including building footprints with structural taxonomy, household data, individual
    demographics, and land use plan. Data formats: GeoJSON, JSON, XLSX.'
  download_url: https://data.tomorrowscities.org/dataset/nablus-future-exposure-dataset-youth/resource/38366625-3e58-4137-bea7-0b67ddce4888
  format: GeoJSON (geojson)
  id: resource_exposure_youth
  media_type: null
  spatial_resolution: null
  temporal:
    duration: P50Y
    end: null
    start: null
    temporal_resolution: null
  title: Nablus Future Exposure Dataset - Youth
- coordinate_system: EPSG:4326
  description: 'Multi-hazard impact assessment results for Apartment Buildings scenario,
    including earthquake, flood, and landslide building damage states, casualties,
    hospital accessibility, power availability, and road network disruption. Data
    formats: GeoJSON, GeoTIFF.'
  download_url: https://data.tomorrowscities.org/dataset/nablus-impact-results-apartment-buildings/resource/223813ce-e9ae-4a15-875b-b48cbfef4a2c
  format: GeoJSON (geojson)
  id: resource_impact_apartment_buildings
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Nablus Impact Results - Apartment Buildings
- coordinate_system: EPSG:4326
  description: 'Multi-hazard impact assessment results for Civil Societies scenario.
    Data formats: GeoJSON, GeoTIFF.'
  download_url: https://data.tomorrowscities.org/dataset/nablus-impact-results-civil-societies/resource/c468a110-1e7f-48b8-83b3-61ea0a2ddfcd
  format: GeoJSON (geojson)
  id: resource_impact_civil_societies
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Nablus Impact Results - Civil Societies
- coordinate_system: EPSG:4326
  description: 'Multi-hazard impact assessment results for Community Service scenario.
    Data formats: GeoJSON, GeoTIFF.'
  download_url: https://data.tomorrowscities.org/dataset/nablus-impact-results-community-service/resource/3831127e-f092-4492-ac8b-b680d2868d48
  format: GeoJSON (geojson)
  id: resource_impact_community_service
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Nablus Impact Results - Community Service
- coordinate_system: EPSG:4326
  description: 'Multi-hazard impact assessment results for Women scenario. Data formats:
    GeoJSON, GeoTIFF.'
  download_url: https://data.tomorrowscities.org/dataset/nablus-impact-results-women/resource/6b321b7a-a33e-4513-83ed-95caf84ef89a
  format: GeoJSON (geojson)
  id: resource_impact_women
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Nablus Impact Results - Women
- coordinate_system: EPSG:4326
  description: 'Multi-hazard impact assessment results for Youth scenario. Data formats:
    GeoJSON, GeoTIFF.'
  download_url: https://data.tomorrowscities.org/dataset/nablus-impact-results-youth/resource/b46d7d8d-9e2f-4c4f-a171-cd9e4c708889
  format: GeoJSON (geojson)
  id: resource_impact_youth
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Nablus Impact Results - Youth
risk_data_type:
- hazard
- exposure
- vulnerability
- loss
schema: rdl-03
slug: rdls_hevl-psetmrwcities_nablus
spatial:
  bbox:
  - 35.22
  - 32.19
  - 35.3
  - 32.25
  countries:
  - PSE
  gazetteer_entries:
  - description: Palestine
    id: gazetteer_1
    scheme: GEONAMES
    uri: https://www.geonames.org/6254930/palestinian-territory.html
  - description: Nablus
    id: gazetteer_2
    scheme: GEONAMES
    uri: https://www.geonames.org/282615/nablus.html
  scale: sub-national
title: Tomorrow's Cities Multi-Hazard Risk Assessment Dataset for Nablus, Palestine
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
  taxonomy: Custom
  unit: ''
---
