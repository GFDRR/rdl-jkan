---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-extent-between-01-august-2019-and-04-october-2021-along-lake-albert-in-d-r-of-the-co
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/water-extent-between-01-august-2019-and-04-october-2021-along-lake-albert-in-d-r-of-the-co
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-between-01-august-2019-and-04-october-2021-along-lake-albert-in-d-r-of-the-co
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-between-01-august-2019-and-04-october-2021-along-lake-albert-in-d-r-of-the-co
dataset_id: rdls_he-cod_unosat_detectedwaterextentbetwee_20211008
description: "UNOSAT code: FL20211008COD This map illustrates satellite-detected surface\
  \ waters in Ituri Province as observed from a Sentinel-2 image acquired on 04 October\
  \ 2021. Within 5 km around Lake Albert, about 40 km2 of lands appear to be flooded.\
  \ The water extent appears to have increased since August 2019 and based on Worldpop\
  \ population data and the detected surface waters in the analyzed area, the potentially\
  \ exposed population is mainly located in the Zone de Sant\xE9 of Nyarambe with\
  \ ~5,200 people, Gethy with ~ 3,300 people and Tchomia with ~1,550 people. This\
  \ is a preliminary analysis and has not yet been validated in the field. Please\
  \ send ground feedback to the United Nations Satellite Centre (UNOSAT). [Source:\
  \ This metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-between-01-august-2019-and-04-october-2021-along-lake-albert-in-d-r-of-the-co]"
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
    description: "Potentially exposed population in Zones de Sant\xE9 of Nyarambe,\
      \ Gethy, and Tchomia based on WorldPop data within 5 km of Lake Albert"
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts compared Sentinel-2 satellite imagery acquired on 04
    October 2021 with baseline imagery from August 2019 to detect changes in surface
    water extent around Lake Albert. Flooded areas were delineated and intersected
    with WorldPop population data to estimate potentially exposed populations in affected
    health zones.
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
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/water-extent-between-01-august-2019-and-04-october-2021-along-lake-albert-in-d-r-of-the-co
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
  description: Satellite detected water extent between 01 August 2019 and 04 October
    2021 along Lake Albert in D.R. of the Congo (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/CD/FL20211008COD/FL20211008COD_gdb.zip
  format: Geodatabase
  id: resource_055afa81
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20211008COD_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent between 01 August 2019 and 04 October
    2021 along Lake Albert in D.R. of the Congo (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/CD/FL20211008COD/FL20211008COD_SHP.zip
  format: null
  id: resource_c2cc0885
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20211008COD_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-cod_unosat_detectedwaterextentbetwee_20211008
spatial:
  bbox: null
  centroid: null
  countries:
  - COD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2021-10-08'
temporal_resolution: null
title: Satellite detected water extent between 01 August 2019 and 04 October 2021
  along Lake Albert in D.R. of the Congo
version: null
vulnerability: null
---
