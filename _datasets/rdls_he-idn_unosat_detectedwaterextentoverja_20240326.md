---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/satellite-detected-water-extent-over-jawa-tengah-province-indonesia-as-of-19-mar-2024
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-over-jawa-tengah-province-indonesia-as-of-19-mar-2024
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-over-jawa-tengah-province-indonesia-as-of-19-mar-2024
dataset_id: rdls_he-idn_unosat_detectedwaterextentoverja_20240326
description: "UNOSAT code: EQ20240326IDN, GDACS ID: 1420595 This map illustrates satellite-detected\
  \ surface waters in Jawa Tengah Province, Indonesia, as observed from a Sentinel-1\
  \ image acquired on 19 March 2024 at 17:58 local time (10:58 UTC). Within the analysed\
  \ area of about 4,400 km\xB2, a total of about 320 km\xB2 of land appears to be\
  \ flooded, receding of about 70 km\xB2 compared to 15 March 2024. This is a preliminary\
  \ analysis and has not yet been validated in the field. Please send ground feedback\
  \ to the United Nations Satellite Centre (UNOSAT). Important note: Flood analysis\
  \ from radar images may underestimate the presence of standing waters in built-up\
  \ areas and densely vegetated areas due to backscattering properties of the radar\
  \ signal.. [Source: This metadata record was automatically extracted from the Humanitarian\
  \ Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extent-over-jawa-tengah-province-indonesia-as-of-19-mar-2024]"
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
    description: Population exposed to detected flood extent in Jawa Tengah Province
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
  description: "Sentinel-1 SAR imagery acquired on 19 March 2024 was analyzed by UNOSAT\
    \ to detect surface water extent through radar backscatter analysis. The flooded\
    \ area (320 km\xB2) was delineated by comparing satellite imagery and identifying\
    \ notable changes in water presence. Population exposure was derived by overlaying\
    \ the detected flood extent with population distribution data."
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/satellite-detected-water-extent-over-jawa-tengah-province-indonesia-as-of-19-mar-2024
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
    as of 19 Mar. 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3810/FL20240326IDN_gdb.zip
  format: Geodatabase
  id: resource_7591a6f4
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
    as of 19 Mar. 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3810/FL20240326IDN_SHP.zip
  format: null
  id: resource_1f2a4fd1
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
    as of 19 Mar. 2024 (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3810/PopulationExposure_FL20240326_Indonesia.xlsx
  format: null
  id: resource_800682bf
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PopulationExposure_FL20240326_Indonesia.xlsx
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-idn_unosat_detectedwaterextentoverja_20240326
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
  start: '2024-03-26'
temporal_resolution: null
title: Satellite detected water extent over Jawa Tengah Province, Indonesia as of
  19 Mar. 2024
version: null
vulnerability: null
---
