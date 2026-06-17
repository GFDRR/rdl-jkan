---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-and-evolution-in-thua-thien-hue-province
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-and-evolution-in-thua-thien-hue-province
dataset_id: rdls_hzd-vnm_unosat_detectedsurfacewatersexte_20161221
description: "This map illustrates the satellite-detected surface waters extent and\
  \ evolution in Thua Thien Hue Province, Vietnam, as observed from the Sentinel-1\
  \ images acquired on 06 December 2016 and 18 December 2016. Within the province\
  \ area, an increase of surface waters extent was observed between the 06 and the\
  \ 18 December 2016. ~38,400 ha of surface water were observed the 06 December 2016\
  \ and reached ~50,850 ha the 18 December 2016. All over the province area, it corresponds\
  \ to an evolution of about 32%. This evolution was particularly observed in Phong\
  \ Di\xEAn District (+6,100 ha) and Quang Di\xEAn District (+1,780 ha). This is a\
  \ preliminary analysis and has not yet been validated in the field. Please send\
  \ ground feedback to UNITAR - UNOSAT.. [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-and-evolution-in-thua-thien-hue-province]"
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
  description: UNOSAT analysts processed Sentinel-1 SAR satellite imagery acquired
    on 6 December 2016 and 18 December 2016 over Thua Thien Hue Province, Vietnam,
    comparing multi-temporal images to detect and quantify changes in surface water
    extent. Surface water areas were delineated and measured in hectares, with spatial
    distribution by district, resulting in empirical flood hazard extent data derived
    from observed satellite observations.
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
- href: https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-and-evolution-in-thua-thien-hue-province
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
    Thua Thien Hue Province (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/VN/FL20161109VNM/FL20161109VNM.gdb.zip
  format: Geodatabase
  id: resource_1651c9b2
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
    Thua Thien Hue Province (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/VN/FL20161109VNM/FL20161109VNM_SHP.zip
  format: null
  id: resource_3fece1d2
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
slug: rdls_hzd-vnm_unosat_detectedsurfacewatersexte_20161221
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
  start: '2016-12-21'
temporal_resolution: null
title: Viet Nam - Satellite Detected Surface Waters Extent and Evolution in Thua Thien
  Hue Province
version: null
vulnerability: null
---
