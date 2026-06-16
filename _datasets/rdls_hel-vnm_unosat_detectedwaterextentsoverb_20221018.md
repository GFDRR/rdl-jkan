---
attributions:
- entity:
    affiliation: null
    email: null
    name: Worldpop
    url: https://data.humdata.org/dataset/water-extents-over-binh-dinh-da-nang-city-phu-yen-quang-nam-quang-ngai-thua-thien-hue-prov
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Sentinel-1
    url: https://data.humdata.org/dataset/water-extents-over-binh-dinh-da-nang-city-phu-yen-quang-nam-quang-ngai-thua-thien-hue-prov
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-over-binh-dinh-da-nang-city-phu-yen-quang-nam-quang-ngai-thua-thien-hue-prov
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-over-binh-dinh-da-nang-city-phu-yen-quang-nam-quang-ngai-thua-thien-hue-prov
dataset_id: rdls_hel-vnm_unosat_detectedwaterextentsoverb_20221018
description: "UNOSAT code FL20221014VNM, GDACS Id: 1101698 This map illustrates satellite-detected\
  \ surface waters in Binh Dinh, Da Nang City, Phu Yen, Quang Nam, Quang Ngai, Thua\
  \ Thien Hue Provinces, Viet Nam as observed from a Sentinel-1 images acquired on\
  \ 15 October 2022 at 17:56 local time. Within the extent of this map of 32,000 km\xB2\
  , about 500 km\xB2 of lands appear to be flooded. Based on Worldpop population data\
  \ and the detected surface waters in the map extent, about 300,000 people are potentially\
  \ exposed or living close to flooded areas. This is a preliminary analysis and has\
  \ not yet been validated in the field. Please send ground feedback to United Nations\
  \ Satellite Centre (UNOSAT). Important note: Flood analysis from radar images may\
  \ underestimate the presence of standing waters in built-up areas and densely vegetated\
  \ areas due to backscattering properties of the radar signal.. [Source: This metadata\
  \ record was automatically extracted from the Humanitarian Data Exchange (HDX);\
  \ Original dataset: https://data.humdata.org/dataset/water-extents-over-binh-dinh-da-nang-city-phu-yen-quang-nam-quang-ngai-thua-thien-hue-prov]"
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
    description: Population potentially exposed to flooded areas derived from WorldPop
      population data
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
  description: "UNOSAT analysts processed Sentinel-1 SAR satellite imagery acquired\
    \ on 15 October 2022 to detect surface water extents through change detection\
    \ analysis. Detected flood polygons (500 km\xB2 total) were intersected with WorldPop\
    \ gridded population data to estimate approximately 300,000 people potentially\
    \ exposed to flooded areas across six central Vietnamese provinces."
  sources:
  - id: source_1
    license: null
    name: Worldpop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: Sentinel-1
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/water-extents-over-binh-dinh-da-nang-city-phu-yen-quang-nam-quang-ngai-thua-thien-hue-prov
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population potentially exposed or living close to satellite-detected
      flooded areas
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
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
  description: Satellite detected water extents over Binh Dinh, Da Nang city, Phu
    Yen, Quang Nam, Quang Ngai, Thua Thien Hue Provinces, Viet Nam as of 15 October
    2022 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3409/FL20221014VNM_gdb.zip
  format: Geodatabase
  id: resource_82f56446
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20221014VNM_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents over Binh Dinh, Da Nang city, Phu
    Yen, Quang Nam, Quang Ngai, Thua Thien Hue Provinces, Viet Nam as of 15 October
    2022 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3409/FL20221014VNM_SHP.zip
  format: null
  id: resource_ed7df0f3
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20221014VNM_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents over Binh Dinh, Da Nang city, Phu
    Yen, Quang Nam, Quang Ngai, Thua Thien Hue Provinces, Viet Nam as of 15 October
    2022 (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3409/Preliminary%20Satellite%20Derived%20Flood%20Evolution%20Assessment%2C%20Viet%20Nam-18%20October%202022.csv
  format: null
  id: resource_35b72ce4
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Preliminary Satellite Derived Flood Evolution Assessment, Viet Nam-18 October
    2022.csv
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-vnm_unosat_detectedwaterextentsoverb_20221018
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
  start: '2022-10-18'
temporal_resolution: null
title: Satellite detected water extents over Binh Dinh, Da Nang city, Phu Yen, Quang
  Nam, Quang Ngai, Thua Thien Hue Provinces, Viet Nam as of 15 October 2022
version: null
vulnerability: null
---
