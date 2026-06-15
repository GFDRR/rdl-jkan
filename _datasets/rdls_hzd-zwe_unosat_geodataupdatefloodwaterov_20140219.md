---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-flood-water-over-tokwe-mukorsi-dam-masvingo-province-zimbabwe-february-19-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-flood-water-over-tokwe-mukorsi-dam-masvingo-province-zimbabwe-february-19-2014
dataset_id: rdls_hzd-zwe_unosat_geodataupdatefloodwaterov_20140219
description: 'This map illustrates satellite-detected water bodies at the Tokwe Mukorsi
  Dam, Masvingo Province, Zimbabwe, as imaged by TerraSAR-X on 18 February 2014. The
  flooded area above the dam has decreased slightly since the previous analysis using
  an image from 11 February 2014 and currently encompasses about 2,278 ha. It is likely
  that flood waters have been systematically underestimated along highly vegetated
  areas along main river banks because of the special characteristics of the satellite
  data used. This analysis has not yet been validated in the field. Please send ground
  feedback to UNITAR /UNOSAT.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-flood-water-over-tokwe-mukorsi-dam-masvingo-province-zimbabwe-february-19-2014]'
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
        intensity_measure: AA:km2
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: UNOSAT analysts compared TerraSAR-X satellite imagery acquired on 11
    February 2014 and 18 February 2014 to detect changes in water body extent at Tokwe
    Mukorsi Dam. The flooded area was delineated and quantified as approximately 2,278
    hectares, with acknowledgment that vegetated riparian zones may underestimate
    true flood extent due to radar signal penetration characteristics. Results were
    delivered as vector geometries (KMZ and shapefile formats) with area calculations
    and confidence metadata.
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
- href: https://data.humdata.org/dataset/geodata-of-flood-water-over-tokwe-mukorsi-dam-masvingo-province-zimbabwe-february-19-2014
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
  description: 'Geodata of Update: Flood Water over Tokwe Mukorsi Dam, Masvingo Province,
    Zimbabwe (KML)'
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/ZW/FL20140207ZWE/TokweMukorsiDam.kmz
  format: null
  id: resource_64062315
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TokweMukorsiDam.kmz
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Geodata of Update: Flood Water over Tokwe Mukorsi Dam, Masvingo Province,
    Zimbabwe (Shapefile)'
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/ZW/FL20140207ZWE/FL20140207ZWE_shp.zip
  format: null
  id: resource_4c3af7ff
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20140207ZWE_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Geodata of Update: Flood Water over Tokwe Mukorsi Dam, Masvingo Province,
    Zimbabwe (KML)'
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/ZW/FL20140207ZWE/FL20140207ZWE.gdb.zip
  format: null
  id: resource_fdf6d52e
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20140207ZWE.gdb.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-zwe_unosat_geodataupdatefloodwaterov_20140219
spatial:
  bbox: null
  centroid: null
  countries:
  - ZWE
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2014-02-19'
temporal_resolution: null
title: 'Geodata of Update: Flood Water over Tokwe Mukorsi Dam, Masvingo Province,
  Zimbabwe'
version: null
vulnerability: null
---
