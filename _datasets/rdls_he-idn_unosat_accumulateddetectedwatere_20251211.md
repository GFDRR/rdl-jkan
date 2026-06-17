---
attributions:
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/accumulated-water-extents-in-ache-province-indonesia-as-of-27-nov-to-4-dec-2025
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/accumulated-water-extents-in-ache-province-indonesia-as-of-27-nov-to-4-dec-2025
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/accumulated-water-extents-in-ache-province-indonesia-as-of-27-nov-to-4-dec-2025
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/accumulated-water-extents-in-ache-province-indonesia-as-of-27-nov-to-4-dec-2025
dataset_id: rdls_he-idn_unosat_accumulateddetectedwatere_20251211
description: "UNOSAT code: FL20251126IDN, GDACS ID: 1103633 This map illustrates cumulative\
  \ satellite-detected water extent in Ache Province, Indonesia as observed from multiple\
  \ satellite imagery acquired between 27 Nov. and 4 Dec. 2025. Within the analysed\
  \ areas of about 56,800 km\xB2, a total of about 1,430 km\xB2 of lands appear to\
  \ be affected with flood waters. Based on Worldpop spatial demographic data, about\
  \ 226,000 people in Ache Province are exposed to or living close to flooded areas\
  \ from 27 Nov. and 4 Dec. 2025. This is a preliminary analysis and has not yet been\
  \ validated in the field. Please send ground feedback to the United Nations Satellite\
  \ Centre (UNOSAT).. [Source: This metadata record was automatically extracted from\
  \ the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/accumulated-water-extents-in-ache-province-indonesia-as-of-27-nov-to-4-dec-2025]"
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
    description: Population exposed to or living close to flooded areas based on WorldPop
      spatial demographic data
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
  description: UNOSAT analysts compared multiple satellite images acquired between
    27 Nov and 4 Dec 2025 to detect notable changes in water extent, identifying cumulative
    flood inundation across Aceh Province. WorldPop spatial demographic data was overlaid
    on the satellite-detected water extent polygons to estimate population exposure.
    This preliminary analysis has not been field-validated.
  sources:
  - id: source_1
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/accumulated-water-extents-in-ache-province-indonesia-as-of-27-nov-to-4-dec-2025
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
  description: Accumulated satellite-detected water extents in Ache Province, Indonesia
    as of 27 Nov. to 4 Dec. 2025 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4226/FL20251126IDN_GDB.zip
  format: Geodatabase
  id: resource_546b4d0c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20251126IDN_GDB.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Accumulated satellite-detected water extents in Ache Province, Indonesia
    as of 27 Nov. to 4 Dec. 2025 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4226/FL20251126IDN_SHP.zip
  format: null
  id: resource_e08ecdb0
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20251126IDN_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Accumulated satellite-detected water extents in Ache Province, Indonesia
    as of 27 Nov. to 4 Dec. 2025 (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/4226/UNOSAT_PopulationExposure_FL20251126IDN_Aceh_29Nov2025.xlsx
  format: null
  id: resource_1aff3c3f
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_PopulationExposure_FL20251126IDN_Aceh_29Nov2025.xlsx
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-idn_unosat_accumulateddetectedwatere_20251211
spatial:
  bbox: null
  centroid: null
  countries:
  - IDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-12-11'
temporal_resolution: null
title: Accumulated satellite-detected water extents in Ache Province, Indonesia as
  of 27 Nov. to 4 Dec. 2025
version: null
vulnerability: null
---
