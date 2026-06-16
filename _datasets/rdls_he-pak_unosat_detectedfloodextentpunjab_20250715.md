---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-1 SAR imagery
    url: https://data.humdata.org/dataset/satellite-detected-flood-extent-in-punjab-province-pakistan-10-july-2025
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/satellite-detected-flood-extent-in-punjab-province-pakistan-10-july-2025
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-flood-extent-in-punjab-province-pakistan-10-july-2025
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-flood-extent-in-punjab-province-pakistan-10-july-2025
dataset_id: rdls_he-pak_unosat_detectedfloodextentpunjab_20250715
description: "UNOSAT code: FL20250630PAK This map illustrates the extent of floodwaters\
  \ detected in Punjab Province using Sentinel-1 imagery acquired on 10 July 2025\
  \ at 18:04 local time (13:04 UTC). Within the analyzed area of approximately 50,000\
  \ km\xB2, around 4,200 km\xB2 of land appears to be inundated. Based on WorldPop\
  \ population data and the observed flood extent, an estimated 3.3 million people\
  \ are potentially exposed or living in close proximity to the affected areas. This\
  \ is a preliminary analysis and has not been validated on the ground. We kindly\
  \ encourage you to share any field observations or feedback with the United Nations\
  \ Satellite Centre (UNOSAT). Important Note: Flood analysis derived from radar imagery\
  \ may underestimate standing water in urban or densely vegetated areas due to the\
  \ radar signal's backscattering characteristics. Should you have any questions or\
  \ require further support, please do not hesitate to contact us. We remain at your\
  \ disposal.. [Source: This metadata record was automatically extracted from the\
  \ Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-flood-extent-in-punjab-province-pakistan-10-july-2025]"
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
    description: Population potentially exposed or living in close proximity to flood-affected
      areas based on WorldPop data
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
  description: "Sentinel-1 SAR imagery from 10 July 2025 was analyzed by UNOSAT analysts\
    \ through visual interpretation and multi-temporal change detection to delineate\
    \ flood extent. The resulting inundation polygon (4,200 km\xB2) was intersected\
    \ with WorldPop gridded population data to estimate 3.3 million people exposed\
    \ to flooding in Punjab Province, Pakistan."
  sources:
  - id: source_1
    license: null
    name: Sentinel-1 SAR imagery
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
- href: https://data.humdata.org/dataset/satellite-detected-flood-extent-in-punjab-province-pakistan-10-july-2025
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
  description: Satellite-detected Flood Extent in Punjab Province, Pakistan - 10 July
    2025 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4147/FL20250630PAK_gdb.zip
  format: Geodatabase
  id: resource_bbb39c58
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20250630PAK_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite-detected Flood Extent in Punjab Province, Pakistan - 10 July
    2025 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4147/FL20250630PAK_SHP.zip
  format: null
  id: resource_a0073f8f
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20250630PAK_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite-detected Flood Extent in Punjab Province, Pakistan - 10 July
    2025 (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/4147/UNOSAT_FL20250630PAK_PopulationExposed_PunJab_10July2025.xlsx
  format: null
  id: resource_b19213aa
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_FL20250630PAK_PopulationExposed_PunJab_10July2025.xlsx
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-pak_unosat_detectedfloodextentpunjab_20250715
spatial:
  bbox: null
  centroid: null
  countries:
  - PAK
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-07-15'
temporal_resolution: null
title: Satellite-detected Flood Extent in Punjab Province, Pakistan - 10 July 2025
version: null
vulnerability: null
---
