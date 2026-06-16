---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-elevation-map-of-kalobeyei-turkana-county-kenya-july-01-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-elevation-map-of-kalobeyei-turkana-county-kenya-july-01-2015
dataset_id: rdls_hzd-ken_unosat_geodataelevationmapkalobe_20150701
description: 'This map illustrates topographic features in the planned Kalobeyei site,
  Turkana County, Kenya using a Digital Elevation Model derived from imagery with
  1m resolution. UNITAR-UNOSAT built water levels scenarios that represents the potentially
  affected areas along the modelled stream network assuming a static raising of waters
  of 1 meter, 2 meters and 3 meters. Streamlines and static water levels has been
  extracted from a Hydrologically Conditioned version of the DEM derived from WorldView-2
  Imagery with 5 m resolution. The model shows spatial distribution of potential water
  levels in the basin based on the elevation extracted from the DEM but does not represent
  a current flood scenario. This is a preliminary analysis & has not yet been validated
  in the field. Please send ground feedback to UNITAR - UNOSAT.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/geodata-of-elevation-map-of-kalobeyei-turkana-county-kenya-july-01-2015]'
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
  - analysis_type: deterministic
    calculation_method: simulated
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
license: CC-BY-4.0
lineage:
  description: A hydrologically conditioned DEM was derived from WorldView-2 satellite
    imagery (5m resolution) of the Kalobeyei site in Turkana County, Kenya. Streamlines
    and static water level surfaces were extracted from this DEM and modeled under
    three deterministic scenarios representing uniform water surface elevation increases
    of 1m, 2m, and 3m above baseline, producing spatial inundation extent maps for
    flood hazard assessment.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/geodata-of-elevation-map-of-kalobeyei-turkana-county-kenya-july-01-2015
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
  description: Geodata of Elevation Map of Kalobeyei, Turkana County, Kenya (Shapefile)
  download_url: https://cern.ch/unosat-maps/SS/CE20131218SSD/Static_Water_Levels_Kalobeyei_Kenya_shp.zip
  format: null
  id: resource_85293729
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Static_Water_Levels_Kalobeyei_Kenya_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Elevation Map of Kalobeyei, Turkana County, Kenya (Shapefile)
  download_url: https://cern.ch/unosat-maps/SS/CE20131218SSD/Static_Water_Levels_Kalobeyei_Kenya_gdb.zip
  format: null
  id: resource_0c4133a8
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Static_Water_Levels_Kalobeyei_Kenya_gdb.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-ken_unosat_geodataelevationmapkalobe_20150701
spatial:
  bbox: null
  centroid: null
  countries:
  - KEN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-07-01'
temporal_resolution: null
title: Geodata of Elevation Map of Kalobeyei, Turkana County, Kenya
version: null
vulnerability: null
---
