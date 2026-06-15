---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-extent-in-jowhar-city-jowhar-district-middle-shabelle-region-somalia-22-november-202
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-jowhar-city-jowhar-district-middle-shabelle-region-somalia-22-november-202
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-jowhar-city-jowhar-district-middle-shabelle-region-somalia-22-november-202
dataset_id: rdls_hel-som_unosat_detectedwaterextentjowhar_20231124
description: 'UNOSAT code: FL20231105SOM This map illustrates satellite-detected surface
  waters in Jowhar City, Jowhar District, Middle Shabelle Region, Somalia as observed
  from a Worldview-2 image acquired on 22 November 2023. Within the analysed area
  of about 13 km2 about 1,4 km2 of land appears to be flooded. Furthermore, within
  the analysed area about 300 buildings are identified as potentially affected by
  the floods. This is a preliminary analysis and has not yet been validated in the
  field. Please send ground feedback to the United Nations Satellite Centre (UNOSAT)..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-in-jowhar-city-jowhar-district-middle-shabelle-region-somalia-22-november-202]'
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
    description: Building footprints identified within the analyzed area of Jowhar
      City
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
  description: Worldview-2 satellite imagery acquired on 22 November 2023 was analyzed
    by UNOSAT to detect surface water extent through visual interpretation and multi-temporal
    comparison. Building footprints within the flooded area were identified and counted
    to assess potential exposure. The analysis is preliminary and unvalidated on the
    ground.
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
- href: https://data.humdata.org/dataset/water-extent-in-jowhar-city-jowhar-district-middle-shabelle-region-somalia-22-november-202
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Buildings potentially affected by detected flood waters in Jowhar
      City
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
  description: Satellite detected water extent in Jowhar City, Jowhar District, Middle
    Shabelle Region, Somalia, 22 November 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3754/FL20231105SOM.gdb.zip
  format: Geodatabase
  id: resource_1e3e231e
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
  description: Satellite detected water extent in Jowhar City, Jowhar District, Middle
    Shabelle Region, Somalia, 22 November 2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3754/FL20231105SOM_SHP.zip
  format: null
  id: resource_a819807c
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
slug: rdls_hel-som_unosat_detectedwaterextentjowhar_20231124
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
  start: '2023-11-24'
temporal_resolution: null
title: Satellite detected water extent in Jowhar City, Jowhar District, Middle Shabelle
  Region, Somalia, 22 November 2023
version: null
vulnerability: null
---
