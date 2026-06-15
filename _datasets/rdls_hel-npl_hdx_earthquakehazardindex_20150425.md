---
attributions:
- entity:
    affiliation: null
    email: null
    name: Humanitarian Data Exchange
    url: https://data.humdata.org/dataset/nepal-earthquake-hazard-index
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX
  url: https://data.humdata.org/dataset/nepal-earthquake-hazard-index
creator:
  affiliation: null
  email: null
  name: HDX
  url: https://data.humdata.org/dataset/nepal-earthquake-hazard-index
dataset_id: rdls_hel-npl_hdx_earthquakehazardindex_20150425
description: 'Data used for the statistical model to predict the number of fatalities
  following an earthquake as in Nepal. The model predicting death counts, developed
  using zero-inflated negative binomial regression to account for excess zeros and
  over-dispersion, then converted into indices that measure relative priority in terms
  of predicted death counts, predicted death rate (predicted death count divided by
  total population), and predicted death density (predicted death count divided by
  area).. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/nepal-earthquake-hazard-index]'
details: 'A paper based on this development has been published by The Statistical
  Journal of the IAOS and it can be accessed here: http://bit.ly/1mkImGM'
exposure:
- asset_type:
    description: District-level population data used to calculate predicted death
      rates
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
    description: House construction type data at district level characterizing building
      vulnerability
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard:
  event_sets_by_hazard_type:
    earthquake:
    - analysis_type: empirical
      calculation_method: inferred
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: MMI:-
        process: ground_motion
        trigger: null
        type: earthquake
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: District-level MMI measurements, population counts, and building construction
    data from HDX were integrated into a zero-inflated negative binomial regression
    model to predict earthquake fatality counts, which were then converted into relative
    priority indices based on predicted deaths, death rates, and death density.
  sources:
  - id: source_1
    license: null
    name: Humanitarian Data Exchange
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/nepal-earthquake-hazard-index
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Predicted earthquake fatality counts derived from zero-inflated negative
      binomial regression model
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: MMI:-
      process: null
      trigger: null
      type: earthquake
    id: loss_1
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
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Nepal earthquake hazard Index (Excel)
  download_url: https://data.humdata.org/dataset/f23cfb6f-71ad-4155-829a-3a8e473654a9/resource/3fa2baf8-23a2-4615-a5ea-4b81b78948c6/download/score_vdc_final_20150616_hdx.xlsx
  format: null
  id: resource_3fa2baf8
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: score_vdc_final_20150616_hdx.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Nepal earthquake hazard Index (Excel)
  download_url: https://data.humdata.org/dataset/f23cfb6f-71ad-4155-829a-3a8e473654a9/resource/3457c192-06ec-4b36-bc84-5ae421983761/download/score_dist_final_20150616_hdx.xlsx
  format: null
  id: resource_3457c192
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: score_dist_final_20150616_hdx.xlsx
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-npl_hdx_earthquakehazardindex_20150425
spatial:
  bbox: null
  centroid: null
  countries:
  - NPL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-04-25'
temporal_resolution: null
title: Nepal earthquake hazard Index
version: null
vulnerability: null
---
