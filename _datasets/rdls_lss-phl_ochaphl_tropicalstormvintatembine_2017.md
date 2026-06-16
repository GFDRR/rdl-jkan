---
attributions:
- entity:
    affiliation: null
    email: null
    name: DSWD DROMIC
    url: https://data.humdata.org/dataset/philippines-tropical-storm-vinta-tembin-idps
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Philippines
  url: https://data.humdata.org/dataset/philippines-tropical-storm-vinta-tembin-idps
creator:
  affiliation: null
  email: null
  name: OCHA Philippines
  url: https://data.humdata.org/dataset/philippines-tropical-storm-vinta-tembin-idps
dataset_id: rdls_lss-phl_ochaphl_tropicalstormvintatembine_2017
description: 'Tropical Storm VINTA (TEMBIN) Effects with PSGC code source: DSWD DROMIC
  (http://dromic.dswd.gov.ph/tropical-depression-vinta-20-december-2017/). [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/philippines-tropical-storm-vinta-tembin-idps]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Post-event impact registry compiled by DSWD DROMIC documenting effects
    of Tropical Storm VINTA (TEMBIN) in December 2017, with internally displaced persons
    counts aggregated by Philippine Standard Geographic Code administrative divisions.
  sources:
  - id: source_1
    license: null
    name: DSWD DROMIC
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/philippines-tropical-storm-vinta-tembin-idps
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons from Tropical Storm VINTA (TEMBIN)
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
  description: 'Philippines: Tropical Storm VINTA (TEMBIN) Effects (170106_Tropical
    Storm Tembin_Effects.xlsx)'
  download_url: https://data.humdata.org/dataset/c33bc325-a885-4113-aced-a2d7e116d151/resource/752a8d11-b048-4215-9099-cbca47428e53/download/170106_tropical-storm-tembin_effects.xlsx
  format: null
  id: resource_752a8d11
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 170106_Tropical Storm Tembin_Effects.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-phl_ochaphl_tropicalstormvintatembine_2017
spatial:
  bbox: null
  centroid: null
  countries:
  - PHL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2018-01-06'
  start: '2017-12-27'
temporal_resolution: null
title: 'Philippines: Tropical Storm VINTA (TEMBIN) Effects'
version: null
vulnerability: null
---
