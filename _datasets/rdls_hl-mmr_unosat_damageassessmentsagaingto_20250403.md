---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/damage-assessment-in-sagaing-township-sagaing-district-sagaing-region-myanmar-as-of-30-mar
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-sagaing-township-sagaing-district-sagaing-region-myanmar-as-of-30-mar
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-sagaing-township-sagaing-district-sagaing-region-myanmar-as-of-30-mar
dataset_id: rdls_hl-mmr_unosat_damageassessmentsagaingto_20250403
description: 'UNOSAT code: EQ20250328MMR, GDACS ID: 1474477 This map illustrates the
  potentially damaged structures/buildings affected by the March 28, 2025, earthquake
  in Mandalay. The analysis focuses on a part of Sagaing Township, Sagaing District,
  Sagaing Region, where damage was detected using a Pleiades very high-resolution
  satellite image acquired on March 30, 2025, at 11:01 local time. UNOSAT identified
  233 damaged structures and 557 potentially damaged ones. This is a preliminary analysis
  and has not yet been validated in the field. Please send ground feedback to the
  United Nations Satellite Centre (UNOSAT).. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-in-sagaing-township-sagaing-district-sagaing-region-myanmar-as-of-30-mar]'
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
  description: UNOSAT analysts compared Pleiades satellite imagery acquired on March
    30, 2025 with pre-event reference imagery to detect structural damage caused by
    the March 28, 2025 earthquake in Sagaing Township. Building damage was classified
    into confirmed damaged (233) and potentially damaged (557) categories based on
    visual change detection. This preliminary assessment has not been field-validated.
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
- href: https://data.humdata.org/dataset/damage-assessment-in-sagaing-township-sagaing-district-sagaing-region-myanmar-as-of-30-mar
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: 'Direct building damage from earthquake ground motion: 233 confirmed
      damaged structures and 557 potentially damaged structures detected via satellite
      imagery'
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
  description: Damage Assessment in Sagaing Township, Sagaing District, Sagaing Region,
    Myanmar as of 30 March 2025 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4095/EQ20250328MMR_SHP.zip
  format: null
  id: resource_829f7a47
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20250328MMR_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Damage Assessment in Sagaing Township, Sagaing District, Sagaing Region,
    Myanmar as of 30 March 2025 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4095/EQ20250328MMR_gdb.zip
  format: Geodatabase
  id: resource_3ae6cad6
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20250328MMR_gdb.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-mmr_unosat_damageassessmentsagaingto_20250403
spatial:
  bbox: null
  centroid: null
  countries:
  - MMR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-04-03'
temporal_resolution: null
title: Damage Assessment in Sagaing Township, Sagaing District, Sagaing Region, Myanmar
  as of 30 March 2025
version: null
vulnerability: null
---
