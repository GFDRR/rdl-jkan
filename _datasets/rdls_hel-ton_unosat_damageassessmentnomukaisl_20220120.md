---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/damage-assessment-in-nomuka-island-mu-omu-a-district-ha-apai-division-tonga-as-of-18-janua
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-nomuka-island-mu-omu-a-district-ha-apai-division-tonga-as-of-18-janua
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-nomuka-island-mu-omu-a-district-ha-apai-division-tonga-as-of-18-janua
dataset_id: rdls_hel-ton_unosat_damageassessmentnomukaisl_20220120
description: 'UNOSAT code: VO20220115TON This map illustrates the impact of the Hunga
  Tonga-hunga Ha''apai volcanic eruption and the subsequent in Nomuka island (Mu''omu''a
  district, Tonga) and damage assessment as detected from a Pleiades image acquired
  on 18 January 2022, 10:45 local time. In this island, UNOSAT identified 260 structures.
  52 structures were identified as damaged and/or destroyed, 13 as potentially flooded
  and almost all the structures were covered with ash. This is a preliminary analysis
  and has not yet been validated in the field. Please send ground feedback to UNITAR-UNOSAT..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-in-nomuka-island-mu-omu-a-district-ha-apai-division-tonga-as-of-18-janua]'
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
    description: Building stock inventory on Nomuka Island identified from satellite
      imagery (260 structures total)
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
      intensity_measure: h_vaf:mm
      process: ashfall
      trigger: null
      type: volcanic
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts performed multi-temporal satellite image analysis comparing
    pre- and post-eruption Pleiades imagery acquired on 18 January 2022 to detect
    structural damage, flooding impacts, and ash coverage on Nomuka Island. Building
    footprints were identified and classified by damage state (damaged/destroyed,
    potentially flooded, ash-covered) through visual interpretation of high-resolution
    satellite data.
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
- href: https://data.humdata.org/dataset/damage-assessment-in-nomuka-island-mu-omu-a-district-ha-apai-division-tonga-as-of-18-janua
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage and destruction from volcanic eruption (52
      structures damaged/destroyed)
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_volcanic
      intensity_measure: h_vaf:mm
      process: null
      trigger: null
      type: volcanic
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
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from tsunami/coastal flooding (13 structures
      potentially flooded)
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: coastal_flood
      trigger: null
      type: flood
    id: loss_2
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
  description: Damage assessment in Nomuka Island, Mu'omu'a district, Ha'apai division,Tonga
    as of 18 January 2022 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/TO/VO20220115TON/VO20220115TON_gdb.zip
  format: Geodatabase
  id: resource_2e5cebda
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VO20220115TON_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Damage assessment in Nomuka Island, Mu'omu'a district, Ha'apai division,Tonga
    as of 18 January 2022 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/TO/VO20220115TON/VO20220115TON_SHP.zip
  format: null
  id: resource_17c0063f
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VO20220115TON_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-ton_unosat_damageassessmentnomukaisl_20220120
spatial:
  bbox: null
  centroid: null
  countries:
  - TON
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-01-20'
temporal_resolution: null
title: Damage assessment in Nomuka Island, Mu'omu'a district, Ha'apai division,Tonga
  as of 18 January 2022
version: null
vulnerability: null
---
