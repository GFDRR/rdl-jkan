---
attributions:
- entity:
    affiliation: null
    email: null
    name: Worldview-3, Spot 6, Sentinel-2, VRRS satellite imagery
    url: https://data.humdata.org/dataset/potentially-affected-areas-by-pyroclastic-flow-deposits-after-the-december-2022-mount-seme
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop population data
    url: https://data.humdata.org/dataset/potentially-affected-areas-by-pyroclastic-flow-deposits-after-the-december-2022-mount-seme
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WSF (World Settlement Footprint) urban areas data
    url: https://data.humdata.org/dataset/potentially-affected-areas-by-pyroclastic-flow-deposits-after-the-december-2022-mount-seme
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/potentially-affected-areas-by-pyroclastic-flow-deposits-after-the-december-2022-mount-seme
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/potentially-affected-areas-by-pyroclastic-flow-deposits-after-the-december-2022-mount-seme
dataset_id: rdls_hel-idn_unosat_potentiallyaffectedareasp_20221213
description: 'UNOSAT code VO20221206IDN, GDACS Id: 1000057 This map illustrates the
  potentially affected areas by pyroclastic flow/deposits of the December 2022 Semeru
  mount eruption in East Java (Indonesia) as inferred from post eruption satellite
  images VRRS, Worldview-3, Spot 6, and Sentinel-2, images acquired on 8, 9, 11 &
  12 Dec. 2022 respectively. Within this area, UNOSAT has identified 208 affected
  structures and 221 structures are potentially affected. Based on Worldpop population
  data, WSF urban areas data, about 7ha of urban areas are affected by the pyroclastic
  flow/deposit and about 8,000 people are potentially directly exposed to pyroclastic
  flow in this zone. This is a preliminary analysis and has not yet been validated
  in the field. Please send ground feedback to the United Nations Satellite Centre
  (UNOSAT).. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/potentially-affected-areas-by-pyroclastic-flow-deposits-after-the-december-2022-mount-seme]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure:
- asset_type:
    description: Building structures identified within and adjacent to pyroclastic
      flow/deposit areas
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
    description: Urban population exposure estimated from WorldPop data and WSF urban
      area classification
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
      quantity_kind: area
      unit: null
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: inferred
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: h_vaf:mm
      process: pyroclastic_flow
      trigger: null
      type: volcanic
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts conducted multi-temporal satellite image analysis comparing
    pre- and post-eruption imagery (Worldview-3, Spot 6, Sentinel-2, VRRS) acquired
    8-12 December 2022 to delineate pyroclastic flow and deposit extent. Building
    structures were identified through manual interpretation and counted within affected
    zones. Population exposure was estimated by intersecting the hazard extent with
    WorldPop gridded population and WSF urban area datasets to quantify affected urban
    areas.
  sources:
  - id: source_1
    license: null
    name: Worldview-3, Spot 6, Sentinel-2, VRRS satellite imagery
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: WorldPop population data
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_3
    license: null
    name: WSF (World Settlement Footprint) urban areas data
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/potentially-affected-areas-by-pyroclastic-flow-deposits-after-the-december-2022-mount-seme
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from pyroclastic flow/deposits with 208 confirmed
      affected and 221 potentially affected structures
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_volcanic
      intensity_measure: h_vaf:mm
      process: null
      trigger: null
      type: volcanic
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
    description: Population exposure in urban areas affected by pyroclastic flow/deposits
      (7 hectares)
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_volcanic
      intensity_measure: h_vaf:mm
      process: null
      trigger: null
      type: volcanic
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
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Indonesia - Potentially affected areas by pyroclastic flow/deposits
    after the December 2022 Mount Semeru volcanic eruption in East Java. (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3462/VO20221206IDN_gdb.zip
  format: Geodatabase
  id: resource_c1c7f9c3
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VO20221206IDN_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Indonesia - Potentially affected areas by pyroclastic flow/deposits
    after the December 2022 Mount Semeru volcanic eruption in East Java. (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3462/VO202212006IDN_SHP.zip
  format: null
  id: resource_c361cb6e
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VO202212006IDN_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-idn_unosat_potentiallyaffectedareasp_20221213
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
  start: '2022-12-13'
temporal_resolution: null
title: Indonesia - Potentially affected areas by pyroclastic flow/deposits after the
  December 2022 Mount Semeru volcanic eruption in East Java.
version: null
vulnerability: null
---
