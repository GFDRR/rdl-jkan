---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-waters-in-elegu-town-amuru-district-uganda
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-waters-in-elegu-town-amuru-district-uganda
dataset_id: rdls_hzd-uga_unosat_detectedwaterselegutownam_20170831
description: 'This map illustrates satellite-detected surface water extent in Elegu
  town and surroundings using a Sentinel-1 satellite image acquired on the 23 August
  2017. Within the map extent, surface waters extended of about 12% more particularly
  south and north-west of Elugu where evidences of floods could be observed. It is
  likely that flood waters have been systematically underestimated along highly vegetated
  areas along main river banks, and within built-up urban areas because of the characteristics
  of the satellite data used. This is a preliminary analysis and has not yet been
  validated in the field. Please send ground feedback to UNITAR-UNOSAT.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-waters-in-elegu-town-amuru-district-uganda]'
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
  description: Sentinel-1 satellite image acquired on 23 August 2017 was analyzed
    by UNOSAT analysts through visual interpretation and multi-temporal comparison
    to detect surface water extent and identify flood inundation areas. The analysis
    produced vector geometries of water bodies with area measurements, representing
    observed flood hazard extent at a single point in time.
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
- href: https://data.humdata.org/dataset/satellite-detected-waters-in-elegu-town-amuru-district-uganda
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
  description: Satellite Detected Waters in Elegu Town, Amuru District, Uganda (Zipped
    geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/UG/FL20170831UGA/FL20170831UGA_gdb.zip
  format: Geodatabase
  id: resource_8efe3a9b
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20170831UGA_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite Detected Waters in Elegu Town, Amuru District, Uganda (Zipped
    shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/UG/FL20170831UGA/FL20170831UGA_shp.zip
  format: null
  id: resource_31593ab2
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20170831UGA_shp.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-uga_unosat_detectedwaterselegutownam_20170831
spatial:
  bbox: null
  centroid: null
  countries:
  - UGA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-08-31'
temporal_resolution: null
title: Satellite Detected Waters in Elegu Town, Amuru District, Uganda
version: null
vulnerability: null
---
