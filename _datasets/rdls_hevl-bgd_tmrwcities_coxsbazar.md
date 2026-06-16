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
dataset_id: rdls_hevl-bgd_tmrwcities_coxsbazar
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
      description: 'Deterministic earthquake Scenario 1 (Sc1) for Jaliya Palong area
        using NGA-West2 GMPEs for active shallow crustal sources: Abrahamson et al
        2014 (ASK14), Boore et al 2014 (BSSA14), Campbell and Bozorgnia 2014 (CB14),
        Chiou and Youngs 2014 (CY14). Provides PGA and Spectral Acceleration at 0.3s,
        0.7s, and 1.0s periods. Available in 32-bit and 64-bit precision. File prefix:
        Jl_Mah_'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_earthquake
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      id: event_earthquake_jaliyapalong_sc1
      occurrence:
        deterministic:
          description: null
          index_criteria: Scenario-based deterministic analysis
          thresholds: null
        empirical: null
        probabilistic: null
    - calculation_method: simulated
      description: 'Deterministic earthquake Scenario 2 (Sc2) for Jaliya Palong area
        using subduction zone GMPEs: Atkinson and Boore, Zhao et al. Provides PGA
        and Spectral Acceleration at 0.3s, 0.7s, and 1.0s periods. Available in 32-bit
        and 64-bit precision. File prefix: JL_Ram_'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_earthquake
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      id: event_earthquake_jaliyapalong_sc2
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
    id: event_set_earthquake_jaliyapalong
    occurrence_range: null
    seasonality: null
  - analysis_type: probabilistic
    calculation_method: simulated
    event_count: 4
    events:
    - calculation_method: simulated
      description: '5-year return period flood scenario for Jaliya Palong area providing
        maximum water depth (m). File: 5RP.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_flood
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_flood_jaliyapalong_5yr
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.2
          probability: null
          return_period: 5
    - calculation_method: simulated
      description: '10-year return period flood scenario for Jaliya Palong area providing
        maximum water depth (m). File: 10RP.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_flood
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_flood_jaliyapalong_10yr
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.1
          probability: null
          return_period: 10
    - calculation_method: simulated
      description: '20-year return period flood scenario for Jaliya Palong area providing
        maximum water depth (m). File: 20RP.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_flood
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_flood_jaliyapalong_20yr
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.05
          probability: null
          return_period: 20
    - calculation_method: simulated
      description: '50-year return period flood scenario for Jaliya Palong area providing
        maximum water depth (m). File: 50RP.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_flood
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_flood_jaliyapalong_50yr
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.02
          probability: null
          return_period: 50
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_flood_jaliyapalong
    occurrence_range: null
    seasonality: null
license: CC0-1.0
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
    license: ODbL-1.0/
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
    license: CC0-1.0
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
    license: CC0-1.0
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
      each community planning scenario (Civil Society, Informal Working, Marginal,
      Women). Damage states (DS1-DS4) derived by convolving spectral acceleration
      hazard with building fragility functions.
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
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
    description: Building damage state results from flood impact assessment for each
      community planning scenario (Civil Society, Informal Working, Marginal, Women).
      Damage states (DS0-DS1) derived by applying depth-damage vulnerability functions
      to flood water depth hazard.
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
      loss_frequency_type: probabilistic
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Casualty results from earthquake impact assessment for each community
      planning scenario, derived from building damage states and residential occupancy.
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: ground_motion
      trigger: null
      type: earthquake
    id: loss_earthquake_casualties
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
  - asset_category: population
    asset_dimension: population
    description: Casualty results from flood impact assessment for each community
      planning scenario, derived from building inundation and residential occupancy.
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
      loss_frequency_type: probabilistic
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: Road and power network damage state results from earthquake impact
      assessment, including edge and node damage for both infrastructure types.
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: ground_motion
      trigger: null
      type: earthquake
    id: loss_earthquake_infrastructure
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
  - asset_category: infrastructure
    asset_dimension: structure
    description: Road network damage state results from flood impact assessment, with
      road edges flagged as damaged/undamaged based on flood inundation.
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
      loss_frequency_type: probabilistic
      loss_type: ground_up
  - asset_category: population
    asset_dimension: disruption
    description: Hospital accessibility and power availability impacts from earthquake,
      derived from road network connectivity analysis and power network damage assessment.
      Each building has hospital_access and has_power boolean attributes.
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: ground_motion
      trigger: null
      type: earthquake
    id: loss_earthquake_indirect
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
  - asset_category: population
    asset_dimension: disruption
    description: Hospital accessibility and power availability impacts from flood,
      derived from road network connectivity analysis (road edges damaged by flooding)
      and power network assessment. Flood causes significant road network disruption
      reducing hospital accessibility.
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
      loss_frequency_type: probabilistic
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
  decision making for Cox's Bazar by providing spatial hazard, synthetic future exposure,
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
- access_url: https://data.tomorrowscities.org/dataset/coxs-bazar-hazard-dataset
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
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
  format: null
  id: resource_hazard_multihazard
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Cox's Bazar Hazard Dataset
- access_url: https://data.tomorrowscities.org/dataset/coxs-bazar-exposure-dataset-civil-society
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Civil Society community planning
    scenario, including building footprints with structural taxonomy (including Steel
    buildings), household socio-economic data, individual demographic data, land use
    plan, road network, and power network infrastructure. Data formats: GeoJSON for
    spatial data (buildings, landuse, road network, power network), JSON and XLSX
    for tabular data (households, individuals).'
  download_url: https://data.tomorrowscities.org/dataset/89b9c298-1d19-4b84-853f-8a76ac49c8b4/resource/98731ba2-c23c-470a-b50c-607bfd6330cb/download/coxsbazarexposuredataset_civil_society.zip
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
  title: Cox's Bazar Future Exposure Dataset - Civil Society
