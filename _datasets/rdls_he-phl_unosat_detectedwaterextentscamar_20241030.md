---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-in-camarines-sur-province-as-of-26-october-2024
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-in-camarines-sur-province-as-of-26-october-2024
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-in-camarines-sur-province-as-of-26-october-2024
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-in-camarines-sur-province-as-of-26-october-2024
dataset_id: rdls_he-phl_unosat_detectedwaterextentscamar_20241030
description: "UNOSAT code: TC20241028PHL, GDACS ID: 1001115 This map illustrates cumulative\
  \ detected water using multiple satellites in Camarines Sur Province, Bicol Region,\
  \ Philippines acquired on 26 October 2024. Within the boundary of Camarines Sur\
  \ Province of about 5,300 km\xB2, a total of about 280 km\xB2 of land appears to\
  \ be affected by flood waters, with around 230 km\xB2 of cropland inundated. Based\
  \ on Worldpop spatial demographic data, about 224,000 people are exposed or living\
  \ close to flooded areas. This is a preliminary analysis and has not yet been validated\
  \ in the field. Please send ground feedback to the United Nations Satellite Centre\
  \ (UNOSAT). Important note: Flood analysis from radar images may underestimate the\
  \ presence of standing waters in built-up areas and densely vegetated areas due\
  \ to the backscattering properties of the radar signal.. [Source: This metadata\
  \ record was automatically extracted from the Humanitarian Data Exchange (HDX);\
  \ Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extents-in-camarines-sur-province-as-of-26-october-2024]"
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
    description: Population exposed or living close to flooded areas, derived from
      WorldPop spatial demographic data
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
    description: "Cropland inundated by flood waters, approximately 230 km\xB2 in\
      \ extent"
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts compared multiple satellite images acquired on 26 October
    2024 to detect cumulative water extents in Camarines Sur Province. Detected water
    polygons were intersected with WorldPop population grids and agricultural land
    use data to quantify population exposure and cropland inundation. This preliminary
    post-event analysis provides empirical flood hazard extent and direct impact estimates
    without field validation.
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
- href: https://data.humdata.org/dataset/satellite-detected-water-extents-in-camarines-sur-province-as-of-26-october-2024
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
  description: Philippines - Satellite detected water extents in Camarines Sur Province
    as of 26 October 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4014/TC20241028PHL_GDB.zip
  format: Geodatabase
  id: resource_3838c797
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
    as of 26 October 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4014/TC20241028PHL_SHP.zip
  format: null
  id: resource_74081039
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20241028PHL_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Philippines - Satellite detected water extents in Camarines Sur Province
    as of 26 October 2024 (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/4014/UNOSAT_PopulationExposureAnalysis_TC20241028PHL_26OCT2024.xlsx
  format: null
  id: resource_ef12fe4c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_PopulationExposureAnalysis_TC20241028PHL_26OCT2024.xlsx
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-phl_unosat_detectedwaterextentscamar_20241030
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
  start: '2024-10-30'
temporal_resolution: null
title: Philippines - Satellite detected water extents in Camarines Sur Province as
  of 26 October 2024
version: null
vulnerability: null
---
