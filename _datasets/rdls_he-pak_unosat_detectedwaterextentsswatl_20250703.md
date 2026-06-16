---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-2 satellite imagery
    url: https://data.humdata.org/dataset/water-extents-in-swat-lower-dir-and-malakand-districts-khyber-pakhtunkhwa-province-pakista
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop population data
    url: https://data.humdata.org/dataset/water-extents-in-swat-lower-dir-and-malakand-districts-khyber-pakhtunkhwa-province-pakista
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-in-swat-lower-dir-and-malakand-districts-khyber-pakhtunkhwa-province-pakista
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-in-swat-lower-dir-and-malakand-districts-khyber-pakhtunkhwa-province-pakista
dataset_id: rdls_he-pak_unosat_detectedwaterextentsswatl_20250703
description: "UNOSAT code: FL20250630PAK This map illustrates the satellite detected\
  \ water extent in Swat, Lower Dir and Malakand Districts, Pakistan as observed from\
  \ a Sentinel-2 satellite image acquired on 1 July 2025 at 10:56 local time (05:56\
  \ UTC). Within the analyzed area of approximately 900 km\xB2, about 40 km\xB2 of\
  \ land appears to be affected by floodwaters. Based on WorldPop population data\
  \ and the flood extent, approximately 105,000 people are potentially exposed or\
  \ living close to the flooded areas. This is a preliminary analysis and has not\
  \ yet been validated in the field. Please send ground feedback to the United Nations\
  \ Satellite Centre (UNOSAT).. [Source: This metadata record was automatically extracted\
  \ from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extents-in-swat-lower-dir-and-malakand-districts-khyber-pakhtunkhwa-province-pakista]"
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
  event_sets_by_hazard_type:
    flood:
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
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "UNOSAT analysts reviewed Sentinel-2 satellite imagery acquired on\
    \ 1 July 2025 and delineated water extent through visual interpretation and change\
    \ detection methods. The detected flood extent (40 km\xB2) was intersected with\
    \ WorldPop gridded population data to estimate approximately 105,000 people potentially\
    \ exposed to floodwaters in the three districts."
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
- href: https://data.humdata.org/dataset/water-extents-in-swat-lower-dir-and-malakand-districts-khyber-pakhtunkhwa-province-pakista
  rel: source
loss:
  losses: []
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
  description: Satellite detected water extents in Swat, Lower Dir and Malakand Districts,
    Khyber Pakhtunkhwa Province, Pakistan as of 1 July 2025 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4143/FL20250630PAK_gdb.zip
  format: Geodatabase
  id: resource_f2238bc5
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20250630PAK_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents in Swat, Lower Dir and Malakand Districts,
    Khyber Pakhtunkhwa Province, Pakistan as of 1 July 2025 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4143/FL20250630PAK_SHP.zip
  format: null
  id: resource_f313d1a2
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20250630PAK_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents in Swat, Lower Dir and Malakand Districts,
    Khyber Pakhtunkhwa Province, Pakistan as of 1 July 2025 (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/4143/UNOSAT_FL20250630PAK_PopulationExposed_Swat_1July2025.xlsx
  format: null
  id: resource_d316087b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_FL20250630PAK_PopulationExposed_Swat_1July2025.xlsx
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-pak_unosat_detectedwaterextentsswatl_20250703
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
  start: '2025-07-03'
temporal_resolution: null
title: Satellite detected water extents in Swat, Lower Dir and Malakand Districts,
  Khyber Pakhtunkhwa Province, Pakistan as of 1 July 2025
version: null
vulnerability: null
---
