---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-extent-in-buloburto-city-and-surroundings-buloburto-district-hiraan-region-somalia-3
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-buloburto-city-and-surroundings-buloburto-district-hiraan-region-somalia-3
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-buloburto-city-and-surroundings-buloburto-district-hiraan-region-somalia-3
dataset_id: rdls_hel-som_unosat_detectedwaterextentbulobu_20231201
description: 'UNOSAT code: FL20231105SOM This map illustrates satellite-detected surface
  waters in Buloburto City, Buloburto District, Hiraan Region, Somalia as observed
  from a Worldview-2 image acquired on 30 November 2023. Within the analysed area
  of about 150 km2 about 23 km2 of land appears to be flooded. Furthermore, within
  the analysed area 7,151 buildings are identified as potentially affected by the
  floods as of 30 November 2023. This is a preliminary analysis and has not yet been
  validated in the field. Please send ground feedback to United Nations Satellite
  Centre (UNOSAT).. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-in-buloburto-city-and-surroundings-buloburto-district-hiraan-region-somalia-3]'
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
    description: "Building footprints identified within the 150 km\xC2\xB2 analysis\
      \ area"
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
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: Worldview-2 satellite imagery acquired on 30 November 2023 was analyzed
    by UNOSAT analysts through visual interpretation and multi-temporal comparison
    to delineate surface water extent and identify building footprints within the
    flooded area. The resulting water extent polygon and building damage assessment
    represent preliminary post-event observations requiring field validation.
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
- href: https://data.humdata.org/dataset/water-extent-in-buloburto-city-and-surroundings-buloburto-district-hiraan-region-somalia-3
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Buildings potentially affected by flood waters as detected from satellite
      imagery on 30 November 2023
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
  description: Satellite detected water extent in Buloburto City and surroundings,
    Buloburto District, Hiraan Region, Somalia, 30 November 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3764/FL20231105SOM.gdb.zip
  format: Geodatabase
  id: resource_712014b2
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
  description: Satellite detected water extent in Buloburto City and surroundings,
    Buloburto District, Hiraan Region, Somalia, 30 November 2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3764/FL20231105SOM_SHP.zip
  format: null
  id: resource_9c78fade
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
slug: rdls_hel-som_unosat_detectedwaterextentbulobu_20231201
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
  start: '2023-12-01'
temporal_resolution: null
title: Satellite detected water extent in Buloburto City and surroundings, Buloburto
  District, Hiraan Region, Somalia, 30 November 2023
version: null
vulnerability: null
---
