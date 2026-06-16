---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-in-louangnamtha-province-lao-pdr-as-of-11-september-2024
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-in-louangnamtha-province-lao-pdr-as-of-11-september-2024
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-in-louangnamtha-province-lao-pdr-as-of-11-september-2024
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-in-louangnamtha-province-lao-pdr-as-of-11-september-2024
dataset_id: rdls_he-lao_unosat_detectedwaterextentslouan_20240917
description: "UNOSAT code: FL20240913LAO This map illustrates the floods detected\
  \ using Sentinel-1 images acquired on 11 September 2024 at 06:07 local time. Within\
  \ the analysed area of approximately 60 km\xB2, about 7 km\xB2 of land appears to\
  \ be affected by floodwaters, including 6 km\xB2 of croplands. According to WorldPop\
  \ spatial demographic data, an estimated 2,500 people are exposed to or living near\
  \ the flooded areas. Please note that this is a preliminary analysis and has not\
  \ been validated in the field. We welcome any ground feedback that can be provided\
  \ to the United Nations Satellite Centre (UNOSAT). Important: Flood analysis based\
  \ on radar images may underestimate the extent of standing water in built-up or\
  \ densely vegetated areas due to the radar signal's backscattering properties..\
  \ [Source: This metadata record was automatically extracted from the Humanitarian\
  \ Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extents-in-louangnamtha-province-lao-pdr-as-of-11-september-2024]"
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
    description: Cropland area affected by floodwaters
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
    description: Population exposed to or living near flooded areas estimated from
      WorldPop data
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
license: CC-BY-SA-4.0
lineage:
  description: "Sentinel-1 SAR imagery acquired on 11 September 2024 was analyzed\
    \ by UNOSAT analysts through multi-temporal comparison to detect water extents\
    \ and map flooded areas. WorldPop spatial demographic data was overlaid to estimate\
    \ population exposure. The resulting geodatabase and shapefile products represent\
    \ observed flood water boundaries and associated exposure metrics for the 60 km\xB2\
    \ study area in Louangnamtha Province."
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
- href: https://data.humdata.org/dataset/satellite-detected-water-extents-in-louangnamtha-province-lao-pdr-as-of-11-september-2024
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
  description: Satellite detected water extents in Louangnamtha Province, Lao PDR
    as of 11 September 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3973/FL20240913LAO_GDB.zip
  format: Geodatabase
  id: resource_331f597f
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240913LAO_GDB.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents in Louangnamtha Province, Lao PDR
    as of 11 September 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3973/FL20240913LAO_SHP.7z
  format: null
  id: resource_8fbdb3a6
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240913LAO_SHP.7z
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-lao_unosat_detectedwaterextentslouan_20240917
spatial:
  bbox: null
  centroid: null
  countries:
  - LAO
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-09-17'
temporal_resolution: null
title: Satellite detected water extents in Louangnamtha Province, Lao PDR as of 11
  September 2024
version: null
vulnerability: null
---
