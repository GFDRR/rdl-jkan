---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/fire-in-algeria-unosat-live-web-map
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/fire-in-algeria-unosat-live-web-map
dataset_id: rdls_hl-dza_unosat_firelivewebmap_20230724
description: 'UNOSAT code FR20230724DZA Live web map showing analysis related to fire
  in Algeria.. [Source: This metadata record was automatically extracted from the
  Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/fire-in-algeria-unosat-live-web-map]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure: []
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: wildfire
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts reviewed and compared multi-temporal satellite imagery
    to identify and delineate wildfire extent in Algeria. Burned areas were digitized
    and quantified in square meters and hectares, with results delivered as geodatabase
    and shapefile formats for operational situational awareness.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/fire-in-algeria-unosat-live-web-map
  rel: source
loss:
  losses:
  - asset_category: natural_environment
    asset_dimension: product
    description: Direct wildfire extent and burned area in hectares derived from satellite
      damage assessment
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: null
      trigger: null
      type: wildfire
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
          unit: null
        metric: loss
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
  description: Fire in Algeria - UNOSAT Live Web Map (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3640/FR20230724DZA_gdb.zip
  format: Geodatabase
  id: resource_2b62e8e9
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FR20230724DZA_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Fire in Algeria - UNOSAT Live Web Map (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3640/FR20230724DZA_SHP.zip
  format: null
  id: resource_07979f49
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FR20230724DZA_SHP.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-dza_unosat_firelivewebmap_20230724
spatial:
  bbox: null
  centroid: null
  countries:
  - DZA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-07-24'
temporal_resolution: null
title: Fire in Algeria - UNOSAT Live Web Map
version: null
vulnerability: null
---
