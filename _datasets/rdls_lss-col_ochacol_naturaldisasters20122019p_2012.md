---
attributions:
- entity:
    affiliation: null
    email: null
    name: "Unidad Nacional de Gesti\xF3n de Riesgos y Desastres - UNGRD"
    url: https://data.humdata.org/dataset/afectados-por-desastres-naturales-2012-2019
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Colombia
  url: https://data.humdata.org/dataset/afectados-por-desastres-naturales-2012-2019
creator:
  affiliation: null
  email: null
  name: OCHA Colombia
  url: https://data.humdata.org/dataset/afectados-por-desastres-naturales-2012-2019
dataset_id: rdls_lss-col_ochacol_naturaldisasters20122019p_2012
description: 'Natural Disasters 2012-2019 (people affected) - Afectados por desastres
  naturales 2012-2019. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/afectados-por-desastres-naturales-2012-2019]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Registry data compiled by UNGRD documenting people affected by natural
    disasters in Colombia during 2012-2019. The dataset aggregates impact records
    from multiple disaster events across hazard types, providing post-event counts
    of affected populations at the national scale.
  sources:
  - id: source_1
    license: null
    name: "Unidad Nacional de Gesti\xF3n de Riesgos y Desastres - UNGRD"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/afectados-por-desastres-naturales-2012-2019
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: People affected by natural disasters including floods
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
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
    description: People affected by natural disasters including earthquakes
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_2
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
    description: People affected by natural disasters including storms
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_3
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
    description: People affected by natural disasters including landslides
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_4
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
  description: Colombia - Natural Disasters 2012-2019 (people affected) - Afectados
    por desastres naturales 2012-2019 (Afectados por desastres naturales 2012-2019)
  download_url: https://docs.google.com/spreadsheets/d/1C4lL6AZADSf_lhH73SCzKbnzY3y81CWOHQTvz8NfupE/edit?usp=drive_web&ouid=117103371495663051607
  format: null
  id: resource_4c9a263a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Afectados por desastres naturales 2012-2019
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-col_ochacol_naturaldisasters20122019p_2012
spatial:
  bbox: null
  centroid: null
  countries:
  - COL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2019-06-30'
  start: '2012-01-01'
temporal_resolution: null
title: Colombia - Natural Disasters 2012-2019 (people affected) - Afectados por desastres
  naturales 2012-2019
version: null
vulnerability: null
---
