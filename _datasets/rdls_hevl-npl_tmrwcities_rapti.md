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
dataset_id: rdls_hevl-npl_tmrwcities_rapti
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
  \ - Nepal-Bihar earthquake, 2015 Gorkha Mw 7.8 replay, and historical 1505 AD earthquake\
  \ - plus a composite multiband intensity raster; (ii) flood hazard GeoTIFFs for\
  \ 20-year and 70-year return periods under future climate conditions (precipitation\
  \ increases of +173mm and +212mm respectively); (iii) landslide susceptibility rasters\
  \ for current and future conditions, each with base and extended variants (extended\
  \ covers 3 power nodes); (iv) vulnerability/fragility functions: earthquake fragility\
  \ for 54 building typologies (period-dependent, 4 damage states), 18 power types\
  \ (HAZUS), road fragility; flood depth-damage vulnerability; and landslide fragility\
  \ for 51 entries (typology \xD7 susceptibility with minor/moderate/severe damage);\
  \ (v) six future exposure dataset variants representing ethnic/caste-based planning\
  \ scenarios, each containing building footprints (10,945 buildings, 352 typologies),\
  \ household data (32,944 households), individual demographics, land use plans (905\
  \ zones, 48 categories), road network (3,659 edges), and power network (2 transmission\
  \ lines, 3 substations); and (vi) impact results for all 7 hazard combinations (3\
  \ EQ cases + 2 flood RPs + 2 landslide temporal) per scenario, with zone-aggregated\
  \ XLSX summaries."
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
    event_count: 3
    events:
    - calculation_method: simulated
      description: 'Nepal-Bihar earthquake scenario for Rapti Municipality. GeoTIFF
        raster: earthquake_scenario1_nepalbihar.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_earthquake
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      id: event_earthquake_rapti_nepalbihar
      occurrence:
        deterministic:
          description: null
          index_criteria: Historical/scenario-based Nepal-Bihar earthquake
          thresholds: null
        empirical: null
        probabilistic: null
    - calculation_method: simulated
      description: '2015 Gorkha earthquake (Mw 7.8) replay scenario for Rapti Municipality.
        GeoTIFF raster: earthquake_scenario2_gorkha.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_earthquake
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      id: event_earthquake_rapti_gorkha
      occurrence:
        deterministic:
          description: null
          index_criteria: Historical replay of 2015 Mw 7.8 Gorkha earthquake
          thresholds: null
        empirical: null
        probabilistic: null
    - calculation_method: simulated
      description: 'Historical 1505 AD earthquake scenario for Rapti Municipality.
        GeoTIFF raster: earthquake_scenario3_the1501.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_earthquake
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      id: event_earthquake_rapti_1505
      occurrence:
        deterministic:
          description: null
          index_criteria: Palaeo-seismic reconstruction of 1505 AD earthquake
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
    id: event_set_earthquake_rapti
    occurrence_range: null
    seasonality: null
  - analysis_type: probabilistic
    calculation_method: simulated
    event_count: 2
    events:
    - calculation_method: simulated
      description: '20-year return period flood under future climate conditions with
        +173mm precipitation increase. GeoTIFF: Rapti_max_depth_20yr_future_173mm_05.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_flood
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_flood_rapti_20yr
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.05
          probability: null
          return_period: 20
    - calculation_method: simulated
      description: '70-year return period flood under future climate conditions with
        +212mm precipitation increase. GeoTIFF: Rapti_max_depth_70yr_future_212mm_05.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_flood
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_flood_rapti_70yr
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.0143
          probability: null
          return_period: 70
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_flood_rapti
    occurrence_range: null
    seasonality: null
  - analysis_type: deterministic
    calculation_method: inferred
    event_count: 2
    events:
    - calculation_method: inferred
      description: Current landslide susceptibility for Rapti Municipality. Base extent
        (landslide_current.tif) plus extended version covering 3 power nodes (landslide_current_extended.tif).
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_landslide
        intensity_measure: LSI:-
        process: landslide_general
        trigger: null
        type: landslide
      id: event_landslide_rapti_current
      occurrence:
        deterministic:
          description: null
          index_criteria: Current baseline susceptibility
          thresholds: null
        empirical: null
        probabilistic: null
    - calculation_method: inferred
      description: Future landslide susceptibility for Rapti Municipality under climate
        change conditions. Base extent (landslide_future.tif) plus extended version
        covering 3 power nodes (landslide_future_extended.tif).
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_landslide
        intensity_measure: LSI:-
        process: landslide_general
        trigger: null
        type: landslide
      id: event_landslide_rapti_future
      occurrence:
        deterministic:
          description: null
          index_criteria: Future climate-informed susceptibility
          thresholds: null
        empirical: null
        probabilistic: null
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: event_set_landslide_rapti
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
    name: Earthquake hazard scenarios
    risk_data_type: null
    type: model
    url: null
    used_in: hazard
  - id: source_4
    license: null
    name: Climate-informed flood hazard modelling
    risk_data_type: null
    type: model
    url: null
    used_in: hazard
  - id: source_5
    license: null
    name: Landslide susceptibility modelling
    risk_data_type: null
    type: model
    url: null
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
    license: null
    name: Landslide fragility functions
    risk_data_type: null
    type: model
    url: null
    used_in: vulnerability
  - id: source_9
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
      3 scenarios (Nepal-Bihar, Gorkha, 1505 AD) and each community planning scenario
      (Ethnic, Madhesi, Pahadi, Planners, Squatter, Tharu).
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
    description: Building damage state results from flood impact assessment for 20-year
      and 70-year return periods under future climate conditions.
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
  - asset_category: buildings
    asset_dimension: structure
    description: Building damage state results from landslide assessment for current
      and future susceptibility conditions.
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: loss_landslide_buildings
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
    description: Casualty results from earthquake impact assessment for each scenario
      combination.
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
  - asset_category: infrastructure
    asset_dimension: structure
    description: Road and power network damage from earthquake assessment.
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
  - asset_category: population
    asset_dimension: disruption
    description: Hospital accessibility and power availability impacts from earthquake,
      flood, and landslide hazards. Each building has hospital_access and has_power
      boolean attributes.
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
  - asset_category: infrastructure
    asset_dimension: structure
    description: Road network damage from flood impact assessment.
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
project:
  name: Tomorrow's Cities - GCRF Urban Disaster Risk Hub
  url: https://tomorrowscities.org/
