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
dataset_id: rdls_hevl-pse_tmrwcities_nablus
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
- asset_type:
    description: Building exposure derived from OpenStreetMap footprints, classified
      using a city-specific structural taxonomy for the risk assessment
    id: Custom
    scheme: Custom
    title: Building taxonomy
    uri: null
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
    event_count: 1
    events:
    - calculation_method: simulated
      description: Earthquake ground motion for rupture scenario 4 (rup4) provided
        as multiband GeoTIFF raster with multiple intensity measures. Structural fragility
        defined in OpenQuake NRML 0.5 discrete format with PGA range 0.05-2.0g at
        30 discrete levels.
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_earthquake
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      id: event_earthquake_nablus_rup4
      occurrence:
        deterministic:
          description: null
          index_criteria: Scenario-based deterministic analysis for rupture scenario
            4
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
    id: event_set_earthquake_nablus
    occurrence_range: null
    seasonality: null
  - analysis_type: deterministic
    calculation_method: simulated
    event_count: 1
    events:
    - calculation_method: simulated
      description: 'Future high-emission climate flood depth scenario (YVS) for Nablus
        providing flood water depth as GeoTIFF raster. File: Nablus_flood_depth_future_high_YVS.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_flood
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_flood_nablus_future_high
      occurrence:
        deterministic:
          description: null
          index_criteria: Future high-emission climate scenario
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
    id: event_set_flood_nablus
    occurrence_range: null
    seasonality: null
  - analysis_type: deterministic
    calculation_method: simulated
    event_count: 1
    events:
    - calculation_method: simulated
      description: 'Earthquake-triggered landslide susceptibility raster derived from
        coupling rup4 ground motion with slope stability analysis. File: eq-landslide-rup4.tif.
        Note: All 3,631 buildings show DS=0 (no landslide damage) in impact results.'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_landslide
        intensity_measure: LSI:-
        process: landslide_general
        trigger: null
        type: landslide
      id: event_landslide_nablus_eq_triggered
      occurrence:
        deterministic:
          description: null
          index_criteria: Earthquake-triggered landslide scenario
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
    id: event_set_landslide_nablus
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
    name: Earthquake hazard simulation
    risk_data_type: null
    type: model
    url: null
    used_in: hazard
  - id: source_4
    license: null
    name: Flood hazard modelling
    risk_data_type: null
    type: model
    url: null
    used_in: hazard
  - id: source_5
    license: null
    name: Earthquake-triggered landslide modelling
    risk_data_type: null
    type: model
    url: null
    used_in: hazard
  - id: source_6
    license: null
    name: OpenQuake structural fragility functions
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
    name: Power and road infrastructure fragility
    risk_data_type: null
    type: model
    url: null
    used_in: vulnerability
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Building damage state results from earthquake impact assessment for
      each community planning scenario (Apartment Buildings, Civil Societies, Community
      Service, Women, Youth).
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
      community planning scenario.
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
  - asset_category: buildings
    asset_dimension: structure
    description: 'Building damage state results from earthquake-triggered landslide
      assessment. Note: All buildings currently show DS=0 (no landslide damage) in
      available results.'
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
    description: Casualty results from earthquake impact assessment for each community
      planning scenario.
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
    asset_dimension: disruption
    description: Hospital accessibility and power availability impacts from earthquake
      and flood, derived from road network connectivity analysis and power network
      damage assessment. Each building has hospital_access and has_power boolean attributes.
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
    description: Road network and power infrastructure damage from earthquake impact
      assessment, including road edge and node damage states.
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
    description: Road network damage from flood impact assessment, with road edges
      flagged as damaged/undamaged based on flood inundation.
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
project:
  name: Tomorrow's Cities - GCRF Urban Disaster Risk Hub
  url: https://tomorrowscities.org/
publisher:
  affiliation: null
  email: support@tomorrowscities.org
  name: Tomorrow's Cities
  url: https://data.tomorrowscities.org/
