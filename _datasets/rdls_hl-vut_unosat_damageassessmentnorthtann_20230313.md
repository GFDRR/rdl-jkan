---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/damage-assessment-in-north-tanna-council-tanna-island-tafea-province-vanuatu
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-north-tanna-council-tanna-island-tafea-province-vanuatu
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-north-tanna-council-tanna-island-tafea-province-vanuatu
dataset_id: rdls_hl-vut_unosat_damageassessmentnorthtann_20230313
description: 'UNOSAT code TC20230227VUT, GDACS Id: 1000965 This map illustrates damaged
  and potentially damaged structures and buildings in Tanna Island, Tafea Province
  of Vanuatu as detected using WorldView-2 satellite image acquired on 04 March 2023
  after the passage of Kevin and Judy tropical cyclones. Within the analysed area
  UNOSAT identified 57 damaged and 88 potentially damaged structures. This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to United Nations Satellite Centre (UNOSAT).. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/damage-assessment-in-north-tanna-council-tanna-island-tafea-province-vanuatu]'
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
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts compared WorldView-2 satellite imagery acquired on
    04 March 2023 with pre-event baseline imagery to detect structural damage in North
    Tanna Council following tropical cyclones Kevin and Judy. Damage was classified
    into confirmed damaged (57 structures) and potentially damaged (88 structures)
    categories based on visual interpretation of satellite-detected changes. This
    is a preliminary post-event assessment not yet validated in the field.
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
- href: https://data.humdata.org/dataset/damage-assessment-in-north-tanna-council-tanna-island-tafea-province-vanuatu
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from tropical cyclones Kevin and Judy detected
      via satellite imagery
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
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
  description: Damage Assessment in North Tanna Council, Tanna Island - Tafea Province,
    Vanuatu (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3527/TC20230227VUT_gdb.zip
  format: Geodatabase
  id: resource_c04542d5
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20230227VUT_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Damage Assessment in North Tanna Council, Tanna Island - Tafea Province,
    Vanuatu (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3527/TC20230227VUT_SHP.zip
  format: null
  id: resource_c5060639
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20230227VUT_SHP.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-vut_unosat_damageassessmentnorthtann_20230313
spatial:
  bbox: null
  centroid: null
  countries:
  - VUT
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-03-13'
temporal_resolution: null
title: Damage Assessment in North Tanna Council, Tanna Island - Tafea Province, Vanuatu
version: null
vulnerability: null
---
