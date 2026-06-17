---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-flood-waters-over-kayin-and-mon-state-myanmar-august-14-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-flood-waters-over-kayin-and-mon-state-myanmar-august-14-2015
dataset_id: rdls_hzd-mmr_unosat_geodatafloodwatersoverkay_20150814
description: 'This map illustrates satellite-detected flood waters in the region of
  Kayin and Mon State in the areas of Papun, Bilin, Hlaingbwe, Thaton, Pa-An, Paung,
  Moulmein, Kyaikmaraw, and Kya In Seikkyi townships of Myanmar as imaged by the Sentinel-1
  satellite on 6 August 2015. Waters along the Salween River have expanded and inundated
  lands on either sides of the river bank. Total surface covered with water in the
  analyzed area has increased from a pre-flood level of 4% to 10% during the flood
  period, and as of 6 August 2015 a total of ~230,000 ha of lands were affected. Most
  of the affected lands north of Letpan town seem to be mainly agricultural fields,
  many of which are of course frequently inundated at other times as well. This is
  a preliminary analysis and has not yet been validated in the field. Please send
  ground feedback to UNITAR-UNOSAT.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-flood-waters-over-kayin-and-mon-state-myanmar-august-14-2015]'
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
license: CC-BY-4.0
lineage:
  description: UNOSAT analysts processed Sentinel-1 satellite imagery acquired on
    6 August 2015, comparing pre-flood and flood-period images to detect notable changes
    in water extent. The analysis identified fluvial flood waters along the Salween
    River in Kayin and Mon State, quantifying the increase in water-covered surface
    area from 4% to 10% and estimating approximately 230,000 hectares of affected
    land. Results were delivered as vector shapefiles with water classification and
    area measurements.
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
- href: https://data.humdata.org/dataset/geodata-of-flood-waters-over-kayin-and-mon-state-myanmar-august-14-2015
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
  description: Geodata of Flood Waters Over Kayin and Mon State, Myanmar (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MM/FL20150703MMR/FL20150703MMR_shp.zip
  format: null
  id: resource_778a8b82
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20150703MMR_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Flood Waters Over Kayin and Mon State, Myanmar (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MM/FL20150703MMR/FL20150703MMR.gdb.zip
  format: null
  id: resource_59d57e7f
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20150703MMR.gdb.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-mmr_unosat_geodatafloodwatersoverkay_20150814
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
  start: '2015-08-14'
temporal_resolution: null
title: Geodata of Flood Waters Over Kayin and Mon State, Myanmar
version: null
vulnerability: null
---
