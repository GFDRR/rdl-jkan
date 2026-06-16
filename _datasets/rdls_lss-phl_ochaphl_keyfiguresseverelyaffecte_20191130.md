---
attributions:
- entity:
    affiliation: null
    email: null
    name: National OCD (Office of Civil Defense)
    url: https://data.humdata.org/dataset/philippines-key-figures-on-the-severely-affected
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Philippines
  url: https://data.humdata.org/dataset/philippines-key-figures-on-the-severely-affected
creator:
  affiliation: null
  email: null
  name: OCHA Philippines
  url: https://data.humdata.org/dataset/philippines-key-figures-on-the-severely-affected
dataset_id: rdls_lss-phl_ochaphl_keyfiguresseverelyaffecte_20191130
description: 'This data is about the key figures of the severely affected areas on
  the 6.6 earthquake in Tulunan, Cotabato (North Cotabato).. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/philippines-key-figures-on-the-severely-affected]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Post-event impact data collected by affected local government units
    in Tulunan, Cotabato and consolidated by the National Office of Civil Defense
    (OCD) to document key figures on building damage and population displacement from
    the 6.6 magnitude earthquake.
  sources:
  - id: source_1
    license: null
    name: National OCD (Office of Civil Defense)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/philippines-key-figures-on-the-severely-affected
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from the 6.6 magnitude earthquake in Tulunan,
      Cotabato
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population displacement resulting from the 6.6 magnitude earthquake
      in Tulunan, Cotabato
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
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Key figures the severely affected areas on 6.6 earthquake in Tulunan,
    Cotabato (North Cotabato)
  download_url: https://data.humdata.org/dataset/99154ff5-7ed3-4517-b316-d359c5264ae2/resource/8c78ccfc-8f4e-427c-945a-adb3cb3c0c73/download/191130_key-figures-on-6.6-earthquake-in-tulunan-on-the-severely-affected-areas.xlsx
  format: null
  id: resource_8c78ccfc
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 191130_Key figures on 6.6 Earthquake in Tulunan on the severely affected
    areas.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-phl_ochaphl_keyfiguresseverelyaffecte_20191130
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
  end: null
  start: '2019-11-30'
temporal_resolution: null
title: 'Philippines: Key figures on the severely affected areas on 6.6 earthquake
  in Tulunan, Cotabato (North Cotabato)'
version: null
vulnerability: null
---
