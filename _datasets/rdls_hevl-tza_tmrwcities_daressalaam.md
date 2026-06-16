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
dataset_id: rdls_hevl-tza_tmrwcities_daressalaam
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
    description: Electricity network nodes and edges derived from OpenStreetMap, classified
      per GED4ALL infrastructure exposure framework
    id: pwr-lin
    scheme: GED4ALL
    title: Infrastructure exposure - power grid
    uri: https://wiki.openstreetmap.org/wiki/GED4ALL
  category: infrastructure
  id: exposure_infrastructure_power
  metrics:
  - dimension: structure
    id: metric_power_node_count
    measurement:
      quantity_kind: count
      unit: count
  - dimension: structure
    id: metric_power_edge_count
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
  event_sets:
  - analysis_type: deterministic
    calculation_method: simulated
    event_count: 2
    events:
    - calculation_method: simulated
      description: "Deterministic pluvial flood Scenario 1 for Dar es Salaam with\
        \ 7mm rainfall over 24 hours. Simulated using high-resolution solver with\
        \ Manning's n=0.06, 5m DTM (2017), breach threshold 200, minimum depth \u2265\
        0.05m. Output: water depth (m) in WGS84."
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_flood
        intensity_measure: wd:m
        process: pluvial_flood
        trigger: null
        type: flood
      id: event_flood_daressalaam_scenario1
      occurrence:
        deterministic:
          description: null
          index_criteria: Scenario-based deterministic analysis
          thresholds: null
        empirical: null
        probabilistic: null
    - calculation_method: simulated
      description: "Deterministic pluvial flood Scenario 2 for Dar es Salaam with\
        \ 19mm/hr rainfall for 6 hours (114mm total). Simulated using high-resolution\
        \ solver with Manning's n=0.06, 5m DTM (2017), breach threshold 200, minimum\
        \ depth \u22650.05m. Output: water depth (m) in WGS84."
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_flood
        intensity_measure: wd:m
        process: pluvial_flood
        trigger: null
        type: flood
      id: event_flood_daressalaam_scenario2
      occurrence:
        deterministic:
          description: null
          index_criteria: Scenario-based deterministic analysis
          thresholds: null
        empirical: null
        probabilistic: null
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: pluvial_flood
      trigger: null
      type: flood
    id: event_set_flood_daressalaam
    occurrence_range: null
    seasonality: null
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
    name: Pluvial flood hazard modelling
    risk_data_type: null
    type: model
    url: null
    used_in: hazard
  - id: source_4
    license: null
    name: Dar es Salaam Digital Terrain Model
    risk_data_type: null
    type: dataset
    url: null
    used_in: hazard
  - id: source_5
    license: null
    name: Depth-damage vulnerability functions for flood
    risk_data_type: null
    type: model
    url: https://publications.jrc.ec.europa.eu/repository/handle/JRC105688
    used_in: vulnerability
  - id: source_6
    license: null
    name: Landslide fragility functions
    risk_data_type: null
    type: model
    url: null
    used_in: vulnerability
  - id: source_7
    license: https://creativecommons.org/publicdomain/zero/1.0/
    name: HAZUS infrastructure fragility functions
    risk_data_type: null
    type: model
    url: https://www.fema.gov/flood-maps/tools-resources/flood-map-products/hazus
    used_in: vulnerability
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Building damage state results from flood impact assessment for each
      community planning scenario (Elderly, Leaders, Residents, Youth) and both flood
      scenarios. Damage states (DS0=undamaged, DS1=damaged) derived by applying depth-damage
      vulnerability functions to flood water depth hazard.
    disaster_identifiers: []
    hazard:
      classification: null
      id: null
      intensity_measure: wd:m
      process: pluvial_flood
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
      planning scenario, derived from building inundation and residential occupancy.
    disaster_identifiers: []
    hazard:
      classification: null
      id: null
      intensity_measure: wd:m
      process: pluvial_flood
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
    description: Road network damage state results from flood impact assessment, with
      road edges flagged as damaged/undamaged based on flood inundation.
    disaster_identifiers: []
    hazard:
      classification: null
      id: null
      intensity_measure: wd:m
      process: pluvial_flood
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
    description: Hospital accessibility and power availability impacts from flood,
      derived from road network connectivity analysis (road edges damaged by flooding)
      and power network assessment. Each building has hospital_access and has_power
      boolean attributes.
    disaster_identifiers: []
    hazard:
      classification: null
      id: null
      intensity_measure: wd:m
      process: pluvial_flood
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
purpose: To support multi-hazard risk assessment and risk-informed urban planning
  decision making for Dar es Salaam by providing spatial hazard, synthetic future
  exposure, vulnerability functions, and impact assessment datasets for participatory
  community planning scenarios.
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
- author_names:
  - Roberto Gentile
  - Gemma Cremen
  - Carmine Galasso
  - Luke T. Jenkins
  - Vibek Manandhar
  - "Emin Yahya Mente\u015Fe"
  - Ramesh Guragain
  - John McCloskey
  date_published: '2022-10-14'
  doi: https://doi.org/10.1016/j.ijdrr.2022.103365
  id: reference_3
  name: Scoring, selecting, and developing physical impact models for multi-hazard
    risk assessment
  url: https://www.sciencedirect.com/science/article/pii/S2212420922005842
