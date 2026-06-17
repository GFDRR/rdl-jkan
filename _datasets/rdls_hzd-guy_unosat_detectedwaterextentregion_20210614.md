---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-extent-in-region-9-upper-takutu-upper-essequibo-guyana-as-of-12-june-2021
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-region-9-upper-takutu-upper-essequibo-guyana-as-of-12-june-2021
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-region-9-upper-takutu-upper-essequibo-guyana-as-of-12-june-2021
dataset_id: rdls_hzd-guy_unosat_detectedwaterextentregion_20210614
description: 'UNOSAT code: FL20210520GUY This map illustrates satellite-detected surface
  waters along the Rupununi river in Upper Takutu-Upper Essequibo Region of Guyana
  as observed from Sentinel-1 image acquired on 12 June 2021 at 09:45 UTC. Within
  the analyzed area of about 6,500 km2, a total of about 235 km2 of lands were observed
  as flooded and the road about 26 km are potentially affected by the floods. This
  is a preliminary analysis that has not yet been validated in the field. Please send
  ground feedback to UNITAR-UNOSAT. Important note: Flood analysis from radar images
  may underestimate the presence of standing waters in built-up areas and densely
  vegetated areas due to backscattering properties of the radar signal.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-in-region-9-upper-takutu-upper-essequibo-guyana-as-of-12-june-2021]'
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
  description: "Sentinel-1 SAR imagery acquired on 12 June 2021 was analyzed by UNOSAT\
    \ analysts through visual interpretation and multi-temporal comparison to detect\
    \ surface water extent. The resulting flood extent polygons (235 km\xC2\xB2 flooded\
    \ area) and affected infrastructure (26 km of roads) were extracted and provided\
    \ as geodatabase and shapefile formats for the Upper Takutu-Upper Essequibo region."
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/water-extent-in-region-9-upper-takutu-upper-essequibo-guyana-as-of-12-june-2021
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
  description: Satellite detected water extent in Region 9-Upper Takutu-Upper Essequibo,
    Guyana as of 12 June 2021 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/GY/FL20210520GUY/FL20210520GUY_gdb.zip
  format: Geodatabase
  id: resource_c888e19e
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20210520GUY_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent in Region 9-Upper Takutu-Upper Essequibo,
    Guyana as of 12 June 2021 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/GY/FL20210520GUY/FL20210520GUY_SHP.zip
  format: null
  id: resource_066db74f
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20210520GUY_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-guy_unosat_detectedwaterextentregion_20210614
spatial:
  bbox: null
  centroid: null
  countries:
  - GUY
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2021-06-14'
temporal_resolution: null
title: Satellite detected water extent in Region 9-Upper Takutu-Upper Essequibo, Guyana
  as of 12 June 2021
version: null
vulnerability: null
---
