---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-30-october-and-03-november-2022-over-chad
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-30-october-and-03-november-2022-over-chad
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-30-october-and-03-november-2022-over-chad
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-30-october-and-03-november-2022-over-chad
dataset_id: rdls_he-tcd_unosat_detectedwaterextentsbetwe_20221104
description: "UNOSAT code FL20221019TCD This map illustrates cumulative satellite-detected\
  \ water using VIIRS in Chad between 30 October to 03 November 2022 compared with\
  \ the period from 14 to 18 October 2022. Within the cloud free analysed areas of\
  \ about 1,200,000 km\xB2, a total of about 18,000 km\xB2 of land appears to be affected.\
  \ Water extent appears to have decreased of about 6,300 km\xB2 since the period\
  \ between 14 to 18 October 2022. Based on Worldpop population data and the maximal\
  \ flood water extent ~1 million people are potentially exposed or living close to\
  \ flooded areas amongst the 16.5 million people living in the analysed zone. This\
  \ is a preliminary analysis and has not yet been validated in the field. Please\
  \ send ground feedback to the United Nations Satellite Centre (UNOSAT).. [Source:\
  \ This metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extents-between-30-october-and-03-november-2022-over-chad]"
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
      estimated at ~1 million people based on WorldPop data and maximal flood extent
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
  description: "UNOSAT analysts compared VIIRS satellite imagery from 30 October to\
    \ 3 November 2022 with baseline imagery from 14 to 18 October 2022 to detect cumulative\
    \ water extent changes across cloud-free areas (~1,200,000 km\xB2). Population\
    \ exposure was estimated by overlaying the maximal flood water extent with WorldPop\
    \ gridded population data to identify ~1 million people potentially affected or\
    \ living near flooded areas."
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
- href: https://data.humdata.org/dataset/satellite-detected-water-extents-between-30-october-and-03-november-2022-over-chad
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
  description: Satellite detected water extents between 30 October and 03 November
    2022 over Chad (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3439/FL20221019TCD_gdb.zip
  format: Geodatabase
  id: resource_e1dc4beb
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20221019TCD_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents between 30 October and 03 November
    2022 over Chad (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3439/FL20221019TCD_SHP.zip
  format: null
  id: resource_f6c051f0
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20221019TCD_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents between 30 October and 03 November
    2022 over Chad (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3439/UNOSAT_A3_Natural_Landscape_FL20221019TCD_30Oct_03Nov2022.xlsx
  format: null
  id: resource_47dd74b8
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_A3_Natural_Landscape_FL20221019TCD_30Oct_03Nov2022.xlsx
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-tcd_unosat_detectedwaterextentsbetwe_20221104
spatial:
  bbox: null
  centroid: null
  countries:
  - TCD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-11-04'
temporal_resolution: null
title: Satellite detected water extents between 30 October and 03 November 2022 over
  Chad
version: null
vulnerability: null
---
