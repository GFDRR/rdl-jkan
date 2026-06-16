---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-extent-in-jilib-city-jilib-district-middle-juba-region-somalia-15-november-2023
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-jilib-city-jilib-district-middle-juba-region-somalia-15-november-2023
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-jilib-city-jilib-district-middle-juba-region-somalia-15-november-2023
dataset_id: rdls_hel-som_unosat_detectedwaterextentjilibc_20231116
description: 'UNOSAT code FL20231105SOM This map illustrates satellite-detected surface
  waters in Jilib City, Jilib District, Middle Juba Region, Somalia as observed from
  a Pleiades image acquired on 14 and 15 November 2023. Within the analysed area of
  about 215 km2 about 123 km2 of land appears to be flooded. Furthermore, within the
  analysed area about 2,800 buildings are identified as potentially affected by the
  floods. This is a preliminary analysis and has not yet been validated in the field.
  Please send ground feedback to the United Nations Satellite Centre (UNOSAT).. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-in-jilib-city-jilib-district-middle-juba-region-somalia-15-november-2023]'
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
    description: Building stock in Jilib City identified as potentially affected by
      flood waters
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
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: Pleiades satellite imagery from 14-15 November 2023 was analyzed by
    UNOSAT analysts through visual interpretation and multi-temporal comparison to
    detect surface water extent and identify potentially affected buildings in Jilib
    City. The analysis produced vector polygons of flooded areas (123 km2 within 215
    km2 study area) and building impact assessments as preliminary post-event observations.
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
- href: https://data.humdata.org/dataset/water-extent-in-jilib-city-jilib-district-middle-juba-region-somalia-15-november-2023
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from fluvial flooding with approximately 2,800
      buildings identified as potentially affected
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
  description: Satellite detected water extent in Jilib City, Jilib District, Middle
    Juba Region, Somalia, 15 November 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3740/FL20231105SOM.gdb.zip
  format: Geodatabase
  id: resource_73287476
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20231105SOM.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent in Jilib City, Jilib District, Middle
    Juba Region, Somalia, 15 November 2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3740/FL20231105SOM_SHP.zip
  format: null
  id: resource_d7b6f226
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20231105SOM_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-som_unosat_detectedwaterextentjilibc_20231116
spatial:
  bbox: null
  centroid: null
  countries:
  - SOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-11-16'
temporal_resolution: null
title: Satellite detected water extent in Jilib City, Jilib District, Middle Juba
  Region, Somalia, 15 November 2023
version: null
vulnerability: null
---
