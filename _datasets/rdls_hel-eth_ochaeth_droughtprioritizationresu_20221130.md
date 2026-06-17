---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Ethiopia
  url: https://data.humdata.org/dataset/ethiopia-drought-prioritization-results
creator:
  affiliation: null
  email: null
  name: OCHA Ethiopia
  url: https://data.humdata.org/dataset/ethiopia-drought-prioritization-results
dataset_id: rdls_hel-eth_ochaeth_droughtprioritizationresu_20221130
description: 'Dataset provides the prioritization results of the drought affected
  areas in Ethiopia.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/ethiopia-drought-prioritization-results]'
details: null
exposure:
- asset_type:
    description: Population in drought-affected areas prioritized for humanitarian
      response
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
    description: Agricultural land and livelihoods affected by drought conditions
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_2
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: inferred
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: SPI:-
      process: meteorological_drought
      trigger: null
      type: drought
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: drought
license: CC-BY-4.0
lineage:
  description: Drought-affected areas in Ethiopia were prioritized using a multi-criteria
    assessment methodology that integrates drought severity indicators and vulnerability
    factors to identify populations and regions requiring humanitarian response. The
    results classify geographic areas by priority level for drought intervention.
  sources:
  - id: source_1
    license: null
    name: OCHA Ethiopia
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/ethiopia-drought-prioritization-results
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by drought in prioritized areas
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
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: agriculture
    asset_dimension: product
    description: Agricultural losses and livelihood impacts from drought
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
          unit: null
        metric: loss
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
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://www.humanitarianresponse.info/sites/www.humanitarianresponse.info/files/documents/files/ethiopia_-_drought_priority_areas_-_november_2022.pdf
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Ethiopia - Drought Prioritization Results (Excel)
  download_url: https://data.humdata.org/dataset/4a63ddeb-ca64-4af6-9a03-976ab4db1fe5/resource/032bba27-456d-45d2-b9f1-1c2b783c62ff/download/ethiopia_november_2022_drought_operational_prioritization_results.xlsx
  format: null
  id: resource_032bba27
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Ethiopia_November_2022_Drought_Operational_Prioritization_Results.xlsx
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-eth_ochaeth_droughtprioritizationresu_20221130
spatial:
  bbox: null
  centroid: null
  countries:
  - ETH
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-11-30'
temporal_resolution: null
title: Ethiopia - Drought Prioritization Results
version: null
vulnerability: null
---
