---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-waters-extent-in-vohipeni-manakara-districts-atsinanana-region-madagascar-2756
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-waters-extent-in-vohipeni-manakara-districts-atsinanana-region-madagascar-2756
dataset_id: rdls_hzd-mdg_unosat_detectedwatersextentvohip_20180109
description: 'This map illustrates satellite-detected water extent as of 07 January
  2018 over Vohipeno & Manakara Atsimo districs, Vatovavy Fitovinary Region, in Madagascar
  as detected by Sentinel-1. As of 07 January 2018. Several communes of these districts
  seem to be affected by inundations due to to the heavy rains that have followed
  the cyclone AVA-18. ~1,000 ha of lands appear to be likely affected in Vohitrindry,
  ~ 800 ha in Lanovo and ~400 ha in Vohilany communes. It is likely that flood waters
  have been systematically underestimated along highly vegetated areas along main
  river banks and within built-up urban areas because of the special characteristics
  of the satellite data used. This is a preliminary analysis and has not yet been
  validated in the field. Please send ground feedback to UNITAR UNOSAT.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-waters-extent-in-vohipeni-manakara-districts-atsinanana-region-madagascar-2756]'
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
  description: UNOSAT analysts compared pre- and post-cyclone Sentinel-1 satellite
    imagery to detect water extent changes in Vohipeno and Manakara districts. Visual
    interpretation of satellite imagery identified inundated areas, with area calculations
    (in hectares and square meters) derived from the mapped water polygons. The dataset
    represents observed flood extent as of 7 January 2018 following cyclone Ava-18.
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
- href: https://data.humdata.org/dataset/satellite-detected-waters-extent-in-vohipeni-manakara-districts-atsinanana-region-madagascar-2756
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
  description: Satellite Detected Waters Extent in Vohipeni & Manakara Districts,
    Atsinanana Region, Madagascar (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MD/TC20180103MDG/TC20180103MDG_gdb.zip
  format: Geodatabase
  id: resource_ac0526c6
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20180103MDG_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite Detected Waters Extent in Vohipeni & Manakara Districts,
    Atsinanana Region, Madagascar (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MD/TC20180103MDG/TC20180103MDG_shp.zip
  format: null
  id: resource_342b4ab4
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20180103MDG_shp.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-mdg_unosat_detectedwatersextentvohip_20180109
spatial:
  bbox: null
  centroid: null
  countries:
  - MDG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-01-09'
temporal_resolution: null
title: Satellite Detected Waters Extent in Vohipeni & Manakara Districts, Atsinanana
  Region, Madagascar
version: null
vulnerability: null
---
