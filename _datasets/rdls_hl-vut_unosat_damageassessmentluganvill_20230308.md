---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/damage-assessment-in-luganville-and-south-east-santo-councils-espiritu-santo-island-sanma-
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-luganville-and-south-east-santo-councils-espiritu-santo-island-sanma-
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-luganville-and-south-east-santo-councils-espiritu-santo-island-sanma-
dataset_id: rdls_hl-vut_unosat_damageassessmentluganvill_20230308
description: 'UNOSAT code TC20230227VUT, GDACS Id: 1000965 This map illustrates damaged
  and potentially damaged structures and buildings in Luganville and South East Santo
  Councils of Vanuatu as detected using Pleiades satellite images acquired on 04 &
  06 March 2023 after the passage of Kevin and Judy tropical cyclones. Within the
  analysed area UNOSAT identified 46 damaged and/or potentially damaged structures.
  This is a preliminary analysis and has not yet been validated in the field. Please
  send ground feedback to United Nations Satellite Centre (UNOSAT).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-in-luganville-and-south-east-santo-councils-espiritu-santo-island-sanma-]'
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
    strong_wind:
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
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts compared Pleiades satellite images acquired on 04 and
    06 March 2023 (post-cyclone) with baseline imagery to detect structural damage
    in Luganville and South East Santo Councils. Damaged and potentially damaged buildings
    were identified through visual interpretation of notable changes between images,
    resulting in a preliminary assessment of 46 affected structures with confidence
    levels and validation status recorded.
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
- href: https://data.humdata.org/dataset/damage-assessment-in-luganville-and-south-east-santo-councils-espiritu-santo-island-sanma-
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
  description: Vanuatu - Damage Assessment in Luganville and South East Santo Councils,
    Espiritu Santo Island - Sanma Province (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3524/TC20230227VUT.gdb.zip
  format: Geodatabase
  id: resource_fb548f23
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20230227VUT.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Vanuatu - Damage Assessment in Luganville and South East Santo Councils,
    Espiritu Santo Island - Sanma Province (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3524/TC20230227VUT_SHP.zip
  format: null
  id: resource_b829b60e
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
slug: rdls_hl-vut_unosat_damageassessmentluganvill_20230308
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
  start: '2023-03-08'
temporal_resolution: null
title: Vanuatu - Damage Assessment in Luganville and South East Santo Councils, Espiritu
  Santo Island - Sanma Province
version: null
vulnerability: null
---
