---
attributions:
- entity:
    affiliation: null
    email: press@ukri.org
    name: Natural Environment Research Council (NERC)
    url: https://www.ukri.org/councils/nerc/
  id: attribution_funder
  role: funder
- entity:
    affiliation: null
    email: servicedesk@ucl.ac.uk
    name: University College London
    url: https://www.ucl.ac.uk/
  id: attribution_collaborator
  role: collaborator
catalog: null
contact_point:
  affiliation: null
  email: emin.mentese@anofa.co
  name: "Mente\u015Fe, E.Y. - Anofa Engineering, Planning and Informatics Ltd."
  url: https://orcid.org/0000-0002-7187-4384
creator:
  affiliation: null
  email: support@tomorrowscities.org
  name: Tomorrow's Cities
  url: https://data.tomorrowscities.org/
dataset_id: rdls_hevl-ken_tmrwcities_nakuru
description: Flood risk data package for Nakuru, Kenya, providing a flood hazard map
  (image-only PNG, no numerical raster), synthetic future urban exposure datasets
  (buildings, households, individuals, land use, road networks) for four community
  planning scenarios (FBO, RES, SNG, WOM), and flood impact assessment results including
  building damage, road disruption, hospital accessibility, power availability, and
  casualties. Developed as part of the Tomorrow's Cities GCRF Urban Disaster Risk
  Hub project for risk-informed decision making in urban planning.
details: 'The dataset includes: (i) flood hazard PNG map visualisation (13.5 MB) -
  critical limitation: no numerical flood depth raster or vector data is provided,
  only an image; (ii) four future exposure dataset variants representing different
  community planning scenarios (FBO: Faith-Based Organisations, RES: Residents, SNG:
  Sub-National Government, WOM: Women), each containing building footprints in GeoJSON
  and Shapefile (34,261 buildings, 255 typologies including Steel material) with rich
  attributes (OccBld, lrstype, CodeLevel, nstoreys, unit_price), household data (89,951
  households), individual demographics, road network (642 edges with bridge types),
  and land use plans (47 zones, 22 categories); and (iii) impact results per scenario
  including building damage states, casualties, hospital accessibility, power availability,
  and road edge damage. Note: WOM impact results appear to be missing from the dataset.'
exposure:
- asset_type:
    description: Building exposure classified using the GEM Global Exposure Database
      for All (GED4ALL) taxonomy, sourced from OpenStreetMap building footprints
    id: bui
    scheme: GED4ALL
    title: Building taxonomy
    uri: https://wiki.openstreetmap.org/wiki/GED4ALL
  category: buildings
  id: exposure_buildings
  metrics:
  - dimension: structure
    id: metric_building_count
    measurement:
      quantity_kind: count
      unit: count
  - dimension: structure
    id: metric_building_replacement_value
    measurement:
      quantity_kind: currency
      unit: null
  - dimension: structure
    id: metric_building_footprint_area
    measurement:
      quantity_kind: area
      unit: square_metre
- asset_type:
    description: Synthetic population derived from census household data using the
      Tomorrow's Cities DST population generation algorithm
    id: sei-pop
    scheme: GED4ALL
    title: Population exposure model
    uri: https://wiki.openstreetmap.org/wiki/GED4ALL
  category: population
  id: exposure_population
  metrics:
  - dimension: population
    id: metric_population_residents
    measurement:
      quantity_kind: count
      unit: count
  - dimension: population
    id: metric_population_households
    measurement:
      quantity_kind: count
      unit: count
  - dimension: population
    id: metric_population_individuals
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Road network infrastructure derived from OpenStreetMap, classified
      per GED4ALL infrastructure exposure framework
    id: trs-rod
    scheme: GED4ALL
    title: Infrastructure exposure - road network
    uri: https://wiki.openstreetmap.org/wiki/GED4ALL
  category: infrastructure
  id: exposure_infrastructure_roads
  metrics:
  - dimension: structure
    id: metric_road_length
    measurement:
      quantity_kind: length
      unit: metre
  - dimension: structure
    id: metric_road_edge_count
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Urban land use classification areas classified per GED4ALL exposure
      framework
    id: land_use_zones
    scheme: null
    title: Land use exposure
    uri: https://wiki.openstreetmap.org/wiki/GED4ALL
  category: economic_indicator
  id: exposure_landuse
  metrics:
  - dimension: structure
    id: metric_landuse_area
    measurement:
      quantity_kind: area
      unit: hectare
