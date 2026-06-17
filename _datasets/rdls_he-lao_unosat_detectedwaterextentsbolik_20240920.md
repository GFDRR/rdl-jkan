---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-1 satellite imagery
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-in-bolikhamzai-province-lao-pdr-as-of-18-september-2024
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop spatial demographic data
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-in-bolikhamzai-province-lao-pdr-as-of-18-september-2024
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-in-bolikhamzai-province-lao-pdr-as-of-18-september-2024
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-in-bolikhamzai-province-lao-pdr-as-of-18-september-2024
dataset_id: rdls_he-lao_unosat_detectedwaterextentsbolik_20240920
description: "UNOSAT code: FL20240913LAO This map illustrates the floods detected\
  \ using Sentinel-1 images acquired on 18 September 2024 at 06:00 local time in Bolikhamzai\
  \ Province. Within the analysed area of approximately 16,000 km\xB2, about 270 km\xB2\
  \ of land appears to be affected by floodwaters. The extent of the flooding has\
  \ increased by approximately 230 km\xB2 since the previous observation on 6 September\
  \ 2024. Based on WorldPop spatial demographic data, an estimated 15,500 people are\
  \ currently exposed to or residing near the flooded areas. Please note that this\
  \ is a preliminary analysis and has not been validated in the field. We welcome\
  \ any ground feedback that can be provided to the United Nations Satellite Centre\
  \ (UNOSAT).. [Source: This metadata record was automatically extracted from the\
  \ Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extents-in-bolikhamzai-province-lao-pdr-as-of-18-september-2024]"
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
    description: Population exposed to or residing near flooded areas estimated from
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
  description: "UNOSAT analysts processed Sentinel-1 SAR imagery acquired on 18 September\
    \ 2024 to detect water extents through comparison with baseline imagery from 6\
    \ September 2024, identifying approximately 270 km\xB2 of flooded area. Population\
    \ exposure was estimated by overlaying the detected flood extent with WorldPop\
    \ spatial demographic data to quantify residents in affected areas."
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
- href: https://data.humdata.org/dataset/satellite-detected-water-extents-in-bolikhamzai-province-lao-pdr-as-of-18-september-2024
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
  description: Satellite detected water extents in Bolikhamzai Province, Lao PDR as
    of 18 September 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3977/FL20240913LAO_GDB.zip
  format: Geodatabase
  id: resource_a82b39d5
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
  description: Satellite detected water extents in Bolikhamzai Province, Lao PDR as
    of 18 September 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3977/FL20240913LAO_SHP.zip
  format: null
  id: resource_f22d99ce
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240913LAO_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents in Bolikhamzai Province, Lao PDR as
    of 18 September 2024 (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3977/UNOSAT_PopulationExposureAnalysis_Flood_BOLIKHAMXAI_LAOPDR_18SEP2024.xlsx
  format: null
  id: resource_d8b1f60b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_PopulationExposureAnalysis_Flood_BOLIKHAMXAI_LAOPDR_18SEP2024.xlsx
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-lao_unosat_detectedwaterextentsbolik_20240920
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
  start: '2024-09-20'
temporal_resolution: null
title: Satellite detected water extents in Bolikhamzai Province, Lao PDR as of 18
  September 2024
version: null
vulnerability: null
---
