---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-of-gumantar-and-dangiang-desa-kagayan-district-lombok-island-indonesia-2836
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-of-gumantar-and-dangiang-desa-kagayan-district-lombok-island-indonesia-2836
dataset_id: rdls_hl-idn_unosat_damageassessmentgumantard_20180807
description: 'This map illustrates satellite-detected building damage assessment as
  of 7 August 2018, over Gumantar and Dangiang Desa, Kagayan District, Lombok Island,
  after the 6.9 earthquake, 3km SSE of Loloan, Indonesia. The analysis was conducted
  using a post-event Pleiades satellite image acquired as of 7 August 2018, two days
  after the earthquake hit the island. UNITAR-UNOSAT analysis identified 1,274 potentially
  damaged structures within the area. Overall, the satellite detected damage level
  was severe, in this part of the island, especially in Boyotan Asli and Dangian Timur
  villages. This is a preliminary analysis and has not yet been validated in the field.
  Please send ground feedback to UNITAR - UNOSAT.. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/damage-assessment-of-gumantar-and-dangiang-desa-kagayan-district-lombok-island-indonesia-2836]'
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
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts compared post-event Pleiades satellite imagery (7 August
    2018, two days after the 6.9 magnitude earthquake) with reference imagery to identify
    notable structural changes. Building damage was classified by severity level and
    confidence, resulting in a vector dataset of 1,274 potentially damaged structures
    with damage classification attributes across two villages in Kagayan District.
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
- href: https://data.humdata.org/dataset/damage-assessment-of-gumantar-and-dangiang-desa-kagayan-district-lombok-island-indonesia-2836
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from earthquake ground motion, with 1,274
      potentially damaged structures identified in Gumantar and Dangiang Desa
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
  description: Damage assessment of Gumantar and Dangiang Desa, Kagayan District,
    Lombok Island, Indonesia (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/ID/EQ20180805IDN/EQ20180805IDN_shp.zip
  format: null
  id: resource_b30c5f24
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20180805IDN_shp.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-idn_unosat_damageassessmentgumantard_20180807
spatial:
  bbox: null
  centroid: null
  countries:
  - IDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-08-07'
temporal_resolution: null
title: Damage assessment of Gumantar and Dangiang Desa, Kagayan District, Lombok Island,
  Indonesia
version: null
vulnerability: null
---
