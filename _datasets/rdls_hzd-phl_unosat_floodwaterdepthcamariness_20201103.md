---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-1 satellite imagery
    url: https://data.humdata.org/dataset/floodwater-depth-in-camarines-sur-provinces-bicol-region-region-v-of-philippines-as-of-1-n
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Digital elevation model (DEM)
    url: https://data.humdata.org/dataset/floodwater-depth-in-camarines-sur-provinces-bicol-region-region-v-of-philippines-as-of-1-n
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/floodwater-depth-in-camarines-sur-provinces-bicol-region-region-v-of-philippines-as-of-1-n
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/floodwater-depth-in-camarines-sur-provinces-bicol-region-region-v-of-philippines-as-of-1-n
dataset_id: rdls_hzd-phl_unosat_floodwaterdepthcamariness_20201103
description: 'UNOSAT code: TC20201101PHL This map illustrates floodwater depth in
  Camarines Sur provinces of Philippines based on surface waters observed from a Sentinel-1
  image acquired on 1st of November 2020 and a digital elevation model data with the
  floodwater depth estimation tool(FwDET). This is a preliminary analysis and has
  not yet been validated in the field. Please send ground feedback to UNITAR-UNOSAT.
  Important Note: Flood analysis from radar images may underestimate the presence
  of standing waters in built-up areas and densely vegetated areas due to backscattering
  properties of the radar signal.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/floodwater-depth-in-camarines-sur-provinces-bicol-region-region-v-of-philippines-as-of-1-n]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure: []
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
        process: pluvial_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: Sentinel-1 SAR imagery acquired on 1 November 2020 was compared with
    reference data to detect surface water extent in Camarines Sur following Typhoon
    Mocha. Floodwater depth was estimated by applying the FwDET algorithm to the detected
    water surfaces using a digital elevation model. The analysis is preliminary and
    unvalidated in the field.
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
    name: Digital elevation model (DEM)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/floodwater-depth-in-camarines-sur-provinces-bicol-region-region-v-of-philippines-as-of-1-n
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
  description: Floodwater depth in Camarines Sur Provinces, Bicol Region (Region V)
    of Philippines as of 1 November 2020 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/PH/TC20201101PHL/TC20201101PHL_gdb.zip
  format: Geodatabase
  id: resource_35aec987
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20201101PHL_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Floodwater depth in Camarines Sur Provinces, Bicol Region (Region V)
    of Philippines as of 1 November 2020 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/PH/TC20201101PHL/TC20201101PHL_SHP.zip
  format: null
  id: resource_0c57ba52
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20201101PHL_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-phl_unosat_floodwaterdepthcamariness_20201103
spatial:
  bbox: null
  centroid: null
  countries:
  - PHL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2020-11-03'
temporal_resolution: null
title: Floodwater depth in Camarines Sur Provinces, Bicol Region (Region V) of Philippines
  as of 1 November 2020
version: null
vulnerability: null
---
