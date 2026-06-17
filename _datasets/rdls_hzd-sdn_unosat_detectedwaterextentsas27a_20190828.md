---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-as-of-27-aug-2019-over-white-nile-state-sudan
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-as-of-27-aug-2019-over-white-nile-state-sudan
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-as-of-27-aug-2019-over-white-nile-state-sudan
dataset_id: rdls_hzd-sdn_unosat_detectedwaterextentsas27a_20190828
description: 'UNOSAT code: FL20190815SDN This map illustrates satellite-detected surface
  water in White Nile State, Sudan as observed from Radarsat-2 imagery acquired on
  27 August 2019. Within the analysed area of about 3,000 km2, a total 176 sq km of
  lands appear to be flooded as of 27 August 2019. This is a preliminary analysis
  and has not yet been validated in the field. Please send ground feedback to UNITAR
  - UNOSAT.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extents-as-of-27-aug-2019-over-white-nile-state-sudan]'
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
  - analysis_type: deterministic
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
  description: Radarsat-2 synthetic aperture radar (SAR) imagery acquired on 27 August
    2019 was processed and analyzed by UNOSAT analysts to detect and delineate satellite-observed
    surface water extents over White Nile State, Sudan. The analysis involved visual
    interpretation and change detection of SAR imagery to map flooded areas within
    an approximately 3,000 km2 study area. The resulting dataset provides a preliminary,
    event-specific flood extent map intended to support emergency response and situational
    awareness.
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
- href: https://data.humdata.org/dataset/satellite-detected-water-extents-as-of-27-aug-2019-over-white-nile-state-sudan
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
  description: Satellite detected water extents, as of 27 Aug 2019 over White Nile
    State, Sudan (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SD/FL20190815SDN/FL20190815SDN_gdb.zip
  format: Geodatabase
  id: resource_ee27627d
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20190815SDN_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents, as of 27 Aug 2019 over White Nile
    State, Sudan (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SD/FL20190815SDN/FL20190815SDN_SHP.zip
  format: null
  id: resource_e5fdd353
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20190815SDN_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-sdn_unosat_detectedwaterextentsas27a_20190828
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
  start: '2019-08-28'
temporal_resolution: null
title: Satellite detected water extents, as of 27 Aug 2019 over White Nile State,
  Sudan
version: null
vulnerability: null
---
