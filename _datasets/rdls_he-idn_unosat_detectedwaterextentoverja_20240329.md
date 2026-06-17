---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/satellite-detected-water-extent-over-jawa-tengah-province-indonesia-as-of-27-march-2024
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UNOSAT Population Exposure Analysis
    url: https://data.humdata.org/dataset/satellite-detected-water-extent-over-jawa-tengah-province-indonesia-as-of-27-march-2024
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-over-jawa-tengah-province-indonesia-as-of-27-march-2024
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-over-jawa-tengah-province-indonesia-as-of-27-march-2024
dataset_id: rdls_he-idn_unosat_detectedwaterextentoverja_20240329
description: "UNOSAT code: EQ20240326IDN, GDACS ID: 1420595 This map illustrates satellite-detected\
  \ surface waters in Jawa Tengah Province, Indonesia, as observed from a Sentinel-1\
  \ image acquired on 27 March 2024 at 22:17 UTC. and a Fucheng-1 image acquired on\
  \ 27 March 2024 at 14:51 UTC. Within the analysed area of about 4,400 km\xB2, a\
  \ total of about 260 km\xB2 of land appears to be flooded, receding of about 60\
  \ km\xB2 compared to 19 March 2024. This is a preliminary analysis and has not yet\
  \ been validated in the field. Please send ground feedback to the United Nations\
  \ Satellite Centre (UNOSAT). Important note: Flood analysis from radar images may\
  \ underestimate the presence of standing waters in built-up areas and densely vegetated\
  \ areas due to backscattering properties of the radar signal.. [Source: This metadata\
  \ record was automatically extracted from the Humanitarian Data Exchange (HDX);\
  \ Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extent-over-jawa-tengah-province-indonesia-as-of-27-march-2024]"
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
    description: Population exposed to flooding in Jawa Tengah Province based on satellite-detected
      water extent
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
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: Sentinel-1 SAR and Fucheng-1 optical satellite imagery acquired on
    27 March 2024 were analyzed by UNOSAT to detect surface water extent through multi-temporal
    comparison with baseline imagery from 19 March 2024. Water classification was
    performed using automated and manual interpretation of satellite data, with confidence
    levels and field validation flags recorded. Population exposure was calculated
    by intersecting the detected water extent polygons with gridded population data.
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
    name: UNOSAT Population Exposure Analysis
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/satellite-detected-water-extent-over-jawa-tengah-province-indonesia-as-of-27-march-2024
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
  description: Satellite detected water extent over Jawa Tengah Province, Indonesia
    as of 27 March 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3814/FL20240326IDN_gdb.zip
  format: Geodatabase
  id: resource_9be629c1
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240326IDN_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent over Jawa Tengah Province, Indonesia
    as of 27 March 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3814/FL20240326IDN_SHP.zip
  format: null
  id: resource_907b8f64
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240326IDN_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent over Jawa Tengah Province, Indonesia
    as of 27 March 2024 (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3814/UNOSAT_PopuationExposure_EQ20240326IDN_27March2024.xlsx
  format: null
  id: resource_d2c7869e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_PopuationExposure_EQ20240326IDN_27March2024.xlsx
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-idn_unosat_detectedwaterextentoverja_20240329
spatial:
  bbox: null
  centroid: null
  countries:
  - IDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-03-29'
temporal_resolution: null
title: Satellite detected water extent over Jawa Tengah Province, Indonesia as of
  27 March 2024
version: null
vulnerability: null
---
