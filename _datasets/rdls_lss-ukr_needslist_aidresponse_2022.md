---
attributions:
- entity:
    affiliation: null
    email: null
    name: RespondLocal-Ukraine Platform
    url: https://data.humdata.org/dataset/ukraine-aid-response
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: NeedsList
  url: https://data.humdata.org/dataset/ukraine-aid-response
creator:
  affiliation: null
  email: null
  name: NeedsList
  url: https://data.humdata.org/dataset/ukraine-aid-response
dataset_id: rdls_lss-ukr_needslist_aidresponse_2022
description: 'Contains data on total dollar value (USD) spent on aid response and
  people reached per sector per oblast in Ukraine based on the activities recorded
  in RespondLocal-Ukraine Platform.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/ukraine-aid-response]'
details: Contains data on total dollar value (USD) spent on aid response and people
  reached per sector per oblast in Ukraine based on the activities recorded in RespondLocal-Ukraine
  Platform started from December 2022.
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Aid response data aggregated from activities recorded in the RespondLocal-Ukraine
    Platform, compiled into summary tables of total USD spending and people reached
    per sector and oblast. This represents post-event humanitarian response metrics
    rather than hazard or exposure data.
  sources:
  - id: source_1
    license: null
    name: RespondLocal-Ukraine Platform
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/ukraine-aid-response
  rel: source
loss:
  losses:
  - asset_category: economic_indicator
    asset_dimension: index
    description: Total USD value of aid response spending across sectors per oblast
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
          quantity_kind: currency
          unit: null
        metric: loss
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Total people reached by aid response per sector per oblast
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
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Contains data on total dollar value (USD) spent on aid response and
    people reached per sector per oblast in Ukraine based on the activities recorded
    in RespondLocal-Ukraine Platform started from December 2022 till June 2023
  download_url: https://data.humdata.org/dataset/24deade1-aa62-4474-bcfc-e64e27e6bebb/resource/4136eaea-1473-4675-8f79-278a0d189b8f/download/ukraine-aid-response-summary.csv
  format: null
  id: resource_4136eaea
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Ukraine Aid Response Summary.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ukr_needslist_aidresponse_2022
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
  end: '2023-06-15'
  start: '2022-12-15'
temporal_resolution: null
title: Ukraine Aid Response
version: null
vulnerability: null
---
