---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/floodwater-depth-in-camarines-sur-provinces-albay-province-bicol-region-of-philippines-as-
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/floodwater-depth-in-camarines-sur-provinces-albay-province-bicol-region-of-philippines-as-
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/floodwater-depth-in-camarines-sur-provinces-albay-province-bicol-region-of-philippines-as-
dataset_id: rdls_hzd-phl_unosat_floodwaterdepthcamariness_20201104
description: 'UNOSAT code: TC20201101PHL This map illustrates floodwater depth in
  Nabua and Baao Municipalities, Camarines Sur Provinces & Bato and Libon, Albay Province,
  Bicol Region (Region V) of Philippines based on surface waters observed from a Sentinel-1
  image acquired on 1st of November 2020 and digital elevation model data with the
  floodwater depth estimation tool (FwDET). This is a preliminary analysis and has
  not yet been validated in the field. Please send ground feedback to UNITAR-UNOSAT.
  Important Note: Flood analysis from radar images may underestimate the presence
  of standing waters in built-up areas and densely vegetated areas due to backscattering
  properties of the radar signal.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/floodwater-depth-in-camarines-sur-provinces-albay-province-bicol-region-of-philippines-as-]'
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
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: Sentinel-1 radar imagery acquired on 1 November 2020 was analyzed to
    detect surface water extent in the aftermath of typhoon-induced flooding. Floodwater
    depth was estimated by integrating the water extent with digital elevation model
    data using UNOSAT's FwDET algorithm. The resulting depth raster represents observed
    flood conditions at a single point in time without field validation.
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
- href: https://data.humdata.org/dataset/floodwater-depth-in-camarines-sur-provinces-albay-province-bicol-region-of-philippines-as-
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
  description: Floodwater depth in Camarines Sur Provinces & Albay Province, Bicol
    Region of Philippines as of 1 November 2020 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/PH/TC20201101PHL/TC20201101PHL_gdb.zip
  format: Geodatabase
  id: resource_2c358b12
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
  description: Floodwater depth in Camarines Sur Provinces & Albay Province, Bicol
    Region of Philippines as of 1 November 2020 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/PH/TC20201101PHL/TC20201101PHL_SHP.zip
  format: null
  id: resource_93b4fba9
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
slug: rdls_hzd-phl_unosat_floodwaterdepthcamariness_20201104
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
  start: '2020-11-04'
temporal_resolution: null
title: Floodwater depth in Camarines Sur Provinces & Albay Province, Bicol Region
  of Philippines as of 1 November 2020
version: null
vulnerability: null
---
