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
dataset_id: rdls_hevl-tur_tmrwcities_istanbul
description: Earthquake risk data package for Istanbul, Turkey, providing 30 simulated
  ground motion fields, synthetic future urban exposure datasets (buildings, households,
  individuals, land use) for six community planning scenarios (Disabled, Elderly,
  Roman, Social, Women, Youth), earthquake fragility functions for buildings, and
  impact assessment results. Developed as part of the Tomorrow's Cities GCRF Urban
  Disaster Risk Hub project for risk-informed decision making in urban planning.
details: 'The dataset includes: (i) 30 simulated ground motion field CSVs (GMs_sim_1.csv
  to GMs_sim_30.csv) providing PGA, PGV, and Spectral Acceleration at 25 periods (0.05s
  to 5.066s) for 42 site locations, plus a hazard site GeoJSON with 66 point features;
  (ii) two earthquake fragility function sets - fragility-IST.xlsx with 23 entries
  and istanbul_fragility_data.xlsx with 41 typologies providing lognormal fragility
  parameters (mu, sigma) for 5 damage states (DS1-DS5); (iii) six future exposure
  dataset variants representing different community planning scenarios, each containing
  building footprints (392 buildings, 85 typologies) with structural taxonomy (Adb,
  RCS, RCi, Sf, Type8, Type10), household socio-economic data (7,122 households),
  individual demographics (22,847 individuals), and land use plans (294 zones, 18
  categories); and (iv) impact results for each scenario including building damage
  states, impact metrics, and hospital accessibility.'
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
  - analysis_type: deterministic
    calculation_method: simulated
    event_count: 30
    events:
    - calculation_method: simulated
      description: 30 simulated ground motion fields (GMs_sim_1.csv to GMs_sim_30.csv)
        for Istanbul study area providing PGA, PGV, and Spectral Acceleration at 25
        periods (0.05s to 5.066s) for 42 site locations. Each simulation represents
        a stochastic realisation of the earthquake scenario. Hazard site GeoJSON provides
        66 point features with intensity measure values.
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_earthquake
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      id: event_earthquake_istanbul_sim
      occurrence:
        deterministic:
          description: null
          index_criteria: Scenario-based deterministic analysis with 30 stochastic
            ground motion realisations
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
    id: event_set_earthquake_istanbul
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
    name: Earthquake ground motion simulation
    risk_data_type: null
    type: model
    url: null
    used_in: hazard
  - id: source_4
    license: null
    name: Building fragility functions for earthquake
    risk_data_type: null
    type: model
    url: https://doi.org/10.1016/j.ijdrr.2022.103365
    used_in: vulnerability
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Building damage state results from earthquake impact assessment for
      each community planning scenario (Disabled, Elderly, Roman, Social, Women, Youth).
      Damage states (DS0-DS5) derived by convolving spectral acceleration hazard with
      building fragility functions.
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
  - asset_category: population
    asset_dimension: population
    description: Affected population results from earthquake impact assessment for
      each community planning scenario, derived from building damage states and residential
      occupancy.
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
  - asset_category: population
    asset_dimension: disruption
    description: Hospital accessibility impacts from earthquake, derived from building
      damage assessment. Each building has hospital_access boolean attribute indicating
      whether hospital services remain accessible post-earthquake.
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
project:
  name: Tomorrow's Cities - GCRF Urban Disaster Risk Hub
  url: https://tomorrowscities.org/
publisher:
  affiliation: null
  email: support@tomorrowscities.org
  name: Tomorrow's Cities
  url: https://data.tomorrowscities.org/
purpose: To support earthquake risk assessment and risk-informed urban planning decision
  making for Istanbul by providing simulated ground motion fields, synthetic future
  exposure, fragility functions, and impact assessment datasets for participatory
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
- access_url: https://data.tomorrowscities.org/dataset/istanbul-multi-hazard-dataset
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Earthquake hazard dataset containing: (1) 30 simulated ground motion
    field CSVs with PGA, PGV, and SA at 25 periods (0.05s-5.066s) for 42 sites; (2)
    Hazard site GeoJSON with 66 point features and IM values; (3) Fragility functions
    for buildings (41 typologies with 5 damage states, plus 23-entry fragility-IST
    mapping). Data formats: CSV for ground motions, GeoJSON for hazard sites, Excel
    (XLSX) for fragility functions.'
  download_url: https://data.tomorrowscities.org/dataset/istanbul-multi-hazard-dataset/resource/a6b589e3-4d94-4f04-8eb3-0ce66be4b19e
  format: null
  id: resource_hazard_multihazard
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Istanbul Multi Hazard Dataset
- access_url: https://data.tomorrowscities.org/dataset/istanbul-future-exposure-dataset-disabled
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:32635
  description: 'Future urban exposure dataset for Disabled community planning scenario,
    including building footprints with structural taxonomy (392 buildings), household
    socio-economic data (7,122 households), individual demographic data (22,847 individuals),
    and land use plan (294 zones). Data formats: Shapefile for building footprints,
    Excel (XLSX) for tabular data.'
  download_url: https://data.tomorrowscities.org/dataset/istanbul-future-exposure-dataset-disabled/resource/38eafa4b-cd66-4e11-bff4-40f4b00d5f22
  format: null
  id: resource_exposure_disabled
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
  title: Istanbul Future Exposure Dataset - Disabled
