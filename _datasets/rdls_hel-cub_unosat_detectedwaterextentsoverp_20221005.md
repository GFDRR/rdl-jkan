---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-1 satellite imagery
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-over-pinar-del-rio-province-cuba-as-of-28-september-2022
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-over-pinar-del-rio-province-cuba-as-of-28-september-2022
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-over-pinar-del-rio-province-cuba-as-of-28-september-2022
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-over-pinar-del-rio-province-cuba-as-of-28-september-2022
dataset_id: rdls_hel-cub_unosat_detectedwaterextentsoverp_20221005
description: "UNOSAT code TC20221001CUB, GDACS Id: 1000923 This map illustrates satellite-detected\
  \ surface waters in Pinar del R\xEDo province, Cuba as observed from a Sentinel-1\
  \ imagery acquired on 28 September 2022 at 07:27 local time. Within the analyzed\
  \ area of about 1,300 km\xB2, a total of about 27 km\xB2 of lands appear to be affected\
  \ with flood waters amongst which 13 km\xB2 are flooded croplands. Based on Worldpop\
  \ population data and the detected surface waters, about 4,200 people are potentially\
  \ exposed or living close to flooded areas. This is a preliminary analysis and has\
  \ not yet been validated in the field. Please send ground feedback to United Nations\
  \ Satellite Centre (UNOSAT). Important note: Flood analysis from radar images may\
  \ underestimate the presence of standing waters in built-up areas and densely vegetated\
  \ areas due to backscattering properties of the radar signal.. [Source: This metadata\
  \ record was automatically extracted from the Humanitarian Data Exchange (HDX);\
  \ Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extents-over-pinar-del-rio-province-cuba-as-of-28-september-2022]"
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
    description: Flooded croplands identified in the affected area
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
      process: pluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: Sentinel-1 SAR imagery acquired on 28 September 2022 was analyzed by
    UNOSAT analysts to detect surface water extents through comparison with reference
    imagery. Detected flood waters were classified by land use type (croplands vs.
    other) and quantified by area. Population exposure was estimated by intersecting
    detected water extents with WorldPop gridded population data to identify people
    living in or near flooded areas.
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
- href: https://data.humdata.org/dataset/satellite-detected-water-extents-over-pinar-del-rio-province-cuba-as-of-28-september-2022
  rel: source
loss:
  losses:
  - asset_category: agriculture
    asset_dimension: product
    description: Direct flood inundation of croplands detected by satellite imagery
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
    description: Population exposed to or living in proximity to detected flood waters
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
  description: "Satellite detected water extents over Pinar del R\xEDo province, Cuba\
    \ as of 28 September 2022 (Zipped geodatabase)"
  download_url: https://unosat.org/static/unosat_filesystem/3392/TC20221001CUB_gdb.zip
  format: Geodatabase
  id: resource_c504f510
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20221001CUB_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Satellite detected water extents over Pinar del R\xEDo province, Cuba\
    \ as of 28 September 2022 (Zipped shapefile)"
  download_url: https://unosat.org/static/unosat_filesystem/3392/TC20221001CUB_SHP.zip
  format: null
  id: resource_71e48ce7
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20221001CUB_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-cub_unosat_detectedwaterextentsoverp_20221005
spatial:
  bbox: null
  centroid: null
  countries:
  - CUB
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-10-05'
temporal_resolution: null
title: "Satellite detected water extents over Pinar del R\xEDo province, Cuba as of\
  \ 28 September 2022"
version: null
vulnerability: null
---
