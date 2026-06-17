---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/flood-waters-as-of-29-november-2019-over-loukolela-cuvette-department-republic-of-congo
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/flood-waters-as-of-29-november-2019-over-loukolela-cuvette-department-republic-of-congo
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/flood-waters-as-of-29-november-2019-over-loukolela-cuvette-department-republic-of-congo
dataset_id: rdls_he-cog_unosat_detectedfloodwatersas29no_20191210
description: "UNOSAT code: FL20191205COG This map illustrates satellite-detected flood\
  \ waters along the Congo River over, Loukol\xE9la, Loukol\xE9la District, Cuvette\
  \ Department in Republic of Congo as observed from Pleiades-1 imagery acquired on\
  \ 29 November 2019. 136 ha of potential flood waters and 168 potentially flooded\
  \ structures have been identified in Loukol\xE9la and its vicinity. This is a preliminary\
  \ analysis and has not yet been validated in the field. Please send ground feedback\
  \ to UNITAR -UNOSAT.. [Source: This metadata record was automatically extracted\
  \ from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/flood-waters-as-of-29-november-2019-over-loukolela-cuvette-department-republic-of-congo]"
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
    description: "Potentially flooded structures identified in Loukol\xE9la and vicinity"
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
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: "UNOSAT analysts reviewed Pleiades-1 satellite imagery acquired on\
    \ 29 November 2019 over Loukol\xE9la, comparing temporal images to identify notable\
    \ changes in water extent. Flood water polygons (136 ha) and potentially flooded\
    \ building structures (168 count) were manually delineated through visual interpretation\
    \ of satellite imagery. This is a preliminary post-event damage assessment product\
    \ not yet validated in the field."
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
- href: https://data.humdata.org/dataset/flood-waters-as-of-29-november-2019-over-loukolela-cuvette-department-republic-of-congo
  rel: source
loss: null
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
  description: "Satellite-detected flood waters, as of 29 November 2019, over Loukol\xE9\
    la, Cuvette Department, Republic of Congo (Zipped geodatabase)"
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/CG/FL20191205COG/FL20191205COG_gdb.zip
  format: Geodatabase
  id: resource_06a0e684
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20191205COG_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Satellite-detected flood waters, as of 29 November 2019, over Loukol\xE9\
    la, Cuvette Department, Republic of Congo (Zipped shapefile)"
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/CG/FL20191205COG/FL20191205COG_SHP.zip
  format: null
  id: resource_1bd3eea2
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20191205COG_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-cog_unosat_detectedfloodwatersas29no_20191210
spatial:
  bbox: null
  centroid: null
  countries:
  - COG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2019-12-10'
temporal_resolution: null
title: "Satellite-detected flood waters, as of 29 November 2019, over Loukol\xE9la,\
  \ Cuvette Department, Republic of Congo"
version: null
vulnerability: null
---
