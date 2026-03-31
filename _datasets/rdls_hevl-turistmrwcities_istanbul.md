---
catalog: null
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
dataset_id: rdls_hevl-turistmrwcities_istanbul
description: Earthquake risk data package for Istanbul, Turkey, providing 30 simulated
  ground motion fields, synthetic future urban exposure datasets (buildings, households,
  individuals, land use) for six community planning scenarios (Disabled, Elderly,
  Roman, Social, Women, Youth), earthquake fragility functions for buildings, and
  impact assessment results. Developed as part of the Tomorrow's Cities GCRF Urban
  Disaster Risk Hub project for risk-informed decision making in urban planning.
details: "The dataset includes: (i) 30 simulated ground motion field CSVs (GMs_sim_1.csv\
  \ to GMs_sim_30.csv) providing PGA, PGV, and Spectral Acceleration at 25 periods\
  \ (0.05s to 5.066s) for 42 site locations, plus a hazard site GeoJSON with 66 point\
  \ features; (ii) two earthquake fragility function sets \u2014 fragility-IST.xlsx\
  \ with 23 entries and istanbul_fragility_data.xlsx with 41 typologies providing\
  \ lognormal fragility parameters (mu, sigma) for 5 damage states (DS1-DS5); (iii)\
  \ six future exposure dataset variants representing different community planning\
  \ scenarios, each containing building footprints (392 buildings, 85 typologies)\
  \ with structural taxonomy (Adb, RCS, RCi, Sf, Type8, Type10), household socio-economic\
  \ data (7,122 households), individual demographics (22,847 individuals), and land\
  \ use plans (294 zones, 18 categories); and (iv) impact results for each scenario\
  \ including building damage states, impact metrics, and hospital accessibility."
exposure:
  category: buildings, economic_indicator, population
  dimension: population, structure
  quantity_kind: area, count, currency
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
  hazard_type: earthquake
  intensity: PGA:g
  occurrence_range: ''
  processes: ground_motion
  seasonality: ''
license: CC0-1.0
loss:
  approach: ''
  base_data_type: ''
  category: ''
  description: Affected population results from earthquake impact assessment for each
    community planning scenario, derived from building damage states and residential
    occupancy., Building damage state results from earthquake impact assessment for
    each community planning scenario (Disabled, Elderly, Roman, Social, Women, Youth).
    Damage states (DS0-DS5) derived by convolving spectral acceleration hazard with
    building fragility functions., Hospital accessibility impacts from earthquake,
    derived from building damage assessment. Each building has hospital_access boolean
    attribute indicating whether hospital services remain accessible post-earthquake.
  dimension: ''
  exposure_id: ''
  hazard_analysis_type: ''
  hazard_id: ''
  hazard_process: ground_motion
  hazard_type: earthquake
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
purpose: To support earthquake risk assessment and risk-informed urban planning decision
  making for Istanbul by providing simulated ground motion fields, synthetic future
  exposure, fragility functions, and impact assessment datasets for participatory
  community planning scenarios.
resources:
- coordinate_system: EPSG:4326
  description: 'Earthquake hazard dataset containing: (1) 30 simulated ground motion
    field CSVs with PGA, PGV, and SA at 25 periods (0.05s-5.066s) for 42 sites; (2)
    Hazard site GeoJSON with 66 point features and IM values; (3) Fragility functions
    for buildings (41 typologies with 5 damage states, plus 23-entry fragility-IST
    mapping). Data formats: CSV for ground motions, GeoJSON for hazard sites, Excel
    (XLSX) for fragility functions.'
  download_url: https://data.tomorrowscities.org/dataset/istanbul-multi-hazard-dataset/resource/a6b589e3-4d94-4f04-8eb3-0ce66be4b19e
  format: CSV (csv)
  id: resource_hazard_multihazard
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Istanbul Multi Hazard Dataset
- coordinate_system: EPSG:32635
  description: 'Future urban exposure dataset for Disabled community planning scenario,
    including building footprints with structural taxonomy (392 buildings), household
    socio-economic data (7,122 households), individual demographic data (22,847 individuals),
    and land use plan (294 zones). Data formats: Shapefile for building footprints,
    Excel (XLSX) for tabular data.'
  download_url: https://data.tomorrowscities.org/dataset/istanbul-future-exposure-dataset-disabled/resource/38eafa4b-cd66-4e11-bff4-40f4b00d5f22
  format: Shapefile (shp)
  id: resource_exposure_disabled
  media_type: null
  spatial_resolution: null
  temporal:
    duration: P50Y
    end: null
    start: null
    temporal_resolution: null
  title: Istanbul Future Exposure Dataset - Disabled
