---
attributions:
- entity:
    affiliation: null
    email: null
    name: Food and Agriculture Organization (FAO)
    url: https://data.humdata.org/dataset/fao-diem-monitoring-system-household-surveys-aggregated-data
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Food and Agriculture Organization (FAO) of the United Nations
  url: https://data.humdata.org/dataset/fao-diem-monitoring-system-household-surveys-aggregated-data
creator:
  affiliation: null
  email: null
  name: Food and Agriculture Organization (FAO) of the United Nations
  url: https://data.humdata.org/dataset/fao-diem-monitoring-system-household-surveys-aggregated-data
dataset_id: rdls_lss-fao_dataemergenciesmonitoring_2022
description: 'The Food and Agriculture Organization of the United Nations (FAO) has
  developed a monitoring system in 26 food crisis countries to better understand the
  impacts of various shocks on agricultural livelihoods, food security and local value
  chains. The Monitoring System consists of primary data collected from households
  on a periodic basis (more or less every four months, depending on seasonality).
  Data are collected through Computer-Assisted Telephone Interviews (CATI) and in-person
  surveys where the circumstances allow for field access. As the system is developed,
  the information collected and analyzed is being used to guide strategic decisions,
  to design programmes and to inform analytical processes such as the Integrated Phase
  Classification (IPC) and the Humanitarian Needs Overview (HNO). At the core of the
  system is a standardized household questionnaire administered to around 150,000
  households per year across the 26 countries. Standardization permits comparisons
  across time and space, considerably enhancing the utility of the data for decision
  makers. At minimum the household data are representative at Admin 1 level (e.g.
  province, or region) and in frequent cases at Admin 2 level (e.g. district). In
  each aggregated field, the values indicate the frequencies of the different responses,
  expressed as a weighted percentage of the total sample. The present datasets represents
  aggregated data referring to household interviews performed after December 2022.
  At every new survey data release, after cleaning and validation phases, aggregated
  data is appended to the present dataset. For real-time updates, for accessing archived
  data or microdata and for additional survey-specific information, please visit the
  DIEM Hub: https://data-in-emergencies.fao.org/ or contact DIEM View the column descriptions
  here . Metadata available here . Reference administrative boundaries (levels 0,
  1 and 2) available here in GIS format.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/fao-diem-monitoring-system-household-surveys-aggregated-data]'
details: 'Fore more information and API access, visit: https://data-in-emergencies.fao.org/.
  Monitoring system app: https://data-in-emergencies.fao.org/pages/monitoring Reference
  administrative boundaries(levels 0, 1 and 2): https://data-in-emergencies.fao.org/maps/3596c3ad318849068eda21517ade30be/about
  Questionnaires used for data collection available [here](https://data-in-emergencies.fao.org/search?tags=household%20survey%20questionnaire''here'').'
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: FAO DIEM collects primary household survey data from agricultural producers
    in 26 food crisis countries through Computer-Assisted Telephone Interviews and
    field surveys on a periodic basis (approximately every four months). Data are
    aggregated by administrative level and thematic area (food security, crop production,
    livestock production, income shocks and needs) to monitor impacts of various shocks
    on agricultural livelihoods and food security.
  sources:
  - id: source_1
    license: null
    name: Food and Agriculture Organization (FAO)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/fao-diem-monitoring-system-household-surveys-aggregated-data
  rel: source
loss:
  losses:
  - asset_category: agriculture
    asset_dimension: product
    description: Agricultural livelihood impacts from drought and food security shocks
      affecting crop and livestock producers
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
          unit: null
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Sample Survey
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: FAO Data in Emergencies Monitoring System (DIEM) (Income, shocks and
    needs thematic areas.)
  download_url: https://data.humdata.org/dataset/e9942071-bf80-4216-9175-044720b82e6f/resource/766c7b22-b8b0-49b4-9cd5-9e1aa558799d/download/diem_aggregated_data_income__shocks_and_needs_thematic_areas.csv
  format: null
  id: resource_766c7b22
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DIEM_household_surveys_aggregated_data_(income_shocks_and_needs_thematic_areas).csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: FAO Data in Emergencies Monitoring System (DIEM) (Food security thematic
    area.)
  download_url: https://data.humdata.org/dataset/e9942071-bf80-4216-9175-044720b82e6f/resource/72f98532-6663-4c0d-b835-aa7d19e3b59b/download/diem_aggregated_data_food_security_thematic_area.csv
  format: null
  id: resource_72f98532
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DIEM_household_surveys_aggregated_data_(food_security_thematic_area).csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: FAO Data in Emergencies Monitoring System (DIEM) (Livestock production
    thematic area.)
  download_url: https://data.humdata.org/dataset/e9942071-bf80-4216-9175-044720b82e6f/resource/11237acc-4854-4482-b357-b56313e110d7/download/diem_aggregated_data_livestock_production_thematic_area.csv
  format: null
  id: resource_11237acc
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DIEM_household_surveys_aggregated_data_(livestock_production_thematic_area).csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: FAO Data in Emergencies Monitoring System (DIEM) (Crop production thematic
    area.)
  download_url: https://data.humdata.org/dataset/e9942071-bf80-4216-9175-044720b82e6f/resource/b60b6404-ac25-4df6-a3fe-0feaf366fed6/download/diem_aggregated_data_crop_production_thematic_area.csv
  format: null
  id: resource_b60b6404
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DIEM_household_surveys_aggregated_data_(crop_production_thematic_area).csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-fao_dataemergenciesmonitoring_2022
spatial:
  bbox: null
  centroid: null
  countries:
  - COD
  - IRQ
  - PSE
  - YEM
  - AFG
  - BDI
  - BEN
  - BFA
  - CAF
  - TCD
  - COG
  - DZA
  - ERI
  - ETH
  - GMB
  - GIN
  - GNB
  - HTI
  - KEN
  - LBR
  - LBY
  - MLI
  - MOZ
  - NER
  - NGA
  - SEN
  - SOM
  - SSD
  - SYR
  - UGA
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-08-19'
  start: '2022-12-01'
temporal_resolution: null
title: FAO Data in Emergencies Monitoring System (DIEM)
version: null
vulnerability: null
---
