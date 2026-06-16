---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/infrastructure-and-roads-damage-assessment-of-deir-ez-zor-deir-ez-zor-governorate-syria-2748
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/infrastructure-and-roads-damage-assessment-of-deir-ez-zor-deir-ez-zor-governorate-syria-2748
dataset_id: rdls_el-syr_unosat_infrastructureroadsdamage_20171211
description: 'This map illustrates satellite-detected damage to infrastructure and
  roads in a portion of the city of Deir Ez Zor, Syrian Arab Republic and is derived
  from a full UNOSAT analysis of damage to Deir Ez Zor in 2017. Using satellite imagery
  acquired 9 November 2017, UNITAR - UNOSAT identified 6 destroyed bridges, 54 damaged
  road segments and 93 visible impact craters affecting roads. Approximately 169 structures
  corresponding to educational facilities, and 21 structures likely related to health
  facilities are also affected. UNOSAT analysis shows that there are 3 destroyed electricity
  towers south of the city. Note that sources of infrastructure data include various
  open source datasets which are likely incomplete, as well as visual review of satellite
  imagery by UNOSAT for certain features like towers. This is a preliminary analysis
  and has not yet been validated in the field. Please send ground feedback to UNITAR
  - UNOSAT.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/infrastructure-and-roads-damage-assessment-of-deir-ez-zor-deir-ez-zor-governorate-syria-2748]'
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
    description: Road segments and bridges in Deir Ez Zor city
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Educational and health facility structures
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts reviewed satellite imagery acquired on 9 November 2017
    and compared it with prior imagery to detect notable changes and damage signatures.
    Damage assessment methodology involved visual interpretation of satellite imagery
    to identify destroyed/damaged infrastructure (bridges, roads, electricity towers)
    and affected facilities (schools, health centers), with results compiled into
    geospatial vector datasets.
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
- href: https://data.humdata.org/dataset/infrastructure-and-roads-damage-assessment-of-deir-ez-zor-deir-ez-zor-governorate-syria-2748
  rel: source
loss:
  losses:
  - asset_category: infrastructure
    asset_dimension: structure
    description: Direct damage to road segments and bridges from conflict-related
      impacts
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
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: Direct damage to educational and health facilities from conflict-related
      impacts
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
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
  description: Infrastructure and roads damage assessment of Deir Ez Zor, Deir Ez
    Zor Governorate, Syria (Zipped geodatabase)
  download_url: https://cern.ch/unosat-maps/SY/CE20130604SYR/CE20130604SYR_Raqqa_Deir.gdb.zip
  format: Geodatabase
  id: resource_03860c1a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20130604SYR_Raqqa_Deir.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Infrastructure and roads damage assessment of Deir Ez Zor, Deir Ez
    Zor Governorate, Syria (Zipped shapefile)
  download_url: https://cern.ch/unosat-maps/SY/CE20130604SYR/CE20130604SYR_Raqqa_Deir_shp.zip
  format: null
  id: resource_94cffaa7
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20130604SYR_Raqqa_Deir_shp.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-syr_unosat_infrastructureroadsdamage_20171211
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
  start: '2017-12-11'
temporal_resolution: null
title: Infrastructure and roads damage assessment of Deir Ez Zor, Deir Ez Zor Governorate,
  Syria
version: null
vulnerability: null
---
