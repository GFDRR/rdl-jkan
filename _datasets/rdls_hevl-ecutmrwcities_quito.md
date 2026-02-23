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
dataset_id: rdls_hevl-ecutmrwcities_quito
description: Multi-hazard risk data package for Santa Rosa district, Quito, Ecuador,
  providing earthquake hazard (2 PGA scenarios as XLSX grid data), debris flow hazard
  (1 depth scenario), flood vulnerability functions (no flood depth data), synthetic
  future urban exposure datasets (buildings, households, land use) for three community
  planning scenarios (VS0, VS2, VS3), and multi-hazard impact assessment results.
  Developed as part of the Tomorrow's Cities GCRF Urban Disaster Risk Hub project
  for risk-informed decision making in urban planning.
details: "The dataset includes: (i) earthquake hazard as 2 XLSX PGA scenario grids\
  \ (EQ-SCEN1-PGA.xlsx, EQ-SCEN2-PGA.xlsx) with 499 points providing X/Y projected\
  \ coordinates and IM (PGA in g), earthquake fragility for 11 building typologies\
  \ (5 damage states DS1-DS5 with SA intensity measure and period-dependent parameters),\
  \ debris flow fragility for 11 typologies; (ii) debris flow depth scenario (DF-SCEN01-DPTH.xlsx,\
  \ 3.0 MB) with depth values; (iii) flood vulnerability functions for 1,260 building\
  \ typologies at 9 water depths (0-6m) \u2014 note: no flood depth hazard map provided,\
  \ flood assessed through debris flow depth proxy; (iv) three future exposure dataset\
  \ variants (VS0: Santa Rosa baseline, VS2: Vision 2, VS3: Vision 3; VS1 absent)\
  \ each containing building footprints (333 buildings) with structural taxonomy,\
  \ household data (497 households), and land use plans (6 zones, 2 residential types);\
  \ and (v) multi-hazard impact results including metrics.txt summary files with damage\
  \ distribution and impact metrics (metric3-metric8) for both basic (v1) and enhanced\
  \ (v2) analysis versions."
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
  calculation_method: simulated
  disaster_identifiers: ''
  hazard_analysis_type: deterministic
  hazard_type: earthquake, landslide
  intensity: PGA:g, wd:m
  occurrence_range: ''
  processes: ground_motion, landslide_mudflow
  seasonality: ''
license: CC0-1.0
loss:
  approach: ''
  base_data_type: ''
  category: ''
  description: Affected population metrics from multi-hazard impact assessment including
    homeless households/individuals (metric5/metric6), hospital access disruption
    (metric3/metric4), and total reposition value for damaged buildings (metric8).,
    Building damage state results from debris flow impact assessment for each vision
    scenario., Building damage state results from earthquake impact assessment for
    each vision scenario (VS0, VS2, VS3) and both earthquake scenarios (SCEN1, SCEN2),
    with basic (v1) and enhanced (v2) analysis versions.
  dimension: ''
  exposure_id: ''
  hazard_analysis_type: ''
  hazard_id: ''
  hazard_process: ground_motion, landslide_mudflow
  hazard_type: earthquake, landslide
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
  decision making for Quito (Santa Rosa district) by providing spatial hazard, synthetic
  future exposure, vulnerability/fragility functions, and impact assessment datasets
  for participatory community planning scenarios.
resources:
- coordinate_system: null
  description: 'Multi-hazard dataset containing: (1) 2 earthquake PGA scenario XLSX
    grids (499 points each); (2) 1 debris flow depth scenario XLSX (3.0 MB); (3) Earthquake
    fragility for 11 typologies (DS1-DS5); (4) Debris flow fragility for 11 typologies;
    (5) Flood vulnerability for 1,260 typologies (no flood depth data provided). All
    hazard data is tabular (XLSX), not raster.'
  download_url: https://data.tomorrowscities.org/dataset/quito-multi-hazard-dataset/resource/ac00a37d-ecd5-4a3e-bc04-4cea0484324a
  format: Excel (xlsx)
  id: resource_hazard_multihazard
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Quito Multi Hazard Dataset
- coordinate_system: EPSG:32717
  description: 'Future urban exposure dataset for VS0 (Santa Rosa baseline), including
    building footprints (333 buildings) with structural taxonomy, household data (497
    households), and land use plan (6 zones). Data formats: Shapefile for spatial
    data, Excel (XLSX) for tabular data. No individual-level data.'
  download_url: https://data.tomorrowscities.org/dataset/quito-future-exposure-dataset-vs0/resource/c4a322ef-935f-46b6-9421-d256fbd35bee
  format: Shapefile (shp)
  id: resource_exposure_vs0
  media_type: null
  spatial_resolution: null
  temporal:
    duration: P50Y
    end: null
    start: null
    temporal_resolution: null
  title: Quito Future Exposure Dataset - VS0