- access_url: https://data.tomorrowscities.org/dataset/coxs-bazar-exposure-dataset-informal-working
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Informal Working community planning
    scenario, including building footprints with structural taxonomy (including Steel
    buildings), household socio-economic data, individual demographic data, land use
    plan, road network, and power network infrastructure. Data formats: GeoJSON for
    spatial data (buildings, landuse, road network, power network), JSON and XLSX
    for tabular data (households, individuals).'
  download_url: https://data.tomorrowscities.org/dataset/618cfee1-13ed-4702-a57f-a44d902df75f/resource/23d68778-5dd7-47c0-b642-78c2b6194108/download/coxsbazarexposuredataset_informal_working.zip
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
  title: Cox's Bazar Future Exposure Dataset - Informal Working
- access_url: https://data.tomorrowscities.org/dataset/coxs-bazar-exposure-dataset-marginal
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Marginal community planning scenario,
    including building footprints with structural taxonomy (including Steel buildings),
    household socio-economic data, individual demographic data, land use plan, road
    network, and power network infrastructure. Data formats: GeoJSON for spatial data
    (buildings, landuse, road network, power network), JSON and XLSX for tabular data
    (households, individuals), QMD for QGIS metadata.'
  download_url: https://data.tomorrowscities.org/dataset/e1b0423f-a5e8-437f-938f-b5368a09ada3/resource/9cc73da0-e710-4bbc-8317-3402d73b0e67/download/coxsbazarexposuredataset_marginal.zip
  format: null
  id: resource_exposure_marginal
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
  title: Cox's Bazar Future Exposure Dataset - Marginal
- access_url: https://data.tomorrowscities.org/dataset/coxs-bazar-exposure-dataset-women
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Women community planning scenario,
    including building footprints with structural taxonomy (including Steel buildings),
    household socio-economic data, individual demographic data, land use plan, road
    network, and power network infrastructure. Data formats: GeoJSON for spatial data
    (buildings, landuse, road network, power network), JSON and XLSX for tabular data
    (households, individuals), QMD for QGIS metadata.'
  download_url: https://data.tomorrowscities.org/dataset/c0aa46d6-48bf-45e7-8406-e4e156e8eaa7/resource/9fb30762-19a6-4dc2-96ca-0a2c2ed0d796/download/coxsbazarexposuredataset_women.zip
  format: null
  id: resource_exposure_women
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
  title: Cox's Bazar Future Exposure Dataset - Women
