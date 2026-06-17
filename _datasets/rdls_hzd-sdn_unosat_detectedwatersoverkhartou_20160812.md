---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-waters-over-khartoum-area-khartoum-state-sudan
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-waters-over-khartoum-area-khartoum-state-sudan
dataset_id: rdls_hzd-sdn_unosat_detectedwatersoverkhartou_20160812
description: 'This map illustrates satellite-detected waters around the Khartoum City
  in Sudan as detected in satellite imagery acquired by the TerraSAR-X satellite on
  11 August 2016 in Khartoum State. UNOSAT analysis shows an expansion of water of~
  90Km2 (over the analysed area) particularly located in the left bank of White Nile
  without causing floods inside build up areas. The exact limit of flood waters is
  uncertain because of the low spatial resolution of the satellite data used for this
  analysis. Detected water bodies likely reflect an underestimation of all flood-affected
  areas within the map extent. This analysis has not yet been validated in the field.
  Please send ground feedback to UNITAR - UNOSAT.. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/satellite-detected-waters-over-khartoum-area-khartoum-state-sudan]'
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
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: "TerraSAR-X satellite imagery acquired on 11 August 2016 was analyzed\
    \ by UNOSAT through visual comparison with reference imagery to detect and delineate\
    \ water body extent. Analysts identified notable changes in water coverage, particularly\
    \ along the left bank of the White Nile, and quantified the expanded water area\
    \ at approximately 90 km\xC2\xB2 across the analyzed region."
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
- href: https://data.humdata.org/dataset/satellite-detected-waters-over-khartoum-area-khartoum-state-sudan
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
  description: Satellite Detected Waters Over Khartoum Area, Khartoum State, Sudan
    (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SD/FL20160808SDN/FL20160808SDN.gdb.zip
  format: Geodatabase
  id: resource_1c319142
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20160808SDN.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite Detected Waters Over Khartoum Area, Khartoum State, Sudan
    (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SD/FL20160808SDN/FL20160808SDN_shp.zip
  format: null
  id: resource_4faf83c0
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20160808SDN_shp.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-sdn_unosat_detectedwatersoverkhartou_20160812
spatial:
  bbox: null
  centroid: null
  countries:
  - SDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-08-12'
temporal_resolution: null
title: Satellite Detected Waters Over Khartoum Area, Khartoum State, Sudan
version: null
vulnerability: null
---