resources:
- access_url: https://data.tomorrowscities.org/dataset/dar-multi-hazard-dataset
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Multi-hazard dataset containing: (1) Flood hazard rasters for two
    deterministic pluvial scenarios - Scenario 1 (7mm/24hr) and Scenario 2 (19mm/hr
    for 6hr) with water depth in WGS84 projection; (2) Vulnerability/fragility functions
    for buildings (7,354 flood typologies) and landslide (60 entries for buildings
    and infrastructure). Data formats: GeoTIFF for hazard rasters, Excel (XLSX) for
    vulnerability/fragility functions.'
  download_url: https://data.tomorrowscities.org/dataset/1069bf2e-b3d2-466e-bc24-306b262f475c/resource/5a8e8fc1-be1b-434f-8e34-e1a7f88b3b31/download/darmultihazarddataset.zip
  format: null
  id: resource_hazard_multihazard
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 5
  temporal: null
  temporal_resolution: null
  title: Dar es Salaam Multi Hazard Dataset
- access_url: https://data.tomorrowscities.org/dataset/dar-future-exposure-dataset-elderly
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Elderly community planning scenario,
    including building footprints with structural taxonomy (including Adobe and income
    levels), household socio-economic data, individual demographic data, land use
    plan (115 zones), road network (106 edges), and power network infrastructure (2
    substations). Data formats: GeoJSON for spatial data, XLSX for tabular data (households,
    individuals).'
  download_url: https://data.tomorrowscities.org/dataset/abde7716-e686-477c-8b86-792de010d3af/resource/aeeb8a8b-d98a-4e4b-a7b6-fbc18bd79673/download/darfutureexposuredataset_elderly.zip
  format: null
  id: resource_exposure_elderly
  media_type: application/zip
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal:
    central_year: null
    duration: P50Y
    end: null
    start: null
  temporal_resolution: null
  title: Dar es Salaam Future Exposure Dataset - Elderly
- access_url: https://data.tomorrowscities.org/dataset/dar-future-exposure-dataset-leaders
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Leaders community planning scenario,
    including building footprints with structural taxonomy (including Adobe and income
    levels), household socio-economic data, individual demographic data, land use
    plan, road network, and power network infrastructure. Data formats: GeoJSON for
    spatial data, XLSX for tabular data (households, individuals).'
  download_url: https://data.tomorrowscities.org/dataset/aafcabf8-1a11-47ce-b5e8-e543e63efe63/resource/f59a4029-f566-4362-9c24-c5d16719fa03/download/darfutureexposuredataset_leaders.zip
  format: null
  id: resource_exposure_leaders
  media_type: application/zip
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal:
    central_year: null
    duration: P50Y
    end: null
    start: null
  temporal_resolution: null
  title: Dar es Salaam Future Exposure Dataset - Leaders
