---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-1 satellite imagery
    url: https://data.humdata.org/dataset/waters-extents-as-of-4-march-2020-over-central-luapula-muchinga-and-northern-province-zamb
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop population data
    url: https://data.humdata.org/dataset/waters-extents-as-of-4-march-2020-over-central-luapula-muchinga-and-northern-province-zamb
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/waters-extents-as-of-4-march-2020-over-central-luapula-muchinga-and-northern-province-zamb
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/waters-extents-as-of-4-march-2020-over-central-luapula-muchinga-and-northern-province-zamb
dataset_id: rdls_he-zmb_unosat_detectedwatersextentsas4m_20200306
description: 'UNOSAT code: FL20200305ZMB This map illustrates satellite-detected waters
  in Chitambo, Lunga, Samfya, Lavushimanda and Chilubi District; Central, Luapula,
  Muchinga and Northern Province of Zambia as observed from Sentinel-1 imagery acquired
  on 4 March 2020. Within the analysed area of 10,000 km2, a total of about 705 km2
  of land appear to be flooded. Based on Worldpop population data and the detected
  surface waters, about 7,000 people are potentially exposed or living close to flooded
  areas. This is a preliminary analysis and has not yet been validated in the field.
  Please send ground feedback to UNITARUNOSAT.. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/waters-extents-as-of-4-march-2020-over-central-luapula-muchinga-and-northern-province-zamb]'
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
    description: Population potentially exposed or living close to flooded areas,
      estimated at approximately 7,000 people based on WorldPop data
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
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: Sentinel-1 SAR imagery from 4 March 2020 was analyzed by UNOSAT through
    visual interpretation and multi-temporal change detection to identify surface
    water extents. The detected flood area (705 km2) was then intersected with WorldPop
    gridded population data to estimate approximately 7,000 people potentially exposed
    to flooded areas in five districts across four provinces of Zambia.
  sources:
  - id: source_1
    license: null
    name: Sentinel-1 satellite imagery
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
- href: https://data.humdata.org/dataset/waters-extents-as-of-4-march-2020-over-central-luapula-muchinga-and-northern-province-zamb
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
  description: Satellite detected waters extents, as of 4 March 2020 over Central,
    Luapula, Muchinga and Northern Province, Zambia (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/ZM/FL20200305ZMB/FL20200305ZMB_gdb.zip
  format: Geodatabase
  id: resource_66948228
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
  description: Satellite detected waters extents, as of 4 March 2020 over Central,
    Luapula, Muchinga and Northern Province, Zambia (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/ZM/FL20200305ZMB/FL20200305ZMB_SHP.zip
  format: null
  id: resource_6035b366
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
slug: rdls_he-zmb_unosat_detectedwatersextentsas4m_20200306
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
title: Satellite detected waters extents, as of 4 March 2020 over Central, Luapula,
  Muchinga and Northern Province, Zambia
version: null
vulnerability: null
---
