---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-inundation-near-sar-e-pol-sar-e-pol-province-afghanistan-may-07-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-inundation-near-sar-e-pol-sar-e-pol-province-afghanistan-may-07-2014
dataset_id: rdls_hzd-afg_unosat_geodatainundationnearsare_20140507
description: 'This map illustrates potential satellite-detected inundated areas and
  water south of Sar-E Pol city, Afghanistan. UNOSAT analyzed imagery from the KOMPSAT2
  satellite collected 05 May 2014 in response to heavy rainfall occurring on 23-24
  April 2014. UNOSAT extracted areas of water and inundated soils to indicate likely
  flood affected lands. This map includes both permanent water bodies, such as streams,
  and potential flood waters together due to limitations in source data. It is likely
  that flood waters and inundation have been systematically underestimated along highly
  vegetated areas and within built-up urban areas because of the special characteristics
  of the satellite data used. This analysis has not yet been validated in the field.
  Please send ground feedback to UNITAR /UNOSAT.. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/geodata-of-inundation-near-sar-e-pol-sar-e-pol-province-afghanistan-may-07-2014]'
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: UNOSAT analysts processed KOMPSAT2 satellite imagery acquired on 05
    May 2014 and compared it with reference imagery to identify notable changes in
    water extent and inundated soils. Water and inundation areas were manually extracted
    and vectorized to create a geodataset representing observed flood-affected lands
    in response to heavy rainfall occurring 23-24 April 2014.
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
- href: https://data.humdata.org/dataset/geodata-of-inundation-near-sar-e-pol-sar-e-pol-province-afghanistan-may-07-2014
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
  description: Geodata of Inundation Near Sar-E Pol, Sar-E Pol Province, Afghanistan
    (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/AF/FL20140430AFG/FL20140430AFG_shp.zip
  format: null
  id: resource_65e0ef21
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20140430AFG_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Inundation Near Sar-E Pol, Sar-E Pol Province, Afghanistan
    (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/AF/FL20140430AFG/FL20140430AFG.gdb.zip
  format: null
  id: resource_81d77ef4
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20140430AFG.gdb.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-afg_unosat_geodatainundationnearsare_20140507
spatial:
  bbox: null
  centroid: null
  countries:
  - AFG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2014-05-07'
temporal_resolution: null
title: Geodata of Inundation Near Sar-E Pol, Sar-E Pol Province, Afghanistan
version: null
vulnerability: null
---
