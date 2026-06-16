---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-of-deir-ez-zor-deir-ez-zor-governorate-syria-2741
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-of-deir-ez-zor-deir-ez-zor-governorate-syria-2741
dataset_id: rdls_el-syr_unosat_damageassessmentdeirezzor_20171128
description: 'This map illustrates satellite-detected damage in a portion of the city
  of Deir Ez Zor, Syrian Arab Republic. Using satellite imagery acquired 9 November
  2017, 25 May 2016, 10 May 2015, 13 May 2014, and 24 October 2013, UNITAR - UNOSAT
  identified a total of 6,348 affected structures within the city. Approximately 1,144
  of these were destroyed, 2,348 severely damaged, and 2,856 moderately damaged. While
  much of the city was damaged by 25 May 2016, 1,859 structures were newly damaged
  and 386 structures experienced an increase in damage between that date and 9 November
  2017. This analysis does not include pre-war military bases and facilities. This
  is a preliminary analysis and has not yet been validated in the field. Please send
  ground feedback to UNITAR - UNOSAT.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-of-deir-ez-zor-deir-ez-zor-governorate-syria-2741]'
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
    description: Building stock in Deir Ez Zor city classified by damage state from
      satellite imagery
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
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts compared satellite imagery acquired on five dates (24
    October 2013, 13 May 2014, 10 May 2015, 25 May 2016, and 9 November 2017) over
    Deir Ez Zor city to identify and classify building damage through visual interpretation
    of structural changes. Buildings were categorized into damage states (destroyed,
    severely damaged, moderately damaged) and temporal changes in damage were tracked
    across the observation period.
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
- href: https://data.humdata.org/dataset/damage-assessment-of-deir-ez-zor-deir-ez-zor-governorate-syria-2741
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from conflict-related destruction
      in Deir Ez Zor
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
  description: Damage assessment of Deir Ez Zor, Deir Ez Zor Governorate, Syria (Zipped
    geodatabase)
  download_url: https://cern.ch/unosat-maps/SY/CE20130604SYR/CE20130604SYR_Raqqa_Deir.gdb.zip
  format: Geodatabase
  id: resource_a6c7da0c
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
  description: Damage assessment of Deir Ez Zor, Deir Ez Zor Governorate, Syria (Zipped
    shapefile)
  download_url: https://cern.ch/unosat-maps/SY/CE20130604SYR/CE20130604SYR_Raqqa_Deir_shp.zip
  format: null
  id: resource_79c2994d
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
slug: rdls_el-syr_unosat_damageassessmentdeirezzor_20171128
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
  start: '2017-11-28'
temporal_resolution: null
title: Damage assessment of Deir Ez Zor, Deir Ez Zor Governorate, Syria
version: null
vulnerability: null
---