publisher:
  affiliation: null
  email: support@tomorrowscities.org
  name: Tomorrow's Cities
  url: https://data.tomorrowscities.org/
purpose: To support multi-hazard risk assessment and risk-informed urban planning
  decision making for Rapti Municipality by providing spatial hazard, synthetic future
  exposure, vulnerability functions, and impact assessment datasets for participatory
  community planning scenarios representing diverse ethnic/caste communities.
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
- access_url: https://data.tomorrowscities.org/dataset/rapti-multi-hazard-dataset
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: "Multi-hazard dataset containing: (1) 3 earthquake scenario GeoTIFFs\
    \ (Nepal-Bihar, Gorkha, 1505 AD) plus composite multiband raster; (2) 2 flood\
    \ GeoTIFFs for 20yr and 70yr return periods under future climate; (3) 4 landslide\
    \ susceptibility GeoTIFFs (current/future \xD7 base/extended); (4) Vulnerability/fragility\
    \ functions for earthquake (54 building + 18 power + road typologies), flood,\
    \ and landslide (51 entries). Data formats: GeoTIFF, XLSX, TXT."
  download_url: https://data.tomorrowscities.org/dataset/rapti-multi-hazard-dataset/resource/0c4b41ab-8e04-4073-83ad-a0bdcc313c34
  format: null
  id: resource_hazard_multihazard
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Rapti Multi Hazard Dataset
- access_url: https://data.tomorrowscities.org/dataset/rapti-future-exposure-dataset-ethnic
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Ethnic minority community planning
    scenario, including building footprints (10,945 buildings, 352 typologies) with
    rich attributes (OccBld, lrstype, CodeLevel, nstoreys, unit_price), household
    data (32,944 households), individual demographics, land use plan (905 zones, 48
    categories), road network (3,659 edges), and power network (2 edges, 3 nodes).
    Data formats: GeoJSON for spatial data, JSON for tabular data.'
  download_url: https://data.tomorrowscities.org/dataset/rapti-future-exposure-dataset-ethnic/resource/d0204033-f8ad-4afd-a944-a5b242db152a
  format: null
  id: resource_exposure_ethnic
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
  title: Rapti Future Exposure Dataset - Ethnic
