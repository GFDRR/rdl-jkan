---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-2 satellite imagery
    url: https://data.humdata.org/dataset/water-extent-over-lumbini-and-sudurpaschim-provinces-nepal-as-of-25-30-october-2022
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop population data
    url: https://data.humdata.org/dataset/water-extent-over-lumbini-and-sudurpaschim-provinces-nepal-as-of-25-30-october-2022
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-over-lumbini-and-sudurpaschim-provinces-nepal-as-of-25-30-october-2022
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-over-lumbini-and-sudurpaschim-provinces-nepal-as-of-25-30-october-2022
dataset_id: rdls_hel-npl_unosat_detectedwaterextentoverlu_20221118
description: "UNOSAT code FL20221117NPL This map illustrates satellite-detected surface\
  \ waters in Sudurpaschim and Lumbini Provinces, Nepal as observed from Sentinel-2\
  \ images acquired on 25 & 30 October 2022 (Cumulative). Within the analyzed area\
  \ of about 5,600 km\xB2, a combined 52 km\xB2 of lands appear to be flooded on the\
  \ 25th and the 30th of October 2022. Water extent appears to have decreased of about\
  \ 37 km\xB2 since the 15th October 2022. Based on Worldpop population data and the\
  \ detected surface waters, about 23,000 people are potentially exposed or living\
  \ close to flooded areas, of which 10,000 are located In Janaki, Tikapur, Geruwa,\
  \ Rajapur, Thakurbaba & Madhuwan Palikas. This is a preliminary analysis and has\
  \ not yet been validated in the field. Please send ground feedback to the United\
  \ Nations Satellite Centre (UNOSAT).. [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-over-lumbini-and-sudurpaschim-provinces-nepal-as-of-25-30-october-2022]"
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
    description: Population potentially exposed or living close to flooded areas based
      on WorldPop data
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
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts reviewed and compared Sentinel-2 satellite images acquired
    on 25 and 30 October 2022 to detect surface water extent through visual interpretation
    and change detection methods. Detected water polygons were intersected with WorldPop
    gridded population data to estimate approximately 23,000 people potentially exposed
    to flooded areas in Sudurpaschim and Lumbini Provinces, Nepal.
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
- href: https://data.humdata.org/dataset/water-extent-over-lumbini-and-sudurpaschim-provinces-nepal-as-of-25-30-october-2022
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by detected flood water extent in Sudurpaschim
      and Lumbini Provinces
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
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
  description: Satellite detected water extent over Lumbini and Sudurpaschim Provinces,
    Nepal as of 25 & 30 October 2022 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3449/FL20221117NPL_gdb.zip
  format: Geodatabase
  id: resource_3f3c9d1e
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
    Nepal as of 25 & 30 October 2022 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3449/FL20221117NPL_SHP.zip
  format: null
  id: resource_0cafe1b5
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
    Nepal as of 25 & 30 October 2022 (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3449/UNOSAT_Population_Exposure_FL20221117NPL_Bardiya_Kailali_BankeDistricts_Nepal_25_30Oct2022.xlsx
  format: null
  id: resource_71d32c0f
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_Population_Exposure_FL20221117NPL_Bardiya_Kailali_BankeDistricts_Nepal_25_30Oct2022.xlsx
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-npl_unosat_detectedwaterextentoverlu_20221118
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
  start: '2022-11-18'
temporal_resolution: null
title: Satellite detected water extent over Lumbini and Sudurpaschim Provinces, Nepal
  as of 25 & 30 October 2022
version: null
vulnerability: null
---
