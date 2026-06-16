---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-extents-as-of-30-october-2019-over-beled-weyne-district-hiraan-region-in-somalia
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-as-of-30-october-2019-over-beled-weyne-district-hiraan-region-in-somalia
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-as-of-30-october-2019-over-beled-weyne-district-hiraan-region-in-somalia
dataset_id: rdls_hzd-som_unosat_detectedwaterextentsas30o_20191031
description: 'UNOSAT code: FL20191030SOM This map illustrates satellite-detected surface
  water in Beled Weyne District, Hiraan Region in Somalia analyzed with Sentinel-1
  imagery acquired on 30 October 2019. Within the analysed extent of about 2,500 km2,
  a total of about 155 km2 of land appear to be flooded. This is a preliminary analysis
  and has not yet been validated in the field. Please send ground feedback to UNITAR
  - UNOSAT. Important note: Flood analysis based on Sentinel-1 imagery may significantly
  underestimate the presence of standing floodwater in dense built-up areas due to
  backscattering of the radar signal.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extents-as-of-30-october-2019-over-beled-weyne-district-hiraan-region-in-somalia]'
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
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts processed Sentinel-1 synthetic aperture radar imagery
    acquired on 30 October 2019 over Beled Weyne District, comparing satellite images
    to detect notable changes in surface water extent. The analysis identified approximately
    155 km2 of flooded area within a 2,500 km2 study extent, with results delivered
    as vector geodatabase and shapefile formats containing area measurements in hectares
    and square meters.
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
- href: https://data.humdata.org/dataset/water-extents-as-of-30-october-2019-over-beled-weyne-district-hiraan-region-in-somalia
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
  description: Satellite-detected water extents as of 30 October 2019, over Beled
    Weyne District, Hiraan Region in Somalia (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SO/FL20191030SOM/FL20191030SOM_gdb.zip
  format: Geodatabase
  id: resource_6f718ce3
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20191030SOM_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite-detected water extents as of 30 October 2019, over Beled
    Weyne District, Hiraan Region in Somalia (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SO/FL20191030SOM/FL20191030SOM_SHP.zip
  format: null
  id: resource_09d6a636
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20191030SOM_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-som_unosat_detectedwaterextentsas30o_20191031
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
  start: '2019-10-31'
temporal_resolution: null
title: Satellite-detected water extents as of 30 October 2019, over Beled Weyne District,
  Hiraan Region in Somalia
version: null
vulnerability: null
---
