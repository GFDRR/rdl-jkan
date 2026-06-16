---
attributions:
- entity:
    affiliation: null
    email: null
    name: HeiGIT GAIA Pipeline
    url: https://data.humdata.org/dataset/ecuador---risk-assessment-indicators
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HeiGIT (Heidelberg Institute for Geoinformation Technology)
  url: https://data.humdata.org/dataset/ecuador---risk-assessment-indicators
creator:
  affiliation: null
  email: null
  name: HeiGIT (Heidelberg Institute for Geoinformation Technology)
  url: https://data.humdata.org/dataset/ecuador---risk-assessment-indicators
dataset_id: rdls_hev-ecu_heigit_riskassessmentindicators_2025
description: 'This dataset provides comprehensive Risk Assessment Indicators for Ecuador
  , aggregated at admin level 2 and can in particular be used to perform a structured
  risk assessment for flood hazards. It includes demographic, environmental, infrastructure,
  accessibility, and hazard-related data to support disaster risk and resilience analysis.
  All layers are derived from HeiGIT''s GAIA Pipeline , integrating open data sources
  such as WorldPop , OpenStreetMap , and Google Earth Engine based on HDX COD-AB boundaries.
  Data Overview Access to Services ( ECU_ADM2_access ) Facilities ( ECU_ADM2_facilities
  ) Coping Capacity ( ECU_ADM2_coping ) Demographics ( ECU_ADM2_demographics ) Rural
  Population ( ECU_ADM2_rural_population ) Vulnerability ( ECU_ADM2_vulnerability
  ) Flood Exposure ( ECU_ADM2_flood_exposure ) Indicator Descriptions Access to Services
  ( ECU_ADM2_access ) Represents the share of the population with access to key facilities
  within defined distances or travel times. ADM2_PCODE - Administrative division code
  (ADM2) access_pop_education_5km / 10km / 20km - Population within 5, 10, and 20
  km of educational facilities access_pop_hospitals_30min / 1h / 2h - Population within
  30 minutes, 1 hour, and 2 hours of a hospital access_pop_primary_healthcare_30min
  / 1h / 2h - Population within 30 minutes, 1 hour, and 2 hours of a primary health
  care facility Data Source: openrouteservice (ORS) Facilities ( ECU_ADM2_facilities
  ) Counts of essential service facilities within each district. ADM2_PCODE - Administrative
  division code (ADM2) education_count - Number of educational facilities hospitals_count
  - Number of hospitals primary_healthcare_count - Number of primary health care facilities
  Data Source: OpenStreetMap (OSM) Coping Capacity ( ECU_ADM2_coping ) Combines Access
  to Services and Facilities data to represent a district''s coping capacity. Demographics
  ( ECU_ADM2_demographics ) Shows the population composition by age and gender. ADM2_PCODE
  - Administrative division code (ADM2) female_pop - Total female population children_u5
  - Population under 5 years old female_u5 - Female population under 5 years old elderly
  - Population aged 65 and older pop_u15 - Population under 15 years old female_u15
  - Female population under 15 years old Data Source: Worldpop Rural Population (
  ECU_ADM2_rural_population ) Same demographic breakdown as above, but limited to
  rural populations. Rural areas are those outside urban extents, typically characterized
  by lower population density, agricultural or natural land use, and limited infrastructure
  compared to urban centers. ADM2_PCODE - Administrative division code (ADM2) female_pop_rural
  , children_u5_rural , female_u5_rural , elderly_rural , pop_u15_rural , female_u15_rural
  - Rural demographic counts rural_pop_perc - Percentage of total population living
  in rural areas Data Source: Global Human Settlement Layer (GHSL) Vulnerability (
  ECU_ADM2_vulnerability ) Combines Demographics and Rural Population indicators.
  Flood Exposure ( ECU_ADM2_flood_exposure ) Shows population and facility exposure
  to flooding at 30 cm depth for multiple return periods. ADM2_PCODE - Administrative
  division code (ADM2) female_pop_30cm , children_u5_30cm , female_u5_30cm , elderly_30cm
  , pop_u15_30cm , female_u15_30cm - Exposed population by group education_30cm_pct
  / count , hospitals_30cm_pct / count , primary_healthcare_30cm_pct / count - Facility
  exposure (percentage and count) Data Source: The Joint Research Centre (JRC) QGIS
  Plugin Risk Assessment Inputs Coping Capacity = Access + Facilities Vulnerability
  = Demographics + Rural Population Exposure = Vulnerable Population + Facilities
  exposed to Floods This dataset is part of HeiGIT''s Risk Assessment Indicator Collection
  on HDX. See more at HeiGIT on HDX and learn about HeiGIT''s research at HeiGIT .
  We are happy to hear about your use-cases - contact us at communications@heigit.org
  !. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/ecuador---risk-assessment-indicators]'
