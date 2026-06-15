---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-extent-along-the-mazaruni-river-as-of-09-june-2021-region-7-cuyuni-mazaruni-guyana
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-along-the-mazaruni-river-as-of-09-june-2021-region-7-cuyuni-mazaruni-guyana
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-along-the-mazaruni-river-as-of-09-june-2021-region-7-cuyuni-mazaruni-guyana
dataset_id: rdls_hzd-guy_unosat_detectedwaterextentalongm_20210610
description: 'UNOSAT code: FL20210520GUY This map illustrates satellite-detected surface
  waters along the Mazaruni river in Cuyuni-Mazaruni Region of Guyana as observed
  from RCM-2 radar image acquired on 09 June 2021 at 22:17 UTC. Within the analyzed
  area of about 700 km2, a total of about 4 km2 of lands were observed as flooded.
  This is a preliminary analysis that has not yet been validated in the field. Please
  send ground feedback to UNITAR-UNOSAT. Important note: Flood analysis from radar
  images may underestimate the presence of standing waters in built-up areas and densely
  vegetated areas due to backscattering properties of the radar signal.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-along-the-mazaruni-river-as-of-09-june-2021-region-7-cuyuni-mazaruni-guyana]'
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "RCM-2 radar satellite imagery acquired on 09 June 2021 was analyzed\
    \ by UNOSAT analysts through visual interpretation and multi-temporal comparison\
    \ to detect changes in surface water extent. Flooded areas were delineated and\
    \ quantified (4 km\xB2 identified within 700 km\xB2 study area) as a preliminary\
    \ post-event assessment without field validation."
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
- href: https://data.humdata.org/dataset/water-extent-along-the-mazaruni-river-as-of-09-june-2021-region-7-cuyuni-mazaruni-guyana
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
  description: Satellite detected water extent along the Mazaruni river as of 09 June
    2021, Region 7 - Cuyuni-Mazaruni, Guyana (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/GY/FL20210520GUY/FL20210520GUY_gdb.zip
  format: Geodatabase
  id: resource_ff8a5e8f
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
  description: Satellite detected water extent along the Mazaruni river as of 09 June
    2021, Region 7 - Cuyuni-Mazaruni, Guyana (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/GY/FL20210520GUY/FL20210520GUY_SHP.zip
  format: null
  id: resource_6692180b
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
slug: rdls_hzd-guy_unosat_detectedwaterextentalongm_20210610
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
  start: '2021-06-10'
temporal_resolution: null
title: Satellite detected water extent along the Mazaruni river as of 09 June 2021,
  Region 7 - Cuyuni-Mazaruni, Guyana
version: null
vulnerability: null
---
