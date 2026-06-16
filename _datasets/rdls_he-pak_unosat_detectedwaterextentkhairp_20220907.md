---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-2 satellite imagery
    url: https://data.humdata.org/dataset/water-extent-in-khairpur-nathan-shah-town-sindh-province-pakistan-as-of-31-august-2022
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop population data
    url: https://data.humdata.org/dataset/water-extent-in-khairpur-nathan-shah-town-sindh-province-pakistan-as-of-31-august-2022
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-khairpur-nathan-shah-town-sindh-province-pakistan-as-of-31-august-2022
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-khairpur-nathan-shah-town-sindh-province-pakistan-as-of-31-august-2022
dataset_id: rdls_he-pak_unosat_detectedwaterextentkhairp_20220907
description: 'UNOSAT code FL20220808PAK, GDACS Id: 1101522 This map illustrates satellite-detected
  surface waters in Sindh Province, Pakistan as observed from a Sentinel-2 image acquired
  on 31 August 2022 at 10:56 local time. Khairpur Nathan Shah town appears to be surrounded
  by flood waters. Within the extent of this map of 1,300 km2, about 845 km2 of lands
  appear to be flooded. Based on Worldpop population data and the detected surface
  waters in the map extent, about 440,000 people are potentially exposed or living
  close to flooded areas. This is a preliminary analysis and has not yet been validated
  in the field. Please send ground feedback to United Nations Satellite Centre (UNOSAT)..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-in-khairpur-nathan-shah-town-sindh-province-pakistan-as-of-31-august-2022]'
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
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "UNOSAT analysts reviewed Sentinel-2 satellite imagery acquired on\
    \ 31 August 2022 and performed visual change detection to delineate surface water\
    \ extent across 1,300 km\xB2 in Khairpur Nathan Shah Town. Detected flood polygons\
    \ (845 km\xB2) were intersected with WorldPop gridded population data to estimate\
    \ approximately 440,000 people potentially exposed to flooded areas."
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
- href: https://data.humdata.org/dataset/water-extent-in-khairpur-nathan-shah-town-sindh-province-pakistan-as-of-31-august-2022
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
  description: Satellite detected water extent in Khairpur Nathan Shah Town, Sindh
    Province, Pakistan as of 31 August 2022 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3349/FL20220808PAK_gdb.zip
  format: Geodatabase
  id: resource_b1ee7e6c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20220808PAK_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent in Khairpur Nathan Shah Town, Sindh
    Province, Pakistan as of 31 August 2022 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3349/FL20220808PAK_SHP.zip
  format: null
  id: resource_17c917f1
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20220808PAK_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent in Khairpur Nathan Shah Town, Sindh
    Province, Pakistan as of 31 August 2022 (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3349/UNOSAT_Population_Exposure_FL20220808PAK_31Aug2022_Sindh.xlsx
  format: null
  id: resource_582d3245
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_Population_Exposure_FL20220808PAK_31Aug2022_Sindh.xlsx
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-pak_unosat_detectedwaterextentkhairp_20220907
spatial:
  bbox: null
  centroid: null
  countries:
  - PAK
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-09-07'
temporal_resolution: null
title: Satellite detected water extent in Khairpur Nathan Shah Town, Sindh Province,
  Pakistan as of 31 August 2022
version: null
vulnerability: null
---
