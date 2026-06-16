---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/flood-impact-assessment-in-santo-antao-island-cabo-verde-13-to-16-august-2025
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/flood-impact-assessment-in-santo-antao-island-cabo-verde-13-to-16-august-2025
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/flood-impact-assessment-in-santo-antao-island-cabo-verde-13-to-16-august-2025
dataset_id: rdls_hel-cpv_unosat_floodimpactassessmentsant_20250826
description: "UNOSAT code: FL20250812CPV This map illustrates satellite-detected mudflow\
  \ extent in Santo Antao Island, Cabo Verde as observed from Pleiades very high-resolution\
  \ satellite image acquired on 13 to 16 August 2025. Within the analyzed area of\
  \ approximately 700 km\xB2, about 3 km\xB2 of land appears to be affected by flood.\
  \ Additionally, UNOSAT identified around 460 damaged buildings, two damaged bridges,\
  \ and approximately 5 km of affected roads. This is a preliminary analysis and has\
  \ not yet been validated in the field. Please send ground feedback to the United\
  \ Nations Satellite Centre (UNOSAT).. [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/flood-impact-assessment-in-santo-antao-island-cabo-verde-13-to-16-august-2025]"
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
    description: Building stock in Santo Antao Island exposed to flood hazard
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
    description: Road network and bridge infrastructure exposed to flood hazard
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
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: Pleiades satellite imagery acquired 13-16 August 2025 was analyzed
    by UNOSAT analysts through visual interpretation and multi-temporal comparison
    to detect mudflow extent and map direct damage impacts. Satellite-detected features
    were vectorized and quantified to produce damage assessments of buildings, bridges,
    and road networks affected by the flood event.
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
- href: https://data.humdata.org/dataset/flood-impact-assessment-in-santo-antao-island-cabo-verde-13-to-16-august-2025
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: 'Direct building damage from flood event: 460 damaged buildings identified'
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
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: 'Direct infrastructure damage from flood event: 2 damaged bridges
      and approximately 5 km of affected roads'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
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
  description: Flood impact assessment in Santo Antao Island, Cabo Verde (13 to 16
    August 2025) (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4181/FL20250812CPV_GDB.zip
  format: Geodatabase
  id: resource_54fc23da
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
  description: Flood impact assessment in Santo Antao Island, Cabo Verde (13 to 16
    August 2025) (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4181/FL20250812CPV_SHP.zip
  format: null
  id: resource_9e864412
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
slug: rdls_hel-cpv_unosat_floodimpactassessmentsant_20250826
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
  start: '2025-08-26'
temporal_resolution: null
title: Flood impact assessment in Santo Antao Island, Cabo Verde (13 to 16 August
  2025)
version: null
vulnerability: null
---
