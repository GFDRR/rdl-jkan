---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/floods-in-norway-august-2023-unosat-live-web-map
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/floods-in-norway-august-2023-unosat-live-web-map
dataset_id: rdls_lss-nor_unosat_floodsaugust2023livewebma_20230814
description: 'UNOSAT code FL20230811NOR Live web map showing analysis related to floods
  in Norway. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/floods-in-norway-august-2023-unosat-live-web-map]'
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
hazard: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts reviewed and compared satellite imagery from before
    and after the August 2023 flood event in Norway, identifying notable changes in
    inundated areas and damage to structures. Affected areas were digitized and attributed
    with sensor dates, area measurements, and analyst notes to produce a post-event
    damage assessment geodatabase.
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
- href: https://data.humdata.org/dataset/floods-in-norway-august-2023-unosat-live-web-map
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from August 2023 floods in Norway
      derived from satellite imagery analysis
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
  description: Floods in Norway, August 2023 - UNOSAT Live Web Map (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3657/FL20230811NOR_gdb.zip
  format: Geodatabase
  id: resource_bd4063d2
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230811NOR_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Floods in Norway, August 2023 - UNOSAT Live Web Map (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3657/FL20230811NOR_SHP.zip
  format: null
  id: resource_f19aaaf8
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230811NOR_SHP.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-nor_unosat_floodsaugust2023livewebma_20230814
spatial:
  bbox: null
  centroid: null
  countries:
  - NOR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-08-14'
temporal_resolution: null
title: Floods in Norway, August 2023 - UNOSAT Live Web Map
version: null
vulnerability: null
---