purpose: To support multi-hazard risk assessment and risk-informed urban planning
  decision making for Nablus by providing spatial hazard, synthetic future exposure,
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
- access_url: https://data.tomorrowscities.org/dataset/nablus-multi-hazard-dataset
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Multi-hazard dataset containing: (1) Earthquake multiband GeoTIFF
    for rup4 scenario with ground motion IMs; (2) OpenQuake NRML structural fragility
    XML (discrete, PGA, 4 DS), power fragility (18 types), road fragility (29 types);
    (3) Future high-emission flood depth GeoTIFF (YVS scenario) with vulnerability
    functions for 91 typologies; Data formats: GeoTIFF, XML, XLSX.'
  download_url: https://data.tomorrowscities.org/dataset/nablus-multi-hazard-dataset/resource/a4aac9d1-7ccb-4dcf-af98-234641fbdc75
  format: null
  id: resource_hazard_multihazard
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Nablus Multi Hazard Dataset
- access_url: https://data.tomorrowscities.org/dataset/nablus-future-exposure-dataset-apartment-buildings
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Apartment Buildings community planning
    scenario, including building footprints (3,631 buildings, 80 typologies in GEM
    Taxonomy v2.0) with structural attributes, household data (9,704 households),
    individual demographics (59,580 individuals), and land use plan (35 zones). Data
    formats: GeoJSON for spatial data, JSON and XLSX for tabular data.'
  download_url: https://data.tomorrowscities.org/dataset/nablus-future-exposure-dataset-apartment-buildings/resource/b9a2a521-4b99-48b2-ba16-fc50ba9dc279
  format: null
  id: resource_exposure_apartment_buildings
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
  title: Nablus Future Exposure Dataset - Apartment Buildings
- access_url: https://data.tomorrowscities.org/dataset/nablus-future-exposure-dataset-civil-societies
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Civil Societies community planning
    scenario, including building footprints with structural taxonomy, household data,
    individual demographics, and land use plan. Data formats: GeoJSON, JSON, XLSX.'
  download_url: https://data.tomorrowscities.org/dataset/nablus-future-exposure-dataset-civil-societies/resource/76a0adc4-947a-4037-8cc2-a20f78540d45
  format: null
  id: resource_exposure_civil_societies
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
  title: Nablus Future Exposure Dataset - Civil Societies
- access_url: https://data.tomorrowscities.org/dataset/nablus-future-exposure-dataset-community-service
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Community Service planning scenario,
    including building footprints with structural taxonomy, household data, individual
    demographics, and land use plan. Data formats: GeoJSON, JSON, XLSX.'
  download_url: https://data.tomorrowscities.org/dataset/nablus-future-exposure-dataset-community-service/resource/7663f6dd-b8f5-4e20-8450-1705fab1f992
  format: null
  id: resource_exposure_community_service
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
  title: Nablus Future Exposure Dataset - Community Service
- access_url: https://data.tomorrowscities.org/dataset/nablus-future-exposure-dataset-women
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Women community planning scenario,
    including building footprints with structural taxonomy, household data, individual
    demographics, and land use plan. Data formats: GeoJSON, JSON, XLSX.'
  download_url: https://data.tomorrowscities.org/dataset/nablus-future-exposure-dataset-women/resource/b4558674-4acf-43b3-b7ef-02b6ff6a63f0
  format: null
  id: resource_exposure_women
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
  title: Nablus Future Exposure Dataset - Women
- access_url: https://data.tomorrowscities.org/dataset/nablus-future-exposure-dataset-youth
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Youth community planning scenario,
    including building footprints with structural taxonomy, household data, individual
    demographics, and land use plan. Data formats: GeoJSON, JSON, XLSX.'
  download_url: https://data.tomorrowscities.org/dataset/nablus-future-exposure-dataset-youth/resource/38366625-3e58-4137-bea7-0b67ddce4888
  format: null
  id: resource_exposure_youth
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
  title: Nablus Future Exposure Dataset - Youth
