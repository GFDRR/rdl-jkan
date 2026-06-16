---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-1 satellite imagery
    url: https://data.humdata.org/dataset/satellite-detected-waters-in-sylhet-division-bangladesh-2819
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/satellite-detected-waters-in-sylhet-division-bangladesh-2819
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-waters-in-sylhet-division-bangladesh-2819
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-waters-in-sylhet-division-bangladesh-2819
dataset_id: rdls_he-bgd_unosat_detectedwaterssylhetdivis_20180619
description: 'This map illustrates satellite-detected surface water extent in the
  northeastern part of Bangladesh using a Sentinel-1 satellite image acquired on the
  15 June 2018. In the analysed area; about 500,000 ha of lands are likely affected.
  The population exposure analysis using WorldPop data shows that 3,500,000 people
  are potentially affected by floods in this analysed zone: ~1,500,000 are located
  in Sylhet Division and ~1,000,000 in Sumanganj Division and about 35% of the population
  is leaving within or close to inundated areas. This is a preliminary analysis and
  has not yet been validated in the field. Please send ground feedback to UNITAR-UNOSAT..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-waters-in-sylhet-division-bangladesh-2819]'
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
    description: Population exposure analysis using WorldPop data showing 3,500,000
      people potentially affected by floods, with approximately 35% located within
      or close to inundated areas
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
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: Sentinel-1 SAR imagery from 15 June 2018 was analyzed by UNOSAT through
    visual interpretation and multi-temporal change detection to delineate surface
    water extent in Sylhet Division. Population exposure was quantified by intersecting
    the inundated area polygons with WorldPop gridded population data to estimate
    affected populations across administrative divisions.
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
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/satellite-detected-waters-in-sylhet-division-bangladesh-2819
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
  description: Satellite Detected Waters in Sylhet Division, Bangladesh (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/BD/FL20180619BGD/FL20180619BGD_SHP.zip
  format: null
  id: resource_e91bec17
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20180619BGD_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-bgd_unosat_detectedwaterssylhetdivis_20180619
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
  start: '2018-06-19'
temporal_resolution: null
title: Satellite Detected Waters in Sylhet Division, Bangladesh
version: null
vulnerability: null
---
