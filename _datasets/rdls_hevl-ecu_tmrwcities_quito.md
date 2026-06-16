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
dataset_id: rdls_hevl-ecu_tmrwcities_quito
description: Multi-hazard risk data package for Santa Rosa district, Quito, Ecuador,
  providing earthquake hazard (2 PGA scenarios as XLSX grid data), debris flow hazard
  (1 depth scenario), flood vulnerability functions (no flood depth data), synthetic
  future urban exposure datasets (buildings, households, land use) for three community
  planning scenarios (VS0, VS2, VS3), and multi-hazard impact assessment results.
  Developed as part of the Tomorrow's Cities GCRF Urban Disaster Risk Hub project
  for risk-informed decision making in urban planning.
details: 'The dataset includes: (i) earthquake hazard as 2 XLSX PGA scenario grids
  (EQ-SCEN1-PGA.xlsx, EQ-SCEN2-PGA.xlsx) with 499 points providing X/Y projected coordinates
  and IM (PGA in g), earthquake fragility for 11 building typologies (5 damage states
  DS1-DS5 with SA intensity measure and period-dependent parameters), debris flow
  fragility for 11 typologies; (ii) debris flow depth scenario (DF-SCEN01-DPTH.xlsx,
  3.0 MB) with depth values; (iii) flood vulnerability functions for 1,260 building
  typologies at 9 water depths (0-6m) - note: no flood depth hazard map provided,
  flood assessed through debris flow depth proxy; (iv) three future exposure dataset
  variants (VS0: Santa Rosa baseline, VS2: Vision 2, VS3: Vision 3; VS1 absent) each
  containing building footprints (333 buildings) with structural taxonomy, household
  data (497 households), and land use plans (6 zones, 2 residential types); and (v)
  multi-hazard impact results including metrics.txt summary files with damage distribution
  and impact metrics (metric3-metric8) for both basic (v1) and enhanced (v2) analysis
  versions.'
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
      description: 'Earthquake Scenario 1 for Santa Rosa area providing Peak Ground
        Acceleration (PGA) values at 499 grid points. Tabular XLSX format with X/Y
        projected coordinates and IM values. File: EQ-SCEN1-PGA.xlsx'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_earthquake
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      id: event_earthquake_quito_scen1
      occurrence:
        deterministic:
          description: null
          index_criteria: Scenario-based deterministic analysis
          thresholds: null
        empirical: null
        probabilistic: null
    - calculation_method: simulated
      description: 'Earthquake Scenario 2 for Santa Rosa area providing Peak Ground
        Acceleration (PGA) values at 499 grid points. File: EQ-SCEN2-PGA.xlsx'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_earthquake
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      id: event_earthquake_quito_scen2
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
    id: event_set_earthquake_quito
    occurrence_range: null
    seasonality: null
  - analysis_type: deterministic
    calculation_method: simulated
    event_count: 1
    events:
    - calculation_method: simulated
      description: 'Debris flow Scenario 01 for Santa Rosa area providing depth values.
        Tabular XLSX format (3.0 MB). Also serves as proxy for flood hazard assessment.
        File: DF-SCEN01-DPTH.xlsx'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_debris_flow
        intensity_measure: wd:m
        process: landslide_mudflow
        trigger: null
        type: landslide
      id: event_debris_flow_quito_scen01
      occurrence:
        deterministic:
          description: null
          index_criteria: Scenario-based deterministic analysis - return period and
            trigger mechanism undocumented
          thresholds: null
        empirical: null
        probabilistic: null
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_debris_flow
      intensity_measure: wd:m
      process: landslide_mudflow
      trigger: null
      type: landslide
    id: event_set_debris_flow_quito
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
    license: CC0-1.0
    name: Building footprints and exposure data
    risk_data_type: null
    type: dataset
    url: null
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
    name: Earthquake hazard scenarios
    risk_data_type: null
    type: model
    url: null
    used_in: hazard
  - id: source_4
    license: null
    name: Debris flow depth scenario
    risk_data_type: null
    type: model
    url: null
    used_in: hazard
  - id: source_5
    license: null
    name: Earthquake fragility functions
    risk_data_type: null
    type: model
    url: null
    used_in: vulnerability
  - id: source_6
    license: null
    name: Debris flow fragility functions
    risk_data_type: null
    type: model
    url: null
    used_in: vulnerability
  - id: source_7
    license: null
    name: Flood vulnerability functions
    risk_data_type: null
    type: model
    url: https://publications.jrc.ec.europa.eu/repository/handle/JRC105688
    used_in: vulnerability
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Building damage state results from earthquake impact assessment for
      each vision scenario (VS0, VS2, VS3) and both earthquake scenarios (SCEN1, SCEN2),
      with basic (v1) and enhanced (v2) analysis versions.
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
    description: Building damage state results from debris flow impact assessment
      for each vision scenario.
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: landslide_mudflow
      trigger: null
      type: landslide
    id: loss_debris_flow_buildings
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
    description: Affected population metrics from multi-hazard impact assessment including
      homeless households/individuals (metric5/metric6), hospital access disruption
      (metric3/metric4), and total reposition value for damaged buildings (metric8).
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
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
project:
  name: Tomorrow's Cities - GCRF Urban Disaster Risk Hub
  url: https://tomorrowscities.org/
