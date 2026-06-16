---
attributions:
- entity:
    affiliation: null
    email: null
    name: OCHA Situation Reports
    url: https://data.humdata.org/dataset/ukraine-key-figures-2022
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: FTS (Financial Tracking Service)
    url: https://data.humdata.org/dataset/ukraine-key-figures-2022
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Flash Appeal
    url: https://data.humdata.org/dataset/ukraine-key-figures-2022
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX
  url: https://data.humdata.org/dataset/ukraine-key-figures-2022
creator:
  affiliation: null
  email: null
  name: HDX
  url: https://data.humdata.org/dataset/ukraine-key-figures-2022
dataset_id: rdls_lss-ukr_hdx_keyfigures_2022
description: 'Key Figures extracted from Ukraine Flash Appeal, FTS and the daily Situation
  Reports.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/ukraine-key-figures-2022]'
details: Key Figures extracted from Ukraine Flash Appeal, FTS and the daily SitReps
  (i.e https://reliefweb.int/sites/reliefweb.int/files/resources/2022-03-07_Ukraine%20Humanitarian%20Impact%20SitRep_final.pdf)
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Key figures aggregated from OCHA Situation Reports, FTS funding data,
    and Flash Appeal documents to compile consolidated impact metrics including affected
    population and casualty counts from the Ukraine humanitarian crisis.
  sources:
  - id: source_1
    license: null
    name: OCHA Situation Reports
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: FTS (Financial Tracking Service)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: Flash Appeal
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/ukraine-key-figures-2022
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Total affected population from the Ukraine conflict and humanitarian
      crisis
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
        metric: exposure
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Casualty figures from the Ukraine conflict
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
        metric: casualty_count
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
purpose: Registry
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Ukraine Key Figures (Key figures)
  download_url: https://docs.google.com/spreadsheets/d/e/2PACX-1vQIdedbZz0ehRC0b4fsWiP14R7MdtU1mpmwAkuXUPElSah2AWCURKGALFDuHjvyJUL8vzZAt3R1B5qg/pub?output=csv
  format: null
  id: resource_22fb535c
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Key figures
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ukr_hdx_keyfigures_2022
spatial:
  bbox: null
  centroid: null
  countries:
  - UKR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-07-31'
  start: '2022-03-03'
temporal_resolution: null
title: Ukraine Key Figures
version: null
vulnerability: null
---
