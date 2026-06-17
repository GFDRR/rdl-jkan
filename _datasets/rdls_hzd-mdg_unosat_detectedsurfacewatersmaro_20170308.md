---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-surface-waters-in-maroantsetra-area-analanjirofo-region-madagascar
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-surface-waters-in-maroantsetra-area-analanjirofo-region-madagascar
dataset_id: rdls_hzd-mdg_unosat_detectedsurfacewatersmaro_20170308
description: 'This map illustrates satellite-detected flood waters over Maroantsetra
  area, Analanjirofo region in Madagastcar as observed from the TerraSAR-X radar image
  acquired on 08 March 2017 compared with to a Radarsat-2 image acquired on 04 May
  2014. Several zones seem to be inundated and have experienced an increase of standing
  waters. These zones are mainly agricultural and/or swamps around the town of Maroantsetra.
  These waters seem to be the results of the recent heavy rain related also to the
  cyclone ENAWO-17 which made landfall the 07 March 2017. It is likely that flood
  waters have been systematically underestimated along highly vegetated areas along
  main river banks and within built-up urban areas because of the special characteristics
  of the satellite data used. This is a preliminary analysis and has not yet been
  validated in the field. Please send ground feedback to UNITAR UNOSAT.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-surface-waters-in-maroantsetra-area-analanjirofo-region-madagascar]'
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
      process: pluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts compared TerraSAR-X radar imagery acquired on 08 March
    2017 (post-cyclone ENAWO-17) with Radarsat-2 baseline imagery from 04 May 2014
    to detect changes in surface water extent. Standing water zones were identified
    and mapped in agricultural and swamp areas around Maroantsetra, with confidence
    levels and validation flags recorded for each detected water polygon.
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
- href: https://data.humdata.org/dataset/satellite-detected-surface-waters-in-maroantsetra-area-analanjirofo-region-madagascar
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
  description: Satellite Detected Surface Waters in Maroantsetra area, Analanjirofo
    region, Madagascar (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MD/TC20170306MDG/TC20170306MDG_gdb.zip
  format: Geodatabase
  id: resource_a339a04c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20170306MDG_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite Detected Surface Waters in Maroantsetra area, Analanjirofo
    region, Madagascar (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MD/TC20170306MDG/TC20170306MDG_SHP.zip
  format: null
  id: resource_a302ff86
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20170306MDG_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-mdg_unosat_detectedsurfacewatersmaro_20170308
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
  start: '2017-03-08'
temporal_resolution: null
title: Satellite Detected Surface Waters in Maroantsetra area, Analanjirofo region,
  Madagascar
version: null
vulnerability: null
---
