---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Federation of Red Cross and Red Crescent Societies (IFRC)
  url: https://data.humdata.org/dataset/peru-floods-dana-matrix-glide-number-fl2017-000014
creator:
  affiliation: null
  email: null
  name: International Federation of Red Cross and Red Crescent Societies (IFRC)
  url: https://data.humdata.org/dataset/peru-floods-dana-matrix-glide-number-fl2017-000014
dataset_id: rdls_el-per_ifrc_floodsdamageneedsassessme_20170522
description: 'Peru-Floods: damage and needs assessment matrix, GLIDE NUMBER:FL2017-000014.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/peru-floods-dana-matrix-glide-number-fl2017-000014]'
details: null
exposure:
- asset_type:
    description: Building stock affected by the 2017 flood event in Peru
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Population affected by the 2017 flood event in Peru
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_2
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: CC-BY-4.0
lineage:
  description: Post-event damage and needs assessment matrix compiled by IFRC following
    the 2017 Peru floods using census methodology to document direct impacts on buildings
    and population across affected areas.
  sources:
  - id: source_1
    license: null
    name: International Federation of Red Cross and Red Crescent Societies (IFRC)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/peru-floods-dana-matrix-glide-number-fl2017-000014
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from the 2017 Peru flood event
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
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population affected by the 2017 Peru flood event
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
purpose: Census
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Peru - Floods damage and needs assessment matrix (Peru-Floods: damage
    and needs assessment matrix, GLIDE NUMBER:FL2017-000014)'
  download_url: https://docs.google.com/spreadsheets/d/1oC0U_uzbeOuk2XBbagUY9Mwz0vkMaAoQ4nGd-7AknO0/edit?usp=sharing
  format: null
  id: resource_98189d1d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DC_OP4_DANA.xlsx
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-per_ifrc_floodsdamageneedsassessme_20170522
spatial:
  bbox: null
  centroid: null
  countries:
  - PER
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-05-22'
temporal_resolution: null
title: Peru - Floods damage and needs assessment matrix
version: null
vulnerability: null
---