- access_url: https://data.tomorrowscities.org/dataset/dar-future-exposure-dataset-residents
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Residents community planning scenario,
    including building footprints with structural taxonomy (including Adobe and income
    levels), household socio-economic data, individual demographic data, land use
    plan, road network, and power network infrastructure. Data formats: GeoJSON for
    spatial data, XLSX for tabular data (households, individuals).'
  download_url: https://data.tomorrowscities.org/dataset/3b4809d3-da30-4cfd-87fe-f1b1c81bd855/resource/d87afb73-a1fc-46ea-8d1b-aac8fdb1995d/download/darfutureexposuredataset_residents.zip
  format: null
  id: resource_exposure_residents
  media_type: application/zip
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal:
    central_year: null
    duration: P50Y
    end: null
    start: null
  temporal_resolution: null
  title: Dar es Salaam Future Exposure Dataset - Residents
- access_url: https://data.tomorrowscities.org/dataset/dar-future-exposure-dataset-youth
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Youth community planning scenario,
    including building footprints with structural taxonomy (including Adobe and income
    levels), household socio-economic data, individual demographic data, land use
    plan, road network, and power network infrastructure. Data formats: GeoJSON for
    spatial data, XLSX for tabular data (households, individuals).'
  download_url: https://data.tomorrowscities.org/dataset/60fa9b22-6c55-48d5-98e4-826ffee8923f/resource/c984310e-bdec-4051-b79e-0fd0495c7082/download/darfutureexposuredataset_youth.zip
  format: null
  id: resource_exposure_youth
  media_type: application/zip
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal:
    central_year: null
    duration: P50Y
    end: null
    start: null
  temporal_resolution: null
  title: Dar es Salaam Future Exposure Dataset - Youth
