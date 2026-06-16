---
attributions:
- entity:
    affiliation: null
    email: null
    name: Planet Scope
    url: https://data.humdata.org/dataset/wildfires-in-qastal-maaf-sub-district-latakia-governorate-syria-as-of-4-july-2025
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/wildfires-in-qastal-maaf-sub-district-latakia-governorate-syria-as-of-4-july-2025
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/wildfires-in-qastal-maaf-sub-district-latakia-governorate-syria-as-of-4-july-2025
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/wildfires-in-qastal-maaf-sub-district-latakia-governorate-syria-as-of-4-july-2025
dataset_id: rdls_hel-syr_unosat_wildfiresqastalmaafsubdis_20250708
description: "UNOSAT code: FR20250707SYR, GDACS ID: 1024188 This map illustrates satellite-detected\
  \ burned areas in Qastal Maaf Subdistrict, Latakia Governorate, Syria based on Planet\
  \ Scope image acquired on 4 July 2025 at 11:43 local time. Within the analyzed area\
  \ of about 30 km\xB2, about 4 km\xB2 of lands appear to be potentially burned. Based\
  \ on WorldPop population data and the extent of burned areas (within 1 km), approximately\
  \ 900 people are potentially exposed or living in close to burned areas. In addition,\
  \ about 500 buildings are located within 1 km of the burned zones, which may also\
  \ be at risk or affected. This is a preliminary analysis and has not yet been validated\
  \ in the field. Please send ground feedback to United Nations Satellite Centre (UNOSAT)..\
  \ [Source: This metadata record was automatically extracted from the Humanitarian\
  \ Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/wildfires-in-qastal-maaf-sub-district-latakia-governorate-syria-as-of-4-july-2025]"
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
    description: Approximately 900 people potentially exposed or living within 1 km
      of burned areas based on WorldPop data
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Approximately 500 buildings located within 1 km of burned zones
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_2
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
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts reviewed Planet Scope satellite imagery from 4 July
    2025 to detect burned areas through multi-temporal image comparison. Burned area
    polygons were delineated and intersected with WorldPop population grids and building
    footprints within a 1 km buffer to estimate exposure and potential impacts in
    Qastal Maaf Sub-district, Latakia Governorate, Syria.
  sources:
  - id: source_1
    license: null
    name: Planet Scope
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/wildfires-in-qastal-maaf-sub-district-latakia-governorate-syria-as-of-4-july-2025
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population potentially exposed to wildfire within 1 km of burned
      areas
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
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
  - asset_category: buildings
    asset_dimension: structure
    description: Buildings potentially affected by wildfire within 1 km of burned
      zones
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: null
      trigger: null
      type: wildfire
    id: loss_2
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
  description: Wildfires in Qastal Maaf Sub-district, Latakia Governorate, Syria as
    of 4 July 2025 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4145/FR20250707SYR_gdb.zip
  format: Geodatabase
  id: resource_6289abe8
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FR20250707SYR_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Wildfires in Qastal Maaf Sub-district, Latakia Governorate, Syria as
    of 4 July 2025 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4145/FR20250707SYR_SHP.zip
  format: null
  id: resource_5d9fb768
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FR20250707SYR_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-syr_unosat_wildfiresqastalmaafsubdis_20250708
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
  start: '2025-07-08'
temporal_resolution: null
title: Wildfires in Qastal Maaf Sub-district, Latakia Governorate, Syria as of 4 July
  2025
version: null
vulnerability: null
---
