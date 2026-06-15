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
dataset_id: rdls_hevl-bgd_tmrwcities_chattogram
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
    earthquake:
    - analysis_type: deterministic
      calculation_method: simulated
      event_count: 2
      events:
      - calculation_method: simulated
        description: 'Deterministic earthquake Scenario 1 (Sc1) for Bairag area using
          NGA-West2 GMPEs for active shallow crustal sources: Abrahamson et al 2014
          (ASK14), Boore et al 2014 (BSSA14), Campbell and Bozorgnia 2014 (CB14),
          Chiou and Youngs 2014 (CY14). Provides PGA and Spectral Acceleration at
          0.3s, 0.7s, and 1.0s periods. Available in 32-bit and 64-bit precision.'
        disaster_identifiers: []
        hazard:
          classification: null
          id: hazard_earthquake
          intensity_measure: PGA:g
          process: ground_motion
          trigger: null
          type: earthquake
        id: event_earthquake_bairag_sc1
        occurrence:
          deterministic:
            description: null
            index_criteria: Scenario-based deterministic analysis
            thresholds: null
          empirical: null
          probabilistic: null
      - calculation_method: simulated
        description: 'Deterministic earthquake Scenario 2 (Sc2) for Bairag area using
          subduction zone GMPEs: Atkinson and Boore, Zhao et al. Provides PGA and
          Spectral Acceleration at 0.3s, 0.7s, and 1.0s periods. Available in 32-bit
          and 64-bit precision.'
        disaster_identifiers: []
        hazard:
          classification: null
          id: hazard_earthquake
          intensity_measure: PGA:g
          process: ground_motion
          trigger: null
          type: earthquake
        id: event_earthquake_bairag_sc2
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
        id: hazard_earthquake
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      id: event_set_earthquake_bairag
      occurrence_range: null
      seasonality: null
    flood:
    - analysis_type: deterministic
      calculation_method: simulated
      event_count: 2
      events:
      - calculation_method: simulated
        description: Riverine flood scenario for Bairag area providing maximum water
          depth (m) from fluvial flooding simulation.
        disaster_identifiers: []
        hazard:
          classification: null
          id: hazard_flood
          intensity_measure: wd:m
          process: fluvial_flood
          trigger: null
          type: flood
        id: event_flood_bairag_riverine
        occurrence:
          deterministic:
            description: null
            index_criteria: Scenario-based deterministic analysis
            thresholds: null
          empirical: null
          probabilistic: null
      - calculation_method: simulated
        description: Pluvial (rainfall-induced) flood scenario for Bairag area providing
          maximum water depth (m) from surface water flooding simulation.
        disaster_identifiers: []
        hazard:
          classification: null
          id: hazard_flood
          intensity_measure: wd:m
          process: pluvial_flood
          trigger: null
          type: flood
        id: event_flood_bairag_pluvial
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
        process: fluvial_flood
        trigger: null
        type: flood
      - classification: null
        id: hazard_flood_pluvial_flood
        intensity_measure: wd:m
        process: pluvial_flood
        trigger: null
        type: flood
      id: event_set_flood_bairag
      occurrence_range: null
      seasonality: null
  event_sets_count: 2
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
    name: Earthquake hazard simulation
    risk_data_type: null
    type: model
    url: https://doi.org/10.1016/j.ijdrr.2022.103338
    used_in: hazard
  - id: source_4
    license: null
    name: Flood hazard modelling
    risk_data_type: null
    type: model
    url: null
    used_in: hazard
  - id: source_5
    license: https://creativecommons.org/publicdomain/zero/1.0/
    name: NASADEM Digital Elevation Model
    risk_data_type: null
    type: dataset
    url: https://www.earthdata.nasa.gov/esds/competitive-programs/measures/nasadem
    used_in: hazard
  - id: source_6
    license: null
    name: Building fragility functions for earthquake
    risk_data_type: null
    type: model
    url: https://doi.org/10.1016/j.ijdrr.2022.103365
    used_in: vulnerability
  - id: source_7
    license: null
    name: Depth-damage vulnerability functions for flood
    risk_data_type: null
    type: model
    url: https://publications.jrc.ec.europa.eu/repository/handle/JRC105688
    used_in: vulnerability
  - id: source_8
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
    description: Building damage state results from earthquake impact assessment for
      each community planning scenario (Civil Society, Farmers/Fishermen, Informal
      Working, Landless). Damage states derived by convolving spectral acceleration
      hazard with building fragility functions.
    disaster_identifiers: []
    hazard:
      classification: null
      id: null
      intensity_measure: PGA:g
      process: ground_motion
      trigger: null
      type: earthquake
    id: loss_earthquake_buildings
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
  - asset_category: buildings
    asset_dimension: structure
    description: Building damage ratio results from flood impact assessment for each
      community planning scenario (Civil Society, Farmers/Fishermen, Informal Working,
      Landless). Damage ratios derived by applying depth-damage vulnerability functions
      to flood water depth hazard.
    disaster_identifiers: []
    hazard:
      classification: null
      id: null
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_flood_buildings
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: dimensionless_ratio
          unit: null
        metric: damage
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: deterministic
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Affected population results from earthquake impact assessment for
      each community planning scenario, derived from building damage states and residential
      occupancy.
    disaster_identifiers: []
    hazard:
      classification: null
      id: null
      intensity_measure: PGA:g
      process: ground_motion
      trigger: null
      type: earthquake
    id: loss_earthquake_population
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: deterministic
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Affected population results from flood impact assessment for each
      community planning scenario, derived from building inundation and residential
      occupancy.
    disaster_identifiers: []
    hazard:
      classification: null
      id: null
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_flood_population
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
        modelling: simulated
        type: direct
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
  decision making for Chattogram by providing spatial hazard, synthetic future exposure,
  vulnerability functions, and impact assessment datasets for participatory community
  planning scenarios.
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
- access_url: https://data.tomorrowscities.org/dataset/chattogram-multi-hazard-dataset
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
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
  format: null
  id: resource_hazard_multihazard
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Chattogram Multi Hazard Dataset
- access_url: https://data.tomorrowscities.org/dataset/chattogram-future-exposure-dataset-civil-society
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Civil Society community planning
    scenario, including building footprints with structural taxonomy, household socio-economic
    data, individual demographic data, land use plan, and road network. Data formats:
    GeoJSON for spatial data (buildings, landuse, road network), JSON for tabular
    data (households, individuals).'
  download_url: https://data.tomorrowscities.org/dataset/ca37dabd-dd6a-4545-bae9-665943704205/resource/88f85d4b-97ed-49a8-adf7-a02fcd75b747/download/chattogramfutureexposuredataset_civil_society.zip
  format: null
  id: resource_exposure_civil_society
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
  title: Chattogram Future Exposure Dataset - Civil Society
