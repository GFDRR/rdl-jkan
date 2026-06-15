---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/unosat-fao-gaza-strip-greenhouse-comprehensive-damage-assessment-december-2024
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Food and Agriculture Organization (FAO)
    url: https://data.humdata.org/dataset/unosat-fao-gaza-strip-greenhouse-comprehensive-damage-assessment-december-2024
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-fao-gaza-strip-greenhouse-comprehensive-damage-assessment-december-2024
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-fao-gaza-strip-greenhouse-comprehensive-damage-assessment-december-2024
dataset_id: rdls_el-pse_unosat_statefaostripgreenhouseco_20241223
description: 'UNOSAT code: CE20231007PSE This map a satellite imagery-based comprehensive
  assessment of damage and destruction to greenhouses within the area of interest
  in the Gaza Strip, Occupied Palestinian Territory, based on images collected on
  3 and 23 December 2024 when compared to images collected on 18 August 2024, 23-24
  April 2024, 30-31 March 2024, 23 March 2024, 21 March 2024, 26 November 2023, 7
  November 2023, 24-26 October 2023, 21 October 20223, 15 October 1 May 2023, 10 May
  2023, 18 September 2023, 15 October 2023, 10 October 2023, 18 September 2023, 10
  May 2023, and 1 May 2023. According to satellite imagery analysis, UNOSAT identified
  4,578 destroyed greenhouses, 439 severely damaged greenhouses, and 643 moderately
  damaged greenhouses for a total of 5660 greenhouses. This accounts for approximately
  64% of the total greenhouses in the Gaza Strip, with 33% of these suffering additional
  damage since the previous assessment on 18 August 2024. Furthermore, 6% of the damage
  recorded in December 2024 is new compared to the previous analysis. In terms of
  surface area, 56% of the greenhouse extent is now damaged, reflecting a 37% increase
  compared to the previous analysis. The governorate of Rafah has experienced the
  highest increase in new damage since the 18 August 2024 analysis, with around 838
  new greenhouses affected. Khan Yunis has seen an intensification of previously damaged
  greenhouses, with 703 more greenhouses sustaining further damage. This is a preliminary
  analysis and has not yet been validated in the field.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/unosat-fao-gaza-strip-greenhouse-comprehensive-damage-assessment-december-2024]'
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
    description: Greenhouse structures in the Gaza Strip classified by damage status
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
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
  description: UNOSAT analysts compared satellite imagery acquired on 3 and 23 December
    2024 against baseline images from August 2023 through April 2024 to identify and
    classify greenhouse damage and destruction. Damage assessment was conducted through
    visual interpretation of multi-temporal satellite imagery, with changes in greenhouse
    structure integrity classified into damage categories. The resulting geodatabase
    provides spatial inventory of agricultural asset damage from the conflict.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Food and Agriculture Organization (FAO)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/unosat-fao-gaza-strip-greenhouse-comprehensive-damage-assessment-december-2024
  rel: source
loss:
  losses:
  - asset_category: agriculture
    asset_dimension: product
    description: Direct damage to greenhouse structures from conflict-related destruction
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
          quantity_kind: area
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
  description: State of Palestine - FAO Gaza Strip Greenhouse Comprehensive Damage
    Assessment (UNOSAT) - December 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4073/FAO-PAL-013_UNOSAT_Greenhouse_CDA_GDB_23December2024.zip
  format: Geodatabase
  id: resource_d0df4944
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FAO-PAL-013_UNOSAT_Greenhouse_CDA_GDB_23December2024.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-pse_unosat_statefaostripgreenhouseco_20241223
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
  start: '2024-12-23'
temporal_resolution: null
title: State of Palestine - FAO Gaza Strip Greenhouse Comprehensive Damage Assessment
  (UNOSAT) - December 2024
version: null
vulnerability: null
---