- access_url: https://data.tomorrowscities.org/dataset/rapti-future-exposure-dataset-madhesi
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Madhesi community planning scenario.
    Data formats: GeoJSON, JSON.'
  download_url: https://data.tomorrowscities.org/dataset/rapti-future-exposure-dataset-madhesi/resource/e7d1489e-2776-4783-8bcc-4eaef7e8dc2a
  format: null
  id: resource_exposure_madhesi
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
  title: Rapti Future Exposure Dataset - Madhesi
- access_url: https://data.tomorrowscities.org/dataset/rapti-future-exposure-dataset-pahadi
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Pahadi community planning scenario.
    Data formats: GeoJSON, JSON.'
  download_url: https://data.tomorrowscities.org/dataset/rapti-future-exposure-dataset-pahadi/resource/628371c4-7b70-4be7-9b8d-d0e4338b60f2
  format: null
  id: resource_exposure_pahadi
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
  title: Rapti Future Exposure Dataset - Pahadi
- access_url: https://data.tomorrowscities.org/dataset/rapti-future-exposure-dataset-planners
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for urban Planners optimal scenario.
    Data formats: GeoJSON, JSON.'
  download_url: https://data.tomorrowscities.org/dataset/rapti-future-exposure-dataset-planners/resource/e8c5de85-f084-4fba-a2b9-e619207da873
  format: null
  id: resource_exposure_planners
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
  title: Rapti Future Exposure Dataset - Planners
- access_url: https://data.tomorrowscities.org/dataset/rapti-future-exposure-dataset-squatter
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Squatter/informal settlement community
    planning scenario. Data formats: GeoJSON, JSON.'
  download_url: https://data.tomorrowscities.org/dataset/rapti-future-exposure-dataset-squatter/resource/757d3097-c837-48ee-ae49-53b0f0280f38
  format: null
  id: resource_exposure_squatter
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
  title: Rapti Future Exposure Dataset - Squatter
- access_url: https://data.tomorrowscities.org/dataset/rapti-future-exposure-dataset-tharu
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Tharu indigenous community planning
    scenario. Data formats: GeoJSON, JSON.'
  download_url: https://data.tomorrowscities.org/dataset/rapti-future-exposure-dataset-tharu/resource/ad747579-6c20-444f-858d-7ac78ed78ef3
  format: null
  id: resource_exposure_tharu
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
  title: Rapti Future Exposure Dataset - Tharu
