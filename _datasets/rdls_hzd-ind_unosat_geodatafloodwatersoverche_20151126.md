---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-flood-waters-over-chennai-area-tamil-nadu-state-india-november-26-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-flood-waters-over-chennai-area-tamil-nadu-state-india-november-26-2015
dataset_id: rdls_hzd-ind_unosat_geodatafloodwatersoverche_20151126
description: 'This map illustrates satellite-detected waters and probable flood waters
  in the Chennai area of the Tamil Nadu State in India. Using satellite imagery acquired
  12 November 2015, 01 September 2015, and 14 October 2015, UNITAR-UNOSAT identified
  expansion of wetlands and standing waters in the area of Chennai and also some saturated
  soils areas which are mainly agricultural fields. Saturation in the area increased
  between 14 October 2015 and 12 November 2015, and the total water expansion is estimated
  to be about 28%. This analysis has not yet been validated in the field. Please send
  ground feedback to UNITAR-UNOSAT.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-flood-waters-over-chennai-area-tamil-nadu-state-india-november-26-2015]'
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: UNOSAT analysts compared satellite imagery acquired on 01 September
    2015, 14 October 2015, and 12 November 2015 to identify and map standing waters
    and saturated soils in the Chennai area. Water extent was delineated through visual
    interpretation of spectral signatures, with confidence levels and validation status
    recorded for each polygon feature.
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
- href: https://data.humdata.org/dataset/geodata-of-flood-waters-over-chennai-area-tamil-nadu-state-india-november-26-2015
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
  description: Geodata of Flood Waters Over Chennai Area, Tamil Nadu State, India
    (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/IN/FL20151123IND/FL20151123IND_shp.zip
  format: null
  id: resource_15be0d7d
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20151123IND_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Flood Waters Over Chennai Area, Tamil Nadu State, India
    (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/IN/FL20151123IND/FL20151123IND.gdb.zip
  format: null
  id: resource_c4d83b9e
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20151123IND.gdb.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-ind_unosat_geodatafloodwatersoverche_20151126
spatial:
  bbox: null
  centroid: null
  countries:
  - IND
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-11-26'
temporal_resolution: null
title: Geodata of Flood Waters Over Chennai Area, Tamil Nadu State, India
version: null
vulnerability: null
---
