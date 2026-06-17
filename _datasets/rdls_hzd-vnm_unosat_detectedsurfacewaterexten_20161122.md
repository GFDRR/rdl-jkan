---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-surface-water-extent-evolution-of-dinh-binh-lake
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-surface-water-extent-evolution-of-dinh-binh-lake
dataset_id: rdls_hzd-vnm_unosat_detectedsurfacewaterexten_20161122
description: 'This map illustrates the satellite-detected surface water evolution
  of Dinh Binh Lake, Vinh Thanh District, Binh Dinh Province, Vietnam, as detected
  by Sentinel-1 images acquired on 26 October 2016 and 07 November 2016. An increase
  of surface water extent was detected in the 07 November 2016 image, particularly
  in the upstream part of the lake : ~500 ha of surface water were observed the 26
  October 2016 and reached ~930 ha the 07 November 2016 corresponding to an evolution
  of about 85%. This is a preliminary analysis and has not yet been validated in the
  field. Please send ground feedback to UNITAR - UNOSAT.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/satellite-detected-surface-water-extent-evolution-of-dinh-binh-lake]'
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
  description: UNOSAT analysts compared Sentinel-1 synthetic aperture radar imagery
    acquired on 26 October 2016 and 07 November 2016 to detect changes in surface
    water extent of Dinh Binh Lake. Surface water area was delineated and quantified
    for both dates, revealing an 85% increase from ~500 ha to ~930 ha, with results
    delivered as geodatabase and shapefile formats. This is a preliminary analysis
    not yet validated in the field.
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
- href: https://data.humdata.org/dataset/satellite-detected-surface-water-extent-evolution-of-dinh-binh-lake
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
  description: Viet Nam - Satellite Detected Surface Water Extent Evolution of Dinh
    Binh Lake (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/VN/FL20161109VNM/FL20161109VNM.gdb.zip
  format: Geodatabase
  id: resource_13b3ad68
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
  description: Viet Nam - Satellite Detected Surface Water Extent Evolution of Dinh
    Binh Lake (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/VN/FL20161109VNM/FL20161109VNM_SHP.zip
  format: null
  id: resource_bb97a0cb
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
slug: rdls_hzd-vnm_unosat_detectedsurfacewaterexten_20161122
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
title: Viet Nam - Satellite Detected Surface Water Extent Evolution of Dinh Binh Lake
version: null
vulnerability: null
---
