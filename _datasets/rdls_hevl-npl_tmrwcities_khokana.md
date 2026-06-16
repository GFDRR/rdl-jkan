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
dataset_id: rdls_hevl-npl_tmrwcities_khokana
description: Multi-hazard risk data package for Khokana (Lalitpur), Nepal, providing
  earthquake hazard (OpenQuake Mw 7.8 Gorkha scenario with 500 ground motion field
  realisations), flood hazard (100-year return period multi-model ensemble with historic,
  maximum, and median variants), landslide susceptibility (binary prone area), synthetic
  future urban exposure datasets (buildings, households, individuals, land use) for
  four community planning scenarios (VS1, VS2, VS3, VS5), and multi-hazard impact
  assessment results. Developed as part of the Tomorrow's Cities GCRF Urban Disaster
  Risk Hub project for risk-informed decision making in urban planning.
details: 'The dataset includes: (i) earthquake hazard from OpenQuake scenario simulation
  of the 2015 Mw 7.8 Gorkha earthquake (USGS finite fault us20002926) with 500 ground
  motion field realisations, GMPEs AtkinsonBoore2003SInterNSHMP2008 (50%) and BooreEtAl2014
  (50%), JB2009 correlation model, 14 intensity measures (PGA plus SA at 0.1s-1.3s),
  hypocentre at 28.2305N 84.7314E depth 8.2km; (ii) 100-year return period flood hazard
  GeoTIFFs from multi-model ensemble in historic, maximum (MF_max), and median (MF_med)
  variants with corresponding Excel depth tables; (iii) binary landslide susceptibility
  shapefile; (iv) HVSR ambient vibration measurements and report; (v) four future
  exposure dataset variants (VS1-VS3, VS5) each containing building footprints (10,970
  buildings, 76 typologies) with structural taxonomy, household socio-economic data,
  individual demographics, and land use plans (32 zones, 14 categories); and (vi)
  multi-sheet XLSX impact results disaggregated by hazard type (earthquake, flood)
  and functional impact (uninhabitable residential, non-functional workplace/school/hospital).'
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
    event_count: 1
    events:
    - calculation_method: simulated
      description: 'OpenQuake scenario simulation of the 2015 Mw 7.8 Gorkha earthquake
        using USGS finite fault model (us20002926). Complex fault geometry with top
        edge at 13km and bottom edge at 20km depth. Hypocentre: 28.2305N, 84.7314E,
        depth 8.2km. GMPEs: AtkinsonBoore2003SInterNSHMP2008 (50%) and BooreEtAl2014
        (50%). JB2009 spatial correlation, truncation level 2 sigma, 500 ground motion
        field realisations. 14 intensity measures: PGA, SA(0.1s-1.3s). Scenario 33
        ground motion field selected for analysis.'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_earthquake
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      id: event_earthquake_khokana_gorkha
      occurrence:
        deterministic:
          description: null
          index_criteria: Scenario-based deterministic analysis using 2015 Mw 7.8
            Gorkha earthquake rupture model
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
    id: event_set_earthquake_khokana
    occurrence_range: null
    seasonality: null
  - analysis_type: probabilistic
    calculation_method: simulated
    event_count: 3
    events:
    - calculation_method: simulated
      description: 'Historical 100-year return period flood extent and depth for Khokana.
        File: 100yr_flood_historic_Khok.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_flood
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_flood_khokana_historic
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.01
          probability: null
          return_period: 100
    - calculation_method: simulated
      description: 'Maximum flood extent from multi-model ensemble for 100-year return
        period. Represents worst-case among ensemble members. File: 100yr_flood_MF_max_Khok.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_flood
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_flood_khokana_mf_max
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.01
          probability: null
          return_period: 100
    - calculation_method: simulated
      description: 'Median flood extent from multi-model ensemble for 100-year return
        period. Represents central estimate among ensemble members. File: 100yr_flood_MF_med_Khok.tif'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_flood
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_flood_khokana_mf_med
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
    id: event_set_flood_khokana
    occurrence_range: null
    seasonality: null
  - analysis_type: deterministic
    calculation_method: inferred
    event_count: 1
    events:
    - calculation_method: inferred
      description: Binary landslide susceptibility map indicating landslide-prone
        areas in Khokana. Shapefile with polygon boundaries of susceptible zones.
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_landslide
        intensity_measure: LSI:-
        process: landslide_general
        trigger: null
        type: landslide
      id: event_landslide_khokana
      occurrence:
        deterministic:
          description: null
          index_criteria: Binary susceptibility classification
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
    id: event_set_landslide_khokana
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
    name: OpenQuake earthquake hazard simulation
    risk_data_type: null
    type: model
    url: https://doi.org/10.1016/j.ijdrr.2022.103338
    used_in: hazard
  - id: source_4
    license: null
    name: Multi-model flood ensemble
    risk_data_type: null
    type: model
    url: null
    used_in: hazard
  - id: source_5
    license: null
    name: Landslide susceptibility mapping
    risk_data_type: null
    type: model
    url: null
    used_in: hazard
  - id: source_6
    license: null
    name: HVSR ambient vibration measurements
    risk_data_type: null
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Building damage state results from earthquake impact assessment for
      each vision scenario (VS1, VS2, VS3, VS5). Results disaggregated into uninhabitable
      residential buildings and non-functional workplaces, schools, and hospitals.
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
      vision scenario (VS1, VS2, VS3, VS5). Results disaggregated into uninhabitable
      residential buildings and non-functional workplaces, schools, and hospitals.
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
    description: Affected population results from earthquake impact assessment for
      each vision scenario, derived from building damage states and residential occupancy.
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
    asset_dimension: population
    description: Affected population results from flood impact assessment for each
      vision scenario, derived from building inundation and residential occupancy.
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
purpose: To support multi-hazard risk assessment and risk-informed urban planning
  decision making for Khokana by providing spatial hazard, synthetic future exposure,
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
- access_url: https://data.tomorrowscities.org/dataset/khokana-multi-hazard-dataset
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Multi-hazard dataset containing: (1) Earthquake hazard from OpenQuake
    Mw 7.8 Gorkha scenario simulation (gmf-data_33.csv with 500 realisations, 14 IMs,
    rupture model XML, GMPE logic tree, Vs30 values); (2) 100-year flood GeoTIFFs
    and depth tables for historic, MF_max, and MF_med variants; (3) Landslide-prone
    area shapefile; (4) HVSR ambient vibration survey data. Data formats: CSV, XML,
    GeoTIFF, XLSX, Shapefile, PDF, DOCX.'
  download_url: https://data.tomorrowscities.org/dataset/khokana-multi-hazard-dataset/resource/75e3e7ce-7001-4915-a57b-6eac1593ab44
  format: null
  id: resource_hazard_multihazard
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Khokana Multi Hazard Dataset
- access_url: https://data.tomorrowscities.org/dataset/khokana-future-exposure-dataset-vs1
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:32645
  description: 'Future urban exposure dataset for Vision Scenario 1, including building
    footprints (10,970 buildings, 76 typologies) with structural taxonomy, household
    socio-economic data (15,844 households), individual demographics (70,093 individuals),
    and land use plan (32 zones). Data formats: Shapefile for spatial data, Excel
    (XLSX) for tabular data.'
  download_url: https://data.tomorrowscities.org/dataset/khokana-future-exposure-dataset-vs1/resource/caa62e24-632c-476c-a1af-202d0d8cc474
  format: null
  id: resource_exposure_vs1
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
  title: Khokana Future Exposure Dataset - VS1
