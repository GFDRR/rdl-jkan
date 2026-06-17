---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-extents-as-of-5-november-2019-over-basse-kotto-prefectures-of-the-central-african-re
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-as-of-5-november-2019-over-basse-kotto-prefectures-of-the-central-african-re
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-as-of-5-november-2019-over-basse-kotto-prefectures-of-the-central-african-re
dataset_id: rdls_hzd-caf_unosat_detectedwaterextentsas5no_20191113
description: 'UNOSAT code: FL20191028CAF This map illustrates satellite-detected surface
  water in Ouaka and Basse-Kotto Prefectures of the Central African Republic, as observed
  from Sentinel-1 imagery acquired on 5 November 2019. Within the analysed extent
  of about 970 km2, a total about 9 km2 of land appear to be flooded. This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to UNITAR -UNOSAT. Important note: Flood analysis with Sentinel-1 imagery may notably
  underestimate the presence of standing water in built up areas due to backscattering
  of the radar signal.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extents-as-of-5-november-2019-over-basse-kotto-prefectures-of-the-central-african-re]'
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
  description: Sentinel-1 synthetic aperture radar imagery acquired on 5 November
    2019 was analyzed by UNOSAT analysts through visual interpretation and multi-temporal
    comparison to detect surface water extent changes. Water bodies were delineated
    and mapped as vector polygons with area calculations, representing observed flood
    extent at a single point in time without field validation.
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
- href: https://data.humdata.org/dataset/water-extents-as-of-5-november-2019-over-basse-kotto-prefectures-of-the-central-african-re
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
  description: Satellite-detected water extents, as of 5 November 2019 over Basse-Kotto
    Prefectures of the Central African Republic (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/CF/FL20191028CAF/FL20191028CAF_gdb.zip
  format: Geodatabase
  id: resource_745a9ee6
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20191028CAF_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite-detected water extents, as of 5 November 2019 over Basse-Kotto
    Prefectures of the Central African Republic (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/CF/FL20191028CAF/FL20191028CAF_SHP.zip
  format: null
  id: resource_af6b89f3
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20191028CAF_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-caf_unosat_detectedwaterextentsas5no_20191113
spatial:
  bbox: null
  centroid: null
  countries:
  - CAF
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2019-11-13'
temporal_resolution: null
title: Satellite-detected water extents, as of 5 November 2019 over Basse-Kotto Prefectures
  of the Central African Republic
version: null
vulnerability: null
---
