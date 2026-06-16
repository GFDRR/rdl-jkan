---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-flood-waters-over-khartoum-state-sudan-august-08-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-flood-waters-over-khartoum-state-sudan-august-08-2014
dataset_id: rdls_hzd-sdn_unosat_geodatafloodwatersoverkha_20140808
description: 'This map illustrates satellite-detected areas of flood affected land
  as detected by RADARSAT-2 imagery acquired 08 August 2014 in Khartoum State, Sudan.
  The area surrounding Khartoum City and Umdurman was inundated by floods caused by
  heavy rains. Areas to the South of Umdurman seem to have been flooded and many other
  areas including Umdaba and East Nile seem to suffer from waters and/or muds. It
  is likely that flood waters have been systematically underestimated along highly
  vegetated areas along main river banks, and within built-up urban areas because
  of the characteristics of the satellite data used. This analysis has not yet been
  validated in the field. Please send ground feedback to UNITAR /UNOSAT.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-flood-waters-over-khartoum-state-sudan-august-08-2014]'
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
  description: UNOSAT analysts processed RADARSAT-2 satellite imagery from 8 August
    2014 by comparing pre- and post-flood images to identify notable changes in surface
    water extent. Flood-affected areas were manually delineated and vectorized as
    polygons with area measurements in square meters and hectares, representing observed
    inundation extent during the August 2014 flooding event in Khartoum State.
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
- href: https://data.humdata.org/dataset/geodata-of-flood-waters-over-khartoum-state-sudan-august-08-2014
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
  description: Geodata of Flood Waters Over Khartoum State, Sudan (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SD/FL20140803SDN/FL20140803SDN.shp.zip
  format: null
  id: resource_11ac3c00
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20140803SDN.shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Flood Waters Over Khartoum State, Sudan (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SD/FL20140803SDN/FL20140803SDN.gdb.zip
  format: null
  id: resource_5be3442b
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20140803SDN.gdb.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-sdn_unosat_geodatafloodwatersoverkha_20140808
spatial:
  bbox: null
  centroid: null
  countries:
  - SDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2014-08-08'
temporal_resolution: null
title: Geodata of Flood Waters Over Khartoum State, Sudan
version: null
vulnerability: null
---
