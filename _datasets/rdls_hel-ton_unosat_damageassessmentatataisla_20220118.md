---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/damage-assessment-in-atata-island-kolovao-district-tongatapu-division-tonga-as-of-18-janua
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-atata-island-kolovao-district-tongatapu-division-tonga-as-of-18-janua
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-atata-island-kolovao-district-tongatapu-division-tonga-as-of-18-janua
dataset_id: rdls_hel-ton_unosat_damageassessmentatataisla_20220118
description: 'UNOSAT code: VO20220115TON This map illustrates impact of the Hunga
  Tonga-hunga Ha''apai volcanic eruption and subsequent tsunami in the Atata island
  (Kolovao district, Tonga) and the related damage assessment as detected from a Pleiades
  image acquired on 18 January 2022, 19:45 local time. Within this island, UNOSAT
  identified 72 structures as damaged, 28 structures as potentially damaged. Furthermore,
  the entire island appears to be covered with volcanic ash. This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to the United Nations Satellite Centre (UNOSAT).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/damage-assessment-in-atata-island-kolovao-district-tongatapu-division-tonga-as-of-18-janua]'
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
    description: Building structures on Atata Island identified and classified by
      damage status from satellite imagery
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
  description: UNOSAT analysts reviewed Pleiades satellite imagery acquired on 18
    January 2022 to detect post-event damage on Atata Island following the 15 January
    2022 Hunga Tonga-Hunga Ha'apai volcanic eruption and subsequent tsunami. Damage
    assessment was conducted through visual interpretation and comparison of satellite
    images, identifying 72 damaged structures, 28 potentially damaged structures,
    and widespread volcanic ash coverage. This is a preliminary remote-sensing-based
    assessment not yet validated through field surveys.
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
- href: https://data.humdata.org/dataset/damage-assessment-in-atata-island-kolovao-district-tongatapu-division-tonga-as-of-18-janua
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from volcanic eruption and ashfall on Atata
      Island (72 confirmed damaged, 28 potentially damaged)
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
    description: Direct building damage from tsunami triggered by volcanic eruption
      on Atata Island
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_tsunami
      intensity_measure: wd:m
      process: null
      trigger: null
      type: tsunami
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
  description: Damage assessment in Atata Island, Kolovao district, Tongatapu division,
    Tonga as of 18 January 2022 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/TO/VO20220115TON/VO20220115TON_gdb.zip
  format: Geodatabase
  id: resource_286c6b5d
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
  description: Damage assessment in Atata Island, Kolovao district, Tongatapu division,
    Tonga as of 18 January 2022 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/TO/VO20220115TON/VO20220115TON_SHP.zip
  format: null
  id: resource_23026a79
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
slug: rdls_hel-ton_unosat_damageassessmentatataisla_20220118
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
  start: '2022-01-18'
temporal_resolution: null
title: Damage assessment in Atata Island, Kolovao district, Tongatapu division, Tonga
  as of 18 January 2022
version: null
vulnerability: null
---
