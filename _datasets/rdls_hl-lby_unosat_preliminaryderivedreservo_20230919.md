---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/preliminary-satellite-derived-reservoir-assessment-benghazi-almarj-derna-governorates-east
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/preliminary-satellite-derived-reservoir-assessment-benghazi-almarj-derna-governorates-east
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/preliminary-satellite-derived-reservoir-assessment-benghazi-almarj-derna-governorates-east
dataset_id: rdls_hl-lby_unosat_preliminaryderivedreservo_20230919
description: 'UNOSAT code FL20230912LBY, GDACS Id: 1102204 Status: increased water
  observed Further action(s): continue monitoring Wadi Qattarra Dam 1 & 2 appears
  to be filled as of 16 September 2023; Wadi Jaza dam appears to be filled as of 15
  September 2023; Increased water observed in Al Marj dam as of 15 September 2023;
  Both Derna dams destroyed by rushing flood waters.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/preliminary-satellite-derived-reservoir-assessment-benghazi-almarj-derna-governorates-east]'
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
    flood:
    - analysis_type: probabilistic
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
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts reviewed and compared satellite imagery acquired before
    and after the September 2023 flooding event in East Libya to assess reservoir
    water levels and identify infrastructure damage. The analysis produced geospatial
    datasets documenting increased water in multiple dams and destruction of Derna
    dam infrastructure, with confidence levels and validation fields recorded for
    each observation.
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
- href: https://data.humdata.org/dataset/preliminary-satellite-derived-reservoir-assessment-benghazi-almarj-derna-governorates-east
  rel: source
loss:
  losses:
  - asset_category: infrastructure
    asset_dimension: structure
    description: Direct destruction of Derna dams by flood waters; damage assessment
      of reservoir infrastructure
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
  description: Preliminary satellite-derived reservoir assessment, Benghazi, Almarj
    & Derna governorates, East province, Libya - 19 September 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3675/FL20230912LBY_gdb.zip
  format: Geodatabase
  id: resource_c8f425d4
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230912LBY_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Preliminary satellite-derived reservoir assessment, Benghazi, Almarj
    & Derna governorates, East province, Libya - 19 September 2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3675/FL20230912LBY_SHP.zip
  format: null
  id: resource_a8db064c
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230912LBY_SHP.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-lby_unosat_preliminaryderivedreservo_20230919
spatial:
  bbox: null
  centroid: null
  countries:
  - LBY
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-09-19'
temporal_resolution: null
title: Preliminary satellite-derived reservoir assessment, Benghazi, Almarj & Derna
  governorates, East province, Libya - 19 September 2023
version: null
vulnerability: null
---
