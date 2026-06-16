---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-2 satellite imagery
    url: https://data.humdata.org/dataset/satellite-detected-waters-in-sirwah-and-ma-rib-city-districts-of-yemen-as-of-5-august-2021
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop population data
    url: https://data.humdata.org/dataset/satellite-detected-waters-in-sirwah-and-ma-rib-city-districts-of-yemen-as-of-5-august-2021
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-waters-in-sirwah-and-ma-rib-city-districts-of-yemen-as-of-5-august-2021
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-waters-in-sirwah-and-ma-rib-city-districts-of-yemen-as-of-5-august-2021
dataset_id: rdls_hel-yem_unosat_detectedwaterssirwahmarib_20210807
description: 'UNOSAT code: FL20210729YEM This map illustrates satellite-detected surface
  waters over Sirwah and Ma''rib City districts of Yemen as observed from a Sentinel-2
  image acquired on 5 August 2021. From the previous preliminary flood assessment
  conducted on 2 August 2021, an additional 1.45 km2. Based on Worldpop population
  data and the detected surface waters, about 90 additional people may be potentially
  exposed or living close to flooded areas. This is a preliminary analysis and has
  not yet been validated in the field. Please send ground feedback to UNITAR- UNOSAT..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-waters-in-sirwah-and-ma-rib-city-districts-of-yemen-as-of-5-august-2021]'
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
    description: Population potentially exposed or living close to detected flooded
      areas based on WorldPop data
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
  description: UNOSAT analysts reviewed Sentinel-2 satellite imagery acquired on 5
    August 2021 and compared it with previous imagery from 2 August 2021 to detect
    changes in surface water extent. Detected water polygons were intersected with
    WorldPop gridded population data to estimate the number of people potentially
    exposed to flooded areas in Sirwah and Ma'rib City districts.
  sources:
  - id: source_1
    license: null
    name: Sentinel-2 satellite imagery
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
- href: https://data.humdata.org/dataset/satellite-detected-waters-in-sirwah-and-ma-rib-city-districts-of-yemen-as-of-5-august-2021
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Approximately 90 people potentially exposed to flooded areas detected
      by satellite imagery
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
  description: Satellite detected waters in Sirwah, and Ma'rib City districts of Yemen
    as of 5 August 2021. (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/YE/FL20210729YEM/FL20210729YEM_gdb.zip
  format: Geodatabase
  id: resource_5e8b951a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20210729YEM_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected waters in Sirwah, and Ma'rib City districts of Yemen
    as of 5 August 2021. (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/YE/FL20210729YEM/FL20210729YEM_shp.zip
  format: null
  id: resource_d00aff4d
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20210729YEM_shp.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-yem_unosat_detectedwaterssirwahmarib_20210807
spatial:
  bbox: null
  centroid: null
  countries:
  - YEM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2021-08-07'
temporal_resolution: null
title: Satellite detected waters in Sirwah, and Ma'rib City districts of Yemen as
  of 5 August 2021.
version: null
vulnerability: null
---
