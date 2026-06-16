---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-overview-of-flood-waters-in-wazirabad-area-punjab-province-pakista-september-11-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-overview-of-flood-waters-in-wazirabad-area-punjab-province-pakista-september-11-2014
dataset_id: rdls_hzd-pak_unosat_geodataoverviewfloodwater_20140911
description: 'This map illustrates satellite-detected areas of flood affected land
  as detected by LANDSAT-8 imagery acquired 10 September 2014 in Wazirabad area, Punjab
  Province (Pakistan). The area along Chenab River and agricultural areas northern
  Wazirabad are most likely inundated by floods caused by monsoon rains. It is likely
  that flood waters have been systematically underestimated because of the cloud coverage
  on the image. This analysis has not yet been validated in the field. Please send
  ground feedback to UNITAR /UNOSAT.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-overview-of-flood-waters-in-wazirabad-area-punjab-province-pakista-september-11-2014]'
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
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-4.0
lineage:
  description: UNOSAT analysts interpreted LANDSAT-8 satellite imagery acquired on
    10 September 2014, comparing pre- and post-event images to identify areas of flood
    inundation caused by monsoon rains. Flood extent polygons were manually delineated
    with confidence classifications and area calculations in square meters and hectares.
    Cloud coverage limitations may have resulted in systematic underestimation of
    flood waters.
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
- href: https://data.humdata.org/dataset/geodata-of-overview-of-flood-waters-in-wazirabad-area-punjab-province-pakista-september-11-2014
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
  description: Geodata of Overview of Flood Waters in Wazirabad area, Punjab Province,
    Pakistan (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/PK/FL20140910PAK/FL20140910PAK_shp.zip
  format: null
  id: resource_9ec64e17
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20140910PAK_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Overview of Flood Waters in Wazirabad area, Punjab Province,
    Pakistan (Geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/PK/FL20140910PAK/FL20140910PAK_gdb.zip
  format: Geodatabase
  id: resource_e4338ee5
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20140910PAK_gdb.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-pak_unosat_geodataoverviewfloodwater_20140911
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
  start: '2014-09-11'
temporal_resolution: null
title: Geodata of Overview of Flood Waters in Wazirabad area, Punjab Province, Pakistan
version: null
vulnerability: null
---
