---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/flood-impact-assessment-in-north-taungoo-bago-state-myanmar-as-of-02-october-2024
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/flood-impact-assessment-in-north-taungoo-bago-state-myanmar-as-of-02-october-2024
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/flood-impact-assessment-in-north-taungoo-bago-state-myanmar-as-of-02-october-2024
dataset_id: rdls_hel-mmr_unosat_floodimpactassessmentnort_20241009
description: "UNOSAT code: FL20240912MMR This map illustrates satellite detected floods\
  \ using WorldView-3 images acquired on 02 October 2024. Within the analysed area\
  \ of about 23 km\xB2, a total of about 21 km\xB2 of land appears to be affected\
  \ by flood waters with about 18 km\xB2 of cropland inundated. UNITAR-UNOSAT identified\
  \ approximately 2,240 affected buildings, representing 94% of the buildings as well\
  \ as 35 km of affected roads, covering 88% of the roads in the analysed area. This\
  \ is a preliminary analysis and has not yet been validated in the field. Please\
  \ send ground feedback to the United Nations Satellite Centre (UNOSAT).. [Source:\
  \ This metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/flood-impact-assessment-in-north-taungoo-bago-state-myanmar-as-of-02-october-2024]"
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
    description: Building stock in North Taungoo, Bago State classified by flood exposure
      status
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
- asset_type:
    description: Cropland area in the study region affected by flood inundation
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_2
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
- asset_type:
    description: Road network infrastructure in the analysed area
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_3
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: length
      unit: null
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts processed WorldView-3 satellite imagery acquired on
    02 October 2024 over North Taungoo, Bago State, Myanmar, comparing pre- and post-flood
    images to delineate flood extent and identify affected assets. Satellite-detected
    inundation polygons were intersected with building footprints, cropland, and road
    networks to quantify direct impacts. This preliminary post-event damage assessment
    provides empirical flood hazard extent and direct loss estimates for buildings,
    agriculture, and infrastructure.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/flood-impact-assessment-in-north-taungoo-bago-state-myanmar-as-of-02-october-2024
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: 'Direct building damage from flood inundation: 2,240 affected buildings
      (94% of total)'
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
  - asset_category: agriculture
    asset_dimension: product
    description: "Direct cropland loss from flood inundation: 18 km\xB2 of inundated\
      \ agricultural land"
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_2
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
  - asset_category: infrastructure
    asset_dimension: structure
    description: 'Direct road infrastructure damage from flood: 35 km of affected
      roads (88% of total)'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_3
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
  description: Flood Impact Assessment in North Taungoo, Bago State, Myanmar as of
    02 October 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3998/FL20240912MMR_gdb.zip
  format: Geodatabase
  id: resource_ec192bb9
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240912MMR_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flood Impact Assessment in North Taungoo, Bago State, Myanmar as of
    02 October 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3998/FL20240912MMR_SHP.zip
  format: null
  id: resource_48600c67
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240912MMR_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-mmr_unosat_floodimpactassessmentnort_20241009
spatial:
  bbox: null
  centroid: null
  countries:
  - MMR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-10-09'
temporal_resolution: null
title: Flood Impact Assessment in North Taungoo, Bago State, Myanmar as of 02 October
  2024
version: null
vulnerability: null
---
