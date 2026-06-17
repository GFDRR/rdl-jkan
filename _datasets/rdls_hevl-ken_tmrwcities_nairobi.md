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
dataset_id: rdls_hevl-ken_tmrwcities_nairobi
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
  - analysis_type: probabilistic
    calculation_method: simulated
    event_count: 1
    events:
    - calculation_method: simulated
      description: '100-year return period flood depth for Nairobi provided as vector
        point grid GeoJSON (127,422 point features). Each point contains IM (intensity
        measure / water depth in metres) and projected x/y coordinates. File: _nairobi_flood_depth_100yr.geojson'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_flood
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_flood_nairobi_100yr
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.01
          probability: null
          return_period: 100
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_flood_nairobi
    occurrence_range: null
    seasonality: null
  type: flood
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
    name: Flood hazard modelling
    risk_data_type: null
    type: model
    url: null
    used_in: hazard
  - id: source_4
    license: null
    name: Depth-damage vulnerability functions for flood
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
    description: Building damage state results from flood impact assessment for each
      community planning scenario (Business, Elders, Women, Youth1, Youth2).
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
    description: Affected population results from flood impact assessment for each
      community planning scenario.
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
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
purpose: To support flood risk assessment and risk-informed urban planning decision
  making for Nairobi by providing spatial hazard, synthetic future exposure, vulnerability
  functions, and impact assessment datasets for participatory community planning scenarios.
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
- access_url: https://data.tomorrowscities.org/dataset/nairobi-multi-hazard-dataset
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Flood hazard dataset containing: (1) 100-year return period flood
    depth GeoJSON (127,422 point features with IM/depth values); (2) Flood depth-damage
    vulnerability functions for 6,300 building typologies in JSON columnar dict format.
    Note: Only flood hazard present despite Multi Hazard naming.'
  download_url: https://data.tomorrowscities.org/dataset/nairobi-multi-hazard-dataset/resource/e5f04bdc-5409-4558-874b-d79b3649a6b6
  format: null
  id: resource_hazard_multihazard
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Nairobi Multi Hazard Dataset
- access_url: https://data.tomorrowscities.org/dataset/nairobi-future-exposure-dataset-business
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Business community planning scenario,
    including building footprints (5,815 buildings, 116 typologies) with structural
    taxonomy, household data, individual demographics, and land use plan (110 zones).
    Data formats: GeoJSON for spatial data, XLSX for tabular data.'
  download_url: https://data.tomorrowscities.org/dataset/nairobi-future-exposure-dataset-business/resource/84f14e0d-0d20-42cd-9610-b79066e6e788
  format: null
  id: resource_exposure_business
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
  title: Nairobi Future Exposure Dataset - Business
- access_url: https://data.tomorrowscities.org/dataset/nairobi-future-exposure-dataset-elders
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Elders community planning scenario.
    Data formats: GeoJSON, XLSX.'
  download_url: https://data.tomorrowscities.org/dataset/nairobi-future-exposure-dataset-elders/resource/8c58c990-b4ff-4067-b152-405258ddd001
  format: null
  id: resource_exposure_elders
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
  title: Nairobi Future Exposure Dataset - Elders
- access_url: https://data.tomorrowscities.org/dataset/nairobi-future-exposure-dataset-women
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Women community planning scenario.
    Data formats: GeoJSON, XLSX.'
  download_url: https://data.tomorrowscities.org/dataset/nairobi-future-exposure-dataset-women/resource/bc4e5e3e-b6bc-412c-974f-8fe33ac8f478
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
  title: Nairobi Future Exposure Dataset - Women
- access_url: https://data.tomorrowscities.org/dataset/nairobi-future-exposure-dataset-youth1
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Youth Group 1 community planning
    scenario. Data formats: GeoJSON, XLSX.'
  download_url: https://data.tomorrowscities.org/dataset/nairobi-future-exposure-dataset-youth1/resource/86c505f3-95d4-4da5-bb2b-f15d85eb64c8
  format: null
  id: resource_exposure_youth1
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
  title: Nairobi Future Exposure Dataset - Youth1