- access_url: https://data.tomorrowscities.org/dataset/coxs-bazar-impact-results-civil-society
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Impact assessment results for earthquake and flood hazards under the
    Civil Society community planning scenario, including building damage states, casualties,
    road network disruption, power network impacts, hospital accessibility, and power
    availability per building. Data formats: ESRI File Geodatabase (GDB) and GeoJSON.'
  download_url: https://data.tomorrowscities.org/dataset/1515bb10-af96-40e3-8ea5-1b2b9b9b1cbf/resource/01b8fc60-f6a2-4fc8-b7f5-974d2120b333/download/coxsbazarimpactresults_civil_society.zip
  format: File Geodatabase (gdb)
  id: resource_impact_civil_society
  media_type: null
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Cox's Bazar Impact Results - Civil Society
- access_url: https://data.tomorrowscities.org/dataset/coxs-bazar-impact-results-informal-working
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Impact assessment results for earthquake and flood hazards under the
    Informal Working community planning scenario, including building damage states,
    casualties, road network disruption, power network impacts, hospital accessibility,
    and power availability per building. Data formats: ESRI File Geodatabase (GDB)
    and GeoJSON.'
  download_url: https://data.tomorrowscities.org/dataset/64489c05-9af4-49b4-aea8-85d951ff1630/resource/95b40d12-e65a-4778-abe6-43468667db89/download/coxsbazarimpactresults_informal_working.zip
  format: File Geodatabase (gdb)
  id: resource_impact_informal_working
  media_type: null
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Cox's Bazar Impact Results - Informal Working
- access_url: https://data.tomorrowscities.org/dataset/coxs-bazar-impact-results-marginal
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Impact assessment results for earthquake and flood hazards under the
    Marginal community planning scenario, including building damage states, casualties,
    road network disruption, power network impacts, hospital accessibility, and power
    availability per building. Data formats: ESRI File Geodatabase (GDB) and GeoJSON,
    QMD for QGIS metadata.'
  download_url: https://data.tomorrowscities.org/dataset/36d4d669-c16a-4aca-a17f-a4a178a4d5ef/resource/1618e2c9-7c0b-4024-ba25-ae47ff04b94a/download/coxsbazarimpactresults_marginal.zip
  format: File Geodatabase (gdb)
  id: resource_impact_marginal
  media_type: null
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Cox's Bazar Impact Results - Marginal
- access_url: https://data.tomorrowscities.org/dataset/coxs-bazar-impact-results-women
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Impact assessment results for earthquake and flood hazards under the
    Women community planning scenario, including building damage states, casualties,
    road network disruption, power network impacts, hospital accessibility, and power
    availability per building. Data formats: ESRI File Geodatabase (GDB) and GeoJSON.'
  download_url: https://data.tomorrowscities.org/dataset/05faed28-08b3-4086-b1ee-316e06eaa1a1/resource/cbcd212f-60c8-45dd-9111-9fa096443175/download/coxsbazarimpactresults_women.zip
  format: File Geodatabase (gdb)
  id: resource_impact_women
  media_type: null
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Cox's Bazar Impact Results - Women
risk_data_type:
- hazard
- exposure
- vulnerability
- loss
schema: rdls-10
slug: rdls_hevl-bgd_tmrwcities_coxsbazar
spatial:
  bbox:
  - 92.0428
  - 21.078
  - 92.138
  - 21.303
  centroid: null
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
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Tomorrow's Cities Multi-Hazard Risk Assessment Dataset for Cox's Bazar (Jaliya
  Palong), Bangladesh
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
        with flexible), S (steel); CodeLevel includes LC (low code), MC (moderate
        code), HC (high code); Height includes LR (low-rise), MR (mid-rise), HR (high-rise).
      approach: analytical
      category: buildings
      damage_scale_name: null
      damage_states_names: null
      hazard_analysis_type: deterministic
      hazard_primary:
        classification: null
        id: hazard_earthquake
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
        HWB5, HWB7, HWB19 highway bridge classes) defining median PGA and dispersion
        for 4 damage states (slight, moderate, extensive, complete).
      approach: empirical
      category: infrastructure
      damage_scale_name: null
      damage_states_names: null
      hazard_analysis_type: deterministic
      hazard_primary:
        classification: null
        id: hazard_earthquake
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
    - analysis_details: 'HAZUS-based fragility functions for power network infrastructure
        with 18 classes: ESS1-ESS6 (substations at 115/230/500 kV, anchored/unanchored),
        EPP1-EPP4 (power plants, small/medium-large, anchored/unanchored), EDC1-EDC2
        (distribution circuits), and 6 transformer classes (TLAS, TLUS, TMAS, TMUS,
        THAS, THUS for low/medium/high voltage, anchored/unanchored). Each defines
        median PGA and dispersion (beta) for 4 damage states (slight, moderate, extensive,
        complete).'
      approach: empirical
      category: infrastructure
      damage_scale_name: null
      damage_states_names: null
      hazard_analysis_type: deterministic
      hazard_primary:
        classification: null
        id: hazard_earthquake
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
        3, 4, 5, 6m) for 1,521 building typologies classified by lateral resistance
        system (BrCfl, BrCri, Rci, S), code level (LC, MC, HC), storeys, and occupancy
        type (Res, Com, Edu, etc.). Functions based on consultation with local partners
        and JRC global flood depth-damage database.'
      approach: analytical
      category: buildings
      hazard_analysis_type: probabilistic
      hazard_primary:
        classification: null
        id: hazard_flood
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
