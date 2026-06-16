---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/eaux-de-surface-detectees-par-satellite-a-fada-et-alentours-tchad
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/eaux-de-surface-detectees-par-satellite-a-fada-et-alentours-tchad
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/eaux-de-surface-detectees-par-satellite-a-fada-et-alentours-tchad
dataset_id: rdls_hzd-tcd_unosat_eauxdesurfacedetecteespar_20190828
description: "UNOSAT code: FL20190827TCD Cette carte illustre l'\xE9tendue des eaux\
  \ de surface d\xE9tect\xE9es par satellite (Landsat 8, image comprenant des donn\xE9\
  es du 23 au 27 Ao\xFBt 2019) \xE0 Fada et alentours. Dans la zone analys\xE9e d'environs\
  \ 20,000 ha,quelques centaines de personnes vivent en proximit\xE9 des1,500 ha d'eau\
  \ de surface d\xE9tect\xE9es entre le 23 et le 27 Ao\xFBt2019. Ceci est une analyse\
  \ pr\xE9liminaire qui n'a pas \xE9t\xE9 valid\xE9e sur le terrain. Merci d'envoyer\
  \ vos commentaires \xE0 UNITAR-UNOSAT.. [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/eaux-de-surface-detectees-par-satellite-a-fada-et-alentours-tchad]"
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts processed Landsat 8 satellite imagery from August 23-27,
    2019 covering the Fada region in Chad, applying change detection and visual interpretation
    methods to delineate surface water extent. The resulting vector dataset maps approximately
    1,500 hectares of detected water bodies within a 20,000 hectare study area, representing
    observed flood hazard extent at a single point in time.
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
- href: https://data.humdata.org/dataset/eaux-de-surface-detectees-par-satellite-a-fada-et-alentours-tchad
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
  description: "Eaux de surface d\xE9tect\xE9es par satellite \xE0 Fada et alentours,\
    \ Tchad (Zipped geodatabase)"
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/TD/FL20190827TCD/FL20190827TCD_gdb.zip
  format: Geodatabase
  id: resource_41e42102
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20190827TCD_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Eaux de surface d\xE9tect\xE9es par satellite \xE0 Fada et alentours,\
    \ Tchad (Zipped shapefile)"
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/TD/FL20190827TCD/FL20190827TCD_SHP.zip
  format: null
  id: resource_4dd30c32
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20190827TCD_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-tcd_unosat_eauxdesurfacedetecteespar_20190828
spatial:
  bbox: null
  centroid: null
  countries:
  - TCD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2019-08-28'
temporal_resolution: null
title: "Eaux de surface d\xE9tect\xE9es par satellite \xE0 Fada et alentours, Tchad"
version: null
vulnerability: null
---
