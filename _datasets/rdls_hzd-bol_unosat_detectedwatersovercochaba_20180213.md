---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/satellite-detected-waters-over-cochabamba-department-bolivia
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-waters-over-cochabamba-department-bolivia
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-waters-over-cochabamba-department-bolivia
dataset_id: rdls_hzd-bol_unosat_detectedwatersovercochaba_20180213
description: 'This map illustrates satellite-detected standing water over the Cochabamba
  department in Bolivia, as of the 10 February 2018, following the heavy rainfalls
  that caused severe flooding in the area. The analysis was conducted using Sentinel
  -1b and Radarsat-2 images as of 9, 10 and 12 February 2018 respectively. UNITAR-UNOSAT
  identified in the analyzed area of the Cochabamba Department, around 1,300 Ha of
  land seem to be inundated, which almost 35% ,450 Ha, are in the province of Punata.
  It is likely that flood waters have been systematically underestimated within built-up
  urban areas because of the special characteristics of the satellite data used. This
  is a preliminary analysis and has not yet been validated in the field. Please send
  ground feedback to UNITAR UNOSAT.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-waters-over-cochabamba-department-bolivia]'
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
      process: pluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-4.0
lineage:
  description: UNOSAT analysts processed Sentinel-1b and Radarsat-2 synthetic aperture
    radar imagery acquired on 9, 10, and 12 February 2018 to detect standing water
    extent in Cochabamba Department following heavy rainfall events. Multi-temporal
    image comparison identified approximately 1,300 hectares of inundated land, with
    results vectorized as polygon features with area measurements in square meters
    and hectares.
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
- href: https://data.humdata.org/dataset/satellite-detected-waters-over-cochabamba-department-bolivia
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
  description: Satellite detected waters over Cochabamba department, Bolivia (zipped
    shapefile)
  download_url: https://cern.ch/unosat-maps/BO/FL20180209BOL/FL20180209BOL_shp.zip
  format: null
  id: resource_98bed7a2
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20180209BOL_shp.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-bol_unosat_detectedwatersovercochaba_20180213
spatial:
  bbox: null
  centroid: null
  countries:
  - BOL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-02-13'
temporal_resolution: null
title: Satellite detected waters over Cochabamba department, Bolivia
version: null
vulnerability: null
---
