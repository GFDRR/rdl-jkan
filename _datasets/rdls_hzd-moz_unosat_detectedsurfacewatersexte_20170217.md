---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-and-evolution-along-save-river-mozambique
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-and-evolution-along-save-river-mozambique
dataset_id: rdls_hzd-moz_unosat_detectedsurfacewatersexte_20170217
description: 'This map illustrates satellite-detected flood waters over Save River
  in Mozambique as observed from the Radarsat-2 images acquired on 17 February 2017
  and 05 February 2017. A decrease of surface waters was observed in the 17 February
  2017 image compared to the 05 February 2017 image along the Save river. It is likely
  that flood waters have been systematically underestimated along highly vegetated
  areas along main river banks and within built-up urban areas because of the special
  characteristics of the satellite data used. This is a preliminary analysis and has
  not yet been validated in the field. Please send ground feedback to UNITAR UNOSAT..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-and-evolution-along-save-river-mozambique]'
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
  description: UNOSAT analysts processed Radarsat-2 SAR imagery acquired on 05 February
    2017 and 17 February 2017 over the Save River in Mozambique, comparing the two
    images to detect changes in surface water extent and map flood water boundaries.
    The resulting geodatabase and shapefile products contain polygon geometries of
    detected water surfaces with area measurements in square meters and hectares.
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
- href: https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-and-evolution-along-save-river-mozambique
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
  description: Mozambique - Satellite Detected Surface Waters Extent and Evolution
    along Save River (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MZ/FL20170118MOZ/FL20170118MOZ.gdb.zip
  format: Geodatabase
  id: resource_7ded7b8d
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20170118MOZ.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Mozambique - Satellite Detected Surface Waters Extent and Evolution
    along Save River (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MZ/FL20170118MOZ/FL20170118MOZ_SHP.zip
  format: null
  id: resource_c5a37c66
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20170118MOZ_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-moz_unosat_detectedsurfacewatersexte_20170217
spatial:
  bbox: null
  centroid: null
  countries:
  - MOZ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-02-17'
temporal_resolution: null
title: Mozambique - Satellite Detected Surface Waters Extent and Evolution along Save
  River
version: null
vulnerability: null
---
