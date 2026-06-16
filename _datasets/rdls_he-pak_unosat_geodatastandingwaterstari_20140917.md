---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-standing-waters-in-tarind-muhammed-panah-area-punjab-province-paki-september-17-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-standing-waters-in-tarind-muhammed-panah-area-punjab-province-paki-september-17-2014
dataset_id: rdls_he-pak_unosat_geodatastandingwaterstari_20140917
description: 'This map illustrates satellite-detected areas with waters as detected
  by SENTINEL-1 imagery acquired the 16 September 2014 in Tarind Muhammad Panah area.
  The Indus and the Panjnad rivers expanded and seem to have inundated some agricultural
  fields along the Indus River and the Panjnad River in the Punjab Province (Pakistan).
  This analysis has not yet been validated in the field. Please send ground feedback
  to UNITAR /UNOSAT.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-standing-waters-in-tarind-muhammed-panah-area-punjab-province-paki-september-17-2014]'
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
    description: Agricultural fields inundated along the Indus River and Panjnad River
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_1
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
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
        intensity_measure: AA:km2
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: SENTINEL-1 satellite imagery acquired on 16 September 2014 was analyzed
    by UNOSAT to detect water-covered areas through visual interpretation and comparison
    with reference imagery. The resulting inundated area polygons were classified
    by water status and confidence level, with areas calculated in square meters and
    hectares. This represents an observed, post-event flood extent map without field
    validation at the time of publication.
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
- href: https://data.humdata.org/dataset/geodata-of-standing-waters-in-tarind-muhammed-panah-area-punjab-province-paki-september-17-2014
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
  description: Geodata of Standing Waters in Tarind Muhammed Panah Area, Punjab Province,
    Pakistan (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/PK/FL20140910PAK/FL20140910PAK_shp.zip
  format: null
  id: resource_63012b46
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20140910PAK_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Standing Waters in Tarind Muhammed Panah Area, Punjab Province,
    Pakistan (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/PK/FL20140910PAK/FL20140910PAK_gdb.zip
  format: null
  id: resource_8078502a
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20140910PAK_gdb.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-pak_unosat_geodatastandingwaterstari_20140917
spatial:
  bbox: null
  centroid: null
  countries:
  - PAK
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2014-09-17'
temporal_resolution: null
title: Geodata of Standing Waters in Tarind Muhammed Panah Area, Punjab Province,
  Pakistan
version: null
vulnerability: null
---
