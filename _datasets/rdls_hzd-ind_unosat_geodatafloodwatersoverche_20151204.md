---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-flood-waters-over-chennai-area-tamil-nadu-state-india-december-04-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-flood-waters-over-chennai-area-tamil-nadu-state-india-december-04-2015
dataset_id: rdls_hzd-ind_unosat_geodatafloodwatersoverche_20151204
description: 'This map illustrates satellite-detected waters and probable flood waters
  in the Chennai area of the Tamil Nadu State in India. Using satellite imagery acquired
  24 November 2015, 12 November 2015, 14 October 2015 and 01 September 2015. UNITAR-UNOSAT
  identified expansion of waters in the area of Chennai. Standing waters extended
  between the 24 November 2015 and 12 November 2015 and the total water expansion
  is estimated to be about 10% between the two dates. This analysis has not yet been
  validated in the field. Please send ground feedback to UNITAR-UNOSAT.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-flood-waters-over-chennai-area-tamil-nadu-state-india-december-04-2015]'
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
  event_sets_by_hazard_type:
    flood:
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
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: UNOSAT analysts compared satellite imagery acquired on four dates (01
    September 2015, 14 October 2015, 12 November 2015, and 24 November 2015) to identify
    and map standing water and probable flood waters in Chennai. Water extent polygons
    were digitized with confidence levels and field validation flags; total water
    expansion of approximately 10% was estimated between 12 and 24 November 2015.
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
- href: https://data.humdata.org/dataset/geodata-of-flood-waters-over-chennai-area-tamil-nadu-state-india-december-04-2015
  rel: source
loss:
  losses: []
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
  id: resource_811aad8d
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
  id: resource_39ee9119
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
slug: rdls_hzd-ind_unosat_geodatafloodwatersoverche_20151204
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
  start: '2015-12-04'
temporal_resolution: null
title: Geodata of Flood Waters Over Chennai Area, Tamil Nadu State, India
version: null
vulnerability: null
---
