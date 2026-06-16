---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/preliminary-satellite-derived-flood-evolution-assessment-23-september-2022
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/preliminary-satellite-derived-flood-evolution-assessment-23-september-2022
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/preliminary-satellite-derived-flood-evolution-assessment-23-september-2022
dataset_id: rdls_hel-pak_unosat_preliminaryderivedfloodev_20220922
description: "UNOSAT code FL20220808PAK, GDACS Id: 1101522 Status: Overall decreasing\
  \ flood waters observed Further action(s): continue monitoring Evolution of Cumulative\
  \ Flood Impact Assessment (08 - 14 September Vs 15-21 September 2022): From 15 to\
  \ 21 September 2022 approximately 17 million people remain potentially exposed or\
  \ living close to flooded areas; Based on satellite observations between 08 to 14\
  \ September 2022 and compared with observations between 15 and 21 September 2022,\
  \ the overall flood waters extents appears to continue to decrease with approximately\
  \ 600 km\xB2 in Balochistan, ~Punjab 1,100 km\xB2 and ~5,000 km\xB2 in Sindh.. [Source:\
  \ This metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/preliminary-satellite-derived-flood-evolution-assessment-23-september-2022]"
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
    description: Population potentially exposed or living close to flooded areas
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
  description: UNOSAT analysts processed multi-temporal satellite imagery from 08-14
    September and 15-21 September 2022, comparing images to detect changes in flood
    extent and map cumulative inundation areas. Flood polygons were digitized and
    attributed with sensor date, area measurements, and event metadata. Population
    exposure was calculated by intersecting flood extent with gridded population data
    to estimate affected populations.
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
- href: https://data.humdata.org/dataset/preliminary-satellite-derived-flood-evolution-assessment-23-september-2022
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population exposed to flood inundation based on satellite-observed
      flood extent
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
  description: Pakistan - Preliminary satellite-derived flood evolution assessment
    - 23 September 2022 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3376/FL20220808PAK_gdb.zip
  format: Geodatabase
  id: resource_8144af3b
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20220808PAK_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pakistan - Preliminary satellite-derived flood evolution assessment
    - 23 September 2022 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3376/FL20220808PAK_SHP.zip
  format: null
  id: resource_7db2a7c2
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20220808PAK_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pakistan - Preliminary satellite-derived flood evolution assessment
    - 23 September 2022 (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3376/UNOSAT_Population_Exposure_FL20220808PAK_20220815_20220821_WeeklyUpdate3.xlsx
  format: null
  id: resource_e90f9bcd
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_Population_Exposure_FL20220808PAK_20220815_20220821_WeeklyUpdate3.xlsx
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-pak_unosat_preliminaryderivedfloodev_20220922
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
  start: '2022-09-22'
temporal_resolution: null
title: Pakistan - Preliminary satellite-derived flood evolution assessment - 23 September
  2022
version: null
vulnerability: null
---
