---
attributions:
- entity:
    affiliation: null
    email: null
    name: Worldpop
    url: https://data.humdata.org/dataset/waters-in-ha-tinh-and-nghe-an-provinces-of-viet-nam-as-of-21-october-2020
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Sentinel-1
    url: https://data.humdata.org/dataset/waters-in-ha-tinh-and-nghe-an-provinces-of-viet-nam-as-of-21-october-2020
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/waters-in-ha-tinh-and-nghe-an-provinces-of-viet-nam-as-of-21-october-2020
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/waters-in-ha-tinh-and-nghe-an-provinces-of-viet-nam-as-of-21-october-2020
dataset_id: rdls_he-vnm_unosat_detectedwatershatinhnghep_20201022
description: 'UNOSAT code: TC20201013VNM This map illustrates satellite-detected surface
  waters in Ha Tinh and Nghe An Provinces of Viet Nam as observed from a Sentinel-1
  image acquired on 21 October 2020. Within the analyzed area of about 8,000 km2,
  a total of about 300 km2 of lands appear to be flooded. In Ha Tinh province, the
  water extent appears to have receded of about 200 km2 since 18 October 2020. Based
  on Worldpop population data and the detected surface waters, about 100,000 people
  are potentially exposed or living close to flooded areas. The potentially exposed
  population is mainly located in the districts of Cam Xuyen with ~15,000 people,
  Can Loc with ~15,000 people and Thach Ha with ~15,000 people. This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to UNITAR-UNOSAT. Important Note: Flood analysis from radar images may underestimate
  the presence of standing waters in built-up areas and densely vegetated areas due
  to backscattering properties of the radar signal.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/waters-in-ha-tinh-and-nghe-an-provinces-of-viet-nam-as-of-21-october-2020]'
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
    description: Approximately 100,000 people potentially exposed or living close
      to satellite-detected flooded areas
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
  description: Sentinel-1 SAR imagery acquired on 21 October 2020 was analyzed by
    UNOSAT through visual interpretation and multi-temporal comparison with imagery
    from 18 October 2020 to detect changes in surface water extent. Detected flooded
    areas (approximately 300 km2) were then intersected with Worldpop population distribution
    data to estimate potentially exposed population (approximately 100,000 people)
    in the study area covering Ha Tinh and Nghe An provinces.
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
    name: Sentinel-1
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/waters-in-ha-tinh-and-nghe-an-provinces-of-viet-nam-as-of-21-october-2020
  rel: source
loss:
  losses: []
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
  description: Satellite detected waters in Ha Tinh and Nghe An Provinces of Viet
    Nam as of 21 October 2020 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/VN/TC20201013VNM/TC20201013VNM_gdb.zip
  format: Geodatabase
  id: resource_3c84ad97
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20201013VNM_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected waters in Ha Tinh and Nghe An Provinces of Viet
    Nam as of 21 October 2020 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/VN/TC20201013VNM/TC20201013VNM_SHP.zip
  format: null
  id: resource_96f845f3
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20201013VNM_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-vnm_unosat_detectedwatershatinhnghep_20201022
spatial:
  bbox: null
  centroid: null
  countries:
  - VNM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2020-10-22'
temporal_resolution: null
title: Satellite detected waters in Ha Tinh and Nghe An Provinces of Viet Nam as of
  21 October 2020
version: null
vulnerability: null
---
