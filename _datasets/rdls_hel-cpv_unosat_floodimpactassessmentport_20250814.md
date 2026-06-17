---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/flood-impact-assessment-in-porto-novo-town-porto-novo-municipality-cabo-verde-as-of-13-aug
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/flood-impact-assessment-in-porto-novo-town-porto-novo-municipality-cabo-verde-as-of-13-aug
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/flood-impact-assessment-in-porto-novo-town-porto-novo-municipality-cabo-verde-as-of-13-aug
dataset_id: rdls_hel-cpv_unosat_floodimpactassessmentport_20250814
description: "UNOSAT code: FL20250812CPV This map illustrates satellite-detected mudflow\
  \ extent in Porto Novo Town, Porto Novo Municipality, Cabo Verde as observed from\
  \ Pleiades very high-resolution satellite image acquired on 13 August 2025 at 11:01\
  \ local time (12:01 UTC). Within the analyzed area of approximately 2 km\xB2, about\
  \ 0.3 km\xB2 of land appears to be affected by flood. UNOSAT identified around 300\
  \ damaged buildings and approximately 1 km of affected roads. This is a preliminary\
  \ analysis and has not yet been validated in the field. Please send ground feedback\
  \ to the United Nations Satellite Centre (UNOSAT).. [Source: This metadata record\
  \ was automatically extracted from the Humanitarian Data Exchange (HDX); Original\
  \ dataset: https://data.humdata.org/dataset/flood-impact-assessment-in-porto-novo-town-porto-novo-municipality-cabo-verde-as-of-13-aug]"
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
    description: Building stock in Porto Novo Town affected by flood mudflow
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Road network affected by flood mudflow in the study area
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: length
      unit: null
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
  description: UNOSAT analysts reviewed Pleiades very high-resolution satellite imagery
    acquired on 13 August 2025 and compared it with reference imagery to detect mudflow
    extent and identify notable changes. Damage assessment was conducted through visual
    interpretation of satellite imagery to quantify affected buildings and road infrastructure
    in Porto Novo Town, Cabo Verde.
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
- href: https://data.humdata.org/dataset/flood-impact-assessment-in-porto-novo-town-porto-novo-municipality-cabo-verde-as-of-13-aug
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: 'Direct building damage from flood mudflow: approximately 300 damaged
      buildings identified'
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
    description: 'Direct infrastructure damage from flood mudflow: approximately 1
      km of affected roads'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
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
  description: Flood impact assessment in Porto Novo Town, Porto Novo Municipality,
    Cabo Verde as of 13 August 2025 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4171/FL20250812CPV_GDB.zip
  format: Geodatabase
  id: resource_e236adb8
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20250812CPV_GDB.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flood impact assessment in Porto Novo Town, Porto Novo Municipality,
    Cabo Verde as of 13 August 2025 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4171/FL20250812CPV_SHP.zip
  format: null
  id: resource_13b53143
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20250812CPV_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-cpv_unosat_floodimpactassessmentport_20250814
spatial:
  bbox: null
  centroid: null
  countries:
  - CPV
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-08-14'
temporal_resolution: null
title: Flood impact assessment in Porto Novo Town, Porto Novo Municipality, Cabo Verde
  as of 13 August 2025
version: null
vulnerability: null
---
