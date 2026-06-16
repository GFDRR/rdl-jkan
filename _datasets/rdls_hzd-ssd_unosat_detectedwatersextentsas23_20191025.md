---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/waters-extents-as-of-23-october-2019-over-unity-jonglei-and-lakes-state-of-south-sudan
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/waters-extents-as-of-23-october-2019-over-unity-jonglei-and-lakes-state-of-south-sudan
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/waters-extents-as-of-23-october-2019-over-unity-jonglei-and-lakes-state-of-south-sudan
dataset_id: rdls_hzd-ssd_unosat_detectedwatersextentsas23_20191025
description: 'UNOSAT code: FL20191023SSD This map illustrates satellite-detected surface
  water in Unity, Jonglei and Lakes State of South Sudan as observed from Sentinel-1
  imagery acquired on 23 October 2019. Within the analysed extent of about 85,000
  km2, a total about 1,180 km2 of land appear to be flooded. This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to UNITAR - UNOSAT. Important Note: Flood analysis from Sentinel-1 imagery acquired
  on 23 October 2019 may seriously underestimate the presence of standing floodwater
  in built-up areas due to backscattering of the radar signal. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/waters-extents-as-of-23-october-2019-over-unity-jonglei-and-lakes-state-of-south-sudan]'
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
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: "UNOSAT analysts processed Sentinel-1 synthetic aperture radar imagery\
    \ acquired on 23 October 2019 over Unity, Jonglei and Lakes State, comparing satellite\
    \ images to detect notable changes in surface water presence. The resulting flood\
    \ extent map delineates approximately 1,180 km\xB2 of standing floodwater within\
    \ an 85,000 km\xB2 analysis area, delivered as geodatabase and shapefile formats\
    \ with area measurements in hectares and square meters."
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
- href: https://data.humdata.org/dataset/waters-extents-as-of-23-october-2019-over-unity-jonglei-and-lakes-state-of-south-sudan
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
  description: Satellite detected waters extents, as of 23 October 2019 over Unity,
    Jonglei and Lakes State of South Sudan (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SS/FL20191023SSD/FL20191023SSD_gdb.zip
  format: Geodatabase
  id: resource_ce4c30f4
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20191023SSD_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected waters extents, as of 23 October 2019 over Unity,
    Jonglei and Lakes State of South Sudan (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SS/FL20191023SSD/FL20191023SSD_SHP.zip
  format: null
  id: resource_165831a0
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20191023SSD_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-ssd_unosat_detectedwatersextentsas23_20191025
spatial:
  bbox: null
  centroid: null
  countries:
  - SSD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2019-10-25'
temporal_resolution: null
title: Satellite detected waters extents, as of 23 October 2019 over Unity, Jonglei
  and Lakes State of South Sudan
version: null
vulnerability: null
---
