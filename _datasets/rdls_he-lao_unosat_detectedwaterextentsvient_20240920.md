---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-1 SAR imagery
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-in-vientiane-capital-lao-pdr-as-of-18-september-2024
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop spatial demographic data
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-in-vientiane-capital-lao-pdr-as-of-18-september-2024
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-in-vientiane-capital-lao-pdr-as-of-18-september-2024
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-in-vientiane-capital-lao-pdr-as-of-18-september-2024
dataset_id: rdls_he-lao_unosat_detectedwaterextentsvient_20240920
description: "UNOSAT code: FL20240913LAO This map illustrates the floods using Sentinel-1\
  \ images acquired on 18 September 2024 at 06:00 local time. Within the analyzed\
  \ area of approximately 7,000 km\xB2, around 230 km\xB2 of land appears to be affected\
  \ by floodwaters. The extent of the flooding has increased by approximately 50 km\xB2\
  \ since the previous observation on 13 September 2024. Based on WorldPop spatial\
  \ demographic data, an estimated 26,000 people are currently exposed or residing\
  \ near the flooded areas. This is a preliminary analysis and has not yet been validated\
  \ in the field. Please send ground feedback to the United Nations Satellite Centre\
  \ (UNOSAT). Important note: Flood analysis from radar images may underestimate the\
  \ presence of standing waters in built-up areas and densely vegetated areas due\
  \ to the backscattering properties of the radar signal.. [Source: This metadata\
  \ record was automatically extracted from the Humanitarian Data Exchange (HDX);\
  \ Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extents-in-vientiane-capital-lao-pdr-as-of-18-september-2024]"
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
    description: Population exposed or residing near flooded areas, estimated at 26,000
      people using WorldPop spatial demographic data
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
  description: "Sentinel-1 SAR imagery from 18 September 2024 was analyzed by UNOSAT\
    \ to detect water surface extent through comparison with baseline imagery. The\
    \ resulting flood water polygon (230 km\xB2 affected area) was spatially intersected\
    \ with WorldPop gridded population data to estimate 26,000 people exposed to flooding\
    \ in Vientiane Capital. This represents a preliminary post-event empirical assessment\
    \ of flood hazard and population exposure."
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
    name: WorldPop spatial demographic data
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/satellite-detected-water-extents-in-vientiane-capital-lao-pdr-as-of-18-september-2024
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
  description: Satellite detected water extents in Vientiane Capital, Lao PDR as of
    18 September 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3976/FL20240913LAO_GDB.zip
  format: Geodatabase
  id: resource_6bfffe6a
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
  description: Satellite detected water extents in Vientiane Capital, Lao PDR as of
    18 September 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3976/FL20240913LAO_SHP.zip
  format: null
  id: resource_f17f7427
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
  description: Satellite detected water extents in Vientiane Capital, Lao PDR as of
    18 September 2024 (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3976/UNOSAT_PopulationExposureAnalysis_Flood_VIENTIANE_CAPITAL_LAOPDR_18SEP2024.xlsx
  format: null
  id: resource_47859cc3
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_PopulationExposureAnalysis_Flood_VIENTIANE_CAPITAL_LAOPDR_18SEP2024.xlsx
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-lao_unosat_detectedwaterextentsvient_20240920
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
title: Satellite detected water extents in Vientiane Capital, Lao PDR as of 18 September
  2024
version: null
vulnerability: null
---
