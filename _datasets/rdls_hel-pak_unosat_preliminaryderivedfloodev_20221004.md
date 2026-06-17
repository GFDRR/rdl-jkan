---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/preliminary-satellite-derived-flood-evolution-assessment-islamic-republic-of-pakistan-4-oc
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/preliminary-satellite-derived-flood-evolution-assessment-islamic-republic-of-pakistan-4-oc
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/preliminary-satellite-derived-flood-evolution-assessment-islamic-republic-of-pakistan-4-oc
dataset_id: rdls_hel-pak_unosat_preliminaryderivedfloodev_20221004
description: "UNOSAT code FL20220808PAK, GDACS Id: 1101522 Status: Overall decrease\
  \ of flood waters observed Further action(s): continue monitoring Summary of findings;\
  \ Evolution of Cumulative Flood Waters over I.R. of Pakistan (15 - 21 September\
  \ Vs 26 September-2 October 2022): Between 26 September and 2 October 2022 approximately\
  \ 15 million people remain potentially exposed or living close to flooded areas;\
  \ Based on satellite observations between 15 to 21 September 2022 and compared with\
  \ observations between 26 September and 2 October 2022, the overall flood water\
  \ extents appear to continue to decrease with approximately 600 km\xB2 in Balochistan,\
  \ ~Punjab 500 km\xB2 and ~2,600 km\xB2 in Sindh.. [Source: This metadata record\
  \ was automatically extracted from the Humanitarian Data Exchange (HDX); Original\
  \ dataset: https://data.humdata.org/dataset/preliminary-satellite-derived-flood-evolution-assessment-islamic-republic-of-pakistan-4-oc]"
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
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts compared satellite imagery from two time periods (15-21
    September vs 26 September-2 October 2022) to identify and map cumulative flood
    water extents across Pakistan. Flood polygons were digitized from satellite observations
    and stored in geodatabase and shapefile formats with area calculations in hectares
    and square meters. The dataset tracks flood evolution and provides exposure estimates
    of approximately 15 million people living in or near affected areas.
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
- href: https://data.humdata.org/dataset/preliminary-satellite-derived-flood-evolution-assessment-islamic-republic-of-pakistan-4-oc
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population exposed to flood waters based on satellite-derived inundation
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
  description: Preliminary Satellite Derived Flood Evolution Assessment, Islamic Republic
    of Pakistan-4 October 2022 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3389/FL20220808PAK_gdb.zip
  format: Geodatabase
  id: resource_c7472f8d
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
  description: Preliminary Satellite Derived Flood Evolution Assessment, Islamic Republic
    of Pakistan-4 October 2022 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3389/FL20220808PAK_SHP.zip
  format: null
  id: resource_09c18232
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
  description: Preliminary Satellite Derived Flood Evolution Assessment, Islamic Republic
    of Pakistan-4 October 2022 (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3389/Preliminary%20satellite-derived%20flood%20evolution%20assessment%20-%2002%20October%202022.csv
  format: null
  id: resource_ef5aeb2b
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Preliminary satellite-derived flood evolution assessment - 02 October 2022.csv
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-pak_unosat_preliminaryderivedfloodev_20221004
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
  start: '2022-10-04'
temporal_resolution: null
title: Preliminary Satellite Derived Flood Evolution Assessment, Islamic Republic
  of Pakistan-4 October 2022
version: null
vulnerability: null
---
