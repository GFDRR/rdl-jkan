---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-overview-of-flood-waters-in-hai-phong-province-vietnam-august-06-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-overview-of-flood-waters-in-hai-phong-province-vietnam-august-06-2015
dataset_id: rdls_hzd-vnm_unosat_geodataoverviewfloodwater_20150806
description: 'This map provides an overview of satellite detected waters in Hai Phong
  Province, northern Vietnam. Due to continuous rainfall, a notable increase in inundated
  areas occurred within this area. Using satellite imagery acquired 02 August 2015
  and 05 October 2009, UNITAR - UNOSAT identified numerous regions with flood affected
  land in the analyzed extent. This is a preliminary analysis and has not yet been
  validated in the field. Please send ground feedback to UNITAR - UNOSAT.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-overview-of-flood-waters-in-hai-phong-province-vietnam-august-06-2015]'
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
license: CC-BY-4.0
lineage:
  description: UNOSAT analysts compared satellite imagery from 02 August 2015 and
    05 October 2009 to identify notable changes in inundated areas across Hai Phong
    Province following continuous rainfall. Flood-affected land polygons were delineated
    and stored as vector shapefiles with area measurements in square meters and hectares.
    This is a preliminary satellite-based hazard assessment not yet validated through
    field surveys.
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
- href: https://data.humdata.org/dataset/geodata-of-overview-of-flood-waters-in-hai-phong-province-vietnam-august-06-2015
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
  description: Geodata of Overview of Flood Waters in Hai Phong Province, Vietnam
    (Shapefile)
  download_url: https://cern.ch/unosat-maps/VN/FL20150730VNM/FL20150730VNM_shp.zip
  format: null
  id: resource_2d6891e2
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20150730VNM_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Overview of Flood Waters in Hai Phong Province, Vietnam
    (Shapefile)
  download_url: https://cern.ch/unosat-maps/VN/FL20150730VNM/FL20150730VNM_gdb.zip
  format: null
  id: resource_da444f82
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20150730VNM_gdb.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-vnm_unosat_geodataoverviewfloodwater_20150806
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
  start: '2015-08-06'
temporal_resolution: null
title: Geodata of Overview of Flood Waters in Hai Phong Province, Vietnam
version: null
vulnerability: null
---
