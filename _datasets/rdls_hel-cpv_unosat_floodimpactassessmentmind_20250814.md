---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/flood-impact-assessment-in-mindelo-city-sao-vicente-municipality-cabo-verde-as-of-13-augus
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/flood-impact-assessment-in-mindelo-city-sao-vicente-municipality-cabo-verde-as-of-13-augus
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/flood-impact-assessment-in-mindelo-city-sao-vicente-municipality-cabo-verde-as-of-13-augus
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/flood-impact-assessment-in-mindelo-city-sao-vicente-municipality-cabo-verde-as-of-13-augus
dataset_id: rdls_hel-cpv_unosat_floodimpactassessmentmind_20250814
description: "UNOSAT code: FL20250812CPV This map illustrates satellite-detected mudflow\
  \ extent in Mindelo City, Sao Vicente Municipality, Cabo Verde as observed from\
  \ Pleiades very high-resolution satellite image acquired on 13 August 2025 at 11:01\
  \ local time (12:01 UTC). Within the analyzed area of approximately 30 km\xB2, about\
  \ 5 km\xB2 of land appears to be affected by flood. Based on WorldPop population\
  \ data and the flood extent, approximately 6,600 people are potentially exposed\
  \ or living close to the flooded areas. Additionally, UNOSAT identified around 2,500\
  \ damaged buildings, five damaged bridges, and approximately 44 km of affected roads.\
  \ This is a preliminary analysis and has not yet been validated in the field. Please\
  \ send ground feedback to the United Nations Satellite Centre (UNOSAT).. [Source:\
  \ This metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/flood-impact-assessment-in-mindelo-city-sao-vicente-municipality-cabo-verde-as-of-13-augus]"
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
    description: Residential population potentially exposed or living close to flooded
      areas, estimated using WorldPop population data intersected with flood extent
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
    description: Building stock within the analyzed area assessed for flood/mudflow
      damage
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
        intensity_measure: AA:km2
        process: pluvial_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "Pleiades very high-resolution satellite imagery acquired on 13 August\
    \ 2025 was analyzed by UNOSAT analysts using visual interpretation and change\
    \ detection to delineate mudflow/flood extent and identify damaged buildings across\
    \ approximately 30 km\xB2 in Mindelo City. WorldPop population data was spatially\
    \ intersected with the derived flood extent to estimate exposed population. The\
    \ resulting geodatabase and shapefile provide a rapid post-event impact assessment\
    \ to support emergency response."
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
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/flood-impact-assessment-in-mindelo-city-sao-vicente-municipality-cabo-verde-as-of-13-augus
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Count of buildings identified as damaged by satellite image analysis
      of the 13 August 2025 flood/mudflow event in Mindelo City
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
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
  - asset_category: population
    asset_dimension: population
    description: Estimated number of people potentially exposed or living close to
      flooded areas based on WorldPop data and satellite-derived flood extent
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: flood
    id: loss_2
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
  description: Flood impact assessment in Mindelo City, Sao Vicente Municipality,
    Cabo Verde as of 13 August 2025 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4169/FL20250812COD_GDB.zip
  format: Geodatabase
  id: resource_f5d1e606
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20250812COD_GDB.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flood impact assessment in Mindelo City, Sao Vicente Municipality,
    Cabo Verde as of 13 August 2025 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4169/FL20250812COD_SHP.zip
  format: null
  id: resource_7610c21a
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20250812COD_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-cpv_unosat_floodimpactassessmentmind_20250814
spatial:
  bbox: null
  centroid: null
  countries:
  - CPV
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-08-14'
temporal_resolution: null
title: Flood impact assessment in Mindelo City, Sao Vicente Municipality, Cabo Verde
  as of 13 August 2025
version: null
vulnerability: null
---