- access_url: https://data.tomorrowscities.org/dataset/nairobi-future-exposure-dataset-youth2
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Future urban exposure dataset for Youth Group 2 community planning
    scenario. Data formats: GeoJSON, XLSX.'
  download_url: https://data.tomorrowscities.org/dataset/nairobi-future-exposure-dataset-youth2/resource/a28e7d87-0f82-4658-80cf-ecfba8de3ad8
  format: null
  id: resource_exposure_youth2
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
  title: Nairobi Future Exposure Dataset - Youth2
- access_url: https://data.tomorrowscities.org/dataset/nairobi-impact-results-business
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Flood impact assessment results for Business scenario, including building
    damage states and impact metrics. Data formats: GeoJSON, File Geodatabase (GDB).'
  download_url: https://data.tomorrowscities.org/dataset/nairobi-impact-results-business/resource/662f53c0-25b5-458a-8f8a-cbbd1eb46623
  format: File Geodatabase (gdb)
  id: resource_impact_business
  media_type: null
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Nairobi Impact Results - Business
- access_url: https://data.tomorrowscities.org/dataset/nairobi-impact-results-elders
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Flood impact assessment results for Elders scenario. Data formats:
    GeoJSON, File Geodatabase (GDB).'
  download_url: https://data.tomorrowscities.org/dataset/nairobi-impact-results-elders/resource/7f442350-a96b-46bc-86d7-8c2646128032
  format: File Geodatabase (gdb)
  id: resource_impact_elders
  media_type: null
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Nairobi Impact Results - Elders
- access_url: https://data.tomorrowscities.org/dataset/nairobi-impact-results-women
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Flood impact assessment results for Women scenario. Data formats:
    GeoJSON, File Geodatabase (GDB).'
  download_url: https://data.tomorrowscities.org/dataset/nairobi-impact-results-women/resource/33925fbe-41fb-4df7-b52e-10563f421362
  format: File Geodatabase (gdb)
  id: resource_impact_women
  media_type: null
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Nairobi Impact Results - Women
- access_url: https://data.tomorrowscities.org/dataset/nairobi-impact-results-youth1
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Flood impact assessment results for Youth Group 1 scenario. Data formats:
    GeoJSON, File Geodatabase (GDB).'
  download_url: https://data.tomorrowscities.org/dataset/nairobi-impact-results-youth1/resource/5eb24c6b-9187-435e-b314-6f1e0bc28cab
  format: File Geodatabase (gdb)
  id: resource_impact_youth1
  media_type: null
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Nairobi Impact Results - Youth1
- access_url: https://data.tomorrowscities.org/dataset/nairobi-impact-results-youth2
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Flood impact assessment results for Youth Group 2 scenario. Data formats:
    GeoJSON, File Geodatabase (GDB).'
  download_url: https://data.tomorrowscities.org/dataset/nairobi-impact-results-youth2/resource/d01bba13-cd3f-4605-b518-fff9473f7bf4
  format: File Geodatabase (gdb)
  id: resource_impact_youth2
  media_type: null
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Nairobi Impact Results - Youth2
risk_data_type:
- hazard
- exposure
- vulnerability
- loss
schema: rdls-10
slug: rdls_hevl-ken_tmrwcities_nairobi
spatial:
  bbox:
  - 36.8
  - -1.35
  - 36.9
  - -1.25
  centroid: null
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
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Tomorrow's Cities Flood Risk Assessment Dataset for Nairobi, Kenya
version: '1'
vulnerability:
  functions:
    damage_to_loss: []
    engineering_demand: []
    fragility: []
    socio_economic: []
    vulnerability:
    - analysis_details: 'Depth-damage vulnerability functions defining damage ratio
        as a function of water depth (0-6m at 9 discrete levels: 0, 0.5, 1, 1.5, 2,
        3, 4, 5, 6m) for 6,300 building typologies classified by lateral resistance
        system (Adb, BrCfl, BrCri, BrM, RCi), code level (LC, MC, HC), storeys, and
        occupancy type (Res, ResCom, Com, Edu, Hea, Ind). Functions based on consultation
        with local partners and JRC global flood depth-damage database.'
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
