---
attributions:
- entity:
    affiliation: null
    email: null
    name: VIIRS-NOAA
    url: https://data.humdata.org/dataset/waters-extents-between-the-1st-and-the-05th-march-2020-over-northern-zambia
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/waters-extents-between-the-1st-and-the-05th-march-2020-over-northern-zambia
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/waters-extents-between-the-1st-and-the-05th-march-2020-over-northern-zambia
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/waters-extents-between-the-1st-and-the-05th-march-2020-over-northern-zambia
dataset_id: rdls_he-zmb_unosat_detectedwatersextentsover_20200306
description: 'UNOSAT code: FL20200305ZMB This map illustrates satellite-detected water
  via VIIRS-NOAA over Central, Luapula, Muchinga and Northern Province in Republic
  of Zambia between the 1st and the 05th March 2020. Within the analysed extent not
  covered by clouds, a total of about 10,000 km2 appear to be flooded. Based on Worldpop
  population about 28,000 people were potentially exposed or living close to flooded
  areas in Lunga district. This is a preliminary analysis and has not yet been validated
  in the field. Please send ground fedback to UNITAR - UNOSAT.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/waters-extents-between-the-1st-and-the-05th-march-2020-over-northern-zambia]'
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
    description: Population potentially exposed or living close to flooded areas based
      on WorldPop data
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "UNOSAT analysts reviewed and compared VIIRS-NOAA satellite imagery\
    \ acquired between March 1-5, 2020 to detect water extents and identify flooded\
    \ areas across four provinces in Zambia. Detected flood polygons (approximately\
    \ 10,000 km\xC2\xB2) were intersected with WorldPop population data to estimate\
    \ exposure in Lunga district. This is a preliminary post-event satellite-based\
    \ damage assessment not yet validated in the field."
  sources:
  - id: source_1
    license: null
    name: VIIRS-NOAA
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/waters-extents-between-the-1st-and-the-05th-march-2020-over-northern-zambia
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
  description: Satellite detected waters extents over Northern Zambia (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/ZM/FL20200305ZMB/FL20200305ZMB_gdb.zip
  format: Geodatabase
  id: resource_1464d5aa
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20200305ZMB_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected waters extents over Northern Zambia (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/ZM/FL20200305ZMB/FL20200305ZMB_SHP.zip
  format: null
  id: resource_c68e7697
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20200305ZMB_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-zmb_unosat_detectedwatersextentsover_20200306
spatial:
  bbox: null
  centroid: null
  countries:
  - ZMB
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2020-03-06'
temporal_resolution: null
title: Satellite detected waters extents over Northern Zambia
version: null
vulnerability: null
---