hazard:
  event_sets_by_hazard_type:
    flood:
    - analysis_type: deterministic
      calculation_method: simulated
      event_count: 1
      events:
      - calculation_method: simulated
        description: 'Flood hazard map for Nakuru provided as PNG image only (FloodHazardMap.png,
          13.5 MB). Critical limitation: no numerical flood depth raster or vector
          data available - flood depths cannot be extracted for quantitative risk
          assessment. Impact results reference flood damage but hazard is only a visual
          map.'
        disaster_identifiers: []
        hazard:
          classification: null
          id: hazard_flood
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: event_flood_nakuru
        occurrence:
          deterministic:
            description: null
            index_criteria: Scenario-based deterministic analysis - return period
              and parameters undocumented
            thresholds: null
          empirical: null
          probabilistic: null
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_flood
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_set_flood_nakuru
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/publicdomain/zero/1.0/
lineage:
  description: Integrated multi-hazard risk dataset produced by the Tomorrow's Cities
    GCRF Urban Disaster Risk Hub. OpenStreetMap building footprints were classified
    by construction type, occupancy, and number of storeys and enriched with replacement
    value estimates. A synthetic population was generated from census data using the
    agent-based algorithm of Calderon and Silva (2023, doi:10.1016/j.ijdrr.2023.103651),
    disaggregating individuals to buildings via household composition models. Earthquake
    hazard scenarios were simulated using OpenQuake-based GMPE ensembles (Weatherill
    et al. 2022). Flood hazard maps were derived from NASADEM-based hydrodynamic modelling.
    Earthquake building fragility functions and road/infrastructure fragility functions
    were adapted from HAZUS guidelines; flood depth-damage vulnerability functions
    from the JRC European flood damage database.
  sources:
  - id: source_1
    license: https://opendatacommons.org/licenses/odbl/1-0/
    name: OpenStreetMap building footprints
    risk_data_type: null
    type: dataset
    url: https://www.openstreetmap.org/
    used_in: exposure
  - id: source_2
    license: null
    name: Synthetic population generation algorithm
    risk_data_type: null
    type: model
    url: https://doi.org/10.1016/j.ijdrr.2023.103651
    used_in: exposure
  - id: source_3
    license: null
    name: Flood hazard map
    risk_data_type: null
    type: model
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Building damage state results from flood impact assessment for community
      planning scenarios (FBO, RES, SNG). WOM impact results not available.
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_flood_buildings
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: damage
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: deterministic
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Casualty results from flood impact assessment for each community
      planning scenario.
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_flood_casualties
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: casualty_count
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: deterministic
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: Road network damage from flood impact assessment (642 road edges
      with damage state and bridge type attributes).
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_flood_infrastructure
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: damage
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: deterministic
      loss_type: ground_up
  - asset_category: population
    asset_dimension: disruption
    description: Hospital accessibility and power availability impacts from flood.
      Each building has hospital_access and has_power boolean attributes.
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_flood_indirect
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: downtime
        modelling: simulated
        type: indirect
      loss_approach: analytical
      loss_frequency_type: deterministic
      loss_type: ground_up
project:
  name: Tomorrow's Cities - GCRF Urban Disaster Risk Hub
  url: https://tomorrowscities.org/
publisher:
  affiliation: null
  email: support@tomorrowscities.org
  name: Tomorrow's Cities
  url: https://data.tomorrowscities.org/
purpose: To support flood risk assessment and risk-informed urban planning decision
  making for Nakuru by providing spatial hazard visualisation, synthetic future exposure,
  and impact assessment datasets for participatory community planning scenarios.
referenced_by:
- author_names:
  - Gemma Cremen
  - Carmine Galasso
  - John McCloskey
  - Alejandro Barcena
  - Maggie Creed
  - Maria Evangelina Filippi
  - Roberto Gentile
  - Luke T. Jenkins
  - Mehmet Kalaycioglu
  - Emin Yahya Mentese
  - Manoranjan Muthusamy
  - Karim Tarbali
  - "Robert \u0160aki\u0107 Trogrli\u0107"
  date_published: '2022-12-29'
  doi: https://doi.org/10.1016/j.ijdrr.2022.103400
  id: reference_1
  name: A state-of-the-art decision-support environment for risk-sensitive and pro-poor
    urban planning and design in Tomorrow's cities
  url: https://www.sciencedirect.com/science/article/pii/S2212420922006197
- author_names:
  - "Emin Yahya Mente\u015Fe"
  - Gemma Cremen
  - Roberto Gentile
  - Carmine Galasso
  - Maria Evangelina Filippi
  - John McCloskey
  date_published: '2023-03-27'
  doi: https://doi.org/10.1016/j.ijdrr.2023.103651
  id: reference_2
  name: Future exposure modelling for risk-informed decision making in urban planning
  url: https://www.sciencedirect.com/science/article/pii/S2212420923001310
