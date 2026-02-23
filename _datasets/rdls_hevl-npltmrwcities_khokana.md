---
contact_point:
  email: emin.mentese@anofa.co
  id: attribution_contact
  name: "Mente\u015Fe, E.Y. - Anofa Engineering, Planning and Informatics Ltd."
  url: https://orcid.org/0000-0002-7187-4384
creator:
  email: support@tomorrowscities.org
  id: attribution_creator
  name: Tomorrow's Cities
  url: https://data.tomorrowscities.org/
dataset_id: rdls_hevl-npltmrwcities_khokana
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
- category: buildings
  dimension: structure
  quantity_kind: area, count, currency
  taxonomy: GED4ALL
- category: population
  dimension: population
  quantity_kind: count
  taxonomy: GED4ALL
- category: economic_indicator
  dimension: structure
  quantity_kind: area
  taxonomy: GED4ALL
extra_attributions:
- email: press@ukri.org
  id: attribution_funder
  name: Natural Environment Research Council (NERC)
  role: funder
  url: https://www.ukri.org/councils/nerc/
- email: servicedesk@ucl.ac.uk
  id: attribution_collaborator
  name: University College London
  role: collaborator
  url: https://www.ucl.ac.uk/
hazard:
  calculation_method: inferred, simulated
  disaster_identifiers: ''
  hazard_analysis_type: deterministic, probabilistic
  hazard_type: earthquake, flood, landslide
  intensity: PGA:g, susceptibility, wd:m
  occurrence_range: ''
  processes: fluvial_flood, ground_motion, landslide_general
  seasonality: ''
license: CC0-1.0
loss:
  approach: ''
  base_data_type: ''
  category: ''
  description: Affected population results from earthquake impact assessment for each
    vision scenario, derived from building damage states and residential occupancy.,
    Affected population results from flood impact assessment for each vision scenario,
    derived from building inundation and residential occupancy., Building damage state
    results from earthquake impact assessment for each vision scenario (VS1, VS2,
    VS3, VS5). Results disaggregated into uninhabitable residential buildings and
    non-functional workplaces, schools, and hospitals., Building damage state results
    from flood impact assessment for each vision scenario (VS1, VS2, VS3, VS5). Results
    disaggregated into uninhabitable residential buildings and non-functional workplaces,
    schools, and hospitals.
  dimension: ''
  exposure_id: ''
  hazard_analysis_type: ''
  hazard_id: ''
  hazard_process: fluvial_flood, ground_motion
  hazard_type: earthquake, flood
  impact_metric: ''
  impact_type: ''
  impact_unit: ''
  type: ''
  vulnerability_id: ''
project:
  name: Tomorrow's Cities - GCRF Urban Disaster Risk Hub
  url: https://tomorrowscities.org/
publisher:
  email: support@tomorrowscities.org
  id: attribution_publisher
  name: Tomorrow's Cities
  url: https://data.tomorrowscities.org/
purpose: To support multi-hazard risk assessment and risk-informed urban planning
  decision making for Khokana by providing spatial hazard, synthetic future exposure,
  and impact assessment datasets for participatory community planning scenarios.
resources:
- coordinate_system: EPSG:4326
  description: 'Multi-hazard dataset containing: (1) Earthquake hazard from OpenQuake
    Mw 7.8 Gorkha scenario simulation (gmf-data_33.csv with 500 realisations, 14 IMs,
    rupture model XML, GMPE logic tree, Vs30 values); (2) 100-year flood GeoTIFFs
    and depth tables for historic, MF_max, and MF_med variants; (3) Landslide-prone
    area shapefile; (4) HVSR ambient vibration survey data. Data formats: CSV, XML,
    GeoTIFF, XLSX, Shapefile, PDF, DOCX.'
  download_url: https://data.tomorrowscities.org/dataset/khokana-multi-hazard-dataset/resource/75e3e7ce-7001-4915-a57b-6eac1593ab44
  format: GeoTIFF (tif)
  id: resource_hazard_multihazard
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Khokana Multi Hazard Dataset
- coordinate_system: EPSG:32645
  description: 'Future urban exposure dataset for Vision Scenario 1, including building
    footprints (10,970 buildings, 76 typologies) with structural taxonomy, household
    socio-economic data (15,844 households), individual demographics (70,093 individuals),
    and land use plan (32 zones). Data formats: Shapefile for spatial data, Excel
    (XLSX) for tabular data.'
  download_url: https://data.tomorrowscities.org/dataset/khokana-future-exposure-dataset-vs1/resource/caa62e24-632c-476c-a1af-202d0d8cc474
  format: Shapefile (shp)
  id: resource_exposure_vs1
  media_type: null
  spatial_resolution: null
  temporal:
    duration: P50Y
    end: null
    start: null
    temporal_resolution: null
  title: Khokana Future Exposure Dataset - VS1
