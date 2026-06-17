---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-killi-idlib-district-syria-as-of-16-february-2023
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-killi-idlib-district-syria-as-of-16-february-2023
dataset_id: rdls_hl-syr_unosat_damageassessmentkilliidli_20230306
description: 'UNOSAT code EQ20230206SYR, GDACS Id: 1357372 This map illustrates the
  potentially damaged structures/buildings affected by the 6th of February 2023 earthquake
  in Killi in Idlib district (Aleppo governorate), Syria as detected from a Pleiades
  very highresolution satellite image acquired on 16 February 2023. UNOSAT 11 potentially
  damaged structures. This is a preliminary analysis and has not yet been validated
  in the field. Please send ground feedback to United Nations Satellite Centre (UNOSAT)..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-in-killi-idlib-district-syria-as-of-16-february-2023]'
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
  - analysis_type: probabilistic
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
  description: UNOSAT analysts performed visual interpretation and change detection
    analysis on Pleiades satellite imagery acquired 16 February 2023 to identify structural
    damage from the 6 February 2023 earthquake in Killi. Potentially damaged buildings
    were mapped as vector features with area measurements. This is a preliminary assessment
    not yet validated in the field.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/damage-assessment-in-killi-idlib-district-syria-as-of-16-february-2023
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from the 6 February 2023 earthquake
      detected via satellite imagery in Killi, Idlib
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
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
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
  description: Damage Assessment in Killi (Idlib District), Syria as of 16 February
    2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3516/EQ20230206SYR_gdb.zip
  format: Geodatabase
  id: resource_6d8ed490
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20230206SYR_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Damage Assessment in Killi (Idlib District), Syria as of 16 February
    2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3516/EQ20230206SYR_SHP.zip
  format: null
  id: resource_90ff2442
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20230206SYR_SHP.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-syr_unosat_damageassessmentkilliidli_20230306
spatial:
  bbox: null
  centroid: null
  countries:
  - SYR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-03-06'
temporal_resolution: null
title: Damage Assessment in Killi (Idlib District), Syria as of 16 February 2023
version: null
vulnerability: null
---
