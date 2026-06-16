---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-2 satellite imagery
    url: https://data.humdata.org/dataset/water-extent-12-jan-2024-and-18-sep-2024-along-lake-albert-in-d-r-of-the-congo
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/water-extent-12-jan-2024-and-18-sep-2024-along-lake-albert-in-d-r-of-the-congo
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-12-jan-2024-and-18-sep-2024-along-lake-albert-in-d-r-of-the-congo
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-12-jan-2024-and-18-sep-2024-along-lake-albert-in-d-r-of-the-congo
dataset_id: rdls_hel-cod_unosat_detectedwaterextent12jan2_20241009
description: "UNOSAT code: FL20240919COD This map illustrates satellite-detected surface\
  \ waters in Ituri Province as observed from a Sentinel-2 image acquired on 18 Sep.\
  \ 2024. Within the analysed area, about 15km\xB2 of lands appear to be affected\
  \ with water increase. Based on Worldpop population data and the detected surface\
  \ waters, about 2,300 people are potentially exposed to the water increase. This\
  \ is a preliminary analysis and has not yet been validated in the field. Please\
  \ send ground feedback to the United Nations Satellite Centre (UNOSAT).. [Source:\
  \ This metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-12-jan-2024-and-18-sep-2024-along-lake-albert-in-d-r-of-the-congo]"
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
    description: Population potentially exposed to water increase derived from WorldPop
      data
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
  description: "UNOSAT analysts compared Sentinel-2 satellite imagery from 12 January\
    \ 2024 and 18 September 2024 to detect surface water extent changes in Ituri Province,\
    \ identifying approximately 15 km\xB2 of water increase. Population exposure was\
    \ estimated by overlaying detected water extent with WorldPop gridded population\
    \ data, yielding approximately 2,300 potentially exposed people. This is a preliminary\
    \ empirical assessment not yet validated in the field."
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
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/water-extent-12-jan-2024-and-18-sep-2024-along-lake-albert-in-d-r-of-the-congo
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population potentially exposed to detected water extent increase
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
  description: Satellite detected water extent 12 Jan. 2024 and 18 Sep. 2024 along
    Lake Albert in D.R. of the Congo (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3999/FL20240919COD_gdb.zip
  format: Geodatabase
  id: resource_c040b537
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240919COD_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent 12 Jan. 2024 and 18 Sep. 2024 along
    Lake Albert in D.R. of the Congo (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3999/FL20240919COD_SHP.zip
  format: null
  id: resource_2e5ff96a
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240919COD_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-cod_unosat_detectedwaterextent12jan2_20241009
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
  start: '2024-10-09'
temporal_resolution: null
title: Satellite detected water extent 12 Jan. 2024 and 18 Sep. 2024 along Lake Albert
  in D.R. of the Congo
version: null
vulnerability: null
---
