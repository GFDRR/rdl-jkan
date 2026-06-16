---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/preliminary-satellite-derived-flood-and-landslide-assessment
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/preliminary-satellite-derived-flood-and-landslide-assessment
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/preliminary-satellite-derived-flood-and-landslide-assessment
dataset_id: rdls_hel-zaf_unosat_preliminaryderivedfloodla_20220425
description: 'UNOSAT code: FL20220418ZAF SUMMARY OF FINDINGS: Increased water level,
  inundated infrastructure & damaged road observed along the Mlazi river as of 14
  April 2022; Inundated SAPREF Oil Refinery as of 14 April 2022; Increased water level
  and damaged roadway observed along the Mhlatuzana river as of 14 April 2022; Inundated
  area observed along the Umbilo river as of 14 April 2022; Increased water level
  and landslide observed along the Palmiet river as of 14 April 2022. Status: : Increased
  water level and landslides observed Further action(s): Continue monitoring. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/preliminary-satellite-derived-flood-and-landslide-assessment]'
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
    description: Road networks and oil refinery infrastructure exposed to flood inundation
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_1
  metrics:
  - dimension: structure
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
      id: es_flood_hzd
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: es_flood
    occurrence_range: null
    seasonality: null
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: es_landslide_hzd
      intensity_measure: pgd:m
      process: landslide_mudflow
      trigger: null
      type: landslide
    id: es_landslide
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts conducted comparative satellite imagery analysis of
    the Durban region as of 14 April 2022, identifying changes in water levels, inundation
    extents, and landslide occurrence across five river systems (Mlazi, Mhlatuzana,
    Umbilo, Palmiet) and critical infrastructure (SAPREF Oil Refinery). Results were
    delivered as vector geodatabase and shapefile formats with spatial extent and
    area measurements.
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
- href: https://data.humdata.org/dataset/preliminary-satellite-derived-flood-and-landslide-assessment
  rel: source
loss:
  losses:
  - asset_category: infrastructure
    asset_dimension: structure
    description: Direct damage to roads and SAPREF Oil Refinery from fluvial flooding
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
  - asset_category: infrastructure
    asset_dimension: structure
    description: Direct landslide impact observed along Palmiet river
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
  description: South Africa - PRELIMINARY SATELLITE-DERIVED FLOOD AND LANDSLIDE ASSESSMENT
    (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/ZA/FL20220418ZAF/FL20220418ZAF_gdb.zip
  format: Geodatabase
  id: resource_27b61c3c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20220418ZAF_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: South Africa - PRELIMINARY SATELLITE-DERIVED FLOOD AND LANDSLIDE ASSESSMENT
    (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/ZA/FL20220418ZAF/FL20220418ZAF_SHP.zip
  format: null
  id: resource_1b759aae
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20220418ZAF_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-zaf_unosat_preliminaryderivedfloodla_20220425
spatial:
  bbox: null
  centroid: null
  countries:
  - ZAF
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-04-25'
temporal_resolution: null
title: South Africa - PRELIMINARY SATELLITE-DERIVED FLOOD AND LANDSLIDE ASSESSMENT
version: null
vulnerability: null
---