- access_url: https://data.tomorrowscities.org/dataset/chattogram-future-exposure-dataset-farmers-fishermen
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Farmers/Fishermen community planning
    scenario, including building footprints with structural taxonomy, household socio-economic
    data, individual demographic data, land use plan, and road network. Data formats:
    GeoJSON for spatial data (buildings, landuse, road network), JSON for tabular
    data (households, individuals).'
  download_url: https://data.tomorrowscities.org/dataset/6f46d7af-e3b0-4fd6-bb68-398213e4ec4f/resource/c4a37c18-022d-4e22-88c3-61ad0d05c775/download/chattogramfutureexposuredataset_farmers_fishermen.zip
  format: null
  id: resource_exposure_farmers_fishermen
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
  title: Chattogram Future Exposure Dataset - Farmers Fishermen
- access_url: https://data.tomorrowscities.org/dataset/chattogram-future-exposure-dataset-informal-working
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Informal Working community planning
    scenario, including building footprints with structural taxonomy, household socio-economic
    data, individual demographic data, land use plan, and road network. Data formats:
    GeoJSON for spatial data (buildings, landuse, road network), JSON for tabular
    data (households, individuals).'
  download_url: https://data.tomorrowscities.org/dataset/07df0763-2441-4b7d-9252-dc209e78d81a/resource/41f36288-6e2f-4e04-9363-9f8bab0150e5/download/chattogramfutureexposuredataset_informal_working.zip
  format: null
  id: resource_exposure_informal_working
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
  title: Chattogram Future Exposure Dataset - Informal Working
- access_url: https://data.tomorrowscities.org/dataset/chattogram-future-exposure-dataset-landless
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Landless community planning scenario,
    including building footprints with structural taxonomy, household socio-economic
    data, individual demographic data, land use plan, and road network. Data formats:
    GeoJSON for spatial data (buildings, landuse, road network), JSON for tabular
    data (households, individuals).'
  download_url: https://data.tomorrowscities.org/dataset/5940db5c-e04f-4855-8353-54f2cf2d3466/resource/aafc37fb-1258-466f-a30f-2559bdcc422b/download/chattogramfutureexposuredataset_landless.zip
  format: null
  id: resource_exposure_landless
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
  title: Chattogram Future Exposure Dataset - Landless