- coordinate_system: EPSG:32635
  description: 'Future urban exposure dataset for Elderly community planning scenario,
    including building footprints with structural taxonomy, household socio-economic
    data, individual demographic data, and land use plan. Data formats: Shapefile
    for building footprints, Excel (XLSX) for tabular data.'
  download_url: https://data.tomorrowscities.org/dataset/istanbul-future-exposure-dataset-elderly/resource/4a4d08cb-7440-4842-a1e7-2655c94ea4ba
  format: Shapefile (shp)
  id: resource_exposure_elderly
  media_type: null
  spatial_resolution: null
  temporal:
    duration: P50Y
    end: null
    start: null
    temporal_resolution: null
  title: Istanbul Future Exposure Dataset - Elderly
- coordinate_system: EPSG:32635
  description: 'Future urban exposure dataset for Roman community planning scenario,
    including building footprints with structural taxonomy, household socio-economic
    data, individual demographic data, and land use plan. Data formats: Shapefile
    for building footprints, Excel (XLSX) for tabular data.'
  download_url: https://data.tomorrowscities.org/dataset/istanbul-future-exposure-dataset-roman/resource/db58e066-e53e-417e-ba7e-6d03330c3fad
  format: Shapefile (shp)
  id: resource_exposure_roman
  media_type: null
  spatial_resolution: null
  temporal:
    duration: P50Y
    end: null
    start: null
    temporal_resolution: null
  title: Istanbul Future Exposure Dataset - Roman
- coordinate_system: EPSG:32635
  description: 'Future urban exposure dataset for Social community planning scenario,
    including building footprints with structural taxonomy, household socio-economic
    data, individual demographic data, and land use plan. Data formats: Shapefile
    for building footprints, Excel (XLSX) for tabular data.'
  download_url: https://data.tomorrowscities.org/dataset/istanbul-future-exposure-dataset-social/resource/450bbcaa-ebe5-486d-a38f-6f8e5094ccd7
  format: Shapefile (shp)
  id: resource_exposure_social
  media_type: null
  spatial_resolution: null
  temporal:
    duration: P50Y
    end: null
    start: null
    temporal_resolution: null
  title: Istanbul Future Exposure Dataset - Social
- coordinate_system: EPSG:32635
  description: 'Future urban exposure dataset for Women community planning scenario,
    including building footprints with structural taxonomy, household socio-economic
    data, individual demographic data, and land use plan. Data formats: Shapefile
    for building footprints, Excel (XLSX) for tabular data.'
  download_url: https://data.tomorrowscities.org/dataset/istanbul-future-exposure-dataset-women/resource/69192021-faa0-4b84-8f7d-dc2c3fb98ef1
  format: Shapefile (shp)
  id: resource_exposure_women
  media_type: null
  spatial_resolution: null
  temporal:
    duration: P50Y
    end: null
    start: null
    temporal_resolution: null
  title: Istanbul Future Exposure Dataset - Women
- coordinate_system: EPSG:32635
  description: 'Future urban exposure dataset for Youth community planning scenario,
    including building footprints with structural taxonomy, household socio-economic
    data, individual demographic data, and land use plan. Data formats: Shapefile
    for building footprints, Excel (XLSX) for tabular data.'
  download_url: https://data.tomorrowscities.org/dataset/istanbul-future-exposure-dataset-youth/resource/b33c1481-6923-4c24-abd5-bc7375586250
  format: Shapefile (shp)
  id: resource_exposure_youth
  media_type: null
  spatial_resolution: null
  temporal:
    duration: P50Y
    end: null
    start: null
    temporal_resolution: null
  title: Istanbul Future Exposure Dataset - Youth
