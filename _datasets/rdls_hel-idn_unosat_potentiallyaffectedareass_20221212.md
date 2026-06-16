---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/potentially-affected-areas-se-semeru-mount-in-east-java-indonesia
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/potentially-affected-areas-se-semeru-mount-in-east-java-indonesia
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/potentially-affected-areas-se-semeru-mount-in-east-java-indonesia
dataset_id: rdls_hel-idn_unosat_potentiallyaffectedareass_20221212
description: 'UNOSAT code VO20221206IDN, GDACS Id: 1000057 This map illustrates the
  potentially affected areas by pyroclastic flow/deposits of the December 2022 Semeru
  mount eruption in East Java (Indonesia) as detected by satellite images acquired
  on 4 Dec 2022 10km SE Mount Semeru. Based on analysis of Worldview-3, Spot 6 and
  Sentinel-2 images acquired on 9, 11 & 12 Dec. 2022 respectively, about 460ha of
  land appear to be severely affected by the volcanic eruption induced effects in
  the analyzed area of about 2,000ha. Within this area, UNOSAT has identified 206
  affected structures and 10 potentially affected structures. Based on Worldpop population
  data and affected area by the pyroclastic flow/deposit, about 1,500 people are potentially
  exposed in this zone. This is a preliminary analysis and has not yet been validated
  in the field. Please send ground feedback to the United Nations Satellite Centre
  (UNOSAT).. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/potentially-affected-areas-se-semeru-mount-in-east-java-indonesia]'
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
    description: Building structures identified within the potentially affected area
      by pyroclastic flow
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
      intensity_measure: h_vaf:mm
      process: pyroclastic_flow
      trigger: null
      type: volcanic
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts compared multi-temporal satellite imagery (Worldview-3,
    Spot 6, Sentinel-2) acquired 9-12 December 2022 to detect changes in land cover
    and identify pyroclastic flow deposits and affected structures. Approximately
    460 hectares of severe volcanic impact were mapped within a 2,000 hectare analysis
    area, with 206 affected structures identified through visual interpretation of
    satellite imagery.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/potentially-affected-areas-se-semeru-mount-in-east-java-indonesia
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from pyroclastic flow and volcanic deposits
      detected via satellite imagery
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
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
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
  description: Potentially affected areas SE Semeru mount in East Java, Indonesia
    (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3461/VO20221206IDN_gdb.zip
  format: Geodatabase
  id: resource_ba6f009a
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
  description: Potentially affected areas SE Semeru mount in East Java, Indonesia
    (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3461/VO202212006IDN_SHP.zip
  format: null
  id: resource_23c5d9cc
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
slug: rdls_hel-idn_unosat_potentiallyaffectedareass_20221212
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
  start: '2022-12-12'
temporal_resolution: null
title: Potentially affected areas SE Semeru mount in East Java, Indonesia
version: null
vulnerability: null
---
