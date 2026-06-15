---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/floods-over-cox-s-bazar-area-bangladesh-unosat-live-web-map
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/floods-over-cox-s-bazar-area-bangladesh-unosat-live-web-map
dataset_id: rdls_hzd-bgd_unosat_floodsovercoxsbazarareali_20210803
description: 'UNOSAT code: FL20210729BGD This is a web map showing analysis and results
  related to floods in Cox''s Bazar area, Chittagong division, Bangladesh. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/floods-over-cox-s-bazar-area-bangladesh-unosat-live-web-map]'
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
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts reviewed and compared satellite imagery from before
    and after the July 2021 flooding event in Cox's Bazar, Bangladesh, to identify
    and delineate water bodies and flood extent. The resulting flood extent polygons
    were classified by water status and confidence level, with field validation and
    sensor metadata recorded for quality assurance.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/floods-over-cox-s-bazar-area-bangladesh-unosat-live-web-map
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
  description: Floods over Cox's Bazar area, Bangladesh - UNOSAT Live Web Map (Zipped
    geodatabase)
  download_url: https://unosat-maps.web.cern.ch/BD/FL20210729BGD/FL20210729BGD_gdb.zip
  format: Geodatabase
  id: resource_7c342697
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20210729BGD_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Floods over Cox's Bazar area, Bangladesh - UNOSAT Live Web Map (Zipped
    shapefile)
  download_url: https://unosat-maps.web.cern.ch/BD/FL20210729BGD/FL20210729BGD_SHP.zip
  format: null
  id: resource_0e41bc12
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20210729BGD_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-bgd_unosat_floodsovercoxsbazarareali_20210803
spatial:
  bbox: null
  centroid: null
  countries:
  - BGD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2021-08-03'
temporal_resolution: null
title: Floods over Cox's Bazar area, Bangladesh - UNOSAT Live Web Map
version: null
vulnerability: null
---
