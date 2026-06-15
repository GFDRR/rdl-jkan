---
attributions:
- entity:
    affiliation: null
    email: null
    name: ACU Population Monitoring
    url: https://data.humdata.org/dataset/population-displacement-and-return-movements-in-northern-syria
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: HNAP statistics
    url: https://data.humdata.org/dataset/population-displacement-and-return-movements-in-northern-syria
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Local councils
    url: https://data.humdata.org/dataset/population-displacement-and-return-movements-in-northern-syria
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Assistance Coordination Unit
  url: https://data.humdata.org/dataset/population-displacement-and-return-movements-in-northern-syria
creator:
  affiliation: null
  email: null
  name: Assistance Coordination Unit
  url: https://data.humdata.org/dataset/population-displacement-and-return-movements-in-northern-syria
dataset_id: rdls_el-syr_acu_northernpopulationtrackin_20241001
description: 'This dashboard monitors the population movements in Northern Syria in
  non-governmental areas. The data is collected from the communities and IDP camps
  in the targeted area by the ACU field enumerators and triangulated with various
  sources like the local councils and humanitarian organizations to ensure the maximum
  level of accuracy. The baseline was set by cross-checking the population numbers
  from ACU Population Monitoring and HNAP statistics. RESIDENT POPULATION: Resident
  populations are individuals or households living in a location and are neither displaced
  nor newly returned (in the current calendar year). INTERNALLY DISPLACED PERSONS
  (IDPs): individuals who have been forced to flee their location of origin to another
  location within Syria for at least one month. RETURNEES: are individuals who returned
  to their community of origin within the calendar year and have stayed for at least
  one month after having previously fled for at least one month. Newly INTERNALLY
  DISPLACED PERSONS (N-IDPs): individuals who have been forced to flee their location
  of origin to another location within Syria, and at the time of the data collection,
  their stay in the displacement sites did not exceed one month. Departures: individuals
  who were not in their original locations during the data collection period and had
  left their locations for about a month.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/population-displacement-and-return-movements-in-northern-syria]'
details: null
exposure:
- asset_type:
    description: Resident population, internally displaced persons, and returnees
      tracked across Northern Syria communities and IDP camps
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
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Population tracking data collected through direct field enumeration
    by ACU enumerators in Northern Syria communities and IDP camps, triangulated with
    local councils and humanitarian organization sources (HNAP), and cross-validated
    against baseline statistics to establish resident, displaced, and returnee population
    counts.
  sources:
  - id: source_1
    license: null
    name: ACU Population Monitoring
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: HNAP statistics
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: Local councils
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/population-displacement-and-return-movements-in-northern-syria
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced population counts resulting from conflict-driven
      displacement in Northern Syria
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
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
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Syria Population Tracking - October 2024.xlsx
  download_url: https://data.humdata.org/dataset/7bfbbfb3-fd01-462f-9682-6279cebc3cc3/resource/083183d9-1443-4b90-bfbc-1f5afdfe3969/download/northern-syria-population-tracking-october-2024.xlsx
  format: null
  id: resource_083183d9
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Northern Syria Population Tracking - October 2024.xlsx
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-syr_acu_northernpopulationtrackin_20241001
spatial:
  bbox: null
  centroid: null
  countries:
  - SYR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-10-01'
temporal_resolution: null
title: Northern Syria Population Tracking
version: null
vulnerability: null
---
