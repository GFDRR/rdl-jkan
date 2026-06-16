---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-1 (ESA Copernicus)
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-28-august-4-september-2024-in-bangladesh
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-28-august-4-september-2024-in-bangladesh
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-28-august-4-september-2024-in-bangladesh
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-28-august-4-september-2024-in-bangladesh
dataset_id: rdls_he-bgd_unosat_detectedwaterextentsbetwe_20240908
description: "UNOSAT code: FL20240825BGD This map illustrates the aggregated floods\
  \ using Sentinel-1 images acquired between 18 to 26 August 2024 and between 28 August\
  \ & 4 September 2024 using an automated analysis with a machine learning method.\
  \ Within the analysed area of about 140,000 km\xB2, a total of about 8,100 km\xB2\
  \ of land appears to be affected by flood waters. Based on Worldpop spatial demographic\
  \ data, about 6.2 million people are exposed or living close to flooded areas. Over\
  \ these two periods, floodwaters receded by approximately 8,700 km\xB2. This is\
  \ a preliminary analysis and has not yet been validated in the field. Please send\
  \ ground feedback to the United Nations Satellite Centre (UNOSAT). Important note:\
  \ Flood analysis from radar images may underestimate the presence of standing waters\
  \ in built-up areas and densely vegetated areas due to the backscattering properties\
  \ of the radar signal.. [Source: This metadata record was automatically extracted\
  \ from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extents-between-28-august-4-september-2024-in-bangladesh]"
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
    description: "Population exposed to or living close to flooded areas, estimated\
      \ using WorldPop spatial demographic data for the analysed area of ~140,000\
      \ km\xB2"
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
  description: "Sentinel-1 SAR imagery from two acquisition periods (18\u201326 August\
    \ and 28 August\u20134 September 2024) was processed using an automated machine\
    \ learning method by UNOSAT to delineate flood water extents across approximately\
    \ 140,000 km\xB2 of Bangladesh. The resulting flood polygons were aggregated to\
    \ quantify total inundated area (~8,100 km\xB2) and flood recession (~8,700 km\xB2\
    ), and intersected with WorldPop demographic data to estimate exposed population\
    \ (~6.2 million people). This preliminary analysis supports rapid humanitarian\
    \ response and disaster impact assessment."
  sources:
  - id: source_1
    license: null
    name: Sentinel-1 (ESA Copernicus)
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
- href: https://data.humdata.org/dataset/satellite-detected-water-extents-between-28-august-4-september-2024-in-bangladesh
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
  description: Satellite detected water extents between 28 August & 4 September 2024
    in Bangladesh (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3954/FL20240825BGD_gdb.zip
  format: Geodatabase
  id: resource_10aac3f5
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240825BGD_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents between 28 August & 4 September 2024
    in Bangladesh (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3954/FL20240825BGD_SHP.zip
  format: null
  id: resource_61e05a55
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240825BGD_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents between 28 August & 4 September 2024
    in Bangladesh (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3954/UNOSAT_FL20240825BGD_PopulationExposed_18_August_04_September_2024.xlsx
  format: null
  id: resource_facb115a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_FL20240825BGD_PopulationExposed_18_August_04_September_2024.xlsx
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-bgd_unosat_detectedwaterextentsbetwe_20240908
spatial:
  bbox: null
  centroid: null
  countries:
  - BGD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-09-08'
temporal_resolution: null
title: Satellite detected water extents between 28 August & 4 September 2024 in Bangladesh
version: null
vulnerability: null
---