publisher:
  affiliation: null
  email: support@tomorrowscities.org
  name: Tomorrow's Cities
  url: https://data.tomorrowscities.org/
purpose: To support multi-hazard risk assessment and risk-informed urban planning
  decision making for Quito (Santa Rosa district) by providing spatial hazard, synthetic
  future exposure, vulnerability/fragility functions, and impact assessment datasets
  for participatory community planning scenarios.
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
- access_url: https://data.tomorrowscities.org/dataset/quito-multi-hazard-dataset
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Multi-hazard dataset containing: (1) 2 earthquake PGA scenario XLSX
    grids (499 points each); (2) 1 debris flow depth scenario XLSX (3.0 MB); (3) Earthquake
    fragility for 11 typologies (DS1-DS5); (4) Debris flow fragility for 11 typologies;
    (5) Flood vulnerability for 1,260 typologies (no flood depth data provided). All
    hazard data is tabular (XLSX), not raster.'
  download_url: https://data.tomorrowscities.org/dataset/quito-multi-hazard-dataset/resource/ac00a37d-ecd5-4a3e-bc04-4cea0484324a
  format: null
  id: resource_hazard_multihazard
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Quito Multi Hazard Dataset
- access_url: https://data.tomorrowscities.org/dataset/quito-future-exposure-dataset-vs0
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:32717
  description: 'Future urban exposure dataset for VS0 (Santa Rosa baseline), including
    building footprints (333 buildings) with structural taxonomy, household data (497
    households), and land use plan (6 zones). Data formats: Shapefile for spatial
    data, Excel (XLSX) for tabular data. No individual-level data.'
  download_url: https://data.tomorrowscities.org/dataset/quito-future-exposure-dataset-vs0/resource/c4a322ef-935f-46b6-9421-d256fbd35bee
  format: null
  id: resource_exposure_vs0
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal:
    central_year: null
    duration: P50Y
    end: null
    start: null
  temporal_resolution: null
  title: Quito Future Exposure Dataset - VS0
- access_url: https://data.tomorrowscities.org/dataset/quito-future-exposure-dataset-vs2
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:32717
  description: 'Future urban exposure dataset for Vision Scenario 2. Data formats:
    Shapefile, XLSX.'
  download_url: https://data.tomorrowscities.org/dataset/quito-future-exposure-dataset-vs2/resource/f1515843-2259-4e69-93e1-8a5f98bd1993
  format: null
  id: resource_exposure_vs2
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal:
    central_year: null
    duration: P50Y
    end: null
    start: null
  temporal_resolution: null
  title: Quito Future Exposure Dataset - VS2