resources:
- access_url: https://data.tomorrowscities.org/dataset/nakuru-multi-hazard-dataset
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Flood hazard dataset containing a flood hazard map image (FloodHazardMap.png,
    13.5 MB). Critical limitation: only PNG visualisation - no numerical GeoTIFF or
    GeoJSON flood depth raster is available.'
  download_url: https://data.tomorrowscities.org/dataset/nakuru-multi-hazard-dataset/resource/cd00fa68-8d74-409a-b757-0b39e144b119
  format: null
  id: resource_hazard_multihazard
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Nakuru Multi Hazard Dataset
- access_url: https://data.tomorrowscities.org/dataset/nakuru-future-exposure-dataset-fbo
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Faith-Based Organisations planning
    scenario, including building footprints (34,261 buildings, 255 typologies) with
    rich attributes (OccBld, lrstype, CodeLevel, nstoreys, unit_price), household
    data (89,951 households), individual demographics, road network (642 edges), and
    land use plan (47 zones). Data formats: GeoJSON, Shapefile, JSON, XLSX, PNG.'
  download_url: https://data.tomorrowscities.org/dataset/nakuru-future-exposure-dataset-fbo/resource/c7b7189c-3527-4fef-be66-90477e727e11
  format: null
  id: resource_exposure_fbo
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal:
    central_year: null
    duration: P50Y
    end: null
    start: null
  temporal_resolution: null
  title: Nakuru Future Exposure Dataset - FBO
- access_url: https://data.tomorrowscities.org/dataset/nakuru-future-exposure-dataset-res
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Residents planning scenario. Data
    formats: GeoJSON, Shapefile, JSON, XLSX.'
  download_url: https://data.tomorrowscities.org/dataset/nakuru-future-exposure-dataset-res/resource/cbfc7d35-95f6-41bd-8647-c847b41b0fcf
  format: null
  id: resource_exposure_res
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal:
    central_year: null
    duration: P50Y
    end: null
    start: null
  temporal_resolution: null
  title: Nakuru Future Exposure Dataset - RES
- access_url: https://data.tomorrowscities.org/dataset/nakuru-future-exposure-dataset-sng
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Single/Non-Governmental planning
    scenario. Data formats: GeoJSON, Shapefile, JSON, XLSX.'
  download_url: https://data.tomorrowscities.org/dataset/nakuru-future-exposure-dataset-sng/resource/5b21b5ad-2f47-4bcc-8014-6306f1659358
  format: null
  id: resource_exposure_sng
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal:
    central_year: null
    duration: P50Y
    end: null
    start: null
  temporal_resolution: null
  title: Nakuru Future Exposure Dataset - SNG
- access_url: https://data.tomorrowscities.org/dataset/nakuru-future-exposure-dataset-wom
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Women planning scenario. Data formats:
    GeoJSON, Shapefile, JSON, XLSX.'
  download_url: https://data.tomorrowscities.org/dataset/nakuru-future-exposure-dataset-wom/resource/a0f77693-86c5-4eee-b7f4-e5da246c7fe2
  format: null
  id: resource_exposure_wom
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal:
    central_year: null
    duration: P50Y
    end: null
    start: null
  temporal_resolution: null
  title: Nakuru Future Exposure Dataset - WOM
- access_url: https://data.tomorrowscities.org/dataset/nakuru-impact-results-fbo
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Flood impact results for Faith-Based Organisations scenario including
    building damage, casualties, hospital accessibility, power availability, and road
    damage. Data format: GeoJSON.'
  download_url: https://data.tomorrowscities.org/dataset/nakuru-impact-results-fbo/resource/bdc3f70b-4808-4665-a084-8225a6d5d7ec
  format: null
  id: resource_impact_fbo
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Nakuru Impact Results - FBO
- access_url: https://data.tomorrowscities.org/dataset/nakuru-impact-results-res
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Flood impact results for Residents scenario. Data format: GeoJSON.'
  download_url: https://data.tomorrowscities.org/dataset/nakuru-impact-results-res/resource/c31c8e73-f934-4e62-81ad-3e6ce2a5e87f
  format: null
  id: resource_impact_res
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Nakuru Impact Results - RES
- access_url: https://data.tomorrowscities.org/dataset/nakuru-impact-results-sng
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Flood impact results for Sub-National Government scenario. Data format:
    GeoJSON.'
  download_url: https://data.tomorrowscities.org/dataset/nakuru-impact-results-sng/resource/9ec3523d-31bb-41dd-b8ee-7ae4b9b37437
  format: null
  id: resource_impact_sng
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Nakuru Impact Results - SNG
- access_url: https://data.tomorrowscities.org/dataset/nakuru-impact-results-wom
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Flood impact results for Women scenario. Data format: GeoJSON.'
  download_url: https://data.tomorrowscities.org/dataset/nakuru-impact-results-wom/resource/1643d851-7239-45e7-a47b-06dfdba11a4d
  format: null
  id: resource_impact_sng
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Nakuru Impact Results - WOM
risk_data_type:
- hazard
- exposure
- vulnerability
- loss
schema: rdls-10
slug: rdls_hevl-ken_tmrwcities_nakuru
spatial:
  bbox:
  - 36.05
  - -0.35
  - 36.15
  - -0.25
  centroid: null
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
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Tomorrow's Cities Flood Risk Assessment Dataset for Nakuru, Kenya
version: '1'
vulnerability: null
---
