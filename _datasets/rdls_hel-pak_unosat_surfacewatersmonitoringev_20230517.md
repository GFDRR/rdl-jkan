---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/surface-waters-monitoring-in-pakistan-evolution-17-may-2023
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/surface-waters-monitoring-in-pakistan-evolution-17-may-2023
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/surface-waters-monitoring-in-pakistan-evolution-17-may-2023
dataset_id: rdls_hel-pak_unosat_surfacewatersmonitoringev_20230517
description: "UNOSAT code FL20221121PAK Status: Overall decrease in the observed surface\
  \ waters Further action(s): continue monitoring Evolution of Cumulative Surface\
  \ Waters over I.R. of Pakistan (21 to 25 Apr. 2023) Vs. (26 to 30 Apr. 2023) Between\
  \ 26 to 30 April 2023 approximately 1 million people are potentially exposed or\
  \ living close to maximum floodwaters areas( ); Approximately 230,000 people are\
  \ potentially exposed or living close to minimum floodwaters areas( *) between 26\
  \ to 30 April 2023; Based on satellite observations between 21 to 25 April 2023\
  \ and compared with observations between 26 to 30 April 2023, the maximum flood\
  \ water extent appears to continue to retract with approximately ~ -3,700 km\xB2\
  \ in Sindh, ~ - 1,500 km\xB2 in Punjab, ~ -160 km\xB2 in Balochistan and ~ - 180\
  \ km\xB2 in Khyber Pakhtunkhwa.. [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/surface-waters-monitoring-in-pakistan-evolution-17-may-2023]"
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
    description: Population living close to or potentially exposed to maximum and
      minimum floodwater areas
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
  description: UNOSAT analysts compared satellite imagery from two time periods (April
    21-25 vs. April 26-30, 2023) to map cumulative surface water extent across Pakistan.
    Population exposure was derived by intersecting observed floodwater polygons with
    gridded population data to quantify potentially affected populations at maximum
    and minimum inundation levels.
  sources:
  - id: source_1
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
- href: https://data.humdata.org/dataset/surface-waters-monitoring-in-pakistan-evolution-17-may-2023
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population exposed to floodwaters based on satellite-observed inundation
      extent
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
  description: Surface Waters Monitoring In Pakistan - Evolution - 17 May 2023 (Zipped
    geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3594/FL20221121PAK_gdb.zip
  format: Geodatabase
  id: resource_5765c418
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20221121PAK_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Surface Waters Monitoring In Pakistan - Evolution - 17 May 2023 (Zipped
    shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3594/FL20221121PAK_SHP.zip
  format: null
  id: resource_5aa49819
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20221121PAK_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Surface Waters Monitoring In Pakistan - Evolution - 17 May 2023 (Excel
    file)
  download_url: https://unosat.org/static/unosat_filesystem/3594/UNOSAT_PopulationExposure_FL20221121PAK_20230421_20230430.csv
  format: null
  id: resource_89cbb7c7
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_PopulationExposure_FL20221121PAK_20230421_20230430.csv
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-pak_unosat_surfacewatersmonitoringev_20230517
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
  start: '2023-05-17'
temporal_resolution: null
title: Surface Waters Monitoring In Pakistan - Evolution - 17 May 2023
version: null
vulnerability: null
---