- access_url: https://data.tomorrowscities.org/dataset/istanbul-future-exposure-dataset-elderly
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:32635
  description: 'Future urban exposure dataset for Elderly community planning scenario,
    including building footprints with structural taxonomy, household socio-economic
    data, individual demographic data, and land use plan. Data formats: Shapefile
    for building footprints, Excel (XLSX) for tabular data.'
  download_url: https://data.tomorrowscities.org/dataset/istanbul-future-exposure-dataset-elderly/resource/4a4d08cb-7440-4842-a1e7-2655c94ea4ba
  format: null
  id: resource_exposure_elderly
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
  title: Istanbul Future Exposure Dataset - Elderly
- access_url: https://data.tomorrowscities.org/dataset/istanbul-future-exposure-dataset-roman
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:32635
  description: 'Future urban exposure dataset for Roman community planning scenario,
    including building footprints with structural taxonomy, household socio-economic
    data, individual demographic data, and land use plan. Data formats: Shapefile
    for building footprints, Excel (XLSX) for tabular data.'
  download_url: https://data.tomorrowscities.org/dataset/istanbul-future-exposure-dataset-roman/resource/db58e066-e53e-417e-ba7e-6d03330c3fad
  format: null
  id: resource_exposure_roman
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
  title: Istanbul Future Exposure Dataset - Roman
- access_url: https://data.tomorrowscities.org/dataset/istanbul-future-exposure-dataset-social
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:32635
  description: 'Future urban exposure dataset for Social community planning scenario,
    including building footprints with structural taxonomy, household socio-economic
    data, individual demographic data, and land use plan. Data formats: Shapefile
    for building footprints, Excel (XLSX) for tabular data.'
  download_url: https://data.tomorrowscities.org/dataset/istanbul-future-exposure-dataset-social/resource/450bbcaa-ebe5-486d-a38f-6f8e5094ccd7
  format: null
  id: resource_exposure_social
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
  title: Istanbul Future Exposure Dataset - Social
- access_url: https://data.tomorrowscities.org/dataset/istanbul-future-exposure-dataset-women
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:32635
  description: 'Future urban exposure dataset for Women community planning scenario,
    including building footprints with structural taxonomy, household socio-economic
    data, individual demographic data, and land use plan. Data formats: Shapefile
    for building footprints, Excel (XLSX) for tabular data.'
  download_url: https://data.tomorrowscities.org/dataset/istanbul-future-exposure-dataset-women/resource/69192021-faa0-4b84-8f7d-dc2c3fb98ef1
  format: null
  id: resource_exposure_women
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
  title: Istanbul Future Exposure Dataset - Women
- access_url: https://data.tomorrowscities.org/dataset/istanbul-future-exposure-dataset-youth
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:32635
  description: 'Future urban exposure dataset for Youth community planning scenario,
    including building footprints with structural taxonomy, household socio-economic
    data, individual demographic data, and land use plan. Data formats: Shapefile
    for building footprints, Excel (XLSX) for tabular data.'
  download_url: https://data.tomorrowscities.org/dataset/istanbul-future-exposure-dataset-youth/resource/b33c1481-6923-4c24-abd5-bc7375586250
  format: null
  id: resource_exposure_youth
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
  title: Istanbul Future Exposure Dataset - Youth