- access_url: https://data.tomorrowscities.org/dataset/khokana-future-exposure-dataset-vs2
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:32645
  description: 'Future urban exposure dataset for Vision Scenario 2, including building
    footprints with structural taxonomy, household socio-economic data, individual
    demographics, and land use plan. Data formats: Shapefile for spatial data, Excel
    (XLSX) for tabular data.'
  download_url: https://data.tomorrowscities.org/dataset/khokana-future-exposure-dataset-vs2/resource/88eb88a7-ec02-45f1-9663-361a1dc3aace
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
  title: Khokana Future Exposure Dataset - VS2
- access_url: https://data.tomorrowscities.org/dataset/khokana-future-exposure-dataset-vs3
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:32645
  description: 'Future urban exposure dataset for Vision Scenario 3, including building
    footprints with structural taxonomy, household socio-economic data, individual
    demographics, and land use plan. Data formats: Shapefile for spatial data, Excel
    (XLSX) for tabular data.'
  download_url: https://data.tomorrowscities.org/dataset/khokana-future-exposure-dataset-vs3/resource/8d4b38f5-0b95-415a-bad3-49d530217454
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
  title: Khokana Future Exposure Dataset - VS3
- access_url: https://data.tomorrowscities.org/dataset/khokana-future-exposure-dataset-vs5
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:32645
  description: 'Future urban exposure dataset for Vision Scenario 5, including building
    footprints with structural taxonomy, household socio-economic data, individual
    demographics, and land use plan. Data formats: Shapefile for spatial data, Excel
    (XLSX) for tabular data.'
  download_url: https://data.tomorrowscities.org/dataset/khokana-future-exposure-dataset-vs5/resource/2d4b502e-5b67-40fb-9542-2b1ca5192cc4
  format: null
  id: resource_exposure_vs5
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
  title: Khokana Future Exposure Dataset - VS5
