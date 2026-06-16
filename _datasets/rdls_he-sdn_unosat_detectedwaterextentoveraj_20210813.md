---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-extent-over-aj-jazirah-gedaref-and-sennar-states-sudan-as-of-10-august-2021
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-over-aj-jazirah-gedaref-and-sennar-states-sudan-as-of-10-august-2021
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-over-aj-jazirah-gedaref-and-sennar-states-sudan-as-of-10-august-2021
dataset_id: rdls_he-sdn_unosat_detectedwaterextentoveraj_20210813
description: 'UNOSAT code: FL20210812SDN This map illustrates satellite detected waters
  and the related potentially affected croplands as deduced using a satellite Sentinel-2
  image acquired on 10 August 2021 over the Aj Jazirah, Gedaref and Sennar states,
  Sudan. In this area, about 220 km2 of croplands appear to be likely affected by
  the flood waters. This is a preliminary analysis and has not yet been validated
  in the field. Please send ground feedback to United Nations Satellite Centre (UNOSAT)..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-over-aj-jazirah-gedaref-and-sennar-states-sudan-as-of-10-august-2021]'
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
    description: Croplands potentially affected by flood waters in Aj Jazirah, Gedaref
      and Sennar states
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_1
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
hazard:
  event_sets_by_hazard_type:
    flood:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: AA:km2
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: Sentinel-2 satellite imagery acquired on 10 August 2021 was analyzed
    by UNOSAT analysts through visual interpretation and multi-temporal comparison
    to detect water extent and delineate potentially affected croplands. The resulting
    geodatabase contains observed flood water polygons and affected agricultural area
    estimates (220 km2) across three Sudanese states.
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
- href: https://data.humdata.org/dataset/water-extent-over-aj-jazirah-gedaref-and-sennar-states-sudan-as-of-10-august-2021
  rel: source
loss:
  losses: []
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
  description: Satellite detected water extent over Aj Jazirah, Gedaref and Sennar
    states, Sudan as of 10 August 2021 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/SD/FL20210812SDN/FL20210812SDN_gdb.zip
  format: Geodatabase
  id: resource_6482cc8c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20210812SDN_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent over Aj Jazirah, Gedaref and Sennar
    states, Sudan as of 10 August 2021 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/SD/FL20210812SDN/FL20210812SDN_gdb.zip
  format: null
  id: resource_b81e24e2
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20210812SDN_gdb.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-sdn_unosat_detectedwaterextentoveraj_20210813
spatial:
  bbox: null
  centroid: null
  countries:
  - SDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2021-08-13'
temporal_resolution: null
title: Satellite detected water extent over Aj Jazirah, Gedaref and Sennar states,
  Sudan as of 10 August 2021
version: null
vulnerability: null
---
