---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-of-old-city-mosul-ninawa-governorate-iraq-16-june-2017
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-of-old-city-mosul-ninawa-governorate-iraq-16-june-2017
dataset_id: rdls_el-irq_unosat_damageassessmentoldcitymo_20170706
description: 'This map illustrates satellite-detected damage in Old City, Mosul, Ninawa
  Governorate, Iraq. Using satellite imagery acquired 16 June 2017, UNITAR - UNOSAT
  identified a total of 4,040 affected structures within this part of city. This marks
  an overall increase of 56% in damage affected structures from the assessment five
  days prior on 11 June. Approximately 196 of these were destroyed (5% of the total
  affected buildings), 2,107 severely damaged (52% of the total affected buildings)
  and 1,737 moderately damaged (43% of the total affected buildings). This marks a
  28% increase in destroyed buildings, 17% in moderately damaged buildings and 121%
  severely damaged buildings from the 11 June assessment. The most heavily impacted
  area appears to be the Bab al-Tub neighbourhood (see inset). Due to the densely
  constructed nature of this part of the city, these values might be underestimated.
  This is a preliminary analysis and has not yet been validated in the field. Please
  send ground feedback to UNITAR - UNOSAT.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-of-old-city-mosul-ninawa-governorate-iraq-16-june-2017]'
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
    description: Building stock in Old City, Mosul classified by damage severity (destroyed,
      severely damaged, moderately damaged)
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts reviewed satellite imagery acquired on 16 June 2017
    and compared it with prior imagery from 11 June 2017 to detect structural damage
    in Old City, Mosul. Buildings were classified into three damage categories (destroyed,
    severely damaged, moderately damaged) based on visual interpretation of satellite-detected
    changes, producing a spatial inventory of 4,040 affected structures with damage
    severity classification.
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
- href: https://data.humdata.org/dataset/damage-assessment-of-old-city-mosul-ninawa-governorate-iraq-16-june-2017
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from conflict-related destruction in Old City,
      Mosul
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
  description: Damage assessment of Old City, Mosul, Ninawa Governorate, Iraq (16
    June 2017) (Zipped geodatabase)
  download_url: https://cern.ch/unosat-maps/IQ/CE20140613IRQ/CE20140613IRQ_Mosul_damage_assessment.gdb.zip
  format: Geodatabase
  id: resource_7aeedf38
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20140613IRQ_Mosul_damage_assessment.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Damage assessment of Old City, Mosul, Ninawa Governorate, Iraq (16
    June 2017) (Zipped shapefile)
  download_url: https://cern.ch/unosat-maps/IQ/CE20140613IRQ/CE20140613IRQ_Mosul_damage_assessment_shp.zip
  format: null
  id: resource_5a7889e3
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20140613IRQ_Mosul_damage_assessment_shp.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-irq_unosat_damageassessmentoldcitymo_20170706
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
  start: '2017-07-06'
temporal_resolution: null
title: Damage assessment of Old City, Mosul, Ninawa Governorate, Iraq (16 June 2017)
version: null
vulnerability: null
---
