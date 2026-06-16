---
attributions:
- entity:
    affiliation: null
    email: null
    name: National Disaster Management Agencies (BNPB)
    url: https://data.humdata.org/dataset/population-affected-area-jakarta-banten-west-java-flood
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Civil Registration Office, Ministry of Home Affairs
    url: https://data.humdata.org/dataset/population-affected-area-jakarta-banten-west-java-flood
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: UNFPA Indonesia (inactive)
  url: https://data.humdata.org/dataset/population-affected-area-jakarta-banten-west-java-flood
creator:
  affiliation: null
  email: null
  name: UNFPA Indonesia (inactive)
  url: https://data.humdata.org/dataset/population-affected-area-jakarta-banten-west-java-flood
dataset_id: rdls_el-idn_unfpaidn_populationaffectedareajak_20200114
description: 'Number of population affected by flood in Jakarta, Banten, and West
  Java Provinces. The affected area based at village level source from National Disaster
  Management Agencies (BNPB), the Population data is from Civil Registration Office,
  Ministry of Home Affairs.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/population-affected-area-jakarta-banten-west-java-flood]'
details: null
exposure:
- asset_type:
    description: Residential population by age, gender, marital status, education,
      and religion at village level in flood-affected areas
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
hazard: null
license: CC0-1.0
lineage:
  description: Village-level population baseline data from civil registration was
    spatially intersected with flood-affected areas delineated by BNPB to produce
    affected population counts. The dataset combines administrative population statistics
    with post-event disaster impact boundaries to quantify population exposure to
    the 2020 flood event.
  sources:
  - id: source_1
    license: null
    name: National Disaster Management Agencies (BNPB)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Civil Registration Office, Ministry of Home Affairs
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/population-affected-area-jakarta-banten-west-java-flood
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by flooding in Jakarta, Banten, and West Java
      provinces
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
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Population affected to Flood in Jakarta, Banten, and West Java Province
    on Jan 2020
  download_url: https://data.humdata.org/dataset/cc0c8c69-03ff-4171-9189-69aedae28fdf/resource/002776e1-165f-4991-8b0d-87ff1b375836/download/banjir_jakarta_2020.zip
  format: null
  id: resource_002776e1
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: banjir_jakarta_2020.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-idn_unfpaidn_populationaffectedareajak_20200114
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
  start: '2020-01-14'
temporal_resolution: null
title: Indonesia - Population affected area Jakarta, Banten, West Java Flood
version: null
vulnerability: null
---
