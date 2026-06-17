---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/damage-assessment-in-spera-district-khost-province-as-of-24-june-2022
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-spera-district-khost-province-as-of-24-june-2022
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-spera-district-khost-province-as-of-24-june-2022
dataset_id: rdls_hl-afg_unosat_damageassessmentsperadist_20220701
description: 'UNOSAT code: EQ20220622AFG This map illustrates potentially damaged
  buildings and damaged buildings in Spera district, Khost province of Afghanistan
  as detected by a NewSat image acquired on 24 June 2022. Within the analyzed area,
  UNOSAT has identified 81 potentially damaged buildings, 12 damaged buildings and
  170 shelters. This is a preliminary analysis and has not yet been validated in the
  field. Please send ground feedback to the United Nations Satellite Centre (UNOSAT)..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-in-spera-district-khost-province-as-of-24-june-2022]'
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
      intensity_measure: PGA:g
      process: ground_motion
      trigger: null
      type: earthquake
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: earthquake
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts reviewed NewSat satellite imagery acquired on 24 June
    2022 and compared it with pre-event imagery to detect notable changes in building
    structures. Damaged buildings were classified into two categories (confirmed damaged
    and potentially damaged) through visual interpretation of structural changes,
    with results validated against ground observations where available.
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
- href: https://data.humdata.org/dataset/damage-assessment-in-spera-district-khost-province-as-of-24-june-2022
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: 'Direct building damage assessment from 22 June 2022 earthquake:
      81 potentially damaged buildings and 12 confirmed damaged buildings detected
      via satellite imagery'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
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
  description: Afghanistan - Damage Assessment in Spera district, Khost province as
    of 24 June 2022 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/AF/EQ20220622AFG/EQ20220622AFG_gdb.zip
  format: Geodatabase
  id: resource_cbb664be
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20220622AFG_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Afghanistan - Damage Assessment in Spera district, Khost province as
    of 24 June 2022 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/AF/EQ20220622AFG/EQ20220622AFG_SHP.zip
  format: null
  id: resource_a92b3636
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20220622AFG_SHP.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-afg_unosat_damageassessmentsperadist_20220701
spatial:
  bbox: null
  centroid: null
  countries:
  - AFG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-07-01'
temporal_resolution: null
title: Afghanistan - Damage Assessment in Spera district, Khost province as of 24
  June 2022
version: null
vulnerability: null
---
