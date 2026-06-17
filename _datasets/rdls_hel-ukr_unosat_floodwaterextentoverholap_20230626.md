---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/flood-water-extent-over-hola-prystan-city-in-the-east-bank-of-the-dnipro-dnieper-in-kherso
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/flood-water-extent-over-hola-prystan-city-in-the-east-bank-of-the-dnipro-dnieper-in-kherso
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/flood-water-extent-over-hola-prystan-city-in-the-east-bank-of-the-dnipro-dnieper-in-kherso
dataset_id: rdls_hel-ukr_unosat_floodwaterextentoverholap_20230626
description: "UNOSAT code FL20230606UKR This map illustrates satellite-detected flood\
  \ waters and affected structures over Hola Prystan City, in the east bank of the\
  \ Dnieper/Dnipro River in Khersonska Oblast, Ukraine as observed from a WorldView-3\
  \ satellite images acquired on 17 June 2023 at 09:13 UTC and 8 June 2023 at 08:35\
  \ UTC. Within the analysed area of 11 km\xB2, about 27% (3 km\xB2) of Hola Prystan\
  \ City area appears to be flooded. Water extent appears to have decreased by about\
  \ 5 km\xB2 since 8 June 2023. About 1,300 structures were still affected by floods\
  \ on 17 June 2023. This is a preliminary analysis and has not yet been validated\
  \ in the field. Please send ground feedback to United Nations Satellite Centre (UNOSAT)..\
  \ [Source: This metadata record was automatically extracted from the Humanitarian\
  \ Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/flood-water-extent-over-hola-prystan-city-in-the-east-bank-of-the-dnipro-dnieper-in-kherso]"
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
    description: Building structures affected by flood waters in Hola Prystan City
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
  event_sets:
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
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts compared WorldView-3 satellite imagery acquired on
    8 June 2023 and 17 June 2023 to detect flood water extent and identify affected
    structures in Hola Prystan City. Flood water boundaries were manually delineated
    from satellite imagery, and structures within inundated areas were counted to
    quantify direct building impacts. The dataset provides post-event observed hazard
    extent and associated structural damage counts.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
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
- href: https://data.humdata.org/dataset/flood-water-extent-over-hola-prystan-city-in-the-east-bank-of-the-dnipro-dnieper-in-kherso
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: 'Direct building damage from fluvial flooding: approximately 1,300
      structures affected by flood waters as of 17 June 2023'
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
  description: Flood water extent over Hola Prystan City in the east bank of the Dnipro
    (Dnieper) in Khersonska Oblast, Ukraine as of 17 June 2023; 09:13 UTC (Zipped
    geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3634/FL20230606UKR_gdb.zip
  format: Geodatabase
  id: resource_a78b5445
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
  description: Flood water extent over Hola Prystan City in the east bank of the Dnipro
    (Dnieper) in Khersonska Oblast, Ukraine as of 17 June 2023; 09:13 UTC (Zipped
    shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3634/FL20230606UKR_SHP.zip
  format: null
  id: resource_fbf506ce
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
slug: rdls_hel-ukr_unosat_floodwaterextentoverholap_20230626
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
  start: '2023-06-26'
temporal_resolution: null
title: Flood water extent over Hola Prystan City in the east bank of the Dnipro (Dnieper)
  in Khersonska Oblast, Ukraine as of 17 June 2023; 09:13 UTC
version: null
vulnerability: null
---
