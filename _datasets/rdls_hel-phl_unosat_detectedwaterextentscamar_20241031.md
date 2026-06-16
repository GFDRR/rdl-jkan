---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-in-camarines-sur-province-as-of-29-october-2024
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-in-camarines-sur-province-as-of-29-october-2024
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-in-camarines-sur-province-as-of-29-october-2024
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-in-camarines-sur-province-as-of-29-october-2024
dataset_id: rdls_hel-phl_unosat_detectedwaterextentscamar_20241031
description: "UNOSAT code: TC20241028PHL, GDACS ID: 1001115 This map illustrates a\
  \ satellite-detected surface waters in Camarines Sur Province, Bicol Region, Philippines\
  \ acquired on 29 October 2024 at 17:58 local time (09:58 UTC). Within the boundary\
  \ of Camarines Sur Province of about 5,300 km\xB2, a total of about 130 km\xB2 of\
  \ land appears to be affected by flood waters, with around 230 km\xB2 of cropland\
  \ inundated. The flood extent has receded by approximately 150 km\xB2 since the\
  \ previous observation on 26 October 2024. Based on Worldpop spatial demographic\
  \ data, about 93,000 people are exposed or living close to flooded areas. This is\
  \ a preliminary analysis and has not yet been validated in the field. Please send\
  \ ground feedback to the United Nations Satellite Centre (UNOSAT). Important note:\
  \ Flood analysis from radar images may underestimate the presence of standing waters\
  \ in built-up areas and densely vegetated areas due to the backscattering properties\
  \ of the radar signal.. [Source: This metadata record was automatically extracted\
  \ from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extents-in-camarines-sur-province-as-of-29-october-2024]"
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
    description: Residential population exposed to flood waters based on WorldPop
      spatial demographic data
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
    description: Cropland inundated by flood waters
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
      process: pluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: Satellite imagery acquired on 29 October 2024 was analyzed by UNOSAT
    analysts through visual comparison with previous observations from 26 October
    2024 to detect surface water extents and quantify flood-affected areas. Population
    exposure was estimated by overlaying detected flood extents with WorldPop spatial
    demographic data. The dataset provides post-event empirical observations of flood
    hazard extent and associated impacts on agriculture and population in Camarines
    Sur Province following Typhoon Kong-rey.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
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
- href: https://data.humdata.org/dataset/satellite-detected-water-extents-in-camarines-sur-province-as-of-29-october-2024
  rel: source
loss:
  losses:
  - asset_category: agriculture
    asset_dimension: product
    description: "Direct agricultural loss from inundation of approximately 230 km\xB2\
      \ of cropland"
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population exposed to flood waters estimated at approximately 93,000
      people
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: flood
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
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
  description: Philippines - Satellite detected water extents in Camarines Sur Province
    as of 29 October 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4015/TC20241028PHL_GDB.zip
  format: Geodatabase
  id: resource_c413bd47
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20241028PHL_GDB.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Philippines - Satellite detected water extents in Camarines Sur Province
    as of 29 October 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4015/TC20241028PHL_SHP.zip
  format: null
  id: resource_f0d9c3bf
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20241028PHL_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-phl_unosat_detectedwaterextentscamar_20241031
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
  start: '2024-10-31'
temporal_resolution: null
title: Philippines - Satellite detected water extents in Camarines Sur Province as
  of 29 October 2024
version: null
vulnerability: null
---
