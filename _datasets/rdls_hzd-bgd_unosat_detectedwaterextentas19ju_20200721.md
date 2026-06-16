---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/satellite-detected-water-extent-as-of-19-july-2020-of-bangladesh
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-as-of-19-july-2020-of-bangladesh
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-as-of-19-july-2020-of-bangladesh
dataset_id: rdls_hzd-bgd_unosat_detectedwaterextentas19ju_20200721
description: 'UNOSAT code: FL20200713BGD This map illustrates satellite-detected surface
  waters in the central parts of Bangladesh as observed from a Sentinel-1 image acquired
  on 19 July 2020 and 13 July 2020. Within the analyzed area of about 40,000 km2,
  a total of about 8,700 km2 of lands appear to be flooded. This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to UNITAR - UNOSAT. Important Note: Flood analysis from Sentinel-1 imagery acquired
  on 19 July 2020 and 13 July 2020 may underestimate the presence of standing waters
  in built-up areas and densely vegetated areas due to backscattering properties of
  the radar signal.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extent-as-of-19-july-2020-of-bangladesh]'
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
  description: "Sentinel-1 synthetic aperture radar imagery acquired on 13 and 19\
    \ July 2020 was analyzed by UNOSAT through visual interpretation and multi-temporal\
    \ comparison to detect surface water extent changes. The resulting water body\
    \ polygons represent observed flooded areas within a 40,000 km\xC2\xB2 study area\
    \ in central Bangladesh, delivered as geodatabase and shapefile formats."
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
- href: https://data.humdata.org/dataset/satellite-detected-water-extent-as-of-19-july-2020-of-bangladesh
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
  description: Satellite detected water extent as of 19 July 2020 of Bangladesh (Zipped
    geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/BD/FL20200713BGD/FL20200713BGD_gdb.zip
  format: Geodatabase
  id: resource_f01ab231
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20200713BGD_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent as of 19 July 2020 of Bangladesh (Zipped
    shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/BD/FL20200713BGD/FL20200713BGD_SHP.zip
  format: null
  id: resource_fbe72e76
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20200713BGD_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-bgd_unosat_detectedwaterextentas19ju_20200721
spatial:
  bbox: null
  centroid: null
  countries:
  - BGD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2020-07-21'
temporal_resolution: null
title: Satellite detected water extent as of 19 July 2020 of Bangladesh
version: null
vulnerability: null
---
