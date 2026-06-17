---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-2 satellite imagery
    url: https://data.humdata.org/dataset/water-extent-in-n-djamena-department-n-djamena-region-chad-as-of-20-october-2022
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop population data
    url: https://data.humdata.org/dataset/water-extent-in-n-djamena-department-n-djamena-region-chad-as-of-20-october-2022
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-n-djamena-department-n-djamena-region-chad-as-of-20-october-2022
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-n-djamena-department-n-djamena-region-chad-as-of-20-october-2022
dataset_id: rdls_he-tcd_unosat_detectedwaterextentndjame_20221021
description: 'UNOSAT code FL20221019TCD This map illustrates satellite-detected surface
  waters in N''Djamena Department, N''Djamena Region, Chad as observed from a Sentinel-2
  image acquired on 20 October 2022 at 10:20 local time. Within the map extent of
  about 100 km2, about 42 km2 of lands appear to be flooded and 5,408 structures are
  potentially affected by the floods. Based on Worldpop population data and the detected
  surface waters, about 160,000 people are potentially exposed or living close to
  flooded areas. This is a preliminary analysis and has not yet been validated in
  the field. Please send ground feedback to United Nations Satellite Centre (UNOSAT)..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-in-n-djamena-department-n-djamena-region-chad-as-of-20-october-2022]'
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
    description: Building structures potentially affected by detected flood waters
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Population potentially exposed or living close to flooded areas based
      on WorldPop data
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_2
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
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts reviewed Sentinel-2 satellite imagery acquired on 20
    October 2022 and performed visual change detection to delineate surface water
    extent in N'Djamena department. Detected flood polygons were intersected with
    building footprints and WorldPop population grids to estimate structural and population
    exposure. Results represent preliminary satellite-based assessment not yet validated
    in the field.
  sources:
  - id: source_1
    license: null
    name: Sentinel-2 satellite imagery
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: WorldPop population data
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/water-extent-in-n-djamena-department-n-djamena-region-chad-as-of-20-october-2022
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
  description: Satellite detected water extent in N'Djamena department, N'Djamena
    Region, Chad as of 20 October 2022 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3422/FL20221019TCD_gdb.zip
  format: Geodatabase
  id: resource_c8cefb64
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20221019TCD_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent in N'Djamena department, N'Djamena
    Region, Chad as of 20 October 2022 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3422/FL20221019TCD_SHP.zip
  format: null
  id: resource_2038ddfe
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20221019TCD_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-tcd_unosat_detectedwaterextentndjame_20221021
spatial:
  bbox: null
  centroid: null
  countries:
  - TCD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-10-21'
temporal_resolution: null
title: Satellite detected water extent in N'Djamena department, N'Djamena Region,
  Chad as of 20 October 2022
version: null
vulnerability: null
---
