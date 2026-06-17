---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-waters-extent-in-tomasina-districts-atsinanana-region-madagascar-2758
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-waters-extent-in-tomasina-districts-atsinanana-region-madagascar-2758
dataset_id: rdls_hzd-mdg_unosat_detectedwatersextenttomas_20180110
description: 'This map illustrates satellite-detected water extent as of 07 January
  2018 over Toamasina districts, Atsinanana Region, in Madagascar as detected by Sentinel-1.
  Some standing water areas could be observed north and south of Toamasina, mainly
  in the agricultural and/or open areas along the river. It is likely that floodwaters
  have been systematically underestimated along highly vegetated areas along main
  river banks and within built-up urban areas because of the special characteristics
  of the satellite data used. This is a preliminary analysis and has not yet been
  validated in the field. Please send ground feedback to UNITAR UNOSAT.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-waters-extent-in-tomasina-districts-atsinanana-region-madagascar-2758]'
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
  description: UNOSAT analysts interpreted Sentinel-1 synthetic aperture radar imagery
    acquired on 7 January 2018, comparing pre- and post-event images to detect changes
    in water extent across Toamasina districts. Water bodies were manually delineated
    and classified by confidence level, with areas of standing water identified in
    agricultural zones and along river banks. The dataset represents observed flood
    extent at a single point in time following a cyclone event.
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
- href: https://data.humdata.org/dataset/satellite-detected-waters-extent-in-tomasina-districts-atsinanana-region-madagascar-2758
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
  description: Satellite Detected Waters Extent in Tomasina Districts, Atsinanana
    Region, Madagascar (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MD/TC20180103MDG/TC20180103MDG_gdb.zip
  format: Geodatabase
  id: resource_596586de
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
  description: Satellite Detected Waters Extent in Tomasina Districts, Atsinanana
    Region, Madagascar (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MD/TC20180103MDG/TC20180103MDG_shp.zip
  format: null
  id: resource_38097d29
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
slug: rdls_hzd-mdg_unosat_detectedwatersextenttomas_20180110
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
  start: '2018-01-10'
temporal_resolution: null
title: Satellite Detected Waters Extent in Tomasina Districts, Atsinanana Region,
  Madagascar
version: null
vulnerability: null
---