- access_url: https://data.tomorrowscities.org/dataset/khokana-impact-results-vs1
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:32645
  description: 'Multi-hazard impact assessment results for Vision Scenario 1, including
    building damage states disaggregated by hazard type (earthquake, flood) and functional
    impact (uninhabitable residential, non-functional workplace, school, hospital).
    Data format: multi-sheet Excel workbook (XLSX).'
  download_url: https://data.tomorrowscities.org/dataset/kokhana-impact-results-vs1/resource/0d7c78b5-747a-4f60-b8c2-4dd99066962e
  format: null
  id: resource_impact_vs1
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Khokana Impact Results - VS1
- access_url: https://data.tomorrowscities.org/dataset/khokana-impact-results-vs2
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:32645
  description: 'Multi-hazard impact assessment results for Vision Scenario 2, including
    building damage states disaggregated by hazard type (earthquake, flood) and functional
    impact. Data format: multi-sheet Excel workbook (XLSX).'
  download_url: https://data.tomorrowscities.org/dataset/kokhana-impact-results-vs2/resource/862c8ab1-2f94-4ad0-b3f1-64c98d2e01a0
  format: null
  id: resource_impact_vs2
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Khokana Impact Results - VS2
- access_url: https://data.tomorrowscities.org/dataset/khokana-impact-results-vs3
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:32645
  description: 'Multi-hazard impact assessment results for Vision Scenario 3, including
    building damage states disaggregated by hazard type (earthquake, flood) and functional
    impact. Data format: multi-sheet Excel workbook (XLSX).'
  download_url: https://data.tomorrowscities.org/dataset/kokhana-impact-results-vs3/resource/874f5097-23f6-4100-84bf-d57c2a65341f
  format: null
  id: resource_impact_vs3
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Khokana Impact Results - VS3
- access_url: https://data.tomorrowscities.org/dataset/khokana-impact-results-vs5
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:32645
  description: 'Multi-hazard impact assessment results for Vision Scenario 5, including
    building damage states disaggregated by hazard type (earthquake, flood) and functional
    impact. Data format: multi-sheet Excel workbook (XLSX).'
  download_url: https://data.tomorrowscities.org/dataset/kokhana-impact-results-vs5/resource/d87d37d0-e892-4389-8890-d2597cebc8d6
  format: null
  id: resource_impact_vs5
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: Individual building footprint level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Khokana Impact Results - VS5
risk_data_type:
- hazard
- exposure
- vulnerability
- loss
schema: rdls-10
slug: rdls_hevl-npl_tmrwcities_khokana
spatial:
  bbox:
  - 85.2888
  - 27.6067
  - 85.3109
  - 27.6546
  centroid: null
  countries:
  - NPL
  gazetteer_entries:
  - description: Nepal
    id: gazetteer_1
    scheme: GEONAMES
    uri: https://www.geonames.org/1282988/nepal.html
  - description: Lalitpur
    id: gazetteer_2
    scheme: GEONAMES
    uri: https://www.geonames.org/1283240/lalitpur.html
  - description: Khokana
    id: gazetteer_3
    scheme: GEONAMES
    uri: https://www.geonames.org/1283350/khokana.html
  scale: sub-national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Tomorrow's Cities Multi-Hazard Risk Assessment Dataset for Khokana, Nepal
version: '1'
vulnerability: null
---
