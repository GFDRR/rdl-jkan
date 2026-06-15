---
attributions:
- entity:
    affiliation: null
    email: null
    name: Worldpop
    url: https://data.humdata.org/dataset/satellite-detected-water-extent-over-province-1-and-2-nepal-as-of-1-of-july-2021
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Sentinel-1 SAR imagery
    url: https://data.humdata.org/dataset/satellite-detected-water-extent-over-province-1-and-2-nepal-as-of-1-of-july-2021
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-over-province-1-and-2-nepal-as-of-1-of-july-2021
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-over-province-1-and-2-nepal-as-of-1-of-july-2021
dataset_id: rdls_hel-npl_unosat_detectedwaterextentoverpr_20210702
description: 'UNOSAT code: FL20210630NPL This map illustrates satellite-detected surface
  waters in Province 1 and 2 as observed from a Sentinel-1 image acquired on 1 July
  2021 at 05:58 local time and using an automated analysis with Artificial Intelligence
  based methods. Within the analyzed area of about 110,000 km2 and, about 645km2 of
  lands appear to be flooded. Based on Worldpop population data and the detected surface
  waters in the analyzed area, about 700,000 people are potentially exposed or living
  close to flooded areas. This is a preliminary analysis and has not yet been validated
  in the field. Please send ground feedback to UNITAR-UNOSAT. Important note: Flood
  analysis from radar images may underestimate the presence of standing waters in
  built-up areas and densely vegetated areas due to backscattering properties of the
  radar signal.. [Source: This metadata record was automatically extracted from the
  Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extent-over-province-1-and-2-nepal-as-of-1-of-july-2021]'
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
  description: "Sentinel-1 SAR satellite imagery acquired on 1 July 2021 was processed\
    \ using automated artificial intelligence methods to detect surface water extent.\
    \ The resulting water extent polygons (645 km\xC2\xB2) were intersected with WorldPop\
    \ gridded population data to estimate population exposure in Province 1 and 2,\
    \ Nepal."
  sources:
  - id: source_1
    license: null
    name: Worldpop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: Sentinel-1 SAR imagery
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/satellite-detected-water-extent-over-province-1-and-2-nepal-as-of-1-of-july-2021
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population exposed to flooded areas as of 1 July 2021
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
  description: Satellite detected water extent over Province 1 and 2 , Nepal as of
    1 of July 2021 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/NP/FL20210630NPL/FL20210630NPL_gdb.zip
  format: Geodatabase
  id: resource_8f2536c8
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20210630NPL_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent over Province 1 and 2 , Nepal as of
    1 of July 2021 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/NP/FL20210630NPL/FL20210630NPL_SHP.zip
  format: null
  id: resource_a4f99204
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20210630NPL_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-npl_unosat_detectedwaterextentoverpr_20210702
spatial:
  bbox: null
  centroid: null
  countries:
  - NPL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2021-07-02'
temporal_resolution: null
title: Satellite detected water extent over Province 1 and 2 , Nepal as of 1 of July
  2021
version: null
vulnerability: null
---
