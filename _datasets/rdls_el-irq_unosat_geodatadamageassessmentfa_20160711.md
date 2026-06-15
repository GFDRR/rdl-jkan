---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-fallujah-al-anbar-province-iraq-july-11-2016
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-fallujah-al-anbar-province-iraq-july-11-2016
dataset_id: rdls_el-irq_unosat_geodatadamageassessmentfa_20160711
description: 'This map illustrates satellite-detected damage and destruction in the
  city of Fallujah, Al Anbar Province, Iraq. Using satellite imagery acquired 28 and
  29 June 2016, UNOSAT identified 491 destroyed structures, 300 severely damaged structures,
  and 453 moderately damaged structure. This latest analysis, combined with a previous
  UNOSAT analysis (done using an image from 30 November 2014), indicates a total of
  1,422 destroyed structures (an increase of 53% from 2014), 604 severely damaged
  structures (an increase of 99% from 2014), and 578 moderately damaged structures
  (an increase of 362% from 2014). The total number of destroyed or damaged structures
  therefore increased from 1,360 to 3,964, an increase of 191%. This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to UNITAR - UNOSAT.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-fallujah-al-anbar-province-iraq-july-11-2016]'
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
    description: Building stock in Fallujah and Al Anbar classified by damage severity
      (destroyed, severely damaged, moderately damaged)
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
  description: UNOSAT analysts reviewed and compared multi-temporal satellite imagery
    (June 2016 and November 2014) of Fallujah to identify and classify building damage
    through visual interpretation. Structures were categorized into three damage classes
    (destroyed, severely damaged, moderately damaged) and georeferenced as point or
    polygon features with confidence levels and validation flags.
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
- href: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-fallujah-al-anbar-province-iraq-july-11-2016
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from conflict-related destruction
      in Fallujah
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
  description: Iraq - Geodata of Damage Assessment for Fallujah and Al Anbar Provinces
    (Shapefile)
  download_url: https://cern.ch/unosat-maps/IQ/CE20140613IRQ/CE20140613IRQ_Fallujah_shp.zip
  format: null
  id: resource_be918efc
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20140613IRQ_Fallujah_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Iraq - Geodata of Damage Assessment for Fallujah and Al Anbar Provinces
    (Shapefile)
  download_url: https://cern.ch/unosat-maps/IQ/CE20140613IRQ/CE20140613IRQ_Fallujah_gdb.zip
  format: null
  id: resource_73748c45
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20140613IRQ_Fallujah_gdb.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-irq_unosat_geodatadamageassessmentfa_20160711
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
  start: '2016-07-11'
temporal_resolution: null
title: Iraq - Geodata of Damage Assessment for Fallujah and Al Anbar Provinces
version: null
vulnerability: null
---
