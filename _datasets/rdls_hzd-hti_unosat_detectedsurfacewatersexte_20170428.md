---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-in-les-cayes-and-cavaillon-communes-sud-department-haiti
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-in-les-cayes-and-cavaillon-communes-sud-department-haiti
dataset_id: rdls_hzd-hti_unosat_detectedsurfacewatersexte_20170428
description: 'This map illustrates the satellite-detected water extent in Les Cayes
  and Cavaillon communes in Sud Department (Haiti) located in the southwestern part
  of Haiti. The UNITAR-UNOSAT analysis used a Sentinel-1 satellite image acquired
  on the 26 April 2017 and a Radarsat-2 image acquired on the 17 May 2016 and could
  observe areas with standing waters mainly affecting agricultural fields. The UNITAR-UNOSAT
  analysis identified 718 ha of flooded areas, which cover ~4% of this map''s extent
  of ~20300 ha of land. The increase of waters within the analyzed zone is about 460%.
  ~155 ha of surface waters were observed the 17 May 2016 and reached ~873 ha the
  26 April 2017. About 9km of roads, mainly local roads are potentially affected.
  It is likely that flood waters have been systematically underestimated along highly
  vegetated areas along main river banks and within built-up urban areas because of
  the special characteristics of the satellite data used. This is a preliminary analysis
  and has not yet been validated in the field. Please send ground feedback to UNITAR-UNOSAT..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-in-les-cayes-and-cavaillon-communes-sud-department-haiti]'
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
        intensity_measure: wd:m
        process: pluvial_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts compared multi-temporal satellite imagery (Sentinel-1
    and Radarsat-2) to detect changes in surface water extent and identify flooded
    agricultural areas. The analysis identified 718 ha of standing water representing
    a 460% increase in water coverage within the study zone, with results delivered
    as vector geodatabase and shapefile formats.
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
- href: https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-in-les-cayes-and-cavaillon-communes-sud-department-haiti
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
  description: Haiti - Satellite Detected Surface Waters Extent in Les Cayes and Cavaillon
    Communes, Sud Department (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/HT/FL20170424HTI/FL20170424HTI_gdb.zip
  format: Geodatabase
  id: resource_4103dd5e
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20170424HTI_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Haiti - Satellite Detected Surface Waters Extent in Les Cayes and Cavaillon
    Communes, Sud Department (Zipped shapefile.)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/HT/FL20170424HTI/FL20170424HTI_SHP.zip
  format: null
  id: resource_5a9a2c4f
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20170424HTI_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-hti_unosat_detectedsurfacewatersexte_20170428
spatial:
  bbox: null
  centroid: null
  countries:
  - HTI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-04-28'
temporal_resolution: null
title: Haiti - Satellite Detected Surface Waters Extent in Les Cayes and Cavaillon
  Communes, Sud Department
version: null
vulnerability: null
---
