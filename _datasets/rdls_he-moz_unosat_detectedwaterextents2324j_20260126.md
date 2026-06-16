---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-1 satellite imagery
    url: https://data.humdata.org/dataset/water-extents-from-23-to-24-january-2026-in-gaza-maputo-and-maputo-city-provinces-mozambiq
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop spatial demographic data
    url: https://data.humdata.org/dataset/water-extents-from-23-to-24-january-2026-in-gaza-maputo-and-maputo-city-provinces-mozambiq
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-from-23-to-24-january-2026-in-gaza-maputo-and-maputo-city-provinces-mozambiq
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-from-23-to-24-january-2026-in-gaza-maputo-and-maputo-city-provinces-mozambiq
dataset_id: rdls_he-moz_unosat_detectedwaterextents2324j_20260126
description: "UNOSAT code: FL20251229MOZ, GDACS ID: 1103694 This map illustrates cumulative\
  \ satellite-detected water extent derived from Sentinel-1 imagery acquired on 23\
  \ and 24 January 2026. Within the analysed area of approximately 64,000 km\xB2,\
  \ an estimated 4,800 km\xB2 of land appears to be affected by floodwaters. Based\
  \ on WorldPop spatial demographic data, approximately 252,000 people are exposed\
  \ to or living near the flooded areas. This is a preliminary analysis and has not\
  \ yet been validated in the field. Please send ground feedback to the United Nations\
  \ Satellite Centre (UNOSAT). Important note: Flood analysis from radar images may\
  \ underestimate the presence of standing waters in built-up areas and densely vegetated\
  \ areas due to the backscattering properties of the radar signal.. [Source: This\
  \ metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/water-extents-from-23-to-24-january-2026-in-gaza-maputo-and-maputo-city-provinces-mozambiq]"
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
    description: Population exposed to or living near flooded areas derived from WorldPop
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
  description: "Sentinel-1 SAR imagery from 23-24 January 2026 was analyzed by UNOSAT\
    \ to detect cumulative water extent through multi-temporal image comparison. WorldPop\
    \ gridded population data was overlaid on the detected flood extent to estimate\
    \ population exposure. The analysis covers approximately 64,000 km\xB2 across\
    \ Gaza, Maputo and Maputo City Provinces, Mozambique."
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
    name: WorldPop spatial demographic data
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/water-extents-from-23-to-24-january-2026-in-gaza-maputo-and-maputo-city-provinces-mozambiq
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
  description: Satellite detected water extents from 23 to 24 January 2026 in Gaza,
    Maputo and Maputo City Provinces, Mozambique (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4231/FL20251229MOZ_GDB.zip
  format: Geodatabase
  id: resource_44db7493
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20251229MOZ_GDB.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents from 23 to 24 January 2026 in Gaza,
    Maputo and Maputo City Provinces, Mozambique (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4231/FL20251231MOZ_SHP.zip
  format: null
  id: resource_51410e18
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20251231MOZ_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents from 23 to 24 January 2026 in Gaza,
    Maputo and Maputo City Provinces, Mozambique (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/4231/UNOSAT_PopulationExposure_FL20251229_Maputo_Mozambique_24JAN2026.xlsx
  format: null
  id: resource_fb9fb3de
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_PopulationExposure_FL20251229_Maputo_Mozambique_24JAN2026.xlsx
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-moz_unosat_detectedwaterextents2324j_20260126
spatial:
  bbox: null
  centroid: null
  countries:
  - MOZ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2026-01-26'
temporal_resolution: null
title: Satellite detected water extents from 23 to 24 January 2026 in Gaza, Maputo
  and Maputo City Provinces, Mozambique
version: null
vulnerability: null
---
