---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/flood-impact-assessment-in-mokwa-town-niger-local-government-area-niger-state-nigeria-as-o
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/flood-impact-assessment-in-mokwa-town-niger-local-government-area-niger-state-nigeria-as-o
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/flood-impact-assessment-in-mokwa-town-niger-local-government-area-niger-state-nigeria-as-o
dataset_id: rdls_hel-nga_unosat_floodimpactassessmentmokw_20250603
description: "UNOSAT code: FL20250601NGA, GDACS ID: 1103303 This map illustrates the\
  \ satellite-detected water extent in Mokwa Town, Niger Local Government Area, Niger\
  \ State, Nigeria as observed from a GeoEye-1 imagery acquired on 2 June 2025 at\
  \ 11:24 local time. Within the analysed area of approximately 100 km\xB2, an estimated\
  \ 1.5 km\xB2 of land appears to be affected by floodwaters. UNOSAT has identified\
  \ within this area 470 damaged structures and 199 potentially affected structures.\
  \ This is a preliminary analysis and has not yet been validated in the field. Please\
  \ send ground feedback to the United Nations Satellite Centre (UNOSAT).. [Source:\
  \ This metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/flood-impact-assessment-in-mokwa-town-niger-local-government-area-niger-state-nigeria-as-o]"
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
    description: Building structures in Mokwa Town identified through satellite imagery
      analysis
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
  description: "GeoEye-1 satellite imagery acquired on 2 June 2025 was analyzed by\
    \ UNOSAT analysts through visual comparison and change detection methods to delineate\
    \ water extent (1.5 km\xB2 affected area) and manually identify damaged (470)\
    \ and potentially affected (199) structures within Mokwa Town. This preliminary\
    \ post-event damage assessment provides empirical loss data from observed satellite-detected\
    \ impacts."
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
- href: https://data.humdata.org/dataset/flood-impact-assessment-in-mokwa-town-niger-local-government-area-niger-state-nigeria-as-o
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: 'Direct building damage from fluvial flooding: 470 damaged structures
      identified'
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
  - asset_category: buildings
    asset_dimension: structure
    description: 'Buildings potentially affected by fluvial flooding: 199 structures
      at risk'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
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
  description: Flood impact assessment in Mokwa Town, Niger Local Government Area,
    Niger State, Nigeria as of 2 June 2025 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4138/FL20250601NGA_gdb.zip
  format: Geodatabase
  id: resource_6321aa18
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20250601NGA_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flood impact assessment in Mokwa Town, Niger Local Government Area,
    Niger State, Nigeria as of 2 June 2025 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4138/FL20250601NGA_SHP.zip
  format: null
  id: resource_95037538
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20250601NGA_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-nga_unosat_floodimpactassessmentmokw_20250603
spatial:
  bbox: null
  centroid: null
  countries:
  - NGA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-06-03'
temporal_resolution: null
title: Flood impact assessment in Mokwa Town, Niger Local Government Area, Niger State,
  Nigeria as of 2 June 2025
version: null
vulnerability: null
---
