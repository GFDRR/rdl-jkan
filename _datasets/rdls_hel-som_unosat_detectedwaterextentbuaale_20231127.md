---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-extent-in-bu-aale-city-bu-aale-district-middle-juba-region-somalia-22-november-2023
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-bu-aale-city-bu-aale-district-middle-juba-region-somalia-22-november-2023
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-bu-aale-city-bu-aale-district-middle-juba-region-somalia-22-november-2023
dataset_id: rdls_hel-som_unosat_detectedwaterextentbuaale_20231127
description: 'UNOSAT code: FL20231105SOM This map illustrates satellite-detected surface
  waters in Bu''aale City, Bu''aale District, Middle Juba Region, Somalia as observed
  from a Worldview-3 image acquired on 22 November 2023 at 07:35 UTC. Within the analysed
  area of about 1,000 hectares about 800 hectares of land appear to be flooded. Compared
  to the situation on 13 November, the flood-affected area in the analysed extent
  increased about 20 hectares and the number of flood-affected buildings increased
  about 330. This is a preliminary analysis and has not yet been validated in the
  field. Please send ground feedback to United Nations Satellite Centre (UNOSAT)..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-in-bu-aale-city-bu-aale-district-middle-juba-region-somalia-22-november-2023]'
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
    description: Building footprints and structures in Bu'aale City identified in
      satellite imagery
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
        intensity_measure: AA:km2
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: Worldview-3 satellite imagery acquired on 22 November 2023 was analyzed
    by UNOSAT analysts through visual interpretation and multi-temporal comparison
    with imagery from 13 November 2023 to detect surface water extent and quantify
    flood-affected area and buildings in Bu'aale City. The analysis produced vector
    geodatabase and shapefile outputs delineating flooded zones and affected structures.
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
- href: https://data.humdata.org/dataset/water-extent-in-bu-aale-city-bu-aale-district-middle-juba-region-somalia-22-november-2023
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from flood inundation, with approximately
      330 additional buildings affected between 13-22 November 2023
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
  description: Satellite detected water extent in Bu'aale City, Bu'aale District,
    Middle Juba Region, Somalia, 22 November 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3760/FL20231105SOM.gdb.zip
  format: Geodatabase
  id: resource_a222a702
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
  description: Satellite detected water extent in Bu'aale City, Bu'aale District,
    Middle Juba Region, Somalia, 22 November 2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3760/FL20231105SOM_SHP.zip
  format: null
  id: resource_b93ce05a
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
slug: rdls_hel-som_unosat_detectedwaterextentbuaale_20231127
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
  start: '2023-11-27'
temporal_resolution: null
title: Satellite detected water extent in Bu'aale City, Bu'aale District, Middle Juba
  Region, Somalia, 22 November 2023
version: null
vulnerability: null
---