- coordinate_system: EPSG:32645
  description: 'Future urban exposure dataset for Vision Scenario 2, including building
    footprints with structural taxonomy, household socio-economic data, individual
    demographics, and land use plan. Data formats: Shapefile for spatial data, Excel
    (XLSX) for tabular data.'
  download_url: https://data.tomorrowscities.org/dataset/khokana-future-exposure-dataset-vs2/resource/88eb88a7-ec02-45f1-9663-361a1dc3aace
  format: Shapefile (shp)
  id: resource_exposure_vs2
  media_type: null
  spatial_resolution: null
  temporal:
    duration: P50Y
    end: null
    start: null
    temporal_resolution: null
  title: Khokana Future Exposure Dataset - VS2
- coordinate_system: EPSG:32645
  description: 'Future urban exposure dataset for Vision Scenario 3, including building
    footprints with structural taxonomy, household socio-economic data, individual
    demographics, and land use plan. Data formats: Shapefile for spatial data, Excel
    (XLSX) for tabular data.'
  download_url: https://data.tomorrowscities.org/dataset/khokana-future-exposure-dataset-vs3/resource/8d4b38f5-0b95-415a-bad3-49d530217454
  format: Shapefile (shp)
  id: resource_exposure_vs3
  media_type: null
  spatial_resolution: null
  temporal:
    duration: P50Y
    end: null
    start: null
    temporal_resolution: null
  title: Khokana Future Exposure Dataset - VS3
- coordinate_system: EPSG:32645
  description: 'Future urban exposure dataset for Vision Scenario 5, including building
    footprints with structural taxonomy, household socio-economic data, individual
    demographics, and land use plan. Data formats: Shapefile for spatial data, Excel
    (XLSX) for tabular data.'
  download_url: https://data.tomorrowscities.org/dataset/khokana-future-exposure-dataset-vs5/resource/2d4b502e-5b67-40fb-9542-2b1ca5192cc4
  format: Shapefile (shp)
  id: resource_exposure_vs5
  media_type: null
  spatial_resolution: null
  temporal:
    duration: P50Y
    end: null
    start: null
    temporal_resolution: null
  title: Khokana Future Exposure Dataset - VS5
- coordinate_system: EPSG:32645
  description: 'Multi-hazard impact assessment results for Vision Scenario 1, including
    building damage states disaggregated by hazard type (earthquake, flood) and functional
    impact (uninhabitable residential, non-functional workplace, school, hospital).
    Data format: multi-sheet Excel workbook (XLSX).'
  download_url: https://data.tomorrowscities.org/dataset/kokhana-impact-results-vs1/resource/0d7c78b5-747a-4f60-b8c2-4dd99066962e
  format: Excel (xlsx)
  id: resource_impact_vs1
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Khokana Impact Results - VS1
- coordinate_system: EPSG:32645
  description: 'Multi-hazard impact assessment results for Vision Scenario 2, including
    building damage states disaggregated by hazard type (earthquake, flood) and functional
    impact. Data format: multi-sheet Excel workbook (XLSX).'
  download_url: https://data.tomorrowscities.org/dataset/kokhana-impact-results-vs2/resource/862c8ab1-2f94-4ad0-b3f1-64c98d2e01a0
  format: Excel (xlsx)
  id: resource_impact_vs2
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Khokana Impact Results - VS2
- coordinate_system: EPSG:32645
  description: 'Multi-hazard impact assessment results for Vision Scenario 3, including
    building damage states disaggregated by hazard type (earthquake, flood) and functional
    impact. Data format: multi-sheet Excel workbook (XLSX).'
  download_url: https://data.tomorrowscities.org/dataset/kokhana-impact-results-vs3/resource/874f5097-23f6-4100-84bf-d57c2a65341f
  format: Excel (xlsx)
  id: resource_impact_vs3
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Khokana Impact Results - VS3
- coordinate_system: EPSG:32645
  description: 'Multi-hazard impact assessment results for Vision Scenario 5, including
    building damage states disaggregated by hazard type (earthquake, flood) and functional
    impact. Data format: multi-sheet Excel workbook (XLSX).'
  download_url: https://data.tomorrowscities.org/dataset/kokhana-impact-results-vs5/resource/d87d37d0-e892-4389-8890-d2597cebc8d6
  format: Excel (xlsx)
  id: resource_impact_vs5
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Khokana Impact Results - VS5
risk_data_type:
- hazard
- exposure
- vulnerability
- loss
schema: rdl-03
slug: rdls_hevl-npltmrwcities_khokana
spatial:
  bbox:
  - 85.2888
  - 27.6067
  - 85.3109
  - 27.6546
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
title: Tomorrow's Cities Multi-Hazard Risk Assessment Dataset for Khokana, Nepal
version: '1'
vulnerability:
  approach: ''
  base_data_type: ''
  category: ''
  dimension: ''
  function_type: ''
  hazard_analysis_type: ''
  hazard_primary: ''
  hazard_process_primary: ''
  hazard_process_secondary: ''
  hazard_secondary: ''
  intensity: ''
  metric: ''
  relationship: ''
  taxonomy: ''
  unit: ''
---
