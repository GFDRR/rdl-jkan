---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-1 satellite imagery
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-in-north-viet-nam-as-of-26-august-2025
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop population data
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-in-north-viet-nam-as-of-26-august-2025
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-in-north-viet-nam-as-of-26-august-2025
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-in-north-viet-nam-as-of-26-august-2025
dataset_id: rdls_he-vnm_unosat_detectedwaterextentsnorth_20250828
description: "UNOSAT code: TC20250826VNM This map illustrates the satellite detected\
  \ water extent in Northern part of Viet Nam as observed from Sentinel-1 satellite\
  \ images acquired on 26 August 2025 at 05:51 local time (22:51 UTC). Within the\
  \ analyzed area of approximately 74,000 km\xB2, about 1,200 km\xB2 of land appears\
  \ to be affected by floodwaters. Based on WorldPop population data and the flood\
  \ extent, approximately 708,000 people are potentially exposed or living close to\
  \ the flooded areas. This is a preliminary analysis and has not yet been validated\
  \ in the field. Please send ground feedback to the United Nations Satellite Centre\
  \ (UNOSAT). Important note: Flood analysis from radar images may underestimate the\
  \ presence of standing waters in built-up areas and densely vegetated areas due\
  \ to the backscattering properties of the radar signal. [Source: This metadata record\
  \ was automatically extracted from the Humanitarian Data Exchange (HDX); Original\
  \ dataset: https://data.humdata.org/dataset/satellite-detected-water-extents-in-north-viet-nam-as-of-26-august-2025]"
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
    description: Population potentially exposed or living close to flooded areas derived
      from WorldPop data
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
  description: "Sentinel-1 SAR satellite imagery acquired on 26 August 2025 was analyzed\
    \ by UNOSAT to detect water extent through comparison with reference imagery.\
    \ The resulting flood extent polygon (1,200 km\xB2) was intersected with WorldPop\
    \ gridded population data to estimate approximately 708,000 people potentially\
    \ exposed to floodwaters in northern Vietnam."
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
- href: https://data.humdata.org/dataset/satellite-detected-water-extents-in-north-viet-nam-as-of-26-august-2025
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
  description: Satellite detected water extents in north Viet Nam as of 26 August
    2025 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4184/TC20250825VNM_GDB.zip
  format: Geodatabase
  id: resource_410c00b8
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20250825VNM_GDB.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents in north Viet Nam as of 26 August
    2025 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4184/TC20250825VNM_SHP.zip
  format: null
  id: resource_f6681231
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20250825VNM_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents in north Viet Nam as of 26 August
    2025 (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/4184/UNOSAT_PopulationExposure_TC20250826VNM_26Aug2025.xlsx
  format: null
  id: resource_75cb2117
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_PopulationExposure_TC20250826VNM_26Aug2025.xlsx
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-vnm_unosat_detectedwaterextentsnorth_20250828
spatial:
  bbox: null
  centroid: null
  countries:
  - VNM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-08-28'
temporal_resolution: null
title: Satellite detected water extents in north Viet Nam as of 26 August 2025
version: null
vulnerability: null
---
