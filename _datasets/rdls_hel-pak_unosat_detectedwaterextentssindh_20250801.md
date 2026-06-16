---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-2 satellite imagery
    url: https://data.humdata.org/dataset/water-extents-in-sindh-balochistan-and-punjab-provinces-pakistan-as-of-31-july-2025
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop population data
    url: https://data.humdata.org/dataset/water-extents-in-sindh-balochistan-and-punjab-provinces-pakistan-as-of-31-july-2025
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-in-sindh-balochistan-and-punjab-provinces-pakistan-as-of-31-july-2025
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-in-sindh-balochistan-and-punjab-provinces-pakistan-as-of-31-july-2025
dataset_id: rdls_hel-pak_unosat_detectedwaterextentssindh_20250801
description: "UNOSAT code: FL20250630PAK This map illustrates the satellite-detected\
  \ water extent in Sindh, Balochistan, and Punjab Provinces, Pakistan, as observed\
  \ from Sentinel-2 satellite images acquired on 31 July 2025 at 13:02 local time\
  \ (08:02 UTC). Within the analyzed area of approximately 83,000 km\xB2, about 6,300\
  \ km\xB2 of land appears to be affected by floodwaters. The floodwater extent appears\
  \ to have increased by approximately 1,300 km\xB2 since 11 July 2025. Based on WorldPop\
  \ population data and the flood extent, approximately 2.3 million people are potentially\
  \ exposed or living close to the flooded areas. This is a preliminary analysis and\
  \ has not yet been validated in the field. Please send ground feedback to the United\
  \ Nations Satellite Centre (UNOSAT).. [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extents-in-sindh-balochistan-and-punjab-provinces-pakistan-as-of-31-july-2025]"
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
    description: Population potentially exposed or living close to detected floodwaters
      based on WorldPop data
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
  description: UNOSAT analysts processed Sentinel-2 satellite imagery acquired on
    31 July 2025 over Sindh, Balochistan, and Punjab provinces, comparing multi-temporal
    images to detect changes in water extent since 11 July 2025. Water extent polygons
    were delineated through visual interpretation and change detection analysis. Population
    exposure was calculated by intersecting the flood extent with WorldPop gridded
    population data to estimate potentially affected populations.
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
- href: https://data.humdata.org/dataset/water-extents-in-sindh-balochistan-and-punjab-provinces-pakistan-as-of-31-july-2025
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by satellite-detected fluvial flooding in Sindh,
      Balochistan, and Punjab
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
  description: Satellite detected water extents in Sindh, Balochistan and Punjab Provinces,
    Pakistan as of 31 July 2025 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4163/FL20250630PAK_31July2025_gdb.zip
  format: Geodatabase
  id: resource_a7494274
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20250630PAK_31July2025_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents in Sindh, Balochistan and Punjab Provinces,
    Pakistan as of 31 July 2025 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4163/FL20250630PAK_31July2025_SHP.zip
  format: null
  id: resource_07bf7ee4
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20250630PAK_31July2025_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents in Sindh, Balochistan and Punjab Provinces,
    Pakistan as of 31 July 2025 (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/4163/UNOSAT_FL20250630PAK_PopulationExposed_CentralPakistan_31July2025.xlsx
  format: null
  id: resource_d541c5d4
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_FL20250630PAK_PopulationExposed_CentralPakistan_31July2025.xlsx
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-pak_unosat_detectedwaterextentssindh_20250801
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
  start: '2025-08-01'
temporal_resolution: null
title: Satellite detected water extents in Sindh, Balochistan and Punjab Provinces,
  Pakistan as of 31 July 2025
version: null
vulnerability: null
---