- access_url: https://data.tomorrowscities.org/dataset/dar-impact-results-elderly
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Impact assessment results for flood hazards (both scenarios) under
    the Elderly community planning scenario, including building damage states, casualties,
    hospital accessibility, power availability, and road network disruption. Data
    formats: ESRI File Geodatabase (GDB) and GeoJSON.'
  download_url: https://data.tomorrowscities.org/dataset/c4da084d-0c38-426b-8beb-f9abc21b7e33/resource/c986fb15-8350-4d60-913d-03657dccb0b2/download/darimpactresults_elderly.zip
  format: File Geodatabase (gdb)
  id: resource_impact_elderly
  media_type: null
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Dar es Salaam Impact Results - Elderly
- access_url: https://data.tomorrowscities.org/dataset/dar-impact-results-leaders
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Impact assessment results for flood hazards (both scenarios) under
    the Leaders community planning scenario, including building damage states, casualties,
    hospital accessibility, power availability, and road network disruption. Data
    formats: ESRI File Geodatabase (GDB) and GeoJSON.'
  download_url: https://data.tomorrowscities.org/dataset/a79d86bd-4ecb-475a-b7c5-5933abcd7d00/resource/a0d509ae-29aa-4fbe-b40d-f0d6535e6479/download/darimpactresults_leaders.zip
  format: File Geodatabase (gdb)
  id: resource_impact_leaders
  media_type: null
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Dar es Salaam Impact Results - Leaders
- access_url: https://data.tomorrowscities.org/dataset/dar-impact-results-residents
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Impact assessment results for flood hazards (both scenarios) under
    the Residents community planning scenario, including building damage states, casualties,
    hospital accessibility, power availability, and road network disruption. Data
    formats: ESRI File Geodatabase (GDB) and GeoJSON.'
  download_url: https://data.tomorrowscities.org/dataset/10097ffd-2638-4bdb-bd60-f0b2bb9f73ee/resource/836134a2-9da3-43db-941a-292a57fa5dd5/download/darimpactresults_residents.zip
  format: File Geodatabase (gdb)
  id: resource_impact_residents
  media_type: null
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Dar es Salaam Impact Results - Residents
- access_url: https://data.tomorrowscities.org/dataset/dar-impact-results-youth
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Impact assessment results for flood hazards (both scenarios) under
    the Youth community planning scenario, including building damage states, casualties,
    hospital accessibility, power availability, and road network disruption. Data
    formats: ESRI File Geodatabase (GDB) and GeoJSON.'
  download_url: https://data.tomorrowscities.org/dataset/3b530d66-9e8b-425d-9c19-d7b2266560ed/resource/83594a76-6c24-4281-8784-13c336427d81/download/darimpactresults_youth.zip
  format: File Geodatabase (gdb)
  id: resource_impact_youth
  media_type: null
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Dar es Salaam Impact Results - Youth
risk_data_type:
- hazard
- exposure
- vulnerability
- loss
schema: rdls-10
slug: rdls_hevl-tza_tmrwcities_daressalaam
spatial:
  bbox:
  - 39.2378
  - -6.95
  - 39.274
  - -6.9207
  centroid: null
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
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Tomorrow's Cities Multi-Hazard Risk Assessment Dataset for Dar es Salaam, Tanzania
version: '1'
vulnerability:
  functions:
    damage_to_loss: []
    engineering_demand: []
    fragility:
    - analysis_details: "Landslide fragility functions for 20 typologies across 3\
        \ susceptibility levels (low, medium, high), providing probability of minor,\
        \ moderate, and severe damage. Building typologies: Adb+LC/MC/HC, BrM+LC/MC/HC,\
        \ BrCfl+LC/MC/HC, BrCri+LC/MC/HC, Rci+LC/MC/HC, S+LC/MC/HC. Infrastructure:\
        \ LSS1 (substations), roads. Total 60 entries (20 typologies \xD7 3 susceptibility\
        \ levels)."
      approach: analytical
      category: buildings
      damage_scale_name: null
      damage_states_names: null
      hazard_analysis_type: deterministic
      hazard_primary:
        classification: null
        id: null
        intensity_measure: LSI:-
        process: landslide_general
        trigger: null
        type: landslide
      hazard_secondary: null
      id: fragility_function_landslide_buildings
      impact:
        measurement:
          quantity_kind: dimensionless_ratio
          unit: null
        metric: damage
        modelling: simulated
        type: direct
      relationship: discrete
      taxonomy: Custom
    - analysis_details: HAZUS-based vulnerability functions for power network infrastructure
        (HazusSS for substations) under flood loading.
      approach: empirical
      category: infrastructure
      damage_scale_name: null
      damage_states_names: null
      hazard_analysis_type: deterministic
      hazard_primary:
        classification: null
        id: null
        intensity_measure: wd:m
        process: pluvial_flood
        trigger: null
        type: flood
      hazard_secondary: null
      id: fragility_function_flood_power
      impact:
        measurement:
          quantity_kind: dimensionless_ratio
          unit: null
        metric: damage
        modelling: simulated
        type: direct
      relationship: math_parametric
      taxonomy: HAZUS
    socio_economic: []
    vulnerability:
    - analysis_details: 'Depth-damage vulnerability functions defining damage ratio
        as a function of water depth (0-6m at 9 discrete levels: 0, 0.5, 1, 1.5, 2,
        3, 4, 5, 6m) for 7,354 building typologies classified by lateral resistance
        system (Adb, BrCfl, BrCri, BrM, Rci, S), code level (LC, MC, HC), storeys,
        and occupancy type. Includes special industrial types (SteelIndustrial). Functions
        based on consultation with local partners and JRC global flood depth-damage
        database.'
      approach: analytical
      category: buildings
      hazard_analysis_type: deterministic
      hazard_primary:
        classification: null
        id: null
        intensity_measure: wd:m
        process: pluvial_flood
        trigger: null
        type: flood
      hazard_secondary: null
      id: vulnerability_function_flood_buildings
      impact:
        measurement:
          quantity_kind: dimensionless_ratio
          unit: null
        metric: damage
        modelling: simulated
        type: direct
      relationship: discrete
      taxonomy: Custom
---