- coordinate_system: EPSG:32717
  description: 'Future urban exposure dataset for Vision Scenario 2. Data formats:
    Shapefile, XLSX.'
  download_url: https://data.tomorrowscities.org/dataset/quito-future-exposure-dataset-vs2/resource/f1515843-2259-4e69-93e1-8a5f98bd1993
  format: Shapefile (shp)
  id: resource_exposure_vs2
  media_type: null
  spatial_resolution: null
  temporal:
    duration: P50Y
    end: null
    start: null
    temporal_resolution: null
  title: Quito Future Exposure Dataset - VS2
- coordinate_system: EPSG:32717
  description: 'Future urban exposure dataset for Vision Scenario 3. Data formats:
    Shapefile, XLSX.'
  download_url: https://data.tomorrowscities.org/dataset/quito-future-exposure-dataset-vs3/resource/702720b9-35ef-401e-8dee-221088f2f385
  format: Shapefile (shp)
  id: resource_exposure_vs3
  media_type: null
  spatial_resolution: null
  temporal:
    duration: P50Y
    end: null
    start: null
    temporal_resolution: null
  title: Quito Future Exposure Dataset - VS3
- coordinate_system: null
  description: 'Multi-hazard impact results for VS0 including earthquake (2 scenarios,
    basic v1 and enhanced v2), debris flow, and flood damage. Contains metrics.txt
    summaries with building damage distributions and impact metrics (metric3-metric8).
    Data formats: CSV, TXT.'
  download_url: https://data.tomorrowscities.org/dataset/quito-impact-results-vs0/resource/2686985e-842a-4458-9156-6ae2fb90b1cf
  format: CSV (csv)
  id: resource_impact_vs0
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Quito Impact Results - VS0
- coordinate_system: null
  description: 'Multi-hazard impact results for Vision Scenario 2. Data formats: CSV,
    TXT.'
  download_url: https://data.tomorrowscities.org/dataset/quito-impact-results-vs2/resource/8023e4e8-55fa-49e3-8ae1-86fecf4aaeb4
  format: CSV (csv)
  id: resource_impact_vs2
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Quito Impact Results - VS2
- coordinate_system: null
  description: 'Multi-hazard impact results for Vision Scenario 3. Data formats: CSV,
    TXT.'
  download_url: https://data.tomorrowscities.org/dataset/quito-impact-results-vs3/resource/7c794f1a-95ab-414d-994b-62ef77936729
  format: CSV (csv)
  id: resource_impact_vs3
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Quito Impact Results - VS3
risk_data_type:
- hazard
- exposure
- vulnerability
- loss
schema: rdl-03
slug: rdls_hevl-ecutmrwcities_quito
spatial:
  bbox:
  - -78.58
  - -0.32
  - -78.54
  - -0.28
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
title: Tomorrow's Cities Multi-Hazard Risk Assessment Dataset for Quito (Santa Rosa),
  Ecuador
version: '1'
vulnerability:
  approach: analytical
  base_data_type: simulated
  category: buildings
  dimension: ''
  function_type: ''
  hazard_analysis_type: deterministic
  hazard_primary: earthquake, flood, landslide
  hazard_process_primary: fluvial_flood, ground_motion, landslide_mudflow
  hazard_process_secondary: ''
  hazard_secondary: ''
  intensity: ''
  metric: damage_ratio
  relationship: discrete, math_parametric
  taxonomy: Custom
  unit: ''
---
