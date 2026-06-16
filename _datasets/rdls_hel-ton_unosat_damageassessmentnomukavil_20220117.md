---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/damage-assessment-in-nomuka-village-mu-omu-a-district-ha-apai-division-nomuka-island-as-of
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-nomuka-village-mu-omu-a-district-ha-apai-division-nomuka-island-as-of
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-nomuka-village-mu-omu-a-district-ha-apai-division-nomuka-island-as-of
dataset_id: rdls_hel-ton_unosat_damageassessmentnomukavil_20220117
description: 'UNOSAT code: VO20220115TON This map illustrates effects of the Hunga
  Tonga-hunga Ha''apai volcanic eruption in Nomuka island (Mu''omu''a district, Tonga)
  and damage assessment as detected from a Pleiades image acquired on 17 January 2022,
  10:53 local time. In this island we identified~250 structures. 104 structures were
  analyzed in the cloud-free area and 41 structures were identified as damaged and
  almost all the structures were covered with ash. This is a preliminary analysis
  and has not yet been validated in the field. Please send ground feedback to UNITAR-UNOSAT..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-in-nomuka-village-mu-omu-a-district-ha-apai-division-nomuka-island-as-of]'
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
    description: Building stock in Nomuka village identified from satellite imagery,
      approximately 250 structures total
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
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts reviewed Pleiades satellite imagery acquired on 17
    January 2022 following the Hunga Tonga-Hunga Ha'apai volcanic eruption, comparing
    multi-temporal images to detect changes in building condition and ashfall coverage.
    Damage assessment was conducted through visual interpretation of the cloud-free
    area covering 104 structures, identifying 41 damaged buildings and widespread
    ash deposition across the island.
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
- href: https://data.humdata.org/dataset/damage-assessment-in-nomuka-village-mu-omu-a-district-ha-apai-division-nomuka-island-as-of
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from volcanic ashfall, with 41 structures
      identified as damaged out of 104 analyzed in cloud-free areas
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
  description: Tonga - Damage assessment in Nomuka village, Mu'omu'a district, Ha'apai
    division, Nomuka Island, as of 17 January 2022 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/TO/VO20220115TON/VO20220115TON_gdb.zip
  format: Geodatabase
  id: resource_8a2f8e90
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
  description: Tonga - Damage assessment in Nomuka village, Mu'omu'a district, Ha'apai
    division, Nomuka Island, as of 17 January 2022 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/TO/VO20220115TON/VO20220115TON_SHP.zip
  format: null
  id: resource_4cd6e756
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
slug: rdls_hel-ton_unosat_damageassessmentnomukavil_20220117
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
  start: '2022-01-17'
temporal_resolution: null
title: Tonga - Damage assessment in Nomuka village, Mu'omu'a district, Ha'apai division,
  Nomuka Island, as of 17 January 2022
version: null
vulnerability: null
---
