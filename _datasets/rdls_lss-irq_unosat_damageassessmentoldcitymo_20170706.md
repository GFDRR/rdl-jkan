---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-of-old-city-mosul-ninawa-governorate-iraq-11-june-2017
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-of-old-city-mosul-ninawa-governorate-iraq-11-june-2017
dataset_id: rdls_lss-irq_unosat_damageassessmentoldcitymo_20170706
description: 'This map illustrates satellite-detected damage in Old City, Mosul, Ninawa
  Governorate, Iraq. Using satellite imagery acquired 11 June 2017, UNITAR - UNOSAT
  identified a total of 2,589 affected structures within this part of city. Approximately
  153 (6% of the total affected buildings) of these were destroyed, 950 (37% of the
  total affected buildings) severely damaged and 1,486 (57% of the total affected
  buildings) moderately damaged. The most heavily impacted location appears to be
  the Bazaar area (see inset). Due to the densely constructed nature of this part
  of the city, these values might be underestimated. This is a preliminary analysis
  and has not yet been validated in the field. Please send ground feedback to UNITAR
  - UNOSAT.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-of-old-city-mosul-ninawa-governorate-iraq-11-june-2017]'
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
hazard: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts reviewed satellite imagery acquired on 11 June 2017
    and compared multi-temporal images to detect notable changes in building structures.
    Damage was classified into three categories (destroyed, severely damaged, moderately
    damaged) through visual interpretation of satellite-detected structural changes
    in the Old City of Mosul.
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
- href: https://data.humdata.org/dataset/damage-assessment-of-old-city-mosul-ninawa-governorate-iraq-11-june-2017
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from conflict-related destruction
      in Old City Mosul
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
  description: Damage assessment of Old City, Mosul, Ninawa Governorate, Iraq (11
    June 2017) (Zipped geodatabase)
  download_url: https://cern.ch/unosat-maps/IQ/CE20140613IRQ/CE20140613IRQ_Mosul_damage_assessment.gdb.zip
  format: Geodatabase
  id: resource_4585b0c0
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
  description: Damage assessment of Old City, Mosul, Ninawa Governorate, Iraq (11
    June 2017) (Zipped shapefile)
  download_url: https://cern.ch/unosat-maps/IQ/CE20140613IRQ/CE20140613IRQ_Mosul_damage_assessment_shp.zip
  format: null
  id: resource_05028f3c
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20140613IRQ_Mosul_damage_assessment_shp.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-irq_unosat_damageassessmentoldcitymo_20170706
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
title: Damage assessment of Old City, Mosul, Ninawa Governorate, Iraq (11 June 2017)
version: null
vulnerability: null
---
