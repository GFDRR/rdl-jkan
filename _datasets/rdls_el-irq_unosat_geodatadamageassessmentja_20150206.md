---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-jalawla-diyala-governorate-iraq-february-06-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-jalawla-diyala-governorate-iraq-february-06-2015
dataset_id: rdls_el-irq_unosat_geodatadamageassessmentja_20150206
description: 'This map illustrates satellite-detected damage and destruction in the
  city of Jalawla, Diyala Governorate, Iraq. Using satellite imagery acquired 20 January
  2015 and 23 June 2014, UNITAR / UNOSAT identified a total of 1,771 affected structures.
  Approximately 395 of these were destroyed, 678 severely damaged, and 698 moderately
  damaged. This is a preliminary analysis and has not yet been validated in the field.
  Please send ground feedback to UNITAR / UNOSAT.. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/geodata-of-damage-assessment-of-jalawla-diyala-governorate-iraq-february-06-2015]'
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
    description: Building stock in Jalawla classified by damage severity from satellite
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
  description: UNOSAT analysts compared satellite imagery acquired on 23 June 2014
    and 20 January 2015 of Jalawla, Diyala Governorate to detect structural damage
    through visual change detection. Building damage was classified into three categories
    (destroyed, severely damaged, moderately damaged) based on satellite-observed
    structural changes, resulting in a spatial inventory of 1,771 affected structures.
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
- href: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-jalawla-diyala-governorate-iraq-february-06-2015
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from conflict-related destruction
      in Jalawla
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
  description: Geodata of Damage Assessment of Jalawla, Diyala Governorate, Iraq (Shapefile)
  download_url: https://cern.ch/unosat-maps/IQ/CE20140613IRQ/CE20140613IRQ_Jalawla_shp.zip
  format: null
  id: resource_c5ebf19b
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20140613IRQ_Jalawla_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Damage Assessment of Jalawla, Diyala Governorate, Iraq (Shapefile)
  download_url: https://cern.ch/unosat-maps/IQ/CE20140613IRQ/CE20140613IRQ_Jalawla.gdb.zip
  format: null
  id: resource_30680ebb
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20140613IRQ_Jalawla.gdb.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-irq_unosat_geodatadamageassessmentja_20150206
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
  start: '2015-02-06'
temporal_resolution: null
title: Geodata of Damage Assessment of Jalawla, Diyala Governorate, Iraq
version: null
vulnerability: null
---