- access_url: https://data.tomorrowscities.org/dataset/nablus-impact-results-apartment-buildings
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Multi-hazard impact assessment results for Apartment Buildings scenario,
    including earthquake, flood, and landslide building damage states, casualties,
    hospital accessibility, power availability, and road network disruption. Data
    formats: GeoJSON, GeoTIFF.'
  download_url: https://data.tomorrowscities.org/dataset/nablus-impact-results-apartment-buildings/resource/223813ce-e9ae-4a15-875b-b48cbfef4a2c
  format: null
  id: resource_impact_apartment_buildings
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Nablus Impact Results - Apartment Buildings
- access_url: https://data.tomorrowscities.org/dataset/nablus-impact-results-civil-societies
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Multi-hazard impact assessment results for Civil Societies scenario.
    Data formats: GeoJSON, GeoTIFF.'
  download_url: https://data.tomorrowscities.org/dataset/nablus-impact-results-civil-societies/resource/c468a110-1e7f-48b8-83b3-61ea0a2ddfcd
  format: null
  id: resource_impact_civil_societies
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Nablus Impact Results - Civil Societies
- access_url: https://data.tomorrowscities.org/dataset/nablus-impact-results-community-service
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Multi-hazard impact assessment results for Community Service scenario.
    Data formats: GeoJSON, GeoTIFF.'
  download_url: https://data.tomorrowscities.org/dataset/nablus-impact-results-community-service/resource/3831127e-f092-4492-ac8b-b680d2868d48
  format: null
  id: resource_impact_community_service
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Nablus Impact Results - Community Service
- access_url: https://data.tomorrowscities.org/dataset/nablus-impact-results-women
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Multi-hazard impact assessment results for Women scenario. Data formats:
    GeoJSON, GeoTIFF.'
  download_url: https://data.tomorrowscities.org/dataset/nablus-impact-results-women/resource/6b321b7a-a33e-4513-83ed-95caf84ef89a
  format: null
  id: resource_impact_women
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Nablus Impact Results - Women
- access_url: https://data.tomorrowscities.org/dataset/nablus-impact-results-youth
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Multi-hazard impact assessment results for Youth scenario. Data formats:
    GeoJSON, GeoTIFF.'
  download_url: https://data.tomorrowscities.org/dataset/nablus-impact-results-youth/resource/b46d7d8d-9e2f-4c4f-a171-cd9e4c708889
  format: null
  id: resource_impact_youth
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Nablus Impact Results - Youth
risk_data_type:
- hazard
- exposure
- vulnerability
- loss
schema: rdls-10
slug: rdls_hevl-pse_tmrwcities_nablus
spatial:
  bbox:
  - 35.22
  - 32.19
  - 35.3
  - 32.25
  centroid: null
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
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Tomorrow's Cities Multi-Hazard Risk Assessment Dataset for Nablus, Palestine
version: '1'
vulnerability:
  functions:
    damage_to_loss: []
    engineering_demand: []
    fragility:
    - analysis_details: 'OpenQuake NRML 0.5 discrete fragility functions for building
        typologies using GEM Building Taxonomy v2.0 (e.g., CR+CIP/LDUAL+DUM+HC+2s+Edu).
        PGA intensity measure with 30 discrete levels from 0.05g to 2.0g. Four damage
        states: slight, moderate, extensive, complete. No-damage limit: 0.05g.'
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
      relationship: discrete
      taxonomy: Custom
    - analysis_details: Fragility functions for 18 power infrastructure types providing
        lognormal parameters (median PGA and beta) for 4 damage states (slight, moderate,
        extensive, complete). Also includes 29 road type fragility functions with
        median and dispersion parameters.
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
      taxonomy: Custom
    socio_economic: []
    vulnerability:
    - analysis_details: 'Depth-damage vulnerability functions defining damage ratio
        as a function of water depth (0-6m at 9 discrete levels: 0, 0.5, 1, 1.5, 2,
        3, 4, 5, 6m) for 91 building typologies. Functions based on consultation with
        local partners and JRC global flood depth-damage database.'
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
---
