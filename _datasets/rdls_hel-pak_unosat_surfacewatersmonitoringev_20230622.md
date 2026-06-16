---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/surface-waters-monitoring-in-pakistan-evolution-22-june-2023
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/surface-waters-monitoring-in-pakistan-evolution-22-june-2023
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/surface-waters-monitoring-in-pakistan-evolution-22-june-2023
dataset_id: rdls_hel-pak_unosat_surfacewatersmonitoringev_20230622
description: "UNOSAT code TC20230616PAK Status: Overall increase in the observed surface\
  \ waters Further action(s): continue monitoring Evolution of Cumulative Surface\
  \ Waters over I.R. of Pakistan (26 to 30 April 2023) Vs. (16 to 20 June 2023) -\
  \ Between 16 to 20 June 2023 approximately 3 million people are potentially exposed\
  \ or living close to maximum floodwaters areas( ); - Approximately 468,000 people\
  \ are potentially exposed or living close to minimum floodwaters areas( *) between\
  \ 16 to 20 June 2023; - Based on satellite observations between 16 to 20 June 2023\
  \ and compared with observations between 26 to 30 April 2023, the maximum flood\
  \ water extent appears to increase approximately ~ 2,000 km\xB2 in Sindh and ~ 3,500\
  \ km\xB2 in Punjab.. [Source: This metadata record was automatically extracted from\
  \ the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/surface-waters-monitoring-in-pakistan-evolution-22-june-2023]"
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts compared satellite imagery from two time periods (26-30
    April 2023 vs. 16-20 June 2023) to map cumulative surface water extent across
    Pakistan. Observed floodwater areas were vectorized and attributed with area measurements.
    Population exposure was estimated by spatial intersection of mapped water extents
    with population data to quantify people living close to maximum and minimum floodwater
    zones.
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
- href: https://data.humdata.org/dataset/surface-waters-monitoring-in-pakistan-evolution-22-june-2023
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population potentially exposed to floodwaters based on satellite-observed
      surface water extent
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
  description: Surface Waters Monitoring In Pakistan - Evolution - 22 June 2023 (Zipped
    geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3630/TC20230616PAK_gdb.zip
  format: Geodatabase
  id: resource_f3de3c48
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20230616PAK_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Surface Waters Monitoring In Pakistan - Evolution - 22 June 2023 (Zipped
    shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3630/TC20230616PAK_SHP.zip
  format: null
  id: resource_bdc3186e
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20230616PAK_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Surface Waters Monitoring In Pakistan - Evolution - 22 June 2023 (Excel
    file)
  download_url: https://unosat.org/static/unosat_filesystem/3630/Surface%20Waters%20Monitoring%20In%20Pakistan%20-%20Evolution%20-%2022%20June%202023.csv
  format: null
  id: resource_2a3c815c
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Surface Waters Monitoring In Pakistan - Evolution - 22 June 2023.csv
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-pak_unosat_surfacewatersmonitoringev_20230622
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
  start: '2023-06-22'
temporal_resolution: null
title: Surface Waters Monitoring In Pakistan - Evolution - 22 June 2023
version: null
vulnerability: null
---
