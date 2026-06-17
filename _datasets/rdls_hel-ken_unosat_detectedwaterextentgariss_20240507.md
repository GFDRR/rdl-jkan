---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/satellite-detected-water-extent-in-garissa-city-and-mororo-village-kenya-as-of-5-may-2024
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-in-garissa-city-and-mororo-village-kenya-as-of-5-may-2024
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-in-garissa-city-and-mororo-village-kenya-as-of-5-may-2024
dataset_id: rdls_hel-ken_unosat_detectedwaterextentgariss_20240507
description: "UNOSAT code: FL20240426KEN, GDACS ID: 1102561 This map illustrates satellite-detected\
  \ surface waters in Garissa City and Mororo Village, Kenya, as observed from a Pl\xE9\
  iades image acquired on 5 May 2024 at 07:36 UTC Within the analysed area , a total\
  \ of about 22 km\xB2 of land appears to be flooded. Furthermore, within the analyzed\
  \ area, 3,377 buildings are identified as affected by the floods, along with about\
  \ 90 km of roads, as of 5 May 2024 This is a preliminary analysis and has not yet\
  \ been validated in the field. Please send ground feedback to the United Nations\
  \ Satellite Centre (UNOSAT).. [Source: This metadata record was automatically extracted\
  \ from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extent-in-garissa-city-and-mororo-village-kenya-as-of-5-may-2024]"
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
    description: Building footprints or counts within the analysed area used to assess
      flood exposure in Garissa City and Mororo Village.
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
    description: Road network within the analysed area assessed for flood exposure,
      totalling approximately 90 km.
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
  - analysis_type: deterministic
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
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: "A Pl\xE9iades satellite image acquired on 5 May 2024 at 07:36 UTC\
    \ was analysed by UNOSAT analysts using visual interpretation and multi-image\
    \ comparison to delineate surface water extent in Garissa City and Mororo Village,\
    \ Kenya. The resulting flood footprint (~22 km\xB2) was intersected with building\
    \ and road datasets to quantify affected assets. This preliminary analysis supports\
    \ rapid emergency response under GDACS event 1102561 (UNOSAT code FL20240426KEN)."
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
- href: https://data.humdata.org/dataset/satellite-detected-water-extent-in-garissa-city-and-mororo-village-kenya-as-of-5-may-2024
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: 3,377 buildings identified as affected by floods in Garissa City
      and Mororo Village as of 5 May 2024.
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
        modelling: inferred
        type: direct
      loss_approach: analytical
      loss_frequency_type: deterministic
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: Approximately 90 km of roads identified as affected by floods in
      Garissa City and Mororo Village as of 5 May 2024.
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
        modelling: inferred
        type: direct
      loss_approach: analytical
      loss_frequency_type: deterministic
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
  description: Satellite detected water extent in Garissa City and Mororo Village,
    Kenya as of 5 May 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3835/FL20240426KEN_gdb.zip
  format: Geodatabase
  id: resource_83705e58
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240426KEN_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent in Garissa City and Mororo Village,
    Kenya as of 5 May 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3835/FL20240426KEN_SHP.zip
  format: null
  id: resource_00cd46f8
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240426KEN_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-ken_unosat_detectedwaterextentgariss_20240507
spatial:
  bbox: null
  centroid: null
  countries:
  - KEN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-05-07'
temporal_resolution: null
title: Satellite detected water extent in Garissa City and Mororo Village, Kenya as
  of 5 May 2024
version: null
vulnerability: null
---
