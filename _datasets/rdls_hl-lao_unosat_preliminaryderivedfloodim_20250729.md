---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/preliminary-satellite-derived-flood-impact-assessment-muang-sam-tai-xamtay-district-houaph
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/preliminary-satellite-derived-flood-impact-assessment-muang-sam-tai-xamtay-district-houaph
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/preliminary-satellite-derived-flood-impact-assessment-muang-sam-tai-xamtay-district-houaph
dataset_id: rdls_hl-lao_unosat_preliminaryderivedfloodim_20250729
description: 'UNOSAT code: TC20250722LAO, GDACS ID: 1001181 Status: Landslide and
  Increased water of Nam Xam River and areas of washaway along the riverbank Further
  action(s): continue monitoring Summary of findings: Increased water in the Nam Xam
  River and areas of washaway along the riverbank were observed in Muang Sam Tai,
  Xamtay District, Houaphan Province as of 28 July 2025. Structures/buildings damaged
  by landslides were observed in Muang Sam Tai, Xamtay District, Houaphan Province,
  as of 28 July 2025.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/preliminary-satellite-derived-flood-impact-assessment-muang-sam-tai-xamtay-district-houaph]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure: []
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
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts reviewed and compared satellite imagery acquired on
    28-29 July 2025 to detect changes in water extent along Nam Xam River and identify
    structures damaged by landslides. Visual interpretation of satellite data was
    used to map flood impacts and damage locations without quantitative intensity
    measurements.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/preliminary-satellite-derived-flood-impact-assessment-muang-sam-tai-xamtay-district-houaph
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from fluvial flooding and associated riverbank
      washaway
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from landslides triggered during the event
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
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
  description: Preliminary Satellite-derived Flood Impact Assessment, Muang Sam Tai,
    Xamtay District, Houaphan Province, LAO PDR, 29 July 2025 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4159/TC20250722LAO_gdb.zip
  format: Geodatabase
  id: resource_a07c9940
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20250722LAO_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Preliminary Satellite-derived Flood Impact Assessment, Muang Sam Tai,
    Xamtay District, Houaphan Province, LAO PDR, 29 July 2025 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4159/TC20250722LAO_SHP.zip
  format: null
  id: resource_0518010a
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20250722LAO_SHP.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-lao_unosat_preliminaryderivedfloodim_20250729
spatial:
  bbox: null
  centroid: null
  countries:
  - LAO
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-07-29'
temporal_resolution: null
title: Preliminary Satellite-derived Flood Impact Assessment, Muang Sam Tai, Xamtay
  District, Houaphan Province, LAO PDR, 29 July 2025
version: null
vulnerability: null
---
