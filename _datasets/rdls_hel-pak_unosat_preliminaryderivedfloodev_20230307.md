---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/preliminary-satellite-derived-flood-evolution-assessment-islamic-republic-of-pakistan-07-m
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/preliminary-satellite-derived-flood-evolution-assessment-islamic-republic-of-pakistan-07-m
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/preliminary-satellite-derived-flood-evolution-assessment-islamic-republic-of-pakistan-07-m
dataset_id: rdls_hel-pak_unosat_preliminaryderivedfloodev_20230307
description: "UNOSAT code FL20221121PAK Status: Overall decrease of flood waters observed\
  \ Further action(s): continue monitoring Evolution of Cumulative Flood Waters over\
  \ I.R. of Pakistan (11-15 February 2023 Vs 24-28 February 2023): Between 24 and\
  \ 28 February 2023 approximately 1.8 million people are potentially exposed or living\
  \ close to maximum floodwaters areas( ); Approximately 420,000 people are potentially\
  \ exposed or living close to minimum floodwaters areas( *) between 24 and 28 February\
  \ 2023; Based on satellite observations between 11 and 15 February 2023 and compared\
  \ with observations between 24 and 28 February 2023 , the maximum flood water extent\
  \ appears to continue to retract with approximately ~ -850 km\xB2 in Sindh , ~ -\
  \ 150 km\xB2 in Punjab, ~ -140 km\xB2 in Balochistan and ~ - 60 km\xB2 in Khyber\
  \ Pakhtunkhwa.. [Source: This metadata record was automatically extracted from the\
  \ Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/preliminary-satellite-derived-flood-evolution-assessment-islamic-republic-of-pakistan-07-m]"
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
    description: Population potentially exposed or living close to maximum and minimum
      floodwater areas
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
  description: UNOSAT analysts compared satellite imagery acquired between 11-15 February
    2023 and 24-28 February 2023 to identify and map cumulative floodwater extents
    across Pakistan. Flood polygons were digitized from satellite observations and
    attributed with confidence levels, sensor information, and area measurements.
    Population exposure estimates were derived by overlaying flood extent data with
    population distribution data to quantify people living in or near maximum and
    minimum floodwater areas.
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
- href: https://data.humdata.org/dataset/preliminary-satellite-derived-flood-evolution-assessment-islamic-republic-of-pakistan-07-m
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population exposed to floodwaters during February 2023 event in Pakistan
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
  description: Preliminary Satellite Derived Flood Evolution Assessment, Islamic Republic
    of Pakistan - 07 March 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3519/FL20221121PAK_gdb.zip
  format: Geodatabase
  id: resource_f07c9c17
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
  description: Preliminary Satellite Derived Flood Evolution Assessment, Islamic Republic
    of Pakistan - 07 March 2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3519/FL20221121PAK_SHP.zip
  format: null
  id: resource_6441752a
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
  description: Preliminary Satellite Derived Flood Evolution Assessment, Islamic Republic
    of Pakistan - 07 March 2023 (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3519/UNOSAT_Population_Exposure_FL20221121PAK_WeeklyUpdate_24Feb2023_28Feb2023_Pakistan.xlsx
  format: null
  id: resource_d128f87c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_Population_Exposure_FL20221121PAK_WeeklyUpdate_24Feb2023_28Feb2023_Pakistan.xlsx
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-pak_unosat_preliminaryderivedfloodev_20230307
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
  start: '2023-03-07'
temporal_resolution: null
title: Preliminary Satellite Derived Flood Evolution Assessment, Islamic Republic
  of Pakistan - 07 March 2023
version: null
vulnerability: null
---
