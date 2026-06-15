---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/unosat-gaza-strip-comprehensive-damage-assessment-7-november-2023
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-gaza-strip-comprehensive-damage-assessment-7-november-2023
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-gaza-strip-comprehensive-damage-assessment-7-november-2023
dataset_id: rdls_el-pse_unosat_stripcomprehensivedamagea_20231113
description: 'UNOSAT code CE20231007PSE This map illustrates a satellite-imagery based
  comprehensive damage assessment to detect damage and destruction to structures within
  the area of interest in the Gaza Strip, Occupied Palestinian Territory, based on
  an image collected on 7 November 2023 when compared to images collected on 1 May
  2023, 10 May 2023, 18 September 2023, and 15 October 2023. According to satellite
  imagery analysis, UNOSAT identified 6,583 destroyed structures, 6,062 severely damaged
  structures and 12,405 moderately damaged structures, for a total of 25,050 structures.
  This corresponds to approximately 10 per cent of the total structures in the Gaza
  Strip. The areas most affected by damage are the governorates of North Gaza and
  Gaza. Between 15 October and 7 November, there was an increase in the number of
  damaged buildings by approximately 137 per cent. From 15 October to 7 November 2023,
  the neighborhood of Al Qaraya al Badawiya al Maslakh in North Gaza has seen a notable
  increase in damage (see inset 1). This is a preliminary analysis and has not yet
  been validated in the field.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/unosat-gaza-strip-comprehensive-damage-assessment-7-november-2023]'
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
    description: Building stock classified by damage severity (destroyed, severely
      damaged, moderately damaged)
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
  description: UNOSAT analysts compared satellite imagery from 7 November 2023 against
    baseline images from May, September, and October 2023 to detect structural damage
    through visual interpretation. Buildings were classified into three damage categories
    (destroyed, severely damaged, moderately damaged) based on observable changes
    in satellite imagery, producing a comprehensive post-event damage inventory.
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
- href: https://data.humdata.org/dataset/unosat-gaza-strip-comprehensive-damage-assessment-7-november-2023
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from conflict-related destruction
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
  description: Palestine - UNOSAT Gaza Strip Comprehensive Damage Assessment - 7 November
    2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3734/UNOSAT_GazaStrip_CDA_07Nov2023_GDB.zip
  format: Geodatabase
  id: resource_e2d40247
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_GazaStrip_CDA_07Nov2023_GDB.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-pse_unosat_stripcomprehensivedamagea_20231113
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
  start: '2023-11-13'
temporal_resolution: null
title: Palestine - UNOSAT Gaza Strip Comprehensive Damage Assessment - 7 November
  2023
version: null
vulnerability: null
---