- access_url: https://data.tomorrowscities.org/dataset/istanbul-impact-results-disabled
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Impact assessment results for earthquake hazard under the Disabled
    community planning scenario, including building damage states (281 features),
    impact metrics, and hospital accessibility. Data formats: ESRI File Geodatabase
    (GDB), GeoJSON, and Excel (XLSX).'
  download_url: https://data.tomorrowscities.org/dataset/istanbul-impact-results-disabled/resource/66f4ef49-2ac3-4b0b-9876-708a357d7781
  format: File Geodatabase (gdb)
  id: resource_impact_disabled
  media_type: null
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Istanbul Impact Results - Disabled
- access_url: https://data.tomorrowscities.org/dataset/istanbul-impact-results-elderly
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Impact assessment results for earthquake hazard under the Elderly
    community planning scenario, including building damage states, impact metrics,
    and hospital accessibility. Data formats: ESRI File Geodatabase (GDB), GeoJSON,
    and Excel (XLSX).'
  download_url: https://data.tomorrowscities.org/dataset/istanbul-impact-results-elderly/resource/5724966a-4340-411e-a2e9-5a84c79db996
  format: File Geodatabase (gdb)
  id: resource_impact_elderly
  media_type: null
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Istanbul Impact Results - Elderly
- access_url: https://data.tomorrowscities.org/dataset/istanbul-impact-results-roman
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Impact assessment results for earthquake hazard under the Roman community
    planning scenario, including building damage states, impact metrics, and hospital
    accessibility. Data formats: ESRI File Geodatabase (GDB), GeoJSON, and Excel (XLSX).'
  download_url: https://data.tomorrowscities.org/dataset/istanbul-impact-results-roman/resource/f9343e62-28bc-4c50-ad75-8b364541c71a
  format: File Geodatabase (gdb)
  id: resource_impact_roman
  media_type: null
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Istanbul Impact Results - Roman
- access_url: https://data.tomorrowscities.org/dataset/istanbul-impact-results-social
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Impact assessment results for earthquake hazard under the Social community
    planning scenario, including building damage states, impact metrics, and hospital
    accessibility. Data formats: ESRI File Geodatabase (GDB), GeoJSON, and Excel (XLSX).'
  download_url: https://data.tomorrowscities.org/dataset/istanbul-impact-results-social/resource/d049a649-18ed-412b-a7cc-4b44291967c9
  format: File Geodatabase (gdb)
  id: resource_impact_social
  media_type: null
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Istanbul Impact Results - Social
- access_url: https://data.tomorrowscities.org/dataset/istanbul-impact-results-women
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Impact assessment results for earthquake hazard under the Women community
    planning scenario, including building damage states, impact metrics, and hospital
    accessibility. Data formats: ESRI File Geodatabase (GDB), GeoJSON, and Excel (XLSX).'
  download_url: https://data.tomorrowscities.org/dataset/istanbul-impact-results-women/resource/e22e8d27-4712-4bd9-8a23-4f08f2b9ffa6
  format: File Geodatabase (gdb)
  id: resource_impact_women
  media_type: null
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Istanbul Impact Results - Women
- access_url: https://data.tomorrowscities.org/dataset/istanbul-impact-results-youth
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Impact assessment results for earthquake hazard under the Youth community
    planning scenario, including building damage states, impact metrics, and hospital
    accessibility. Data formats: ESRI File Geodatabase (GDB), GeoJSON, and Excel (XLSX).'
  download_url: https://data.tomorrowscities.org/dataset/istanbul-impact-results-youth/resource/b774e776-602a-45d1-9553-84659489b25a
  format: File Geodatabase (gdb)
  id: resource_impact_youth
  media_type: null
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Istanbul Impact Results - Youth
risk_data_type:
- hazard
- exposure
- vulnerability
- loss
schema: rdls-10
slug: rdls_hevl-tur_tmrwcities_istanbul
spatial:
  bbox:
  - 28.5
  - 41.005
  - 28.55
  - 41.03
  centroid: null
  countries:
  - TUR
  gazetteer_entries:
  - description: Turkey
    id: gazetteer_1
    scheme: GEONAMES
    uri: https://www.geonames.org/298795/turkey.html
  - description: Istanbul
    id: gazetteer_2
    scheme: GEONAMES
    uri: https://www.geonames.org/745044/istanbul.html
  scale: sub-national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Tomorrow's Cities Earthquake Risk Assessment Dataset for Istanbul, Turkey
version: '1'
vulnerability:
  functions:
    damage_to_loss: []
    engineering_demand: []
    fragility:
    - analysis_details: Lognormal fragility functions for 41 building typologies defining
        probability of exceeding 5 damage states (DS1-DS5) as a function of PGA or
        spectral acceleration (g). Parameters include median (mu) and dispersion (sigma)
        for each damage state. Building taxonomy follows {Material}+{CodeLevel}+{Height}
        pattern where Material includes Adb (Adobe), RCS (RC Shear wall), RCi (RC
        Infilled frame), Sf (Steel frame), Type8, Type10; CodeLevel includes LC (Low
        Code), HC (High Code); Height includes LR (Low-rise), MR (Mid-rise), HR (High-rise).
        Additional fragility set (fragility-IST.xlsx) provides 23 vulnerability string
        entries with period-dependent fragility parameters.
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
    vulnerability: []
---
