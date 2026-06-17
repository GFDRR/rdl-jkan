---
attributions:
- entity:
    affiliation: null
    email: null
    name: World Population database
    url: https://data.humdata.org/dataset/geodata-of-flood-waters-over-zambezia-province-mozambique-january-19-2015
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-flood-waters-over-zambezia-province-mozambique-january-19-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-flood-waters-over-zambezia-province-mozambique-january-19-2015
dataset_id: rdls_he-moz_unosat_geodatafloodwatersoverzam_20150119
description: 'This map illustrates satellite-detected flood waters in the Maganka
  Da Costa, Namacurra and Mocuba Districts of Zambezia Province, Mozambique, as detected
  by Radarsat-2 imagery acquired 18 January 2015. Between 11 and 18 January 2015 flood
  waters affected roughly 85,000 hectares of land, with inundated areas increasing
  approximately 800% from pre-flood areas, particularly in the coastal part of Mangaja
  Da Costa District. About 41 villages are located within the flooded zone, and according
  to the World Population database around 73,000 people are located within these potentially
  affected areas. This is a preliminary analysis and has not yet been validated in
  the field. Please send ground feedback to UNITAR / UNOSAT.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/geodata-of-flood-waters-over-zambezia-province-mozambique-january-19-2015]'
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
    description: Approximately 73,000 people located within potentially affected flood
      areas across 41 villages
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Agricultural land and natural environment affected by flood waters
      covering approximately 85,000 hectares
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_2
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
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
license: CC-BY-4.0
lineage:
  description: Radarsat-2 satellite imagery acquired on 18 January 2015 was analyzed
    by UNOSAT to detect flood water extent through comparison with pre-flood baseline
    imagery. Inundated areas were mapped as vector geometries covering approximately
    85,000 hectares across three districts. Population exposure was estimated by overlaying
    World Population database with the mapped flood extent to identify approximately
    73,000 people in 41 villages within the affected zone.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: World Population database
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/geodata-of-flood-waters-over-zambezia-province-mozambique-january-19-2015
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
  description: Geodata of Flood Waters Over Zambezia Province, Mozambique (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MZ/FL20150112MOZ/FL20150112MOZ_shp.zip
  format: null
  id: resource_b675e0d3
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20150112MOZ_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Flood Waters Over Zambezia Province, Mozambique (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MZ/FL20150112MOZ/FL20150112MOZ.gdb.zip
  format: null
  id: resource_be7f19f1
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20150112MOZ.gdb.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-moz_unosat_geodatafloodwatersoverzam_20150119
spatial:
  bbox: null
  centroid: null
  countries:
  - MOZ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-01-19'
temporal_resolution: null
title: Geodata of Flood Waters Over Zambezia Province, Mozambique
version: null
vulnerability: null
---