- access_url: https://data.tomorrowscities.org/dataset/quito-future-exposure-dataset-vs3
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:32717
  description: 'Future urban exposure dataset for Vision Scenario 3. Data formats:
    Shapefile, XLSX.'
  download_url: https://data.tomorrowscities.org/dataset/quito-future-exposure-dataset-vs3/resource/702720b9-35ef-401e-8dee-221088f2f385
  format: null
  id: resource_exposure_vs3
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal:
    central_year: null
    duration: P50Y
    end: null
    start: null
  temporal_resolution: null
  title: Quito Future Exposure Dataset - VS3
- access_url: https://data.tomorrowscities.org/dataset/quito-impact-results-vs0
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Multi-hazard impact results for VS0 including earthquake (2 scenarios,
    basic v1 and enhanced v2), debris flow, and flood damage. Contains metrics.txt
    summaries with building damage distributions and impact metrics (metric3-metric8).
    Data formats: CSV, TXT.'
  download_url: https://data.tomorrowscities.org/dataset/quito-impact-results-vs0/resource/2686985e-842a-4458-9156-6ae2fb90b1cf
  format: null
  id: resource_impact_vs0
  media_type: text/csv
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Quito Impact Results - VS0
- access_url: https://data.tomorrowscities.org/dataset/quito-impact-results-vs2
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Multi-hazard impact results for Vision Scenario 2. Data formats: CSV,
    TXT.'
  download_url: https://data.tomorrowscities.org/dataset/quito-impact-results-vs2/resource/8023e4e8-55fa-49e3-8ae1-86fecf4aaeb4
  format: null
  id: resource_impact_vs2
  media_type: text/csv
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Quito Impact Results - VS2
- access_url: https://data.tomorrowscities.org/dataset/quito-impact-results-vs3
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Multi-hazard impact results for Vision Scenario 3. Data formats: CSV,
    TXT.'
  download_url: https://data.tomorrowscities.org/dataset/quito-impact-results-vs3/resource/7c794f1a-95ab-414d-994b-62ef77936729
  format: null
  id: resource_impact_vs3
  media_type: text/csv
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Quito Impact Results - VS3
risk_data_type:
- hazard
- exposure
- vulnerability
- loss
schema: rdls-10
slug: rdls_hevl-ecu_tmrwcities_quito
spatial:
  bbox:
  - -78.58
  - -0.32
  - -78.54
  - -0.28
  centroid: null
  countries:
  - ECU
  gazetteer_entries:
  - description: Ecuador
    id: gazetteer_1
    scheme: GEONAMES
    uri: https://www.geonames.org/3658394/ecuador.html
  - description: Quito
    id: gazetteer_2
    scheme: GEONAMES
    uri: https://www.geonames.org/3652462/quito.html
  scale: sub-national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Tomorrow's Cities Multi-Hazard Risk Assessment Dataset for Quito (Santa Rosa),
  Ecuador
version: '1'
vulnerability:
  functions:
    damage_to_loss: []
    engineering_demand: []
    fragility:
    - analysis_details: Lognormal fragility functions for 11 building typologies defining
        probability of exceeding 5 damage states (DS1-DS5) as a function of spectral
        acceleration (g). Period-dependent parameters (periodMin, periodMax). Typologies
        include Adobe (Adb+LC+LR), RC infilled, Brick masonry with various code levels.
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
    socio_economic: []
    vulnerability:
    - analysis_details: 'Depth-damage vulnerability functions defining damage ratio
        as a function of water depth (0-6m at 9 discrete levels) for 1,260 building
        typologies. Note: No flood depth hazard map provided - flood is assessed through
        debris flow depth proxy.'
      approach: analytical
      category: buildings
      hazard_analysis_type: deterministic
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
    - analysis_details: Debris flow depth-damage vulnerability functions for 11 building
        typologies defining damage ratios at debris depths from hw0 to hw6 (same format
        as flood vulnerability).
      approach: analytical
      category: buildings
      hazard_analysis_type: deterministic
      hazard_primary:
        classification: null
        id: hazard_landslide
        intensity_measure: wd:m
        process: landslide_mudflow
        trigger: null
        type: landslide
      hazard_secondary: null
      id: vulnerability_function_debris_flow_buildings
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
