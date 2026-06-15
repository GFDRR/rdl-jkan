---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-ramadi-al-anbar-province-iraq-january-22-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-ramadi-al-anbar-province-iraq-january-22-2015
dataset_id: rdls_el-irq_unosat_geodatadamageassessmentra_20150122
description: 'This map illustrates satellite-detected damage and destruction in a
  portion of the city of Ramadi, Al Anbar Province, Iraq. Using satellite imagery
  acquired 02 December, 11 November and 06 July 2014, UNOSAT identified a total of
  168 affected structures within the area of this map. Approximatively 61 of these
  were destroyed, 24 severely damaged and 83 moderately damaged. The city-wide analysis
  of Ramadi revealed a total of 208 affected structures, of which 72 were destroyed,
  33 severely damaged and 103 moderately damaged. This is a preliminary analysis and
  has not yet been validated in the field. Please send ground feedback to UNITAR /
  UNOSAT.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-ramadi-al-anbar-province-iraq-january-22-2015]'
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
    description: Building stock in Ramadi classified by damage severity from satellite
      imagery
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
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: UNOSAT analysts compared satellite imagery acquired on 02 December,
    11 November, and 06 July 2014 to identify structural damage through visual interpretation
    of notable changes between images. Buildings were classified into three damage
    categories (destroyed, severely damaged, moderately damaged) based on satellite-detected
    changes, producing a preliminary damage assessment dataset without field validation.
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
- href: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-ramadi-al-anbar-province-iraq-january-22-2015
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from conflict-related destruction
      in Ramadi
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
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
  description: Geodata of Damage Assessment of Ramadi, Al Anbar Province, Iraq (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/IQ/CE20140613IRQ/CE20140613IRQ_Ramadi_shp.zip
  format: null
  id: resource_0b034301
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20140613IRQ_Ramadi_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Damage Assessment of Ramadi, Al Anbar Province, Iraq (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/IQ/CE20140613IRQ/CE20140613IRQ_Ramadi.gdb.zip
  format: null
  id: resource_6f83a479
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20140613IRQ_Ramadi.gdb.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-irq_unosat_geodatadamageassessmentra_20150122
spatial:
  bbox: null
  centroid: null
  countries:
  - IRQ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-01-22'
temporal_resolution: null
title: Geodata of Damage Assessment of Ramadi, Al Anbar Province, Iraq
version: null
vulnerability: null
---
