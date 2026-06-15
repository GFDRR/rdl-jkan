---
attributions:
- entity:
    affiliation: null
    email: null
    name: IOM
    url: https://data.humdata.org/dataset/cameroon-nw-sw-crisis-idp-population-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: MIRA LT OU
    url: https://data.humdata.org/dataset/cameroon-nw-sw-crisis-idp-population-estimates
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: OCHA partners
    url: https://data.humdata.org/dataset/cameroon-nw-sw-crisis-idp-population-estimates
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Cameroon
  url: https://data.humdata.org/dataset/cameroon-nw-sw-crisis-idp-population-estimates
creator:
  affiliation: null
  email: null
  name: OCHA Cameroon
  url: https://data.humdata.org/dataset/cameroon-nw-sw-crisis-idp-population-estimates
dataset_id: rdls_lss-cmr_ochacmr_nwswcrisisidppopulationes_20180930
description: 'Internaly displaced population estimates in North West and South West
  crisis in Cameroon. Data have been compiled from various by OCHA Cameroon.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/cameroon-nw-sw-crisis-idp-population-estimates]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Internally displaced population estimates were compiled from multiple
    sources including IOM, MIRA assessments, and OCHA partner organizations using
    registry methodology to document displacement from the North West and South West
    crisis in Cameroon.
  sources:
  - id: source_1
    license: null
    name: IOM
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: MIRA LT OU
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: OCHA partners
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/cameroon-nw-sw-crisis-idp-population-estimates
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced population from the North West and South West
      crisis in Cameroon
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
purpose: Registry
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Cameroon - NW & SW Crisis: IDP Population Estimates (IDP Population
    Estimates for North West and South West crisis)'
  download_url: https://data.humdata.org/dataset/b6c836df-de51-4598-9025-438065146a03/resource/1744dd52-f3db-47be-bed9-d09507f0107a/download/cmr_lt_nw_ou_sw_displaced_pop_2018-09_v01.xlsx
  format: null
  id: resource_1744dd52
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cmr_lt_nw_ou_sw_displaced_pop_2018-09_v01.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-cmr_ochacmr_nwswcrisisidppopulationes_20180930
spatial:
  bbox: null
  centroid: null
  countries:
  - CMR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-09-30'
temporal_resolution: null
title: 'Cameroon - NW & SW Crisis: IDP Population Estimates'
version: null
vulnerability: null
---
