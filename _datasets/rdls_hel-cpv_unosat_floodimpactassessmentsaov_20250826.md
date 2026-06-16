---
attributions:
- entity:
    affiliation: null
    email: null
    name: Pleiades very high-resolution satellite imagery
    url: https://data.humdata.org/dataset/flood-impact-assessment-in-sao-vicente-and-santo-antao-islands-cabo-verde-13-to-16-august-
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop population data
    url: https://data.humdata.org/dataset/flood-impact-assessment-in-sao-vicente-and-santo-antao-islands-cabo-verde-13-to-16-august-
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/flood-impact-assessment-in-sao-vicente-and-santo-antao-islands-cabo-verde-13-to-16-august-
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/flood-impact-assessment-in-sao-vicente-and-santo-antao-islands-cabo-verde-13-to-16-august-
dataset_id: rdls_hel-cpv_unosat_floodimpactassessmentsaov_20250826
description: "UNOSAT code: FL20250812CPV This map illustrates satellite-detected mudflow\
  \ extent in Sao Vicente and Santo Islands, Cabo Verde as observed from Pleiades\
  \ very high-resolution satellite image acquired on 13 to 16 August 2025. Within\
  \ the analyzed area, approximately, about 16 km\xB2 of land appears to be affected\
  \ by flood. Based on WorldPop population data and the flood extent, approximately\
  \ 13,600 people are potentially exposed or living close to the flooded areas. Additionally,\
  \ UNOSAT identified around 4,660 damaged buildings, five damaged bridges, and approximately\
  \ 85 km of affected roads. This is a preliminary analysis and has not yet been validated\
  \ in the field. Please send ground feedback to the United Nations Satellite Centre\
  \ (UNOSAT).. [Source: This metadata record was automatically extracted from the\
  \ Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/flood-impact-assessment-in-sao-vicente-and-santo-antao-islands-cabo-verde-13-to-16-august-]"
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
    description: Building stock in flood-affected areas of Sao Vicente and Santo Antao
      Islands
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
    description: Population potentially exposed or living close to flooded areas based
      on WorldPop data
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_2
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Road networks and bridges in flood-affected areas
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
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: "UNOSAT analysts processed Pleiades very high-resolution satellite\
    \ imagery acquired 13-16 August 2025 over Sao Vicente and Santo Antao Islands,\
    \ comparing pre- and post-event images to detect mudflow and flood extent. Satellite-derived\
    \ flood extent (approximately 16 km\xB2) was intersected with WorldPop population\
    \ data to estimate exposed population (~13,600 people). Damage assessment identified\
    \ 4,660 damaged buildings, 5 damaged bridges, and ~85 km of affected road networks\
    \ through visual interpretation of satellite imagery."
  sources:
  - id: source_1
    license: null
    name: Pleiades very high-resolution satellite imagery
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: WorldPop population data
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/flood-impact-assessment-in-sao-vicente-and-santo-antao-islands-cabo-verde-13-to-16-august-
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from flood and mudflow impact
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
  - asset_category: infrastructure
    asset_dimension: structure
    description: Direct infrastructure damage including bridges and road networks
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
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population affected or exposed to flood hazard
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: flood
    id: loss_3
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
  description: Flood impact assessment in Sao Vicente and Santo Antao Islands, Cabo
    Verde (13 to 16 August 2025) (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4182/FL20250812CPV_GDB.zip
  format: Geodatabase
  id: resource_43ffb686
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20250812CPV_GDB.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flood impact assessment in Sao Vicente and Santo Antao Islands, Cabo
    Verde (13 to 16 August 2025) (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4182/FL20250812CPV_SHP.zip
  format: null
  id: resource_4df28bb6
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20250812CPV_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-cpv_unosat_floodimpactassessmentsaov_20250826
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
  start: '2025-08-26'
temporal_resolution: null
title: Flood impact assessment in Sao Vicente and Santo Antao Islands, Cabo Verde
  (13 to 16 August 2025)
version: null
vulnerability: null
---
