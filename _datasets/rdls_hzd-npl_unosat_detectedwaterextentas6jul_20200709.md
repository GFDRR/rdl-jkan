---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/satellite-detected-water-extent-as-of-6-july-2020-over-province-1-and-2-of-nepal
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-as-of-6-july-2020-over-province-1-and-2-of-nepal
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-as-of-6-july-2020-over-province-1-and-2-of-nepal
dataset_id: rdls_hzd-npl_unosat_detectedwaterextentas6jul_20200709
description: 'UNOSAT code: FL20200708NPL This map illustrates satellite-detected surface
  waters in Province 1 and 2 of Nepal as observed from a Sentinel-1 image acquired
  on 6 July 2020. Within the analyzed area of about 2,700 km2, a total of a bout 76
  km2 of lands appear to be flooded. This is a preliminary analysis and has not yet
  been validated in the field. Please send ground feedback to UNITAR - UNOSAT. Important
  Note: Flood analysis from Sentinel-1 imagery acquired on 6 July 2020 may seriously
  underestimate presence of standing flood water in built up areas due to backscattering
  properties. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extent-as-of-6-july-2020-over-province-1-and-2-of-nepal]'
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
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: Sentinel-1 synthetic aperture radar imagery acquired on 6 July 2020
    was analyzed by UNOSAT analysts through visual interpretation and multi-temporal
    comparison to detect surface water extent changes. The resulting water classification
    polygons with confidence levels and area measurements represent observed flood
    extent at a single point in time, not a predictive or probabilistic hazard model.
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
- href: https://data.humdata.org/dataset/satellite-detected-water-extent-as-of-6-july-2020-over-province-1-and-2-of-nepal
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
  description: Satellite detected water extent as of 6 July 2020 over Province 1 and
    2 of Nepal (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/NP/FL20200708NPL/FL20200708NPL_gdb.zip
  format: Geodatabase
  id: resource_70fe8f91
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20200708NPL_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent as of 6 July 2020 over Province 1 and
    2 of Nepal (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/NP/FL20200708NPL/FL20200708NPL_SHP.zip
  format: null
  id: resource_a3f2cdfb
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20200708NPL_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-npl_unosat_detectedwaterextentas6jul_20200709
spatial:
  bbox: null
  centroid: null
  countries:
  - NPL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2020-07-09'
temporal_resolution: null
title: Satellite detected water extent as of 6 July 2020 over Province 1 and 2 of
  Nepal
version: null
vulnerability: null
---
