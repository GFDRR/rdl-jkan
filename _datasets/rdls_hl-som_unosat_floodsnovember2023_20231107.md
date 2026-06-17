---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/floods-in-somalia-november-2023
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/floods-in-somalia-november-2023
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/floods-in-somalia-november-2023
dataset_id: rdls_hl-som_unosat_floodsnovember2023_20231107
description: 'UNOSAT code FL20231105SOM This application provides geospatial information
  on ongoing satellite based-assessment related to the ongoing floods in Somalia that
  started in November 2023. Important note: The boundaries and names shown, and the
  designations used on this map do not imply official endorsement or acceptance by
  the United Nations. The United Nations Satellite Centre -UNOSAT is not responsible
  for the misuse or misrepresentation of the map.. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/floods-in-somalia-november-2023]'
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
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts reviewed and compared satellite imagery from the November
    2023 Somalia flood event to identify and delineate flood extent. Affected areas
    were digitized and stored in geodatabase and shapefile formats with metadata including
    sensor date, sensor ID, and area measurements in square meters and hectares.
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
- href: https://data.humdata.org/dataset/floods-in-somalia-november-2023
  rel: source
loss:
  losses:
  - asset_category: natural_environment
    asset_dimension: product
    description: Observed flood extent area in square meters/hectares from satellite
      imagery
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
  description: Floods in Somalia, November 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3726/FL20231105SOM_gdb.zip
  format: Geodatabase
  id: resource_7efde38a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20231105SOM_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Floods in Somalia, November 2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3726/FL20231105SOM_SHP.zip
  format: null
  id: resource_a5b36745
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20231105SOM_SHP.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-som_unosat_floodsnovember2023_20231107
spatial:
  bbox: null
  centroid: null
  countries:
  - SOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-11-07'
temporal_resolution: null
title: Floods in Somalia, November 2023
version: null
vulnerability: null
---
