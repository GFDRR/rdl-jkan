---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-submerged-homesteads-at-tokwe-mukorsi-dam-masvingo-province-zimbab-february-13-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-submerged-homesteads-at-tokwe-mukorsi-dam-masvingo-province-zimbab-february-13-2014
dataset_id: rdls_he-zwe_unosat_geodatasubmergedhomestead_20140213
description: 'This map illustrates water bodies at the Tokwe Mukorsi Dam, Masvingo
  Province, Zimbabwe, as detected by TerraSAR-X on 11 February 2014. The flooded area
  above the dam has greatly increased due to recent heavy rains and currently encompasses
  about 2,300 ha. Using a WorldView-1 image acquired on 2 January 2012, UNOSAT located
  a total of 751 structures in 143 homestead locations that would be submerged by
  the current flood water extent. It is likely that flood waters have been systematically
  underestimated along highly vegetated areas along main river banks because of the
  special characteristics of the satellite data used. This analysis has not yet been
  validated in the field. Please send ground feedback to UNITAR /UNOSAT.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-submerged-homesteads-at-tokwe-mukorsi-dam-masvingo-province-zimbab-february-13-2014]'
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
    description: 751 residential structures located in 143 homestead locations identified
      as submerged by current flood water extent
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
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
license: CC-BY-4.0
lineage:
  description: UNOSAT analysts compared multi-temporal satellite imagery (WorldView-1
    from January 2012 and TerraSAR-X from February 2014) to identify structures at
    risk and map the current flood extent caused by heavy rains at Tokwe Mukorsi Dam.
    Satellite-based change detection and manual feature extraction were used to delineate
    the inundated area and locate residential structures vulnerable to submersion.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/geodata-of-submerged-homesteads-at-tokwe-mukorsi-dam-masvingo-province-zimbab-february-13-2014
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
  description: Geodata of Submerged Homesteads At Tokwe Mukorsi Dam, Masvingo Province,
    Zimbabwe (KML)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/ZW/FL20140207ZWE/TokweMukorsiDam.kmz
  format: null
  id: resource_fef54bcc
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TokweMukorsiDam.kmz
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-zwe_unosat_geodatasubmergedhomestead_20140213
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
  start: '2014-02-13'
temporal_resolution: null
title: Geodata of Submerged Homesteads At Tokwe Mukorsi Dam, Masvingo Province, Zimbabwe
version: null
vulnerability: null
---
