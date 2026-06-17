---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/damage-assessment-in-ohonua-town-eua-prope-district-eua-division-tonga-as-of-20-21-january
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-ohonua-town-eua-prope-district-eua-division-tonga-as-of-20-21-january
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-ohonua-town-eua-prope-district-eua-division-tonga-as-of-20-21-january
dataset_id: rdls_hel-ton_unosat_damageassessmentohonuatow_20220121
description: 'UNOSAT code: VO20220115TON This map illustrates the impact of the Hunga
  Tonga-hunga Ha''apai volcanic eruption and the subsequent tsunami in ''Ohonoua town
  (''Eua Prope district, Tonga) and damage assessment as detected from Pleiades images
  acquired on 20 January 2022 at 11:20 local time and 21 January 2022 at 11:13 local
  time. Among the 2,028 structures were identified, of which 1,231 structures are
  in cloud-free areas. Amongst the analyzed 1,231 structures, 54 were identified as
  damaged or destroyed, three as potentially damaged structures, and 1,174 buildings
  appeared without any visible damage from space imagery analysis. Six road obstacles
  were also identified in the cloud-free areas. This is a preliminary analysis and
  has not yet been validated in the field. Please send ground feedback to the United
  Nations Satellite Centre (UNOSAT).. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-in-ohonua-town-eua-prope-district-eua-division-tonga-as-of-20-21-january]'
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
    description: Building stock in 'Ohonua town identified from satellite imagery,
      comprising 2,028 structures of which 1,231 were in cloud-free areas
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
  type: volcanic
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts compared multi-temporal Pleiades satellite imagery
    (20-21 January 2022) of 'Ohonua town to detect structural changes and damage from
    the Hunga Tonga-Hunga Ha'apai volcanic eruption and subsequent tsunami. Building
    footprints were identified and classified as damaged, potentially damaged, or
    undamaged based on visual interpretation of satellite imagery.
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
- href: https://data.humdata.org/dataset/damage-assessment-in-ohonua-town-eua-prope-district-eua-division-tonga-as-of-20-21-january
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: 'Direct building damage from volcanic eruption and tsunami: 54 destroyed/damaged
      and 3 potentially damaged structures'
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
  description: Damage assessment in 'Ohonua town, 'Eua Prope district, 'Eua division,
    Tonga as of 20 & 21 January 2022 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/TO/VO20220115TON/VO20220115TON_gdb.zip
  format: Geodatabase
  id: resource_e9e1bc34
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
  description: Damage assessment in 'Ohonua town, 'Eua Prope district, 'Eua division,
    Tonga as of 20 & 21 January 2022 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/TO/VO20220115TON/VO20220115TON_SHP.zip
  format: null
  id: resource_8bf7e296
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
slug: rdls_hel-ton_unosat_damageassessmentohonuatow_20220121
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
  start: '2022-01-21'
temporal_resolution: null
title: Damage assessment in 'Ohonua town, 'Eua Prope district, 'Eua division, Tonga
  as of 20 & 21 January 2022
version: null
vulnerability: null
---
