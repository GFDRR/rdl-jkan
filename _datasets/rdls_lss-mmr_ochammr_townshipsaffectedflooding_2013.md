---
attributions:
- entity:
    affiliation: null
    email: null
    name: Humanitarian partners
    url: https://data.humdata.org/dataset/myanmar-townships-affected-by-flooding
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Myanmar
  url: https://data.humdata.org/dataset/myanmar-townships-affected-by-flooding
creator:
  affiliation: null
  email: null
  name: OCHA Myanmar
  url: https://data.humdata.org/dataset/myanmar-townships-affected-by-flooding
dataset_id: rdls_lss-mmr_ochammr_townshipsaffectedflooding_2013
description: 'Townships affected by flooding in Myanmar from 2013 to 2020.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/myanmar-townships-affected-by-flooding]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Township-level flood impact data compiled from direct observational
    reports and anecdotal information provided by humanitarian partners operating
    in Myanmar between 2013 and 2020. Data identifies which administrative divisions
    experienced flooding events without providing quantified hazard measurements or
    detailed asset inventories.
  sources:
  - id: source_1
    license: null
    name: Humanitarian partners
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/myanmar-townships-affected-by-flooding
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by flooding across townships in Myanmar
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
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Myanmar: Townships Affected by Flooding (Townships affected by flooding
    in Myanmar from 2013 to 2020.)'
  download_url: https://data.humdata.org/dataset/f40573e5-e8a0-4190-ad36-0121e4c03893/resource/cbba3e60-cdb9-4fab-a35d-c7fafa444a5b/download/myanmar_flood_affected_townships_2013-2020.xlsx
  format: null
  id: resource_cbba3e60
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Myanmar_Flood_Affected_Townships_2013-2020.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-mmr_ochammr_townshipsaffectedflooding_2013
spatial:
  bbox: null
  centroid: null
  countries:
  - MMR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-12-31'
  start: '2013-01-01'
temporal_resolution: null
title: 'Myanmar: Townships Affected by Flooding'
version: null
vulnerability: null
---
