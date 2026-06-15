---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
    url: https://data.humdata.org/dataset/the-bahamas-hurricane-dorian-site-assessment-round-3-november-2019
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/the-bahamas-hurricane-dorian-site-assessment-round-3-november-2019
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/the-bahamas-hurricane-dorian-site-assessment-round-3-november-2019
dataset_id: rdls_lss-bhs_iom_bahamasdisplacementhurric_20191105
description: 'This data was collected through 66 key informant interviews across 23
  settlements in the affected areas of between the 30th of October and 5th of November.
  At the time of completion, 5,704 individuals were identified as living in the affected
  settlements in Greater & Little Abaco. This multi-sectoral location assessment has
  been designed with input from the various Emergency Support Functions (ESFs) coordinating
  the Hurricane Dorian response in the Bahamas. It provides an overview of the population
  distribution, needs, and access to services, of returnees, remainees, and evacuees
  across Greater and Little Abaco. This document is part of a series of ongoing efforts
  conducted by IOM to inform service providers, humanitarian actors and donors on
  main needs while reducing survey fatigue of key informants by streamlining assessment
  activities.. [Source: This metadata record was automatically extracted from the
  Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/the-bahamas-hurricane-dorian-site-assessment-round-3-november-2019]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Post-event displacement and needs data collected through 66 key informant
    interviews across 23 settlements in Greater and Little Abaco between 30 October
    and 5 November 2019. The multi-sectoral assessment documented population distribution,
    needs, and service access for returnees, remainees, and evacuees, identifying
    5,704 individuals in affected settlements.
  sources:
  - id: source_1
    license: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/the-bahamas-hurricane-dorian-site-assessment-round-3-november-2019
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population displacement from Hurricane Dorian across affected settlements
      in the Bahamas
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
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
  - asset_category: population
    asset_dimension: population
    description: Affected population identified in post-hurricane site assessment
      across 23 settlements
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
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
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Clean database of Displacement Tracking Matrix Round 3 - the Bahamas
    - Hurricane Dorian
  download_url: https://data.humdata.org/dataset/799e619c-ef79-4101-8a31-50418adbb4a8/resource/038f595a-baaf-4fa2-9b4e-04f7f901ba42/download/dtm_bahamas_msla_data_round_3.xlsx
  format: null
  id: resource_038f595a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM_Bahamas_MSLA_Data_Round_3
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-bhs_iom_bahamasdisplacementhurric_20191105
spatial:
  bbox: null
  centroid: null
  countries:
  - BHS
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2019-11-05'
temporal_resolution: null
title: The Bahamas Displacement - Hurricane Dorian - Site Assessment R3 - [IOM DTM]
version: null
vulnerability: null
---
