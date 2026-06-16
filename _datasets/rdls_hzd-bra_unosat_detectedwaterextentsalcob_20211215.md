---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-extents-alcobaca-prado-itamaraju-municipalities-state-of-bahia-brazil
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-alcobaca-prado-itamaraju-municipalities-state-of-bahia-brazil
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-alcobaca-prado-itamaraju-municipalities-state-of-bahia-brazil
dataset_id: rdls_hzd-bra_unosat_detectedwaterextentsalcob_20211215
description: "UNOSAT code: FL20211213BRA This map illustrates satellite-detected surface\
  \ waters in Alcobaca, Prado and Itamaraju municipalities, State of Bahia, Brazil\
  \ as observed from Sentinel-2 image acquired on 11 Dec. 2021 & Sentinel-1 image\
  \ acquired on 09 Dec. 2021. Within the analyzed area of about 300,000 ha, about\
  \ 13,500 ha of lands appear to be flooded. Along the Jucuru\xE7u river, mainly agricultural\
  \ lands appear to be flooded. This is a preliminary analysis and has not yet been\
  \ validated in the field. Please send ground feedback to the United Nations Satellite\
  \ Centre (UNOSAT). Important note: Flood analysis from radar images may underestimate\
  \ the presence of standing waters in built-up areas and densely vegetated areas\
  \ due to backscattering properties of the radar signal.. [Source: This metadata\
  \ record was automatically extracted from the Humanitarian Data Exchange (HDX);\
  \ Original dataset: https://data.humdata.org/dataset/water-extents-alcobaca-prado-itamaraju-municipalities-state-of-bahia-brazil]"
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
license: CC-BY-SA-4.0
lineage:
  description: "UNOSAT analysts compared Sentinel-2 imagery from 11 December 2021\
    \ and Sentinel-1 imagery from 9 December 2021 to detect notable changes in surface\
    \ water extent across approximately 300,000 hectares. The analysis identified\
    \ approximately 13,500 hectares of flooded lands, primarily agricultural areas\
    \ along the Jucuru\xE7u river, using visual interpretation and change detection\
    \ methods. This is a preliminary post-event observation without field validation."
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
- href: https://data.humdata.org/dataset/water-extents-alcobaca-prado-itamaraju-municipalities-state-of-bahia-brazil
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
  description: Satellite detected water extents Alcobaca, Prado & Itamaraju municipalities,
    State of Bahia, Brazil (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/BR/FL20211213BRA/FL20211213BRA_gdb.zip
  format: Geodatabase
  id: resource_810c3b2f
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20211213BRA_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents Alcobaca, Prado & Itamaraju municipalities,
    State of Bahia, Brazil (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/BR/FL20211213BRA/FL20211213BRA_SHP.zip
  format: null
  id: resource_6f9616c9
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20211213BRA_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-bra_unosat_detectedwaterextentsalcob_20211215
spatial:
  bbox: null
  centroid: null
  countries:
  - BRA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2021-12-15'
temporal_resolution: null
title: Satellite detected water extents Alcobaca, Prado & Itamaraju municipalities,
  State of Bahia, Brazil
version: null
vulnerability: null
---
