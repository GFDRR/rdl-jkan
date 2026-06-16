---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-1 satellite imagery
    url: https://data.humdata.org/dataset/satellite-detected-water-in-izabal-department-of-guatemala-as-of-23-november-2020
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/satellite-detected-water-in-izabal-department-of-guatemala-as-of-23-november-2020
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-in-izabal-department-of-guatemala-as-of-23-november-2020
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-in-izabal-department-of-guatemala-as-of-23-november-2020
dataset_id: rdls_he-gtm_unosat_detectedwaterizabaldepart_20201125
description: 'UNOSAT code: TC20201119GTM This map illustrates satellite-detected surface
  waters in Izabal department of Guatemala as observed from a Sentinel-1 image acquired
  on 23 November 2020 at 05:45 Local time. Within the analyzed area of about 6,000
  km2, a total of about 150 km2 of lands appear to be flooded. Based on Worldpop population
  data and the detected surface waters, about 8,600 people are potentially exposed
  or living close to flooded areas. This is a preliminary analysis and has not yet
  been validated in the field. Please send ground feedback to UNITAR-UNOSAT. Important
  Note: Flood analysis from radar images may underestimate the presence of standing
  waters in built-up areas and densely vegetated areas due to backscattering properties
  of the radar signal.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-in-izabal-department-of-guatemala-as-of-23-november-2020]'
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
      process: pluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: "Sentinel-1 SAR satellite imagery acquired on 23 November 2020 was\
    \ analyzed by UNOSAT to detect surface water extent through visual interpretation\
    \ and change detection methods. Detected flooded areas (~150 km\xB2) were intersected\
    \ with WorldPop gridded population data to estimate approximately 8,600 people\
    \ potentially exposed to or living near flooded areas in the 6,000 km\xB2 study\
    \ area of Izabal department."
  sources:
  - id: source_1
    license: null
    name: Sentinel-1 satellite imagery
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/satellite-detected-water-in-izabal-department-of-guatemala-as-of-23-november-2020
  rel: source
loss: null
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
  description: Satellite detected water in Izabal department of Guatemala as of 23
    November 2020 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/GT/TC20201119GTM/TC20201119GTM_gdb.zip
  format: Geodatabase
  id: resource_11efce70
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20201119GTM_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water in Izabal department of Guatemala as of 23
    November 2020 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/GT/TC20201119GTM/TC20201119GTM_SHP.zip
  format: null
  id: resource_277be035
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20201119GTM_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-gtm_unosat_detectedwaterizabaldepart_20201125
spatial:
  bbox: null
  centroid: null
  countries:
  - GTM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2020-11-25'
temporal_resolution: null
title: Satellite detected water in Izabal department of Guatemala as of 23 November
  2020
version: null
vulnerability: null
---
