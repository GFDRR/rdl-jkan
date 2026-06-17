---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-surface-waters-in-d-joumane-bongor-areas-chad-2706
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-surface-waters-in-d-joumane-bongor-areas-chad-2706
dataset_id: rdls_hzd-cmrtcd_unosat_detectedsurfacewatersdjou_20171010
description: 'This map illustrates the satellite-detected surface water extent over
  D''joumane/Bongor and surroundings in Chad along the Logone River as observed from
  the Radarsat-2 SAR image acquired on 5 October 2017. The analysis of the image indicate
  that localized standing flood water with very little impact on population and agriculture
  area. Within the analyzed area (11,680 km2), 15,331 ha of surface water extent was
  observed of which 6667 ha in Chad and 8664 ha in Cameroon. This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to UNITAR - UNOSAT.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-surface-waters-in-d-joumane-bongor-areas-chad-2706]'
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
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: "Radarsat-2 SAR satellite image acquired on 5 October 2017 was analyzed\
    \ by UNOSAT through visual interpretation and comparison with reference imagery\
    \ to detect and delineate surface water extent. The resulting vector geodatabase\
    \ and shapefile contain mapped flood water polygons with area measurements in\
    \ hectares across the 11,680 km\xC2\xB2 study area covering D'joumane/Bongor and\
    \ surrounding regions along the Logone River."
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
- href: https://data.humdata.org/dataset/satellite-detected-surface-waters-in-d-joumane-bongor-areas-chad-2706
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
  description: Satellite Detected Surface Waters in D'joumane/Bongor areas, Chad (Zipped
    geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/TD/FL20170926TCD/FL20170926TCD_gdb.zip
  format: Geodatabase
  id: resource_d24e7356
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20170926TCD_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite Detected Surface Waters in D'joumane/Bongor areas, Chad (Zipped
    shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/TD/FL20170926TCD/FL20170926TCD_shp.zip
  format: null
  id: resource_6b4652f5
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20170926TCD_shp.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-cmrtcd_unosat_detectedsurfacewatersdjou_20171010
spatial:
  bbox: null
  centroid: null
  countries:
  - TCD
  - CMR
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-10-10'
temporal_resolution: null
title: Satellite Detected Surface Waters in D'joumane/Bongor areas, Chad
version: null
vulnerability: null
---
