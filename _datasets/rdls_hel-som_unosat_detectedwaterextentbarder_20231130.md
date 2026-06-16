---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-extent-in-bardere-city-baardheere-district-gedo-region-somalia-29-november-2023
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-bardere-city-baardheere-district-gedo-region-somalia-29-november-2023
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-bardere-city-baardheere-district-gedo-region-somalia-29-november-2023
dataset_id: rdls_hel-som_unosat_detectedwaterextentbarder_20231130
description: 'UNOSAT code: FL20231105SOM This map illustrates satellite-detected surface
  waters in Bardere City, Baardheere District, Gedo Region, Somalia as observed from
  a WorldView-3 image acquired on 29 November 2023. Within the analysed area of about
  32 km2 about 4.5 km2 of land appears to be flooded. The water extent appears to
  have receded about 1.5 km2 since 22 November 2023. Furthermore, within the analysed
  area about 1,200 buildings are identified as potentially affected by the floods
  as of 29 November 2023. This is a preliminary analysis and has not yet been validated
  in the field. Please send ground feedback to United Nations Satellite Centre (UNOSAT)..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-in-bardere-city-baardheere-district-gedo-region-somalia-29-november-2023]'
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
    description: Building stock in Bardere City identified from satellite imagery
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
  description: UNOSAT analysts interpreted WorldView-3 satellite imagery from 29 November
    2023 to detect surface water extent in Bardere City, comparing with prior imagery
    from 22 November 2023 to assess water recession. Building footprints were identified
    from the same satellite imagery and overlaid with the water extent to determine
    potentially affected structures.
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
- href: https://data.humdata.org/dataset/water-extent-in-bardere-city-baardheere-district-gedo-region-somalia-29-november-2023
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Buildings potentially affected by flood waters in Bardere City as
      of 29 November 2023
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
  description: Satellite detected water extent in Bardere City, Baardheere District,
    Gedo Region, Somalia, 29 November 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3762/FL20231105SOM.gdb.zip
  format: Geodatabase
  id: resource_6cc52733
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
  description: Satellite detected water extent in Bardere City, Baardheere District,
    Gedo Region, Somalia, 29 November 2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3762/FL20231105SOM_SHP.zip
  format: null
  id: resource_407670fa
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
slug: rdls_hel-som_unosat_detectedwaterextentbarder_20231130
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
  start: '2023-11-30'
temporal_resolution: null
title: Satellite detected water extent in Bardere City, Baardheere District, Gedo
  Region, Somalia, 29 November 2023
version: null
vulnerability: null
---
