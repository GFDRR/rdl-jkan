---
attributions:
- entity:
    affiliation: null
    email: null
    name: Commissions Mouvements de Populations (CMP)
    url: https://data.humdata.org/dataset/internally-displaced-persons-natural-disaster
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: OIM (International Organization for Migration)
    url: https://data.humdata.org/dataset/internally-displaced-persons-natural-disaster
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: OCHA et Partenaires
    url: https://data.humdata.org/dataset/internally-displaced-persons-natural-disaster
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Democratic Republic of the Congo (DRC)
  url: https://data.humdata.org/dataset/internally-displaced-persons-natural-disaster
creator:
  affiliation: null
  email: null
  name: OCHA Democratic Republic of the Congo (DRC)
  url: https://data.humdata.org/dataset/internally-displaced-persons-natural-disaster
dataset_id: rdls_lss-cod_ochacod_naturaldisasterimpact_2015
description: 'This dataset available on https://ehtools.org contains information on
  population movements due to the impacts of natural hazards in the DRC.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/internally-displaced-persons-natural-disaster]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Post-event impact registry compiled from multiple humanitarian sources
    (CMP, OIM, OCHA) documenting population movements, displacement, and casualties
    resulting from natural hazards in DRC. Data collected through alert-based monitoring
    system with administrative hierarchy tracking and severity classification, covering
    climate-related and weather-related disaster impacts from 2024-2025.
  sources:
  - id: source_1
    license: null
    name: Commissions Mouvements de Populations (CMP)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: OIM (International Organization for Migration)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: OCHA et Partenaires
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/internally-displaced-persons-natural-disaster
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population displacement due to flood hazards
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
        metric: displaced
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population affected by flood hazards
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
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
  - asset_category: population
    asset_dimension: population
    description: Fatalities from flood hazards
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_3
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
  - asset_category: population
    asset_dimension: population
    description: Injuries from flood hazards
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_4
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: ppl_injured
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population displacement due to strong wind hazards
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_5
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
    description: Population affected by strong wind hazards
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_6
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
purpose: Registry
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Natural disaster Impact (Flood data
    from January to november 2025)'
  download_url: https://data.humdata.org/dataset/f576c7d6-ac24-48d4-bb52-e7ce791080a9/resource/6cf2dfed-45ef-4a41-b723-d2230f3e91b5/download/drc_climate-impact-jan-nov-2025.xlsx
  format: null
  id: resource_6cf2dfed
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DRC_climate impact jan-Nov 2025.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Natural disaster Impact (Climatic
    impacts in DRC from March 2022 to August 2024.)'
  download_url: https://data.humdata.org/dataset/f576c7d6-ac24-48d4-bb52-e7ce791080a9/resource/362cd02c-c2e3-47f6-87e2-d990981ab126/download/alert_from_ehtools_202408271724786738.xlsx
  format: null
  id: resource_362cd02c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DRC_Climate impact August 2024
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-cod_ochacod_naturaldisasterimpact_2015
spatial:
  bbox: null
  centroid: null
  countries:
  - COD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-11-27'
  start: '2015-08-12'
temporal_resolution: null
title: 'Democratic Republic of the Congo: Natural disaster Impact'
version: null
vulnerability: null
---
