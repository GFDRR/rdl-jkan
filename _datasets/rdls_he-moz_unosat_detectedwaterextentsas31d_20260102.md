---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-1 satellite imagery
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-as-of-31-december-2025-in-sofala-province-mozambique
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop spatial demographic data
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-as-of-31-december-2025-in-sofala-province-mozambique
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-as-of-31-december-2025-in-sofala-province-mozambique
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-as-of-31-december-2025-in-sofala-province-mozambique
dataset_id: rdls_he-moz_unosat_detectedwaterextentsas31d_20260102
description: "UNOSAT code: FL20251229MOZ This map illustrates the flood extent derived\
  \ from Sentinel-1 imagery acquired on 31 December 2025, using an automated machine-learning-based\
  \ analysis. Within the analysed area of approximately 32,000 km\xB2, an estimated\
  \ 930 km\xB2 of land appears to be affected by floodwaters. Based on WorldPop spatial\
  \ demographic data, approximately 4,200 people are exposed to or living in close\
  \ to the flooded areas. This is a preliminary analysis and has not yet been validated\
  \ in the field. Please send ground feedback to the United Nations Satellite Centre\
  \ (UNOSAT). Important note: Flood analysis from radar images may underestimate the\
  \ presence of standing waters in built-up areas and densely vegetated areas due\
  \ to the backscattering properties of the radar signal.. [Source: This metadata\
  \ record was automatically extracted from the Humanitarian Data Exchange (HDX);\
  \ Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extents-as-of-31-december-2025-in-sofala-province-mozambique]"
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
    description: Population exposed to or living in close proximity to flooded areas,
      derived from WorldPop spatial demographic data
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
license: CC-BY-SA-4.0
lineage:
  description: "Sentinel-1 SAR imagery acquired on 31 December 2025 was processed\
    \ using automated machine-learning algorithms to detect water surface extents.\
    \ The resulting flood extent map (930 km\xB2) was intersected with WorldPop gridded\
    \ population data to estimate approximately 4,200 people exposed to or living\
    \ near flooded areas in Sofala Province. This preliminary post-event analysis\
    \ has not been field-validated."
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
- href: https://data.humdata.org/dataset/satellite-detected-water-extents-as-of-31-december-2025-in-sofala-province-mozambique
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
  description: Satellite detected water extents as of 31 December 2025 in Sofala Province,
    Mozambique (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4228/FL20251229MOZ_GDB.zip
  format: Geodatabase
  id: resource_e72c5ca6
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
  description: Satellite detected water extents as of 31 December 2025 in Sofala Province,
    Mozambique (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4228/FL20251231MOZ_SHP.zip
  format: null
  id: resource_5c88a784
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
  description: Satellite detected water extents as of 31 December 2025 in Sofala Province,
    Mozambique (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/4228/UNOSAT_PopulationExposure_FL20251229_Sofala_Mozambique_31DEC2025_V2.xlsx
  format: null
  id: resource_565cf220
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_PopulationExposure_FL20251229_Sofala_Mozambique_31DEC2025_V2.xlsx
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-moz_unosat_detectedwaterextentsas31d_20260102
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
  start: '2026-01-02'
temporal_resolution: null
title: Satellite detected water extents as of 31 December 2025 in Sofala Province,
  Mozambique
version: null
vulnerability: null
---
