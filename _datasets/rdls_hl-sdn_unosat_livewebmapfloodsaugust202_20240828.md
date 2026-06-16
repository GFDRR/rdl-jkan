---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/unosat-live-webmap-floods-in-sudan-august-2024
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-live-webmap-floods-in-sudan-august-2024
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-live-webmap-floods-in-sudan-august-2024
dataset_id: rdls_hl-sdn_unosat_livewebmapfloodsaugust202_20240828
description: 'UNOSAT code: FL20240826SDN, GDACS ID: 1102854 This application provides
  geospatial information regarding the analysis related to the floods in Sudan in
  August 2024. Important note: The boundaries and names shown, and the designations
  used on this map do not imply official endorsement or acceptance by the United Nations.
  The United Nations Satellite Centre. UNOSAT is not responsible for the misuse or
  misrepresentation of the map.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/unosat-live-webmap-floods-in-sudan-august-2024]'
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
  description: "UNOSAT analysts reviewed and compared multi-temporal satellite imagery\
    \ to detect notable changes in flood extent. The resulting geodatabase and shapefile\
    \ contain mapped flood polygons with area measurements (m\xC2\xB2 and hectares)\
    \ and metadata including sensor type, observation date, and event code, representing\
    \ direct observational assessment of the August 2024 Sudan flood event."
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/unosat-live-webmap-floods-in-sudan-august-2024
  rel: source
loss:
  losses:
  - asset_category: natural_environment
    asset_dimension: product
    description: Flood-affected area extent derived from satellite imagery change
      detection
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: flood
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
  description: UNOSAT Live Webmap, Floods in Sudan - August 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3931/FL20240826SDN_gdb.zip
  format: Geodatabase
  id: resource_c8db223a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240826SDN_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: UNOSAT Live Webmap, Floods in Sudan - August 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3931/FL20240826SDN_SHP.zip
  format: null
  id: resource_03885a3c
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240826SDN_SHP.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-sdn_unosat_livewebmapfloodsaugust202_20240828
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
  start: '2024-08-28'
temporal_resolution: null
title: UNOSAT Live Webmap, Floods in Sudan - August 2024
version: null
vulnerability: null
---
