---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-gaza-strip-comprehensive-damage-assessment-september-2024
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-gaza-strip-comprehensive-damage-assessment-september-2024
dataset_id: rdls_el-pse_unosat_stripcomprehensivedamagea_20240929
description: 'UNOSAT code: CE20231007PSE This map illustrates a satellite imagery-based
  comprehensive assessment of damage and destruction to structures within the area
  of interest in the Gaza Strip, Occupied Palestinian Territory, based on images collected
  on 3 and 6 September 2024 when compared to images collected on 1 May 2023, 10 May
  2023, 18 September 2023, 15 October 2023, 7 November 2023, 26 November 2023, 6-7
  January 2024, 29 February 2024, 31 March - 1 April 2024, 3 May 2024, and 6 July
  2024. According to satellite imagery analysis, UNOSAT identified 52,564 destroyed
  structures, 18,913 severely damaged structures, 56,710 moderately damaged structures,
  and 35,591 possibly damaged structures for a total of 163,778 structures. These
  correspond to around 66% of the total structures in the Gaza Strip and a total of
  227,591 estimated damaged housing units. The governorates of Khan Yunis and Rafah
  have experienced the highest rise in damage compared to the 6 July 2024 analysis,
  with around 1,470 new structures damaged in Khan Yunis and around 3,770 in Rafah.
  Within Rafah, Rafah City municipality had the highest number of newly damaged structures,
  totalling 3,289. This is a preliminary analysis and has not yet been validated in
  the field.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/unosat-gaza-strip-comprehensive-damage-assessment-september-2024]'
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
    description: Building stock classified by damage state (destroyed, severely damaged,
      moderately damaged, possibly damaged)
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
  description: UNOSAT analysts conducted multi-temporal satellite imagery analysis
    comparing baseline images (May-November 2023) with post-event imagery (January-September
    2024) to identify and classify structural damage across Gaza Strip. Visual interpretation
    of satellite imagery changes was used to categorize buildings into damage states
    (destroyed, severely damaged, moderately damaged, possibly damaged), producing
    a comprehensive damage inventory for humanitarian and operational assessment purposes.
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
- href: https://data.humdata.org/dataset/unosat-gaza-strip-comprehensive-damage-assessment-september-2024
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from conflict-related destruction
      identified through satellite imagery comparison
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
  description: Palestine - UNOSAT Gaza Strip Comprehensive Damage Assessment - September
    2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3984/OCHA-OPT-017_UNOSAT_A3_Gaza_Strip_OPT_CDA_GDB_06092024.zip
  format: Geodatabase
  id: resource_035510e2
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: OCHA-OPT-017_UNOSAT_A3_Gaza_Strip_OPT_CDA_GDB_06092024.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-pse_unosat_stripcomprehensivedamagea_20240929
spatial:
  bbox: null
  centroid: null
  countries:
  - PSE
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-09-29'
temporal_resolution: null
title: Palestine - UNOSAT Gaza Strip Comprehensive Damage Assessment - September 2024
version: null
vulnerability: null
---
