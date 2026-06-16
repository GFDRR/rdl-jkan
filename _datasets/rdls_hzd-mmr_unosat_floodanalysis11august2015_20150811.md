---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/fl20150703mmr-flood-vectors-sentinel1-11-august-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/fl20150703mmr-flood-vectors-sentinel1-11-august-2015
dataset_id: rdls_hzd-mmr_unosat_floodanalysis11august2015_20150811
description: 'This is ''Flood vectors - Sentinel-1 (11 August 2015)'' of the Flood
  analysis for Myanmar which began on 03 July 2015. It includes 54,800 satellite detected
  water bodies with a spatial extent of 2,939.48 square kilometers derived from the
  Sentinel-1 image a.... [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/fl20150703mmr-flood-vectors-sentinel1-11-august-2015]'
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: UNOSAT analysts interpreted Sentinel-1 synthetic aperture radar imagery
    acquired on 11 August 2015, comparing multiple images to detect notable changes
    in water body extent. Satellite-detected water bodies were vectorized and mapped
    to produce observed flood extent data for the Myanmar 2015 flood event.
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
- href: https://data.humdata.org/dataset/fl20150703mmr-flood-vectors-sentinel1-11-august-2015
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
- access_url: https://unosatgis.cern.ch/arcgis/rest/services/FP02/FP02_FL_20150703_MMR_20150811_Flood_Sentinel1/MapServer/kml/mapImage.kmz
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flood analysis for Myanmar (11 August 2015) (KMZ)
  download_url: null
  format: null
  id: resource_058a7d24
  media_type: application/vnd.google-earth.kmz
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mapImage.kmz
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flood analysis for Myanmar (11 August 2015) (Geodatabase)
  download_url: https://floods.unosat.org/geoportal/FP02/FL20150703MMR_gdb.zip
  format: Geodatabase
  id: resource_1dccc045
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20150703MMR_gdb.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-mmr_unosat_floodanalysis11august2015_20150811
spatial:
  bbox: null
  centroid: null
  countries:
  - MMR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-08-11'
temporal_resolution: null
title: Flood analysis for Myanmar (11 August 2015)
version: null
vulnerability: null
---
