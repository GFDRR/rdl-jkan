---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-1 satellite imagery
    url: https://data.humdata.org/dataset/waters-in-camarines-norte-province-bicol-region-region-v-of-philippines-as-of-12-november-
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/waters-in-camarines-norte-province-bicol-region-region-v-of-philippines-as-of-12-november-
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/waters-in-camarines-norte-province-bicol-region-region-v-of-philippines-as-of-12-november-
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/waters-in-camarines-norte-province-bicol-region-region-v-of-philippines-as-of-12-november-
dataset_id: rdls_he-phl_unosat_detectedwaterscamarinesno_20201112
description: 'UNOSAT code: TC20201111PHL This map illustrates satellite-detected surface
  waters in Camarines Norte province of Philippines as observed from a Sentinel-1
  image acquired on 12 November 2020 at 05:38 local time. Within the analyzed area
  of about 650 km2, a total of about 60 km2 of lands appear to be flooded. Based on
  Worldpop population data and the detected surface waters, about 32,000 people are
  potentially exposed or living close to flooded areas. This is a preliminary analysis
  and has not yet been validated in the field. Please send ground feedback to UNITAR-UNOSAT.
  Important Note: Flood analysis from radar images may underestimate the presence
  of standing waters in built-up areas and densely vegetated areas due to backscattering
  properties of the radar signal.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/waters-in-camarines-norte-province-bicol-region-region-v-of-philippines-as-of-12-november-]'
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
    description: Population potentially exposed to flooded areas based on WorldPop
      data
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "Sentinel-1 SAR imagery acquired on 12 November 2020 was analyzed by\
    \ UNOSAT analysts through visual interpretation and change detection to identify\
    \ surface water extent in Camarines Norte province. Detected flooded areas (~60\
    \ km\xC2\xB2) were intersected with WorldPop gridded population data to estimate\
    \ approximately 32,000 people potentially exposed to or living close to flooded\
    \ areas. This is a preliminary post-event damage assessment product."
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
- href: https://data.humdata.org/dataset/waters-in-camarines-norte-province-bicol-region-region-v-of-philippines-as-of-12-november-
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
  description: Satellite detected waters in Camarines Norte Province, Bicol Region
    (Region V) of Philippines as of 12 November 2020 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/PH/TC20201111PHL/TC20201111PHL_gdb.zip
  format: Geodatabase
  id: resource_9b77a078
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20201111PHL_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected waters in Camarines Norte Province, Bicol Region
    (Region V) of Philippines as of 12 November 2020 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/PH/TC20201111PHL/TC20201111PHL_SHP.zip
  format: null
  id: resource_6d8f80fe
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20201111PHL_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-phl_unosat_detectedwaterscamarinesno_20201112
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
  start: '2020-11-12'
temporal_resolution: null
title: Satellite detected waters in Camarines Norte Province, Bicol Region (Region
  V) of Philippines as of 12 November 2020
version: null
vulnerability: null
---
