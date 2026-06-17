---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-1 satellite imagery
    url: https://data.humdata.org/dataset/water-extent-over-barisal-dhaka-and-khulna-divisions-bangladesh-as-of-1-june-2024
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop population data
    url: https://data.humdata.org/dataset/water-extent-over-barisal-dhaka-and-khulna-divisions-bangladesh-as-of-1-june-2024
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-over-barisal-dhaka-and-khulna-divisions-bangladesh-as-of-1-june-2024
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-over-barisal-dhaka-and-khulna-divisions-bangladesh-as-of-1-june-2024
dataset_id: rdls_he-bgd_unosat_detectedwaterextentoverba_20240604
description: 'UNOSAT code: FL20240502BGD, GDACS ID: 1001064 This map illustrates satellite-detected
  surface waters in Barisal, Dhaka and Khulna Divisions, Bangladesh as observed from
  a Sentinel-1 images acquired on 1 June 2024 at 05:56 local time and using an automated
  analysis with machine learning method. Within the analyzed area of about 52,000
  km2, about 1,000 km2 of land appears to be flooded. Based on Worldpop population
  data and the detected surface waters in the analyzed area, the potentially exposed
  population is mainly located in the district of Bagerhat, Khulna Division with ~96,000
  people, and Barguna, Barisal Division with ~74,000 people. This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to the United Nations Satellite Centre (UNOSAT). Important note: Flood analysis
  from radar images may underestimate the presence of standing waters in built-up
  areas and densely vegetated areas due to backscattering properties of the radar
  signal.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-over-barisal-dhaka-and-khulna-divisions-bangladesh-as-of-1-june-2024]'
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
    description: Potentially exposed population in flooded areas derived from WorldPop
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
  description: "Sentinel-1 SAR imagery acquired on 1 June 2024 was processed using\
    \ automated machine learning methods to detect surface water extent across 52,000\
    \ km\xB2 in three Bangladesh divisions. Detected water bodies (~1,000 km\xB2)\
    \ were intersected with WorldPop gridded population data to estimate potentially\
    \ exposed population, with results compiled into shapefiles and exposure summary\
    \ tables by administrative district."
  sources:
  - id: source_1
    license: null
    name: Sentinel-1 satellite imagery
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
- href: https://data.humdata.org/dataset/water-extent-over-barisal-dhaka-and-khulna-divisions-bangladesh-as-of-1-june-2024
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
  description: Satellite detected water extent over Barisal, Dhaka and Khulna Divisions,
    Bangladesh as of 1 June 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3865/FL20240502BGD_SHP.zip
  format: null
  id: resource_442f27a2
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240502BGD_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent over Barisal, Dhaka and Khulna Divisions,
    Bangladesh as of 1 June 2024 (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3865/UNOSAT_PopulationExposure_FL20240502BGD_Bangladesh_01Jun2024.xlsx
  format: null
  id: resource_ed927aba
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_PopulationExposure_FL20240502BGD_Bangladesh_01Jun2024.xlsx
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-bgd_unosat_detectedwaterextentoverba_20240604
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
  start: '2024-06-04'
temporal_resolution: null
title: Satellite detected water extent over Barisal, Dhaka and Khulna Divisions, Bangladesh
  as of 1 June 2024
version: null
vulnerability: null
---