details: null
exposure:
- asset_type:
    description: Demographic and rural population data aggregated at admin level 2
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Health facilities and accessibility infrastructure indicators
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: simulated
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: Risk assessment indicators derived through HeiGIT's GAIA Pipeline,
    integrating multiple open data sources to compute demographic, environmental,
    infrastructure, accessibility, and hazard-related metrics aggregated at administrative
    level 2 for Ecuador.
  sources:
  - id: source_1
    license: null
    name: HeiGIT GAIA Pipeline
    risk_data_type:
    - exposure
    type: model
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/ecuador---risk-assessment-indicators
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: This dataset aggregates multiple risk assessment indicators for the country.
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Ecuador - Risk Assessment Indicators (ECU_ADM2_flood_exposure.csv -
    Risk assessment indicator for Ecuador)
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/risk_assessment_inputs/ecu/ECU_ADM2_flood_exposure.csv
  format: null
  id: resource_e35e7476
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ECU_ADM2_flood_exposure.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Ecuador - Risk Assessment Indicators (ECU_ADM2_rural_population.csv
    - Risk assessment indicator for Ecuador)
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/risk_assessment_inputs/ecu/ECU_ADM2_rural_population.csv
  format: null
  id: resource_9d522d68
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ECU_ADM2_rural_population.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Ecuador - Risk Assessment Indicators (ECU_ADM2_demographics.csv - Risk
    assessment indicator for Ecuador)
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/risk_assessment_inputs/ecu/ECU_ADM2_demographics.csv
  format: null
  id: resource_bd1eda3b
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ECU_ADM2_demographics.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Ecuador - Risk Assessment Indicators (ECU_ADM2_facilities.csv - Risk
    assessment indicator for Ecuador)
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/risk_assessment_inputs/ecu/ECU_ADM2_facilities.csv
  format: null
  id: resource_6ab19798
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ECU_ADM2_facilities.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Ecuador - Risk Assessment Indicators (ECU_ADM2_coping.csv - Risk assessment
    indicator for Ecuador)
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/risk_assessment_inputs/ecu/ECU_ADM2_coping.csv
  format: null
  id: resource_a91fb036
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ECU_ADM2_coping.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Ecuador - Risk Assessment Indicators (ECU_ADM2_access.csv - Risk assessment
    indicator for Ecuador)
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/risk_assessment_inputs/ecu/ECU_ADM2_access.csv
  format: null
  id: resource_80f8e4c7
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ECU_ADM2_access.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Ecuador - Risk Assessment Indicators (ECU_ADM2_vulnerability.csv -
    Risk assessment indicator for Ecuador)
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/risk_assessment_inputs/ecu/ECU_ADM2_vulnerability.csv
  format: null
  id: resource_3ed82f0e
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ECU_ADM2_vulnerability.csv
risk_data_type:
- hazard
- exposure
- vulnerability
schema: rdls-10
slug: rdls_hev-ecu_heigit_riskassessmentindicators_2025
spatial:
  bbox: null
  centroid: null
  countries:
  - ECU
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-11-27'
  start: '2025-05-29'
temporal_resolution: null
title: Ecuador - Risk Assessment Indicators
version: null
vulnerability: null
---
