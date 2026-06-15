---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-and-evolution-in-phu-yen-province
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-and-evolution-in-phu-yen-province
dataset_id: rdls_hzd-vnm_unosat_detectedsurfacewatersexte_20161213
description: "This map illustrates the satellite-detected surface waters extent and\
  \ evolution in Phu Yen Province, Vietnam, as observed from the Sentinel-1 images\
  \ acquired on 07 November 2016 and 01 December 2016. Within the analysed zone, representing\
  \ ~85% of the total province area, an increase of surface waters extent was observed\
  \ between the 07 November 2016 and 01 December 2016. ~19,200 ha of surface water\
  \ were observed the 07 November 2016 and reached ~26,400 ha the 01 December 2016.\
  \ All over the analysed area, it corresponds to an evolution of about 37 % : Tuy\
  \ Hoa District (+3,320 ha), D\xF4ng H\xF2a District (+2,000 ha), Phu H\xF2a District\
  \ (+1,460 ha) and Tuy An District (+1,340 ha). This is a preliminary analysis and\
  \ has not yet been validated in the field. Please send ground feedback to UNITAR\
  \ - UNOSAT.. [Source: This metadata record was automatically extracted from the\
  \ Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-and-evolution-in-phu-yen-province]"
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
  description: Sentinel-1 SAR imagery acquired on 07 November 2016 and 01 December
    2016 were analyzed by UNOSAT analysts through visual interpretation and multi-temporal
    comparison to detect and map surface water extent changes across Phu Yen Province.
    Surface water areas were digitized and quantified in hectares to characterize
    flood hazard extent and evolution during the study period.
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
- href: https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-and-evolution-in-phu-yen-province
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
  description: Viet Nam - Satellite Detected Surface Waters Extent and Evolution in
    Phu Yen Province (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/VN/FL20161109VNM/FL20161109VNM.gdb.zip
  format: Geodatabase
  id: resource_cf72ab78
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
    Phu Yen Province (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/VN/FL20161109VNM/FL20161109VNM_SHP.zip
  format: null
  id: resource_8a27eff4
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
slug: rdls_hzd-vnm_unosat_detectedsurfacewatersexte_20161213
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
  start: '2016-12-13'
temporal_resolution: null
title: Viet Nam - Satellite Detected Surface Waters Extent and Evolution in Phu Yen
  Province
version: null
vulnerability: null
---
