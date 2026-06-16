---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-2 satellite imagery
    url: https://data.humdata.org/dataset/water-extent-over-lumbini-and-sudurpaschim-provinces-nepal-as-of-15-october-2022
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop population data
    url: https://data.humdata.org/dataset/water-extent-over-lumbini-and-sudurpaschim-provinces-nepal-as-of-15-october-2022
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-over-lumbini-and-sudurpaschim-provinces-nepal-as-of-15-october-2022
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-over-lumbini-and-sudurpaschim-provinces-nepal-as-of-15-october-2022
dataset_id: rdls_he-npl_unosat_detectedwaterextentoverlu_20221117
description: "UNOSAT code FL20221117NPL This map illustrates satellite-detected surface\
  \ waters in Sudurpaschim and Lumbini Provinces, Nepal as observed from a Sentinel-2\
  \ image acquired on 15 October 2022. Within the total analyzed area of about 4,700\
  \ km\xB2, ~70 km\xB2 of lands appear to be flooded. Based on Worldpop population\
  \ data and the detected surface waters about 35,000 people are potentially exposed\
  \ or living close to flooded areas, of which 18,000 are located In Janaki, Tikapur,\
  \ Geruwa, Rajapur, Thakurbaba & Madhuwan Palikas. This is a preliminary analysis\
  \ and has not yet been validated in the field. Please send ground feedback to the\
  \ United Nations Satellite Centre (UNOSAT).. [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-over-lumbini-and-sudurpaschim-provinces-nepal-as-of-15-october-2022]"
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
      derived from WorldPop data intersected with detected water extent
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
  description: "UNOSAT analysts reviewed Sentinel-2 satellite imagery acquired on\
    \ 15 October 2022 and performed visual change detection to identify surface water\
    \ extent across ~4,700 km\xB2 in Sudurpaschim and Lumbini Provinces. Detected\
    \ water polygons were intersected with WorldPop gridded population data to estimate\
    \ potentially exposed population. The resulting dataset provides observed flood\
    \ extent and derived population exposure metrics for post-event impact assessment."
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
- href: https://data.humdata.org/dataset/water-extent-over-lumbini-and-sudurpaschim-provinces-nepal-as-of-15-october-2022
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
  description: Satellite detected water extent over Lumbini and Sudurpaschim Provinces,
    Nepal as of 15 October 2022 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3447/FL20221117NPL_gdb.zip
  format: Geodatabase
  id: resource_de2b1345
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20221117NPL_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent over Lumbini and Sudurpaschim Provinces,
    Nepal as of 15 October 2022 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3447/FL20221117NPL_SHP.zip
  format: null
  id: resource_0c1b8ec4
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20221117NPL_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent over Lumbini and Sudurpaschim Provinces,
    Nepal as of 15 October 2022 (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3447/UNOSAT_Population_Exposure_FL20221117NPL_Bardiya_KailaliDistricts_Nepal_15Oct2022.xlsx
  format: null
  id: resource_36ad0e82
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_Population_Exposure_FL20221117NPL_Bardiya_KailaliDistricts_Nepal_15Oct2022.xlsx
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-npl_unosat_detectedwaterextentoverlu_20221117
spatial:
  bbox: null
  centroid: null
  countries:
  - NPL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-11-17'
temporal_resolution: null
title: Satellite detected water extent over Lumbini and Sudurpaschim Provinces, Nepal
  as of 15 October 2022
version: null
vulnerability: null
---
