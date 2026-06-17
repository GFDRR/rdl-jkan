---
attributions:
- entity:
    affiliation: null
    email: null
    name: Humanitarian partner organisations
    url: https://data.humdata.org/dataset/somalia-cumulative-drought-response-2022
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Somalia
  url: https://data.humdata.org/dataset/somalia-cumulative-drought-response-2022
creator:
  affiliation: null
  email: null
  name: OCHA Somalia
  url: https://data.humdata.org/dataset/somalia-cumulative-drought-response-2022
dataset_id: rdls_hl-som_ochasom_cumulativedroughtresponse_2022
description: 'This data is produced by OCHA Somalia in collaboration with humanitarian
  partners. It provides information on the worsening drought situation in Somalia
  in 2022. It indicates the drought response by clusters in this period. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/somalia-cumulative-drought-response-2022]'
details: null
exposure: []
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: observed
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
  description: OCHA Somalia compiled cumulative drought response data from multiple
    humanitarian partner organizations operating through the cluster system during
    the 2022 drought crisis. The dataset aggregates affected population figures and
    cluster-level response information collected through humanitarian coordination
    mechanisms to document the scale and progression of the drought impact.
  sources:
  - id: source_1
    license: null
    name: OCHA Somalia
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Humanitarian partner organisations
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/somalia-cumulative-drought-response-2022
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Cumulative affected population from drought response operations across
      clusters
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
        modelling: simulated
        type: total
      loss_approach: analytical
      loss_frequency_type: probabilistic
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
  description: Somalia - Cumulative Drought Response (Excel)
  download_url: https://data.humdata.org/dataset/f0432d4c-d2f9-40f3-9b76-85352ec931c0/resource/a22a5c1a-5282-4ece-be0b-bf2dcf60d207/download/somalia-cumulative_drought_response_jan-june-1.xlsx
  format: null
  id: resource_a22a5c1a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: somalia-cumulative_drought_response_jan-june.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia - Cumulative Drought Response (Cumulative_Drought_Response_Jan-Apr
    2022.xlsx)
  download_url: https://data.humdata.org/dataset/f0432d4c-d2f9-40f3-9b76-85352ec931c0/resource/7630eb1d-8b9d-40f7-83b8-4175d433aedb/download/cumulative_drought_response_jan-apr-2022.xlsx
  format: null
  id: resource_7630eb1d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Cumulative_Drought_Response_Jan-Apr 2022.xlsx
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-som_ochasom_cumulativedroughtresponse_2022
spatial:
  bbox: null
  centroid: null
  countries:
  - SOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2022-06-30'
  start: '2022-01-01'
temporal_resolution: null
title: Somalia - Cumulative Drought Response
version: null
vulnerability: null
---
