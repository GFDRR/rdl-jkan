---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/damage-assessment-in-jindires-and-the-surrounding-area-syria-as-of-10-february-2023
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-jindires-and-the-surrounding-area-syria-as-of-10-february-2023
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-jindires-and-the-surrounding-area-syria-as-of-10-february-2023
dataset_id: rdls_hl-syr_unosat_damageassessmentjindiress_20230214
description: 'UNOSAT code EQ20230206SYR, GDACS Id: 1357372 This map illustrates the
  potentially damaged structures/buildings affected by the 10h of February 2023 earthquake
  in Jindires and in the surrounding area in Afrin district (Aleppo governorate),
  Syria as detected from a Pleiades very highresolution satellite image acquired on
  10 February 2023. Within the 17 locations (including the city of Jindires), UNOSAT
  identified 310 damaged structures and 470 potentially damaged. This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to United Nations Satellite Centre (UNOSAT).. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/damage-assessment-in-jindires-and-the-surrounding-area-syria-as-of-10-february-2023]'
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
  event_sets_by_hazard_type:
    earthquake:
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
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts reviewed Pleiades satellite imagery acquired on 10
    February 2023 and compared it with reference imagery to detect structural damage
    in Jindires and surrounding areas. Building damage was classified into confirmed
    damaged (310 structures) and potentially damaged (470 structures) categories across
    17 locations in Afrin district. This is a preliminary satellite-based assessment
    not yet validated through field surveys.
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
- href: https://data.humdata.org/dataset/damage-assessment-in-jindires-and-the-surrounding-area-syria-as-of-10-february-2023
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: 'Direct building damage from the 10 February 2023 earthquake: 310
      confirmed damaged structures and 470 potentially damaged structures detected
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
  description: Damage Assessment in Jindires and the surrounding area, Syria as of
    10 February 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3496/EQ20230206SYR_gdb.zip
  format: Geodatabase
  id: resource_d3b751ae
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
  description: Damage Assessment in Jindires and the surrounding area, Syria as of
    10 February 2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3496/EQ20230206SYR_SHP.zip
  format: null
  id: resource_0eb5e372
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
slug: rdls_hl-syr_unosat_damageassessmentjindiress_20230214
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
  start: '2023-02-14'
temporal_resolution: null
title: Damage Assessment in Jindires and the surrounding area, Syria as of 10 February
  2023
version: null
vulnerability: null
---
