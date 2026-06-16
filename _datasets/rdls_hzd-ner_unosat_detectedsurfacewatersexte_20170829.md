---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-and-evolution-in-niamey-niger
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-and-evolution-in-niamey-niger
dataset_id: rdls_hzd-ner_unosat_detectedsurfacewatersexte_20170829
description: 'This map illustrates the satellite-detected surface waters extent and
  evolution over Niamey and surroundings in Niger as observed from the Sentinel-1
  images acquired on 14 and 26 August 2017. Within the analysed area, an increase
  of surface waters extent was observed from the 26 August 2017 image: ~7,870 ha of
  surface water were observed the 14 August 2017 and reached ~10,210 ha the 26 August
  2017. All over the analysed zone, it corresponds to an evolution of about 30%. In
  Niamey an increase of water surface of 320 ha was observed corresponding to an evolution
  of ~20% by comparison to the surface water detected on 14 August 2017. This is a
  preliminary analysis and has not yet been validated in the field. Please send ground
  feedback to UNITAR - UNOSAT.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-and-evolution-in-niamey-niger]'
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
  description: UNOSAT analysts processed Sentinel-1 SAR imagery from 14 and 26 August
    2017 through visual interpretation and multi-temporal comparison to detect and
    quantify surface water extent changes in Niamey. Surface water polygons were delineated
    and area measurements (in hectares and square meters) were calculated to characterize
    the observed flood hazard evolution during the event.
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
- href: https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-and-evolution-in-niamey-niger
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
  description: Satellite Detected Surface Waters Extent and Evolution in Niamey, Niger
    (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/NE/FL20170828NER/FL20170828NER_gdb.zip
  format: Geodatabase
  id: resource_97296d99
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20170828NER_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite Detected Surface Waters Extent and Evolution in Niamey, Niger
    (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/NE/FL20170828NER/FL20170828NER_shp.zip
  format: null
  id: resource_a9d0533d
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20170828NER_shp.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-ner_unosat_detectedsurfacewatersexte_20170829
spatial:
  bbox: null
  centroid: null
  countries:
  - NER
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-08-29'
temporal_resolution: null
title: Satellite Detected Surface Waters Extent and Evolution in Niamey, Niger
version: null
vulnerability: null
---
