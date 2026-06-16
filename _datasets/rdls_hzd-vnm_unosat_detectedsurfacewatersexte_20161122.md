---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-and-evolution-in-ha-tinh-province
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-and-evolution-in-ha-tinh-province
dataset_id: rdls_hzd-vnm_unosat_detectedsurfacewatersexte_20161122
description: 'This map illustrates the satellite-detected surface waters extent and
  evolution in Ha Tinh Province, Vietnam, as observed from the Sentinel-1 images acquired
  on 12 and 24 October 2016. An increase of surface waters extent was observed from
  the 24 October 2016 image: ~26,400 ha of surface water were observed the 12 October
  2016 and reached ~30,700 ha the 24 October 2016. All over the analysed zone, it
  corresponds to an evolution of about 16%. More specifically, in Tri River (Song
  Tri) lake and dam an increase of 177 ha was observed. For Ke Go Lake and dam, an
  evolution of 30% of the total surface water was observed in between the 12 October
  and the 24 October 2016. This is a preliminary analysis and has not yet been validated
  in the field. Please send ground feedback to UNITAR - UNOSAT.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-and-evolution-in-ha-tinh-province]'
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
  description: UNOSAT analysts processed Sentinel-1 SAR imagery acquired on 12 and
    24 October 2016 over Ha Tinh Province, Vietnam, performing change detection analysis
    to quantify surface water extent evolution. Surface water areas were delineated
    and measured in hectares, with temporal comparison revealing a 16% increase in
    total surface water coverage and specific changes in major water bodies including
    Tri River and Ke Go Lake.
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
- href: https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-and-evolution-in-ha-tinh-province
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
  description: Viet Nam - Satellite Detected Surface Waters Extent and Evolution in
    Ha Tinh Province (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/VN/FL20161109VNM/FL20161109VNM.gdb.zip
  format: Geodatabase
  id: resource_431d0681
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20161109VNM.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Viet Nam - Satellite Detected Surface Waters Extent and Evolution in
    Ha Tinh Province (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/VN/FL20161109VNM/FL20161109VNM_SHP.zip
  format: null
  id: resource_65367246
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20161109VNM_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-vnm_unosat_detectedsurfacewatersexte_20161122
spatial:
  bbox: null
  centroid: null
  countries:
  - VNM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-11-22'
temporal_resolution: null
title: Viet Nam - Satellite Detected Surface Waters Extent and Evolution in Ha Tinh
  Province
version: null
vulnerability: null
---
