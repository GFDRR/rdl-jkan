---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-2 satellite imagery
    url: https://data.humdata.org/dataset/water-extents-in-swat-district-khyber-pakhtunkhwa-province-pakistan-as-of-20-august-2025
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop population data
    url: https://data.humdata.org/dataset/water-extents-in-swat-district-khyber-pakhtunkhwa-province-pakistan-as-of-20-august-2025
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-in-swat-district-khyber-pakhtunkhwa-province-pakistan-as-of-20-august-2025
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-in-swat-district-khyber-pakhtunkhwa-province-pakistan-as-of-20-august-2025
dataset_id: rdls_he-pak_unosat_detectedwaterextentsswatd_20250822
description: "UNOSAT code: FL20250818PAK This map illustrates the satellite detected\
  \ water extent in Swat District, Khyber Pakhtunkhwa Province, Pakistan as observed\
  \ from a Sentinel-2 satellite image acquired on 20 August 2025 at 13:35 local time\
  \ (08:35 UTC). Within the analyzed area of approximately 340 km\xB2, about 4 km\xB2\
  \ of land appears to be affected by floodwaters. Based on WorldPop population data\
  \ and the flood extent, approximately 134,500 people are potentially exposed or\
  \ living close to the flooded areas. additional. In addition, UNOSAT identified\
  \ approximately 3,860 exposed buildings and about 30 km of affected roads. This\
  \ is a preliminary analysis and has not yet been validated in the field. Please\
  \ send ground feedback to the United Nations Satellite Centre (UNOSAT).. [Source:\
  \ This metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/water-extents-in-swat-district-khyber-pakhtunkhwa-province-pakistan-as-of-20-august-2025]"
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
      estimated at approximately 134,500 people based on WorldPop data
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
    description: Building stock exposed to flood extent, with approximately 3,860
      buildings identified in the affected area
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_2
  metrics:
  - dimension: structure
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
  description: "UNOSAT analysts reviewed Sentinel-2 satellite imagery acquired on\
    \ 20 August 2025 and performed visual change detection to identify water extent\
    \ boundaries in Swat District. The delineated flood extent (approximately 4 km\xB2\
    ) was intersected with WorldPop population grids and building footprint data to\
    \ estimate exposure of approximately 134,500 people and 3,860 buildings. The resulting\
    \ geodatabase and shapefile products provide observed hazard geometry and derived\
    \ exposure metrics for post-event flood impact assessment."
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
- href: https://data.humdata.org/dataset/water-extents-in-swat-district-khyber-pakhtunkhwa-province-pakistan-as-of-20-august-2025
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
  description: Satellite detected water extents in Swat District, Khyber Pakhtunkhwa
    Province, Pakistan as of 20 August 2025 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4177/FL20250818PAK_gdb.zip
  format: Geodatabase
  id: resource_efb200f0
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20250818PAK_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents in Swat District, Khyber Pakhtunkhwa
    Province, Pakistan as of 20 August 2025 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4177/FL20250818PAK_SHP.zip
  format: null
  id: resource_087e22e9
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20250818PAK_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-pak_unosat_detectedwaterextentsswatd_20250822
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
  start: '2025-08-22'
temporal_resolution: null
title: Satellite detected water extents in Swat District, Khyber Pakhtunkhwa Province,
  Pakistan as of 20 August 2025
version: null
vulnerability: null
---
