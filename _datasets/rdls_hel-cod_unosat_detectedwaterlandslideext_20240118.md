---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-and-landslide-extents-in-kinshasa-province-democratic-republic-of-the-congo-as-of-13
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-and-landslide-extents-in-kinshasa-province-democratic-republic-of-the-congo-as-of-13
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-and-landslide-extents-in-kinshasa-province-democratic-republic-of-the-congo-as-of-13
dataset_id: rdls_hel-cod_unosat_detectedwaterlandslideext_20240118
description: 'UNOSAT code: FL20231229COD This map illustrates satellite-detected surface
  waters and landslide location in Kinshasa Province, Democratic Republic of The Congo,
  as observed from a WorldView-3 image acquired on 13 January 2024, at 10:36 local
  time. Within the analysed area of 130km2, approximately 4 km2 of land appear to
  be flooded and a landslide location observed. Within the analysed area 9,352 buildings
  are identified as potentially affected by the floods and landslide. This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to United Nations Satellite Centre (UNOSAT).. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/water-and-landslide-extents-in-kinshasa-province-democratic-republic-of-the-congo-as-of-13]'
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
    description: "Building footprints identified within the 130 km\xB2 analysis area"
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
license: CC-BY-SA-4.0
lineage:
  description: "UNOSAT analysts processed WorldView-3 satellite imagery acquired on\
    \ 13 January 2024 over Kinshasa Province, comparing multi-temporal images to detect\
    \ surface water extent (approximately 4 km\xB2 flooded) and identify a landslide\
    \ location. Building footprints were extracted and spatially intersected with\
    \ hazard extents to estimate exposure and direct impacts within the 130 km\xB2\
    \ analysis area."
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
- href: https://data.humdata.org/dataset/water-and-landslide-extents-in-kinshasa-province-democratic-republic-of-the-congo-as-of-13
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Buildings potentially affected by satellite-detected flooding
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
          quantity_kind: count
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: Buildings potentially affected by detected landslide location
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: landslide
    id: loss_2
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
  description: Satellite detected water and landslide extents in Kinshasa Province,
    Democratic Republic of The Congo as of 13 January 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3786/FL20231229COD_gdb.zip
  format: Geodatabase
  id: resource_24771c7c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20231229COD_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water and landslide extents in Kinshasa Province,
    Democratic Republic of The Congo as of 13 January 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3786/FL20231229COD_SHP.zip
  format: null
  id: resource_5c8a6869
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20231229COD_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-cod_unosat_detectedwaterlandslideext_20240118
spatial:
  bbox: null
  centroid: null
  countries:
  - COD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-01-18'
temporal_resolution: null
title: Satellite detected water and landslide extents in Kinshasa Province, Democratic
  Republic of The Congo as of 13 January 2024
version: null
vulnerability: null
---
