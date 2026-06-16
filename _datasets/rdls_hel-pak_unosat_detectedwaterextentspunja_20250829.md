---
attributions:
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-in-punjab-province-pakistan-as-of-27-28-august-2025
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Sentinel-1 satellite imagery
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-in-punjab-province-pakistan-as-of-27-28-august-2025
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-in-punjab-province-pakistan-as-of-27-28-august-2025
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-in-punjab-province-pakistan-as-of-27-28-august-2025
dataset_id: rdls_hel-pak_unosat_detectedwaterextentspunja_20250829
description: "UNOSAT code: FL20250818PAK, GDACS ID: 1103435 This map illustrates the\
  \ satellite detected water extent in Punjab Province, Pakistan as observed from\
  \ a Sentinel-1 satellite image acquired on 27-28 August 2025. Within the analyzed\
  \ area of approximately 88,300 km\xB2, about 3,660 km\xB2 of land appears to be\
  \ affected by floodwaters. Based on WorldPop population data and the flood extent,\
  \ approximately 2.5 million people are potentially exposed or living close to the\
  \ flooded areas. This is a preliminary analysis and has not yet been validated in\
  \ the field. Please send ground feedback to the United Nations Satellite Centre\
  \ (UNOSAT). Important note: Flood analysis from radar images may underestimate the\
  \ presence of standing waters in built-up areas and densely vegetated areas due\
  \ to the backscattering properties of the radar signal.. [Source: This metadata\
  \ record was automatically extracted from the Humanitarian Data Exchange (HDX);\
  \ Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extents-in-punjab-province-pakistan-as-of-27-28-august-2025]"
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
    description: Population potentially exposed or living close to flooded areas in
      Punjab Province based on WorldPop data
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
  description: "Sentinel-1 SAR satellite imagery from 27-28 August 2025 was analyzed\
    \ by UNOSAT to detect water extent through comparison of pre- and post-event images,\
    \ identifying notable changes in surface water. The resulting flood extent polygon\
    \ (3,660 km\xB2) was intersected with WorldPop gridded population data to estimate\
    \ approximately 2.5 million people potentially exposed to floodwaters in Punjab\
    \ Province."
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
    name: Sentinel-1 satellite imagery
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/satellite-detected-water-extents-in-punjab-province-pakistan-as-of-27-28-august-2025
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by flood extent in Punjab Province, Pakistan
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
  description: Satellite detected water extents in Punjab Province, Pakistan as of
    27 & 28 August 2025 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4185/FL20250818PAK_gdb.zip
  format: Geodatabase
  id: resource_24b31e78
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20250818PAK_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents in Punjab Province, Pakistan as of
    27 & 28 August 2025 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4185/FL20250818PAK_SHP.zip
  format: null
  id: resource_b9217388
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20250818PAK_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents in Punjab Province, Pakistan as of
    27 & 28 August 2025 (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/4185/UNOSAT_PopulationExposure_FL20250818PAK_Punjab_27_28Aug2025.xlsx
  format: null
  id: resource_ae8cc63f
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_PopulationExposure_FL20250818PAK_Punjab_27_28Aug2025.xlsx
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-pak_unosat_detectedwaterextentspunja_20250829
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
  start: '2025-08-29'
temporal_resolution: null
title: Satellite detected water extents in Punjab Province, Pakistan as of 27 & 28
  August 2025
version: null
vulnerability: null
---
