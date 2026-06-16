---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-2 satellite imagery
    url: https://data.humdata.org/dataset/water-extent-between-30-october-2022-and-31-october-2018-in-hadjer-lamis-lac-regions-chad
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop population data
    url: https://data.humdata.org/dataset/water-extent-between-30-october-2022-and-31-october-2018-in-hadjer-lamis-lac-regions-chad
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-between-30-october-2022-and-31-october-2018-in-hadjer-lamis-lac-regions-chad
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-between-30-october-2022-and-31-october-2018-in-hadjer-lamis-lac-regions-chad
dataset_id: rdls_he-tcd_unosat_detectedwaterextentbetwee_20221103
description: 'UNOSAT code FL20221019TCD This map illustrates satellite-detected surface
  waters in Hadjer-Lamis & Lac Regions, Chad as observed from a Sentinel-2 acquired
  on 30 October 2022 at 10:37 local time. Within the cloud free analyzed area of about
  17,000 km2, the surface waters appears to have increased of about 700 km2 since
  31 October 2018. Based on Worldpop population data and the detected surface waters,
  the potentially exposed population is mainly located in Mamdi Department with ~28,000
  people, Haraze-Al-Biar Department with ~9,700 people and Wayi department with ~9,300
  people. This is a preliminary analysis and has not yet been validated in the field.
  Please send ground feedback to United Nations Satellite Centre (UNOSAT).. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-between-30-october-2022-and-31-october-2018-in-hadjer-lamis-lac-regions-chad]'
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
    description: Potentially exposed population in Mamdi, Haraze-Al-Biar, and Wayi
      departments based on WorldPop data and detected water extent
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
  description: UNOSAT analysts compared Sentinel-2 satellite imagery from 30 October
    2022 with historical imagery from 31 October 2018 to detect changes in surface
    water extent across a 17,000 km2 study area in Chad. Detected water polygons were
    intersected with WorldPop population data to estimate potentially exposed populations
    by administrative department.
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
- href: https://data.humdata.org/dataset/water-extent-between-30-october-2022-and-31-october-2018-in-hadjer-lamis-lac-regions-chad
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
  description: Satellite detected water extent between 30 October 2022 and 31 October
    2018 in Hadjer-Lamis & Lac Regions, Chad (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3434/FL20221019TCD_gdb.zip
  format: Geodatabase
  id: resource_65aa3c60
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
  description: Satellite detected water extent between 30 October 2022 and 31 October
    2018 in Hadjer-Lamis & Lac Regions, Chad (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3434/FL20221019TCD_SHP.zip
  format: null
  id: resource_61af7c2d
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
  description: Satellite detected water extent between 30 October 2022 and 31 October
    2018 in Hadjer-Lamis & Lac Regions, Chad (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3434/UNOSAT_Population_Exposure_FL20221019TCD_HadjerLamisLacRegions_Chad_30Oct2022.xlsx
  format: null
  id: resource_32ea21f3
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_Population_Exposure_FL20221019TCD_HadjerLamisLacRegions_Chad_30Oct2022.xlsx
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-tcd_unosat_detectedwaterextentbetwee_20221103
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
  start: '2022-11-03'
temporal_resolution: null
title: Satellite detected water extent between 30 October 2022 and 31 October 2018
  in Hadjer-Lamis & Lac Regions, Chad
version: null
vulnerability: null
---
