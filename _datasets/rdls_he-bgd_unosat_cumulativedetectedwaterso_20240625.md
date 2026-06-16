---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-1 satellite imagery
    url: https://data.humdata.org/dataset/cumulative-satellite-detected-waters-over-sylhet-division-bangladesh-as-of-19-22-june-2024
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/cumulative-satellite-detected-waters-over-sylhet-division-bangladesh-as-of-19-22-june-2024
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/cumulative-satellite-detected-waters-over-sylhet-division-bangladesh-as-of-19-22-june-2024
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/cumulative-satellite-detected-waters-over-sylhet-division-bangladesh-as-of-19-22-june-2024
dataset_id: rdls_he-bgd_unosat_cumulativedetectedwaterso_20240625
description: 'UNOSAT code: FL20240502BGD, GDACS ID: 1001064 This map illustrates cumulative
  satellite-detected surface waters in Sylhet Division, Bangladesh as observed from
  Sentinel-1 images acquired on the 19th and 22nd June 2024 and using an automated
  analysis with machine learning method. Within the analysed area of about 12,000
  km2, about 2,600 km2 of land appears to be flooded. Based on Worldpop population
  data and the detected surface waters in the analysed area, the potentially exposed
  population is mainly located in the district of Sylhet with ~1 million people, Habiganj
  with ~530,000 people, Sunamganj with ~420,000 people. This is a preliminary analysis
  and has not yet been validated in the field. Please send ground feedback to the
  United Nations Satellite Centre (UNOSAT). Important note: Flood analysis from radar
  images may underestimate the presence of standing waters in built-up areas and densely
  vegetated areas due to backscattering properties of the radar signal.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/cumulative-satellite-detected-waters-over-sylhet-division-bangladesh-as-of-19-22-june-2024]'
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
    description: Potentially exposed population in Sylhet Division derived from WorldPop
      data intersected with detected flood extent
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
  description: "Sentinel-1 SAR imagery from 19-22 June 2024 was processed using automated\
    \ machine learning methods to detect cumulative surface water extent across ~12,000\
    \ km\xB2 in Sylhet Division. The resulting 2,600 km\xB2 flood extent was intersected\
    \ with WorldPop population data to estimate potentially exposed population by\
    \ district."
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
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/cumulative-satellite-detected-waters-over-sylhet-division-bangladesh-as-of-19-22-june-2024
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
  description: Cumulative Satellite Detected Waters over Sylhet Division, Bangladesh
    as of 19 & 22 June 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3885/TC20240502BGD_gdb.zip
  format: Geodatabase
  id: resource_bbec31a1
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20240502BGD_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Cumulative Satellite Detected Waters over Sylhet Division, Bangladesh
    as of 19 & 22 June 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3885/TC20240502BGD_SHP.zip
  format: null
  id: resource_87bb2227
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20240502BGD_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Cumulative Satellite Detected Waters over Sylhet Division, Bangladesh
    as of 19 & 22 June 2024 (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3885/UNOSAT_Population_Exposure_FL20240502BGD_19To22June2024.xlsx
  format: null
  id: resource_e7c9f952
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_Population_Exposure_FL20240502BGD_19To22June2024.xlsx
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-bgd_unosat_cumulativedetectedwaterso_20240625
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
  start: '2024-06-25'
temporal_resolution: null
title: Cumulative Satellite Detected Waters over Sylhet Division, Bangladesh as of
  19 & 22 June 2024
version: null
vulnerability: null
---
