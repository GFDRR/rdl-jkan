---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-and-evolution-over-eastern-part-of-bangladesh
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-and-evolution-over-eastern-part-of-bangladesh
dataset_id: rdls_hzd-bgd_unosat_detectedwaterextentevolut_20160728
description: 'This map illustrates satellite-detected water extent and evolution in
  the eastern part of Bangladesh as imaged by the SENTINEL-1 satellite on 30 June
  2016 and 24 July 2016. The analysis shows an expansion of waters of 75% between
  the two dates within the entire analyzed zone. Heavy rains at the onset of the Monsoon
  season have caused flooding. This is a preliminary analysis and has not yet been
  validated in the field. Please send ground feedback to UNITAR-UNOSAT.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extent-and-evolution-over-eastern-part-of-bangladesh]'
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
  description: UNOSAT analysts processed Sentinel-1 SAR satellite imagery acquired
    on 30 June 2016 and 24 July 2016 over eastern Bangladesh, comparing multi-temporal
    images to detect and delineate water extent changes during monsoon-triggered flooding.
    Water bodies were digitized as polygon geometries with area calculations in hectares
    and square meters, representing observed inundation extent evolution with 75%
    expansion documented between the two acquisition dates.
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
- href: https://data.humdata.org/dataset/satellite-detected-water-extent-and-evolution-over-eastern-part-of-bangladesh
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
  description: Satellite Detected Water Extent and Evolution Over Eastern part of
    Bangladesh (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/BD/FL20160725BGD/FL20160725BGD.gdb.zip
  format: Geodatabase
  id: resource_ace8c1b7
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20160725BGD.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite Detected Water Extent and Evolution Over Eastern part of
    Bangladesh (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/BD/FL20160725BGD/FL20160725BGD_shp.zip
  format: null
  id: resource_5f653541
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20160725BGD_shp.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-bgd_unosat_detectedwaterextentevolut_20160728
spatial:
  bbox: null
  centroid: null
  countries:
  - BGD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-07-28'
temporal_resolution: null
title: Satellite Detected Water Extent and Evolution Over Eastern part of Bangladesh
version: null
vulnerability: null
---