- coordinate_system: EPSG:4326
  description: 'Impact assessment results for earthquake hazard under the Disabled
    community planning scenario, including building damage states (281 features),
    impact metrics, and hospital accessibility. Data formats: ESRI File Geodatabase
    (GDB), GeoJSON, and Excel (XLSX).'
  download_url: https://data.tomorrowscities.org/dataset/istanbul-impact-results-disabled/resource/66f4ef49-2ac3-4b0b-9876-708a357d7781
  format: File Geodatabase (gdb)
  id: resource_impact_disabled
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Istanbul Impact Results - Disabled
- coordinate_system: EPSG:4326
  description: 'Impact assessment results for earthquake hazard under the Elderly
    community planning scenario, including building damage states, impact metrics,
    and hospital accessibility. Data formats: ESRI File Geodatabase (GDB), GeoJSON,
    and Excel (XLSX).'
  download_url: https://data.tomorrowscities.org/dataset/istanbul-impact-results-elderly/resource/5724966a-4340-411e-a2e9-5a84c79db996
  format: File Geodatabase (gdb)
  id: resource_impact_elderly
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Istanbul Impact Results - Elderly
- coordinate_system: EPSG:4326
  description: 'Impact assessment results for earthquake hazard under the Roman community
    planning scenario, including building damage states, impact metrics, and hospital
    accessibility. Data formats: ESRI File Geodatabase (GDB), GeoJSON, and Excel (XLSX).'
  download_url: https://data.tomorrowscities.org/dataset/istanbul-impact-results-roman/resource/f9343e62-28bc-4c50-ad75-8b364541c71a
  format: File Geodatabase (gdb)
  id: resource_impact_roman
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Istanbul Impact Results - Roman
- coordinate_system: EPSG:4326
  description: 'Impact assessment results for earthquake hazard under the Social community
    planning scenario, including building damage states, impact metrics, and hospital
    accessibility. Data formats: ESRI File Geodatabase (GDB), GeoJSON, and Excel (XLSX).'
  download_url: https://data.tomorrowscities.org/dataset/istanbul-impact-results-social/resource/d049a649-18ed-412b-a7cc-4b44291967c9
  format: File Geodatabase (gdb)
  id: resource_impact_social
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Istanbul Impact Results - Social
- coordinate_system: EPSG:4326
  description: 'Impact assessment results for earthquake hazard under the Women community
    planning scenario, including building damage states, impact metrics, and hospital
    accessibility. Data formats: ESRI File Geodatabase (GDB), GeoJSON, and Excel (XLSX).'
  download_url: https://data.tomorrowscities.org/dataset/istanbul-impact-results-women/resource/e22e8d27-4712-4bd9-8a23-4f08f2b9ffa6
  format: File Geodatabase (gdb)
  id: resource_impact_women
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Istanbul Impact Results - Women
- coordinate_system: EPSG:4326
  description: 'Impact assessment results for earthquake hazard under the Youth community
    planning scenario, including building damage states, impact metrics, and hospital
    accessibility. Data formats: ESRI File Geodatabase (GDB), GeoJSON, and Excel (XLSX).'
  download_url: https://data.tomorrowscities.org/dataset/istanbul-impact-results-youth/resource/b774e776-602a-45d1-9553-84659489b25a
  format: File Geodatabase (gdb)
  id: resource_impact_youth
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Istanbul Impact Results - Youth
risk_data_type:
- hazard
- exposure
- vulnerability
- loss
schema: rdl-03
slug: rdls_hevl-turistmrwcities_istanbul
spatial:
  bbox:
  - 28.5
  - 41.005
  - 28.55
  - 41.03
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
title: Tomorrow's Cities Earthquake Risk Assessment Dataset for Istanbul, Turkey
version: '1'
vulnerability:
  approach: analytical
  base_data_type: simulated
  category: buildings
  dimension: ''
  function_type: ''
  hazard_analysis_type: deterministic
  hazard_primary: earthquake
  hazard_process_primary: ground_motion
  hazard_process_secondary: ''
  hazard_secondary: ''
  intensity: ''
  metric: damage_ratio
  relationship: math_parametric
  taxonomy: Custom
  unit: ''
---
