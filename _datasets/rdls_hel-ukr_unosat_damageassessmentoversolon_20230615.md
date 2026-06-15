---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/damage-assessment-over-solontsi-village-and-pidlisne-village-khersonskyi-region-khersonska
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-over-solontsi-village-and-pidlisne-village-khersonskyi-region-khersonska
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-over-solontsi-village-and-pidlisne-village-khersonskyi-region-khersonska
dataset_id: rdls_hel-ukr_unosat_damageassessmentoversolon_20230615
description: 'UNOSAT code FL20230606UKR This map illustrates satellite-detected flood
  waters and affected structures over Solontsi Village and Pidlisne Village, Khersonskyi
  Region, Khersonska Oblast (Ukraine) as observed from a WorldView-3 image acquired
  on 7 June 2023 at 08:19 UTC; and ICEYE image acquired on 7 June 2023. Within the
  analysed area of 330 ha, about 97% (320 ha) of Solontsi Village area appears to
  be flooded and 1,070 structures are affected. About 3% (1 ha) of Pidlisne Village
  area appears to be flooded and 13 structures are potentially affected. This is a
  preliminary analysis and has not yet been validated in the field. Please send ground
  feedback to United Nations Satellite Centre (UNOSAT).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/damage-assessment-over-solontsi-village-and-pidlisne-village-khersonskyi-region-khersonska]'
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
    description: Building structures in Solontsi and Pidlisne villages identified
      from satellite imagery
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
hazard:
  event_sets_by_hazard_type:
    flood:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts compared WorldView-3 optical and ICEYE SAR satellite
    imagery acquired on 7 June 2023 to detect flood water extent and identify affected
    building structures in two Ukrainian villages. Satellite-detected changes between
    pre- and post-event imagery were manually interpreted to produce damage counts
    and inundated area estimates.
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
- href: https://data.humdata.org/dataset/damage-assessment-over-solontsi-village-and-pidlisne-village-khersonskyi-region-khersonska
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from fluvial flooding detected via satellite
      imagery comparison
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
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
  description: Damage assessment over Solontsi Village and Pidlisne Village, Khersonskyi
    Region, Khersonska Oblast, Ukraine as of 07 June 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3627/FL20230606UKR_gdb.zip
  format: Geodatabase
  id: resource_3df31ea0
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230606UKR_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Damage assessment over Solontsi Village and Pidlisne Village, Khersonskyi
    Region, Khersonska Oblast, Ukraine as of 07 June 2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3627/FL20230606UKR_SHP.zip
  format: null
  id: resource_0d4dc87a
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230606UKR_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-ukr_unosat_damageassessmentoversolon_20230615
spatial:
  bbox: null
  centroid: null
  countries:
  - UKR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-06-15'
temporal_resolution: null
title: Damage assessment over Solontsi Village and Pidlisne Village, Khersonskyi Region,
  Khersonska Oblast, Ukraine as of 07 June 2023
version: null
vulnerability: null
---
