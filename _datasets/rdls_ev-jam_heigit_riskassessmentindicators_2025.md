---
attributions:
- entity:
    affiliation: null
    email: null
    name: HeiGIT GAIA Pipeline
    url: https://data.humdata.org/dataset/jamaica---risk-assessment-indicators
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HeiGIT (Heidelberg Institute for Geoinformation Technology)
  url: https://data.humdata.org/dataset/jamaica---risk-assessment-indicators
creator:
  affiliation: null
  email: null
  name: HeiGIT (Heidelberg Institute for Geoinformation Technology)
  url: https://data.humdata.org/dataset/jamaica---risk-assessment-indicators
dataset_id: rdls_ev-jam_heigit_riskassessmentindicators_2025
description: 'This dataset provides comprehensive Risk Assessment Indicators for Jamaica
  , aggregated at admin level 2 and can in particular be used to perform a structured
  risk assessment for flood and cyclone hazards. It includes demographic, environmental,
  infrastructure, accessibility, and hazard-related data to support disaster risk
  and resilience analysis. All layers are derived from HeiGIT''s GAIA Pipeline , integrating
  open data sources such as WorldPop , OpenStreetMap , and Google Earth Engine based
  on HDX COD-AB boundaries. Data Overview Access to Services ( JAM_ADM2_access ) Facilities
  ( JAM_ADM2_facilities ) Coping Capacity ( JAM_ADM2_coping ) Demographics ( JAM_ADM2_demographics
  ) Rural Population ( JAM_ADM2_rural_population ) Vulnerability ( JAM_ADM2_vulnerability
  ) Flood Exposure ( JAM_ADM2_flood_exposure ) Cyclone Exposure ( JAM_ADM2_cyclone_exposure
  ) Indicator Descriptions Access to Services ( JAM_ADM2_access ) Represents the share
  of the population with access to key facilities within defined distances or travel
  times. ADM2_PCODE - Administrative division code (ADM2) access_pop_education_5km
  / 10km / 20km - Population within 5, 10, and 20 km of educational facilities access_pop_hospitals_30min
  / 1h / 2h - Population within 30 minutes, 1 hour, and 2 hours of a hospital access_pop_primary_healthcare_30min
  / 1h / 2h - Population within 30 minutes, 1 hour, and 2 hours of a primary health
  care facility Data Source: openrouteservice (ORS) Facilities ( JAM_ADM2_facilities
  ) Counts of essential service facilities within each district. ADM2_PCODE - Administrative
  division code (ADM2) education_count - Number of educational facilities hospitals_count
  - Number of hospitals primary_healthcare_count - Number of primary health care facilities
  Data Source: OpenStreetMap (OSM) Coping Capacity ( JAM_ADM2_coping ) Combines Access
  to Services and Facilities data to represent a district''s coping capacity. Demographics
  ( JAM_ADM2_demographics ) Shows the population composition by age and gender. ADM2_PCODE
  - Administrative division code (ADM2) female_pop - Total female population children_u5
  - Population under 5 years old female_u5 - Female population under 5 years old elderly
  - Population aged 65 and older pop_u15 - Population under 15 years old female_u15
  - Female population under 15 years old Data Source: Worldpop Rural Population (
  JAM_ADM2_rural_population ) Same demographic breakdown as above, but limited to
  rural populations. Rural areas are those outside urban extents, typically characterized
  by lower population density, agricultural or natural land use, and limited infrastructure
  compared to urban centers. ADM2_PCODE - Administrative division code (ADM2) female_pop_rural
  , children_u5_rural , female_u5_rural , elderly_rural , pop_u15_rural , female_u15_rural
  - Rural demographic counts rural_pop_perc - Percentage of total population living
  in rural areas Data Source: Global Human Settlement Layer (GHSL) Vulnerability (
  JAM_ADM2_vulnerability ) Combines Demographics and Rural Population indicators.
  Flood Exposure ( JAM_ADM2_flood_exposure ) Shows population and facility exposure
  to flooding at 30 cm depth for multiple return periods. ADM2_PCODE - Administrative
  division code (ADM2) female_pop_30cm , children_u5_30cm , female_u5_30cm , elderly_30cm
  , pop_u15_30cm , female_u15_30cm - Exposed population by group education_30cm_pct
  / count , hospitals_30cm_pct / count , primary_healthcare_30cm_pct / count - Facility
  exposure (percentage and count) Data Source: The Joint Research Centre (JRC) Cyclone
  Exposure ( JAM_ADM2_cyclone_exposure ) Represents the exposure of populations and
  facilities to cyclones, based on historical cyclone tracks and intensity categories
  (1-3). Vulnerable populations and facilities are quantified per admin unit. ADM2_PCODE
  - Administrative division code (ADM2) kt34_female_pop_cat1 / cat2 / cat3 , kt34_children_u5_cat1
  / cat2 / cat3 , etc. - Population exposed to cyclone categories 1-3 kt34_education_perc
  / count_cat1 / cat2 / cat3 , kt34_hospitals_perc / count_cat1 / cat2 / cat3 , kt34_primary_healthcare_perc
  / count_cat1 / cat2 / cat3 - Facilities exposed to cyclone categories Data Source:
  IBTrACS - NOAA International Best Track Archive for Climate Stewardship QGIS Plugin
  Risk Assessment Inputs Coping Capacity = Access + Facilities Vulnerability = Demographics
  + Rural Population Exposure = Vulnerable Population + Facilities exposed to Floods
  and Cyclones This dataset is part of HeiGIT''s Risk Assessment Indicator Collection
  on HDX. See more at HeiGIT on HDX and learn about HeiGIT''s research at HeiGIT .
  We are happy to hear about your use-cases - contact us at communications@heigit.org
  !. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/jamaica---risk-assessment-indicators]'
