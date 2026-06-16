---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-overview-of-flood-waters-in-lahore-area-punjab-province-pakistan-july-30-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-overview-of-flood-waters-in-lahore-area-punjab-province-pakistan-july-30-2015
dataset_id: rdls_hzd-pak_unosat_geodataoverviewfloodwater_20150730
description: 'This map illustrates satellite-detected areas of flood as detected by
  Sentinel-1 imagery acquired on 28 July 2015 near Lahore area in Northern Punjab.
  It is likely that flood waters have been systematically underestimated along highly
  vegetated areas along main river banks, and within built-up urban areas because
  of the special characteristics of the satellite data used. This analysis has not
  yet been validated in the field. Please send ground feedback to UNITAR /UNOSAT..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-overview-of-flood-waters-in-lahore-area-punjab-province-pakistan-july-30-2015]'
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
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: UNOSAT analysts processed Sentinel-1 SAR satellite imagery acquired
    on 28 July 2015 by comparing pre- and post-event images to detect and delineate
    flood water extent in the Lahore area. The resulting flood polygon dataset includes
    confidence levels and area measurements but has not been field-validated. Flood
    extent may be underestimated in vegetated riparian zones and urban areas due to
    SAR signal characteristics.
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
- href: https://data.humdata.org/dataset/geodata-of-overview-of-flood-waters-in-lahore-area-punjab-province-pakistan-july-30-2015
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
  description: Geodata of Overview Of Flood Waters In Lahore Area, Punjab Province
    (Pakistan) (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/PK/FL20150723PAK/FL20150723PAK_shp.zip
  format: null
  id: resource_8eb8caa0
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20150723PAK_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Overview Of Flood Waters In Lahore Area, Punjab Province
    (Pakistan) (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/PK/FL20150723PAK/FL20150723PAK.gdb.zip
  format: null
  id: resource_6ec7375a
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20150723PAK.gdb.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-pak_unosat_geodataoverviewfloodwater_20150730
spatial:
  bbox: null
  centroid: null
  countries:
  - PAK
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-07-30'
temporal_resolution: null
title: Geodata of Overview Of Flood Waters In Lahore Area, Punjab Province (Pakistan)
version: null
vulnerability: null
---