- access_url: https://data.tomorrowscities.org/dataset/rapti-impact-results-ethnic
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Multi-hazard impact results for Ethnic scenario including 7 hazard
    GeoJSONs (3 EQ cases + 2 flood RPs + 2 landslide temporal) and zone-aggregated
    XLSX summaries. Data formats: GeoJSON, XLSX.'
  download_url: https://data.tomorrowscities.org/dataset/rapti-impact-results-ethnic/resource/c4469a4c-cc5d-4baf-a9d4-c03f40605d47
  format: null
  id: resource_impact_ethnic
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Rapti Impact Results - Ethnic
- access_url: https://data.tomorrowscities.org/dataset/rapti-impact-results-madhesi
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Multi-hazard impact results for Madhesi scenario. Data formats: GeoJSON,
    XLSX.'
  download_url: https://data.tomorrowscities.org/dataset/rapti-impact-results-madhesi/resource/920c35e4-12c5-4c6f-bdf6-9a98f4aeb73d
  format: null
  id: resource_impact_madhesi
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Rapti Impact Results - Madhesi
- access_url: https://data.tomorrowscities.org/dataset/rapti-impact-results-pahadi
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Multi-hazard impact results for Pahadi scenario. Data formats: GeoJSON,
    XLSX.'
  download_url: https://data.tomorrowscities.org/dataset/rapti-impact-results-pahadi/resource/63333717-81ba-4c8d-a01d-9361b114f31f
  format: null
  id: resource_impact_pahadi
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Rapti Impact Results - Pahadi
- access_url: https://data.tomorrowscities.org/dataset/rapti-impact-results-planners
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Multi-hazard impact results for Planners scenario. Data formats: GeoJSON,
    XLSX.'
  download_url: https://data.tomorrowscities.org/dataset/rapti-impact-results-planners/resource/43b92857-26d8-45f2-891c-6cad599ef208
  format: null
  id: resource_impact_planners
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Rapti Impact Results - Planners
- access_url: https://data.tomorrowscities.org/dataset/rapti-impact-results-squatter
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Multi-hazard impact results for Squatter scenario. Data formats: GeoJSON,
    XLSX.'
  download_url: https://data.tomorrowscities.org/dataset/rapti-impact-results-squatter/resource/a1c0920e-2b90-41ab-8cf9-501d793e5911
  format: null
  id: resource_impact_squatter
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Rapti Impact Results - Squatter
- access_url: https://data.tomorrowscities.org/dataset/rapti-impact-results-tharu
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Multi-hazard impact results for Tharu scenario. Data formats: GeoJSON,
    XLSX.'
  download_url: https://data.tomorrowscities.org/dataset/rapti-impact-results-tharu/resource/240eec13-11e5-4e4d-85d8-ca3f3d3aa9d5
  format: null
  id: resource_impact_tharu
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Rapti Impact Results - Tharu
risk_data_type:
- hazard
- exposure
- vulnerability
- loss
schema: rdls-10
slug: rdls_hevl-npl_tmrwcities_rapti
spatial:
  bbox:
  - 82.6
  - 27.8
  - 82.75
  - 27.95
  centroid: null
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
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Tomorrow's Cities Multi-Hazard Risk Assessment Dataset for Rapti Municipality,
  Nepal
version: '1'
vulnerability:
  functions:
    damage_to_loss: []
    engineering_demand: []
    fragility:
    - analysis_details: Lognormal fragility functions for 54 building typologies defining
        probability of exceeding 4 damage states (DS1-DS4) as a function of spectral
        acceleration (g). Period-dependent parameters (minperiod, maxperiod) for each
        typology. Building taxonomy follows {Material}+{CodeLevel}+{Storeys}s+{Occupancy}
        pattern.
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
    - analysis_details: HAZUS-based fragility functions for 18 power infrastructure
        classes and road infrastructure under earthquake loading.
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
      id: fragility_function_earthquake_infrastructure
      impact:
        measurement:
          quantity_kind: dimensionless_ratio
          unit: null
        metric: damage
        modelling: simulated
        type: direct
      relationship: math_parametric
      taxonomy: HAZUS
    - analysis_details: Landslide fragility functions for 51 entries providing probability
        of minor, moderate, and severe damage for building typologies (Adb, BrCfl,
        BrCri, BrM, Rci with code levels) and infrastructure (roads, substations)
        across landslide susceptibility levels.
      approach: analytical
      category: buildings
      damage_scale_name: null
      damage_states_names: null
      hazard_analysis_type: deterministic
      hazard_primary:
        classification: null
        id: hazard_landslide
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
    socio_economic: []
    vulnerability:
    - analysis_details: Depth-damage vulnerability functions defining damage ratio
        as a function of water depth (0-6m at 9 discrete levels) for building typologies
        classified by lateral resistance system (Adb, BrCfl, BrCri, BrM, Rci), code
        level, storeys, and occupancy type.
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
