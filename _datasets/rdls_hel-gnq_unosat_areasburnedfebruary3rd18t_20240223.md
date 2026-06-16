---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/areas-burned-from-february-3rd-to-18th-2024-around-the-pico-basil-volcano-on-bioko-island-
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/areas-burned-from-february-3rd-to-18th-2024-around-the-pico-basil-volcano-on-bioko-island-
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/areas-burned-from-february-3rd-to-18th-2024-around-the-pico-basil-volcano-on-bioko-island-
dataset_id: rdls_hel-gnq_unosat_areasburnedfebruary3rd18t_20240223
description: 'UNOSAT code: FR20240222GNQ This map illustrates the burned areas as
  observed from Sentinel-2 images acquired on the 3rd and 18th of February 2024, over
  the Pico Basil Volcano on Bioko Island, Equatorial Guinea. Approximately 3 km2 of
  vegetation appeared to have burned around the Pico Basil Volcano as of February
  3rd, 2024, increasing to about 6 km2 by 18th of February 2024. UNOSAT has identified
  16 potentially affected structures and potentially affected roads approximately
  2 kilometers. This is a preliminary analysis and has not yet been validated in the
  field. Please send ground feedback to the United Nations Satellite Centre (UNOSAT)..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/areas-burned-from-february-3rd-to-18th-2024-around-the-pico-basil-volcano-on-bioko-island-]'
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
    description: Potentially affected structures identified within 2 km of burned
      areas
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
    description: Potentially affected road network within 2 km of burned areas
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_2
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
      intensity_measure: AA:km2
      process: wildfire
      trigger: null
      type: wildfire
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts processed Sentinel-2 satellite imagery acquired on
    3 and 18 February 2024, comparing multi-temporal images to identify and delineate
    burned vegetation areas around Pico Basil Volcano. Spatial analysis identified
    16 potentially affected structures and affected road segments within 2 km of the
    burned perimeter. Results are preliminary and field-validated.
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
- href: https://data.humdata.org/dataset/areas-burned-from-february-3rd-to-18th-2024-around-the-pico-basil-volcano-on-bioko-island-
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Potentially affected structures from wildfire around Pico Basil Volcano
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: wildfire
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: natural_environment
    asset_dimension: product
    description: "Burned vegetation area expanding from 3 km\xB2 to 6 km\xB2 between\
      \ 3-18 February 2024"
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: wildfire
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
  description: Areas burned from February 3rd to 18th, 2024, around the Pico Basil
    Volcano on Bioko Island, Equatorial Guinea (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3799/FR20240222GNQ_gdb.zip
  format: Geodatabase
  id: resource_bb0e75cb
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FR20240222GNQ_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Areas burned from February 3rd to 18th, 2024, around the Pico Basil
    Volcano on Bioko Island, Equatorial Guinea (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3799/FR20240222GNQ_SHP.zip
  format: null
  id: resource_62d7b209
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FR20240222GNQ_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-gnq_unosat_areasburnedfebruary3rd18t_20240223
spatial:
  bbox: null
  centroid: null
  countries:
  - GNQ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-02-23'
temporal_resolution: null
title: Areas burned from February 3rd to 18th, 2024, around the Pico Basil Volcano
  on Bioko Island, Equatorial Guinea
version: null
vulnerability: null
---
