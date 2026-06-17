---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-lilawa-village-jarablus-district-aleppo-governorate-syria-as-of-7-feb
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-lilawa-village-jarablus-district-aleppo-governorate-syria-as-of-7-feb
dataset_id: rdls_hl-syr_unosat_damageassessmentlilawavil_20230209
description: 'UNOSAT code EQ20230206SYR, GDACS Id: 1357372 This map illustrates potentially
  damaged structures/buildings by the 06th of February 2023 earthquake in Lilawa Village,
  Jarablus District, Aleppo Governorate, Syria as detected by a Worldview-3 Very high-resolution
  satellite image acquired on 7 February 2023. Within this village, UNOSAT identified
  30 damaged structures and 68 potentially damaged structures. This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to United Nations Satellite Centre (UNOSAT).. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/damage-assessment-in-lilawa-village-jarablus-district-aleppo-governorate-syria-as-of-7-feb]'
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
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: PGA:g
      process: ground_motion
      trigger: null
      type: earthquake
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: earthquake
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts compared pre- and post-event Worldview-3 satellite
    imagery acquired on 7 February 2023 to detect structural damage in Lilawa Village
    caused by the 6 February 2023 earthquake. Visual interpretation identified 30
    confirmed damaged and 68 potentially damaged buildings, classified by damage confidence
    levels and validated through satellite change detection methodology.
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
- href: https://data.humdata.org/dataset/damage-assessment-in-lilawa-village-jarablus-district-aleppo-governorate-syria-as-of-7-feb
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment identifying 30 confirmed damaged
      and 68 potentially damaged structures from the 6 February 2023 earthquake
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
  description: Damage Assessment in Lilawa Village, Jarablus District, Aleppo Governorate,
    Syria as of 7 February 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3484/EQ20230206SYR_gdb.zip
  format: Geodatabase
  id: resource_1281acad
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20230206SYR_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Damage Assessment in Lilawa Village, Jarablus District, Aleppo Governorate,
    Syria as of 7 February 2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3484/EQ20230206SYR_SHP.zip
  format: null
  id: resource_0def011c
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20230206SYR_SHP.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-syr_unosat_damageassessmentlilawavil_20230209
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
  start: '2023-02-09'
temporal_resolution: null
title: Damage Assessment in Lilawa Village, Jarablus District, Aleppo Governorate,
  Syria as of 7 February 2023
version: null
vulnerability: null
---
