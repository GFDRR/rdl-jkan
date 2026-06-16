---
attributions:
- entity:
    affiliation: null
    email: null
    name: BNPB
    url: https://data.humdata.org/dataset/population-and-infrastructure-exposed-by-west-sulawesi-eq
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: UNFPA Indonesia (inactive)
  url: https://data.humdata.org/dataset/population-and-infrastructure-exposed-by-west-sulawesi-eq
creator:
  affiliation: null
  email: null
  name: UNFPA Indonesia (inactive)
  url: https://data.humdata.org/dataset/population-and-infrastructure-exposed-by-west-sulawesi-eq
dataset_id: rdls_he-idn_unfpaidn_populationinfrastructuree_20210122
description: 'West Sulawesi Data on population and infrastructure that are affected
  by the Earthquake. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/population-and-infrastructure-exposed-by-west-sulawesi-eq]'
details: null
exposure:
- asset_type:
    description: Population exposed to West Sulawesi earthquake
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
    description: Infrastructure facilities exposed to West Sulawesi earthquake
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
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
      intensity_measure: PGA:g
      process: ground_motion
      trigger: null
      type: earthquake
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-4.0
lineage:
  description: Baseline exposure data for West Sulawesi combining population and infrastructure
    inventories with observed earthquake hazard event information from BNPB to quantify
    assets at risk from the earthquake.
  sources:
  - id: source_1
    license: null
    name: BNPB
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/population-and-infrastructure-exposed-by-west-sulawesi-eq
  rel: source
loss: null
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
  description: West Sulawesi Data on population and infrastructure that are affected
    by the Earthquake
  download_url: https://data.humdata.org/dataset/6b5867f7-9037-4863-b0e2-b58f63661680/resource/a7a036a9-3b95-4318-824d-abdd83467a0b/download/westsulawesi_baseline_data_exposed.xlsx
  format: null
  id: resource_a7a036a9
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: WestSulawesi_Baseline_Data_Exposed.xlsx
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-idn_unfpaidn_populationinfrastructuree_20210122
spatial:
  bbox: null
  centroid: null
  countries:
  - IDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2021-01-22'
temporal_resolution: null
title: Indonesia - Population and Infrastructure Exposed by West Sulawesi EQ
version: null
vulnerability: null
---
