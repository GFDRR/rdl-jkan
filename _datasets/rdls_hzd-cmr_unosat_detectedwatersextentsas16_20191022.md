---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/waters-extents-as-of-16-october-2019-over-mayodanay-and-logone-et-chari-department-far-nor
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/waters-extents-as-of-16-october-2019-over-mayodanay-and-logone-et-chari-department-far-nor
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/waters-extents-as-of-16-october-2019-over-mayodanay-and-logone-et-chari-department-far-nor
dataset_id: rdls_hzd-cmr_unosat_detectedwatersextentsas16_20191022
description: 'UNOSAT code: FL20191017CMR This map illustrates satellite-detected surface
  water in Mayo-Danay and Logone-et-Chari Department, Far-North Region of Cameroon
  as observed from Sentinel-2 imagery acquired on 16 October 2019. Within the analysed
  extent of about 2,500 km2, a total about 211 km2 of land appear to be flooded. This
  is a preliminary analysis and has not yet been validated in the field. Please send
  ground feedback to UNITAR - UNOSAT.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/waters-extents-as-of-16-october-2019-over-mayodanay-and-logone-et-chari-department-far-nor]'
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
license: CC-BY-SA-4.0
lineage:
  description: Sentinel-2 satellite imagery acquired on 16 October 2019 was analyzed
    by UNOSAT through visual interpretation and comparison with reference imagery
    to detect and delineate surface water extent. The resulting water polygon features
    were quantified by area (211 km2 flooded within 2,500 km2 study area) and provided
    as geodatabase and shapefile formats for the Far-North Region of Cameroon.
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
- href: https://data.humdata.org/dataset/waters-extents-as-of-16-october-2019-over-mayodanay-and-logone-et-chari-department-far-nor
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
  description: Cameroon - Satellite detected waters extents, as of 16 October 2019
    over MayoDanay and Logone-et-Chari Department, Far-North Region (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/CM/FL20191017CMR/FL20191017CMR_gdb.zip
  format: Geodatabase
  id: resource_6aa6d033
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20191017CMR_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Cameroon - Satellite detected waters extents, as of 16 October 2019
    over MayoDanay and Logone-et-Chari Department, Far-North Region (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/CM/FL20191017CMR/FL20191017CMR_SHP.zip
  format: null
  id: resource_c35b36ba
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20191017CMR_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-cmr_unosat_detectedwatersextentsas16_20191022
spatial:
  bbox: null
  centroid: null
  countries:
  - CMR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2019-10-22'
temporal_resolution: null
title: Cameroon - Satellite detected waters extents, as of 16 October 2019 over MayoDanay
  and Logone-et-Chari Department, Far-North Region
version: null
vulnerability: null
---
