---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-satellite-detected-waters-over-san-miguel-leyte-eastern-visayas-ph-december-08-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-satellite-detected-waters-over-san-miguel-leyte-eastern-visayas-ph-december-08-2014
dataset_id: rdls_hzd-phl_unosat_geodatadetectedwatersover_20141208
description: 'This map illustrates satellite-detected areas with waters as detected
  by TerraSAR-X imagery acquired the 08 December 2014 in San Miguel area, west of
  Tacloban city, Leyte Province (Philippines). The heavy rains related to the typhoon
  Hagupit induced areas with standing waters. This analysis has not yet been validated
  in the field. Please send ground feedback to UNITAR /UNOSAT.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/geodata-of-satellite-detected-waters-over-san-miguel-leyte-eastern-visayas-ph-december-08-2014]'
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
      process: pluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-4.0
lineage:
  description: TerraSAR-X satellite imagery acquired on 8 December 2014 was analyzed
    by UNOSAT to detect standing water areas resulting from heavy rainfall associated
    with typhoon Hagupit. Analysts compared satellite imagery to identify notable
    changes and delineate water-covered areas as vector polygons. The analysis represents
    observed post-event water extent but has not been field-validated.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/geodata-of-satellite-detected-waters-over-san-miguel-leyte-eastern-visayas-ph-december-08-2014
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
  description: Geodata of Satellite Detected Waters Over San Miguel, Leyte, Eastern
    Visayas, Philippines (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/PH/TC20141204PHL/TC20141204PHL_shp.zip
  format: null
  id: resource_248726bc
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20141204PHL_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Satellite Detected Waters Over San Miguel, Leyte, Eastern
    Visayas, Philippines (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/PH/TC20141204PHL/TC20141204PHL.gdb.zip
  format: null
  id: resource_c6294cf6
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20141204PHL.gdb.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-phl_unosat_geodatadetectedwatersover_20141208
spatial:
  bbox: null
  centroid: null
  countries:
  - PHL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2014-12-08'
temporal_resolution: null
title: Geodata of Satellite Detected Waters Over San Miguel, Leyte, Eastern Visayas,
  Philippines
version: null
vulnerability: null
---