- access_url: https://data.tomorrowscities.org/dataset/chattogram-impact-results-civil-society
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Impact assessment results for earthquake and flood hazards under the
    Civil Society community planning scenario, including building damage states and
    affected population. Data formats: ESRI File Geodatabase (GDB) and GeoJSON.'
  download_url: https://data.tomorrowscities.org/dataset/ccde0b57-a447-4e15-a018-c2a0ab5eaaea/resource/afddc29c-6187-447c-87eb-60866603bc00/download/chattogramimpactresults_civil_society.zip
  format: File Geodatabase (gdb)
  id: resource_impact_civil_society
  media_type: null
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Chattogram Impact Results - Civil Society
- access_url: https://data.tomorrowscities.org/dataset/chattogram-impact-results-farmers
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Impact assessment results for earthquake and flood hazards under the
    Farmers/Fishermen community planning scenario, including building damage states
    and affected population. Data formats: ESRI File Geodatabase (GDB) and GeoJSON.'
  download_url: https://data.tomorrowscities.org/dataset/6f13c0b5-00c0-4bec-946d-e7644845478c/resource/5243bd1f-d134-4a14-88f6-b6f48a190748/download/chattogramimpactresults_farmers.zip
  format: File Geodatabase (gdb)
  id: resource_impact_farmers
  media_type: null
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Chattogram Impact Results - Farmers
- access_url: https://data.tomorrowscities.org/dataset/chattogram-impact-results-informal-working
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Impact assessment results for earthquake and flood hazards under the
    Informal Working community planning scenario, including building damage states
    and affected population. Data formats: ESRI File Geodatabase (GDB) and GeoJSON.'
  download_url: https://data.tomorrowscities.org/dataset/618b12f3-4839-4b6d-ae50-42d7f09fd7de/resource/cba12127-cdf0-4abd-af8d-2c1babd8c55b/download/chattogramimpactresults_informal_working.zip
  format: File Geodatabase (gdb)
  id: resource_impact_informal_working
  media_type: null
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Chattogram Impact Results - Informal Working
- access_url: https://data.tomorrowscities.org/dataset/chattogram-impact-results-landless
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Impact assessment results for earthquake and flood hazards under the
    Landless community planning scenario, including building damage states and affected
    population. Data formats: ESRI File Geodatabase (GDB) and GeoJSON.'
  download_url: https://data.tomorrowscities.org/dataset/3bc2f627-c16a-46ae-9e46-44a0fcc586b3/resource/d0a7a407-92ae-4db5-aabb-cec623611a7d/download/chattogramimpactresults_landless.zip
  format: File Geodatabase (gdb)
  id: resource_impact_landless
  media_type: null
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Chattogram Impact Results - Landless
risk_data_type:
- hazard
- exposure
- vulnerability
- loss
schema: rdls-10
slug: rdls_hevl-bgd_tmrwcities_chattogram
spatial:
  bbox:
  - 91.8134
  - 22.2096
  - 91.8681
  - 22.2534
  centroid: null
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
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Tomorrow's Cities Multi-Hazard Risk Assessment Dataset for Chattogram (Bairag),
  Bangladesh
version: '1'
vulnerability:
  functions:
    damage_to_loss: []
    engineering_demand: []
    fragility:
    - analysis_details: Lognormal fragility functions for 45 building typologies defining
        probability of exceeding 4 damage states (DS1-DS4) as a function of PGA or
        spectral acceleration (g). Parameters include median (mu) and dispersion (sigma)
        for each damage state, with period range (minperiod, maxperiod) for each typology.
        Building taxonomy follows {LRS}+{CodeLevel}+{Height} pattern where LRS includes
        RCi (reinforced concrete infill), BrCri (brick with concrete), BrCfl (brick
        with flexible); CodeLevel includes LC (low code), MC (moderate code), HC (high
        code); Height includes LR (low-rise), MR (mid-rise), HR (high-rise).
      approach: analytical
      category: buildings
      damage_scale_name: null
      damage_states_names: null
      hazard_analysis_type: deterministic
      hazard_primary:
        classification: null
        id: null
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      hazard_secondary: null
      id: fragility_function_earthquake_buildings
      impact:
        measurement:
          quantity_kind: dimensionless_ratio
          unit: null
        metric: damage
        modelling: simulated
        type: direct
      relationship: math_parametric
      taxonomy: Custom
    - analysis_details: HAZUS-based fragility functions for road infrastructure (HWB3,
        HWB5, HWB7 highway bridge classes) defining median PGA and dispersion for
        4 damage states (slight, moderate, extensive, complete).
      approach: empirical
      category: infrastructure
      damage_scale_name: null
      damage_states_names: null
      hazard_analysis_type: deterministic
      hazard_primary:
        classification: null
        id: null
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      hazard_secondary: null
      id: fragility_function_earthquake_roads
      impact:
        measurement:
          quantity_kind: dimensionless_ratio
          unit: null
        metric: damage
        modelling: simulated
        type: direct
      relationship: math_parametric
      taxonomy: HAZUS
    - analysis_details: HAZUS-based fragility functions for power network infrastructure
        (ESS1-ESS18 substation classes at 115/230/500 kV, anchored and unanchored
        configurations) defining median PGA and dispersion (beta) for 4 damage states
        (slight, moderate, extensive, complete).
      approach: empirical
      category: infrastructure
      damage_scale_name: null
      damage_states_names: null
      hazard_analysis_type: deterministic
      hazard_primary:
        classification: null
        id: null
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      hazard_secondary: null
      id: fragility_function_earthquake_power
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
        3, 4, 5, 6m) for 495 building typologies classified by lateral resistance
        system (BrCfl, BrCri, Rci), code level (LC, MC, HC), storeys, and occupancy
        type (Res, Com, Edu, etc.). Functions based on consultation with local partners
        and JRC global flood depth-damage database.'
      approach: analytical
      category: buildings
      hazard_analysis_type: deterministic
      hazard_primary:
        classification: null
        id: null
        intensity_measure: wd:m
        process: fluvial_flood
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
