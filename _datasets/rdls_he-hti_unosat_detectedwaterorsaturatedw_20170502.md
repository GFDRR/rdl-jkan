---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-and-or-saturated-wet-soil-extent-in-solon-communal-section-haiti
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-and-or-saturated-wet-soil-extent-in-solon-communal-section-haiti
dataset_id: rdls_he-hti_unosat_detectedwaterorsaturatedw_20170502
description: 'This map illustrates the satellite-detected water and/or saturated wet
  soil extent in Solon Communal Section, St. Louis du Sud Commune in Sud Department
  located in the southwestern part of Haiti. The UNITAR-UNOSAT analysis used a WorldView-2
  satellite image acquired on the 28 April 2017 and could observe areas with standing
  waters and saturated wet soil mainly affecting agricultural fields. The UNITAR-UNOSAT
  analysis identified 118 ha of those areas, which cover 8.50% of this map''s extent
  of 1385 ha of land. This is a preliminary analysis and has not yet been validated
  in the field. Please send ground feedback to UNITAR-UNOSAT.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/satellite-detected-water-and-or-saturated-wet-soil-extent-in-solon-communal-section-haiti]'
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
    description: Agricultural fields affected by standing water and saturated soil
      conditions
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_1
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
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
  description: UNOSAT analysts interpreted WorldView-2 satellite imagery acquired
    on 28 April 2017, comparing spectral signatures to identify standing water and
    saturated wet soil areas. The analysis delineated 118 hectares of affected agricultural
    land (8.50% of the 1385 ha study area) in vector format without field validation.
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
- href: https://data.humdata.org/dataset/satellite-detected-water-and-or-saturated-wet-soil-extent-in-solon-communal-section-haiti
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
  description: Satellite Detected Water and/or Saturated Wet Soil Extent in Solon
    Communal Section, Haiti (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/HT/FL20170424HTI/FL20170424HTI_gdb.zip
  format: Geodatabase
  id: resource_c531fe69
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20170424HTI_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite Detected Water and/or Saturated Wet Soil Extent in Solon
    Communal Section, Haiti (Zipped shapefile.)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/HT/FL20170424HTI/FL20170424HTI_SHP.zip
  format: null
  id: resource_7a459078
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20170424HTI_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-hti_unosat_detectedwaterorsaturatedw_20170502
spatial:
  bbox: null
  centroid: null
  countries:
  - HTI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-05-02'
temporal_resolution: null
title: Satellite Detected Water and/or Saturated Wet Soil Extent in Solon Communal
  Section, Haiti
version: null
vulnerability: null
---