details: null
exposure:
- asset_type:
    description: Rural and total population at risk to flood and cyclone hazards
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
    description: Health facilities and accessibility infrastructure
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
hazard: null
license: CC-BY-SA-4.0
lineage:
  description: Risk assessment indicators were aggregated from multiple sources at
    Jamaica's admin level 2 boundaries using HeiGIT's GAIA processing pipeline. The
    dataset integrates demographic, environmental, infrastructure, accessibility,
    and hazard-related data to support structured risk assessment for flood and cyclone
    hazards.
  sources:
  - id: source_1
    license: null
    name: HeiGIT GAIA Pipeline
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/jamaica---risk-assessment-indicators
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
  description: Jamaica - Risk Assessment Indicators (JAM_ADM2_flood_exposure.csv -
    Risk assessment indicator for Jamaica)
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/risk_assessment_inputs/jam/JAM_ADM2_flood_exposure.csv
  format: null
  id: resource_df6abc86
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: JAM_ADM2_flood_exposure.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Jamaica - Risk Assessment Indicators (JAM_ADM2_vulnerability.csv -
    Risk assessment indicator for Jamaica)
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/risk_assessment_inputs/jam/JAM_ADM2_vulnerability.csv
  format: null
  id: resource_cb4cdaa5
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: JAM_ADM2_vulnerability.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Jamaica - Risk Assessment Indicators (JAM_ADM2_rural_population.csv
    - Risk assessment indicator for Jamaica)
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/risk_assessment_inputs/jam/JAM_ADM2_rural_population.csv
  format: null
  id: resource_4f2ae470
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: JAM_ADM2_rural_population.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Jamaica - Risk Assessment Indicators (JAM_ADM2_access.csv - Risk assessment
    indicator for Jamaica)
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/risk_assessment_inputs/jam/JAM_ADM2_access.csv
  format: null
  id: resource_497e05cd
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: JAM_ADM2_access.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Jamaica - Risk Assessment Indicators (JAM_ADM2_facilities.csv - Risk
    assessment indicator for Jamaica)
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/risk_assessment_inputs/jam/JAM_ADM2_facilities.csv
  format: null
  id: resource_b4bfb295
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: JAM_ADM2_facilities.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Jamaica - Risk Assessment Indicators (JAM_ADM2_cyclone_exposure.csv
    - Risk assessment indicator for Jamaica)
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/risk_assessment_inputs/jam/JAM_ADM2_cyclone_exposure.csv
  format: null
  id: resource_c6e66715
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: JAM_ADM2_cyclone_exposure.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Jamaica - Risk Assessment Indicators (JAM_ADM2_coping.csv - Risk assessment
    indicator for Jamaica)
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/risk_assessment_inputs/jam/JAM_ADM2_coping.csv
  format: null
  id: resource_a89e9e76
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: JAM_ADM2_coping.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Jamaica - Risk Assessment Indicators (JAM_ADM2_demographics.csv - Risk
    assessment indicator for Jamaica)
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/risk_assessment_inputs/jam/JAM_ADM2_demographics.csv
  format: null
  id: resource_db6afdb5
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: JAM_ADM2_demographics.csv
risk_data_type:
- exposure
- vulnerability
schema: rdls-10
slug: rdls_ev-jam_heigit_riskassessmentindicators_2025
spatial:
  bbox: null
  centroid: null
  countries:
  - JAM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-11-27'
  start: '2025-05-29'
temporal_resolution: null
title: Jamaica - Risk Assessment Indicators
version: null
vulnerability: null
---
