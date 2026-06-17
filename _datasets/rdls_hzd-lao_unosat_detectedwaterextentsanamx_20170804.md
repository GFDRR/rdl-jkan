---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-in-the-sanamxay-district-attapeu-province-lao-pdr
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-in-the-sanamxay-district-attapeu-province-lao-pdr
dataset_id: rdls_hzd-lao_unosat_detectedwaterextentsanamx_20170804
description: 'This map illustrates the satellite-detected water extent in the District
  of Sanamay, Attapeu Province, in the southwestern part of Lao People''s Democratic
  Republic after the tropical storm SONCA-17. The UNITAR-UNOSAT analysis used a Sentinel-1
  satellite image acquired on the 30 July 2017 and detected several areas with potentially
  standing waters. In the district of Sanamxay ~5,225 ha are likely flooded.This is
  a preliminary analysis and has not yet been validated in the field. Please send
  ground feedback to UNITAR-UNOSAT.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extent-in-the-sanamxay-district-attapeu-province-lao-pdr]'
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
  - analysis_type: probabilistic
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
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts processed Sentinel-1 satellite imagery acquired on
    30 July 2017 following tropical storm SONCA-17, comparing pre- and post-event
    images to detect notable changes in water extent. The analysis identified standing
    water areas across Sanamxay District and quantified the flooded area as approximately
    5,225 hectares, delivered as vector geodatabase and shapefile formats.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/satellite-detected-water-extent-in-the-sanamxay-district-attapeu-province-lao-pdr
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
  description: Satellite Detected Water Extent in the Sanamxay District, Attapeu Province,
    Lao PDR (Zipped geodatabase)
  download_url: https://cern.ch/unosat-maps/LA/TC20170731LAO/TC20170731LAO.gdb.zip
  format: Geodatabase
  id: resource_201e194a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20170731LAO.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite Detected Water Extent in the Sanamxay District, Attapeu Province,
    Lao PDR (Zipped shapefile)
  download_url: https://cern.ch/unosat-maps/LA/TC20170731LAO/TC20170731LAO_shp.zip
  format: null
  id: resource_635a2900
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20170731LAO_shp.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-lao_unosat_detectedwaterextentsanamx_20170804
spatial:
  bbox: null
  centroid: null
  countries:
  - LAO
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-08-04'
temporal_resolution: null
title: Satellite Detected Water Extent in the Sanamxay District, Attapeu Province,
  Lao PDR
version: null
vulnerability: null
---
